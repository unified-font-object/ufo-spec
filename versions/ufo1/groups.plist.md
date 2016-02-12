---
layout: default
title: groups.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains the definitions of arbitrary groups of glyphs. This file is optional. If it is not defined in the UFO, there is no group data.

## Specification

The property list data consists of a dictionary at the top level. Keys are group names and values are arrays of glyph name strings. There is no standard for naming groups. Glyphs may be in more than one group. Glyphs listed in the arrays are not required to be in the font.

#### Special Considerations

Some groups may be used in kerning. See the [kerning.plist documentation] for more information and special considerations.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Group1</key>
  <array>
    <string>A</string>
    <string>A.alt</string>
  </array>
  <key>B</key>
  <array>
    <string>B</string>
    <string>B.alt</string>
  </array>
</dict>
</plist>
```

 [kerning.plist documentation]: ../kerning.plist
