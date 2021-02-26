---
layout: default
title: Glyph Interchange Format
---

{: .fileformat}
| **File Format** | XML |

The Glyph Interchange Format (GLIF) is a simple and clear XML representation of a single glyph. GLIF files typically have a *.glif* extension.

The GLIF data follows this structure:


{: .filediagram}
- glyph
- advance
- unicode
- note
- image
- guideline
- anchor
- outline
  - contour
    - point
  - component
- lib

## Specification

In all elements, where an attribute has a defined default value the attribute is optional unless otherwise stated. If the attribute is not defined, the value for the attribute is implicitly the default value.

{: #glyph }
### glyph: The top level element.

#### Attributes

{: .name-description}
| name | description |
|--|--|
| name | The name of the glyph. This must be at least one character long. Names must not contain [control characters]. Different font specifications, such as OpenType, often have their own glyph name restrictions. Authoring tools should not make assumptions about the validity of a glyph's name for a particular font specification. |
| format | The major format version. 2 for this version. |
| formatMinor | The minor format version. Optional if the minor version is 0, must be present if the minor version is not 0. |

The `name` attribute has limited uses in this version. The *contents.plist* file maps glyph names to file names, and one of the reasons to do this is to avoid having to parse all files just to get at a list of available glyph names. When reading GLIF files, the `name` attribute should be ignored, since manual editing may have caused a mismatch with the glyph name as stored in *contents.plist*, as well as with the file name, which is an algorithmic transformation of the glyph name. This attribute may become more useful in future versions of GLIF.

#### Child Elements

{: .name-description}
| name | description |
|--|--|
| [advance] | May occur at most once. |
| [unicode] | May occur any number of times. |
| [note] | May occur at most once. |
| [image] | May occur at most once. |
| [guideline] | May occur any number of times. |
| [anchor] | May occur any number of times. |
| [outline] | May occur at most once. |
| [lib] | May occur at most once. |

{: #advance }
### advance: Horizontal and vertical metrics.

#### Attributes

{: .name-type-description-default}
| name | type | description | default |
|--|--|--|--|
| width | integer or float | The advance width. Optional if *height* is defined. | 0 |
| height | integer or float | The vertical advance. Optional if *width* is defined. | 0 |

#### This element has no child elements.

#### Example

```xml
<advance width="400" />
```

{: #unicode }
### unicode: Unicode code point.

#### Attributes

{: .name-type-description}
| name | type | description |
|--|--|--|
| hex | string | A unicode code point as a hexadecimal number. The string is case-insensitive and must contain the hex value without a prefix. |

#### This element has no child elements.

The first occurrence of this element defines the primary Unicode value for this glyph.

#### Example

```xml
<unicode hex="0041" />
```

{: #image }
### image: An image reference.

This optional element represents an image element in a glyph. It may occur at most once. The image should always be considered to be *behind* the outline element.

#### Attributes

{: .name-type-description-default}
| name | type | description | default |
|--|--|--|--|
| fileName | string | The image file name, including any file extension, not an absolute or relative path in the file system. | None |
| xScale | integer or float | See below. | 1 |
| xyScale | integer or float | See below. | 0 |
| yxScale | integer or float | See below. | 0 |
| yScale | integer or float | See below. | 1 |
| xOffset | integer or float | See below. | 0 |
| yOffset | integer or float | See below. | 0 |
| color | string | The color that should be applied to the image. The format follows the [color definition] standard. This attribute is optional. | no color |

`xScale, xyScale, yxScale, yScale, xOffset, yOffset` taken together in that order form an Affine transformation matrix, to be used to transform the image. The default matrix is `[1 0 0 1 0 0]`, the identity transformation.

One image width unit equals one horizontal font unit and one image height unit equals one vertical font unit **before** `xScale, xyScale, yxScale, yScale, xOffset, yOffset` are applied.

#### This element has no child elements.

#### Format

All images must be in Portable Network Graphics (PNG) format.

#### Coloring Images

There are two places that the color for an image can be defined: the color attribute of the image element and the `color` defined in [layerinfo.plist]. The color defined in the image element's color attribute always takes precedence. If that is not defined and the `color` is defined for the layer, the layer's `color` should be used. If both of these are undefined, the image's colors, without modification, should be used unless an authoring tool has a default color for images. If a color is to be applied, the authoring tool should convert the image to grayscale and then apply the color. This modified version of the image must not be saved into the images directory.

#### Example

```xml
<image fileName="Sketch 1.png" xOffset="100" yOffset="200"
    xScale=".75" yScale=".75" color="1,0,0,.5" />

```

{: #guideline }
### guideline: A reference guideline.

This element may occur any number of times.

#### Attributes

{: .name-type-description-default}
| name | type | description | default |
|--|--|--|--|
| x | integer or float | The 'x' coordinate. See below for details. | 0 |
| y | integer or float | The 'y' coordinate. See below for details. | 0 |
| angle | integer or float | The angle of the guideline. This must be an angle between 0 and 360 degrees in a counter-clockwise direction from the horizontal. See below for details. | 0 |
| name | string | An arbitrary name for the guideline. This attribute is optional. Name must not contain [control characters]. | no name |
| color | string | The color that should be applied to the guideline. The format follows the [color definition] standard. This attribute is optional. | no color |
| identifier | string | Unique identifier for the guideline. This attribute is not required and should only be added to guidelines as needed. However, once an identifier has been assigned to a guideline it must not be unnecessarily removed or changed. Identifiers may be changed in incoming guidelines during editing operations such as "paste," but they should be maintained unless a duplicate identifier will be created. The identifier value must be unique within all identifiers (including identifiers for elements other than guidelines) in the glyph that the guideline belongs to but it is not required to be unique among the identifiers assigned in other glyphs or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

The guideline extends along `angle` to infinity in both directions out of the point defined by `x` and `y`.

#### This element has no child elements.

{: #anchor }
### anchor: A reference position.

This element may occur any number of times.

#### Attributes

{: .name-type-description-default}
| name | type | description | default |
|--|--|--|--|
| x | integer or float | The 'x' coordinate. | None |
| y | integer or float | The 'y' coordinate. | None |
| name | string | An arbitrary name for the anchor. This attribute is optional. Name must not contain [control characters]. | no name |
| color | string | The color that should be applied to the anchor. The format follows the [color definition] standard. This attribute is optional. | no color |
| identifier | string | Unique identifier for the anchor. This attribute is not required and should only be added to anchors as needed. However, once an identifier has been assigned to an anchor it must not be unnecessarily removed or changed. Identifiers may be changed in incoming anchors during editing operations such as "paste," but they should be maintained unless a duplicate identifier will be created. The identifier value must be unique within all identifiers (including identifiers for elements other than anchors) in the glyph that the anchor belongs to but it is not required to be unique among the identifiers assigned in other glyphs or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

#### This element has no child elements.

#### Anchor naming conventions

The following are agreed upon standard naming conventions for special uses of the `name` attribute.

##### Ligature Carets

Anchors with a `name` starting with `caret_` or `vcaret_` indicate horizontal or vertical caret positions for ligature glyphs. Example usage would be to compile the [OpenType GDEF Ligature Caret List table]. 

Anchor names starting with `caret_` provide the `x` value for a ligature caret position, and the `y` value is ignored. Likewise, anchor names starting with `vcaret_` provide the `y` value for a ligature caret position, and the `x` value is ignored.

Both names may be followed arbitrary text (`caret_1`, `caret_blah`, etc) for designers or applications to have unique caret position names.

There must be exactly N-1 caret positions for N ligature components.

#### Converting implied anchors in GLIF 1 to GLIF 2 anchor elements

In GLIF 1 there was no official anchor element. Anchors were unofficially but widely supported through the use of a contour containing only one "move" point. For example:

```xml
<contour>
  <point x="250" y="650" type="move" name="top"/>
</contour>

```

Authoring tools may convert instances of contours like this to anchor elements when converting GLIF 1 to GLIF 2. The required `x` and `y` and optional `name` attributes directly map to the same attributes of the anchor element.

{: #outline }
### outline: Outline description.

#### This element has no attributes.

#### Child Elements

{: .name-description}
| name | description |
|--|--|
| [component] | May occur any number of times. |
| [contour] | May occur any number of times. |

{: #component }
### component: Insert another glyph as part of the outline.

#### Attributes

{: .name-type-description-default}
| name | type | description | default |
|--|--|--|--|
| base | string | Name of the base glyph | None |
| xScale | integer or float | See below. | 1 |
| xyScale | integer or float | See below. | 0 |
| yxScale | integer or float | See below. | 0 |
| yScale | integer or float | See below. | 1 |
| xOffset | integer or float | See below. | 0 |
| yOffset | integer or float | See below. | 0 |
| identifier | string | Unique identifier for the component. This attribute is not required and should only be added to components as needed. However, once an identifier has been assigned to a component it must not be unnecessarily removed or changed. Identifiers may be changed in incoming components during editing operations such as "paste," but they should be maintained unless a duplicate identifier will be created. The identifier value must be unique within all identifiers (including identifiers for elements other than components) in the glyph that the component belongs to but it is not required to be unique among the identifiers assigned in other glyphs, in any layerinfo.plist or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

`xScale, xyScale, yxScale, yScale, xOffset, yOffset` taken together in that order form an Affine transformation matrix, to be used to transform the base glyph. The default matrix is `[1 0 0 1 0 0]`, the identity transformation.

The base glyph referenced by a component may contain components. The base glyph must not create a circular reference to the glyph that contains the component. Components must only reference glyphs within the same layer that the component belongs to.

#### This element has no child elements.

#### Example

```xml
<component base="A" xOffset="100" />
```

{: #contour }
### contour: Contour description.

#### Attributes

{: .name-type-description-default}
| name | type | description | default |
|--|--|--|--|
| identifier | string | Unique identifier for the contour. This attribute is not required and should only be added to contours as needed. However, once an identifier has been assigned to a contour it must not be unnecessarily removed or changed. Identifiers may be changed in incoming contours during editing operations such as "paste" and component decomposition, but they should be maintained unless a duplicate identifier will be created. Identifiers should also be retained when possible during outline manipulation operations such as path direction changes and remove overlap. The identifier value must be unique within all identifiers (including identifiers for elements other than contours) in the glyph that the contour belongs to but it is not required to be unique among the identifiers assigned in other glyphs, in any layerinfo.plist or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

#### Child Elements

{: .name-description}
| name | description |
|--|--|
| [point] | May occur any number of times. |

There is no requirement that a contour contain an on-curve point. If a contour contains only off-curve points the contour must be treated as a quadratic curve.

{: #point }
### point: An attributed coordinate pair.

#### Attributes

{: .name-type-description-default}
| name | type | description | default |
|--|--|--|--|
| x | integer or float | The 'x' coordinate. | None |
| y | integer or float | The 'y' coordinate. | None |
| type | string | The point and/or segment type. The options are detailed below. | offcurve |
| smooth | string | This attribute must only be given when `type` indicates the point is on-curve. When set to `yes`, it signifies that a smooth curvature should be maintained at this point, either as a `curve point` or a `tangent point` in Fontographer terms. This attribute may be set for all point types except `offcurve`. | no |
| name | string | Arbitrary name or label for this point. The name does not have to be unique within a contour, nor within an outline. Name must not contain [control characters]. | no name |
| identifier | string | Unique identifier for the point. This attribute is not required and should only be added to points as needed. However, once an identifier has been assigned to a point it must not be unnecessarily removed or changed. Identifiers may be changed in incoming points during editing operations such as "paste" and component decomposition, but they should be maintained unless a duplicate identifier will be created. Identifiers should also be retained when possible during outline manipulation operations such as path direction changes and remove overlap. The identifier value must be unique within all identifiers (including identifiers for elements other than poinys) in the glyph that the point belongs to but it is not required to be unique among the identifiers assigned in other glyphs, in any layerinfo.plist or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

##### Point Types


{: .name-description}
| name | description |
|--|--|
| move | A point of this type must be the first in a `contour`. The reverse is not true: a `contour` does not necessarily start with a `move` point. When a `contour` **does** start with a `move` point, it signifies the beginning of an **open** contour. A **closed** contour does **not** start with a `move` and is defined as a cyclic list of points, with no predominant start point. There is always a *next point* and a *previous point*. For this purpose the list of points can be seen as endless in both directions. The actual list of points can be rotated arbitrarily (by removing the first N points and appending them at the end) while still describing the same outline. |
| line | Draw a straight line from the previous point to this point. The previous point must be a `move`, a `line`, a `curve` or a `qcurve`. It must not be an `offcurve`. |
| offcurve | This point is part of a curve segment that goes up to the next point that is either a `curve` or a `qcurve`. |
| curve | Draw a cubic bezier curve from the last non-*offcurve* point to this point. The number of *offcurve* points can be zero, one or two. If the number of `offcurve` points is zero, a straight line is drawn. If it is one, a quadratic curve is drawn. If it is two, a regular cubic bezier is drawn. |
| qcurve | Similar to curve, but uses quadratic curves, using the TrueType "implied on-curve points" principle. |

#### This element has no child elements.

#### Examples

move point:

```xml
<point x="433" y="371" type="move" />
```

line point:

```xml
<point x="433" y="371" type="line" />
```

offcurve point:

```xml
<point x="433" y="366" />
```

curve point:

```xml
<point x="441" y="363" type="curve" smooth="yes" />
```

qcurve point:

```xml
<point x="441" y="363" type="qcurve" />
```

{: #note }
### note: Note about the glyph.

This element is a place for the user to define arbitrary text about the glyph. There is no standardized structure for the note apart from that it being the content of the note element.

{: #lib }
### lib: Custom data storage.

This element is a place to store authoring tool specific, user specific or otherwise arbitrary data for the glyph. lib must have one child element that is structure as a dictionary formatted as an [XML Property List]. This element may occur at most once. In order to prevent conflicts in the lib, keys in the top level should follow a [reverse domain naming scheme]. The pattern "public.\*", where \* represents an arbitrary string of one or more characters, is reserved for use in standardized lib keys. It is recommended that the data stored as a value be as shallow as possible.

Data that is too complex or too large for lib can be stored in the [data directory].

#### Common Key Registry

The following is a registry of public lib keys that map to functionality that is often seen in font editing applications but is not suitable for storage elsewhere in this particular version of the UFO.

##### public.markColor

This key is used for representing the "mark" color seen in various font editors. The value for the key must be a string following the [color definition] standard. This data is optional.

##### public.truetype.instructions

This key provides a dict defining a set of TrueType instructions assembly code for a glyph.
This data is optional.

```xml
<key>public.truetype.instructions</key>
<dict>
  <key>formatVersion</key>
  <string>1</string>
  <key>id</key>
  <string>fb063b7cbc6859d5e9bd61651e10cbc27b8362c296d3b9fcecaadbf60999b038cae7f3716e9815f9766af29e167e12e89e9e2334a710cd8ce621218f0534f585</string>
  <key>assembly</key>
  <string>
PUSHB[ ]        /* 3 values pushed */
0
4
5
SRP1[ ] /* SetRefPoint1 */
SRP2[ ] /* SetRefPoint2 */
IP[ ]   /* InterpolatePts */
SVTCA[0]        /* SetFPVectorToAxis */
PUSHB[ ]        /* 1 value pushed */
0
MDAP[1] /* MoveDirectAbsPt */
PUSHB[ ]        /* 2 values pushed */
2
1
PUSHB[ ]        /* 1 value pushed */
10
CALL[ ] /* CallFunction */
IF[ ]   /* If */
POP[ ]  /* PopTopStack */
MDRP[11000]     /* MoveDirectRelPt */
ELSE[ ] /* Else */
MIRP[10100]     /* MoveIndirectRelPt */
EIF[ ]  /* EndIf */
IUP[0]  /* InterpolateUntPts */
IUP[1]  /* InterpolateUntPts */
  </string>
</dict>
```

###### TrueType Instructions Dict

{: .name-type-description }
| key | type | description |
|--|--|--|
| formatVersion | string | Format version. Set to "1". |
| id | string | Hash of glyph outlines which may have been processed by authoring tools. This is computed when the instructions dict is created or modified. It is used to determine if the glyph outlines have changed since the glyph was hinted: if it has, then the instructions for the glyph should not be used by authoring tools. See "Hint ID Computation" below. |
| assembly | string | TrueType instructions assembly as a string. The assembly is represented by a single string of fontTools TrueType instructions assembly with optional line formatting between instructions. |

#### public.truetype.overlap

This key is a boolean used for indicating the glyph contours or components may have overlap.
Authoring tools may use this to set bit 6 (OVERLAP_SIMPLE) in the TrueType Simple Glyph flags or bit 10 (OVERLAP_COMPOUND) in the TrueType Composite Glyph flags listed in the [OpenType glyf Simple Glyph Description] and the [OpenType glyf Composite Glyph Description]. Authoring tools may ignore or override this data. This data is optional.

##### public.verticalOrigin

This key is used for representing the "vertical origin" 'y' coordinate used for vertical layout. The value for the key must be an integer or float. This data is optional. Authoring tools can use this data and the advance element's `height` attribute to create the VORG and vmtx tables.

##### public.postscript.hints

This key provides a dict defining a set of PostScript hints for a glyph. The key is optional. Note that the set of hints become invalid whenever the outline is edited so as to change point types or coordinates. Rather than requiring all editing apps to remove hints whenever the outline is changed, the hint dict "id" is provided so that a third party can see if the current outline differs from what was present when the hints were last derived. If the hash for the current outline differs from the hint dict "id" value, then the hints are invalid for the current outline, and should be discarded.

###### Hint Dict

{: .name-type-description}
| key | type | description |
|--|--|--|
| formatVersion | string | format version. Currently "1", the first public version. |
| id | string | Hash of glyph outlines. This is computed when the glyph is hinted. It is used to determine if the glyph outline has been changed since the glyph was hinted: if it has, then the hint dict for the glyph should be deleted. See "Hint ID Computation" below. |
| hintSetList | list | List of hint sets. A hint set is a dict containing a list of hints, and a unique point name which identifies the point after which the hint set is applied. |
| flexList | string | List of unique point names. Each point name identifies the point at which a flex hint starts. |

###### Hint Set

{: .name-type-description}
| key | type | description |
|--|--|--|
| pointTag | string | unique point name. Must match a point 'name' attribute. |
| stems | list of strings | list of stem strings. Each stem string starts with either 'hstem" or "vstem" and is a followed by a series of white-space delimited stem coordinate values. A stem coordinate value is an absolute coordinate. There must be an even number of stem coordinates: each pair of values defines a lower and upper edge of a stem hint. The stems must be sorted in ascending order of lower edge values. 'hstem' strings must be sorted before 'vstem' strings. |

*Hint ID computation.* The hash string is initialized with the width value as a
decimal string, with the prefix w'. The glyph outline element is converted to a
string by iterating through all the child elements.

If the child is a contour element, it is converted to a string and added to the
hash string by iterating through all the point elements. Any contour with a
length of less than 2 is skipped. For each point, the point 'type' attribute, if
present, is written; else a space is written. The x and y values are then
written as decimal strings separated by a comma. The x and y values are rounded
to a precision of no more than 3 decimal places.

If the child is a component element, first the transform values are written, if
any. These are written by writing 't' followed by the comma-separated decimal
values of the transform attributes in the following order: ["xScale", "xyScale",
"yxScale","yScale", "xOffset", "yOffset"]. The letter 'h' is then written,
followed by the hash ID for the component glyph. The four scale values will be
rounded to a precision of 8 decimal places, and the offset values will be
rounded to a precision of at most 3 decimal places.

Once the hash string is built, it is used as is for the Hint ID if it is less
than 128 characters. Otherwise, a SHA 512 hash is computed, and this is used as
the Hint ID for the hint dict. The SHA 512 hash is written with lowercase
hexidecimal digits.

##### public.objectLibs

This key provides a dictionary of data containing object-level lib data for individual contours, points, components, anchors or guidelines within the glyph that this lib belongs to. The dictionary is structured with object identifiers that correspond to objects in the glyph as keys and object-level dictionaries as values. Within each of these of these object-level dictionaries, keys should follow a [reverse domain naming scheme]. The pattern "public.\*", where `*` represents an arbitrary string of one or more characters, is reserved for use in standardized lib keys. It is recommended that the data stored as a value be as shallow as possible. If a key in this dictionary is not an identifier of any object within this glyph, the key and value may be discarded.

```xml
<key>public.objectLibs</key>
<dict>
  <key>KN3WZjorob</key>
  <dict>
    <key>com.foundry.pointColor</key>
    <string>0,1,0,0.5</string>
  </dict>
  <key>h0ablXAzTg</key>
  <dict>
    <key>com.foundry.pointColor</key>
    <string>1,0,0,0.5</string>
  </dict>
  <key>vMlVuTQd4d</key>
  <dict>
    <key>com.foundry.contourColor</key>
    <string>1,0,0,0.5</string>
  </dict>
</dict>
```

##### Standardized object lib keys

{: .name-type-description }
| key | type | description |
|--|--|--|
| public.truetype.roundOffsetToGrid | boolean | This key is used in a component object-level dictionary and, when set to true, indicates bit 2 (ROUND_XY_TO_GRID) listed in the [OpenType glyf Composite Glyph Description] should be set for the component the Component Glyph flags in TrueType binaries. Authoring tools may ignore this data. This data is optional.
| public.truetype.useMyMetrics | boolean | This key is used in a component object-level dictionary and, when set to true, indicates bit 9 (USE_MY_METRICS) listed in the [OpenType glyf Composite Glyph Description] should be set for the component in the Component Glyph flags in TrueType binaries. It may be used to update the `xOffset, yOffset` of the component and the `width`, `height` and `verticalOrigin` of the glyph it is in. Authoring tools may ignore this data. This data is optional.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<glyph name="period" format="2">
  <advance width="268"/>
  <unicode hex="002E"/>
  <image fileName="period sketch.png" xScale="0.5" yScale="0.5"/>
  <guideline y="-12" name="overshoot"/>
  <anchor x="74" y="197" name="top"/>
  <outline>
    <contour identifier="vMlVuTQd4d">
      <point x="237" y="152"/>
      <point x="193" y="187"/>
      <point x="134" y="187" type="curve" smooth="yes" identifier="KN3WZjorob"/>
      <point x="74" y="187"/>
      <point x="30" y="150"/>
      <point x="30" y="88" type="curve" smooth="yes"/>
      <point x="30" y="23"/>
      <point x="74" y="-10"/>
      <point x="134" y="-10" type="curve" smooth="yes"/>
      <point x="193" y="-10"/>
      <point x="237" y="25"/>
      <point x="237" y="88" type="curve" smooth="yes" identifier="h0ablXAzTg"/>
    </contour>
  </outline>
  <lib>
    <dict>
      <key>com.letterror.somestuff</key>
      <string>arbitrary custom data!</string>
      <key>public.markColor</key>
      <string>1,0,0,0.5</string>
      <key>public.objectLibs</key>
      <dict>
        <key>KN3WZjorob</key>
        <dict>
          <key>com.foundry.pointColor</key>
          <string>0,1,0,0.5</string>
        </dict>
        <key>h0ablXAzTg</key>
        <dict>
          <key>com.foundry.pointColor</key>
          <string>1,0,0,0.5</string>
        </dict>
        <key>vMlVuTQd4d</key>
        <dict>
          <key>com.foundry.contourColor</key>
          <string>1,0,0,0.5</string>
        </dict>
      </dict>
      <key>public.postscript.hints</key>
      <dict>
        <key>formatVersion</key>
        <string>1</string>
        <key>hintSetList</key>
        <array>
          <dict>
            <key>pointTag</key>
            <string>hintSet0000</string>
            <key>stems</key>
            <array>
              <string>hstem -10 197</string>
              <string>vstem 30 207</string>
            </array>
          </dict>
          <dict>
            <key>pointTag</key>
            <string>hintSet0004</string>
            <key>stems</key>
            <array>
              <string>hstem 11 -21</string>
              <string>vstem 30 207</string>
            </array>
          </dict>
        </array>
        <key>id</key>
        <string>w268c237,88 237,152 193,187c134,187 74,187 30,150c30,88 30,23 74,-10c134,-10 193,-10 237,25</string>
      </dict>
    </dict>
  </lib>
</glyph>
```

  [advance]: #advance
  [unicode]: #unicode
  [note]: #note
  [image]: #image
  [guideline]: #guideline
  [anchor]: #anchor
  [outline]: #outline
  [lib]: #lib
  [color definition]: ../../conventions/#colors
  [layerinfo.plist]: ../layerinfo.plist
  [conventions]: ../../conventions/#identifiers
  [component]: #component
  [contour]: #contour
  [point]: #point
  [XML Property List]: ../../conventions/#xml-property-lists
  [reverse domain naming scheme]: ../../conventions/#reverse-domain-naming-schemes
  [data directory]: ../../data
  [OpenType GDEF Ligature Caret List table]: https://docs.microsoft.com/en-us/typography/opentype/spec/gdef#ligature-caret-list-table-overview
  [OpenType glyf Composite Glyph Description]: https://docs.microsoft.com/en-us/typography/opentype/spec/glyf#composite-glyph-description
  [OpenType glyf Simple Glyph Description]: https://docs.microsoft.com/en-us/typography/opentype/spec/glyf#simple-glyph-description
  [control characters]: ../../conventions/#controls
