---
layout: default
title: contents.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

*contents.plist* contains a dictionary that maps glyph names to GLIF file names. Those file names must be plain file names, not absolute or relative paths in the file system. Care must be taken when choosing file names: glyph names are case sensitive, yet many file systems are not. There is no one standard glyph name to file name conversion. However, the most common implementation is described below.

#### Common glyph name to file name algorithm

This algorithm has limited support for case insensitive file systems: it assumes glyph names are not case sensitive apart from the first character.

1.  If a glyph name starts with a ".
    1.  Replace the "." with an "\_". Some file systems regard file names that start with "." as invisible.

2.  Break the glyph name into parts delimited by ".".
3.  **If the first part contains one or more underscores**, it is a compound name.
    1.  Split the compound name by underscore into its member names.
    2.  To each member starting with a capital letter, add a "\_" at the end.
    3.  Rejoin the member names with underscore.

4.  **If the first part contains no underscore:**
    1.  If it starts with a capital letter, add a "\_" to the end.

5.  Rejoin the parts with ".".
6.  Tag the name with ".glif".

##### Examples

| glyph name            | file name             |
|-----------------------|-----------------------|
| a                     | a.glif                |
| A                     | A_.glif               |
| A.alt                 | A_.alt.glif           |
| T_H                   | T__H_.glif            |
| T_h                   | T__h.glif             |
| t_h                   | t_h.glif              |
| F_F_I                 | F__F__I_.glif         |
| f_f_i                 | f_f_i.glif            |
| Aacute_V.swash        | Aacute__V_.swash.glif |

##### Possible problems

1.  Some file systems impose file name length restrictions. This can cause file name clashes.
2.  The assumption that glyph names are not case sensitive apart from the first character causes problems with glyph names like *A.alt* and *A.Alt*.

## Specification

The property list data consists of a dictionary at the top level. The keys are glyph names and the values are file names.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>A</key>
  <string>A_.glif</string>
  <key>B</key>
  <string>B_.glif</string>
</dict>
</plist>
```