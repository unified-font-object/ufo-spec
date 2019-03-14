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

#### public.openTypeMeta

This key is used for representing the `meta` table in OpenType, stored as a dictionary keyed by tag.
If present, the registered tags `appl` and `bild` have their values stored as data and the registered tags `dlng` and `slng` have their values each stored as an array of ScriptLangTag strings.
Authoring tools should translate each value of `dlng` and `slng` to a comma-separated ScriptLangTags string.
Any private tag must have its value stored as data or string.
This data is optional.

##### Notes

[The OpenType meta table specification.]

#### public.postscriptNames

This defines a preferred glyph name to Postscript glyph name mapping for glyphs in the font. Authoring tools should use the values defined in this mapping when outputting font data formats such as the `post` and `CFF ` tables in OpenType. This data is optional.

The mapping is stored as a dictionary with glyphs names as keys and Postscript glyph names as values. Both keys and values must be strings. The values must conform to the Postscript glyph naming specification. The dictionary may contain glyph names that are not in the font. The dictionary may not contain a key, value pair for all glyphs in the font. If a glyph's name is not defined in this mapping, the glyph's name should be used as the Postscript name.

#### public.skipExportGlyphs

This key is a list of glyph names used for representing glyphs that the user does not want exported to the final font file. The UFO compiler is expected to:

1. Decompose the listed glyphs everywhere they are used as components.
2. Remove these glyphs before the compilation run.
3. Prune all groups of the listed glyphs. Subsequently empty groups must be removed.
4. Prune all kerning pairs that contain any of the listed glyphs or now empty groups.
5. Not modify the source UFO on disk. This is a compiler-internal process.

The handling of the feature file is undefined.

This data is optional. Glyph names must not occur more than once. The list may contain glyphs that are not in the font. An empty list or the absence of this key means that all glyphs are to be exported as-is with groups and kerning untouched.

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

  [XML Property List]: ../conventions/#xml-property-lists
  [data directory]: ../data
  [reverse domain naming scheme]: ../conventions/#reverse-domain-naming-schemes
  [The OpenType meta table specification.]: http://www.microsoft.com/typography/otspec/meta.htm
