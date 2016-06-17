---
layout: default
title: Glyph Interchange Format
---

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

| attribute name | description                                                                                                                                                                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name           | The name of the glyph. This must be at least one character long. Different font specifications, such as OpenType, often have their own glyph name restrictions. Authoring tools should not make assumptions about the validity of a glyph's name for a particular font specification. |
| format         | The format version. 2 for this version.                                                                                                                                                                                                                                               |

The `name` attribute has limited uses in this version. The *contents.plist* file maps glyph names to file names, and one of the reasons to do this is to avoid having to parse all files just to get at a list of available glyph names. When reading GLIF files, the `name` attribute should be ignored, since manual editing may have caused a mismatch with the glyph name as stored in *contents.plist*, as well as with the file name, which is an algorithmic transformation of the glyph name. This attribute may become more useful in future versions of GLIF.

#### Child Elements

| element name | description                    |
|--------------|--------------------------------|
| [advance]    | May occur at most once.        |
| [unicode]    | May occur any number of times. |
| [note]       | May occur at most once.        |
| [image]      | May occur at most once.        |
| [guideline]  | May occur any number of times. |
| [anchor]     | May occur any number of times. |
| [outline]    | May occur at most once.        |
| [lib]        | May occur at most once.        |

{: #advance }
### advance: Horizontal and vertical metrics.

#### Attributes

| attribute name | data type        | description                                           | default value |
|----------------|------------------|-------------------------------------------------------|---------------|
| width          | integer or float | The advance width. Optional if *height* is defined.   | 0             |
| height         | integer or float | The vertical advance. Optional if *width* is defined. | 0             |

#### This element has no child elements.

#### Example

```xml
<advance width="400" />
```

{: #unicode }
### unicode: Unicode code point.

#### Attributes

| attribute name | data type | description                                                                                                                   |
|----------------|-----------|-------------------------------------------------------------------------------------------------------------------------------|
| hex            | string    | A unicode code point as a hexadecimal number. The string is case-insensitive and must contain the hex value without a prefix. |

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

| attribute name | data type        | description                                                                                                                    | default value |
|----------------|------------------|--------------------------------------------------------------------------------------------------------------------------------|---------------|
| fileName       | string           | The image file name, including any file extension, not an absolute or relative path in the file system.                        | None          |
| xScale         | integer or float | See below.                                                                                                                     | 1             |
| xyScale        | integer or float | See below.                                                                                                                     | 0             |
| yxScale        | integer or float | See below.                                                                                                                     | 0             |
| yScale         | integer or float | See below.                                                                                                                     | 1             |
| xOffset        | integer or float | See below.                                                                                                                     | 0             |
| yOffset        | integer or float | See below.                                                                                                                     | 0             |
| color          | string           | The color that should be applied to the image. The format follows the [color definition] standard. This attribute is optional. | no color      |

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

| attribute name | data type        | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | default value |
|----------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| x              | integer or float | The 'x' coordinate. Optional if `y` is provided and `angle` is not provided. See below for details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | None          |
| y              | integer or float | The 'y' coordinate. Optional if `x` is provided and `angle` is not provided. See below for details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | None          |
| angle          | integer or float | The angle of the guideline. This must be an angle between 0 and 360 degrees in a clockwise direction from the horizontal. If `x` or `y` are not specified, `angle` must not be specified. See below for details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | None          |
| name           | string           | An arbitrary name for the guideline. This attribute is optional.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | no name       |
| color          | string           | The color that should be applied to the guideline. The format follows the [color definition] standard. This attribute is optional.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | no color      |
| identifier     | string           | Unique identifier for the guideline. This attribute is not required and should only be added to guidelines as needed. However, once an identifier has been assigned to a guideline it must not be unnecessarily removed or changed. Identifiers may be changed in incoming guidelines during editing operations such as "paste," but they should be maintained unless a duplicate identifier will be created. The identifier value must be unique within all identifiers (including identifiers for elements other than guidelines) in the glyph that the guideline belongs to but it is not required to be unique among the identifiers assigned in other glyphs or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

The guideline extends along `angle` to infinity in both directions out of the point defined by `x` and `y`. If `y` and `angle` are omitted, the element represents a vertical guideline. If `x` and `angle` are omitted, the element represents a horizontal guideline.

#### This element has no child elements.

{: #anchor }
### anchor: A reference position.

This element may occur any number of times.

#### Attributes

| attribute name | data type        | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | default value |
|----------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| x              | integer or float | The 'x' coordinate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | None          |
| y              | integer or float | The 'y' coordinate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | None          |
| name           | string           | An arbitrary name for the anchor. This attribute is optional.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | no name       |
| color          | string           | The color that should be applied to the anchor. The format follows the [color definition] standard. This attribute is optional.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | no color      |
| identifier     | string           | Unique identifier for the anchor. This attribute is not required and should only be added to anchors as needed. However, once an identifier has been assigned to an anchor it must not be unnecessarily removed or changed. Identifiers may be changed in incoming anchors during editing operations such as "paste," but they should be maintained unless a duplicate identifier will be created. The identifier value must be unique within all identifiers (including identifiers for elements other than anchors) in the glyph that the anchor belongs to but it is not required to be unique among the identifiers assigned in other glyphs or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

#### This element has no child elements.

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

| element name | description                    |
|--------------|--------------------------------|
| [component]  | May occur any number of times. |
| [contour]    | May occur any number of times. |

{: #component }
### component: Insert another glyph as part of the outline.

#### Attributes

| attribute name | data type        | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | default value |
|----------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| base           | string           | Name of the base glyph                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | None          |
| xScale         | integer or float | See below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1             |
| xyScale        | integer or float | See below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0             |
| yxScale        | integer or float | See below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0             |
| yScale         | integer or float | See below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1             |
| xOffset        | integer or float | See below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0             |
| yOffset        | integer or float | See below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0             |
| identifier     | string           | Unique identifier for the component. This attribute is not required and should only be added to components as needed. However, once an identifier has been assigned to a component it must not be unnecessarily removed or changed. Identifiers may be changed in incoming components during editing operations such as "paste," but they should be maintained unless a duplicate identifier will be created. The identifier value must be unique within all identifiers (including identifiers for elements other than components) in the glyph that the component belongs to but it is not required to be unique among the identifiers assigned in other glyphs, in any layerinfo.plist or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

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

| attribute name | data type | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | default value |
|----------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| identifier     | string    | Unique identifier for the component. This attribute is not required and should only be added to contours as needed. However, once an identifier has been assigned to a contour it must not be unnecessarily removed or changed. Identifiers may be changed in incoming contours during editing operations such as "paste" and component decomposition, but they should be maintained unless a duplicate identifier will be created. Identifiers should also be retained when possible during outline manipulation operations such as path direction changes and remove overlap. The identifier value must be unique within all identifiers (including identifiers for elements other than contours) in the glyph that the contour belongs to but it is not required to be unique among the identifiers assigned in other glyphs, in any layerinfo.plist or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

#### Child Elements

| element name | description                    |
|--------------|--------------------------------|
| [point]      | May occur any number of times. |

There is no requirement that a contour contain an on-curve point. If a contour contains only off-curve points the contour must be treated as a quadratic curve.

{: #point }
### point: An attributed coordinate pair.

#### Attributes

| attribute name | data type        | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | default value |
|----------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| x              | integer or float | The 'x' coordinate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | None          |
| y              | integer or float | The 'y' coordinate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | None          |
| type           | string           | The point and/or segment type. The options are detailed below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | offcurve      |
| smooth         | string           | This attribute must only be given when `type` indicates the point is on-curve. When set to `yes`, it signifies that a smooth curvature should be maintained at this point, either as a `curve point` or a `tangent point` in Fontographer terms. This attribute may be set for all point types except `offcurve`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | no            |
| name           | string           | Arbitrary name or label for this point. The name does not have to be unique within a contour, nor within an outline.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | no name       |
| identifier     | string           | Unique identifier for the point. This attribute is not required and should only be added to points as needed. However, once an identifier has been assigned to a point it must not be unnecessarily removed or changed. Identifiers may be changed in incoming points during editing operations such as "paste" and component decomposition, but they should be maintained unless a duplicate identifier will be created. Identifiers should also be retained when possible during outline manipulation operations such as path direction changes and remove overlap. The identifier value must be unique within all identifiers (including identifiers for elements other than poinys) in the glyph that the point belongs to but it is not required to be unique among the identifiers assigned in other glyphs, in any layerinfo.plist or in fontinfo.plist. The identifier specification is detailed in the [conventions]. | no identifier |

##### Point Types

|          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| move     | A point of this type must be the first in a `contour`. The reverse is not true: a `contour` does not necessarily start with a `move` point. When a `contour` **does** start with a `move` point, it signifies the beginning of an **open** contour. A **closed** contour does **not** start with a `move` and is defined as a cyclic list of points, with no predominant start point. There is always a *next point* and a *previous point*. For this purpose the list of points can be seen as endless in both directions. The actual list of points can be rotated arbitrarily (by removing the first N points and appending them at the end) while still describing the same outline. |
| line     | Draw a straight line from the previous point to this point. The previous point must be a `move`, a `line`, a `curve` or a `qcurve`. It must not be an `offcurve`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| offcurve | This point is part of a curve segment that goes up to the next point that is either a `curve` or a `qcurve`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| curve    | Draw a cubic bezier curve from the last non-*offcurve* point to this point. The number of *offcurve* points can be zero, one or two. If the number of `offcurve` points is zero, a straight line is drawn. If it is one, a quadratic curve is drawn. If it is two, a regular cubic bezier is drawn.                                                                                                                                                                                                                                                                                                                                                                                      |
| qcurve   | Similar to curve, but uses quadratic curves, using the TrueType "implied on-curve points" principle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

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

This element is a place to store authoring tool specific, user specific or otherwise arbitrary data for the glyph. lib mus have one child element that is structure as a dictionary formatted as an [XML Property List]. This element may occur at most once. In order to prevent conflicts in the lib, keys in the top level should follow a [reverse domain naming scheme]. The pattern "public.\*", where \* represents an arbitrary string of one or more characters, is reserved for use in standardized lib keys. It is recommended that the data stored as a value be as shallow as possible.

Data that is too complex or too large for lib can be stored in the [data directory].

#### Common Key Registry

The following is a registry of public lib keys that map to functionality that is often seen in font editing applications but is not suitable for storage elsewhere in this particular version of the UFO.

##### public.markColor

This key is used for representing the "mark" color seen in various font editors. The value for the key must be a string following the [color definition] standard. This data is optional.

##### public.postscriptName

This key is used for representing the indended "production" name for the glyph, which in OpenType fonts would be typically stored in the `CFF ` or `post` table. The value for the key must be a string. It is recommended that the value conforms to the [Adobe Glyph List Specification](https://github.com/adobe-type-tools/agl-specification). Authoring tools may prefer this value over the `glyph` element's `name` attribute when converting the UFO into an OpenType font, but it is solely up to the authoring tool whether it would expect the data in [features.fea](../features.fea) to correspond to the the `glyph` element's `name` attribute or the `public.postscriptName` value. This data is optional. 

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<glyph name="blackcircle" format="2">
  <advance width="268"/>
  <unicode hex="25CF"/>
  <image fileName="blackcircle sketch.png" xScale="0.5" yScale="0.5"/>
  <guideline y="-12" name="overshoot"/>
  <anchor x="74" y="197" name="top"/>
  <outline>
    <contour>
      <point x="237" y="152"/>
      <point x="193" y="187"/>
      <point x="134" y="187" type="curve" smooth="yes"/>
      <point x="74" y="187"/>
      <point x="30" y="150"/>
      <point x="30" y="88" type="curve" smooth="yes"/>
      <point x="30" y="23"/>
      <point x="74" y="-10"/>
      <point x="134" y="-10" type="curve" smooth="yes"/>
      <point x="193" y="-10"/>
      <point x="237" y="25"/>
      <point x="237" y="88" type="curve" smooth="yes"/>
    </contour>
  </outline>
  <lib>
    <dict>
      <key>com.letterror.somestuff</key>
      <string>arbitrary custom data!</string>
      <key>public.markColor</key>
      <string>1,0,0,0.5</string>
      <key>public.postscriptName</key>
      <string>uni25CF</string>
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
  [color definition]: conventions.html#colors
  [layerinfo.plist]: glyphs.html#layerinfo
  [conventions]: conventions.html#identifiers
  [component]: #component
  [contour]: #contour
  [point]: #point
  [XML Property List]: conventions.html#propertylist
  [reverse domain naming scheme]: conventions.html#reversedomain
  [data directory]: data.html
