---
layout: default
navigation: true
order: 100
title: UFO 1
tree:
    - metainfo.plist
    - fontinfo.plist
    - groups.plist
    - kerning.plist
    - lib.plist
    - glyphs
    - glyphs/contents.plist
    - glyphs/glif
---

A UFO file is a directory following this structure:

{: .filediagram}
- {: .filediagramDirectory}*.ufo
  - metainfo.plist
  - fontinfo.plist
  - groups.plist
  - kerning.plist
  - lib.plist
  - {: .filediagramDirectory}glyphs
    - contents.plist
    - *.glif


Each of the files has a unique meaning, purpose and data structure:

| [metainfo.plist](metainfo)                      | Format version, creator, etc. |
| [fontinfo.plist](fontinfo)                      | Various font info data. |
| [groups.plist](groups)                          | Glyph group definitions. |
| [kerning.plist](kerning)                        | Kerning data. |
| [lib.plist](lib)                                | Arbitrary custom data. |
| [glyphs](glyphs)                                | A directory containing all glyphs in the font. |
| glyphs/[contents.plist](content.plist)          | File name to glyph name mapping. |
| glyphs/[*.glif](glif)                           | A glyph definition. |

