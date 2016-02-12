---
layout: default
title: lib.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file is a place to store authoring tool specific, user specific or otherwise arbitrary data for the font. It is optional. If it is not defined in the UFO, there is no lib data.

Data that is too complex or too large for the lib can be stored in the [data directory].

## Specification

The property list data consists of a dictionary at the top level. In order to prevent conflicts in the lib, keys in the top level should follow a [reverse domain naming scheme]. The pattern "public.\*", where \* represents an arbitrary string of one or more characters, is reserved for use in standardized lib keys. It is recommended that the data stored as a value be as shallow as possible.

### Common Key Registry

The following is a registry of public lib keys that map to functionality that is often seen in font editing applications but is not suitable for storage elsewhere in this particular version of the UFO.

#### public.glyphOrder

This key is used for representing the user's preferred glyph order in the font. Authoring tools may use this order for displaying glyphs to the user or setting the glyph order in binaries created with the font data. However, authoring tools are not required to use this order in any way. This data is optional.

The glyph order is stored as a list of glyphs names. Glyph names must not occur more than once. Glyph names in the font may not appear in the order. The order may contain glyphs that are not in the font.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>org.robofab.scripts.SomeData</key>
  <string>Hello World.</string>
  <key>public.glyphOrder</key>
  <array>
    <string>A</string>
    <string>C</string>
    <string>B</string>
  </array>
</dict>
</plist>
```

  [XML Property List]: conventions.html#propertylist
  [data directory]: data.html
  [reverse domain naming scheme]: conventions.html#reversedomain
