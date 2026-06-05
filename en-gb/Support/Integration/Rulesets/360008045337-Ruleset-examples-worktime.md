---
id: 360008045337
title: Ruleset examples - worktime
url: https://support.nepton.com/hc/en-gb/articles/360008045337-Ruleset-examples-worktime
locale: en-gb
category: Support
category_id: 360000446658
section: Rulesets
section_id: 360000827378
section_path:
- Integration
- Rulesets
labels:
- sääntöjoukko
- poimintasäännöt
- palkkaliittymä
- poiminta
promoted: false
updated_at: '2026-02-25T10:46:44Z'
edited_at: '2026-02-25T10:46:44Z'
---

# Ruleset examples - worktime

Please note that creating and modifying integration rules requires a basic understanding of SQL.
This article presents a typical integration ruleset for payroll. It showcases best practices for defining payroll rules, where a single rule captures an entire set at once - such as all overtime hours. These rules can be used as they are, but you must take into account the requirements of the target system, such as data grouping and possible system-specific data fields.
  * [This article](<https://support.nepton.com/hc/fi/articles/21077132021149>) covers the basic principles of creating an integration rule set.  
Additionally, the most commonly needed additional rules are introduced.  

  * You can find descriptions of the database table columns [here](<https://support.nepton.com/hc/fi/articles/360002489257>).  

  * Examples of other integration rulesets can be found in the following articles:  
  
[Rule set examples for absences](<https://support.nepton.com/hc/en-gb/articles/360013979998>)  
[Rule set examples for project details, structure and project types](<https://support.nepton.com/hc/en-gb/articles/360013894637>)  
[Rule set examples for personnel data](<https://support.nepton.com/hc/en-gb/articles/360015612638>)


### Extraction of personnel data (UserInfoData)
NOTE: If personnel data is linked by using a JOIN clause incorrectly, this can easily lead to the duplication of hourly amounts in payroll data.
If personnel data needs to be retrieved from multiple different personnel data fields, multiple JOIN clauses are required.
Instead of using JOIN clauses, also the following method can be used to retrieve data from multiple different personnel data fields:
[code]
    SELECT
      usd.*,
      SUM(Amount) AS OverrideAmount,
    -- Person group code selected to field CustomData1
      IFNULL(
        (SELECT
           uid.Value
         FROM
           UserInfoData uid
         WHERE uid.InfoTypeName = 'UserGroupCode_SDSQL'
         AND datetime(usd.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo
         LIMIT 1), '') AS CustomData1,
    -- Payment group code,selected to field CustomData2
      IFNULL(
        (SELECT
           uid.Value
         FROM
           UserInfoData uid
         WHERE
           uid.InfoTypeName = 'NeptonPaymentGroupCode_SDSQL'
           AND datetime(usd.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo
         LIMIT 1), '') AS CustomData2
    FROM
      UserSalaryData usd
    GROUP BY
      usd.SalaryRenderingDate,
      usd.CompensationType,
      usd.ProjectCode1
[/code]
## Rule set model
The following integration rules are set up for the Integration ruleset. These model rules are formed so that each rule extracts a complete set of data at once, such as all overtime hours or sick leave types. The model rules must be modified to include the correct system-specific or customer-specific pay types and the desired grouping.
### Interpreted work time without overtime (hourly paid)
Extract all events that count toward regular working hours (CompensationType = 'BasicTime'), as well as time deducted from the balance.
[code]
    SELECT
      *, 
      SUM(Amount) As OverrideAmount
    FROM 
      UserSalaryData
    WHERE
      (ActivityTypeCategoryId = 1
      AND CompensationType = 'BasicTime'
      AND BasePartTarget = 'salary'
      AND (OvertimeTarget IS NULL OR OvertimeTarget = 'uncompensated')) -- Worked hours
      OR
      (BasePartTarget = 'salary' AND ActivityTypeCode IS NULL AND IsTimeBorrowedFromBAlance = 'Y') -- Deducted from balance
    --  AND EmployeeSalaryType = 'hourly'
    GROUP BY 
      SalaryRenderingDate
[/code]
If results need to be grouped not only by day (SalaryRenderingDate) but also by project, the GROUP BY section should include, as needed, ProjectCode1, ProjectCode2, ProjectCode3, ProjectCode4, ProjectCode5, ProjectCode6.
[code]
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6
[/code]
If the payroll system requires specifying the notes added to an event, then grouping should also be done by notes (Comment).
[code]
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
[/code]
### Interpreted overtime
Extract all events that generate overtime, where both the base-part and the overtime-part are paid as salary.
If the extracted data contains rows without a set salary code, these rows will get the salary code 'NOT_DEFINED'.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      CASE
        BasePartTarget = 'salary' AND OvertimeTarget = 'salary' 
        WHEN CompensationType = 'AdditionalWork' AND OvertimePercentage = 0 THEN 'ADDITIONALWORK0%_SALARY_CODE' -- additional work 0%
        WHEN CompensationType = 'AdditionalWork' AND OvertimePercentage = 50 THEN 'ADDITIONALWORK50%_SALARY_CODE' -- additional work 50%
        WHEN CompensationType = 'OvertimeDaily50' THEN  'DAY50_SALARY_CODE' -- day50
        WHEN CompensationType = 'OvertimeDaily100' THEN 'DAY100_SALARY_CODE' -- day100
        WHEN CompensationType = 'OvertimeWeekly50' THEN 'WEEK50_SALARY_CODE' -- week50
        WHEN CompensationType = 'OvertimeWeekly100' THEN 'WEEK100_SALARY_CODE' -- week100
        WHEN CompensationType = 'OvertimeSunday50' THEN 'SUNDAY50_SALARY_CODE' -- Sunday50
        WHEN CompensationType = 'OvertimeSunday100' THEN 'SUNDAY100_SALARY_CODE' -- Sunday100
        WHEN CompensationType = 'OvertimeBaseFixed' THEN 'BASEFIXED_SALARY_CODE' -- Base fixed
        WHEN CompensationType = 'OvertimeExtraFixed' THEN 'EXTRAFIXED_SALARY_CODE' -- Extra fixed
        WHEN CompensationType = 'LevellingPeriodAdditional' THEN 'LEVELLINGPERIODADDITIONAL_SALARY_CODE' -- Levelling period additional work
        WHEN CompensationType = 'LevellingPeriodOvertime50' THEN 'LEVELLINGPERIOROVERTIME50_SALARY_CODE' -- Levelling period overtime 50
        WHEN CompensationType = 'LevellingPeriodOvertime100' THEN 'LEVELLINGPERIOROVERTIME100_SALARY_CODE' -- Levelling period overtime 100
        ELSE 'NOT_DEFINED'
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('AdditionalWork', 'OvertimeDaily50', 'OvertimeDaily100', 'OvertimeWeekly50',
                           'OvertimeWeekly100', 'OvertimeSunday50', 'OvertimeSunday100',
                           'OvertimeBaseFixed', 'OvertimeExtraFixed', 'TESOvertime50', 'TESOvertime100',
                           'LevellingPeriodAdditional', 'LevellingPeriodOvertime50', 'LevellingPeriodOvertime100')
      AND BasePartTarget = 'salary'
      AND OvertimeTarget = 'salary'
      AND IsApproved = 'Y'
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Work rises
All work rises are extracted and assigned the salary code set in the work rise settings. The salary code can be formatted using slashes ("/") to represent:
  * First part: regular working hours pay type
  * Second part: 50% overtime pay type
  * Third part: 100% overtime pay type


However, splitting the code like this isn't mandatory - the rule will pick up the full code regardless of formatting.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      CASE
        WHEN instr(WorkRiseSalaryCode,'/') = 0 OR WorkRiseEarnedAtCompensationType = 'BasicTime' THEN substring_part(WorkRiseSalaryCode, '/', 1)
        WHEN WorkRiseEarnedAtCompensationType IN ('OvertimeDaily50','OvertimeWeekly50','OvertimeSunday50') THEN substring_part(WorkRiseSalaryCode, '/', 2)
        ELSE substring_part(WorkRiseSalaryCode, '/', 3) 
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'WorkRise' 
      AND workrisepaytarget = 'Salary'
      AND IsApproved = 'Y'
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Supplements
Extract all work supplements and assign them the salary code set in the supplement settings.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      WorkIncrementCode as OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'WorkIncrement' 
      AND IsApproved = 'Y'
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Part-day sick leave
Extract all part-day sick leaves.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      CASE
        WHEN SickLeaveTypeId = 1 AND CompensationType = 'UnpaidBasicTime' THEN 'UNPAID_SICK' -- unpaid, sick
        WHEN SickLeaveTypeId = 2 AND CompensationType = 'UnpaidBasicTime' THEN 'UNPAID_CHILD_SICK' -- unpaid, child sick
        WHEN SickLeaveTypeId = 3 AND CompensationType = 'UnpaidBasicTime' THEN 'UNPAID_ACCIDENT_AT_WORK' -- unpaid, accident at work 
        WHEN SickLeaveTypeId = 4 AND CompensationType = 'UnpaidBasicTime' THEN 'UNPAID_ACCIDENT_WHILE_COMMUTING' -- unpaid, accident while commuting
        WHEN SickLeaveTypeId = 5 AND CompensationType = 'UnpaidBasicTime' THEN 'UNPAID_ACCIDENT_IN_FREE_TIME' -- unpaid, accident in free time
        WHEN SickLeaveTypeId = 1 AND CompensationType = 'BasicTime' THEN 'PAID_SICK' -- paid, sick
        WHEN SickLeaveTypeId = 2 AND CompensationType = 'BasicTime' THEN 'PAID_CHILD_SICK' -- paid, child sick
        WHEN SickLeaveTypeId = 3 AND CompensationType = 'BasicTime' THEN 'PAID_ACCIDENT_AT_WORK' -- paid, accident at work
        WHEN SickLeaveTypeId = 4 AND CompensationType = 'BasicTime' THEN 'PAID_ACCIDENT_WHILE_COMMUTING' -- paid, accident while commuting
        WHEN SickLeaveTypeId = 5 AND CompensationType = 'BasicTime' THEN 'UNPAID_ACCIDENT_IN_FREE_TIME' -- paid, accident in free time
        WHEN SickLeaveTypeId IS NOT NULL THEN ('Sick_leave: ' || SickLeaveTypeId || ' - ' || CompensationType) --this row picks up all sick leaves´types that are not picked up by the rule already
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('BasicTime','UnpaidBasicTime')
      AND SickLeaveTypeId IS NOT NULL
      AND IsApproved = 'Y'
    -- With the condition below, only those days are included where work time has also been compensated as work
      AND SalaryRenderingDate IN 
        (SELECT
           SalaryRenderingDate 
         FROM
           UserSalaryData 
         WHERE
           ActivityTypeCategoryId = 1
           AND CompensationType IN ('BasicTime', 'AdditionalWork', 'OvertimeDaily50', 'OvertimeDaily100',
                                    'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50', 'OvertimeSunday100'))
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Part-day absences
Extract all part-day absences.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      CASE
        WHEN AbsenceTypeId = 25 AND CompensationType = 'UnpaidBasicTime' THEN 'TRAID_UNION_EVENTS_UNPAID' -- Unpaid, Trade union events 
        WHEN AbsenceTypeId = 10 AND CompensationType = 'UnpaidBasicTime' THEN 'MILITARY_OR_CIVIL_SERVICE_TIME_UNPAID' -- Unpaid, Military or civil service time 
        WHEN AbsenceTypeId = 1 AND CompensationType = 'UnpaidBasicTime' THEN 'SPECIAL_MATERNITY_LEAVE_UNPAID'-- Unpaid, Special maternity leave 
        WHEN AbsenceTypeId = 5 AND CompensationType = 'UnpaidBasicTime' THEN 'NURSING_LEAVE_UNPAID'-- Unpaid, Nursing leave 
        WHEN AbsenceTypeId = 3 AND CompensationType = 'UnpaidBasicTime' THEN 'PATERNITY_LEAVE_UNPAID'-- Unpaid, Paternity leave 
        WHEN AbsenceTypeId = 11 AND CompensationType = 'UnpaidBasicTime' THEN 'MILITARY_REFRESHER_COURSE_UNPAID'-- Unpaid, Military refresher course
        WHEN AbsenceTypeId = 27 AND CompensationType = 'UnpaidBasicTime' THEN 'REHABILITATION_UNPAID' -- Unpaid, Rehabilitation 
        WHEN AbsenceTypeId = 18 AND CompensationType = 'UnpaidBasicTime' THEN 'MILITARY_CALL_TO_ARMS_HAPPENING_UNPAID' -- Unpaid, Military call to arms happening 
        WHEN AbsenceTypeId = 13 AND CompensationType = 'UnpaidBasicTime' THEN 'OTHER_UNPAID' -- Unpaid, other absence 
        WHEN AbsenceTypeId = 26 AND CompensationType = 'UnpaidBasicTime' THEN 'MOVING_LEAVE_UNPAID' -- Unpaid, Moving leave 
        WHEN AbsenceTypeId = 452 AND CompensationType = 'UnpaidBasicTime' THEN 'FAMILY_CARE_LEAVE_UNPAID' -- Unpaid, Family care leave
        WHEN AbsenceTypeId = 17 AND CompensationType = 'UnpaidBasicTime' THEN 'OWN_50TH_OR_60TH_BIRTHDAY_UNPAID' -- Unpaid, Own 50th or 60th birthday
        WHEN AbsenceTypeId = 16 AND CompensationType = 'UnpaidBasicTime' THEN 'OWN_MARRIAGE_UNPAID' -- Unpaid, Own marriage 
        WHEN AbsenceTypeId = 8 AND CompensationType = 'UnpaidBasicTime' THEN 'STUDY_LEAVE_UNPAID' -- Unpaid, Study leave
        WHEN AbsenceTypeId = 22 AND CompensationType = 'UnpaidBasicTime' THEN 'PART_TIME_PENSION_UNPAID' -- Unpaid, Part time pension
        WHEN AbsenceTypeId = 31 AND CompensationType = 'UnpaidBasicTime' THEN 'PART-TIMER_UNPAID' -- Unpaid, Part-timer 
        WHEN AbsenceTypeId = 14 AND CompensationType = 'UnpaidBasicTime' THEN 'FAMILY_MEMBERS_DEATH_UNPAID' -- Unpaid, Family members death 
        WHEN AbsenceTypeId = 15 AND CompensationType = 'UnpaidBasicTime' THEN 'FAMILY_MEMBERS_FUNERAL_UNPAID' -- Unpaid, Family members funeral 
        WHEN AbsenceTypeId = 20 AND CompensationType = 'UnpaidBasicTime' THEN 'FAMILY_MEMBER_BECOMING_SICK_SUDDENLY_UNPAID' -- Unpaid, Family member becoming sick suddenly 
        WHEN AbsenceTypeId = 7 AND CompensationType = 'UnpaidBasicTime' THEN 'COMPULSORY_FAMILY_REASON_UNPAID' -- Unpaid, Absence due to compulsory family reason
        WHEN AbsenceTypeId = 450 AND CompensationType = 'UnpaidBasicTime' THEN 'PREGNANCY_LEAVE_UNPAID' -- Unpaid, Pregnancy leave
        WHEN AbsenceTypeId = 6 AND CompensationType = 'UnpaidBasicTime' THEN 'TEMPORARY_NURSING_LEAVE_UNPAID' -- Unpaid, Temporary nursing leave 
        WHEN AbsenceTypeId = 19 AND CompensationType = 'UnpaidBasicTime' THEN 'OFF_DUTY_UNPAID' -- Unpaid, Off duty
        WHEN AbsenceTypeId = 12 AND CompensationType = 'UnpaidBasicTime' THEN 'PERSONAL_REQUEST_LEAVE_UNPAID' -- Unpaid, Personal request leave 
        WHEN AbsenceTypeId = 451 AND CompensationType = 'UnpaidBasicTime' THEN 'PARENTAL_LEAVE_UNPAID' -- Unpaid, Parental leave
        WHEN AbsenceTypeId = 4 AND CompensationType = 'UnpaidBasicTime' THEN 'PARENTAL_LEAVE_UNPAID'-- Unpaid, Parental leave (pre-reform) 
        WHEN AbsenceTypeId = 23 AND CompensationType = 'UnpaidBasicTime' THEN 'LEAVE_OF_ABSENCE_UNPAID' -- Unpaid, Leave of absence
        WHEN AbsenceTypeId = 9 AND CompensationType = 'UnpaidBasicTime' THEN 'JOB_ALTERNATION_LEAVE_UNPAID' -- Unpaid, Job alternation leave 
        WHEN AbsenceTypeId = 2 AND CompensationType = 'UnpaidBasicTime' THEN 'MATERNITY_LEAVE_UNPAID' -- Unpaid, Maternity leave
        WHEN AbsenceTypeId = 25 AND CompensationType = 'BasicTime' THEN 'TRAID_UNION_EVENTS_PAID' -- Paid, Trade union events
        WHEN AbsenceTypeId = 10 AND CompensationType = 'BasicTime' THEN 'MILITARY_OR_CIVIL_SERVICE_TIME_PAID' -- Paid, Military or civil service time
        WHEN AbsenceTypeId = 1 AND CompensationType = 'BasicTime' THEN 'SPECIAL_MATERNITY_LEAVE_PAID'-- Paid, Special maternity leave
        WHEN AbsenceTypeId = 5 AND CompensationType = 'BasicTime' THEN 'NURSING_LEAVE_PAID'-- Paid, Nursing leave 
        WHEN AbsenceTypeId = 3 AND CompensationType = 'BasicTime' THEN 'PATERNITY_LEAVE_PAID'-- Paid, Paternity leave 
        WHEN AbsenceTypeId = 11 AND CompensationType = 'BasicTime' THEN 'MILITARY_REFRESHER_COURSE_PAID'-- Paid, Military refresher course
        WHEN AbsenceTypeId = 27 AND CompensationType = 'BasicTime' THEN 'REHABILITATION_PAID' -- Paid, Rehabilitation 
        WHEN AbsenceTypeId = 18 AND CompensationType = 'BasicTime' THEN 'MILITARY_CALL_TO_ARMS_HAPPENING_PAID' -- Paid, Military call to arms happening
        WHEN AbsenceTypeId = 13 AND CompensationType = 'BasicTime' THEN 'OTHER_PAID' -- Paid, other absence 
        WHEN AbsenceTypeId = 26 AND CompensationType = 'BasicTime' THEN 'MOVING_LEAVE_PAID' -- Paid, Moving leave 
        WHEN AbsenceTypeId = 452 AND CompensationType = 'BasicTime' THEN 'FAMILY_CARE_LEAVE_PAID' -- Paid, Family care leave
        WHEN AbsenceTypeId = 17 AND CompensationType = 'BasicTime' THEN 'OWN_50TH_OR_60TH_BIRTHDAY_PAID' -- Paid, Own 50th or 60th birthday
        WHEN AbsenceTypeId = 16 AND CompensationType = 'BasicTime' THEN 'OWN_MARRIAGE_PAID' -- Paid, Own marriage 
        WHEN AbsenceTypeId = 8 AND CompensationType = 'BasicTime' THEN 'STUDY_LEAVE_PAID' -- Paid, Study leave
        WHEN AbsenceTypeId = 22 AND CompensationType = 'BasicTime' THEN 'PART_TIME_PENSION_PAID' -- Paid, Part time pension
        WHEN AbsenceTypeId = 31 AND CompensationType = 'BasicTime' THEN 'PART-TIMER_PAID' -- Paid, Part-timer
        WHEN AbsenceTypeId = 14 AND CompensationType = 'BasicTime' THEN 'FAMILY_MEMBERS_DEATH_PAID' -- Paid, Family members death 
        WHEN AbsenceTypeId = 15 AND CompensationType = 'BasicTime' THEN 'FAMILY_MEMBERS_FUNERAL_PAID' -- Paid, Family members funeral 
        WHEN AbsenceTypeId = 20 AND CompensationType = 'BasicTime' THEN 'FAMILY_MEMBER_BECOMING_SICK_SUDDENLY_PAID' -- Paid, Family member becoming sick suddenly
        WHEN AbsenceTypeId = 7 AND CompensationType = 'BasicTime' THEN 'COMPULSORY_FAMILY_REASON_PAID' -- Paid, Absence due to compulsory family reason
        WHEN AbsenceTypeId = 450 AND CompensationType = 'BasicTime' THEN 'PREGNANCY_LEAVE_PAID' --Paid, Pregnancy leave
        WHEN AbsenceTypeId = 6 AND CompensationType = 'BasicTime' THEN 'TEMPORARY_NURSING_LEAVE_PAID' -- Paid, Temporary nursing leave 
        WHEN AbsenceTypeId = 19 AND CompensationType = 'BasicTime' THEN 'OFF_DUTY_PAID' -- Paid, Off duty
        WHEN AbsenceTypeId = 12 AND CompensationType = 'BasicTime' THEN 'PERSONAL_REQUEST_LEAVE_PAID' -- Paid, Personal request leave
        WHEN AbsenceTypeId = 451 AND CompensationType = 'BasicTime' THEN 'PARENTAL_LEAVE_PAID' -- Paid, Parental leave
        WHEN AbsenceTypeId = 4 AND CompensationType = 'BasicTime' THEN 'PARENTAL_LEAVE_PAID'-- Paid, Parental leave (pre-reform) 
        WHEN AbsenceTypeId = 23 AND CompensationType = 'BasicTime' THEN 'LEAVE_OF_ABSENCE_PAID' -- Paid, Leave of absence
        WHEN AbsenceTypeId = 9 AND CompensationType = 'BasicTime' THEN 'JOB_ALTERNATION_LEAVE_PAID' -- Paid, Job alternation leave 
        WHEN AbsenceTypeId = 2 AND CompensationType = 'BasicTime' THEN 'MATERNITY_LEAVE_PAID' -- Paid, Maternity leave
        WHEN AbsenceTypeId IS NOT NULL THEN ('ABSENCE: ' || AbsenceTypeId || ' - ' || CompensationType) --this row picks up all absence types set up by the customer without a specific salary code set
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('BasicTime','UnpaidBasicTime')
      AND AbsenceTypeID IS NOT NULL
      AND IsApproved = 'Y'
      AND SalaryRenderingDate IN 
      (SELECT
         SalaryRenderingDate 
       FROM
         UserSalaryData 
       WHERE
         ActivityTypeCategoryId = 1
         AND CompensationType IN ('BasicTime', 'AdditionalWork', 'OvertimeDaily50', 'OvertimeDaily100',
                                  'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50', 'OvertimeSunday100'))
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Weekly rest period and public holiday compensation
Extract weekly rest compensation and public holidays
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      CASE 
        WHEN CompensationType = 'WeeklyRestTime' THEN 'WEEKLY_REST_PERIOD'
        WHEN CompensationType = 'PublicHoliday' THEN 'PUBLIC_HOLIDAYS'
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('WeeklyRestTime', 'PublicHoliday')
      AND IsApproved = 'Y'
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### On-call time after deducting work hours during on-call
The query below extracts on-call time. Events logged on top of on-call time will reduce its duration, unless specific event types are configured in the system not to reduce it. Learn more about on-call settings from [here](<https://support.nepton.com/hc/en-gb/articles/8040695057821>).
You can add GROUP BY and SUM operations to avoid listing every individual duration and time span.
Note. This example changed in system update 2.12.0. The outdated model still works but is not recommended for new integrations. The old model example can be found [here](<https://support.nepton.com/hc/en-gb/articles/8405862536349>).
[code]
    SELECT
      *
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'OnCall'
[/code]
### Start-up and termination work
[code]
    SELECT
      *
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'StartupWork'
[/code]
[code]
    SELECT
      *
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'TerminationWork'
[/code]
## Other examples
The following examples include cases that address unique situations. These can be customized based on client-specific needs.
### Select the working hours in such a way that data is generated for different cost centers depending on the day the data is created
In the WHERE section, the cost center determines which individuals' data is extracted
  * On the 6th, extract employees from cost center 10.
  * On the 14th, extract employees from cost center 20.


[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'BasicTime'
      AND
      CASE --in here define the list of day numbers and the corresponding UserCostGroup we wish to pick 
        WHEN strftime('%d', 'now') = '06' THEN UserCostGroup = '10' 
        WHEN strftime('%d','now') = '14' THEN UserCostGroup = '20'
      END
    GROUP BY
      SalaryRenderingDate,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
[/code]
### Select the accrual value on the last day of the month
Calculation date must be the last day of the month. Only then is the balance value extracted.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount
    FROM
      UserSalaryData
    WHERE 
      CompensationType = 'Accrual'
      AND AccrualType = 'Balance'
      AND SalaryRenderingDate = date(salaryrenderingDate, 'start of month', '+1 month', '-1 day') -- this rule calculates the last day of the month
    GROUP BY
     SalaryRenderingDate
[/code]
### Select the groups of people to be included in the data
Extract employee groups: A100, B100, C100, D100.
[code]
    SELECT ...,
    IFNULL(
      (SELECT
         uid.Value
       FROM
         UserInfoData uid
       WHERE
         uid.InfoTypeName = 'UserGroupCode_SDSQL' AND
         datetime(UserSalaryData.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo
        LIMIT 1), '') AS _UserGroupCode,
    FROM
      UserSalaryData
    WHERE
      _UserGroupCode IN ('A100', 'B100', 'C100', 'D100')
[/code]
### The selected data represents the number of days an individual has worked regular hours or overtime
[code]
    SELECT
      *,
      COUNT(DISTINCT(SalaryRenderingDate)) As OverrideAmount,
      'J' AS OverrideUnitType -- siirretään määrä päivinä
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('BasicTime', 'AdditionalWork', 'OvertimeDaily50', 'OvertimeDaily100',
                           'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50', 'OvertimeSunday100')
      AND BasePartTarget IN ('salary','bank','balance','flexiblehours')
      AND ActivityTypeCategoryId = 1
    GROUP BY
      UserId
    HAVING
      OverrideAmount > 0
[/code]
### Data is selected so that the project code is determined based on the work supplement number
[code]
    SELECT
      *,
      SUM(amount) AS OverrideAmount,
      CASE 
        WHEN WorkIncrementNumber = 10 THEN '5000'
        WHEN WorkIncrementNumber = 30 THEN '6000'
        WHEN WorkIncrementNumber = 50 THEN '7000'
        ELSE 0
      END AS OverrideProjectCode1
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'workincrement'
[/code]
### Select data with the project external identifier as project code
[code]
    SELECT
      *,
      SUM(amount) AS OverrideAmount,
      ProjectExternalIdentifier1 AS OverrideProjectCode1
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'BasicTime'
[/code]
### Select 'balance change' events and transfer the absolute value of the change as the value
[code]
    SELECT
      *,
      ABS(amount) AS OverrideAmount
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 13
[/code]
### Select Travel invoices (other supplements are also extracted, unless the WorkIncrementType rule is added, see below)
[code]
    SELECT 
      *, 
      SUM(amount) AS OverrideAmount, 
      WorkIncrementCode AS OverrideSalaryCode -- Use the salary code from the Työlisät settings
    FROM 
      UserSalaryData 
    WHERE 
      CompensationType = 'WorkIncrement' 
      AND WorkIncrementCode IS NOT NULL -- Export all supplements unless they have been explicitly set not to be exported 
      AND WorkIncrementType = ??? -- If you ONLY want travel invoice supplements you can specify the types you wish here
    GROUP BY 
      SalaryRenderingDate, 
      Workincrementcode, 
      UnitType -- Ensures that if the supplement type changes, the old and new values aren't summed together
    
    
[/code]
### Select Accruals
[code]
    SELECT
      *,
      Amount AS OverrideAmount
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'Accrual'
      AND AccrualType = 'balance' -- Only the balance accrual is extracted
[/code]
### Select the cut amount of the Balance accrual
This rule extracts the trimmed amount from the employee's balance if it exceeds the maximum allowed.
[code]
    SELECT
      usd.*,
      usd.amount + COALESCE(usd2.sumAmount, 0) AS OverrideAmount
    FROM
    UserSalaryData usd
    LEFT JOIN
      (SELECT 
         salaryRenderingDate, 
         COALESCE(SUM(
           CASE
             WHEN compensationType = 'BasicTime' AND basePartTarget = 'balance' AND overtimeTarget = 'uncompensated' THEN - amount
             ELSE amount
           END), 0) AS SumAmount 
    FROM 
      UserSalaryData 
    WHERE 
      compensationType = 'BasicTime' 
      AND isTimeBorrowedFromBalance = 'Y' 
      AND (ActivityTypeId IS NULL 
         OR
          (compensationType = 'BasicTime' 
           AND basePartTarget = 'balance' 
           AND overtimeTarget = 'uncompensated')) 
    GROUP BY 
      salaryRenderingDate) usd2 ON usd.salaryRenderingDate = usd2.salaryRenderingDate 
    WHERE 
      usd.compensationType = 'AccrualChange' 
      AND usd.accrualType = 'Balance' 
    GROUP BY 
      usd.accrualType
[/code]
### Select Holiday pay leave also from Saturdays, which don't have work obligation
This rule exceptionally extracts marked working time (‘MarkedTime’) on specified days. An exception has also been added to the rule so that Sundays are excluded—only Monday through Saturday will be included in the dataset.
[code]
    SELECT 
      *, 
      COUNT(DISTINCT(SalaryRenderingDate)) AS OverrideAmount, 
      'J' AS OverrideUnitType 
    FROM 
      UserSalaryData 
    WHERE 
      ActivityTypeCode = 164 --Lomarahavapaa-tapahtumatyypin koodi
      AND CompensationType = 'MarkedTime' 
      AND Weekday(StartDateTime) != 6  
    GROUP BY 
      UserId, 
      ProjectCode1,
      SalaryRenderingDate
[/code]
### Select workdays
Extract the total amount of paydays where compensated time is calculated. Salary code is ‘1’ if the processed day is in the same month as the last day of the period and otherwise ‘2’.
[code]
    SELECT
      *,
      (CASE
         WHEN
           (SELECT
              strftime('%m', MAX(salaryrenderingdate))
            FROM
              UserSalaryData) = strftime('%m', salaryrenderingdate) THEN 1
         ELSE 2
       END) AS OverrideSalaryCode,
      COUNT(DISTINCT(SalaryRenderingDate)) As OverrideAmount,
      'J' AS OverrideUnitType
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('BasicTime', 'AdditionalWork', 'OvertimeDaily50','OvertimeDaily100',
                           'OvertimeWeekly50', 'OvertimeWeekly100')
      AND BasePartTarget IN ('salary','bank','balance','flexiblehours')
      AND EmployeeSalaryType = 'hourly'
    GROUP BY
      OverrideSalaryCode
[/code]
### Select travel information from Travel invoices
The character `char(10)` used in the extract indicates a line feed (LF) line break.
[code]
    SELECT
      ued.*, 
      utetd.StartDateTime AS OverrideStartDatetime, 
      utetd.EndDateTime AS OverrideEndDatetime, 
      utetd.StartLocation || ' - ' || utetd.EndLocation || char(10) || utetd.ReasonForTrip AS OverrideComment 
    FROM
      UserEventData ued 
    JOIN UserTravelExpenseTripData utetd ON ued.ActivityId = utetd.ActivityId
    ORDER BY
      ued.StartDateTime,
      utetd.TripNumber
[/code]
