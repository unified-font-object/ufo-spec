---
layout: default
title: Conventions
---

These are conventions that are used throughout the UFO.

### XML Property Lists

XML property lists are used throughout this specification. [A DTD is available.]

It is recommended, but not required, that dictionaries in property lists be written in ascending order based on the keys of the dictionary. This makes UFO usage more convenient in revision control systems, among other things.

### Coordinate System

Coordinates and transformations in the UFO are relative to the origin (x=0 and y=0), the positive x-axis points towards the right and the positive y-axis points up, unless otherwise noted.

### Data Types

These types are used throughout the UFO specification.

While efforts have been made to define how many of the values in various UFO files relate to binary files such as OpenType, it is the responsibility of authoring tools to ensure the UFO values convert to said binary values appropriately. For example, in OpenType many fields require unsigned short integers, but a UFO may contain values for these fields that are greater than 65,535.

#### string

A string is specified with one or more characters encoded with the encoding scheme defined for the XML file that the string belongs to. The range of characters allowed in a given string field in the UFO may be limited. In these cases the specification defines the available subset.

#### integer

An integer is specified with an optional sign character ("+" or "-") followed by one or more digits "0" to "9". There is not limit to the number of integer digits. If a sign character is not present, the number is non-negative.

#### non-negative integer

An integer greater than or equal to zero. See above for integer notation.

#### float

A float is specified with an optional sign character ("+" or "-") followed by zero or more digits "0" to "9" followed by a period "." followed by one or more digits "0" to "9". There is no limit to the number of digits before or after the decimal. If a sign character is not present, the number is non-negative.

Authoring tools should not write floats that can be represented losslessly as integers unless the specification requires a float.

#### non-negative float

A float greater than or equal to zero. See above for float notation.

#### list

An collection of items. The items are ordered, however the order is insignificant unless otherwise stated for a particular list in this specification.

#### dictionary

A dictionary is an unordered associative array mapping keys to values. In the XML property lists used throughout the UFO, the keys must be strings. Values may be any type, though the options are defined throughout this specification.

{: #colors }
#### color definition

A color definition is defined as a string containing a comma-separated sequence of four integers or floats between 0 and 1. White space characters are allowed around the numerical values. The values in the string define the red, green, blue and alpha components of the color. The color is always specified in the [sRGB] color space.

Examples

| string | red component | green component | blue component | alpha component |
|--|--|--|--|--|
| 1,0,0,1 | 1.0 | 0 | 0 | 1.0 |
| 0,.5,0,.5 | 0 | 0.5 | 0 | 0.5 |

### Reverse Domain Naming Schemes

In several places in the UFO the [reverse domain naming system] is recommended for creating unique keys and ids. To make a reverse domain, reverse the relevant Internet domain. For example, if the Internet domain is *unifiedfontobject.org*, the reverse domain name would be *org.unifiedfontobject*. Further extensions to make the string unique may be added. For example, *org.unifiedfontobject.MySpecialTool*.

The name *public.\**, where \* represents an arbitrary string of one or more characters, is reserved for use by data structures that are part of the UFO specification.

### Common User Name to File Name Algorithm

There is no standard user name to file name conversion. The algorithm below is an example of a common conversion process. It has been designed to avoid name clashes and work with common file systems. It applies the following rules:

1.  Filenames must be unique.
2.  Filenames must be case insensitive.
3.  Filenames may use any character that can be represented by UTF-8 except: \"(0x22) ( (0x28) ) (0x29) \* (0x2A) + (0x2B) / (0x2F) : (0x3A) &lt; (0x3C) &gt; (0x3E) ? (0x3F) \[ (0x5B) \\ (0x5C) \] (0x5D) \| (0x7C) and anything in the ASCII control character range (0x00-0x1F and 0x7F).
4.  Filenames must be no longer than 255 characters.
5.  Filenames, regardless of extension and case, must not match any of the [MS-DOS reserved file names].

{: .algorithmdiagram}
-   *name* is the user name without any required prefix or suffix.
-   *maximum length* is 255 minus the length of a prefix and/or suffix that will be added to the name.
-   Perform a generic translation of the name without consideration for existing names:
-   -   Replace any illegal characters in *name* with underscores, where the illegal characters are: " \* + / : &lt; &gt; ? \[ \\ \] \| anything in the range 0x00-0x1F and 0x7F.
    -   Insert an underscore immediately after any uppercase character.
    -   If the name begins with a period and a prefix will not be added to the name, replace the period with an underscore.
    -   If the revised *name* is longer than *maximum length*:
    -   -   Remove as many characters from the end of *name* as needed to make *name* no longer than *maximum length*.

-   Use period as a delimiter to split *name* into parts. For every one of these parts:
-   -   If a case-insensitive version of *part* is in the list of MS-DOS reserved filenames, where the illegal filenames are: CON, PRN, AUX, CLOCK$, NUL, A:-Z:, COM1, LPT1, LPT2, LPT3, COM2, COM3 and COM4:
    -   -   Insert an underscore at the beginning of the part.

-   Rejoin all of the parts with periods as needed.
-   -   Insert an underscore before the start of the illegal filename.
-   If a case-insensitive version of *name* is unique:
-   -   Stop.
-   If a case-insensitive version of *name* is not unique:
-   -   Remove as many characters from the end of *name* as needed to make *name* no longer than *maximum length* minus 15.
    -   Starting with 000000000000001, add 15 zero filled characters to the name.
    -   If a case-insensitive version of *name* is unique:
    -   -   Stop.
    -   Otherwise increment the number by 1 and repeat until a case-insensitive unique name is found or 999999999999999 is reached.

-   If a case-insensitive version of *name* is not unique:
-   -   *number* is 1.
    -   *name* is *number*.
    -   If *name* is unique:
    -   -   Stop.
    -   Otherwise increment number by 1 and repeat until a unique name is found or all possible numbers in a string *maximum length* long has been reached.

-   If *name* is not unique:
-   -   Raise an error and let the user know that after trying more than 10<sup>255</sup> names, nothing unique could be found.

#### Examples

| glyph name | file name |
|--|--|
| a | a |
| A | A\_ |
| AE | A\_E\_ |
| Ae | A\_e |
| ae | ae |
| aE | aE\_ |
| a.alt | a.alt |
| A.alt | A\_.alt |
| A.Alt | A\_.A\_lt |
| A.aLt | A\_.aL\_t |
| A.alT | A\_.alT\_ |
| T\_H | T\_\_H\_ |
| T\_h | T\_\_h |
| t\_h | t\_h |
| F\_F\_I | F\_\_F\_\_I\_ |
| f\_f\_i | f\_f\_i |
| Aacute\_V.swash | A\_acute\_V\_.swash |
| .notdef | \_notdef |
| con | \_con |
| CON | C\_O\_N\_ |
| con.alt | \_con.alt |
| alt.con | alt.\_con |

#### Example implementation:

```python
illegalCharacters = "\" * + / : < > ? [ \ ] | \0".split(" ")
illegalCharacters += [chr(i) for i in range(1, 32)]
illegalCharacters += [chr(0x7F)]
reservedFileNames = "CON PRN AUX CLOCK$ NUL A:-Z: COM1".lower().split(" ")
reservedFileNames += "LPT1 LPT2 LPT3 COM2 COM3 COM4".lower().split(" ")
maxFileNameLength = 255

def userNameToFileName(userName, existing=[], prefix="", suffix=""):
    """
    existing should be a case-insensitive list
    of all existing file names.

    >>> userNameToFileName(u"a")
    u'a'
    >>> userNameToFileName(u"A")
    u'A_'
    >>> userNameToFileName(u"AE")
    u'A_E_'
    >>> userNameToFileName(u"Ae")
    u'A_e'
    >>> userNameToFileName(u"ae")
    u'ae'
    >>> userNameToFileName(u"aE")
    u'aE_'
    >>> userNameToFileName(u"a.alt")
    u'a.alt'
    >>> userNameToFileName(u"A.alt")
    u'A_.alt'
    >>> userNameToFileName(u"A.Alt")
    u'A_.A_lt'
    >>> userNameToFileName(u"A.aLt")
    u'A_.aL_t'
    >>> userNameToFileName(u"A.alT")
    u'A_.alT_'
    >>> userNameToFileName(u"T_H")
    u'T__H_'
    >>> userNameToFileName(u"T_h")
    u'T__h'
    >>> userNameToFileName(u"t_h")
    u't_h'
    >>> userNameToFileName(u"F_F_I")
    u'F__F__I_'
    >>> userNameToFileName(u"f_f_i")
    u'f_f_i'
    >>> userNameToFileName(u"Aacute_V.swash")
    u'A_acute_V_.swash'
    >>> userNameToFileName(u".notdef")
    u'_notdef'
    >>> userNameToFileName(u"con")
    u'_con'
    >>> userNameToFileName(u"CON")
    u'C_O_N_'
    >>> userNameToFileName(u"con.alt")
    u'_con.alt'
    >>> userNameToFileName(u"alt.con")
    u'alt._con'
    """
    # the incoming name must be a unicode string
    assert isinstance(userName, unicode),
        "The value for userName must be a unicode string."
    # establish the prefix and suffix lengths
    prefixLength = len(prefix)
    suffixLength = len(suffix)
    # replace an initial period with an _
    # if no prefix is to be added
    if not prefix and userName[0] == ".":
        userName = "_" + userName[1:]
    # filter the user name
    filteredUserName = []
    for character in userName:
        # replace illegal characters with _
        if character in illegalCharacters:
            character = "_"
        # add _ to all non-lower characters
        elif character != character.lower():
            character += "_"
        filteredUserName.append(character)
    userName = "".join(filteredUserName)
    # clip to 255
    sliceLength = maxFileNameLength - prefixLength - suffixLength
    userName = userName[:sliceLength]
    # test for illegal files names
    parts = []
    for part in userName.split("."):
        if part.lower() in reservedFileNames:
            part = "_" + part
        parts.append(part)
    userName = ".".join(parts)
    # test for clash
    fullName = prefix + userName + suffix
    if fullName.lower() in existing:
        fullName = handleClash1(userName, existing, prefix, suffix)
    # finished
    return fullName

def handleClash1(userName, existing=[], prefix="", suffix=""):
    """
    existing should be a case-insensitive list
    of all existing file names.

    >>> prefix = ("0" * 5) + "."
    >>> suffix = "." + ("0" * 10)
    >>> existing = ["a" * 5]

    >>> e = list(existing)
    >>> handleClash1(userName="A" * 5, existing=e,
    ...     prefix=prefix, suffix=suffix)
    '00000.AAAAA000000000000001.0000000000'

    >>> e = list(existing)
    >>> e.append(prefix + "aaaaa" + "1".zfill(15) + suffix)
    >>> handleClash1(userName="A" * 5, existing=e,
    ...     prefix=prefix, suffix=suffix)
    '00000.AAAAA000000000000002.0000000000'

    >>> e = list(existing)
    >>> e.append(prefix + "AAAAA" + "2".zfill(15) + suffix)
    >>> handleClash1(userName="A" * 5, existing=e,
    ...     prefix=prefix, suffix=suffix)
    '00000.AAAAA000000000000001.0000000000'
    """
    # if the prefix length + user name length + suffix length + 15 is at
    # or past the maximum length, silce 15 characters off of the user name
    prefixLength = len(prefix)
    suffixLength = len(suffix)
    if prefixLength + len(userName) + suffixLength + 15 > maxFileNameLength:
        l = (prefixLength + len(userName) + suffixLength + 15)
        sliceLength = maxFileNameLength - l
        userName = userName[:sliceLength]
    finalName = None
    # try to add numbers to create a unique name
    counter = 1
    while finalName is None:
        name = userName + str(counter).zfill(15)
        fullName = prefix + name + suffix
        if fullName.lower() not in existing:
            finalName = fullName
            break
        else:
            counter += 1
        if counter >= 999999999999999:
            break
    # if there is a clash, go to the next fallback
    if finalName is None:
        finalName = handleClash2(existing, prefix, suffix)
    # finished
    return finalName

def handleClash2(existing=[], prefix="", suffix=""):
    """
    existing should be a case-insensitive list
    of all existing file names.

    >>> prefix = ("0" * 5) + "."
    >>> suffix = "." + ("0" * 10)
    >>> existing = [prefix + str(i) + suffix for i in range(100)]

    >>> e = list(existing)
    >>> handleClash2(existing=e, prefix=prefix, suffix=suffix)
    '00000.100.0000000000'

    >>> e = list(existing)
    >>> e.remove(prefix + "1" + suffix)
    >>> handleClash2(existing=e, prefix=prefix, suffix=suffix)
    '00000.1.0000000000'

    >>> e = list(existing)
    >>> e.remove(prefix + "2" + suffix)
    >>> handleClash2(existing=e, prefix=prefix, suffix=suffix)
    '00000.2.0000000000'
    """
    # calculate the longest possible string
    maxLength = maxFileNameLength - len(prefix) - len(suffix)
    maxValue = int("9" * maxLength)
    # try to find a number
    finalName = None
    counter = 1
    while finalName is None:
        fullName = prefix + str(counter) + suffix
        if fullName.lower() not in existing:
            finalName = fullName
            break
        else:
            counter += 1
        if counter >= maxValue:
            break
    # raise an error if nothing has been found
    if finalName is None:
        raise NameTranslationError("No unique name could be found.")
    # finished
    return finalName
```

### Identifiers

Identifiers are optional attributes of several objects in the UFO. These identifiers are required to be unique within certain contexts as defined on a per object basis throughout this specification. Identifiers are specified as a string between one and 100 characters long. All characters must be in the printable ASCII range, 0x20 to 0x7E.

There is no standard identifier generation algorithm. Random strings, simple numbers, UUIDs, time stamps and more may be used. An example algorithm for generating identifiers that are random strings is detailed below.

#### Example Algorithm

This algorithm is designed to generate a unique identifier that is a unique string consisting of 10 characters from 0-9, A-Z and a-z. This allows a glyph to contain 10<sup>62</sup> points that follow this identifier naming scheme.

{: .algorithmdiagram}
-   *possible characters* includes 0-9, A-Z and a-z.
-   *existing identifiers* is a list of all existing identifiers in the glyph.
-   *identifier* a 10 character long string of characters randomly selected from *possible characters*.
-   If *identifier* is not in *existing identifiers*:
-   -   Stop.
-   If *identifier* is in *existing identifiers*:
-   -   Repeat this process until a unique identifier is found.

#### Example implementation:

```python
import random

characters = list("0123456789")
characters += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
characters += list("abcdefghijklmnopqrstuvwxyz")
identifierLength = 10
identifierRange = range(identifierLength)

def makeRandomIdentifier(existing, recursionDepth=0):
    if recursionDepth >= 50:
        raise NotImplementedError,\
            "Failed 50 times in a row to create a unique id. Sorry."
    identifier = []
    for i in identifierRange:
        c = random.choice(characters)
        identifier.append(c)
    identifier = "".join(identifier)
    if identifier in existing:
        return makeRandomIdentifier(existing, recursionDepth+1)
    else:
        return identifier

```

  [A DTD is available.]: http://www.apple.com/DTDs/PropertyList-1.0.dtd
  [sRGB]: http://en.wikipedia.org/wiki/SRGB
  [reverse domain naming system]: http://en.wikipedia.org/wiki/Reverse-DNS
  [MS-DOS reserved file names]: http://support.microsoft.com/kb/74496/en-us
