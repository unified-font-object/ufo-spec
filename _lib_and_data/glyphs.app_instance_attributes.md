---
layout: default
title: Glyphs.app Instance Attributes
summary: |
    Glyphs.app allows to configure more information about each instance
    than what fits in the Designspace format. Some of that information is
    useful for other tools than Glyphs.app.

lib_and_data_keys:
  - name: com.schriftgestaltung.export
    location: Designspace instance lib
    type: boolean
    example_md: |
        ```xml
        <instance name="Only visible in Glyphs.app">
            <lib>
                <dict>
                    <key>com.schriftgestaltung.export</key>
                    <false/>
                </dict>
            </lib>
        </instance>
        ```
    description_md: |
        Mark this instance as only visible in the Glyphs.app UI, but not
        to be generated when building fonts. Designers often use this to
        proof intermediate weights.

        `fontmake` will skip such instances when generating fonts from
        the Designspace file.

  - name: com.schriftgestaltung.weight
    location: Designspace instance lib
    type: string
    example_md: |
        ```xml
        <instance name="Make my OS/2 usWeightClass 200">
            <lib>
                <dict>
                    <key>com.schriftgestaltung.weight</key>
                    <string>ExtraLight</string>
                </dict>
            </lib>
        </instance>
        ```
    description_md: |
        Glyphs.app allows generated instances to have a custom OS/2
        [usWeightClass](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#usweightclass),
        potentially disconnected from their location along the font's weight
        axis.

        This key stores the name what the user has selected in Glyphs.app's
        Weight dropdown for instances ([see their
        tutorial](https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances)).

        The mapping from the strings used in Glyphs.app's UI and the OS/2
        values can be found in [`glyphsLib`'s source
        code](https://github.com/googlefonts/glyphsLib/blob/3e0c6de4aa657156428ccc63dd4576f6cc706563/Lib/glyphsLib/classes.py#L210-L226):
        ```python
        WEIGHT_CODES = {
            "Thin": 100,
            "ExtraLight": 200,
            "UltraLight": 200,
            "Light": 300,
            None: 400,  # default value normally omitted in source
            "Normal": 400,
            "Regular": 400,
            "Medium": 500,
            "DemiBold": 600,
            "SemiBold": 600,
            "Bold": 700,
            "UltraBold": 800,
            "ExtraBold": 800,
            "Black": 900,
            "Heavy": 900,
        }
        ```


  - name: com.schriftgestaltung.width
    location: Designspace instance lib
    type: string
    example_md: |
        ```xml
        <instance name="Make my OS/2 usWidthClass 5">
            <lib>
                <dict>
                    <key>com.schriftgestaltung.width</key>
                    <string>Medium (normal)</string>
                </dict>
            </lib>
        </instance>
        ```
    description_md: |
        Glyphs.app allows generated instances to have a custom OS/2
        [usWidthClass](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#uswidthclass),
        potentially disconnected from their location along the font's width
        axis.

        This key stores the name what the user has selected in Glyphs.app's
        Width dropdown for instances ([see their
        tutorial](https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances)).

        The mapping from the strings used in Glyphs.app's UI and the OS/2
        values can be found in [`glyphsLib`'s source
        code](https://github.com/googlefonts/glyphsLib/blob/3e0c6de4aa657156428ccc63dd4576f6cc706563/Lib/glyphsLib/classes.py#L228-L239):
        ```python
        WIDTH_CODES = {
            "Ultra Condensed": 1,
            "Extra Condensed": 2,
            "Condensed": 3,
            "SemiCondensed": 4,
            None: 5,  # default value normally omitted in source
            "Medium (normal)": 5,
            "Semi Expanded": 6,
            "Expanded": 7,
            "Extra Expanded": 8,
            "Ultra Expanded": 9,
        }
        ```
---

[Glyphs.app](https://glyphsapp.com/) allows to configure more information
about each instance than what fits in the Designspace format, so everything
extra is stored in the Designspace instance's lib when converting the
`.glyphs` file with [`glyphsLib`](https://github.com/googlefonts/glyphsLib).

Some of that extra instance information will be interpreted by
[`fontmake`](https://github.com/googlefonts/fontmake) and
[`ufo2ft`](https://github.com/googlefonts/ufo2ft) to build instances in a
similar way as Glyphs.app does.

{% include lib_and_data_reference.html %}
