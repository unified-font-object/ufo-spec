---
layout: default
navigation: true
order: 200
title: UFO 2
tree:
    - metainfo.plist
    - fontinfo.plist
    - groups.plist
    - kerning.plist
    - features.fea
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
  - features.fea
  - lib.plist
  - {: .filediagramDirectory}glyphs
    - contents.plist
    - .glif


Each of the files has a unique meaning, purpose and data structure:

| [metainfo.plist](metainfo.plist)                       | Format version, creator, etc. |
| [fontinfo.plist](fontinfo.plist)                       | Various font info data. |
| [groups.plist](groups.plist)                           | Glyph group definitions. |
| [kerning.plist](kerning.plist)                         | Kerning data. |
| [features.fea](features.fea)                           | OpenType feature definitions. |
| [lib.plist](lib.plist)                                 | Arbitrary custom data. |
| [glyphs](glyphs)                                       | A directory containing all glyphs in the font. |
| glyphs/[contents.plist](glyphs/contents.plist)         | File name to glyph name mapping. |
| glyphs/[*.glif](glyphs/glif)                           | A glyph definition. |

<hr class="subsection">

# Changes from UFO 1

#### fontinfo.plist

The fontinfo.plist structure was redesigned in UFO 2 to make things cleaner, clearer and more organized.

#### features.fea

features.fea was added.

