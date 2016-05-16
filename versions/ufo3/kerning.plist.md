---
layout: default
title: kerning.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file contains horizontal kerning pairs for the font. This file is optional. If it is not defined in the UFO, there is no horizontal kerning data.

## Specification


The property list data consists of a dictionary at the top level. Keys are *first* member names and values are dictionaries. These dictionaries contain *second* member names as keys and kerning values, either integer or float, as the values.

The kerning pair members are glyph names or group names. Group names used as the first member of a kerning pair must begin with the kerning group prefix defined in the [groups.plist specification]. Group names used as the second member of a kerning pair must begin with the kerning group prefix defined in the [groups.plist specification]. Glyphs or groups in the pairs are not required to be in the font.

Kerning pairs that are not defined in kerning.plist implicitly have a value of "no kerning" or zero. Therefore any kerning pair that has a value of zero, unless it is a necessary value of an [exception], should not be stored in kerning.plist.

### Writing Direction

The kerning data is writing direction neutral. For text written left-to-right, the left-most glyph is the key in the top level dictionary. For text written right-to-left, the right-most glyph is the key in the top level dictionary. For example, given the pair *LG*, written left-to-right, the *L* is the key in the top dictionary and the *G* is the sub-dictionary. Given the pair *GL*, written right-to-left, the *G* is the key in the top dictionary and the *L* is the key in the sub-dictionary.

### Kerning Pair Types

Kerning pairs may reference groups. This is done by using a [group's name] as a member of a kerning pair. These group members allow the kerning data to represent vast amounts of kerning with relatively few pairs. A pair member that contains a group implies that all members of the group are kerned with the other member of the pair with the same value (unless an exception is defined, see below). For example, a font has this group:

| name           | members |
|----------------|---------|
| public.kern1.O | O, D, Q |

The font's kerning contains a pair referencing this group:

| Side 1         | Side 2 | Value |
|----------------|--------|-------|
| public.kern1.O | A      | -50   |

This implies that the pair values for the specific glyphs combinations are as follows:

| Side 1 | Side 2 | Value |
|--------|--------|-------|
| O      | A      | -50   |
| O      | A      | -50   |
| D      | A      | -50   |

The various combinations of glyphs and groups allow for three types of kerning pairs:

1.  Group combinations: group + group. For example, public.kern1.O + public.kern2.E.
2.  Glyph and group combinations: glyph + group and group + glyph. For example, A + public.kern2.E and public.kern1.O + A.
3.  Glyph combinations: glyph + glyph. For example, A + X.

#### Exceptions

The kerning data may contain *exceptions* to group pairs. The kerning pair types are organized in three levels:

Level 1: Group combinations.
Level 2: Glyph and group combinations.
Level 3: Glyph combinations.

Exception pairs may occur at the second and third levels. Second level pairs may be exceptions to first level pairs. Third level pairs may be exceptions to first and second level pairs.

For example, a font has these two groups:

| name           | members |
|----------------|---------|
| public.kern1.O | O, D, Q |
| public.kern2.E | E, F    |

The font's kerning contains a first level pair that references these two groups:

| Side 1         | Side 2         | Value |
|----------------|----------------|-------|
| public.kern1.O | public.kern2.E | -100  |

The font's kerning contains a second level pair that forms an exception to the first level pair:

| Side 1         | Side 2 | Value |
|----------------|--------|-------|
| public.kern1.O | F      | -200  |

The font's kerning contains a third level pair that is an exception to both the first and second level pairs:

| Side 1 | Side 2 | Value |
|--------|--------|-------|
| D      | F      | -300  |

This implies that the pair values for the specific glyphs combinations are as follows:

| Side 1 | Side 2 | Value |
|--------|--------|-------|
| O      | E      | -100  |
| O      | F      | -200  |
| D      | E      | -100  |
| D      | F      | -300  |
| Q      | E      | -100  |
| Q      | F      | -200  |

{: #exception-conflict-resolution }
##### Exception Conflict Resolution

It's possible to create kerning contradictions with exceptions. For example, given the same public.kern1.O and public.kern2.E group as above, a font contains the following kerning pairs:

| Side 1         | Side 2         | Value |
|----------------|----------------|-------|
| public.kern1.O | public.kern2.E | -100  |
| public.kern1.O | F              | -200  |
| Q              | public.kern2.E | -250  |
| D              | F              | -300  |

This implies that the pair values for the specific glyphs combinations are as follows:

| Side 1 | Side 2 | Value            |
|--------|--------|------------------|
| O      | E      | -100             |
| O      | F      | -200             |
| D      | E      | -100             |
| D      | F      | -300             |
| Q      | E      | -250             |
| Q      | F      | **-200 or -250** |

The two second level pairs, public.kern1.O + F and Q + public.kern2.E define two possible values for the pair Q + F. This is an unresolvable ambiguity.

To resolve this, glyph + group pairs are given higher priority than group + glyph pairs when these contradictions occur. In the example above, the Q + F pair value would be -250.

#### Kerning Value Lookup Algorithm

The task of finding a value for a particular glyph + glyph combination is relatively easy. The following algorithm demonstrates a way that it can be done for a given pair.

If the pair *first glyph + second glyph* is in the kerning data:
  - The value for *first glyph + second glyph* is the value.
  - Stop.

If the second glyph is in a kerning group:
  *second group* is the name of the kerning group containing the second glyph.
  If the pair *first glyph + second group* is in the kerning data:
    - The value for *first glyph + second group* is the value.
    - Stop.

If the first glyph is in a kerning group:
  *first group* is the name of the kerning group containing the first glyph.
  If the pair *first group + second glyph* is in the kerning data:
    - The value for *first first + second glyph* is the value.
    - Stop.

If the first glyph is in a kerning group and the second glyph is in a kerning group:
  *first group* is the name of the kerning group containing the first glyph.
  *second group* is the name of the kerning group containing the second glyph.
  If the pair *first group + second group* is in the kerning data:
    - The value for *first group + second group* is the value.
    - Stop.

The value is zero.

##### Sample implementation

```python
def lookupKerningValue(pair, kerning, groups, fallback=0):
    """
    Note: This expects kerning to be a flat dictionary
    of kerning pairs, not the nested structure used
    in kerning.plist.

    >>> groups = {
    ...     "public.kern1.O" : ["O", "D", "Q"],
    ...     "public.kern2.E" : ["E", "F"]
    ... }
    >>> kerning = {
    ...     ("public.kern1.O", "public.kern2.E") : -100,
    ...     ("public.kern1.O", "F") : -200,
    ...     ("D", "F") : -300
    ... }
    >>> lookupKerningValue(("D", "F"), kerning, groups)
    -300
    >>> lookupKerningValue(("O", "F"), kerning, groups)
    -200
    >>> lookupKerningValue(("O", "E"), kerning, groups)
    -100
    >>> lookupKerningValue(("O", "O"), kerning, groups)
    0
    >>> lookupKerningValue(("E", "E"), kerning, groups)
    0
    >>> lookupKerningValue(("E", "O"), kerning, groups)
    0
    >>> lookupKerningValue(("X", "X"), kerning, groups)
    0
    >>> lookupKerningValue(("public.kern1.O", "public.kern2.E"),
    ...     kerning, groups)
    -100
    >>> lookupKerningValue(("public.kern1.O", "F"), kerning, groups)
    -200
    >>> lookupKerningValue(("O", "public.kern2.E"), kerning, groups)
    -100
    >>> lookupKerningValue(("public.kern1.X", "public.kern2.X"), kerning, groups)
    0
    """
    # quickly check to see if the pair is in the kerning dictionary
    if pair in kerning:
        return kerning[pair]
    # get group names and make sure first and second are glyph names
    first, second = pair
    firstGroup = secondGroup = None
    if first.startswith("public.kern1."):
        firstGroup = first
        first = None
    else:
        for group, groupMembers in groups.items():
            if group.startswith("public.kern1."):
                if first in groupMembers:
                    firstGroup = group
                    break
    if second.startswith("public.kern2."):
        secondGroup = second
        second = None
    else:
        for group, groupMembers in groups.items():
            if group.startswith("public.kern2."):
                if second in groupMembers:
                    secondGroup = group
                    break
    # make an ordered list of pairs to look up
    pairs = [
        (first, second),
        (first, secondGroup),
        (firstGroup, second),
        (firstGroup, secondGroup)
    ]
    # look up the pairs and return any matches
    for pair in pairs:
        if pair in kerning:
            return kerning[pair]
    # use the fallback value
    return fallback
```

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>public.kern1.BGroup</key>
  <dict>
    <key>public.kern2.CGroup</key>
    <integer>7</integer>
    <key>public.kern2.DGroup</key>
    <integer>8</integer>
    <key>A</key>
    <integer>5</integer>
    <key>B</key>
    <integer>6</integer>
  </dict>
  <key>public.kern1.CGroup</key>
  <dict>
    <key>public.kern2.CGroup</key>
    <integer>11</integer>
    <key>public.kern2.DGroup</key>
    <integer>12</integer>
    <key>A</key>
    <integer>9</integer>
    <key>B</key>
    <integer>10</integer>
  </dict>
  <key>A</key>
  <dict>
    <key>public.kern2.CGroup</key>
    <integer>3</integer>
    <key>public.kern2.DGroup</key>
    <integer>4</integer>
    <key>A</key>
    <integer>1</integer>
    <key>B</key>
    <integer>2</integer>
  </dict>
</dict>
</plist>

```

# Converting to UFO 3 formatted kerning


In UFO 1 and UFO 2, the implication was that if a member of a kerning pair had the same name as a group and a glyph, that member was the group. In UFO 3, all kerning groups are identified through the use of the standard group prefixes defined in the [groups.plist specification][group's name]. An algorithm for converting UFO 1 and UFO 2 group kerning is detailed below.

### Conversion algorithm

Note: this algorithm, and its sample implementation, does not check the compliance of the kerning groups with the requirements defined in the groups.plist specification.

-   Make a list of groups referenced on the first side of kerning pairs.
-   For each of these groups:
-   -   *original group name* is the original group name.
    -   If *original group name* does not begin with *public.kern1.*:
    -   -   *new group name* is *public.kern1* plus *original group name*.
        -   If *new group name* is already in the groups:
        -   -   Beginning with 1, add a number to the end of *new group name*. Repeat until a unique name is found.

    -   Copy the contents of the group and store them in groups.plist under *new group name*.
    -   Copy and remove the dictionary from kerning.plist that is stored under the key *original group name*.
    -   Add *new group name* as a key to kerning.plist with the copied dictionary as the value.

-   Make a list of groups referenced on the second side of kerning pairs.
-   For each of these groups:
-   -   *original group name* is the original group name.
    -   If *original group name* does not begin with *public.kern2.* as defined in fontinfo.plist:
    -   -   *new group name* is *public.kern2.* plus *original group name*.
        -   If *new group name* is already in the groups:
        -   -   Beginning with 1, add a number to the end of *new group name*. Repeat until a unique name is found.

    -   Copy the contents of the group and store them in groups.plist under *new group name*.
    -   For each first glyph and dictionary in kerning.plist:
    -   -   If *original group name* is a key in the dictionary:
        -   -   Copy the *value* stored under *original group name*.
            -   Remove *original group name* from the dictionary.
            -   Add *new group name* as a key in the dictionary with *value* as the value.

### Sample conversion implementation

```python
def convertUFO1OrUFO2KerningToUFO3Kerning(kerning, groups):
    # Make lists of groups referenced in kerning pairs.
    firstReferencedGroups = set()
    secondReferencedGroups = set()
    for first, seconds in kerning.items():
        if first in groups:
            if not first.startswith("public.kern1."):
                firstReferencedGroups.add(first)
        for second in seconds.keys():
            if second in groups:
                if not second.startswith("public.kern2."):
                    secondReferencedGroups.add(second)
    # Create new names for these groups.
    firstRenamedGroups = {}
    for first in firstReferencedGroups:
        # Make a list of existing group names.
        existingGroupNames = groups.keys() + firstRenamedGroups.keys()
        # Add the prefix to the name.
        newName = "public.kern1." + first
        # Make a unique group name.
        newName = makeUniqueGroupName(newName, existingGroupNames)
        # Store for use later.
        firstRenamedGroups[first] = newName
    secondRenamedGroups = {}
    for second in secondReferencedGroups:
        # Make a list of existing group names.
        existingGroupNames = groups.keys() + secondRenamedGroups.keys()
        # Add the prefix to the name.
        newName = "public.kern2." + second
        # Make a unique group name.
        newName = makeUniqueGroupName(newName, existingGroupNames)
        # Store for use later.
        secondRenamedGroups[second] = newName
    # Populate the new group names into the kerning dictionary as needed.
    newKerning = {}
    for first, seconds in kerning.items():
        first = firstRenamedGroups.get(first, first)
        newSeconds = {}
        for second, value in seconds.items():
            second = secondRenamedGroups.get(second, second)
            newSeconds[second] = value
        newKerning[first] = newSeconds
    # Make copies of the referenced groups and store them
    # under the new names in the overall groups dictionary.
    allRenamedGroups = firstRenamedGroups.items()
    allRenamedGroups += secondRenamedGroups.items()
    for oldName, newName in allRenamedGroups:
        group = list(groups[oldName])
        groups[newName] = group
    # Return the kerning and the groups.
    return newKerning, groups

def makeUniqueGroupName(name, groupNames, counter=0):
    # Add a number to the name if the counter is higher than zero.
    newName = name
    if counter > 0:
        newName = "%s%d" % (newName, counter)
    # If the new name is in the existing group names, recurse.
    if newName in groupNames:
        return makeUniqueGroupName(name, groupNames, counter + 1)
    # Otherwise send back the new name.
    return newName

def test():
    """
    >>> testKerning = {
    ...     "A" : {
    ...         "A" : 1,
    ...         "B" : 2,
    ...         "CGroup" : 3,
    ...         "DGroup" : 4
    ...     },
    ...     "BGroup" : {
    ...         "A" : 5,
    ...         "B" : 6,
    ...         "CGroup" : 7,
    ...         "DGroup" : 8
    ...     },
    ...     "CGroup" : {
    ...         "A" : 9,
    ...         "B" : 10,
    ...         "CGroup" : 11,
    ...         "DGroup" : 12
    ...     },
    ... }
    >>> testGroups = {
    ...     "BGroup" : ["B"],
    ...     "CGroup" : ["C"],
    ...     "DGroup" : ["D"],
    ... }
    >>> kerning, groups = convertUFO1OrUFO2KerningToUFO3Kerning(
    ...     testKerning, testGroups)
    >>> expected = {
    ...     "A" : {
    ...         "A": 1,
    ...         "B": 2,
    ...         "public.kern2.CGroup": 3,
    ...         "public.kern2.DGroup": 4
    ...     },
    ...     "public.kern1.BGroup": {
    ...         "A": 5,
    ...         "B": 6,
    ...         "public.kern2.CGroup": 7,
    ...         "public.kern2.DGroup": 8
    ...     },
    ...     "public.kern1.CGroup": {
    ...         "A": 9,
    ...         "B": 10,
    ...         "public.kern2.CGroup": 11,
    ...         "public.kern2.DGroup": 12
    ...     }
    ... }
    >>> kerning == expected
    True
    >>> expected = {
    ...     "BGroup": ["B"],
    ...     "CGroup": ["C"],
    ...     "DGroup": ["D"],
    ...     "public.kern1.BGroup": ["B"],
    ...     "public.kern1.CGroup": ["C"],
    ...     "public.kern2.CGroup": ["C"],
    ...     "public.kern2.DGroup": ["D"],
    ... }
    >>> groups == expected
    True
    """

```

  [XML Property List]: conventions.html#propertylist
  [groups.plist specification]: groups.plist
  [exception]: #kerning-pair-exceptions
  [exception-conflict-resolution]: #exception-conflict-resolution
  [group's name]: groups.plist
