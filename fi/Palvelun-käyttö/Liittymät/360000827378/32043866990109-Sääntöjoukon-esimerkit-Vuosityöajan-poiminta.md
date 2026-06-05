---
id: 32043866990109
title: Sääntöjoukon esimerkit - Vuosityöajan poiminta
url: https://support.nepton.com/hc/fi/articles/32043866990109-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-Vuosity%C3%B6ajan-poiminta
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels: []
promoted: false
updated_at: '2025-11-25T06:55:07Z'
edited_at: '2025-11-25T06:49:30Z'
---

# Sääntöjoukon esimerkit - Vuosityöajan poiminta

Artikkeliin on koottu tyypillisiä vuosityöajan poimintaan liittyviä esimerkkejä.
Löydät tietokantataulujen sarakekuvaukset [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>).
## Vuositavoitteen muodostumisen erittely
Esimerkki vuositavoitteen muodostumisen erittelystä. Arvot muodossa HH:MM tai HH:MM:SS:
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
Esimerkki vuositavoitteen muodostumisen erittelystä. Arvot desimaalitunteina:
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
