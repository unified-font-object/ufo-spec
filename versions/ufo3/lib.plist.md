---
layout: default
title: lib.plist
---

{: .fileformat}
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

#### public.openTypeCategories

This key is used to define the category of the glyphs to be used, for example, as glyph class in the [OpenType GDEF Glyph Class Definition Table]. The categories are stored in a dictionary keyed by glyph name. Both key and values must be strings. Values must be one of `unassigned`, `base`, `mark`, `ligature` or `component`. This data is optional.

The dictionary may contain glyph names that are not in the font. The dictionary may not contain a key, value pair for all glyphs in the font.
**Note:** If a glyph's category is not defined in the dictionary, authoring tools may assign it to any glyph class in the OpenType GDEF Glyph Class Definition Table.


```xml
<key>public.openTypeCategories</key>
<dict>
  <key>A</key>
  <string>base</string>
  <key>B</key>
  <string>base</string>
  <key>f_f</key>
  <string>ligature</string>
  <key>acutecomb</key>
  <string>mark</string>
</dict>
```

#### public.openTypePostUnderlinePosition

This defines an integer position for underline, defined as the top of the underline from the baseline (the [OpenType post table definition]). If present, this value should be used for `underlinePosition` of the OpenType `post` table. If `postscriptUnderlinePosition` is not defined, this value should be used to calculate the `Type 1` and OpenType `CFF` `underlinePosition`; if `postscriptUnderlinePosition` is also present in addition to `public.openTypePostUnderlinePosition`, the `postscriptUnderlinePosition` value must be used for `Type 1` and `CFF`. 

To calculate the `Type 1`/`CFF` `UnderlinePosition` do:  `public.openTypePostUnderlinePosition` - `postscriptUnderlineThickness`/2. If this result is a float, round the value according to [OpenType normalization] (i.e. 33.5 rounds to 34, -33.5 rounds to 33).

#### public.postscriptNames

This defines a preferred glyph name to Postscript glyph name mapping for glyphs in the font. Authoring tools should use the values defined in this mapping when outputting font data formats such as the `post` and `CFF ` tables in OpenType. This data is optional.

The mapping is stored as a dictionary with glyphs names as keys and Postscript glyph names as values. Both keys and values must be strings. The values must conform to the Postscript glyph naming specification. The dictionary may contain glyph names that are not in the font. The dictionary may not contain a key, value pair for all glyphs in the font. If a glyph's name is not defined in this mapping, the glyph's name should be used as the Postscript name.

#### public.truetype.instructions
This key provides a dict defining TrueType instructions data.
The assembly is represented by a single string of fontTools TrueType instructions assembly with optional line formatting between instructions.
This data is optional.

| key                   | value type | description                 |
|-----------------------|------------|-----------------------------|
| formatVersion         | string     | Format version. Set to "1". |
| controlValue          | dict       | TrueType instructions control values as a dictionary of control values keyed by index. This is optional. |
| controlValueProgram   | string     | TrueType preprogram assembly as a string. This is optional. |
| fontProgram           | string     | TrueType font program assembly as a string. This is optional. |
| maxFunctionDefs       | integer    | Number of function definitions, used by TrueType instructions, stored in the `maxp` in OpenType table as an integer. This is optional.            |
| maxInstructionDefs    | integer    | Number of instruction definitions, used by TrueType instructions, stored in the `maxp` in OpenType table as an integer. This is optional.         |
| maxStackElements      | integer    | Maximum stack depth, used by TrueType instructions, stored in the `maxp` in OpenType table as an integer. This is optional.                       |
| maxStorage            | integer    | Maximum number of storage area locations, used by TrueType instructions, stored in the `maxp` in OpenType table. This is optional.                |
| maxSizeOfInstructions | integer    | Maximum byte count for glyph instructions, used by TrueType instructions, stored in the `maxp` in OpenType table as an integer. This is optional. |
| maxTwilightPoints     | integer    | Maximum points used in zone 0, stored in the `maxp` in OpenType table as an integer. This is optional.                                            |
| maxZones              | integer    | Number of zones used by TrueType instructions, stored in the `maxp` in OpenType table as an integer. This is optional.                            |

#### public.skipExportGlyphs

This key is a list of glyph names used for representing glyphs that the user does not want exported to the final font file. The UFO compiler is expected to:

1. Decompose the listed glyphs everywhere they are used as components.
2. Remove these glyphs before the compilation run.
3. Prune all groups of the listed glyphs.
4. Prune all kerning pairs that contain any of the listed glyphs.
5. Not modify the source UFO on disk. This is a compiler-internal process.

The handling of the feature file is undefined.

This data is optional. Glyph names must not occur more than once. The list may contain glyphs that are not in the font. An empty list or the absence of this key means that all glyphs are to be exported as-is with groups and kerning untouched.

#### public.unicodeVariationSequences

This key is a dictionary for Unicode Variation Sequences. Keys are *Variation Selector* code points as a hexadecimal numbers and values are dictionaries. These dictionaries contain code points as hexidecimal numbers as keys and glyph names as values. This data and the glyphs' Unicode code points can be used to generate the [OpenType cmap subtable format 14] for Unicode [Variation Sequences].

This data is optional.

```xml
<key>public.unicodeVariationSequences</key>
<dict>
  <key>FE0E</key>
  <dict>
    <key>1F170</key>
    <string>Anegativesquared.text</string>
  </dict>
  <key>FE0F</key>
  <dict>
    <key>1F170</key>
    <string>Anegativesquared</string>
  </dict>
</dict>
```

#### public.objectLibs

This key provides a dictionary of data containing object-level lib data for individual guidelines within fontinfo.plist. The dictionary is structured with object identifiers that correspond to guidelines as keys and object-level dictionaries as values. Within each of these of these object-level dictionaries, keys should follow a [reverse domain naming scheme]. The pattern "public.\*", where `*` represents an arbitrary string of one or more characters, is reserved for use in standardized lib keys. It is recommended that the data stored as a value be as shallow as possible. If a key in this dictionary is not an identifier of any guideline within fontinfo.plist, the key and value may be discarded.

```xml
<key>com.sometool.smartGuides</key>
<dict>
  <key>7pdbofkUhz</key>
  <dict>
    <key>unicodeCategory</key>
    <string>Lu</string>
  </dict>
  <key>z1bkCMlhNb</key>
  <dict>
    <key>contourCount</key>
    <array>
      <string>&gt;</string>
      <integer>0</integer>
    </array>
    <key>glyphNamePattern</key>
    <string>*.sc*</string>
  </dict>
</dict>
```

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
  [OpenType cmap subtable format 14]: https://docs.microsoft.com/en-us/typography/opentype/spec/cmap#format-14-unicode-variation-sequences
  [OpenType GDEF Glyph Class Definition Table]: https://docs.microsoft.com/en-us/typography/opentype/spec/gdef#glyph-class-definition-table
  [Variation Sequences]: http://www.unicode.org/faq/vs.html
  [OpenType post table definition]: https://learn.microsoft.com/en-us/typography/opentype/spec/post
  [OpenType normalization]: https://docs.microsoft.com/en-us/typography/opentype/spec/otvaroverview#coordinate-scales-and-normalization
