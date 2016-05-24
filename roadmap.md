---
layout: default
navigation: true
order: 4
title: Roadmap
---

This page serves a a place to collect the UFO team's thoughts on potential future features of the specification.

## Single File UFO

UFO has two possible storage formats. The first, "UFO Package", is a multi-file, file system directory structure. The second, "UFO ZIP", is a [ZIP archive] containing the same directory structure as defined for _UFO Package_.

A _UFO ZIP_ must be a ZIP archive that follows these specifications:

1. ZIP64 format is allowed, but not required.
2. File names must be encoded to UTF-8.
3. All contents of the UFO must be contained within a single directory. For example, `rootdirectory/metainfo.plist` and `rootdirectory/kerning.plist`. The name of this directory will be arbitrary and no assumptions should be made about it's name.
4. The file may or may not be compressed.
5. The file must not be encrypted.

### File Name Extensions

| --- | --- |
| .ufo | UFO Package |
| .ufoz | UFO ZIP |

### Notes

ZIP has been chosen over several other viable candidates because of its broad interoperability and ease of implementation for developers. Most, if not all, modern programming languages have existing code for reading and writing ZIP. Additionally, ZIPs are also easy for users to create on their own. For example in OS X a user can take a _UFO Package_ and create a _UFO ZIP_ directly in the Finder.


## Unified Font Set

We are in the early phase of designing a new file structure that will represent *multiple* UFOs. We are currently calling these "Unified Font Set" (see below for other names). This is the current file structure:

{: .filediagram}
- {: .filediagramDirectory}*.ufs
	- metainfo.plist
	- documents.plist
	- fontinfo.plist
	- groups.plist
	- features.fea
	- lib.plist
	- interpolation.designspace

It is hopefully obvious that this is largely based on the structure of UFO. That is by design. We want clear associations between UFS and UFO data. This will allow for significant code reuse.

_Unless specified otherwise, the files are optional._

#### metainfo.plist
Format version, creator, etc. for the UFS. This file is required.

#### documents.plist
*The name of this file has not been determined. "documents" is too ambiguous.*

The data in a UFS can represent many things and this file will define the intended purpose(s) of the UFS. The goal is to establish common purposes and data structures that can be used across tools. For example, interpolation rules have a wide variety of uses beyond simple outline generation. These rules can be useful in kerning, font mastering, hinting and proofing tools. We want to establish publicly available locations and data structures for this type of data. On the surface, this file appears similar to lib.plist. However, it's intent is different. lib.plist originated as a way to store shallow, private data with only occasional data defined for public use. The purpose of this new file is to define public data that may potentially be deeply structured.

The concepts behind and structure of this file are still being developed. We currently have two ideas for the structure of this file.

##### Category : Items

The first idea is based on categorizing purposes and storing data for each item within a category.

```python
{
    "com.something.category" : [
        {
            "name" : "string",
            # category specific details
        }
    ]
}
```

The top level key would be a category definition that defines what the value for the key represents. A category is an abstraction that would represent universal data like interpolation rules. They could also represent something privately defined. These keys would follow the reverse domain naming scheme we use for the various lib locations. We would reserve `public.*` keys for use by official UFS spec defined categories.

The values would be a list of items in the category. This would allow for more than one definition within a category. The items in the list would be dicts that follow a defined (either publicly or privately) specification. The only requirement would be a name key/value pair that defines a name for the item. Everything else would be defined on an as needed basis.

##### UFO Reference Data

The other idea is to store an ordered list of external UFO references with app-defined data defining the purpose of the reference.

```python
[
    ('master_regular', {'public.source': "sources/MyFontRegular.ufo",
                       'com.something.blah': { ..anything.. }}),
    ('master_bold',    {'public.source': "sources/MyFontBold.ufo",
                       'com.something.blah': { ..anything.. }}),
]
```

#### fontinfo.plist
Global font information data. The potential contents correspond to the UFO fontinfo.plist specification.

#### groups.plist
Global glyph group definitions. The potential contents correspond to the UFO groups.plist specification.

#### features.fea
Global OpenType feature definitions. The potential contents correspond to the UFO features.fea specification.

#### lib.plist
Arbitrary custom data for the UFS. The potential contents correspond to the UFO libs.plist specification.

#### interpolation.designspace
A [MutatorMath] .designspace file defining interpolation rules for the UFS. The .designspace format would need to be modified to allow more than one design space per file.


### Global and Local Data

Global data is data defined in the UFS. Local data is data defined in a UFO. Defining different data for the same location/key/record is allowed. Data collation rules are defined below.

#### fontinfo.plist

If a top level key is in a UFO's fontinfo.plist, the UFO's value for the key overrides the value defined in the UFS. The following are exceptions to this rule.

`openTypeNameRecords` When compiling a name table, the local entries are appended to the global entries.

`guidelines` Local guidelines are appended to the global guidelines. The identifiers for all guidelines must be unique in the combined list.

#### groups.plist

If a group is defined locally, it overrides a group with the same name defined globally.

#### features.fea

The local feature text is appended to the global feature text. The .fea syntax combines, not overrides, the contents of features defined more than once.

#### lib.plist

The UFS lib.plist is specific to the UFS. There is no resolution  order necessary.

### Location of UFOs

UFOs references by the UFS *must* be stored next to the UFS. Path resolution rules will not be defined.

### Other Contents

Not all portions of the UFO file structure are applicable to UFS. Obviously, there is no need for layer or glyph data. Additionally, these are the current thoughts on the other files and directories:

- *kerning.plist* Coalescing font-level and global kerning data is complex. Including it presents a non-trivial implementation requirement. We are weighing the pros and cons of this.
- *images* Images will not be stored in UFS.
- */data* The data directory could be stored within UFS, but we need to think through potential use cases.

### Single File UFS

Just like UFO, there will be "UFS Package" and "UFS ZIP" formats.

### Other Names

Unified Font Set is not the only name we've come up with for this new structure. Here are some others:

| --- | --- |
| Magazine | *.magazine |
| Unified Font Bundle | *.ufb |


## UFO 4

The following ideas are being considered for the UFO 4 specification.

- charactermapping.plist: A new file that defines character to glyph name mapping will be added. To prevent duplicate or conflicting data, the `<unicode>` element will be removed from the GLIF specification.
- Enhanced right-to-left kerning support.
- Vertical kerning support.
- Removing the `name` attribute from the `<glyph>` element in GLIF.
- Support for the OpenType math table.

[ZIP archive]: https://en.wikipedia.org/wiki/Zip_(file_format)
[MutatorMath]: https://github.com/LettError/MutatorMath/blob/master/Docs/designSpaceFileFormat.md
