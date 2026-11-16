---
id: 4408898681233
title: Mandatory fields in person form
url: https://support.nepton.com/hc/en-gb/articles/4408898681233-Mandatory-fields-in-person-form
locale: en-gb
category: Support
category_id: 360000446658
section: Person details management
section_id: 360004485937
section_path:
- HR management
- Person details management
labels: []
promoted: false
updated_at: '2026-11-06T10:36:08Z'
edited_at: '2026-10-15T05:26:28Z'
---

# Mandatory fields in person form

When a new person is added via the person form, certain information is required to be set so that the person information can be saved. The field values may have[ multiple values for different time periods](<https://support.nepton.com/hc/en-gb/articles/360004856937>) but there must be a value for all times. These mandatory fields are:
  * First name
  * Last name
  * Password
  * Role
  * Service usage language
  * Username


For [person import](<https://support.nepton.com/hc/en-gb/articles/360003762577>) the rules for mandatory fields are different.
## Mandatory fields as additional information fields
When additional person information fields are created in the Employees section > Administration > [person’s additional fields](<https://support.nepton.com/hc/en-gb/articles/360002430918>), the fields can be marked as mandatory for everyone or only for some roles. If a person has a role that requires to have a specific field defined, it must have current values ​​as well as values ​​for the past and future when filling personal information, like always with mandatory fields.
Also, when importing users, the required additional person information fields must have current values ​​and values ​​for the past and future. However, if the data for mandatory additional fields of a person are missing in the import, the person data can be imported despite the missing data. In the case of manual personal import, a warning is displayed and in the case of automated personal data imports, a warning message is recorded in the service log.
