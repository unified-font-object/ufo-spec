---
layout: default
title: data directory
---

This directory allows authoring tools to store application specific data that is too complex or too large for [lib.plist] and the [lib element in GLIF]. The items within the directory may be either files or directories. The top level files and directories must follow the same [reverse domain naming scheme] used in the lib. The pattern "public.\*", where \* represents an arbitrary string of one or more characters, is reserved for standardized directory and file names. Authoring tools are responsible for their own sections of the data directory and they must not delete or modify any other sections of the data directory belonging to other tools unless given permission to do so. Empty directories are not allowed within the data directory and its subdirectories. Authoring tools may remove empty directories even if the directories do not belong to them.

  [lib.plist]: ../lib.plist
  [lib element in GLIF]: ../glyphs/glif#lib
  [reverse domain naming scheme]: ../conventions#reversedomain
