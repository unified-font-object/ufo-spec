---
layout: default
title: Designspace 5.0
summary_md: |
    This proposes to extend the Designspace format to make it possible to:

    * have a single designspace file for a whole font project,
    * that covers both interpolatable sources and non-interpolatable ones (e.g. uprights vs italics),
    * that includes STAT information, and
    * that lists all the "products" that can be built from the source files, i.e. several variable fonts and several static instances.
---

This is a proposed update to the
[Designspace](https://github.com/fonttools/fonttools/tree/master/Doc/source/designspaceLib)
file format that standardises the following Dalton Maag practices:

* Allow to mix interpolatable sources and some that are not, as long as they're
part of the same "design space". Introduce discrete axes to organize these
sources. Example: uprights and italics. The goal is to have 1 designspace file
for any cohesive font project, with everything listed in one place. This goes
hand-in-hand with the next points.

* Provide STAT table information from the start, and include it in the
Designspace file format. Also allow to provide STAT information for linked
families that are not interpolatable (e.g. Source Sans Roman and Source Sans
Italic) in one single Designspace file. This feature would supersede the
external Stylespace files that Nikolaus developed (see
[statmake](https://github.com/daltonmaag/statmake))
  * Only one copy of the STAT information is maintained, and it is attached to
    the data that it describes (i.e. the usual contents of desispace files).

    Alternative options at the moment don't achieve this:
      * `statmake`'s file is next to the designspace, and needs to be kept
        up-to-date separately
      * Writing STAT information in a feature file is also separate from the
        designspace and needs to be updated separately.
  * We can use the STAT information to provide default lists of named instances
    to be included in the defined variable fonts.

* Define more clearly what can be "produced" from a Designspace by running it
  through a compiler such as `fontmake`, i.e. list explicitly the outputs of
  the build process in the designspace. This achieves two things:
  * We can just feed the designspace to a compiler and get everything we
    expect from it without fiddling with compiler options
  * Because possible outputs are defined explicitly, we can refer to them and
    associate data to them. For example: if the designspace defines two
    variable fonts, and we have two special font tables dumped in TTX format
    to mix into these two fonts, we can express the link between each font
    and each TTX dump.

* Continous and discrete axes will define groups of sources that are
interpolatable. (or maybe we need to explicitly define these groups? To be
discussed). From there:
  * Define several variable fonts from the same set of interpolatable sources.
    This would allow VF projects with several axes such as Aktiv Grotesk to
    have only 1 Designspace file that describes all 5 variable fonts that we
    ship (instead of the current situation where we write 5 Designspace files
    with repeated information).
  * Define several static instances from each group of interpolatable sources.

## Related discussions

* UFS: https://github.com/unified-font-object/ufo-spec/issues/86
* Original STAT-in-Designspace (before `statmake`):
https://github.com/fonttools/fonttools/issues/1507


## Sample files

### `SourceSans.designspace`

This example file demonstrates how to:
* include STAT table information
* rely on it to get correctly named instances
* mix interpolatable and discrete axes
* define several variable fonts from the "design space"

```xml
<?xml version="1.0" encoding="utf-8"?>
<designspace format="5.0">
  <axes>
    <axis default="200" maximum="900" minimum="200" name="Weight" tag="wght">
      <map input="200" output="0" />
      <map input="300" output="100" />
      <map input="400" output="368" />
      <map input="600" output="600" />
      <map input="700" output="824" />
      <map input="900" output="1000" />
      <!-- All axes provide STAT information with the "labels" element. -->
      <labels>
        <label minimum="0" value="0" maximum="50" name="Extra Light" />
        <label minimum="50" value="100" maximum="234" name="Light" />
        <label minimum="234" value="368" maximum="484" name="Regular" elidable="true" />
        <label minimum="484" value="600" maximum="712" name="Semi Bold" />
        <label minimum="712" value="824" maximum="912" name="Bold" />
        <label minimum="912" value="1000" maximum="1000" name="Black" />
        <label value="368" name="Regular" elidable="true" linkedvalue="824" />
      </labels>
    </axis>
    <!--
      Discrete axes provide a list of discrete `values` instead of the usual
      `minimum` and `maximum`. The `values` are space-separated numbers. There
      can be more than 2. No interpolation is allowed between these.
    -->
    <axis default="0" values="0 1" name="Italic" tag="ital">
      <labels>
        <!-- Discrete axes also provide STAT information. -->
        <label value="0" name="Roman" elidable="true" linkedvalue="1" />
        <label value="1" name="Italic" />
      </labels>
    </axis>
  </axes>

  <sources>
    <source filename="Roman/Masters/master_0/SourceSans_ExtraLight.ufo">
      <info copy="1" />
      <location>
        <dimension name="Weight" xvalue="0" />
        <dimension name="Italic" xvalue="0" />
      </location>
    </source>
    <source filename="Roman/Masters/master_1/SourceSans_Black.ufo">
      <location>
        <dimension name="Weight" xvalue="1000" />
        <dimension name="Italic" xvalue="0" />
      </location>
    </source>
    <source filename="Italic/Masters/master_0/SourceSans_ExtraLight.ufo">
      <info copy="1" />
      <location>
        <dimension name="Weight" xvalue="0" />
        <dimension name="Italic" xvalue="1" />
      </location>
    </source>
    <source filename="Italic/Masters/master_1/SourceSans_Black.ufo">
      <location>
        <dimension name="Weight" xvalue="1000" />
        <dimension name="Italic" xvalue="1" />
      </location>
    </source>
  </sources>

  <variable-fonts>
    <!--
      Each variable font is a subset of the axes provided at the top.
      Continuous axes can be included either:
        * in full,
        * or only on a reduced interval (different minimum-maximum),
        * or only at 1 discrete location
      Dicrete axes cannot be included in full, and we must specify a value
      (or the compiler should assume the default value).
    -->
    <variable-font>
      <!-- This one is the Roman (default location along ital),
           with full range for the Weight axis. -->
      <axes>
        <axis name="Weight"/>
      </axes>
    </variable-font>
    <variable-font>
      <!-- This one is the Italic, with full range for the Weight axis. -->
      <axes>
        <axis name="Weight"/>
        <axis name="Italic" value="1"/>
      </axes>
    </variable-font>
    <variable-font>
      <!-- As an example, this would be the Roman with a reduced range. -->
      <axes>
        <axis name="Weight" minimum="400" maximum="700" default="400"/>
        <axis name="Italic" value="0"/>
      </axes>
    </variable-font>
  </variable-fonts>

  <instances>
    <instance>
      <!--
        Using the STAT information provided above, the names of the instances
        can be generated, and don't need to be specified, except to override
        the generated names (but then you might as well fix your STAT data).
        Example:
        Source Sans Extra Light
        familyName: "Source Sans"
        styleName: "Extra Light"
        postScriptFontName: "SourceSans-ExtraLight"
      -->
      <location>
        <dimension name="Weight" xvalue="0" />
        <dimension name="Italic" xvalue="0" />
      </location>
    </instance>
    <instance>
      <!-- Source Sans Light -->
      <location>
        <dimension name="Weight" xvalue="100" />
        <dimension name="Italic" xvalue="0" />
      </location>
    </instance>
    <instance>
      <!--
        Source Sans Regular
        (because elidable fallback name ID defaults to 2.
      -->
      <location>
        <dimension name="Weight" xvalue="368" />
        <dimension name="Italic" xvalue="0" />
      </location>
    </instance>
    <instance>
      <!-- Source Sans Semi Bold -->
      <location>
        <dimension name="Weight" xvalue="600" />
        <dimension name="Italic" xvalue="0" />
      </location>
    </instance>
    <instance>
      <!--
        Source Sans Bold
        [...]
        styleMapStyleName: "bold"
      -->
      <location>
        <dimension name="Weight" xvalue="824" />
        <dimension name="Italic" xvalue="0" />
      </location>
    </instance>
    <instance>
      <!-- Source Sans Black -->
      <location>
        <dimension name="Weight" xvalue="1000" />
        <dimension name="Italic" xvalue="0" />
      </location>
    </instance>
  </instances>
</designspace>
```


## Details of proposed changes to the specification

Ideally should be a merge request in fontTools/designspaceLib (once the
modifications described are deemed generally good ideas).

