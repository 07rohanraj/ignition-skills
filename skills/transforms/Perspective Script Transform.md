# Perspective Script Transform

## Description

This set of instructions provides working examples of using script transforms in Perspective.

## Documentation

Transforms are added to bindings under a "transform" property. This is an array of transforms, with each being executed in order. The 'value' is passed from the source binding down to the first transform. From there, that transform's output is passed to the next transform in the array as the 'value' repeating through the chain of transforms.

It is typical to only need one transform, but multiple can be used.
The script transform uses jython 2.7 and must be compatible with that. Do not import cpython libraries. Do not use f"string {var}" style string formatting ("string %s" %(var) is a good alternative).

A script transform will have a format of: {"code": "your JSON escaped code", "type": "script"}

# Example View JSON Showing Transform Schema
{"custom":{},"params":{},"props":{},"root":{"children":[{"meta":{"name":"Label"},"position":{"height":78,"width":259,"x":151,"y":97},"propConfig":{"custom.componentTransformMulti":{"binding":{"config":{"expression":"1"},"transforms":[{"code":"\treturn value * 2","type":"script"},{"code":"\treturn value + 100","type":"script"},{"code":"\treturn value * 2","type":"script"}],"type":"expr"}},"custom.componentTransformSingle":{"binding":{"config":{"expression":"1"},"transforms":[{"code":"\treturn value * 2","type":"script"}],"type":"expr"}}},"props":{"text":"Label"},"type":"ia.display.label"}],"meta":{"name":"root"},"propConfig":{"custom.scriptTransformExampleMulti":{"binding":{"config":{"expression":"1"},"transforms":[{"code":"\treturn value * 2","type":"script"},{"code":"\treturn value + 100","type":"script"},{"code":"\treturn value * 2","type":"script"}],"type":"expr"}},"custom.scriptTransformExampleSingle":{"binding":{"config":{"expression":"1"},"transforms":[{"code":"\treturn value * 2","type":"script"}],"type":"expr"}}},"type":"ia.container.coord"}}