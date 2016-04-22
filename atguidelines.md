---
layout: default
navigation: true
order: 5
title: Authoring Tool Guidelines
---

These guidelines define requirements and recommendations for authoring tools that work with UFOs. These guidelines are applicative to all versions of the UFO specification. Each version, and each section, will have additional specific guidelines for authoring tools to follow.

### Authoring Tool Operating Models

Authoring tools may work with UFOs using two different models--import/export and native file format.

#### Import/Export

This model allows an authoring tool to import data from a UFO and/or export data to a UFO. The file format after the import or before the export is _not_ the UFO. Rather, it is a format that is specific to the authoring tool.

#### Native File Format

This model allows the UFO to the the native file format for the authoring tool.

### Requirements and Recommendations

Authoring tools that use the native file format operating model must not remove data from a UFO or any of a UFO's files without informing the user. For example, if an authoring tool doesn't work with groups, the authoring tool must not silently remove the group data from a UFO. Authoring tools that use the import/export operating model may remove data during an import operation as long as the original UFO data is not altered. In these cases, it is recommended that the user be informed of the data being ignored.

When writing data into an existing UFO, authoring tools should not overwrite files unnecessarily. For example, if _A.glif_ already exists in a UFO and a glyph needs to be stored in a file named _A.glif_, the file should not be written if the file contents will be exactly the same. This allows the modification time to be preserved in the original GLIF file.

Authoring tools must not add non-conformant data to the UFO structure outside of designated areas. For example, a _Stuff For Me_ directory must not be created in the root of the UFO. A, _myFontInfoData_ key must not be added to fontinfo.plist.

Authoring tools must write only the allowed parts of a particular UFO version. For example, an authoring tool must not write a _data_ directory into a UFO with a @formatVersion@ of 2 in metainfo.plist.
