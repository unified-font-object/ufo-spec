---
layout: default
navigation: true
order: 3
title: Contributing
---

The UFO specification is a community project and problem reports and enhancement proposals are welcome. If you would like to propose a change or addition to the specification, please follow the process below.

## Problem Identification

The process begins when a problem is identified. A problem may be a mistake in the current specification, a missing bit of data, a new idea that needs storage or something else. When defining the problem it is important to consider the following questions:

- Is the problem caused by a mistake in the specification?
- Is the problem caused by something missing in the specification?
- Has the problem been identified and discussed before?
- How long has this been a problem?
- How urgent is the problem?

It's also important to determine the scope of the problem:

- Does the problem affect only a single user?
- Does the problem affect only a single workflow?
- Does the problem affect only a single tool?
- Does the problem affect only a single font binary format?
- Does the problem potentially affect all users?

If the problem is only affecting a single user, workflow or tool, it is often best to address the problem through an [extension] rather than a specification change. Extensions can be deployed faster and are more flexible than specification changes. If the problem does seem to need a specification change please [open an issue]. If you are unsure if you should open an issue, feel free to discuss the problem on the [UFO Specification Google Group]. Once the issue has been opened, a discussion will begin. (Please be patient as this project is managed by volunteers.) If the problem warrants a specification change, a solution development process will begin.

## Solution Development

Solutions are developed collaboratively in the issue defining the problem. Ideally, the person who identifies the problem will lead, or at least participate in, the development of a solution to the problem. The development process is deliberately slow in order to keep the specification as clear of cruft as possible. Many ideas seem great at first, but over time better solutions evolve through collaboration or the ideas fall by the wayside altogether. Simple ideas with obvious solutions can move quickly, but more complex ideas need time to mature. There is no one development path for all solutions, but there are some general steps in the process.

### Work out a solution in abstract.

It's easy to get lost in the details of storage structures, but those are much easier to figure out once the problem at hand has been solved abstractly. It is usually best to first work out how to explain the solution to the problem rather than getting into the minute details. The following questions are the kinds of things to think about at this stage:

- What data is needed to solve the problem?
- How should this data be interpreted?
- What should happen when this data is not defined?
- What objects in the UFO does this data relate to?
- Do existing tools or specifications support this or similar data?
- What edge cases can occur when interpreting the data?

### Determine how and where the data will be stored.

Once the general idea for a solution is worked out, the storage location and format need to be determined. The following guidelines apply to formats used within the UFO specification:

- Storage formats **must** be open and not proprietary.
- The storage formats must be human readable and human editable.   In practice this means that files should be plain text. The specification makes use of XML, but CSV, YAML and so on are all potentially acceptable. "Human readable and editable" does not necessarily mean "easy to manually edit." Rather, it means "if absolutely necessary, a user must be able to open the file and work on it without any tool beyond a plain text editor." The only exceptions to this are things that can't be represented with plain text, such as images.
- Programmatic reading/writing of the storage format should be easy to implement, preferably with widely accessible, open libraries in multiple programming languages.

If a storage format for the data that fits these requirements already exists, the existing format should be considered instead of inventing a new format. Likewise, if there is data with a similar structure already in the UFO specification, the previously defined structure should serve as a model format.

Additions to the the specification can be stored in several places:

- An existing file.
- A new file.
- A new GLIF attribute in an existing GLIF element.
- A new GLIF element.
- A public lib key/value pair.
- A public public data key/value.

The location of the data must be coordinated with the format of the data. If the data will be added to an existing file, the format must adhere to the conventions of the existing file.

### Determine the UFO versions that the solution applies to.

Once the storage location and format are determined, it's possible to determine which versions of the specification will take the new change. These are the guidelines used to make this determination:

#### Changes that require a major format version increase.

A change that matches any of the following must wait for a full format version increase:

- Any major addition of new data outside of the libs or data directory.
- Any data that will be difficult for developers to implement.
- Anything that fundamentally changes the interpretation of any part of the specification.

The only exceptions to this would be an extreme problem that requires an immediate change.

#### Changes that require a minor format version increase.

A change that matches any of the following must wait for a minor format version increase:

- Any data that could be lost in tools that support the current format major version and minor version.
- Any data added to an official file outside of libs or data directory.

#### Changes that are backwards compatible.

Additions to, removal from and changes to the lib and data directory are backwards compatible, so they may be added at any point.

### Document the change.

Once the format, location and specification versions are approved, the change should be documented in a [fork of the specification]. The documentation must be in the applicable places and follow the established formatting and language. A [pull request] may then be requested.


## Evaluation Criteria

As a problem is discussed, the specification managers will advise the discussion as needed and evaluate the proposed solutions based on criteria such as:

- Is the specification the right place for this solution?
- Does the solution follow the [UFO Design Philosophy]?
- Does the solution come from someone with expertise in the subject? If not, is there an expert who can offer feedback?
- Is the solution as simple and minimal as possible?
- Does the solution completely solve the problem?
- Does the solution change the meaning of data in existing UFOs?
- Is the storage location appropriate for the problem?
- How difficult will it be for developers to implement the solution?
- Is the documentation unambiguous?
- Is it likely that the solution will stand the test of time?
- Changes to the specification are permanent. *Are we absolutely sure about this?*

  [extension]: extending
  [open an issue]: https://github.com/unified-font-object/ufo-spec/issues
  [UFO Specification Google Group]: https://groups.google.com/g/ufo-spec
  [UFO Design Philosophy]: /index#the-ufo-design-philosophy
  [fork of the specification]: https://github.com/unified-font-object/ufo-spec
  [pull request]: https://github.com/unified-font-object/ufo-spec/pulls
  
### Meetings
Historically there are informal meetings about the specification around the [Robothon](http://typemedia.org/robothon/) conference (held roughly every three years). On July 31, 2020, we had the first open virtual meeting, the [notes of which are online](https://docs.google.com/document/d/1REf695Yxnu3aj_UqcVfF0WTyV8PUaPo-r6duEHxtj48/edit).
