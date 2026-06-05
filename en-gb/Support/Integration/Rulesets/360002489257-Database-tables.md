---
id: 360002489257
title: Database tables
url: https://support.nepton.com/hc/en-gb/articles/360002489257-Database-tables
locale: en-gb
category: Support
category_id: 360000446658
section: Rulesets
section_id: 360000827378
section_path:
- Integration
- Rulesets
labels:
- NEPTONNEEDSREVIEW
- palkkalajimääritys
- poimintasäännöt
- sääntöjoukot
- palkkasääntö
- tietotaulu
- tietokantataulu
- database table
- content of database
promoted: false
updated_at: '2026-06-01T14:48:24Z'
edited_at: '2026-06-01T14:48:24Z'
---

# Database tables

A ruleset defines the content to be extracted into the transferable dataset. This article describes the contents of the database tables that can be extracted using a ruleset.
General information about rulesets can be read [here](<https://support.nepton.com/hc/en-gb/articles/360002492278>).
The basic principles behind ruleset data extraction can be found [here](<https://support.nepton.com/hc/en-gb/articles/21077132021149>).
A comprehensive list of integration rule templates is available [here](<https://support.nepton.com/hc/en-gb/sections/360000827378-Rulesets>).
### The content of the database tables
Below are descriptions of the contents of the database tables that can be extracted for transfers.
Database table name | Description | Supported in setting exceptions  
---|---|---  
**UserSalaryData** |  The table contains the interpreted work time data for a person, according to the valid rules. When extracting interpreted events, it is advisable to keep the extraction period as short as possible to avoid long data retrieval times. We recommend a maximum extraction period of two months forward and backward. | No  
**UserEventData** |  The table contains events recorded for a person as they were logged. When extracting recorded events, the extraction period can be longer than when extracting interpreted events. We recommend a maximum extraction period of one year forward and backward. |  Yes, excluding the settings that define the timing of the workday. UserCostGroup information is not available. The data can be found in the UserInfoData table.  
**UserEventHistoryData** | The table contains events recorded for a person as they were logged, including earlier versions of edited events, deleted events, and events edited within the specified time period. Different versions of events may also fall outside the given timeframe if any version's edit or event time occurs within the specified range. |  Yes, excluding the settings that define the timing of the workday. UserCostGroup information is not available. The data can be found in the UserInfoData table.  
**UserEventProjectData** | Each project linked to an event has a row in this table containing the project identifier and notes. | Yes  
**UserTravelExpenseTripData** | The table contains data on the trips logged on the person's travel invoices. | No  
**UserEventExternalIdentifierData** | The table contains data on external identifiers for events. | Yes, excluding the settings that define the timing of the workday.  
**UserData** | The table contains the person's current personal and employment information. It can be joined with queries to the _UserSalaryData_ and _UserEventData_ tables. | Yes  
**UserInfoData** |  The table contains personal and employment information with history values included. It can be joined with queries to the _UserSalaryData_ and _UserEventData_ tables. Organization-specific additional data fields are also available by default. A detailed list of available data can be found in 8 - UserInfoData. |  Yes, excluding sensitive information:
  * RFIDTagNumber
  * SocialSecurityNumber

  
**UserGroupData**  
| The table contains information about person groups for individuals included in the dataset. All parent person groups of selected groups are found in the table. | Yes  
**ProjectData** | Contains complete project data for projects used by the user during the reporting period. | Yes  
**PaymentGroupPeriodData** | Contains payment period data for payment groups assigned to individuals in the dataset. | Yes  
**PlanningYearTargetData** | Contains data for year target planning in work shift planning. | No  
**PlanningYearTargetBreakdownData** | Contains data for formation breakdown of planning year target. | No  
**UserExternalIdentifier** | Contains data of person's external identifiers. With userId-field this table can be joined to other tables such as UserEventData or UserSalary data. This table is useful for integrations that both import users to Nepton and receive person releated work time data from Nepton. | Yes  
### UserSalaryData
Column name | Type | Description  
---|---|---  
**CompensationType** | enum |  Available only for data from the SalaryData table.
  * "BasicTime" - Performed regular working hours and hour-to-hour compensated time
  * "ReducedRateTime" - Time with reduced compensation. Certain absences and sick leaves may earn reduced pay
  * "UnpaidBasicTime" - Basic working time not compensated. E.g. unpaid absences only generate time up to the work obligation.
  * "AdditionalWork" - Additional work earned after regular working hours (length of workday/week) but before the maximum length of the day/week.
  * "OvertimeDaily50" - 50% daily overtime.
  * "OvertimeDaily100" - 100% daily overtime.
  * "OvertimeWeekly50" - 50% weekly overtime.
  * "OvertimeWeekly100" - 100% weekly overtime.
  * "OvertimeSunday50" - 50% Sunday overtime, earned based on Sunday overtime settings.
  * "OvertimeSunday100" - 100% Sunday overtime, earned based on Sunday overtime settings
  * "OvertimeBaseFixed" - Overtime 1, used in some Nordic collective agreements (TES)
  * "OvertimeExtraFixed" - Overtime 2, used in some Nordic collective agreements
  * "TESOvertime50" - TES-based 50% overtime used in some agreements, earned separately from weekly overtime. Only created if setting 'TES overtime earned separately from weekly overtime' is enabled; otherwise, TES-based overtime is regular overtime with IsTesOvertime = "Y".
  * "TESOvertime100" - TES-based 100% overtime used in some agreements, earned separately from weekly overtime. Same conditions as above.
  * "LevellingPeriodAdditional" - Additional work earned at the end of the leveling period.
  * "LevellingPeriodOvertime50" - 50% overtime earned at the end of the leveling period.
  * "LevellingPeriodOvertime100" - 100% overtime earned at the end of the leveling period.
  * "LevellingPeriodUnderTarget" - If less work is done than the target for the leveling period, includes the under-target time.
  * "UnpaidOvertime" - Overtime that is marked _Do not compensate_ and thus not paid.
  * "WorkRise" - Work rise earned for work during certain times, e.g. evening or Sunday compensation
  * "WorkRisePercentagePart" - Calculated percentage or minute-based work rise compensation per hour
  * "WorkIncrement" - Manually recorded work supplement, e.g. manager supplement.
  * "WorkIncrementPercentagePart" - Calculated percentage of work supplement contributing to an accrual.
  * "PublicHoliday" - Public holiday. Compensation depends on how much it shortens the workweek.
  * "YearLeave" - Annual leave
  * "WeeklyRestTime" - Weekly rest period. _Note: when transferring weekly rest compensation to another system using extraction rules, this setting can be defined using the "basePartTarget" field._
  * "ProjectOverAllocation" - Time recorded to a project that exceeds the actual event duration.
  * "StartupWork" - Startup work compensated as regular working time
  * "StartupWorkAdditionalWork" - Startup work compensated as additional work
  * "StartupWorkOvertime50" - Startup work compensated as 50% overtime
  * "StartupWorkOvertime100" - Startup work compensated as 100% overtime
  * "UnpaidStartupWork" - Time marked as startup work that is not compensated.
  * "TerminationWork" - Termination work compensated as regular working time
  * "TerminationWorkAdditionalWork" - Termination work compensated as additional work
  * "TerminationWorkOvertime50" - Termination work compensated as 50% overtime
  * "TerminationWorkOvertime100" - Termination work compensated as 100% overtime
  * "UnpaidTerminationWork" - Time marked as termination work that is not compensated
  * "Accrual" - Ongoing/cumulative value for a specific accrual, e.g. balance or bank
  * "AccrualChange" - Change in accrual value from the previous day
  * "MarkedTime" - Time recorded for an event. EventStartTime and EventEndTime fields show the timestamps. Not generated for the following:
    * Public holiday events
    * Accrual reset and change events (e.g. balance or annual leave)
  * "Lunch" - Lunch break. Indicates how the break is algorithmically placed into the workday
  * "OnCall" - Includes actual on-call time. By default, all events recorded over the on-call period are excluded from it, but settings can define exceptions for certain event types
  * "PayOverAccrualLimit" - Includes hours automatically trimmed from accrual when the behavior for exceeding the positive accrual limit is _Transfer excess to salary_
  * "UnpaidOverMinAccrualLimit" - Includes hours automatically trimmed from accrual when the behavior for exceeding the negative accrual limit is _Transfer excess to salary_

  
**AccrualType** | enum|null | Available for use with accruals and accrual changes  
**Amount** | decimal | Amount. Value in seconds for all non-integer numbers. For integers, the value is represented as a whole number (see UnitType).  
**UnitType** | enum|null | 
  * "U" - integer
  * "D" - decimal
  * "S" - seconds
  * "H" - hours
  * "J" - days
  * "C" - currency

  
**SalaryRenderingDate** | date | Date corresponding to the payment/shift. Format: _YYYY-MM-DD_.  
**PaymentDate** | date | Payment date. Format: _YYYY-MM-DD_.  
**StartDateTime** | datetime |  Start date and time when _salary data_ was earned (if available) Note: Long entries, such as sick leave, are distributed across calculation days. Format: _YYYY-MM-DD HH:MM:SS_ Time zone: User's local time zone  
**EndDateTime** | datetime |  End date and time when _salary data_ was earned (if available) Note: Long entries, such as sick leave, are distributed across calculation days. Format: _YYYY-MM-DD HH:MM:SS_ Time zone: User's local time zone  
**EventStartDateTime** | datetime |  Start date and time when the event related to interpreted working time is marked in the calendar (if available). Format: YYYY-MM-DD HH:MM:SS Time zone: User's local time zone  
**EventEndDateTime** | datetime |  End date and time when the event related to interpreted working time is marked in the calendar (if available) Format: YYYY-MM-DD HH:MM:SS Time zone: User's local time zone  
**CreatedDatetime** | datetime|null |  Date and time when the event related to this row was created. Format: YYYY-MM-DD HH:MM:SS Time zone: Finnish time zone  
**ModifiedDatetime** | datetime|null |  Date and time when the event related to the row was last modified. Format: YYYY-MM-DD HH:MM:SS Time zone: Finnish time zone For leveling period and weekly rest compensation, the latest modification time of an event from the final week of the period is used  
**ActivityId** | int|null |  Unique identifier of the event from the Events table. Useful if you want to group times from the same event (e.g., annual leave salary). ActivityId does not change when an event is modified. If ActivityId is negative, it means the event is generated based on settings (e.g., an assumed event or a shift from a work schedule). In this case, ActivityId may change.  
**ActivityTypeCode** | string|null | Event type code  
**WorkRiseNumber** | int|null | Work rise number defined in settings  
**WorkRiseSalaryCode** | string|null | Work rise salary code defined in work rise settings  
**WorkRisePercentageIncrease** | decimal(4,1)|null | Work rise percentage used to calculate duration for the "WorkRisePercentagePart" row  
**WorkRiseMinutesPerHourIncrease** | smallint|null | Work rise minute/hour increase used to calculate duration for the "WorkRisePercentagePart" row  
**WorkRisePayTarget** | string|null |  Target for work rise compensation. Supported options:
  * "salary" - Directed to salary
  * "annualbalance" - Directed to annual absence accrual
  * "balance" - Directed to balance
  * "bank" - Directed to bank
  * "flexiblehours" - Directed to flexible bank
  * "flexibleworkhours" - Directed to flexible work hours balance
  * "holidaypayleave" - Directed to holiday pay leave accrual
  * "levellingperiodhours" - Directed to levelling period hours accrual
  * "overtimebalance" - Directed to overtime balance
  * "savingsleave" - Directed to savings leave accrual
  * "weeklyrest" - Directed to weekly rest accrual
  * "worktimeshortenigleave" - Directed to work time shortening leave accrual

The target may also be selected from the base or increased portion of the event’s overtime target.  
**WorkIncrementName**  
| string|null | Supplement name  
**WorkIncrementNumber** | int|null | Supplement number/index in settings  
**WorkIncrementTripNumber** | int | Sequential number of the travel invoices trips to which the supplement is linked (if the supplement isn't linked to travel, the value is `null`).  
**WorkIncrementPercentageIncrease** | decimal(4,1)|null | Supplement percentage used to calculate duration on the "WorkIncrementPercentagePart" row.  
**WorkIncrementPercentageAccrualTarget** | string|null | Internal name of the accrual to which "WorkIncrementPercentagePart" is targeted.  
**WorkIncrementCode** | string|null | Supplement salary code, which can be set in the supplement settings (at the working community or setting group level).  
**WorkIncrementDate** | date|null | If the supplement has the date field enabled, the date will appear here (YYYY-MM-DD)  
Time zone: User's local time zone  
**WorkIncrementComment** | string|null | If the supplement has the comment field enabled, the comments will appear here  
**WorkIncrementType** | enum|null | 
  * "normal" - Normal supplement type for normal event types
  * "correction" - Supplements that only appear on Correction events
  * "cafe" - Supplements that only appear in terminal cafeteria mode
  * "expense" - Supplements that only as a travel invoice expense
  * "allowance" - Supplements that only appear as a travel invoice daily allowance
  * "tripReimbursement" - Supplements that only appear as a travel invoice trip/transportation reimbursement
  * null - not a supplement

  
**WorkRiseEarnedAtCompensationType** | enum|null | Filters work rises based on the compensation type by which they were earned. See the CompensationType list for supported values.  
**ProjectId1** | int|null |  The internal identifier of the first project attached to the event. This column repeats for each linked project, so the first project has number 1, the second has number 2, and so on. The column appears for linked project numbers 1–6.  
**EventProjectRowId1** | int|null |  System-internal identifier for the relationship between the event and the project. Can be joined in a query with: `UserSalaryData.EventProjectRowId1 = UserEventProjectData.Id` This column repeats for each linked project, appearing for project numbers 1–6  
**ProjectExternalIdentifier1** | string|null |  External identifier of the first project attached to the event. This column repeats for each linked project, appearing for project numbers 1–6.  
**ProjectCode1** | string|null |  Code of the first project attached to the event. This column repeats for each linked project, appearing for project numbers 1–6.  
**ProjectName1** | string|null |  Name of the first project attached to the event. This column repeats for each linked project, appearing for project numbers 1–6.  
**ProjectType1** | string|null |  Internal name for the type of the first attached project. Examples: "location", "project_work", "unit" This column repeats for each linked project, appearing for project numbers 1–6.  
**BasePartTarget** | string|null |  Work that exceeds the length of the workday is split between the BasePartTarget (base portion) and OvertimeTarget (overtime portion). BasePartTarget defines how the base portion is allocated. For example, when time is compensated hour-for-hour to balance, no increase portion is paid. The recorded time includes the following allocations: BasePartTarget = 'balance' and OvertimeTarget = 'uncompensated'. Supported values:
  * "salary" - Basepart allocated to salary
  * "balance" - Basepart allocated to balance
  * "bank" - Basepart allocated to bank
  * "overtimebalance" - Basepart allocated to overtime balance
  * "uncompensated" - Basepart is not compensated
  * "flexiblehours" - Basepart allocated to flexible bank

  
**OvertimeTarget** | string|null |  Work that exceeds the length of the workday is split between the BasePartTarget (base portion) and OvertimeTarget (overtime portion). OvertimeTarget defines how the overtime portion is allocated. If work is compensated as overtime, OvertimeTarget has a value other than NULL or "uncompensated". For instance, overtime compensated to bank would result in: BasePartTarget = 'bank' and OvertimeTarget = 'bank'. Supported values:
  * "salary" - Overtime-part allocated to salary
  * "balance" - Overtime-part allocated to balance
  * "bank" - Overtime-part allocated to bank
  * "overtimebalance" - Overtime-part allocated to overtime balance
  * "uncompensated" - Overtime portion not compensated
  * "flexiblehours" - Overtime-part allocated to flexible bank
  * NULL - No overtime portion (used when work is performed during regular hours)

  
**OvertimePercentage** | int|null | Event’s overtime percentage. If the setting “Fixed compensation for overtime” is enabled (e.g., calendar shows "Overtime 1/2"), then the value is null.  
**WorkRiseEarnedAtOvertimePercentage** |  | Overtime percentage from which the work rise was formed. If “Fixed compensation for overtime” is enabled, the value is null.  
**UserId** | int |  Service’s internal identifier for user. Not visible in the UI. Use other identifiers whenever possible.  
**ApprovedByUserId** | int|null |  UserId of the person who approved the event. For leveling period and weekly rest compensation, the last approver of the final week of the period is used.  
**UserCostGroup** | string | Person’s default cost center  
**EmployeeSalaryType** | enum | 
  * "hourly" - hourly wage
  * "monthly" - monthly salary

  
**EmployeeWorkContractActive** | enum |  Is the person employed on the specified date
  * "Y" - Yes
  * "N" - No

  
**EmployeeWorkContractStartDate** | date | Employment start date (null if empty). Format: YYYY-MM-DD  
**EmployeeWorkContractEndDate** | date | Employment end date (null if empty). Format: YYYY-MM-DD  
**Comment** | string | Comment, limited to 2000 characters  
**IsTimeBorrowedFromBalance** | enum |  If an employee with flexible work time is not working on a day when they have work obligation, hours are borrowed from the balance accrual.
  * "Y" - Yes
  * "N" - No

  
**IsTesOvertime** | enum |  Is it TES overtime?
  * "Y" - Yes
  * "N" - No

  
**IsEmergencyWork** | enum |  Is it emergency work?
  * "Y" - Yes
  * "N" - No

  
**IsApproved** | enum |  Is the event approved?
  * "Y" - Yes
  * "N" - No

  
**SickLeaveCompensationTypeId** | int |  Sick leave compensation
  * 1 = paid
  * 2 = unpaid
  * 3 = reduced salary

  
**SickLeaveTypeId** | int |  Sick leave reason
  * 1 = sick
  * 2 = child sick
  * 3 = accident at work
  * 4 = accident while commuting
  * 5 = accident in free time

  
**SickLeaveMedicalCertificateId** | int |  Medical certificate
  * 0 = not known
  * 1 = not received
  * 2 = received
  * 3 = permission from supervisor

  
**AbsenceCompensationTypeId** | int |  Absence compensation
  * 1 = paid
  * 2 = unpaid
  * 3 = reduced salary

  
**AbsenceTypeId** | int | Absence type identifier. (NULL if not defined). Appears in settings under _Work Hours → Absence Types_  
**EarnsVacationDays** | enum |  Does the event accrue annual leave days. Value comes from either annual leave settings or event-specific data.
  * "Y" - Yes
  * "N" - No

May also be `null` if not relevant to work time data.  
**FromRounding** | enum | 
  * "Y" = Time has been created due to rounding
  * "N" = Time has not been created due to rounding

  
**OverlapsUnderlyingActivityTypeIds** | string |  Comma-separated list of event type codes that overlap with clock-ins. These are intentionally configured to fall beneath another clock-in—e.g., on-call events. Must be handled in WHERE clauses like:
[code] 
    WHERE overlapsunderlyingactivitytypeids LIKE '%,33,%'
[/code]  
**ActivityTypeCategoryId** | int | Event type category, 1 = work, 2 = absence  
**AdjacencyGroupingId** | int |  Unique identifier for uninterrupted time periods interpreted as a single work cycle. Multiple events can be grouped in the same cycle if interpreted payroll doesn’t break. By grouping by this field, you can get paid blocks from long clock-ins, split by unpaid intervening days. Example: Absence from May 2–22, 2016
  * 2\. - 4.5.2016 - Absence Monday–Wednesday
  * 6.5.2016 - Absence on Friday (Ascension Day on May 5)
  * 9\. - 13.5.2016 - Absence Monday–Friday
  * 16\. - 20.5.2016 - Absence Monday–Friday

  
### UserEventData, UserEventHistoryData
Column name | Type | Description  
---|---|---  
**ActivityId** | int |  Unique identifier of the event from the Events table. Useful if you want to group times from the same event (e.g., annual leave salary). ActivityId does not change when an event is modified. If ActivityId is negative, it means the event is generated based on settings (e.g., an assumed event or a shift from a work schedule). In this case, ActivityId may change.  
**ActivityTypeCode** | string | Event type code  
**BasePartTarget** | string |  Work that exceeds the length of the workday is split between the BasePartTarget (base portion) and OvertimeTarget (overtime portion). BasePartTarget defines how the base portion is allocated. For example, when time is compensated hour-for-hour to balance, no increase portion is paid. The recorded time includes the following allocations: BasePartTarget = 'balance' and OvertimeTarget = 'uncompensated'. Supported values:
  * "salary" - Basepart allocated to salary
  * "balance" - Basepart allocated to balance
  * "bank" - Basepart allocated to bank
  * "overtimebalance" - Basepart allocated to overtime balance
  * "uncompensated" - Basepart is not compensated
  * "flexiblehours" - Basepart allocated to flexible bank

  
**OvertimeTarget** | string |  Work that exceeds the length of the workday is split between the BasePartTarget (base portion) and OvertimeTarget (overtime portion). OvertimeTarget defines how the overtime portion is allocated. If work is compensated as overtime, OvertimeTarget has a value other than NULL or "uncompensated". For instance, overtime compensated to bank would result in: BasePartTarget = 'bank' and OvertimeTarget = 'bank'. Supported values:
  * "salary" - Overtime-part allocated to salary
  * "balance" - Overtime-part allocated to balance
  * "bank" - Overtime-part allocated to bank
  * "overtimebalance" - Overtime-part allocated to overtime balance
  * "uncompensated" - Overtime portion not compensated
  * "flexiblehours" - Overtime-part allocated to flexible bank
  * NULL - No overtime portion (used when work is performed during regular hours)

  
**AccrualType** | enum | Available for use with accrual reset and change events.  
**Amount** | decimal | Value in seconds  
**UnitType** | enum | 
  * "U" - integer
  * "D" - decimal
  * "S" - seconds
  * "H" - hours
  * "J" - days
  * "C" - currency
  * 
  
**StartDatetime** | datetime |  Date and time when the event starts. Format: YYYY-MM-DD HH:MM:SS Time zone: User's local time zone  
**EndDatetime** | datetime |  Date and time when the event ends. Format: YYYY-MM-DD HH:MM:SS Time zone: User's local time zone  
**CreatedDatetime** | datetime |  Date and time when the event was created. Format: YYYY-MM-DD HH:MM:SS Time zone: Finnish time zone  
**ModifiedDatetime** | datetime |  Date and time when the event was last modified. Note! In the UserEventHistoryData table, if the event is a previous version of a modified event, ModifiedDatetime indicates the time when that particular version was created. Format: YYYY-MM-DD HH:MM:SS  
Time zone: Finnish time zone  
**ProjectId1** | int | The internal identifier of the first project attached to the event.  
**ProjectCode1** | string | Code of the first project attached to the event.  
**ProjectExternalIdentifier1** | string | External identifier of the first project attached to the event.  
**ProjectName1** | string | Name of the first project attached to the event.  
**ProjectType1** | string | Internal name for the type of the first attached project. Examples: "location", "project_work", "unit".  
**UserId** | int | Service’s internal identifier for user. Not visible in the UI. Use other identifiers whenever possible.  
**ApprovedByUserId** | int | UserId of the person who approved the event.  
**ApprovedByFirstname** | string | First name of the person who approved the event.  
**ApprovedByLastname** | string | Last name of the person who approved the event.  
**ApprovedByPersonnelNumber** | string | Employee number of the person who approved the event.  
**ApprovedByNeptonGUID** | string | Nepton Id of the person who approved the event.  
**UserCostGroup** | string | Person’s default cost center  
**EmployeeSalaryType** | enum |  Person's salary type
  * "hourly" - hourly wage
  * "monthly" - monthly salary

  
**EmployeeWorkContractActive** | enum |  Is the person employed on the specified date
  * "Y" - Yes
  * "N" - No

  
**EmployeeWorkContractStartDate** | date | Employment start date (null if empty). Format: YYYY-MM-DD  
**EmployeeWorkContractEndDate** | date | Employment end date (null if empty). Format: YYYY-MM-DD  
**Comment** | string | Comment, limited to 2000 characters  
**IsApproved** | enum |  Is the event approved?
  * "Y" - Yes
  * "N" - No

  
**IsRequestType** | enum |  Does the event type require prior approval from a supervisor?
  * "Y" - Yes
  * "N" - No

  
**IsEmergencyWork** | enum |  Is it emergency work?
  * "Y" Yes
  * "N" No

  
**SickLeaveCompensationTypeId** | int |  Sick leave compensation
  * 1 = paid
  * 2 = unpaid
  * 3 = reduced salary

  
**SickLeaveTypeId** | int |  Sick leave reason
  * 1 = sick
  * 2 = child sick
  * 3 = accident at work
  * 4 = accident while commuting
  * 5 = accident in free time

  
**SickLeaveMedicalCertificateId** | int |  Medical certificate
  * 0 = not known
  * 1 = not received
  * 2 = received
  * 3 = permission from supervisor

  
**AbsenceCompensationTypeId** | int |  Absence compensation
  * 1 = paid
  * 2 = unpaid
  * 3 = reduced salary

  
**AbsenceTypeId** | int | Absence type identifier. (NULL if not defined). Appears in settings under _Work Hours → Absence Types_  
**EarnsVacationDays** | enum |  Does the event accrue annual leave days. Value comes from either annual leave settings or event-specific data.
  * "Y" - Yes
  * "N" - No

  
**TravelBeginDateTime** | datetime |  Trip start date.  
Format: YYYY-MM-DD HH:MM:SS Time zone: User's default time zone  
**TravelEndDateTime** | datetime |  Trip end date. Format: YYYY-MM-DD HH:MM:SS Time zone: User's default time zone  
**IsActive** | string |  Only used in the UserEventHistoryData table.  

  * Y = Event is active
  * N = Event has been deleted or is a previous version of a modified event. If the event is a previous version of a modified one, it has an OriginalActivityId assigned.

  
**OriginalActivityId** | int|null |  Only used in the UserEventHistoryData table. Internal identifier of the modified event for which this event is the previous version. The event’s OriginalActivityId is the same as the ActivityId of its most recent version. If OriginalActivityId is null, the event is the most recent version.  
**TerminalId**  
| int|null |  The ID of the terminal the event was started with. If the event is started with a terminal but ended using another method - for example, via a mobile device - then the event’s terminalID is removed with the stop entry.  
**PlannedActivityTypeCode** | string|null | The event type code of the planned event.  
**PlannedActivityAlias** | string|null | Alias of the scheduled shift. Only available for shifts planned with a work schedule.  
**ShiftTypeDescription** | string|null | Additional information of the scheduled shift. Only available for shifts planned with a work schedule.  
### UserEventProjectData
Column name | Type | Description  
---|---|---  
**Id** | int | System's internal identifier for the relationship between the event and the project. Can be added to a query with the parameter UserSalaryData.eventprojectrowidX.  
**ActivityId** | int | System's internal identifier for the event to which the project entry is linked.  
**ProjectId** | int | System's internal identifier for the project data. Can be added using the query parameter ProjectData.id.  
**ProjectDurationMarked** | string | Duration saved to the project, either as a percentage or a time value, as the person marked it for the event. This is different from the calculated project duration (see UserSalaryData).  
**ApprovedByUserId** | int |  UserId of the person who approved the project entry. This should not be confused with the approval of the event itself - project-level approvals are often performed by project managers using the _Approve project hours_ tool.  
**InternalNotes** | string | Internal note for the project entry.  
**PublicNotes** | string | External note for the project entry.  
### UserTravelExpenseTripData
Column name | Type | Description  
---|---|---  
**ActivityId** | int | Unique identifier of the event from the Events table.  
**TripNumber** | int | Trip's sequential number for the event.  
**TransportationMethodId** | int |  Identifier for the method of transportation used. May include the following values:
  * 1 - car
  * 2 - airplane
  * 3 - ship
  * 4 - public transport
  * 5 - other

  
**StartDateTime** | datetime | Trip departure date and time. Format: YYYY-MM-DD HH:MM:SS  
**StartTimeZone** | string | Time zone of the trip departure time. For example: Europe/Helsinki  
**EndDateTime** | datetime | Trip end date and time. Format: YYYY-MM-DD HH:MM:SS  
**EndTimeZone** | string | Time zone of the trip end time. For example: Europe/Helsinki  
**StartLocation** | string | Departure location address  
**StartRegion** | string | Country of departure location  
**EndLocation** | string | Destination location address  
**EndRegion** | string | Country of destination location  
**ReasonForTrip** | string | Reason for trip  
### UserEventExternalIdentifierData
Column name | Type | Description  
---|---|---  
**ActivityId** | int | Unique identifier of the event from the Events table.  
**ExternalIdentifier** | string | External identifier of the event  
**IdentifierType** | string |  The type of the external identifier.  Currently, the only supported type is _External_.  
### UserData
Column name | Type | Description  
---|---|---  
**UserId** | int |  Service’s internal identifier for user. Not visible in the UI. Use other identifiers whenever possible.  
**UserIntegrationId** | string |  Person's unique identifier for integrations Formed according to the selected integration. It may be one of the following:
  * Identifier set for a specific integration
  * Employee number
  * Personal identity code

  
**FirstName** | string | Person’s first name  
**LastName** | string | Person’s last name  
**DefaultProjectId1** | int | Internal identifier for the person's default project  
**DefaultProjectCode1** | string | Code of the person’s default project  
**DefaultProjectType1** | string | Internal name of the default project’s type for the person. For example: “location”, “project_work”, or “unit”  
**DefaultCostGroup** | string | Person’s cost group  
**UserGroupCode** | string | Person’s person group code  
**RootGroupCode** | string | Root-level person group code to which the person’s person group belongs  
**ContractType** | string | Type of contract: "monthly" (Monthly salary) or "hourly" (Hourly wage)  
### UserInfoData
Column name | Type | Description  
---|---|---  
**UserId** | int |  Service’s internal identifier for user. Not visible in the UI. Use other identifiers whenever possible.  
**InfoTypeName** | string |  Identifier for personnel data. The table contains additional data fields created for the person. Value may be, for example:
  * AdministrativeAdditionalInfo
  * AdditionalReportingInfo
  * BIC
  * City
  * DefaultCostGroupCode
  * DefaultProjectId
  * DefaultProjectCode_SDSQL
  * DefaultProjectName_SDSQL
  * Email
  * EventsLockedDate
  * FinnishTaxNumber
  * Firstname
  * HolidayScheduleGroupCode_SDSQL
  * HolidayScheduleName_SDSQL
  * IBAN
  * IntegrationIdAastra
  * IntegrationIdDLSoftware
  * IntegrationIdEmce
  * IntegrationIdFivaldi
  * IntegrationIdHeeros
  * IntegrationIdHogia
  * IntegrationIdIFS
  * IntegrationIdKieku
  * IntegrationIdLessor5
  * IntegrationIdLiksa
  * IntegrationIdMepco
  * IntegrationIdOscar
  * IntegrationIdPersonecF
  * IntegrationIdPersonecW
  * IntegrationIdProCountor
  * IntegrationIdScala
  * IntegrationIdSedab
  * IntegrationIdSonet
  * IntegrationIdTikon
  * IntegrationIdVisma
  * IntegrationIdElisaRing
  * IsSalaryAdvanceAllowed
  * JobTitle
  * Language
  * LastWorkingContractBeginDate
  * LastWorkingContractEndDate
  * LastWorkingContractEndReason
  * LastWorkingContractHourlyWage
  * LastWorkingContractWeeklyHours
  * MicrosoftAxHourlyCost
  * NextOfKinName
  * NextOfKinTel
  * PersonnelNumber
  * NeptonPaymentGroupIdentifier
  * NeptonPaymentGroupCode_SDSQL
  * NeptonPaymentGroupId_SDSQL
  * NeptonPaymentGroupName_SDSQL
  * Postcode
  * PhoneNumber
  * PrimarySupervisor_SDSQL
  * PrimaryUnit_SDSQL
  * RFIDTagNumber
  * Role
  * RootUserGroupCode_SDSQL
  * RootUserGroupId_SDSQL
  * RootUserGroupName_SDSQL
  * SecondarySupervisor_SDSQL, can have multiple rows
  * SecondaryUnit_SDSQL, can have multiple rows
  * SettingGroupCode_SDSQL
  * SettingGroupId_SDSQL
  * SettingGroupName_SDSQL
  * SocialSecurityNumber
  * StreetAddress
  * Surname
  * TrialPeriodEndDate
  * UserGroupCode_SDSQL
  * UserGroupId_SDSQL
  * UserGroupName_SDSQL
  * Username
  * WebPageURL
  * WorkArea
  * WorkDayLength_SDSQL, can have multiple rows, value is in seconds
  * WorkWeekLength_SDSQL, can have multiple rows, value is in seconds
  * WorkTimePercentage_SDSQL, can have multiple rows, defaults to 100.00
  * WorkScheduleGroupCode_SDSQL
  * WorkScheduleName_SDSQL
  * WorkTimeRoleId_SDSQL
  * WorkTimeRoleName_SDSQL

Things to note: Work day length and work week length are affected by the work time percentage.  
The validities for work day length, work week length and worktime percentage, are not strictly correct. The setting may be valid outside of the period, but it will still have both a validFrom and validTo date that falls within the selected period.  
**InfoTypeId** | int |  Internal identifier for the type of personal data. This data should not be used as an identifier for utilizing the information, as it may change.  
**ValidFrom** | datetime | Date and time from which the personal data is valid. If no start date is set for the personal data, the value is: 1970-01-01 00:00:00 Format: YYYY-MM-DD HH:MM:SS  
**ValidTo** | datetime | Date and time until which the personal data is valid. If no end date is set for the personal data, the value is: 2999-12-31 23:59:59 Format: YYYY-MM-DD HH:MM:SS  
**Value** | string |  Field value as a string. The data is presented based on the field type in the following format:
  * Boolean (checkbox) - True / False
  * Date - `YYYY-MM-DD`
  * Datetime - `YYYY-MM-DD HH:MM:SS`

  
### UserGroupData
Column name | Type | Description  
---|---|---  
**Id** | int | Person group's internal identifier  
**Name** | string | Person group's name  
**Code** | string | Person group's code  
**Description** | string | Person group's description  
**ParentId** | int|null | Internal ID of the parent group in Nepton. If the person group has no parent group, the value is null.  
**IsRoot** | enum |  Indicates whether the person group is a root-level group, meaning a group with no parent group.
  * `Y` \- Yes
  * `N` \- No

  
**Depth** | int |  A numerical value indicating how deep the person group is in the tree structure. For example:
  * `0` \- root level group
  * `1` \- subgroup of a root-level group
  * `2` \- subgroup of the previous level
  * etc.

  
### ProjectData
Column name | Type | Description  
---|---|---  
**Id** | int |  Internal ID of the project  
**ExternalId** | int |  External ID of the project. Read more about external identifiers [here](<https://support.nepton.com/hc/en-gb/articles/360006768998>).  
**Name** | string | Project name in the project details page  
**Code** | string | Project code in the project details page  
**Description** | string | Project description in the project details page  
**ParentId** | int|null |  Internal ID of the parent project in Nepton. If the project has no parent group, the value is `null`.  
**StartDate** | date | Project start date on the project details page. Format: `YYYY-MM-DD`  
**EndDate** | date |  Project end date on the project details page. Format: YYYY-MM-DD `YYYY-MM-DD`  
**TypeInternalName** | string |  Internal name of the project type. Read more about project types [here](<https://support.nepton.com/hc/en-gb/articles/360002562338>).  
**IsLeaf** | enum |  Is the project a so-called leaf node, meaning a project that has no subprojects:
  * `Y` \- Yes
  * `N` \- No

  
**IsRoot** | enum |  Is the project a root-level project, meaning a project that has no parent project
  * `Y` \- Yes
  * `N` \- No

  
**IsAssignedProject** | enum |  Is the project recorded for an event:
  * `Y` \- Yes
  * `N` \- No

The value is "yes" if the project is directly recorded for the event. The value is "no" if the project is a parent of the project recorded for the event.  
**Depth** | int |  A numerical value indicating how deep the project is in the tree structure. For example:
  * `0` \- root level project
  * `1` \- subproject of a root level project
  * `2` \- subproject of the previous level
  * etc.

  
### PaymentGroupPeriodData
Column name | Type | Description  
---|---|---  
**Id** | int | Nepton’s internal identifier for the payment group’s salary period  
**NeptonPaymentGroupPeriodIdentifier** | string | Nepton payment group’s salary period identifier  
**PaymentGroupId** | int | Nepton’s internal identifier of the payment group to which the salary period is related  
**NeptonPaymentGroupIdentifier** | string | Nepton payment group’s identifier to which the salary period is related  
**PaymentPeriodStartDate** | date | Start date of the payment group's salary period  
**PaymentPeriodEndDate** | date | End date of the payment group's salary period  
**PaymentDate** | date | Payment date of the payment group's salary period  
**ValueDate** | date | Accounting value date of the payment group's salary period  
### PlanningYearTargetData
Column name | Type | Description  
---|---|---  
**UserId** | int | Internal user ID  
**TargetMinutes** | integer | Period target in minutes  
**PublishedPlannedMinutes** | integer | Published planned minutes in the period  
**DraftedPlannedMinutes** | integer | Drafted planned minutes in the period  
**PeriodBeginDate** | date | Year target period begin date  
**PeriodEndDate** | date | Year target period end date  
### PlanningYearTargetBreakdownData
Column name | Type | Description  
---|---|---  
**UserId** | int | Internal user ID  
**CalculatedTargetInMinutes** | int | Calculated target in minutes for the year target period. The value is limited to 0 or greater.  
**ConfiguredTargetInMinutes** | int | Configured target in minutes for the year target period during the contribution period. This value is not calculated and is the value set in settings.  
**WorktimePercentage** | decimal | Worktime percentage during the contribution period.  
**TargetReductionFromEventsInMinutes** | decimal | The amount of minutes target is reduced by events during the contribution period.  
**ContributedMinutesToTarget** | decimal | The amount of minutes the contribution period contributes to the target in year target period.  
**ContributionBeginDate** | date | Contribution period begin date.  
**ContributionEndDate** | date | Contribution period end date.  
**YearTargetPeriodBeginDate** | date | Year target period begin date.  
**YearTargetPeriodEndDate** | date | Year target period end date.  
### UserExternalIdentifier
Column name | Type | Description  
---|---|---  
**UserId** | int | Person's unique identifier, that can be used to attach this table's information to other tables that contain userId.  
**ExternalIdentifier** | string | Person's external identifier. In a working community persons can not have the same external identifier.  
**FieldName** | string | Technical name for the external identifier field, which defines the type of the external identifier for the person. At the moment only supported value is 'ExternalIdentifier1'. When joining this table to others, FieldName should be used as a clause as in the future there may be support for new field names.
