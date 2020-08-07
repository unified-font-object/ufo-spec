---
layout: default
title: fontinfo.plist
---

{: .fileformat}
| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains information about the font itself, such as naming and dimensions. This file is optional. Not all values are required for a proper file.

#### Changes from UFO 1

The key value pairs in the property list were modified and significantly expanded for UFO 2. The design of the structure follows these rules:

1.  All keys should be tagged for the format and/or table that they represent. For example, *openTypeHheaAscender*.
2.  If data can be used for more than one format and/or table, it is considered *generic* and the format specific tag is removed. For example, *familyName*.

In several cases, data moved to generic keys can be used in a controlled, slightly altered form for format specific fields. In these cases, information about how this can be done is provided. These are merely suggestions for the sake of clarity. Compiler developers are free to interpret these as they wish.

## Specification

#### Generic Identification Information

{: .name-type-description}
| key | type | description |
|--|--|--|
| familyName | string | Family name. |
| styleName | string | Style name. |
| styleMapFamilyName | string | Family name used for bold, italic and bold italic style mapping. |
| styleMapStyleName | string | Style map style. The possible values are *regular*, *italic*, *bold* and *bold italic*. These are case sensitive. |
| versionMajor | integer | Major version. |
| versionMinor | integer | Minor version. |
| year | integer | The year the font was created. This attribute is deprecated as of version 2. It's presence should not be relied upon by applications. However, it may occur in a font's info so applications should preserve it if present. |

#### Generic Legal Information

{: .name-type-description}
| key | type | description |
|--|--|--|
| copyright | string | Copyright statement. |
| trademark | string | Trademark statement. |

#### Generic Dimension Information

{: .name-type-description}
| key | type | description |
|--|--|--|
| unitsPerEm | integer or float | Units per em. |
| descender | integer or float | Descender value. |
| xHeight | integer or float | x-height value. |
| capHeight | integer or float | Cap height value. |
| ascender | integer or float | Ascender value. |
| italicAngle | float | Italic angle. |

#### Generic Miscellaneous Information

{: .name-type-description}
| key | type | description |
|--|--|--|
| note | string | Arbitrary note about the font. |

#### OpenType head Table Fields

{: .name-type-description}
| key | type | description |
|--|--|--|
| openTypeHeadCreated | string | Creation date. Expressed as a string of the format "YYYY/MM/DD HH:MM:SS". "YYYY/MM/DD" is year/month/day. The month should be in the range 1-12 and the day should be in the range 1-end of month. "HH:MM:SS" is hour:minute:second. The hour should be in the range 0:23. The minute and second should each be in the range 0-59. |
| openTypeHeadLowestRecPPEM | integer or float | Smallest readable size in pixels. Corresponds to the OpenType head table lowestRecPPEM field. |
| openTypeHeadFlags | number list | A list of bit numbers indicating the flags. The bit numbers are listed in the OpenType head specification. Corresponds to the OpenType head table flags field. |

##### Notes

<a href="http://www.microsoft.com/typography/otspec/head.htm" target="_blank">The OpenType head table specification.</a>

1.  *fontRevision* can be derived from the generic *versionMajor* and *versionMinor* attributes.
2.  *checkSumAdjustment* should be calculated by the compiler.
3.  *magicNumber* should be set by the compiler.
4.  *unitsPerEm* is found at the generic *unitsPerEm* attribute.
5.  *created* can be calculated by subtracting the *12:00 midnight, January 1, 1904* (as specified in the head table documentation) from the date stored at *openTypeHeadCreated*.
6.  *modified* should be set by the compiler.
7.  *xMin, yMin, xMax* and *yMax* should be calculated by the compiler.
8.  *macStyle* can be derived from the generic *styleMapStyleName* attribute.
9.  *indexToLocFormat* should be set by the compiler.
10. *glyphDataFormat* should be set by the compiler.

#### OpenType hhea Table Fields

{: .name-type-description}
| key | type | description |
|--|--|--|
| openTypeHheaAscender | integer or float | Ascender value. Corresponds to the OpenType hhea table Ascender field. |
| openTypeHheaDescender | integer or float | Descender value. Corresponds to the OpenType hhea table Descender field. |
| openTypeHheaLineGap | integer or float | Line gap value. Corresponds to the OpenType hhea table LineGap field. |
| openTypeHheaCaretSlopeRise | integer | Caret slope rise value. Corresponds to the OpenType hhea table caretSlopeRise field. |
| openTypeHheaCaretSlopeRun | integer | Caret slope run value. Corresponds to the OpenType hhea table caretSlopeRun field. |
| openTypeHheaCaretOffset | integer or float | Caret offset value. Corresponds to the OpenType hhea table caretOffset field. |

##### Notes

<a href="http://www.microsoft.com/typography/otspec/hhea.htm" target="_blank">The OpenType hhea table specification</a>

1.  *advanceWidthMax* should be calculated by the compiler.
2.  *minLeftSideBearing* should be calculated by the compiler.
3.  *minRightSideBearing* should be calculated by the compiler.
4.  *xMaxExtent* should be calculated by the compiler.
5.  *metricDataFormat* should be set by the compiler.
6.  *numberOfHMetrics* should be calculated by the compiler.

#### OpenType Name Table Fields

{: .name-type-description}
| key | type | description |
|--|--|--|
| openTypeNameDesigner | string | Designer name. Corresponds to the OpenType name table name ID 9. |
| openTypeNameDesignerURL | string | URL for the designer. Corresponds to the OpenType name table name ID 12. |
| openTypeNameManufacturer | string | Manufacturer name. Corresponds to the OpenType name table name ID 8. |
| openTypeNameManufacturerURL | string | Manufacturer URL. Corresponds to the OpenType name table name ID 11. |
| openTypeNameLicense | string | License text. Corresponds to the OpenType name table name ID 13. |
| openTypeNameLicenseURL | string | URL for the license. Corresponds to the OpenType name table name ID 14. |
| openTypeNameVersion | string | Version string. Corresponds to the OpenType name table name ID 5. |
| openTypeNameUniqueID | string | Unique ID string. Corresponds to the OpenType name table name ID 3. |
| openTypeNameDescription | string | Description of the font. Corresponds to the OpenType name table name ID 10. |
| openTypeNamePreferredFamilyName | string | Preferred family name. Corresponds to the OpenType name table name ID 16. |
| openTypeNamePreferredSubfamilyName | string | Preferred subfamily name. Corresponds to the OpenType name table name ID 17. |
| openTypeNameCompatibleFullName | string | Compatible full name. Corresponds to the OpenType name table name ID 18. |
| openTypeNameSampleText | string | Sample text. Corresponds to the OpenType name table name ID 20. |
| openTypeNameWWSFamilyName | string | WWS family name. Corresponds to the OpenType name table name ID 21. |
| openTypeNameWWSSubfamilyName | string | WWS Subfamily name. Corresponds to the OpenType name table name ID 22. |

##### Notes

<a href="http://www.microsoft.com/typography/otspec/name.htm" target="_blank">The OpenType name table specification.</a>

1.  *Name ID 0 (copyright)* is found at the generic *copyright* attribute.
2.  *Name ID 1 (font family name)* is found at the generic *styleMapFamilyName* attribute.
3.  *Name ID 2 (font subfamily name)* can be interpreted from the generic *styleMapStyleName* attribute.
4.  *Name ID 4 (full font name)* can be created from the generic *styleMapFamilyName* and *styleMapStyleName* attributes following the rules defined in the specification.
5.  *Name ID 6 (Postscript name)* can be found at *postscriptFontName*. This should follow the rules defined in the specification.
6.  *Name ID 7 (trademark)* is found at the generic *trademark* attribute.
7.  To reiterate the point stated above, these notes are merely provided for clarity. Compilers can and should follow their own recipes for creating the name table. These notes make no considerations for platform specific variations in or application specific limitations on the strings.

#### OpenType OS/2 Table Fields

{: .name-type-description}
| key | type | description |
|--|--|--|
| openTypeOS2WidthClass | integer | Width class value. Must be in the range 1-9. Corresponds to the OpenType OS/2 table usWidthClass field. |
| openTypeOS2WeightClass | integer | Weight class value. Must be a positive integer. Corresponds to the OpenType OS/2 table usWeightClass field. |
| openTypeOS2Selection | number list | A list of bit numbers indicating the bits that should be set in fsSelection. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table selection field. **Note:** Bits 0 (italic), 5 (bold) and 6 (regular) should not be set here. These bits should be taken from the generic *styleMapStyleName* attribute. |
| openTypeOS2VendorID | string | Four character identifier for the creator of the font. Corresponds to the OpenType OS/2 table achVendID field. |
| openTypeOS2Panose | number list | The list should contain 10 integers that represent the setting for each category in the Panose specification. The integers correspond with the option numbers in each of the Panose categories. This corresponds to the OpenType OS/2 table Panose field. |
| openTypeOS2FamilyClass | number list | Two integers representing the IBM font class and font subclass of the font. The first number, representing the class ID, should be in the range 0-14. The second number, representing the subclass, should be in the range 0-15. The numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table sFamilyClass field. |
| openTypeOS2UnicodeRanges | number list | A list of bit numbers that are supported Unicode ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulUnicodeRange1, ulUnicodeRange2, ulUnicodeRange3 and ulUnicodeRange4 fields. |
| openTypeOS2CodePageRanges | number list | A list of bit numbers that are supported code page ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulCodePageRange1 and ulCodePageRange2 fields. |
| openTypeOS2TypoAscender | integer or float | Ascender value. Corresponds to the OpenType OS/2 table sTypoAscender field. |
| openTypeOS2TypoDescender | integer or float | Descender value. Corresponds to the OpenType OS/2 table sTypoDescender field. |
| openTypeOS2TypoLineGap | integer or float | Line gap value. Corresponds to the OpenType OS/2 table sTypoLineGap field. |
| openTypeOS2WinAscent | integer or float | Ascender value. Corresponds to the OpenType OS/2 table usWinAscent field. |
| openTypeOS2WinDescent | integer or float | Descender value. Corresponds to the OpenType OS/2 table usWinDescent field. |
| openTypeOS2Type | number list | A list of bit numbers indicating the embedding type. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table fsType field. |
| openTypeOS2SubscriptXSize | integer or float | Subscript horizontal font size. Corresponds to the OpenType OS/2 table ySubscriptXSize field. |
| openTypeOS2SubscriptYSize | integer or float | Subscript vertical font size. Corresponds to the OpenType OS/2 table ySubscriptYSize field. |
| openTypeOS2SubscriptXOffset | integer or float | Subscript x offset. Corresponds to the OpenType OS/2 table ySubscriptXOffset field. |
| openTypeOS2SubscriptYOffset | integer or float | Subscript y offset. Corresponds to the OpenType OS/2 table ySubscriptYOffset field. |
| openTypeOS2SuperscriptXSize | integer or float | Superscript horizontal font size. Corresponds to the OpenType OS/2 table ySuperscriptXSize field. |
| openTypeOS2SuperscriptYSize | integer or float | Superscript vertical font size. Corresponds to the OpenType OS/2 table ySuperscriptYSize field. |
| openTypeOS2SuperscriptXOffset | integer or float | Superscript x offset. Corresponds to the OpenType OS/2 table ySuperscriptXOffset field. |
| openTypeOS2SuperscriptYOffset | integer or float | Superscript y offset. Corresponds to the OpenType OS/2 table ySuperscriptYOffset field. |
| openTypeOS2StrikeoutSize | integer or float | Strikeout size. Corresponds to the OpenType OS/2 table yStrikeoutSize field. |
| openTypeOS2StrikeoutPosition | integer or float | Strikeout position. Corresponds to the OpenType OS/2 table yStrikeoutPosition field. |

##### Notes

<a href="http://www.microsoft.com/typography/otspec/os2.htm" target="_blank">The OpenType OS/2 table specification.</a>
<a href="http://www.panose.com/ProductsServices/pan1.aspx" target="_blank">The Panose specification.</a>

1.  *xAvgCharWidth* should be calculated by the compiler.
2.  *sFamilyClass* is not supported.
3.  *fsSelection* can be derived from the generic *styleMapStyleName* attribute. (See question below.)
4.  *usFirstCharIndex* should be calculated by the compiler.
5.  *usLastCharIndex* should be calculated by the compiler.
6.  *sxHeight* is found at the generic *xHeight* attribute.
7.  *sCapHeight* is found at the generic *capHeight* attribute.
8.  *usDefaultChar* should be calculated by the compiler. OpenType fonts are required to have a .notdef character for fallback.
9.  *usBreakChar* should be calculated by the compiler.
10. *usMaxContext* should be calculated by the compiler.

#### OpenType vhea Table Fields

{: .name-type-description}
| key | type | description |
|--|--|--|
| openTypeVheaVertTypoAscender | integer or float | Ascender value. Corresponds to the OpenType vhea table vertTypoAscender field. |
| openTypeVheaVertTypoDescender | integer or float | Descender value. Corresponds to the OpenType vhea table vertTypoDescender field. |
| openTypeVheaVertTypoLineGap | integer or float | Line gap value. Corresponds to the OpenType vhea table vertTypoLineGap field. |
| openTypeVheaCaretSlopeRise | integer | Caret slope rise value. Corresponds to the OpenType vhea table caretSlopeRise field. |
| openTypeVheaCaretSlopeRun | integer | Caret slope run value. Corresponds to the OpenType vhea table caretSlopeRun field. |
| openTypeVheaCaretOffset | integer or float | Caret offset value. Corresponds to the OpenType vhea table caretOffset field. |

##### Notes

<a href="http://www.microsoft.com/typography/otspec/vhea.htm" target="_blank">The OpenType vhea table specification</a>

1.  *advanceHeightMax* should be calculated by the compiler.
2.  *minTopSideBearing* should be calculated by the compiler.
3.  *minBottomSideBearing* should be calculated by the compiler.
4.  *yMaxExtent* should be calculated by the compiler.
5.  *metricDataFormat* should be set by the compiler.
6.  *numberOfHMetrics* should be calculated by the compiler.

#### PostScript Specific Data

{: .name-type-description}
| key | type | description |
|--|--|--|
| postscriptFontName | string | Name to be used for the *FontName* field in Type 1/CFF table. |
| postscriptFullName | string | Name to be used for the *FullName* field in Type 1/CFF table. |
| postscriptSlantAngle | float | Artificial slant angle. |
| postscriptUniqueID | integer | A unique ID number as defined in the Type 1/CFF specification. |
| postscriptUnderlineThickness | integer or float | Underline thickness value. Corresponds to the Type 1/CFF/post table UnderlineThickness field. |
| postscriptUnderlinePosition | integer or float | Underline position value. Corresponds to the Type 1/CFF/post table UnderlinePosition field. |
| postscriptIsFixedPitch | boolean | Indicates if the font is monospaced. A compiler could calculate this automatically, but the designer may wish to override this setting. This corresponds to the Type 1/CFF isFixedPitched field |
| postscriptBlueValues | number list | A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF BlueValues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. |
| postscriptOtherBlues | number list | A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF OtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. |
| postscriptFamilyBlues | number list | A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF FamilyBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. |
| postscriptFamilyOtherBlues | number list | A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF FamilyOtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. |
| postscriptStemSnapH | number list | List of horizontal stems sorted in increasing order. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapH field. |
| postscriptStemSnapV | number list | List of vertical stems sorted in increasing order. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapV field. |
| postscriptBlueFuzz | integer or float | BlueFuzz value. This corresponds to the Type 1/CFF BlueFuzz field. |
| postscriptBlueShift | integer or float | BlueShift value. This corresponds to the Type 1/CFF BlueShift field. |
| postscriptBlueScale | float | BlueScale value. This corresponds to the Type 1/CFF BlueScale field. |
| postscriptForceBold | boolean | Indicates how the Type 1/CFF ForceBold field should be set. |
| postscriptDefaultWidthX | integer or float | Default width for glyphs. |
| postscriptNominalWidthX | integer or float | Nominal width for glyphs. |
| postscriptWeightName | string | A string indicating the overall weight of the font. This corresponds to the Type 1/CFF Weight field. It should be in sync with the openTypeOS2WeightClass value. |
| postscriptDefaultCharacter | string | The name of the glyph that should be used as the default character in PFM files. |
| postscriptWindowsCharacterSet | integer | The Windows character set. The values are defined below. |

##### postscriptWindowsCharacterSet Options

| 1 | ANSI |
| 2 | Default |
| 3 | Symbol |
| 4 | Macintosh |
| 5 | Shift JIS |
| 6 | Hangul |
| 7 | Hangul (Johab) |
| 8 | GB2312 |
| 9 | Chinese BIG5 |
| 10 | Greek |
| 11 | Turkish |
| 12 | Vietnamese |
| 13 | Hebrew |
| 14 | Arabic |
| 15 | Baltic |
| 16 | Bitstream |
| 17 | Cyrillic |
| 18 | Thai |
| 19 | Eastern European |
| 20 | OEM |

##### Notes

<a href="http://www.microsoft.com/typography/otspec/post.htm" target="_blank">The OpenType post table specification.</a><br>
<a href="http://partners.adobe.com/public/developer/en/font/T1_SPEC.PDF" target="_blank">The Postscript Type 1 specification.</a><br>
<a href="http://www.adobe.com/devnet/font/pdfs/5176.CFF.pdf" target="_blank">The CFF specification.</a><br>

1.  These fields are a combination of fields in the OpenType post and CFF tables as well as the Type 1 format.
2.  The post table *minMemType42, maxMemType42, minMemType1* and *maxMemType1* fields should be set by the compiler.
3.  The Type 1/CFF *StdHW* and *StdVW* fields can be derived by taking the first value from the *postscriptStemSnapH* and *postscriptStemSnapV* lists.
4.  The Type 1/CFF *version* field can be derived from the generic *versionMajor* and *versionMinor* attributes.
5.  The Type 1/CFF *notice* field is found at the generic *copyright* attribute.
6.  The Type 1/CFF *FamilyName* field can be derived from the generic *familyName* attribute.
7.  If *postscriptFullName* is not given, the Type 1/CFF *FullName* field can be created by combining the generic *familyName* and *styleName* attributes.
8.  The Type 1/CFF/post table *italicAngle* field can be found at the generic *italicAngle* attribute.

#### Macintosh FOND Resource Data

{: .name-type-description}
| key | type | description |
|--|--|--|
| macintoshFONDFamilyID | integer | Family ID number. Corresponds to the ffFamID in the FOND resource. |
| macintoshFONDName | String | Font name for the FOND resource. |

##### Notes

<a href="http://www.adobe.com/devnet/font/pdfs/0091.Mac_Fond.pdf" target="_blank">Adobe FOND Specification</a><br>
<a href="http://developer.apple.com/documentation/mac/Text/Text-269.html" target="_blank">Apple FOND Resource Specification</a><br>
<a href="http://developer.apple.com/documentation/mac/Text/Text-215.html" target="_blank">Apple Font Family Record Specification</a><br>

<hr class="subsection">

## Converting fontinfo.plist in UFO 1 to fontinfo.plist in UFO 2

In many cases, the attributes have been retained in the new structure. However, some attributes are stored under new keys. A few attributes need to be converted to a new data format.

| old key | new key | special conversion instructions |
|--|--|--|
| menuName | styleMapFamilyName | No special conversion needed. |
| fontStyle | styleMapStyleName | The old integer values should be converted to strings following the rules in the chart below. |
| designer | openTypeNameDesigner | No special conversion needed. |
| designerURL | openTypeNameDesignerURL | No special conversion needed. |
| createdBy | openTypeNameManufacturer | No special conversion needed. |
| vendorURL | openTypeNameManufacturerURL | No special conversion needed. |
| license | openTypeNameLicense | No special conversion needed. |
| licenseURL | openTypeNameLicenseURL | No special conversion needed. |
| ttVersion | openTypeNameVersion | No special conversion needed. |
| ttUniqueID | openTypeNameUniqueID | No special conversion needed. |
| notice | openTypeNameDescription | No special conversion needed. |
| otFamilyName | openTypeNamePreferredFamilyName | No special conversion needed. |
| otStyleName | openTypeNamePreferredSubfamilyName | No special conversion needed. |
| otMacName | openTypeNameCompatibleFullName | No special conversion needed. |
| widthName | openTypeOS2WidthClass | The old string values should be converted to integers following the rules in the chart below. |
| weightValue | openTypeOS2WeightClass | No special conversion needed. |
| ttVendor | openTypeOS2VendorID | No special conversion needed. |
| uniqueID | postscriptUniqueID | No special conversion needed. |
| fontName | postscriptFontName | No special conversion needed. |
| fullName | postscriptFullName | No special conversion needed. |
| weightName | postscriptWeightName | No special conversion needed. |
| slantAngle | postscriptSlantAngle | No special conversion needed. |
| defaultWidth | postscriptDefaultWidthX | No special conversion needed. |
| msCharSet | postscriptWindowsCharacterSet | The old bit values should be converted to integers following the rules in the chart below. |
| fondID | macintoshFONDFamilyID | No special conversion needed. |
| fondName | macintoshFONDName | No special conversion needed. |

##### Converting fontStyle to styleMapStyleName

| old value | new value |
|--|--|
| 64 | regular |
| 1 | italic |
| 32 | bold |
| 33 | bold italic |

##### Converting widthName to openTypeOS2WidthClass

| old value | new value |
|--|--|
| Ultra-condensed | 1 |
| Extra-condensed | 2 |
| Condensed | 3 |
| Semi-condensed | 4 |
| Medium (normal) | 5 |
| Semi-expanded | 6 |
| Expanded | 7 |
| Extra-expanded | 8 |
| Ultra-expanded | 9 |

##### Converting msCharSet to postscriptWindowsCharacterSet

| old value | new value |
|--|--|
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 77 | 4 |
| 128 | 5 |
| 129 | 6 |
| 130 | 7 |
| 134 | 8 |
| 136 | 9 |
| 161 | 10 |
| 162 | 11 |
| 163 | 12 |
| 177 | 13 |
| 178 | 14 |
| 186 | 15 |
| 200 | 16 |
| 204 | 17 |
| 222 | 18 |
| 238 | 19 |
| 255 | 20 |


