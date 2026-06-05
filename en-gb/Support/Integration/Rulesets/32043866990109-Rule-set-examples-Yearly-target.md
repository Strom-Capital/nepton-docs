---
id: 32043866990109
title: Rule set examples - Yearly target
url: https://support.nepton.com/hc/en-gb/articles/32043866990109-Rule-set-examples-Yearly-target
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
updated_at: '2025-11-25T06:55:07Z'
edited_at: '2025-11-25T06:54:53Z'
---

# Rule set examples - Yearly target

The article presents some commonly used SQL queries when exportin yearly target data..
Please find all database tables [here](<https://support.nepton.com/hc/en-gb/articles/360002489257>).
## Breakdown of how the annual target is formed
Example of breakdown of annual target formation. Values ​​in HH:MM or HH:MM:SS format:
[code]
    SELECT u.FirstName || ' ' || u.LastName AS PersonName,
    minutesToHHMM(p.CalculatedTargetInMinutes) AS CalculatedTargetHHMM,
    minutesToHHMM(p.ConfiguredTargetInMinutes) AS ConfiguredTargetHHMM,
    p.WorktimePercentage AS WorkTimePercentage,
    minutesToHHMMSS(p.TargetReductionFromEventsInMinutes) AS TargetReductionFromEventsHHMMSS,
    minutesToHHMMSS(p.ContributedMinutesToTarget) AS ContributedToTargetHHMMSS,
    p.ContributionBeginDate || ' - ' || p.ContributionEndDate AS ContributionPeriod,
    p.YearTargetPeriodBeginDate || ' - ' || p.YearTargetPeriodEndDate AS YearTargetPeriod
    
    FROM PlanningYearTargetBreakdownData p
    JOIN UserData u ON (u.UserId = p.UserId);
[/code]
Example of breakdown of annual target formation. Values ​​in decimal hours:
[code]
    SELECT u.FirstName || ' ' || u.LastName AS PersonName,
    ROUND(p.CalculatedTargetInMinutes / 60.0, 2) AS CalculatedTargetHours,
    ROUND(p.ConfiguredTargetInMinutes / 60.0, 2) AS ConfiguredTargetHours,
    p.WorktimePercentage AS WorkTimePercentage,
    ROUND(p.TargetReductionFromEventsInMinutes / 60.0, 2) AS TargetReductionFromEventsHours,
    ROUND(p.ContributedMinutesToTarget / 60.0, 2) AS ContributedToTargetHours,
    p.ContributionBeginDate || ' - ' || p.ContributionEndDate AS ContributionPeriod,
    p.YearTargetPeriodBeginDate || ' - ' || p.YearTargetPeriodEndDate AS YearTargetPeriod
    
    FROM PlanningYearTargetBreakdownData p
    JOIN UserData u ON (u.UserId = p.UserId);
[/code]
