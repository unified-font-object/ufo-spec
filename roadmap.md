---
layout: default
navigation: true
order: 4
title: Roadmap
---

This page serves a a place to collect the UFO team's thoughts on potential future features of the specification.

### Compact UFO

A couple of people have asked about creating a compacted version of the UFO. The easiest way to do this would be to put the contents of the UFO into a zip archive. On a general level, this seems easy enough to do in the specification, there are precedents for compacting packages this way and there would be some benefits for the user. However, the implementation of this will be complicated for applications.

By design the UFO doesn't place a limit on how many glyphs can be in a font, so there could be lots and lots of GLIF files within a UFO. (Modern file systems would allow for up to 4,294,967,295 GLIF files.) The nice thing about the existing UFO structure is that it allows for very efficient management of the GLIF files. Not all glyphs must be loaded all of the time and saving procedures are very simple--if a glyph is to be removed, it is removed with an operating system call; if a glyph is unchanged since loading, the existing GLIF doesn't need to be resaved; a "save as" operation can be initiated with a directory tree copy. Our experiments with creating a compact version of the UFO, for example inside of a zip archive, have indicated that the aforementioned simplicity is no longer available. In the case of zip archives, files cannot be programmatically removed from or replaced in an existing zip. (At least they can't with the Python API.) This means that the entire contents of the UFO must be rewritten with each save. If there are a large number of glyphs, this could introduce serious memory issues. One way around this may be to do a directory tree copy to a temporary location, make the UFO changes, recompress and replace the existing file. This could lead to serious performance issues, so it needs to be studied before moving forward with this addition to the specification.
