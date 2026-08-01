# Perspective Barcode Display Component

## Description

This documentation describes the usage and configuration of the Perspective Barcode Display Component, explaining how to render a data value as a machine-readable image. It details the component's properties for setting the value, selecting from over 100 supported barcode specifications, and applying custom styles to the barcode and its human-readable text.

## Documentation

# Instructions
Of course, here is the information you requested on the Perspective Barcode Display Component.

# Perspective Barcode Display Component

## Description
The Perspective Barcode component is used to display a string or number value as a machine-readable barcode. It supports 105 different barcode specifications, allowing for a wide range of use cases from product identification to information sharing. The component can be configured to show or hide the human-readable value and provides extensive styling options for both the barcode and its associated text.

For quick implementation, the component comes with three variants in the Component Palette: a default Barcode, a Code 128 barcode, and a QR Code.

## Properties

| Property | Type | Description |
| :--- | :--- | :--- |
| **value** | String or Number | **Required.** The data that will be encoded into the barcode. |
| **type** | String | The barcode specification to use for encoding. The default is "code128". See the full list of supported types below. |
| **displayValue** | Boolean | If true, the `value` of the barcode will be displayed as human-readable text. Defaults to `true`. |
| **valuePosition** | String | Determines the position of the human-readable text when `displayValue` is true. Can be "top" or "bottom". Defaults to "bottom". |
| **valueStyle** | Style Object | An object that defines the style for the displayed value text. This includes properties for font, color, background, margins, and borders. |
| **errorStyle** | Style Object | An object that defines the style for the component when the provided `value` cannot be encoded by the selected `type`. This allows for visual feedback on invalid barcode data. |
| **style** | Style Object | An object that defines the overall style for the component, affecting properties like padding, borders, and background of the entire component. |

---

### Supported Barcode Specifications (`type` property)

The `type` property accepts one of the following 105 string values:

**A-B**
*   auspost
*   azteccode
*   azteccodecompact
*   aztecrune
*   bc412

**C**
*   channelcode
*   codablockf
*   code11
*   code128
*   code16k
*   code2of5
*   code32
*   code39
*   code39ext
*   code49
*   code93
*   code93ext
*   codeone
*   coop2of5

**D**
*   daft
*   databarexpanded
*   databarexpandedcomposite
*   databarexpandedstacked
*   databarexpandedstackedcomposite
*   databarlimited
*   databarlimitedcomposite
*   databaromni
*   databaromnicomposite
*   databarstacked
*   databarstackedcomposite
*   databarstackedomni
*   databarstackedomnicomposite
*   databartruncated
*   databartruncatedcomposite
*   datalogic2of5
*   datamatrix
*   datamatrixrectangular
*   datamatrixrectangularextension
*   dotcode

**E-G**
*   ean13
*   ean13composite
*   ean14
*   ean2
*   ean5
*   ean8
*   ean8composite
*   flattermarken
*   gs1-128
*   gs1-128composite
*   gs1-cc
*   gs1datamatrix
*   gs1datamatrixrectangular
*   gs1northamericancoupon
*   gs1qrcode

**H-J**
*   hanxin
*   hibcazteccode
*   hibccodablockf
*   hibccode128
*   hibccode39
*   hibcdatamatrix
*   hibcdatamatrixrectangular
*   hibcmicropdf417
*   hibcpdf417
*   hibcqrcode
*   iata2of5
*   identcode
*   industrial2of5
*   interleaved2of5
*   isbn
*   ismn
*   issn
*   itf14
*   japanpost

**K-P**
*   kix
*   leitcode
*   mailmark
*   matrix2of5
*   maxicode
*   micropdf417
*   microqrcode
*   msi
*   onecode
*   pdf417
*   pdf417compact
*   pharmacode
*   pharmacode2
*   planet
*   plessey
*   posicode
*   postnet
*   pzn

**Q-Z**
*   qrcode
*   rationalizedCodabar
*   raw
*   royalmail
*   sscc18
*   symbol
*   telepen
*   telepennumeric
*   ultracode
*   upca
*   upcacomposite
*   upce
*   upcecomposite

## Component Events
The Barcode component supports standard Perspective component events. For a full reference and configuration instructions, please refer to the official documentation on [Component Events and Actions](https://docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/working-with-perspective-components/component-events-and-actions/) and the [Perspective Event Types Reference](https://docs.inductiveautomation.com/docs/8.1/appendix/reference-pages/perspective-event-types-reference/).

---

## Helpful Tips
*   The `value` property is required. Without a value, the component will not render a barcode.
*   To display the human-readable text of the barcode's value, the `displayValue` property must be set to `true`. This is the default setting.
*   The `valuePosition` and `valueStyle` properties only have an effect when `displayValue` is `true`.
*   You can bind the `value` property to a tag or another component property to create dynamic barcodes that update in real-time.
*   The `errorStyle` property is useful for providing immediate visual feedback to a user if they enter a value that is invalid for the selected barcode type (e.g., non-numeric characters for a numeric-only barcode type).
*   For quick use, drag one of the pre-configured variants from the Component Palette:
    *   **Code 128**: A general-purpose barcode.
    *   **QR Code**: Sets the `type` property to `qrcode`, ideal for encoding URLs or larger amounts of text.
*   **Example 1: Creating a UPC-A Barcode**
    *   Set `props.value` to a valid UPC number, e.g., "014113910613".
    *   Set `props.type` to "upca".
    *   Set `props.displayValue` to `true`.
    *   Set `props.valuePosition` to "bottom".
    *   You can customize the text style using `props.valueStyle`, for example, setting `fontFamily` to "Verdana" and `fontSize` to "18px".
*   **Example 2: Creating a QR Code**
    *   Set `props.value` to the data you want to encode, e.g., a URL like "http://inductiveautomation.com".
    *   Set `props.type` to "qrcode".
    *   To make the value more prominent, you could set `props.valuePosition` to "top" and apply styles like `color`, `fontWeight`, and `fontSize` via the `props.valueStyle` object.
    *   Use the main `props.style` object to add padding around the entire component, for instance, by setting `paddingTop` to "12px".

# Schema - raw
{"schema":{"type":"object","properties":{"valueStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"type":{"description":"What barcode specification to use.","type":"string","enum":["auspost","azteccode","azteccodecompact","aztecrune","bc412","channelcode","codablockf","code11","code128","code16k","code2of5","code32","code39","code39ext","code49","code93","code93ext","codeone","coop2of5","daft","databarexpanded","databarexpandedcomposite","databarexpandedstacked","databarexpandedstackedcomposite","databarlimited","databarlimitedcomposite","databaromni","databaromnicomposite","databarstacked","databarstackedcomposite","databarstackedomni","databarstackedomnicomposite","databartruncated","databartruncatedcomposite","datalogic2of5","datamatrix","datamatrixrectangular","datamatrixrectangularextension","dotcode","ean13","ean13composite","ean14","ean2","ean5","ean8","ean8composite","flattermarken","gs1-128","gs1-128composite","gs1-cc","gs1datamatrix","gs1datamatrixrectangular","gs1northamericancoupon","gs1qrcode","hanxin","hibcazteccode","hibccodablockf","hibccode128","hibccode39","hibcdatamatrix","hibcdatamatrixrectangular","hibcmicropdf417","hibcpdf417","hibcqrcode","iata2of5","identcode","industrial2of5","interleaved2of5","isbn","ismn","issn","itf14","japanpost","kix","leitcode","mailmark","matrix2of5","maxicode","micropdf417","microqrcode","msi","onecode","pdf417","pdf417compact","pharmacode","pharmacode2","planet","plessey","posicode","postnet","pzn","qrcode","rationalizedCodabar","raw","royalmail","sscc18","symbol","telepen","telepennumeric","ultracode","upca","upcacomposite","upce","upcecomposite"],"default":"code128"},"displayValue":{"description":"If true, this barcode's value will be displayed as text.","type":"boolean","default":true},"errorStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"valuePosition":{"description":"If displayValue is true, where should the value be displayed.","type":"string","enum":["top","bottom"],"default":"bottom"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"value":{"description":"The value to be encoded as a barcode","type":["string","number"],"required":true,"default":"Value"}}},"resources":[{"type":"js","path":"/res/perspective/js/PerspectiveBarcode.js","name":"barcode-component"},{"type":"css","path":"/res/perspective/css/PerspectiveBarcode.css","name":"barcode-component-css"}],"defaultMetaName":"Barcode","name":"Barcode","palette":{"variants":[{"tooltip":"Enables text to be displayed as a barcode.","label":"Barcode"},{"tooltip":"Enables text to be displayed as a barcode.","label":"Code 128","id":"barcode-128"},{"tooltip":"Enables text to be displayed as a barcode.","label":"QR Code","props":{"type":"qrcode"},"id":"barcode-qr"}],"category":"display"},"id":"ia.display.barcode"}