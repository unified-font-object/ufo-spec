---
layout: default
navigation: true
order: 5
title: Extensions
---

Very often, a user or developer needs to store some data in a UFO that is not part of the official specification. Inserting this data into an arbitrary location in the UFO will likely result in data loss and unexpected behavior in UFO readers. So, the specification has designated areas where such data can safely be stored and retrieved without any unexpected problems. An overview of these locations and strategies are explained below. *The implementation details of these locations and techniques are officially defined in the UFO specification versions.*

## Storage Locations

If data needs the be stored, there are two designation types: libs and the data directory. The data that needs to be stored will determine which location to use.

### Lib

Data that can be serialized may be stored in the object libs. The font and glyph level files contain lib locations in UFO 1 and later. The layer level files contain lib locations in UFO 3 and later. Lower-level objects have a pseudo lib in UFO 3 and will have official locations in UFO 4.

Libs are useful for storing data about the objects that they relate to. For example, a foundry may have a tool that is used for production of their fonts:

{: .algorithmdiagram}
- Some Foundry Production Tool
	- decompose components: no
	- remove overlap: yes
	- round to integers: no
	- autohint: yes

This data could be stored in `fontinfo.plist` with this serialization structure:

```xml
<key>com.somefoundry.productionTool</key>
<dict>
	<key>autohint</key>
	<true/>
	<key>decomposeComponents</key>
	<false/>
	<key>removeOverlap</key>
	<true/>
	<key>roundToIntegers</key>
	<false/>
</dict>
```

### Data Directory

The data directory was added to the specification in UFO 3. This directory allows for storing data that is not suited to an object lib or that cannot be stored in a property list. For example, if a tool composes a single glyph out of multiple images, the data could be stored in this file structure:

{: .filediagram}
- {: .filediagramDirectory}com.sometool.glyphImages
	- {: .filediagramDirectory}A
		- image1.psd
		- image2.psd
		- image3.psd
	- {: .filediagramDirectory}B
		- image1.psd
		- image2.psd

### Storage Keys

Data collisions are prevented by using a reverse domain name storage key system. The developer of the data structure stores the data under their domain name appended with a relevant name. The documentation for a storage key's data may be published so that other tools can use it or it may remain strictly for private use.

## Object Identifiers

In some cases, a tool may need to refer to specific objects. UFO 3 introduced object identifiers that are designed for such purposes. For example, if a tool shows font guidelines only when certain conditions are met:

{: .algorithmdiagram}
- Smart Guide
	- guide identifier: 7pdbofkUhz
		- unicode category: Lu
- Smart Guide
	- guide identifier: z1bkCMlhNb
	- glyph name pattern: *.sc*
	- contour count: > 0

This data could be stored in `fontinfo.plist` with this serialization structure:

```xml
<key>com.sometool.smartGuides</key>
<dict>
	<key>7pdbofkUhz</key>
	<dict>
		<key>unicodeCategory</key>
		<string>Lu</string>
	</dict>
	<key>z1bkCMlhNb</key>
	<dict>
		<key>contourCount</key>
		<array>
			<string>&gt;</string>
			<integer>0</integer>
		</array>
		<key>glyphNamePattern</key>
		<string>*.sc*</string>
	</dict>
</dict>
```