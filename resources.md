---
layout: default
navigation: true
order: 3
title: Resources
---

The UFO team strives to make it as easy as possible to add UFO support to applications and toolkits. To that effect, we present a small collection of resources.

<hr class="subsection">

## Macintosh Applications

These resources are useful for developing Macintosh OS X applications that support the UFO format.

### UFO Document Icon

A standard UFO document icon. The file is provided in [Apple Icon Image format](http://en.wikipedia.org/wiki/Apple_Icon_Image){:target="_blank"}.

[![UFO Icon]({{ site.baseurl }}/media/resources-macicon.png)]({{ site.baseurl }}/downloads/UFODocumentIcon.zip)

[Click to download]({{ site.baseurl }}/downloads/UFODocumentIcon.zip)

### UTI Declarations

A set of standard "Uniform Type Identifier":http://developer.apple.com/macosx/uniformtypeidentifiers.html declarations.

#### UTExportedTypeDeclarations

```xml
<array>
  <dict>
    <key>UTTypeConformsTo</key>
    <array>
      <string>com.apple.package</string>
    </array>
    <key>UTTypeDescription</key>
    <string>Unified Font Object</string>
    <key>UTTypeIconFile</key>
    <string>UFODocumentIcon.icns</string>
    <key>UTTypeIdentifier</key>
    <string>org.unifiedfontobject.ufo</string>
    <key>UTTypeReferenceURL</key>
    <string>http://unifiedfontobject.org</string>
    <key>UTTypeTagSpecification</key>
    <dict>
      <key>public.filename-extension</key>
      <array>
        <string>ufo</string>
      </array>
    </dict>
  </dict>
</array>
```


#### UTImportedTypeDeclarations

```xml
<array>
  <dict>
    <key>UTTypeConformsTo</key>
    <array>
      <string>com.apple.package</string>
    </array>
    <key>UTTypeDescription</key>
    <string>Unified Font Object</string>
    <key>UTTypeIconFile</key>
    <string>UFODocumentIcon.icns</string>
    <key>UTTypeIdentifier</key>
    <string>org.unifiedfontobject.ufo</string>
    <key>UTTypeReferenceURL</key>
    <string>http://unifiedfontobject.org</string>
    <key>UTTypeTagSpecification</key>
    <dict>
      <key>public.filename-extension</key>
      <array>
        <string>ufo</string>
      </array>
    </dict>
  </dict>
</array>
```
