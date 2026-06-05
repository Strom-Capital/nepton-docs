---
id: 360015807338
title: Field validities in person imports
url: https://support.nepton.com/hc/en-gb/articles/360015807338-Field-validities-in-person-imports
locale: en-gb
category: Support
category_id: 360000446658
section: Field validities in person imports
section_id: 360004603778
section_path:
- Integration
- HR data
- Field validities in person imports
labels: []
promoted: false
updated_at: '2023-12-12T14:18:19Z'
edited_at: '2023-01-27T00:01:38Z'
---

# Field validities in person imports

It is possible to define for which time period a certain field value is valid for person information. This makes it possible e.g. to save future person information changes advance (more about [validities](<https://support.nepton.com/hc/en-gb/articles/360004856937>)). Importing validity information makes it also possible to correctly import the data even if there are delays in the import because of connection problems or service interruptions. This is very important for fields like work time percentage or worktime setting group, where the validity plays a crucial part.
We recommend that a new person imported to Nepton platform is imported without validity information.
Use the _Employment start date_ field to indicate the date the person starts/has started working.
The method used for importing validity information depends on the source system of the imported data. All source systems do not support importing data with validity information.
There are three different methods of import concerning validity information:
  * [Without validity information](<https://support.nepton.com/hc/en-gb/articles/360015741097>)
  * [With Valid from information](<https://support.nepton.com/hc/en-gb/articles/360015754117>)
  * [With Valid from and Valid to information](<https://support.nepton.com/hc/en-gb/articles/360015842238>)


The "Default" person import type which can be used, for example, in [manual person import](<https://support.nepton.com/hc/en-gb/articles/360003762577>), supports importing [without validity information](<https://support.nepton.com/hc/en-gb/articles/360015741097>) and [with Valid from information](<https://support.nepton.com/hc/en-gb/articles/360015754117>). The support for methods of validity information import varies depending on person import type and the source system of the imported data. You can find more detailed information about supported methods of validity information import in the person import type specific guidance.
There must be values for [mandatory fields](<https://support.nepton.com/hc/en-gb/articles/360015933397>) for all times even after person imports.
