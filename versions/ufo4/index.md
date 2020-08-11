---
layout: default
navigation: true
order: 400
title: UFO 4
---

UFO 4 will be an extension of [UFO 3](../ufo3). These are the additions and changes under consideration:

- charactermapping.plist: A new file that defines character to glyph name mapping will be added. To prevent duplicate or conflicting data, the `<unicode>` element will be removed from the GLIF specification.
- Enhanced right-to-left kerning support.
- Vertical kerning support.
- Removing the `name` attribute from the `<glyph>` element in GLIF.
- Support for the OpenType math table.
- Support for storing hints in high level form. Inventing a new storage format for this is far too complex so we'd rather use an existing format (such as the one used by VTT). That will require another party to step forward with a specification for the storage structure and implementation instructions. If this doesn't happen we'll reopen the idea of storing hinting data in low level form.