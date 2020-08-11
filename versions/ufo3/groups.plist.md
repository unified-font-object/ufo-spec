---
layout: default
title: groups.plist
---

{: .fileformat}
| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains the definitions of arbitrary groups of glyphs. This file is optional. If it is not defined in the UFO, there is no group data.

## Specification


The property list data consists of a dictionary at the top level. Keys are group names and values are lists of glyph name strings. Group names must contain one or more characters. There is no name length limit and any character may be used in a group name. The pattern "public.\*", where \* represents an arbitrary string of one or more characters, is reserved for use in standardized group names. With the exception of the kerning groups defined below, glyphs may be in more than one group and they may appear within the same group more than once. Glyphs in the groups are not required to be in the font.

### Kerning Groups

Groups may be used as members of kerning pairs in [kerning.plist]. These groups are divided into two types: groups that appear on the first side of a kerning pair and groups that appear on the second side of a kerning pair.

Kerning groups must begin with standard prefixes. The prefix for groups intended for use in the first side of a kerning pair is "public.kern1.". The prefix for groups intended for use in the second side of a kerning pair is "public.kern2.". One or more characters must follow the prefix. These characters are up to the user and/or authoring tool. There is no requirement that the prefixes be visible to users within an authoring tool, nor is there a requirement that the prefixes be maintained when converting kerning to another format (eg a kerning feature in [features.fea]).

Kerning groups must strictly adhere to the following rules.

#### 1. Kerning group names must begin with the appropriate prefix.

As stated elsewhere, these prefixes eliminate kerning interpretation ambiguities.

#### 2. Only kerning groups are allowed to use the kerning group prefixes in their names.

Any group whose name begins with a kerning group prefix is considered a kerning group.

#### 3. Kerning groups are not required to appear in the kerning pairs.

One or more kerning groups may be unreferenced in kerning pairs. This is allowed and in some cases, for example generating an OpenType kern feature, unreferenced groups have an important role.

#### 4. Glyphs must not appear in more than one kerning group per side.

Glyphs that appear in more than one group per side create a logical ambiguity. For example, consider these two kerning groups:

{: .example-group}
| group name      | group members                |
|-----------------|------------------------------|
| public.kern1.A1 | A, Aacute, Agrave, Adieresis |
| public.kern1.A2 | A, Acircumflex               |

The kerning in this example contains the following kerning pairs:

{: .example-kerning}
| side 1          | side 2 | value |
|-----------------|--------|-------|
| public.kern1.A1 | T      | -50   |
| public.kern1.A2 | T      | -100  |

Now, an application wants to apply the kerning for the pair "AT". There are different ways to find kerning for a pair, but in this case the most general approach is best. The following steps occur:

1. Look to see if (A, T) is a pair in the kerning. It isn't.
2. Locate the groups for the first and second members of the pair.
3. Two groups are found for A: public.kern1.A1 and public.kern1.A2.
4. Look up the kerning value for (public.kern1.A1, T) and (public.kern1.A2, T).

Two kerning values are found: -50 and -100. There is no way to determine which one is correct. This ambiguity is eliminated by requiring that glyphs occur in only one group per kerning side.

#### 5. Glyphs should not appear more than once in a single kerning group.

Any appearances of a glyph after the first appearance of that glyph in a group must be ignored by authoring tools. Duplicate glyphs in a kerning group provide no additional information to authoring tools and, thus, may be safely ignored silently.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>public.kern1.A</key>
  <array>
    <string>A</string>
    <string>Aacute</string>
    <string>Acircumflex</string>
  </array>
  <key>Group1</key>
  <array>
    <string>A</string>
    <string>A.alt</string>
  </array>
  <key>B</key>
  <array>
    <string>B</string>
    <string>B.alt</string>
  </array>
</dict>
</plist>

```

  [XML Property List]: ../conventions.html#xml-property-lists
  [kerning.plist]: ../kerning.plist
  [features.fea]: ../features.fea
