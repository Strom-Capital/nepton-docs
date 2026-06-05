---
id: 26673690781341
title: Workshift planning in Reporting
url: https://support.nepton.com/hc/en-gb/articles/26673690781341-Workshift-planning-in-Reporting
locale: en-gb
category: Support
category_id: 360000446658
section: Insights service
section_id: 25746849648925
section_path:
- Reporting
- Insights service
labels: []
promoted: false
updated_at: '2025-09-29T08:53:43Z'
edited_at: '2025-09-01T08:57:54Z'
---

# Workshift planning in Reporting

# Basic Principles
From the data stored for work shift planning, you can add to a query:
  * Planned and published shifts regardless of how they were created
  * Combinations of shifts, for example:
    * Total planned work for Fri–Sat, Sat–Sun, and Sun–Mon combinations
    * Work scheduled on public holidays
  * Data related to rest-time monitoring, such as:
    * Various shift types (only if shift calendars are in use)
      * e.g. how many evening→morning shift combinations occurred
      * If you’re not using shift calendars (traditional mode), no shift types exist and this data can’t be obtained


**Note:** Extracted shift durations do not account for assumed meal breaks from roster planning. For example, a planned 8 h shift with an automatic 30 min break still appears as 8 h, not 7 h 30 min.
## Available Fields
  * Person’s shift-calendar code and name
  * Person’s leave-calendar code and name
  * Shifts planned and published via roster planning and shift calendars (start and end date/time)
  * For each planned and published shift:
    * Planned event type (code)
    * Abbreviation (from the shift calendar)
    * Additional shift-type information
    * Public shift information (cannot extract shift-group public info)
      * You can search within this public info for specific characters or substrings (e.g. a keyword)


## Can not be added to a query
  * Shift-calendar contents (schemas)
  * Leave-calendar contents (schemas)
  * Shift requirements
  * Tasks
  * Competencies
  * Shift-group planning data
  * Shift-group public information
  * Detailed shift-planning notes
