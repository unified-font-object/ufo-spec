---
layout: default
title: glyphs directory
---

A glyphs directory represents a layer of glyph data in a font. The glyph data files will be in [Glyph Interchange Format (GLIF) Version 2][glif2] or GLIF 1 ([defined in the UFO 2 specification][glif1]). The directory may contain zero or more GLIF files. It must contain a [contents.plist] file defining the file name to glyph name mapping even if no GLIF files are present. A [layerinfo.plist] file may be present defining various properties of the layer.

  [glif2]: glif
  [glif1]: ../../ufo2/glyphs/glif
  [contents.plist]: contents.plist
  [layerinfo.plist]: layerinfo.plist