---
layout: default
navigation: true
order: 300
title: UFO 3
tree:
    - metainfo.plist
    - fontinfo.plist
    - groups.plist
    - kerning.plist
    - features.fea
    - lib.plist
    - layercontents.plist
    - glyphs
    - glyphs/contents.plist
    - glyphs/layerinfo.plist
    - glyphs/glif
    - images
    - data
    - conventions
---


A UFO is a directory representing font data with one or more glyph layers.

### Terminology

The terms "must", "must not", "required", "shall", "shall not", "should", "should not", "recommended", "may", and "optional" used throughout this specification conform to [RFC 2119].

The term "authoring tool" is used throughout this specification to refer to tools that read and write UFOs. Authoring tools may take many forms:

1.  A font editor that uses UFO as its native file format.
2.  A tool that allows for importing data from or exporting data to a UFO.
3.  A programming library for reading or writing UFO data.
4.  A script for modifying a UFO.

This list is not exclusive.

### File Structure

UFO 3 follows this file structure:

{: .filediagram}
- {: .filediagramDirectory}*.ufo
  - metainfo.plist
  - fontinfo.plist
  - groups.plist
  - kerning.plist
  - lib.plist
  - layercontents.plist
  - {: .filediagramDirectory}glyphs
    - contents.plist
    - layerinfo.plist
    - *.glif
  - {: .filediagramDirectory}images
    - *.png
  - {: .filediagramDirectory}data


Each of the files and directories have unique meanings, purposes and data structures:

| [metainfo.plist](metainfo.plist) | Format version, creator, etc. |
| [fontinfo.plist](fontinfo.plist) | Various font info data. |
| [groups.plist](groups.plist) | Glyph group definitions. |
| [kerning.plist](kerning.plist) | Kerning data. |
| [features.fea](features.fea) | OpenType feature definitions. |
| [lib.plist](lib.plist) | Arbitrary custom data. |
| [layercontents.plist](layercontents.plist) | Glyphs directory name to layer name mapping. |
| [glyphs*](glyphs) | A directory containing a glyph set representing a [layer](#glyph-layers). |
| glyphs*/[contents.plist](glyphs/contents.plist) | File name to glyph name mapping. |
| glyphs*/[layerinfo.plist](glyphs/layerinfo.plist) | Information about the layer. |
| glyphs*/[*.glif](glyphs/glif) | A glyph definition. |
| [images](images) | A directory containing images referenced by glyphs. |
| [data](data) | Arbitrary custom data in a quantity or structure that can't be stored in lib.plist. |

### Glyph Layers

The UFO supports layered glyphs. These layers can be used for anything—the common *foreground+background* drawing environment, multi-layered fonts, glyph revision history and so on. The layering structure is designed to be conceptually unrestricted.

Layers are implemented with a series of glyph sets within the UFO. Each glyph set represents one layer for all glyphs in the font. Each glyph set is stored in its own “glyphs” directory. There is one required glyph set that represents the primary outline source of the glyph. This glyph set should be stored in the “glyphs” directory. Additional layers are stored in other directories as defined in the [layercontents.plist] documentation.

#### Character Mapping

A character to glyph mapping for the UFO may be created by skimming the GLIF files in the required layer and retrieving the first Unicode element, if present. There is no guarantee that a single Unicode value will not be used in more than one GLIF. All authoring tools may handle these conflicts in their own particular way. Likewise, a glyph with the same name in more than one layer may have different Unicode values in each layer. Authoring tools using the native file model should maintain the different Unicode values. Import/expert model authoring tools may or may not retain the Unicode values on the layers that are not the required layer. All of this should be done in accordance with the policies outlined in the [Authoring Tool Guidelines].

# Changes from UFO 2

In general, there have been many editorial changes that don't affect the content. The term "authoring tool" has been used to make the references to applications, scripts, etc. consistent. Various conformance statements were modified to make them consistent with RFC 2119.

This list is for reference only as it may leave some changes out. The sub-sections of the specification overrule this list.

### metainfo.plist

The *formatVersion* was bumped to 3.

### fontinfo.plist

Support for specific name id, platform, platform encoding and language name table entries was added.

Support for WOFF metadata was added.

The value types for the following keys were clarified to be more consistent with the specifications they reference: versionMinor, unitsPerEm, openTypeHeadLowestRecPPEM, openTypeHheaAscender, openTypeHheaDescender, openTypeHheaLineGap, openTypeHheaCaretOffset, openTypeOS2WeightClass, openTypeOS2WinAscent, openTypeOS2WinDescent, openTypeOS2TypoAscender, openTypeOS2TypoDescender, openTypeOS2TypoLineGap, openTypeOS2WinAscent, openTypeOS2WinDescent, openTypeOS2SubscriptXSize, openTypeOS2SubscriptYSize, openTypeOS2SubscriptXOffset, openTypeOS2SubscriptYOffset, openTypeOS2SuperscriptXSize, openTypeOS2SuperscriptYSize, openTypeOS2SuperscriptXOffset, openTypeOS2SuperscriptYOffset, openTypeOS2StrikeoutSize, openTypeOS2StrikeoutPosition, openTypeVheaVertTypoAscender, openTypeVheaVertTypoDescender, openTypeVheaVertTypoLineGap and openTypeVheaCaretOffset.

Support for font-level guidelines was added.

Support for the gasp table was added.

### groups.plist

Behavior with regard to kerning groups was defined.

Added a mechanism for standardizing group names.

### kerning.plist

Added information about writing direction.

Information about the new kerning groups was added.

Added extensive information about kerning pair types. The information is applicable to UFO 1 and UFO 2, but it was not written as a formal part of the spec.

Added information about converting UFO 1 and UFO 2 kerning to UFO 3 kerning.

### features.fea

The "should be a plain text file" from UFO 2 was changed to "must be a plain text file."

### lib.plist

Added a mechanism for standardizing lib keys.

Added a standard place for glyph order storage.

### layercontents.plist

This is a new file.

### glyphs

More than one glyphs directory is allowed. Each directory is a layer.

### glyphs/contents.plist

The sample glyph name to file name algorithm was moved to the conventions page and it was abstracted and expanded to be more robust.

Information about the allowed characters in glyph names was added.

The information about the file name being stored in the property list was slightly updated to be more verbose.

### glyphs/layerinfo.plist

This is a new file.

### glyphs/GLIF

The version number was increased to 2.

#### Contour

A new identifier attribute was added.

#### Component

A new identifier attribute was added.

A new rule explaining how components relate to layers was added.

#### Point

A new identifier attribute was added.

Removed references to Super Bezier.

#### Image

A new image element was added.

#### Guideline

A new guideline element was added.

#### Anchor

A new anchor element was added.

#### Lib

Added a mechanism for standardizing lib keys.

Added a standard place for glyph mark color storage.

### images

The images directory was added.

### data

The data directory was added.

# Important corrections

#### Guideline

The guideline’s angle attribute was changed from being measured in the clockwise direction to the counter-clockwise direction.

  [RFC 2119]: http://www.ietf.org/rfc/rfc2119.txt
  [metainfo.plist]: metainfo.plist
  [fontinfo.plist]: fontinfo.plist
  [groups.plist]: groups.plist
  [kerning.plist]: kerning.plist
  [features.fea]: features.fea
  [lib.plist]: lib.plist
  [layercontents.plist]: layercontents.plist
  [glyphs\*]: glyphs
  [layer]: #glyphlayers
  [contents.plist]: glyphs/contents.plist
  [layerinfo.plist]: glyphs/layerinfo.plist
  [\*.glif]: glyphs/glif.plist
  [images]: images
  [data]: data
  [Authoring Tool Guidelines]: ../../atguidelines
