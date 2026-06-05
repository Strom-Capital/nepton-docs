---
id: 360020748037
title: Ruleset examples - event external identifier
url: https://support.nepton.com/hc/en-gb/articles/360020748037-Ruleset-examples-event-external-identifier
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
updated_at: '2025-03-28T12:27:14Z'
edited_at: '2025-03-28T12:27:13Z'
---

# Ruleset examples - event external identifier

This article contains typical examples on rules related to event external identifiers.
Database descriptions can be found [here](<https://support.nepton.com/hc/fi/articles/360002489257>)
### Select regular working hours and event external identifier
External identifier is selected as CustomData1
[code] 
    SELECT  
      usd.*,  
      SUM(usd.Amount) AS OverrideAmount,  
      uexid.ExternalIdentifier AS CustomData1  
    FROM  
      UserSalaryData usd  
    LEFT JOIN UserEventExternalIdentifierData uexid ON  
      uexid.ActivityId = usd.ActivityId  
      AND uexid.IdentifierType = 'External'  
    WHERE  
      usd.CompensationType = 'BasicTime'  
      AND usd.BasePartTarget IN ('salary','bank','balance','flexiblehours')  
      AND (usd.OvertimeTarget IS NULL OR usd.OvertimeTarget = 'uncompensated')  
      AND usd.ActivityTypeCode = 1   
    GROUP BY  
      usd.SalaryRenderingDate,  
      usd.ActivityId
[/code]
### Select regular working hours only from events that have an external identifier
External identifier is selected as CustomData1
[code] 
    SELECT  
      usd.*,  
      SUM(usd.Amount) AS OverrideAmount,  
      uexid.ExternalIdentifier AS CustomData1  
    FROM  
      UserSalaryData usd  
    JOIN UserEventExternalIdentifierData uexid ON  
      uexid.ActivityId = usd.ActivityId  
    WHERE  
      usd.CompensationType = 'BasicTime'  
      AND usd.BasePartTarget IN ('salary','bank','balance','flexiblehours')  
      AND (usd.OvertimeTarget IS NULL OR usd.OvertimeTarget = 'uncompensated')  
      AND usd.ActivityTypeCode = 1  
      AND e.IdentifierType = 'External'  
    GROUP BY  
      usd.SalaryRenderingDate,  
      usd.ActivityId
[/code]
### Select regular working hours only from events that have no external identifier
[code] 
    SELECT  
      usd.*,  
      SUM(usd.Amount) AS OverrideAmount  
    FROM  
      UserSalaryData usd  
    LEFT JOIN UserEventExternalIdentifierData uexid ON  
      uexid.ActivityId = usd.ActivityId  
      AND uexid.IdentifierType = 'External'  
    WHERE  
      usd.CompensationType = 'BasicTime'  
      AND usd.BasePartTarget IN ('salary','bank','balance','flexiblehours')  
      AND (usd.OvertimeTarget IS NULL OR usd.OvertimeTarget = 'uncompensated')  
      AND usd.ActivityTypeCode = '1'  
      AND uexid.ActivityId IS NULL  
    GROUP BY  
      usd.SalaryRenderingDate
[/code]
