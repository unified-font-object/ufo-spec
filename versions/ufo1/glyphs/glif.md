---
layout: default
title: Glyph Interchange Format
---

{: .fileformat}
| **File Format** | XML |

The Glyph Interchange Format (GLIF) is a simple and clear XML representation of a single glyph. GLIF files typically have a *.glif* extension.

## Specification

### \<glyph> The top level element.

#### Attributes

{: .name-description}
| name | description |
|--|--|
| name | The name of the glyph |
| format | The format version. 1 for this version. |

The *name* attribute has limited uses in this version. The *contents.plist* file maps glyph names to file names, and one of the reasons to do this is to avoid having to parse all files just to get at a list of available glyph names. When reading GLIF files, the *name* attribute is probably best ignored, since manual editing may have caused a mismatch with the glyph name as stored in *contents.plist*, as well as with the file name, which is an algorithmic transformation of the glyph name. This attribute may become more useful in future versions of GLIF.

#### Child Elements

{: .name-description}
| name | description |
|--|--|
| advance | May occur at most once. |
| unicode | May occur any number of times. |
| outline | May occur at most once. |
| lib | May occur at most once. |

### \<advance> Horizontal and vertical metrics.

#### Attributes

| name | type | description |
|--|--|--|
| width | integer or float | The advance width. |
| height | integer or float | The vertical advance. |

This element has no child elements.

### \<unicode> Unicode code point.

#### Attributes

{: .name-description}
| name | description |
|--|--|
| hex | A unicode code point as a hexadecimal number. |

This element has no child elements. The first occurrence of this element defines the primary unicode value for this glyph.

### \<outline> Outline description.

#### Child Elements

{: .name-description}
| name | description |
|--|--|
| component | May occur any number of times. |
| contour | May occur any number of times. |

This element has no attributes.

### \<component> Insert another glyph as part of the outline.

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

xScale, xyScale, yxScale, yScale, xOffset, yOffset taken together in that order form an Affine transformation matrix, to be used to transform the base glyph. The default matrix is \[1 0 0 1 0 0\], the identity transformation.

This element has no child elements.

### \<contour> Contour descript