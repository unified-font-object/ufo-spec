---
layout: default
navigation: true
order: 200
title: UFO 2
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

| [metainfo.plist](metainfo.html)                     | Format version, creator, etc. |
| [fontinfo.plist](fontinfo.html)                     | Various font info data. |
| [groups.plist](groups.html)                         | Glyph group definitions. |
| [kerning.plist](kerning.html)                       | Kerning data. |
| [features.fea](features.html)                       | OpenType feature definitions. |
| [lib.plist](lib.html)                               | Arbitrary custom data. |
| [glyphs](glyphs.html)                               | A directory containing all glyphs in the font. |
| glyphs/[contents.plist](glyphs.html)                | File name to glyph name mapping. |
| glyphs/[*.glif](glif.html)                          | A glyph definition. |

<hr class="subsection">

# Changes from UFO 1

#### fontinfo.plist

The fontinfo.plist structure was redesigned in UFO 2 to make things cleaner, clearer and more organized.

#### features.fea

features.fea was added.

