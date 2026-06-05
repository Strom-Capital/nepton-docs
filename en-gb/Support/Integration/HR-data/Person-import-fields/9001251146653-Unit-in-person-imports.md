---
id: 9001251146653
title: Unit in person imports
url: https://support.nepton.com/hc/en-gb/articles/9001251146653-Unit-in-person-imports
locale: en-gb
category: Support
category_id: 360000446658
section: Person import fields
section_id: 9000763181981
section_path:
- Integration
- HR data
- Person import fields
labels: []
promoted: false
updated_at: '2026-06-03T13:12:12Z'
edited_at: '2026-06-03T13:11:28Z'
---

# Unit in person imports

Persons unit can be imported in [person imports](<https://support.nepton.com/hc/en-gb/articles/360003762577>) and it is part of [person import fields](<https://support.nepton.com/hc/en-gb/articles/360015933397>). The unit must first be created in Nepton before it can be used in person import.
### Import rules
  * Can be set by either unit name or code
  * If you wish to set multiple relationships they must be separated by the pipe (|) character
  * The first Unit in the list will be set as primary unit
  * RESET keyword will remove all the units assigned to a person
    * Empty value will not remove the units for a person if the IgnoreEmptyValues setting is applied (e.g. via the web service)
