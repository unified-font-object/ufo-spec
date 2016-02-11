---
layout: default
title: metainfo.plist
---

| __File Format__ | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains metadata about the UFO. This file is required.

## Specification

The property list data consists of a dictionary at the top level. The keys and values are as follows.

| key            | value type   | description |
|----------------|--------------|-------------|
| creator        | string       | The application or library that created the UFO. This should follow a reverse domain naming convention. For example, _org.robofab.ufoLib_. |
| formatVersion  | int          | The version number of the UFO format. 1 for UFO 1. |

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
    <integer>1</integer>
</dict>
</plist>
```

