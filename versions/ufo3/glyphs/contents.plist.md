---
layout: default
title: contents.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

*contents.plist* contains a dictionary that maps glyph names to GLIF file names.

Glyph names may contain any character and they may be any length. Glyph names must be unique within the layer.

## Specification

The property list data consists of a dictionary at the top level. The keys are glyph names and the values are file names.

The file names must end with ".glif" and must begin with a string that is unique within the layer. The file names stored in the property list must be plain file names, not absolute or relative paths in the file system, and they must include the ".glif" extension. Care must be taken when choosing file names: glyph names are case sensitive, yet many file systems are not. There is no one standard glyph name to file name conversion. However, a common implementation is defined in the [conventions].

Authoring tools should preserve GLIF file names when writing into existing UFOs. This can be done by referencing the existing contents.plist before the write operation. The glyph name to file name mapping can then be referenced when creating new file names.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>A</key>
  <string>A_.glif</string>
  <key>B</key>
  <string>B_.glif</string>
</dict>
</plist>
```