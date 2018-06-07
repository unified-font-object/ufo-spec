---
layout: default
title: fontinfo.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains information about the font itself, such as naming and dimensions. This file is optional. Not all values are required for a proper file.

## Specification

The property list data consists of a dictionary at the top level. The keys and values are as follows.

| key | value type | description |
|-|-|-|
| ascender | integer or float | Ascender value. |
| capHeight | integer or float | Cap height value. |
| copyright | string | Copyright statement. |
| createdBy | string | Creator of the font, for example the foundry. |
| descender | integer or float | Descender value. |
| defaultWidth | integer or float | Value for the width of new glyphs. |
| designer | string | Name of the designer |
| designerURL | string | URL for the designer. |
| familyName | string | Family name. |
| fondID | integer | Macintosh OS FOND resource number. |
| fondName | string | Macintosh OS FOND name. |
| fontName | string | Font name. |
| fontStyle | integer | Style code. 64=regular, 1=italic, 32=bold and 33=bold italic. |
| fullName | string | Full name. |
| italicAngle | float | Italic angle. |
| license | string | License text. |
| licenseURL | string | URL for the license. |
| menuName | string | Menu name. |
| msCharSet | integer | MS Char Set flag. |
| note | string | Arbitrary notes about the font. |
| notice | string | A notice about the font. |
| otFamilyName | string | OpenType specific family name. |
| otStyleName | string | OpenType specific style name. |
| otMacName | string | Macintosh and OpenType specific name. |
| slantAngle | float | Slant angle. |
| styleName | string | Style name. |
| trademark | string | Trademark statement. |
| ttUniqueID | string | Unique ID for TrueType fonts. |
| ttVendor | string | Four character vendor code. |
| ttVersion | string | TrueType version. |
| uniqueID | integer | PostScript ID number. |
| unitsPerEm | integer or float | Units per em. |
| vendorURL | string | URL for the font vendor. |
| versionMajor | integer | Major version. |
| versionMinor | integer | Minor version. |
| weightName | string | The width “name.” This corresponds with the OpenType OS/2 table usWeightClass field names. |
| weightValue | integer | Value for the weight. This corresponds with the OpenType OS/2 table usWeightClass field values. |
| widthName | string | This corresponds with the OpenType OS/2 table usWidthClass field names.