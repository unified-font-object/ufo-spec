The Unified Font Object (UFO) is a cross-platform, cross-application, human readable, future proof format for storing font data.

The specification is found at [unifiedfontobject.org](http://unifiedfontobject.org)

## The UFO Design Philosophy
* The data must be human readable and human editable.
* The data should be application independent.
* Data duplication should be avoided unless absolutely necessary.

## Building documentation locally
1. Install ruby gems and bundler ([how to](https://idratherbewriting.com/jekylldoctheme-separate-outputs/mydoc/mydoc_install_dependencies.html))
2. `bundle install`
3. `bundle exec jekyll serve`
4. Browse to localhost:4000

## UFO Specification Process

1. Recognize the problem.
Open an [issue](https://github.com/unified-font-object/ufo-spec/issues) and discuss:
* Is the spec the right place to address this problem?
* Is this a new idea?
* Is this a fix for a broken thing?
* Is this a missing thing?
* How long has this been a problem?
* How urgent is it?

2. Determine scope.
* Is this limited to a single user?
* A single workflow?
* A single tool?
* A single font binary format?
* Global?

3. Draft a proposal.
* Does the person writing the draft have expertise in the subject? If not, is there an expert who can advise?
* Is there an open spec we can build on?
* Is there something similar we can learn from?

4. Evaluate the proposal.
* Does it solve the problem?
* Is it located at the appropriate scope?
* Does it follow the UFO philosophy?
* Does it change the meaning of data in existing UFOs?
* How hard will it be to implement?
* Is the language unambiguous?
* Will it stand the test of time?

5. Make a decision.
* Does this go into the top of the spec?
* Into a public lib/data key?
* Into a private lib/data key for further research and development?
* Remember, this is permanent, so are we really sure about all of this?

6. Update the spec.
* Language consistency.
* Formatting consistency.
* Submit a [PR](https://github.com/unified-font-object/ufo-spec/pulls).


## Meetings
Historically there are informal meetings about the specification around the Robothon conference (held every three years). On July 31, 2020, we had the first open virtual meeting, the [notes of which are online](https://docs.google.com/document/d/1REf695Yxnu3aj_UqcVfF0WTyV8PUaPo-r6duEHxtj48/edit).
