---
layout: default
title: lib.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains arbitrary data for the font. It is a place to store application specific, user specific or otherwise arbitrary data. This file is optional. If it is not defined in the UFO, there is no lib data.

## Specification

The property list data consists of a dictionary at the top level. In order to prevent conflicts in the lib, keys in the top level should follow a reverse domain naming convention (see below). It is recommended that the data stored as a value be as shallow as possible.

#### Reverse Domain Naming Convention

Keys in the lib should follow a reverse domain naming convention. To make your unique key, reverse your Internet domain. For example, if your Internet domain is *robofab.com*, your reverse domain name would be *com.robofab*. When creating a key for storing data in the lib, use this reverse domain at the beginning of your key. For example to store settings for a script, if your Internet domain is *robofab.com* and your script is called *AccentBuilder*, an appropriate key would be *com.robofab.AccentBuilder*.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>org.robofab.scripts.SomeData</key>
  <string>Hello World.</string>
</dict>
</plist>
```

