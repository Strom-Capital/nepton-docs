---
id: 13129687045789
title: Extend employment dates length in person import
url: https://support.nepton.com/hc/en-gb/articles/13129687045789-Extend-employment-dates-length-in-person-import
locale: en-gb
category: Support
category_id: 360000446658
section: System specific person imports
section_id: 7976634441629
section_path:
- Integration
- HR data
- System specific person imports
labels: []
promoted: false
updated_at: '2024-02-06T11:13:45Z'
edited_at: '2023-08-31T06:54:34Z'
---

# Extend employment dates length in person import

This article explains how employment dates for people are updated in person imports. Also, this article explains how to correct if employment start date or end date is imported incorrectly.
Note that employment dates extension logic works the same in all person import types except Default mapping.
## How it works?
  * If a person has an existing employment start date, imported start date can zero out (empty) the existing start date value, or change the start date value to an earlier date, but start date value can't be changed to later date
  * If a person has an existing employment end date, imported end date can zero out (empty) the the existing end date value, or change the end date value to later date, but end date value can't be changed to earlier date
  * These limitations ensure persons who have multiple employment dates can be viewed and managed properly in the service
  * At a later date, full support for multiple contracts per person will be added
  * Examples: 
    1.        1. No existing employment dates  
imported values  
Employment start date : 01.05.2021  
Employment end date : 31.08.2022  
result: 01.05.2021 - 31.08.2022 (new dates can be added when there are no existing dates)
       2. Existing employment dates 01.05.2021 - 31.08.2022  
imported values  
Employment start date : 01.01.2021  
Employment end date : 31.12.2021  
Result: 01.01.2021 - 31.08.2022 (start date can be changed to an earlier value but end date cannot)
       3. Existing employment dates 01.01.2021 - 31.08.2022  
imported values  
Employment start date : 01.01.2022  
Employment end date : 31.12.2022  
Result: 01.01.2021 - 31.12.2022 (end date can be extended to a later value but start date cannot)
       4. Existing employment dates 01.01.2021 - 31.12.2022  
imported values  
Employment start date : ""  
Employment end date : ""  
Result: no working contract start or end dates (working contract start date and end date can always be cleared)


## How to fix if you make a mistake while importing employment dates?
  * We want to import "01.01.2021 - 31.12.2023" as employment dates for a person  

    * We set by mistake the values as following  
Employment start date : 01.01.2022  
Employment end date : 31.12.2022  
Result: 01.01.2021 - 31.12.2023
  * Now we can fix the contract start date by performing following steps 
    1. First import values  
Employment start date : ""  
Employment end date : 31.12.2022  
Result: "" - 31.12.2023
    2. Now import the values  
Employment start date : 01.01.2021  
Employment end date : 31.12.2022  
Result: 01.01.2021 - 31.12.2023


  *
