---
layout: default
title: metainfo.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains metadata about the UFO. This file is required.

## Specification

The property list data consists of a dictionary at the top level. The keys and values are as follows.

| key           | value type | description                                                                                                                                |
|---------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| creator       | string     | The application or library that created the UFO. This should follow a reverse domain naming convention. For example, *org.robofab.ufoLib*. |
| formatVersion | int        | The version number of the UFO format. 2 for UFO 2.                                                                                         |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>creator</key>
    <string>org.robofab.ufoLib</string>
    <key>formatVersion</key>
    <integer>2</integer>
</dict>
</plist>
```