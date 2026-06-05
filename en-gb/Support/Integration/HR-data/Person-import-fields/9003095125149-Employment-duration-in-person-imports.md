---
id: 9003095125149
title: Employment duration in person imports
url: https://support.nepton.com/hc/en-gb/articles/9003095125149-Employment-duration-in-person-imports
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
updated_at: '2025-10-15T07:43:52Z'
edited_at: '2025-10-15T07:43:52Z'
---

# Employment duration in person imports

Employment duration information can be imported in [person imports](<https://support.nepton.com/hc/en-gb/articles/360003762577>) and the fields related to it are part of [person import fields](<https://support.nepton.com/hc/en-gb/articles/360015933397>).
"Default"-person import type doesn't update employment dates according to the rules described below.
On "Default"-person import type, employment dates will be imported exactly as the values are in the import data. In case you need to import using rules and possibilities of "Default"-import, but you want the import to only make the employment date range longer, use the import type "Extend working contract dates".
Employment days are updated in person imports following these rules:
  * Employment start date
    * If employment start date is not already set for a person, new date value is saved.
    * When employment start date has already been set for a person, it is only replaced if the new date is smaller than the set date or an empty value.
  * Employment end date
    * If employment end date is not already set for a person, new date value is saved.
    * When employment end date has already been set for a person, it is only replaced if the new date is greater then the set date or an empty value.


This restriction ensures that persons with multiple Employment start days are handled and showed correctly in Nepton.
If users are imported via the user interface, Employees->Persons->Import persons, any empty values in these fields are ignored, unless "Delete existing field values (Strict)" is chosen for "Empty values in import file"-selection.
