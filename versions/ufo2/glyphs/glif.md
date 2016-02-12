---
layout: default
title: Glyph Interchange Format
---

| **File Format** | XML |

The Glyph Interchange Format (GLIF) is a simple and clear XML representation of a single glyph. GLIF files typically have a *.glif* extension.

## Specification

### \<glyph> The top level element.

#### Attributes

| attribute name | description                             |
|----------------|-----------------------------------------|
| name           | The name of the glyph                   |
| format         | The format version. 1 for this version. |

The *name* attribute has limited uses in this version. The *contents.plist* file maps glyph names to file names, and one of the reasons to do this is to avoid having to parse all files just to get at a list of available glyph names. When reading GLIF files, the *name* attribute is probably best ignored, since manual editing may have caused a mismatch with the glyph name as stored in *contents.plist*, as well as with the file name, which is an algorithmic transformation of the glyph name. This attribute may become more useful in future versions of GLIF.

#### Child Elements

| element name | description                    |
|--------------|--------------------------------|
| advance      | May occur at most once.        |
| unicode      | May occur any number of times. |
| outline      | May occur at most once.        |
| lib          | May occur at most once.        |

### \<advance> Horizontal and vertical metrics.

#### Attributes

| attribute name | data type        | description           |
|----------------|------------------|-----------------------|
| width          | integer or float | The advance width.    |
| height         | integer or float | The vertical advance. |

This element has no child elements.

### \<unicode> Unicode code point.

#### Attributes

| attribute name | description                                   |
|----------------|-----------------------------------------------|
| hex            | A unicode code point as a hexadecimal number. |

This element has no child elements. The first occurrence of this element defines the primary unicode value for this glyph.

### \<outline> Outline description.

#### Child Elements

| element name | description                    |
|--------------|--------------------------------|
| component    | May occur any number of times. |
| contour      | May occur any number of times. |

This element has no attributes.

### \<component> Insert another glyph as part of the outline.

#### Attributes

| attribute name | data type        | description            | default value |
|----------------|------------------|------------------------|---------------|
| base           | string           | Name of the base glyph | None          |
| xScale         | integer or float | See below.             | 1             |
| xyScale        | integer or float | See below.             | 0             |
| yxScale        | integer or float | See below.             | 0             |
| yScale         | integer or float | See below.             | 1             |
| xOffset        | integer or float | See below.             | 0             |
| yOffset        | integer or float | See below.             | 0             |

xScale, xyScale, yxScale, yScale, xOffset, yOffset taken together in that order form an Affine transformation matrix, to be used to transform the base glyph. The default matrix is \[1 0 0 1 0 0\], the identity transformation.

This element has no child elements.

### \<contour> Contour description.

#### Child Elements

| element name | description                    |
|--------------|--------------------------------|
| point        | May occur any number of times. |

This element has no attributes.

### \<point> An attributed coordinate pair.

#### Attributes

| attribute name | data type        | description                                                                                                                                                                                                                                     | default value |
|----------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| x              | integer or float | The 'x' coordinate.                                                                                                                                                                                                                             | None          |
| y              | integer or float | The 'y' coordinate.                                                                                                                                                                                                                             | None          |
| type           | string           | The point and/or segment type. The options are detailed below.                                                                                                                                                                                  | offcurve      |
| smooth         | string           | This attribute can only be given when *type* indicates the point is on-curve. When set to *yes*, it signifies that a smooth curvature should be maintained at this point, either as a *curve point* or a *tangent point* in Fontographer terms. | no            |
| name           | string           | Arbitrary name or label for this point. The name does not have to be unique within a contour, nor within an outline.                                                                                                                            | None          |

This element has no child elements.

##### Point Types

| move     | A point of this type MUST be the first in a *contour*. The reverse is not true: a *contour* does not necessarily start with a *move* point. When a *contour* **does** start with a *move* point, it signifies the beginning of an **open** contour. A **closed** contour does **not** start with a *move* and is defined as a cyclic list of points, with no predominant start point. There is always a *next point* and a *previous point*. For this purpose the list of points can be seen as endless in both directions. The actual list of points can be rotated arbitrarily (by removing the first N points and appending them at the end) while still describing the same outline. |
| line     | Draw a straight line from the previous point to this point. The previous point may be a *move*, a *line*, a *curve* or a *qcurve*, but not an *offcurve*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| offcurve | This point is part of a curve segment, that goes up to the next point that is either a *curve* or a *qcurve*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| curve    | Draw a cubic bezier curve from the last non-*offcurve* point to this point. If the number of *offcurve* points is zero, a straight line is drawn. If it is one, a quadratic curve is drawn. If it is two, a regular cubic bezier is drawn. If it is larger than 2, a series of cubic bezier segments are drawn, as defined by the *Super Bezier* algorithm.                                                                                                                                                                                                                                                                                                                              |
| qcurve   | Similar to curve, but uses quadratic curves, using the TrueType "implied on-curve points" principle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### \<lib> Custom data storage.

This element is structure is defined as a [XML Property List]. This element may occur at most once. lib has exactly one child, which must be *dict*. To avoid naming conflicts, keys should use the Reverse Domain Naming Convention defined for [lib.plist].

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<glyph name="period" format="1">
  <advance width="268"/>
  <unicode hex="002E"/>
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
    </dict>
  </lib>
</glyph>
```

  [XML Property List]: http://www.apple.com/DTDs/PropertyList-1.0.dtd
  [lib.plist]: ../../lib.plist
