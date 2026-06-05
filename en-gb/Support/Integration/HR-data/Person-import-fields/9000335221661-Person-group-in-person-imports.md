---
id: 9000335221661
title: Person group in person imports
url: https://support.nepton.com/hc/en-gb/articles/9000335221661-Person-group-in-person-imports
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
updated_at: '2023-01-27T14:10:17Z'
edited_at: '2023-01-27T12:00:34Z'
---

# Person group in person imports

Person group information can be imported as part of [person imports](<https://support.nepton.com/hc/en-gb/articles/360003762577>) and it is part of [person import fields](<https://support.nepton.com/hc/en-gb/articles/360015933397>).  
### Import rules
  * If the target person group doesn't exist, it is created at the root of the person group tree
  * A reset keyword will remove the person from any person group. There is no validity support for person group membership.


### Person Group including hierarchy information
  * Used for both setting person's person group and importing the person group hierarchy
  * Support for importing this information depends on source system/import mapping


### Person groups can be imported in two different ways
  * Using one field for person group codes and one for person group names. I.e. Codes, Names. Field naming depends on the source system 
    * The 'Codes' field contains pipe (|) character separated list of person group codes.  
Last rightmost code is the code of person's person group and codes left from that defined the person group hierarchy
    * The 'Names' field is similar to the 'Codes' field, but it contains the names of the person groups.  
Names field usage is optional and additional information to the codes. In case only codes are defined, new groups will have code as name.
  * Using multiple fields for person group codes and multiple fields for person group names. I.e. Code1, Code2 and Name1, Name2. 
    * Field naming depends on source system
    * The order of the fields is important, but not the names of the fields. The Last field is the code/name of persons person group and codes/names left from that defined the person group hierarchy
  * If the person group hierarchy defined in import doesn't exist it will be created 
    * If the first group defined in import doesn't exist, it will be created as a root person group 
      * Groups after the first group in the import, will be created and nested under it, unless matching existing groups are found, in which case existing groups with members are moved to the new position in the hierarchy.
    * If the first group defined in import exists, hierarchy defined in import will be created under it in case it doesn't exist
  * All person group codes must be unique, i.e. the same code cannot exist for two different groups even if they are in different hierarchies.
