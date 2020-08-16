---
layout: default
title: layercontents.plist
---

{: .fileformat}
| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file maps the layer names to the glyph directory names. This file is required.

## Specification

The mapping is stored as a list in the property list. This list also defines the order of the layers from top to bottom. The mapping is stored within the list as lists containing the layer names first and the directory name second.

The directory names must begin with "glyphs." and must be followed by a string that is unique within the set of other layer directory names in the font. The directory names stored in the property list must be plain directory names, not absolute or relative paths in the file system, and they must include the "glyphs." prefix if applicable. Care must be taken when choosing directory names: layer names are case sensitive, yet many file systems are not. There is no one standard layer name to file name conversion. However, a common implementation is defined in the [conventions].

The required glyph set stored in the *glyphs* directory may have a user defined name. If it does not, the name "public.default" must be used to represent the name of the layer in the contents.

Layer names may contain any character except they must not contain [control characters]. They must be at least one character long. There is no maximum layer name length. Layer names must be unique within the font. The pattern "public.\*", where \* represents an arbitrary string of one or more characters, is reserved for use in standardized layer names.

Authoring tools should preserve directory names when writing into existing UFOs. This can be done by referencing the existing layercontents.plist before the write operation.

### Common Layer Registry

The following is a registry of public layer names that map to functionality that is often seen in font editing applications. These common layer names allow authoring tools to exchange common layer types while the authoring tools maintain their own unique UI names for the layers.

#### public.default

This layer name indicates that the default layer has no user defined name. It must not be used as the layer name for any directory other than the default *glyphs* directory.

#### public.background

This represents background reference layers such as the "Template" layer in Fontographer, the "Mask" layer in FontLab and the "Background" layer in FontForge. Applications may write this common layer into a UFO using the layer name "public.background" and assigning an appropriate layer directory name. Likewise, an authoring tool that encounters a layer named "public.background" may use this layer for its own particular background reference layer.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
  <array>
    <string>public.default</string>
    <string>glyphs</string>
  </array>
  <array>
    <string>Sketches</string>
    <string>glyphs.S_ketches</string>
  </array>
  <array>
    <string>public.background</string>
    <string>glyphs.public.background</string>
  </array>
</array>
</plist>

```

  [XML Property List]: ../conventions/#xml-property-lists
  [conventions]: ../conventions/#common-user-name-to-file-name-algorithm
  [control characters]: ../conventions/#controls
