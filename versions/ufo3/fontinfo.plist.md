---
layout: default
title: fontinfo.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains information about the font itself, such as naming and dimensions. This file is optional. Not all values are required for a proper file.

#### Bit Numbers

Throughout this specification are references to "bit numbers." These are lists of integers that correspond to the bits that should be set for particular fields in the referenced font specifications. Consider this example from a fictional font specification:

| type   | name | description  |
|--------|------|--------------|
| USHORT | foo  | Bit 0: Left <br>Bit 1: Right <br>Bit 2: Up <br>Bit 3: Down |

Translated to the structure used in this specification would be:

| key                  | value type | description                                                                                                                                                          |
|----------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fictionalFontSpecFoo | list       | A list of bit numbers indicating the bits that should be set in `foo`. The bit numbers are listed in the fictional font specification. Corresponds to the foo field. |

In a fontinfo.plist file, to indicate "left" and "up" the data would look like this:

```xml
<key>fictionalFontSpecFoo</key>
<array>
  <integer>0</integer>
  <integer>2</integer>
</array>
```

## Specification

#### Generic Identification Information

| key                | value type           | description                                                                                                                                                                                                                       |
|--------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| familyName         | string               | Family name.                                                                                                                                                                                                                      |
| styleName          | string               | Style name.                                                                                                                                                                                                                       |
| styleMapFamilyName | string               | Family name used for bold, italic and bold italic style mapping.                                                                                                                                                                  |
| styleMapStyleName  | string               | Style map style. The possible values are *regular*, *italic*, *bold* and *bold italic*. These are case sensitive.                                                                                                                 |
| versionMajor       | integer              | Major version.                                                                                                                                                                                                                    |
| versionMinor       | non-negative integer | Minor version.                                                                                                                                                                                                                    |
| year               | integer              | The year the font was created. This attribute is deprecated as of version 2. It's presence should not be relied upon by authoring tools. However, it may occur in a font's info so authoring tools should preserve it if present. |

#### Generic Legal Information

| key       | value type | description          |
|-----------|------------|----------------------|
| copyright | string     | Copyright statement. |
| trademark | string     | Trademark statement. |

#### Generic Dimension Information

| key         | value type                    | description                                                                         |
|-------------|-------------------------------|-------------------------------------------------------------------------------------|
| unitsPerEm  | non-negative integer or float | Units per em.                                                                       |
| descender   | integer or float              | Descender value.                                                                    |
| xHeight     | integer or float              | x-height value.                                                                     |
| capHeight   | integer or float              | Cap height value.                                                                   |
| ascender    | integer or float              | Ascender value.                                                                     |
| italicAngle | integer or float              | Italic angle. This must be an angle in counter-clockwise degrees from the vertical. |

#### Generic Miscellaneous Information

| key  | value type | description                    |
|------|------------|--------------------------------|
| note | string     | Arbitrary note about the font. |

#### OpenType gasp Table Fields

| key                      | value type | description                                                                                                            |
|--------------------------|------------|------------------------------------------------------------------------------------------------------------------------|
| openTypeGaspRangeRecords | list       | A list of gasp Range Records. These must be sorted in ascending order based on the `rangeMaxPPEM` value of the record. |

##### gasp Range Record Format

The records are stored as dictionaries of the following format.

| key               | value type           | description                                                                                                                                                                                                                                                |
|-------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| rangeMaxPPEM      | non-negative integer | The upper limit of the range, in PPEM. If any records are in the list, the final record should use 65535 (0xFFFF) as defined in the OpenType gasp specification. Corresponds to the rangeMaxPPEM field of the GASPRANGE record in the OpenType gasp table. |
| rangeGaspBehavior | list                 | A list of bit numbers indicating the flags to be set. The bit numbers are defined below. Corresponds to the rangeGaspBehavior field of the GASPRANGE record in the OpenType gasp table.                                                                    |

###### rangeGaspBehavior Bits

The following bit numbers correspond to the matching bits in the OpenType gasp specification listed in the description column.

| value | description                         |
|-------|-------------------------------------|
| 0     | GASP\_GRIDFIT (0x0001)              |
| 1     | GASP\_DOGRAY (0x0002)               |
| 2     | GASP\_SYMMETRIC\_SMOOTHING (0x0004) |
| 3     | GASP\_SYMMETRIC\_GRIDFIT (0x0008)   |

##### Notes

[The OpenType gasp table specification.]

#### OpenType head Table Fields

| key                       | value type           | description                                                                                                                                                                                                                                                                                                                |
|---------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| openTypeHeadCreated       | string               | Creation date. Expressed as a string of the format "YYYY/MM/DD HH:MM:SS". "YYYY/MM/DD" is year/month/day. The month must be in the range 1-12 and the day must be in the range 1-end of month. "HH:MM:SS" is hour:minute:second. The hour must be in the range 0:23. The minute and second must each be in the range 0-59. |
| openTypeHeadLowestRecPPEM | non-negative integer | Smallest readable size in pixels. Corresponds to the OpenType head table `lowestRecPPEM` field.                                                                                                                                                                                                                            |
| openTypeHeadFlags         | list                 | A list of bit numbers indicating the flags. The bit numbers are listed in the OpenType head specification. Corresponds to the OpenType head table `flags` field.                                                                                                                                                           |

##### Notes

[The OpenType head table specification.]

1.  `fontRevision` can be derived from the generic `versionMajor` and `versionMinor` attributes.
2.  `checkSumAdjustment` should be calculated by the authoring tool.
3.  `magicNumber` should be set by the authoring tool.
4.  `unitsPerEm` is found at the generic `unitsPerEm` attribute.
5.  `created` can be calculated by subtracting the *12:00 midnight, January 1, 1904* (as specified in the head table documentation) from the date stored at `openTypeHeadCreated`.
6.  `modified` should be set by the authoring tool.
7.  `xMin, yMin, xMax` and `yMax` should be calculated by the authoring tool.
8.  `macStyle` can be derived from the generic `styleMapStyleName` attribute.
9.  `indexToLocFormat` should be set by the authoring tool.
10. `glyphDataFormat` should be set by the authoring tool.

#### OpenType hhea Table Fields

| key                        | value type | description                                                                            |
|----------------------------|------------|----------------------------------------------------------------------------------------|
| openTypeHheaAscender       | integer    | Ascender value. Corresponds to the OpenType hhea table `Ascender` field.               |
| openTypeHheaDescender      | integer    | Descender value. Corresponds to the OpenType hhea table `Descender` field.             |
| openTypeHheaLineGap        | integer    | Line gap value. Corresponds to the OpenType hhea table `LineGap` field.                |
| openTypeHheaCaretSlopeRise | integer    | Caret slope rise value. Corresponds to the OpenType hhea table `caretSlopeRise` field. |
| openTypeHheaCaretSlopeRun  | integer    | Caret slope run value. Corresponds to the OpenType hhea table `caretSlopeRun` field.   |
| openTypeHheaCaretOffset    | integer    | Caret offset value. Corresponds to the OpenType hhea table `caretOffset` field.        |

##### Notes

[The OpenType hhea table specification]

1.  `advanceWidthMax` should be calculated by the authoring tool.
2.  `minLeftSideBearing` should be calculated by the authoring tool.
3.  `minRightSideBearing` should be calculated by the authoring tool.
4.  `xMaxExtent` should be calculated by the authoring tool.
5.  `metricDataFormat` should be set by the authoring tool.
6.  `numberOfHMetrics` should be calculated by the authoring tool.

#### OpenType Name Table Fields

| key                                | value type | description                                                                                                                                 |
|------------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| openTypeNameDesigner               | string     | Designer name. Corresponds to the OpenType name table name ID 9.                                                                            |
| openTypeNameDesignerURL            | string     | URL for the designer. Corresponds to the OpenType name table name ID 12.                                                                    |
| openTypeNameManufacturer           | string     | Manufacturer name. Corresponds to the OpenType name table name ID 8.                                                                        |
| openTypeNameManufacturerURL        | string     | Manufacturer URL. Corresponds to the OpenType name table name ID 11.                                                                        |
| openTypeNameLicense                | string     | License text. Corresponds to the OpenType name table name ID 13.                                                                            |
| openTypeNameLicenseURL             | string     | URL for the license. Corresponds to the OpenType name table name ID 14.                                                                     |
| openTypeNameVersion                | string     | Version string. Corresponds to the OpenType name table name ID 5.                                                                           |
| openTypeNameUniqueID               | string     | Unique ID string. Corresponds to the OpenType name table name ID 3.                                                                         |
| openTypeNameDescription            | string     | Description of the font. Corresponds to the OpenType name table name ID 10.                                                                 |
| openTypeNamePreferredFamilyName    | string     | Preferred family name. Corresponds to the OpenType name table name ID 16.                                                                   |
| openTypeNamePreferredSubfamilyName | string     | Preferred subfamily name. Corresponds to the OpenType name table name ID 17.                                                                |
| openTypeNameCompatibleFullName     | string     | Compatible full name. Corresponds to the OpenType name table name ID 18.                                                                    |
| openTypeNameSampleText             | string     | Sample text. Corresponds to the OpenType name table name ID 19.                                                                             |
| openTypeNameWWSFamilyName          | string     | WWS family name. Corresponds to the OpenType name table name ID 21.                                                                         |
| openTypeNameWWSSubfamilyName       | string     | WWS Subfamily name. Corresponds to the OpenType name table name ID 22.                                                                      |
| openTypeNameRecords                | list       | A list of name records. This name record storage area is intended for records that require platform, encoding and or language localization. |

##### Name Record Format

The records are stored as dictionaries of the following format.

| key        | value type           | description                      |
|------------|----------------------|----------------------------------|
| nameID     | non-negative integer | The name ID.                     |
| platformID | non-negative integer | The platform ID.                 |
| encodingID | non-negative integer | The encoding ID.                 |
| languageID | non-negative integer | The language ID.                 |
| string     | string               | The string value for the record. |

Records should have a unique `nameID`, `platformID`, `encodingID` and `languageID` combination. In cases where a duplicate is found, the last occurrence of the `nameID`, `platformID`, `encodingID` and `languageID` combination must be taken as the value.

##### Notes

[The OpenType name table specification.]

1.  *Name ID 0 (copyright)* is found at the generic `copyright` attribute.
2.  *Name ID 1 (font family name)* is found at the generic `styleMapFamilyName` attribute.
3.  *Name ID 2 (font subfamily name)* can be interpreted from the generic `styleMapStyleName` attribute.
4.  *Name ID 4 (full font name)* can be created from the generic `styleMapFamilyName` and `styleMapStyleName` attributes following the rules defined in the specification.
5.  *Name ID 6 (Postscript name)* can be found at `postscriptFontName`. This should follow the rules defined in the specification.
6.  *Name ID 7 (trademark)* is found at the generic `trademark` attribute.
7.  Authoring tools should not make any assumptions about the validity (as defined by the OpenType specification) of the naming data contained in these fields.
8.  To reiterate the point stated above, these notes are merely provided for clarity. Authoring tools can and should follow their own recipes for creating the name table. These notes make no considerations for platform specific variations in or application specific limitations on the strings.

#### OpenType OS/2 Table Fields

| key                           | value type           | description                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| openTypeOS2WidthClass         | integer              | Width class value. Must be in the range 1-9. Corresponds to the OpenType OS/2 table `usWidthClass` field.                                                                                                                                                                                                                                              |
| openTypeOS2WeightClass        | integer              | Weight class value. Must be a non-negative integer. Corresponds to the OpenType OS/2 table `usWeightClass` field.                                                                                                                                                                                                                                      |
| openTypeOS2Selection          | list                 | A list of bit numbers indicating the bits that should be set in fsSelection. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table `selection` field. **Note:** Bits 0 (italic), 5 (bold) and 6 (regular) must not be set here. These bits should be taken from the generic *styleMapStyleName* attribute. |
| openTypeOS2VendorID           | string               | Four character identifier for the creator of the font. Corresponds to the OpenType OS/2 table `achVendID` field.                                                                                                                                                                                                                                       |
| openTypeOS2Panose             | list                 | The list must contain 10 non-negative integers that represent the setting for each category in the Panose specification. The integers correspond with the option numbers in each of the Panose categories. This corresponds to the OpenType OS/2 table `Panose` field.                                                                                 |
| openTypeOS2FamilyClass        | list                 | Two integers representing the IBM font class and font subclass of the font. The first number, representing the class ID, must be in the range 0-14. The second number, representing the subclass, must be in the range 0-15. The numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table `sFamilyClass` field.   |
| openTypeOS2UnicodeRanges      | list                 | A list of bit numbers that are supported Unicode ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table `ulUnicodeRange1`, `ulUnicodeRange2`, `ulUnicodeRange3` and `ulUnicodeRange4` fields.                                                                                       |
| openTypeOS2CodePageRanges     | list                 | A list of bit numbers that are supported code page ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table `ulCodePageRange1` and `ulCodePageRange2` fields.                                                                                                                         |
| openTypeOS2TypoAscender       | integer              | Ascender value. Corresponds to the OpenType OS/2 table `sTypoAscender` field.                                                                                                                                                                                                                                                                          |
| openTypeOS2TypoDescender      | integer              | Descender value. Corresponds to the OpenType OS/2 table `sTypoDescender` field.                                                                                                                                                                                                                                                                        |
| openTypeOS2TypoLineGap        | integer              | Line gap value. Corresponds to the OpenType OS/2 table `sTypoLineGap` field.                                                                                                                                                                                                                                                                           |
| openTypeOS2WinAscent          | non-negative integer | Ascender value. Corresponds to the OpenType OS/2 table `usWinAscent` field.                                                                                                                                                                                                                                                                            |
| openTypeOS2WinDescent         | non-negative integer | Descender value. Corresponds to the OpenType OS/2 table `usWinDescent` field.                                                                                                                                                                                                                                                                          |
| openTypeOS2Type               | list                 | A list of bit numbers indicating the embedding type. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table `fsType` field.                                                                                                                                                                             |
| openTypeOS2SubscriptXSize     | integer              | Subscript horizontal font size. Corresponds to the OpenType OS/2 table `ySubscriptXSize` field.                                                                                                                                                                                                                                                        |
| openTypeOS2SubscriptYSize     | integer              | Subscript vertical font size. Corresponds to the OpenType OS/2 table `ySubscriptYSize` field.                                                                                                                                                                                                                                                          |
| openTypeOS2SubscriptXOffset   | integer              | Subscript x offset. Corresponds to the OpenType OS/2 table `ySubscriptXOffset` field.                                                                                                                                                                                                                                                                  |
| openTypeOS2SubscriptYOffset   | integer              | Subscript y offset. Corresponds to the OpenType OS/2 table `ySubscriptYOffset` field.                                                                                                                                                                                                                                                                  |
| openTypeOS2SuperscriptXSize   | integer              | Superscript horizontal font size. Corresponds to the OpenType OS/2 table `ySuperscriptXSize` field.                                                                                                                                                                                                                                                    |
| openTypeOS2SuperscriptYSize   | integer              | Superscript vertical font size. Corresponds to the OpenType OS/2 table `ySuperscriptYSize` field.                                                                                                                                                                                                                                                      |
| openTypeOS2SuperscriptXOffset | integer              | Superscript x offset. Corresponds to the OpenType OS/2 table `ySuperscriptXOffset` field.                                                                                                                                                                                                                                                              |
| openTypeOS2SuperscriptYOffset | integer              | Superscript y offset. Corresponds to the OpenType OS/2 table `ySuperscriptYOffset` field.                                                                                                                                                                                                                                                              |
| openTypeOS2StrikeoutSize      | integer              | Strikeout size. Corresponds to the OpenType OS/2 table `yStrikeoutSize` field.                                                                                                                                                                                                                                                                         |
| openTypeOS2StrikeoutPosition  | integer              | Strikeout position. Corresponds to the OpenType OS/2 table `yStrikeoutPosition` field.                                                                                                                                                                                                                                                                 |

##### Notes

[The OpenType OS/2 table specification.]
[The Panose specification.]

1.  `xAvgCharWidth` should be calculated by the authoring tool.
2.  `sFamilyClass` is not supported.
3.  `fsSelection` can be derived from the generic *styleMapStyleName* attribute. (See question below.)
4.  `usFirstCharIndex` should be calculated by the authoring tool.
5.  `usLastCharIndex` should be calculated by the authoring tool.
6.  `sxHeight` is found at the generic *xHeight* attribute.
7.  `sCapHeight` is found at the generic *capHeight* attribute.
8.  `usDefaultChar` should be calculated by the authoring tool. OpenType fonts are required to have a .notdef character for fallback.
9.  `usBreakChar` should be calculated by the authoring tool.
10. `usMaxContext` should be calculated by the authoring tool.

#### OpenType vhea Table Fields

| key                           | value type | description                                                                            |
|-------------------------------|------------|----------------------------------------------------------------------------------------|
| openTypeVheaVertTypoAscender  | integer    | Ascender value. Corresponds to the OpenType vhea table `vertTypoAscender` field.       |
| openTypeVheaVertTypoDescender | integer    | Descender value. Corresponds to the OpenType vhea table `vertTypoDescender` field.     |
| openTypeVheaVertTypoLineGap   | integer    | Line gap value. Corresponds to the OpenType vhea table `vertTypoLineGap` field.        |
| openTypeVheaCaretSlopeRise    | integer    | Caret slope rise value. Corresponds to the OpenType vhea table `caretSlopeRise` field. |
| openTypeVheaCaretSlopeRun     | integer    | Caret slope run value. Corresponds to the OpenType vhea table `caretSlopeRun` field.   |
| openTypeVheaCaretOffset       | integer    | Caret offset value. Corresponds to the OpenType vhea table `caretOffset` field.        |

##### Notes

[The OpenType vhea table specification]

1.  `advanceHeightMax` should be calculated by the authoring tool.
2.  `minTopSideBearing` should be calculated by the authoring tool.
3.  `minBottomSideBearing` should be calculated by the authoring tool.
4.  `yMaxExtent` should be calculated by the authoring tool.
5.  `metricDataFormat` should be set by the authoring tool.
6.  `numberOfHMetrics` should be calculated by the authoring tool.

#### PostScript Specific Data

| key                           | value type       | description                                                                                                                                                                                                                         |
|-------------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| postscriptFontName            | string           | Name to be used for the `FontName` field in Type 1/CFF table.                                                                                                                                                                       |
| postscriptFullName            | string           | Name to be used for the `FullName` field in Type 1/CFF table.                                                                                                                                                                       |
| postscriptSlantAngle          | integer or float | Artificial slant angle. This must be an angle in counter-clockwise degrees from the vertical.                                                                                                                                       |
| postscriptUniqueID            | integer          | A unique ID number as defined in the Type 1/CFF specification.                                                                                                                                                                      |
| postscriptUnderlineThickness  | integer or float | Underline thickness value. Corresponds to the Type 1/CFF/post table `UnderlineThickness` field.                                                                                                                                     |
| postscriptUnderlinePosition   | integer or float | Underline position value. Corresponds to the Type 1/CFF/post table `UnderlinePosition` field.                                                                                                                                       |
| postscriptIsFixedPitch        | boolean          | Indicates if the font is monospaced. An authoring tool could calculate this automatically, but the designer may wish to override this setting. This corresponds to the Type 1/CFF `isFixedPitched` field                            |
| postscriptBlueValues          | list             | A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF BlueValues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification.       |
| postscriptOtherBlues          | list             | A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF OtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification.       |
| postscriptFamilyBlues         | list             | A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF FamilyBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification.      |
| postscriptFamilyOtherBlues    | list             | A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF FamilyOtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. |
| postscriptStemSnapH           | list             | List of horizontal stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF `StemSnapH` field.                                             |
| postscriptStemSnapV           | list             | List of vertical stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF `StemSnapV` field.                                               |
| postscriptBlueFuzz            | integer or float | BlueFuzz value. This corresponds to the Type 1/CFF `BlueFuzz` field.                                                                                                                                                                |
| postscriptBlueShift           | integer or float | BlueShift value. This corresponds to the Type 1/CFF `BlueShift` field.                                                                                                                                                              |
| postscriptBlueScale           | float            | BlueScale value. This corresponds to the Type 1/CFF `BlueScale` field.                                                                                                                                                              |
| postscriptForceBold           | boolean          | Indicates how the Type 1/CFF `ForceBold` field should be set.                                                                                                                                                                       |
| postscriptDefaultWidthX       | integer or float | Default width for glyphs.                                                                                                                                                                                                           |
| postscriptNominalWidthX       | integer or float | Nominal width for glyphs.                                                                                                                                                                                                           |
| postscriptWeightName          | string           | A string indicating the overall weight of the font. This corresponds to the Type 1/CFF Weight field. It should be in sync with the `openTypeOS2WeightClass` value.                                                                  |
| postscriptDefaultCharacter    | string           | The name of the glyph that should be used as the default character in PFM files.                                                                                                                                                    |
| postscriptWindowsCharacterSet | integer          | The Windows character set. The values are defined below.                                                                                                                                                                            |

##### postscriptWindowsCharacterSet Options

|     |                  |
|-----|------------------|
| 1   | ANSI             |
| 2   | Default          |
| 3   | Symbol           |
| 4   | Macintosh        |
| 5   | Shift JIS        |
| 6   | Hangul           |
| 7   | Hangul (Johab)   |
| 8   | GB2312           |
| 9   | Chinese BIG5     |
| 10  | Greek            |
| 11  | Turkish          |
| 12  | Vietnamese       |
| 13  | Hebrew           |
| 14  | Arabic           |
| 15  | Baltic           |
| 16  | Bitstream        |
| 17  | Cyrillic         |
| 18  | Thai             |
| 19  | Eastern European |
| 20  | OEM              |

##### Notes

[The OpenType post table specification.]
[The Postscript Type 1 specification.]
[The CFF specification.]

1.  These fields are a combination of fields in the OpenType post and CFF tables as well as the Type 1 format.
2.  The post table `minMemType42, maxMemType42, minMemType1` and `maxMemType1` fields should be set by the authoring tool.
3.  The Type 1/CFF `StdHW` and `StdVW` fields can be derived by taking the first value from the `postscriptStemSnapH` and `postscriptStemSnapV` lists.
4.  The Type 1/CFF `version` field can be derived from the generic `versionMajor` and `versionMinor` attributes.
5.  The Type 1/CFF `notice` field is found at the generic `copyright` attribute.
6.  The Type 1/CFF `FamilyName` field can be derived from the generic `familyName` attribute.
7.  If `postscriptFullName` is not given, the Type 1/CFF `FullName` field can be created by combining the generic `familyName` and `styleName` attributes.
8.  The Type 1/CFF/post table `italicAngle` field can be found at the generic `italicAngle` attribute.

#### Macintosh FOND Resource Data

| key                   | value type | description                                                        |
|-----------------------|------------|--------------------------------------------------------------------|
| macintoshFONDFamilyID | integer    | Family ID number. Corresponds to the ffFamID in the FOND resource. |
| macintoshFONDName     | string     | Font name for the FOND resource.                                   |

##### Notes

[Adobe FOND Specification]
[Apple FOND Resource Specification]
[Apple Font Family Record Specification]

#### WOFF Data

Many of these fields *can* be populated from generic elements, but since WOFF is a wrapper format they *may not* always be duplicated. As such, all of the WOFF fields are unique key/value pairs. All of these fields, and the sub-fields that they contain, are optional.

| key                     | value type           | description                                                                                                                                                             |
|-------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| woffMajorVersion        | non-negative integer | Major version of the font.                                                                                                                                              |
| woffMinorVersion        | non-negative integer | Minor version of the font.                                                                                                                                              |
| woffMetadataUniqueID    | dictionary           | Identification string. Corresponds to the WOFF `uniqueid`. The dictionary must follow the WOFF Metadata Unique ID Record structure.                                     |
| woffMetadataVendor      | dictionary           | Font vendor. Corresponds to the WOFF `vendor` element. The dictionary must follow the the WOFF Metadata Vendor Record structure.                                        |
| woffMetadataCredits     | dictionary           | Font credits. Corresponds to the WOFF `credits` element. The dictionary must follow the WOFF Metadata Credits Record structure.                                         |
| woffMetadataDescription | dictionary           | Font description. Corresponds to the WOFF `description` element. The dictionary must follow the WOFF Metadata Description Record structure.                             |
| woffMetadataLicense     | dictionary           | Font description. Corresponds to the WOFF `license` element. The dictionary must follow the WOFF Metadata License Record structure.                                     |
| woffMetadataCopyright   | dictionary           | Font copyright. Corresponds to the WOFF `copyright` element. The dictionary must follow the WOFF Metadata Copyright Record structure.                                   |
| woffMetadataTrademark   | dictionary           | Font trademark. Corresponds to the WOFF `trademark` element. The dictionary must follow the WOFF Metadata Trademark Record structure.                                   |
| woffMetadataLicensee    | dictionary           | Font licensee. Corresponds to the WOFF `licensee` element. The dictionary must follow the WOFF Metadata Licensee Record structure.                                      |
| woffMetadataExtensions  | list                 | List of metadata extension records. The dictionaries must follow the WOFF Metadata Extension Record structure. There must be at least one extension record in the list. |

##### WOFF Metadata Unique ID Record

The record is stored as dictionary of the following format.

| key | value type | description               |
|-----|------------|---------------------------|
| id  | string     | The id. This is required. |

##### WOFF Metadata Vendor Record

The record is stored as dictionary of the following format.

| key   | value type | description                                                                                                                     |
|-------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| name  | string     | Font vendor. Corresponds to the WOFF `vendor` element `name` attribute. This is required.                                       |
| url   | string     | Font vendor URL. Corresponds to the WOFF `vendor` element `url` attribute. This is optional.                                    |
| dir   | string     | Writing direction. The options are *ltr* and *rtl*. Corresponds to the WOFF `vendor` element `dir` attribute. This is optional. |
| class | string     | Class tokens. Corresponds to the WOFF `vendor` element `class` attribute. This is optional.                                     |

##### WOFF Metadata Credits Record

The record is stored as dictionary of the following format.

| key     | value type | description                                                                                                                                                                 |
|---------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| credits | list       | Font credits. Corresponds to the WOFF `credits` element. The items in the list must follow the WOFF Credit Record format. The list must contain at least one credit record. |

##### WOFF Metadata Credit Record

The record is stored as dictionary of the following format.

| key   | value type | description                                                                                                                     |
|-------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| name  | string     | The name for the credit. Corresponds to the WOFF `credit` element `name` attribute. This is required.                           |
| url   | string     | The url for the credit. Corresponds to the WOFF `credit` element `url` attribute. This is optional.                             |
| role  | string     | The role for the credit. Corresponds to the WOFF `credit` element `role` attribute. This is optional.                           |
| dir   | string     | Writing direction. The options are *ltr* and *rtl*. Corresponds to the WOFF `credit` element `dir` attribute. This is optional. |
| class | string     | Class tokens. Corresponds to the WOFF `credit` element `class` attribute. This is optional.                                     |

##### WOFF Metadata Description Record

The record is stored as dictionary of the following format.

| key  | value type | description                                                                                                 |
|------|------------|-------------------------------------------------------------------------------------------------------------|
| url  | string     | A URL for the description. Corresponds to the WOFF `description` element `url` attribute. This is optional. |
| text | list       | A list of WOFF Metadata Text Records for the description. This list must contain at least one text record.  |

##### WOFF Metadata License Record

The record is stored as dictionary of the following format.

| key  | value type | description                                                                                                |
|------|------------|------------------------------------------------------------------------------------------------------------|
| url  | string     | A URL for the license. Corresponds to the WOFF `license` element `url` attribute. This is optional.        |
| id   | string     | Ad ID for the license. Corresponds to the WOFF `license` element `id` attribute. This is optional.         |
| text | list       | A list of WOFF Metadata Text Records for the description. This list must contain at least one text record. |

##### WOFF Metadata Copyright Record

The record is stored as dictionary of the following format.

| key  | value type | description                                                                                              |
|------|------------|----------------------------------------------------------------------------------------------------------|
| text | list       | A list of WOFF Metadata Text Records for the copyright. This list must contain at least one text record. |

##### WOFF Metadata Trademark Record

The record is stored as dictionary of the following format.

| key  | value type | description                                                                                              |
|------|------------|----------------------------------------------------------------------------------------------------------|
| text | list       | A list of WOFF Metadata Text Records for the trademark. This list must contain at least one text record. |

##### WOFF Metadata Licensee Record

The record is stored as dictionary of the following format.

| key   | value type | description                                                                                                                     |
|-------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| name  | string     | The licensee. Corresponds to the WOFF `licensee` element `name` attribute. This is required.                                    |
| dir   | string     | Writing direction. The options are *ltr* and *rtl*. Corresponds to the WOFF `vendor` element `dir` attribute. This is optional. |
| class | string     | Class tokens. Corresponds to the WOFF `licensee` element `class` attribute. This is optional.                                   |

##### WOFF Metadata Text Record

The record is stored as dictionary of the following format.

| key      | value type | description                                                                                                                   |
|----------|------------|-------------------------------------------------------------------------------------------------------------------------------|
| text     | string     | The text for the record. This is required.                                                                                    |
| language | string     | Language. Corresponds to the WOFF `text` element `xml:lang` attribute. This is optional.                                      |
| dir      | string     | Writing direction. The options are *ltr* and *rtl*. Corresponds to the WOFF `text` element `dir` attribute. This is optional. |
| class    | string     | Class tokens. Corresponds to the WOFF `text` element `class` attribute. This is optional.                                     |

##### WOFF Metadata Extension Record

The records are stored as dictionaries of the following format.

| key   | value type | description                                                                                   |
|-------|------------|-----------------------------------------------------------------------------------------------|
| id    | string     | The id for the extension. This is optional.                                                   |
| names | list       | List of WOFF Metadata Extension Name Records.                                                 |
| items | list       | List of WOFF Metadata Extension Item Records. The list must contain at least one item record. |

##### WOFF Metadata Extension Item Record

The records are stored as dictionaries of the following format.

| key    | value type | description                                                                                     |
|--------|------------|-------------------------------------------------------------------------------------------------|
| id     | string     | The id of the item record.                                                                      |
| names  | list       | List of WOFF Metadata Extension Name Records. The list must contain at least one name record.   |
| values | list       | List of WOFF Metadata Extension Value Records. The list must contain at least one value record. |

##### WOFF Metadata Extension Name Record

The records are stored as dictionaries of the following format.

| key      | value type | description                                                                                                                             |
|----------|------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| text     | string     | The name of the name record. This is required.                                                                                          |
| language | string     | The language of the name record. This is optional.                                                                                      |
| dir      | string     | Writing direction. The options are *ltr* and *rtl*. Corresponds to the WOFF extension `name` element `dir` attribute. This is optional. |
| class    | string     | Class tokens. Corresponds to the WOFF extension `name` element `class` attribute. This is optional.                                     |

##### WOFF Metadata Extension Value Record

The records are stored as dictionaries of the following format.

| key      | value type | description                                                                                                                              |
|----------|------------|------------------------------------------------------------------------------------------------------------------------------------------|
| text     | string     | The value of the value record. This is required.                                                                                         |
| language | string     | The language of the value record. This is optional.                                                                                      |
| dir      | string     | Writing direction. The options are *ltr* and *rtl*. Corresponds to the WOFF extension `value` element `dir` attribute. This is optional. |
| class    | string     | Class tokens. Corresponds to the WOFF extension `value` element `class` attribute. This is optional.                                     |

##### Notes

[The WOFF specification]

Several metadata elements in the WOFF specification allow for `<div>` and `<span>` child elements. These must be stored as raw text in appropriate `text` fields in the defined above. For example, for this WOFF metadata:

```xml
<description>
  <text xml:lang="en">
    <div>
      <span dir="ltr">description</span>
    </div>
  </text>
</description>
```

Would be represented like this (string line broken only for formatting resons):

```xml
<key>woffMetadataDescription</key>
<dict>
  <key>text</key>
  <array>
    <dict>
      <key>language</key>
      <string>en</string>
      <key>text</key>
      <string>&lt;div&gt;&lt;span dir=&quot;ltr&quot;&gt;
      description&lt;/span&gt;&lt;/div&gt;</string>
    </dict>
  </array>
</dict>
```

#### Guidelines

| key        | value type | description                                                                                                     |
|------------|------------|-----------------------------------------------------------------------------------------------------------------|
| guidelines | list       | A list of guideline definitions that apply to all glyphs in all layers in the font. This attribute is optional. |

##### Guideline Format

The guidelines are stored as dictionaries of the following format.

| key        | value type       | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | default value |
|------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| x          | integer or float | The 'x' coordinate. Optional if `y` is provided and `angle` is not provided. See below for details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | None          |
| y          | integer or float | The 'y' coordinate. Optional if `x` is provided and `angle` is not provided. See below for details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | None          |
| angle      | integer or float | The angle of the guideline. This must be an angle between 0 and 360 degrees in a clockwise direction from the horizontal. If `x` or `y` are not specified, `angle` must not be specified. See below for details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | None.         |
| name       | string           | An arbitrary name for the guideline. This attribute is optional.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | no name       |
| color      | string           | The color that should be applied to the guideline. The format follows the [color definition] standard. This attribute is optional.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | no color      |
| identifier | string           | Unique identifier for the guideline. This attribute is not required and should only be added to guidelines as needed. However, once an identifier has been assigned to a guideline it must not be unnecessarily removed or changed. Identifiers may be changed in incoming guidelines during editing operations such as "paste," but they should be maintained unless a duplicate identifier will be created. The identifier value must be unique within the fontinfo.plist guidelines list that the guideline belongs to but it is not required to be unique among the identifiers assigned to guidelines in glyphs. The identifier specification is detailed in the [conventions]. | no identifier |

The guideline extends along `angle` to infinity in both directions out of the point defined by `x` and `y`. If `y` and `angle` are omitted, the element represents a vertical guideline. If `x` and `angle` are omitted, the element represents a horizontal guideline.

  [The OpenType gasp table specification.]: http://www.microsoft.com/typography/otspec/gasp.htm
  [The OpenType head table specification.]: http://www.microsoft.com/typography/otspec/head.htm
  [The OpenType hhea table specification]: http://www.microsoft.com/typography/otspec/hhea.htm
  [The OpenType name table specification.]: http://www.microsoft.com/typography/otspec/name.htm
  [The OpenType OS/2 table specification.]: http://www.microsoft.com/typography/otspec/os2.htm
  [The Panose specification.]: http://www.panose.com/ProductsServices/pan1.aspx
  [The OpenType vhea table specification]: http://www.microsoft.com/typography/otspec/vhea.htm
  [The OpenType post table specification.]: http://www.microsoft.com/typography/otspec/post.htm
  [The Postscript Type 1 specification.]: http://partners.adobe.com/public/developer/en/font/T1_SPEC.PDF
  [The CFF specification.]: http://www.adobe.com/devnet/font/pdfs/5176.CFF.pdf
  [Adobe FOND Specification]: http://www.adobe.com/devnet/font/pdfs/0091.Mac_Fond.pdf
  [Apple FOND Resource Specification]: http://developer.apple.com/documentation/mac/Text/Text-269.html
  [Apple Font Family Record Specification]: http://developer.apple.com/documentation/mac/Text/Text-215.html
  [The WOFF specification]: http://www.w3.org/TR/WOFF
  [XML Property List]: ../conventions.html#propertylist
  [color definition]: ../conventions.html#colors
  [conventions]: ../conventions.html#identifiers
