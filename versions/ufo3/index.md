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
    - GLIF
    - images
    - data
    - Conventions
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


<table>
<tr>
<td>
[metainfo.plist]
</td>
<td>
Format version, creator, etc.
</td>
</tr>
<tr>
<td>
[fontinfo.plist]
</td>
<td>
Various font info data.
</td>
</tr>
<tr>
<td>
[groups.plist]
</td>
<td>
Glyph group definitions.
</td>
</tr>
<tr>
<td>
[kerning.plist]
</td>
<td>
Kerning data.
</td>
</tr>
<tr>
<td>
[features.fea]
</td>
<td>
OpenType feature definitions.
</td>
</tr>
<tr>
<td>
[lib.plist]
</td>
<td>
Arbitrary custom data.
</td>
</tr>
<tr>
<td>
<a href="layercontents.html">layercontent

  [RFC 2119]: http://www.ietf.org/rfc/rfc2119.txt
  [metainfo.plist]: metainfo.html
  [fontinfo.plist]: fontinfo.html
  [groups.plist]: groups.html
  [kerning.plist]: kerning.html
  [features.fea]: features.html
  [lib.plist]: lib.html