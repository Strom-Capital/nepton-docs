---
id: 360016216278
title: Ruleset examples - event history
url: https://support.nepton.com/hc/en-gb/articles/360016216278-Ruleset-examples-event-history
locale: en-gb
category: Support
category_id: 360000446658
section: Rulesets
section_id: 360000827378
section_path:
- Integration
- Rulesets
labels: []
promoted: false
updated_at: '2025-05-06T11:35:20Z'
edited_at: '2025-05-06T11:35:20Z'
---

# Ruleset examples - event history

**UserEventHistoryData** table enables querying for all events, including edits and deletions during a given period. This article contains examples on filtering the data.
To filter events, you may use :exportPeriodStart and :exportPeriodEnd variables. :exportPeriodStart will be replaced in the query by the processed range start date in the format YYYY-MM-DD HH:MM:SS as defined in the export options for the integration ruleset or in the integration file download selections. :exportPeriodEnd will reflect the set processed range end date.
Database table descriptions can be found [here](<https://support.nepton.com/hc/fi/articles/360002489257>)
Prettify/format query functionality is not supported when using Data query testing and development tool with :exportPeriodStart and :exportPeriodEnd.
### Select all events overlapping processed range
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData   
    WHERE   
      StartDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd   
      OR   
      EndDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd
[/code]
### Select all events modified during processed range
This example can be used to select all modified events on certain date regardless of edited events start or end dates.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData   
    WHERE  
      ModifiedDateTime BETWEEN :exportPeriodStart AND :exportPeriodEnd
[/code]
### Select all events modified on processed range and join with their current version.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData AS ModifiedEventData   
    LEFT JOIN UserEventHistoryData AS CurrentEventData   
      ON ModifiedEventData.OriginalActivityId = CurrentEventData.ActivityId   
    WHERE   
      ModifiedEventData.ModifiedDateTime BETWEEN :exportPeriodStart AND :exportPeriodEnd
[/code]
### Select deleted events overlapping processed range
This query will select all events that have been deleted and overlapped the given period without any previous versions.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData   
    WHERE  
      ((StartDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd)   
        OR   
       (EndDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd))  
      AND IsActive = 'N'  
      AND OriginalActivityId IS NULL
[/code]
### Select events deleted during processed range
This query will select all events that have been were deleted during the given period regardless of when the event occurs without any previous versions.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData   
    WHERE   
      ModifiedDateTime BETWEEN :exportPeriodStart AND :exportPeriodEnd  
      AND IsActive = 'N'  
      AND OriginalActivityId IS NULL
[/code]
### Select all events deleted events processed range and have their last version deleted
Event is considered deleted when the last modified version of the event is deleted. If there is another version then event is not deleted but modified.
An event that has been moved to another time period or otherwise changed may also have been deleted in a later edit. This query will select all events that overlap the given time period and have been eventually deleted.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData AS ModifiedEventData   
    LEFT JOIN UserEventHistoryData AS CurrentEventData   
      ON ModifiedEventData.OriginalActivityId = CurrentEventData.ActivityId   
    WHERE   
      ((ModifiedEventData.StartDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd)   
        OR   
       (ModifiedEventData.EndDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd))  
      AND  
      ((ModifiedEventData.IsActive = 'N' AND ModifiedEventData.OriginalActivityId IS NULL)  
       OR  
       CurrentEventData.IsActive = 'N')
[/code]
