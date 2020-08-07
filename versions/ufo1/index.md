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

| [metainfo.plist](metainfo.plist) | Format version, creator, etc. |
| [fontinfo.plist](fontinfo.plist) | Various font info data. |
| [groups.plist](groups.plist) | Glyph group definitions. |
| [kerning.plist](kerning.plist) | Kerning data. |
| [lib.plist](lib.plist) | Arbitrary custom data. |
| [glyphs](glyphs) | A directory containing all glyphs in the font. |
| glyphs/[contents.plist](glyphs/contents.plist) | File name to glyph name mapping. |
| glyphs/[*.glif](glyphs/glif) | A glyph definition. |

