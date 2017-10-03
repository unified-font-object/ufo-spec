---
layout: default
title: lib.plist
---

| **File Format** | [XML Property List](http://www.apple.com/DTDs/PropertyList-1.0.dtd) |

This file is a place to store authoring tool specific, user specific or otherwise arbitrary data for the font. It is optional. If it is not defined in the UFO, there is no lib data.

Data that is too complex or too large for the lib can be stored in the [data directory].

## Specification

The property list data consists of a dictionary at the top level. In order to prevent conflicts in the lib, keys in the top level should follow a [reverse domain naming scheme]. The pattern "public.\*", where \* represents an arbitrary string of one or more characters, is reserved for use in standardized lib keys. It is recommended that the data stored as a value be as shallow as possible.

### Common Key Registry

The following is a registry of public lib keys that map to functionality that is often seen in font editing applications but is not suitable for storage elsewhere in this particular version of the UFO.

#### public.glyphOrder

This key is used for representing the user's preferred glyph order in the font. Authoring tools may use this order for displaying glyphs to the user or setting the glyph order in binaries created with the font data. However, authoring tools are not required to use this order in any way. This data is optional.

The glyph order is stored as a list of glyphs names. Glyph names must not occur more than once. Glyph names in the font may not appear in the order. The order may contain glyphs that are not in the font.

#### public.postscriptNames

This defines a preferred glyph name to Postscript glyph name mapping for glyphs in the font. Authoring tools should use the values defined in this mapping when outputting font data formats such as the `post` and `CFF ` tables in OpenType. This data is optional.

The mapping is stored as a dictionary with glyphs names as keys and Postscript glyph names as values. Both keys and values must be strings. The values must conform to the Postscript glyph naming specification. The dictionary may contain glyph names that are not in the font. The dictionary may not contain a key, value pair for all glyphs in the font. If a glyph's name is not defined in this mapping, the glyph's name should be used as the Postscript name.

#### public.postscript.hints

This key provides a mapping from glyph names to sets of PostScript hints for the
default glyph layer. The mapping is stored as a dictionary with glyph names as
keys and Postscript hint sets as values. If a glyph's name is missing from the
mapping, then there are no Postscript hints for that glyph.

Any mapping from glyph names to sets of PostScript hints for any layer other
than the default layer is stored in the layerinfo.plist for the layer, using the
same key.

#### Hint Dict

| key         | value type | description                                                                                                                                                                                                                                                  |
|-------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id          | string     | Hash of glyph outlines. This is computed when the glyph is hinted. It is used to determine if the glyph outline has been changed since the glyph was hinted: if it has, then the hint dict for the glyph should be deleted. See "Hint ID Computation" below. |
| hintSetList | list       | List of hint sets. A hint set is a dict containing a list of hints, and a unique point name which identifies the point after which the hint set is applied.                                                                                                  |
| flexList    | string     | List of unique point names. Each point name identifies the point at which a flex hint starts.                                                                                                                                                                |

#### Hint Set

| key      | value type      | description                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| pointTag | string          | unique point name.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| stems    | list of strings | list of stem strings. Each stem string starts with either 'hstem" or "vstem" and is a followed by a series of white-space delimited stem coordinate values. A stem coordinate value is an absolute coordinate. There must be an even number of stem coordinates: each pair of values defines a lower and upper edge of a stem hint. The stems must be sorted in ascending order of lower edge values. 'hstem' strings must be sorted before 'vstem' strings. |

*Hint ID computation.* The glyph is flattened to a single set of contours, with
all transformations. The contours are converted to a string by iterating through
all the points. For each point in each contour, the GLIF point type is appended,
then the x and y value are converted to decimal strings and appended; white
space is omitted. Any contour with a length of less than 2 is skipped. The glyph
width is pre-pended after being converted to a decimal string.

For each component, the string "base:" is appended to the string. The hash
function is then applied to the component glyph, and the hash string for the
component glyph is then appended to the hash string for the parent glyph.

Once the hash string is built, it is used as is for the Hint ID if it is less
than 128 characters. Otherwise, a SHA 512 hash is computer, and this is used as
the Hint ID for the hint dict.

 

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>org.robofab.scripts.SomeData</key>
  <string>Hello World.</string>
  <key>public.glyphOrder</key>
  <array>
    <string>A</string>
    <string>C</string>
    <string>B</string>
  </array>
  <key>public.postscript.hints</key>
    <dict>
        <key>id</key><string>64bf4987f05ced2a50195f971cd924984047eb1d79c8c43e6a0054f59cc85dea23a49deb20946a4ea84840534363f7a13cca31a81b1e7e33c832185173369086</string>
      <key>hintSetList</key>
      <array>
        <dict>
          <key>pointTag</key>
          <string>hintSet0000</string>
          <key>stems</key>
          <array>
            <string>hstem 338 28</string>
            <string>hstem 632 28</string>
            <string>hstem 100 32</string>
            <string>hstem 496 32</string>
          </array>
        </dict>
        <dict>
          <key>pointTag</key>
          <string>hintSet0005</string>
          <key>stems</key>
          <array>
            <string>hstem 0 28</string>
            <string>hstem 338 28</string>
            <string>hstem 632 28</string>
            <string>hstem 100 32</string>
            <string>hstem 454 32</string>
            <string>hstem 496 32</string>
          </array>
        </dict>
        <dict>
          <key>pointTag</key>
          <string>hintSet0016</string>
          <key>stems</key>
          <array>
            <string>hstem 0 28</string>
            <string>hstem 338 28</string>
            <string>hstem 632 28</string>
            <string>hstem 100 32</string>
            <string>hstem 496 32</string>
          </array>
        </dict>
      </array>
    </dict>
  </dict>
</plist>
```

  [XML Property List]: conventions.html#propertylist
  [data directory]: data.html
  [reverse domain naming scheme]: conventions.html#reversedomain
