# Perspective File Upload Component

## Description

This guide describes the configuration and scripting of the Perspective File Upload component, used to transfer files from a user's machine to the Ignition Gateway. It details how to script the `onFileReceived` event to process and store the uploaded file data, enabling workflows such as saving files to a database or filesystem for subsequent retrieval.

## Documentation

# Instructions
# Perspective File Upload Component

The Perspective File Upload component provides a user interface for uploading files from a local machine to the Ignition Gateway during a Perspective session. The real power of this component is unlocked through scripting, primarily on the `onFileReceived` event, which dictates what happens with the uploaded file data.

### Core Functionality

The component acts as a user-facing control that allows them to select one or more files from their computer or drag and drop them onto the component. Once a file is selected, it is sent to the Gateway. A script action configured on the `onFileReceived` event must then handle this file data, for example, by saving it to a database, writing it to a file server, or processing its contents. The component itself does not store the file permanently; it only facilitates the transfer to the Gateway.

---

### Properties

| Property             | Type                               | Description                                                                                                                                                                                                                                                            |
| -------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`fileUploadIcon`** | Object                             | An object that configures the icon displayed when the component is rendered at a small width. It contains `path` (string, e.g., "material/cloud_upload") and `color` properties.                                                                                         |
| **`supportedFileTypes`** | Array of Strings                   | A list of file extensions that the user is allowed to upload (e.g., `["pdf", "txt", "jpg"]`). If the array is empty, all file types are permitted.                                                                                                                         |
| **`maxUploads`**     | Number (Integer)                   | The maximum number of files that can be uploaded simultaneously. The default value is **5**.                                                                                                                                                                               |
| **`fileSizeLimit`**  | Number (Integer)                   | The maximum size for each individual file, specified in megabytes (MB). The default limit is **10 MB**.                                                                                                                                                                  |
| **`style`**          | Object                             | Standard Perspective style object for customizing the component's appearance, including text, background, margins, borders, and more.                                                                                                                                      |

---

### Event Handling

Component events are configured by right-clicking the component and selecting "Configure Events". The primary logic for the File Upload component resides in these event scripts.

#### `onFileReceived`

This is the most critical event for this component. It fires on the Gateway each time a file has been successfully uploaded from the client. Within a script action on this event, a special `event` object is available, providing access to the file's details and data.

**`event.file` Object Properties and Methods:**

*   **`event.file.name`** (String): The name of the uploaded file (e.g., "report.pdf").
*   **`event.file.size`** (Integer): The size of the uploaded file in bytes.
*   **`event.file.getBytes()`** (Method): Returns the raw data of the file as a byte array. This is the method you will typically use to get the file's contents for storage in a database.
*   **`event.file.getString(encoding)`** (Method): Returns the file's contents as a string, decoded using the specified character set (defaults to "UTF-8").
*   **`event.file.copyTo(filePath)`** (Method): Saves the uploaded file to a specified path on the Gateway's local filesystem. The `filePath` argument should be a string representing the full path and filename (e.g., "C:\\temp\\uploads\\newfile.txt").

#### `onUploadsCleared`

This event fires after a user has cleared all completed uploads from the component's UI. It does not fire while uploads are in progress. This event can be used to log or confirm that the user has cleared the list.

**`event.files` Object:**

*   **`event.files`** (List): A list of objects, where each object represents a file that was cleared from the list. Each object in the list contains two properties: `name` (string) and `size` (integer, in bytes).

---

### Component Functions (Scripting)

Component functions are called from other scripts (e.g., from a button's `onActionPerformed` event) to interact with the component.

#### `.clearUploads()`

This function resets the File Upload component's UI, clearing the list of any uploaded files.

*   **IMPORTANT:** This function only affects the visual state of the component. It **does not** delete or remove any files that have already been processed and saved by a script on the `onFileReceived` event.

---

### Practical Example: Uploading to and Downloading from a Database

A common use case is to store uploaded files in a database and allow users to download them later.

#### Setup: Database Table

First, create a table in your database to store the files. The column data types may vary depending on your SQL database system. This example uses SQL Server.

*   `id`: `INT`, `PRIMARY KEY`, `IDENTITY`
*   `filename`: `VARCHAR(255)`
*   `filedata`: `VARBINARY(MAX)`

#### Uploading a File

1.  **Add Component**: Drag a **File Upload** component onto your View.
2.  **Configure Event**: Right-click the component and select **Configure Events**.
3.  **Add Script Action**: Select the `onFileReceived` event and add a Script Action.
4.  **Add Script**: Place the following script into the action. This script retrieves the file's name and its byte data, then executes a named query to insert them into the database.

    ```python
    # Get the file's name and its data as a byte array
    filename = event.file.name
    filedata = event.file.getBytes()
    
    # Define the database insert query. 
    # The query and data types may need to be adjusted for your specific database (e.g., MySQL, PostgreSQL).
    query = "INSERT INTO files (filename, filedata) VALUES (?, ?)"
    
    # Define the arguments for the query
    args = [filename, filedata]
    
    # Specify the database connection name
    db_connection = "myDatabase" #<-- Change this to your database connection name
    
    # Execute the query
    system.db.runPrepUpdate(query, args, db_connection)
    ```
5.  **Click OK** to save the event configuration. Now, when a user uploads a file, it will be saved into your database table.

#### Downloading a File

1.  **Add a Table**: Drag a **Table** component onto the same or a different View. This will list the available files.
2.  **Bind Table Data**:
    *   Create a **Named Query** to retrieve the list of files. Let's call it `ListFiles`.
      ```sql
      SELECT id, filename FROM files
      ```
    *   On the Table's `props.data` property, add a **Named Query Binding** and point it to the `ListFiles` query.
3.  **Add a Button**: Drag a **Button** component onto the View. This will trigger the download. Set its text to "Download Selected File".
4.  **Enable/Disable Button**: To prevent errors, disable the button if no file is selected.
    *   On the Button's `props.enabled` property, add an **Expression Binding**.
    *   Use the following expression, assuming your Table component is named "Table":
      ```
      !isNull({../Table.props.selection.selectedRow})
      ```
5.  **Configure Download Script**:
    *   Right-click the **Button** and select **Configure Events**.
    *   On the `onActionPerformed` event, add a **Script Action**.
    *   Add the following script:

    ```python
    # Get the selected row index from the Table component
    selectedRowIndex = self.getSibling("Table").props.selection.selectedRow
    
    # Get the file ID from the Table's data using the selected index
    # Note: 'id' must match the column name from your query
    fileId = self.getSibling("Table").props.data[selectedRowIndex]['id']
    
    # Query the database for the full file data using the ID
    query = "SELECT filename, filedata FROM files WHERE id = ?"
    args = [fileId]
    db_connection = "myDatabase" #<-- Change this to your database connection name
    
    # system.db.runPrepQuery returns a list of rows
    results = system.db.runPrepQuery(query, args, db_connection)
    
    # Check if we got a result
    if results:
        # Get the filename and filedata from the first row of the result set
        filename = results[0]['filename']
        filedata = results[0]['filedata']
        
        # Trigger the download in the user's browser
        system.perspective.download(filename, filedata)
    ```

---

### Helpful Tips

*   **Logic is in the Event:** The File Upload component does nothing on its own. All logic for handling the file (saving, processing, etc.) must be implemented in a script on the `onFileReceived` event.
*   **Database Storage:** Using a database is the most common and robust way to store uploaded files for later retrieval. Ensure your database column can handle large binary data (`BLOB`, `VARBINARY(MAX)`, etc.).
*   **File Paths:** When using `event.file.copyTo()`, the path is relative to the Gateway's file system, not the client's. Ensure the Ignition service has read/write permissions for the target directory.
*   **File Type Syntax:** When using the `supportedFileTypes` property, do not include the dot (`.`) before the extension. Use `["pdf", "txt"]`, not `[".pdf", ".txt"]`.
*   **Size Units:** Remember that `props.fileSizeLimit` is in **megabytes (MB)**, while the `event.file.size` property in the `onFileReceived` event is in **bytes**.
*   **UI vs. Data:** The `.clearUploads()` component method only clears the visual list in the user's session. It has no impact on files that have already been saved to a database or the filesystem.

# Schema - raw
{"schema":{"type":"object","default":{"fileUploadIcon":{"color":"","path":"material/cloud_upload","style":{}},"supportedFileTypes":[],"maxUploads":5,"fileSizeLimit":10},"properties":{"fileUploadIcon":{"$ref":"urn:ignition-schema:schemas/icon-schema.json"},"supportedFileTypes":{"description":"A list of the file types that the control will allow. If nothing is specified, all file types are allowed.","type":"array","items":{"pattern":"^([A-Za-z0-9])*$","type":"string"}},"maxUploads":{"description":"The maximum amount of simultaneous uploads.","type":"number"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"fileSizeLimit":{"description":"The maximum file size in MB (per file) that a user can upload.","type":"number"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"FileUpload","name":"File Upload","palette":{"variants":[{"tooltip":"Allows users to upload files to the Gateway from a Perspective Session.","label":"File Upload"}],"category":"input"},"id":"ia.input.fileupload","events":[{"schema":{"type":"object","properties":{"file":{"type":"object","properties":{"size":{"description":"The size (in bytes) of the file that was uploaded.","type":"integer"},"name":{"description":"The name of the uploaded file.","type":"string"}}}}},"documentationUrl":"https://links.inductiveautomation.com/81-file-upload-component-events","description":"Fired after the gateway has received a file upload.","name":"onFileReceived"},{"schema":{"type":"object","properties":{"files":{"description":"A list of completed uploads. Each object in the list will have the following attributes:","type":"array","items":{"type":"object","properties":{"size":{"description":"The size (in bytes) of the file that was uploaded.","type":"integer"},"name":{"description":"The name of the uploaded file.","type":"string"}}}}}},"documentationUrl":"https://links.inductiveautomation.com/81-file-upload-component-events","description":"This event is fired when the user has cleared all uploads after the uploads have completed.","name":"onUploadsCleared"}]}