---
layout: default
title: kerning.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains kerning pairs for the font. This file is optional. If it is not defined in the UFO, there is no kerning data.

## Specification

The property list data consists of a dictionary at the top level. Keys are left glyph or group names and values are dictionaries. These dictionaries contain right glyph or group names as keys and kerning values as the values. Glyphs or groups in the pairs are not required to be in the font.

#### Special Considerations

There is no standard indicator (prefix or otherwise) to flag if a pair member is a group or glyph name. If a member of a pair has a name that is defined as a group name in *groups.plist*, assume that the member is a group. Applications that allow group editing should take care to prevent conflicts in groups used for kerning.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>A</key>
  <dict>
    <key>B</key>
    <integer>-10</integer>
    <key>X</key>
    <integer>-10</integer>
    <key>Z</key>
    <integer>-15</integer>
  </dict>
  <key>X</key>
  <dict>
    <key>Q</key>
    <integer>-10</integer>
  </dict>
</dict>
</plist>
```