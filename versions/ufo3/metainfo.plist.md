---
layout: default
title: metainfo.plist
---

{: .fileformat}
| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains metadata about the UFO. This file is required.

## Specification

The property list data consists of a dictionary at the top level. The keys and values are as follows.

{: .name-type-description}
| key | type | description |
|--|--|--|
| creator | string | The application or library that created the UFO. This should follow a [reverse domain naming scheme]. For example, *org.robofab.ufoLib*. |
| formatVersion | int | The major version number of the UFO format. 3 for UFO 3. |
| formatVersionMinor | int | The minor version number of the UFO format. Optional if the minor version is 0, must be present if the minor version is not 0. |

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
  <integer>3</integer>
  <key>formatVersionMinor</key>
  <integer>0</integer>
</dict>
</plist>
```

  [XML Property List]: ../conventions#xml-property-lists
  [reverse domain naming scheme]: ../conventions#reverse-domain-naming-schemes
