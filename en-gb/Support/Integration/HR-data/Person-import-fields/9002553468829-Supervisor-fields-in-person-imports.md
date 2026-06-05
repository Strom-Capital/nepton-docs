---
id: 9002553468829
title: Supervisor fields in person imports
url: https://support.nepton.com/hc/en-gb/articles/9002553468829-Supervisor-fields-in-person-imports
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
updated_at: '2024-07-12T05:52:31Z'
edited_at: '2024-02-29T12:04:35Z'
---

# Supervisor fields in person imports

Persons supervisor information can be imported in [person imports](<https://support.nepton.com/hc/en-gb/articles/360003762577>) and the fields related to it are part of [person import fields](<https://support.nepton.com/hc/en-gb/articles/360015933397>).
### Primary supervisors/Secondary supervisors
  * These two input fields are for setting primary and/or secondary supervisors by employee number (Primary supervisor and Secondary supervisors)
  * The primary supervisor field works in the following way: 
    * If a value is provided then the existing primary supervisor is replaced with the new one
    * If there are more than one supervisors in this field, first one will be used as primary supervisor and rest of the supervisors will be ignored
    * Primary supervisor will be removed the field value is left empty in the import or the RESET keyword is imported as the value - regardless of if IgnoreEmptyValues setting is used or not (e.g. via the web service)
  * Secondary supervisors (Toissijaiset esimiehet) field works in the following way  

    * With RESET| or NOLLA| prefix - This will replace any existing secondary supervisors, with the new supervisor(s)
    * Without RESET| or NOLLA| prefix - This will append new supervisor(s) to the existing secondary supervisors list
    * Support the RESET keyword and respects the IgnoreEmptyValues setting. i.e. It will leave supervisors as they are if an empty value is sent and IgnoreEmptyValues is True (e.g. via the web service)
  * At present the primary supervisor field only supports a single relationship, but later we will permit multiple primary supervisors


Please be aware that notifications concerning subordinate-sensitive actions, such as Sick Leave, Balance Leave, and Annual Leave requests, are directed solely to primary supervisors.
