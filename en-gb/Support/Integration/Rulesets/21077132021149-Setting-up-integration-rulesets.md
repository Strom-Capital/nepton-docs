---
id: 21077132021149
title: Setting up integration rulesets
url: https://support.nepton.com/hc/en-gb/articles/21077132021149-Setting-up-integration-rulesets
locale: en-gb
category: Support
category_id: 360000446658
section: Rulesets
section_id: 360000827378
section_path:
- Integration
- Rulesets
labels:
- poimintasääntöjen muodostaminen
- sääntöjoukkojen määrittely
promoted: false
updated_at: '2026-09-16T06:22:03Z'
edited_at: '2026-09-16T06:22:03Z'
---

# Setting up integration rulesets

Please note that creating and modifying integration rules requires a basic understanding of SQL.
The ruleset defines the content to be extracted into the material to be transferred. This article reviews the basic principles of extraction and the additional rules most commonly needed in rule sets. Other essential instructions related to creating extraction rules can be found via the following links:
    * [Rulesets in general](<https://support.nepton.com/hc/en-gb/articles/360002492278>)  
General information on the formats and methods for downloading material from the service using rule sets, as well as where the settings can be found in the service.


    * [The content of the database tables](<https://support.nepton.com/hc/en-gb/articles/360002489257>)  
Column descriptions of the database tables.  
  

    * Ruleset examples  
A comprehensive list of rule set extraction rule templates - for example, for [payroll interfaces](<https://support.nepton.com/hc/en-gb/articles/360008045337>), [absences](<https://support.nepton.com/hc/en-gb/articles/360013979998>), and [personnel data](<https://support.nepton.com/hc/en-gb/articles/360015612638>).  
  
Article templates can be used as-is, but the requirements of the target system must be taken into account - for example, in terms of data grouping and any system-specific data fields. Therefore, the templates do not work as-is in all cases. Ready-made templates available from our Support pages often need to be supplemented with the grouping and filtering rules which are specified in this article.


## About SQLite in general
The ruleset presents 100 rows for extraction rules. Each row includes the rule description, the applicable salary code, the integration rule itself, and the unit of measure (hours, pieces, decimals) by which the data is transferred to the dataset.
Integration rules are written in SQL expressions using SQLite syntax. The source data for the integration rules can be drawn from various database tables. When generating the dataset, each selected person is processed individually, and the table being extracted contains only data related to that specific person.
Integration rules follow the SQL structure:
[code]
    SELECT ... FROM <table name> WHERE ...
[/code]
SQL features such as JOIN and aggregate functions (SUM, COUNT, etc.) can also be used.
For more details on SQL syntax and functionality, refer to SQLite’s [official documentation](<https://www.sqlite.org/docs.html>).
In addition to standard SQLite functions, the service includes [helper functions](<https://support.nepton.com/hc/en-gb/articles/360009018778>) to simplify tasks like string handling beyond what SQLite natively offers.
## Using the ruleset for data transfer
The ruleset defines what will be extracted. Once created, data can be loaded in any format. If the chosen data format includes fields not specified in the extraction rule, those fields will either be transferred as default values or as empty depending on the format.
A ruleset at a top level setting group can be overridden by placing another rule in a subgroup. However, for clarity in setting groups, this is not recommended. A rule created at the top level can already exclude data extraction in a subgroup. Therefore, no exceptions are needed in subgroups within the environment and all rules can be managed in one unified list. For instance, if the formation of a specific payroll item should be prevented in a subgroup, an exclusion condition can be added to the top-level rule as shown in the example below. This way, all dataset creation rules are clearly visible in a single ruleset, without division into multiple setting group settings.
Example of a query targeting the UserSalaryData table where individuals belonging to the configuration group with the code "hourly wage contract workers” are excluded from the results.
[code]
    SELECT ...,
    IFNULL(
      (SELECT
         uid.Value
       FROM
         UserInfoData uid
       WHERE
         uid.InfoTypeName = 'SettingGroupCode_SDSQL'
         AND DATETIME(usd.SalaryRenderingDate) BETWEEN ui.ValidFrom AND ui.ValidTo
       LIMIT 1), '') AS _SettingGroupCode
    FROM
      UserSalaryData
    WHERE
      SettingGroupCode != 'hourly wage contract workers'
[/code]
## Grouping data - GROUP BY
The GROUP BY clause allows the data generated for a person to be grouped by various conditions. It aggregates rows where the specified grouping criteria are the same. For data integrations, the data is always generated per individual, so data from different users cannot be grouped together. The dataset is built user by user. For [custom report generation](<https://support.nepton.com/hc/en-gb/articles/19801354657309>), the data is processed as a whole, which allows grouping across multiple users and lets you define the sorting order.
Typically, data sent to payroll systems is grouped by the salary code created by the rule (OverrideSalaryCode), the day (SalaryRenderingDate), and possibly by projects (ProjectCode1 through ProjectCode6)
If you need to group the data by event types, you can use ActivityTypeCode.
If a detailed description of the event is important in the payroll system, then additional grouping can be done by the event notes (Comment).
## Filtering data
### Filtering with the WHERE Clause
If there's a need to exclude for example events or supplements that don't have a salary code assigned, you should include the following condition in the rule's WHERE clause:
[code]
    AND OverrideSalaryCode IS NOT NULL
[/code]
Additional filters can exclude unapproved events or differentiate between hourly and monthly salary types:
[code]
    AND IsApproved = 'Y'
    AND employeesalarytype = 'hourly'
    AND employeesalarytype = 'monthly'
[/code]
When the condition `IsApproved = 'Y'` is used, it specifically excludes unapproved events from the dataset. For example, time automatically borrowed from an accrual (without an event record) cannot be excluded with this condition, because such borrowed accrual time cannot be approved separately.
### Filtering with the HAVING Clause
The salary code may be defined directly in the integration rule or derived from supplement/work rise settings. You can use a HAVING clause to exclude salary type 0 from the dataset:
[code]
    HAVING
    OverrideSalaryCode != 0
[/code]
Setting the rule-based, supplement-based, or work rise -based salary code to zero ensures it won’t be included in the final dataset.
## Person's identifier used in data extraction
Each record automatically includes the person’s identifier, as defined in the integration-specific data description. This identifier can be replaced by extracting an alternative identifier as a column in the rule, e.g. 'AS OverridePersonnelNumber'.
## Amount in extraction
By default, the Amount field is expressed in seconds. To convert seconds to minutes:
[code]
    SELECT *, Amount / 60 AS OverrideAmount
[/code]
Note: Standardized integrations may interpret the amount differently (as seconds, minutes, or hours) depending on the receiving system.
To convert seconds to a `'HH:MM'` formatted string:
[code]
    SELECT
      *,
      CONCAT(PRINTF('%02d', Amount / 3600), ':', PRINTF('%02d', Amount % 3600 / 60)) AS OverrideAmount
[/code]
## Using Override Column Names
When transferring data, fields automatically inherit the values defined in the dataset format. Any field’s value can be overridden by extracting a column with command Override+<column name>.
For example, when transferring quantities (hours, units) across multiple records per day, they are often summed by day. To override the `Amount` field:
[code]
    SELECT *, SUM(Amount) AS OverrideAmount
[/code]
Similarly, you can attach custom data to the comment field with 'AS OverrideComment'. More details on field names can be found in integration-specific descriptions [here](<https://support.nepton.com/hc/en-gb/articles/360002494538>).
## Defining the processed period
The ruleset targets data within a specific date range. The range is defined either in [the scheduled task settings](<https://support.nepton.com/hc/en-gb/articles/360002492458>) or via the user interface. The integration rules target the time period being processed and return results for that time period.
You can use variables `:exportPeriodStart` and `:exportPeriodEnd` to choose the chosen period's first and last date for the exported data (`YYYY-MM-DD HH:MM:SS`). For only the date, you can use :exportPeriodStartDate and :exportPeriodEndDate variables.
Example clause for filtering data by :exportPeriodStart and :exportPeriodEnd:
[code]
    WHERE
      DATE(EventStartDateTime) BETWEEN :ExportPeriodStart AND :ExportPeriodEnd
[/code]
## Setting groups and their validity in extraction
If a setting group changes during the processing period, the group valid on the last day of the period is used. This is especially relevant when salary type codes are defined only in sub-group rules.
This behavior can be overridden by defining the salary code at the highest level of the rule set.
**Example:** Extract salary codes based on the setting group's code with additional filters. The filters in the WHERE-clause define that the data is basictime, from work type events, and only from monthly paid employees:
[code]
    SELECT
      *, 
      SUM(Amount) As OverrideAmount,
      CASE
        WHEN uid.Value = '12h_kp' THEN 105
        WHEN uid.value IN ('12h', '3-vuoro','28') THEN 5
        WHEN uid.value IN ('2-vuoro', 'Keskeytymätön 2-vuoro') THEN 6
        ELSE 1
      END AS OverrideSalaryCode
    FROM 
      UserSalaryData usd
    LEFT JOIN UserInfoData uid ON
      usd.UserId = uid.UserId
      AND InfoTypeName = 'SettingGroupCode_SDSQL'
      AND usd.SalaryRenderingDate BETWEEN DATE(uid.ValidFrom) AND DATE(uid.ValidTo)
    WHERE 
      CompensationType = 'BasicTime' 
      AND BasePartTarget = 'salary'
      AND OvertimeTarget IS NULL
      AND ActivityTypeCategoryId = 1 
      AND EmployeeSalaryType = 'monthly' 
    GROUP BY
      SalaryRenderingDate,
      ProjectCode1
[/code]
## Validity of integration rules and related issues
Just like configuration settings, extraction rules can have defined validity periods, allowing their behavior to be modified on specific dates. If a rule is defined at a setting group level, it can also change for a person if they are reassigned to a different setting group. The system handles cases where a rule is valid only for part of the selected time period or changes during that period.
![](https://support.nepton.com/hc/article_attachments/29047195137565)If the user is affected by such a situation (as illustrated above), the system will apply the first version of the rule from days 1 to 9, and the second version from day 10 onward. The output will include records generated by both versions of the rule. If either version involves grouping or combining rows (e.g., summing hours per person), combining outputs from both versions might produce undesired results. The system will log a warning message in such cases.
![](https://support.nepton.com/hc/article_attachments/29047195139613)
If the scenario above occurs, the system processes the user's working hours according to the rule, but only for days 1 to 9. The log will include a message describing the situation. Depending on the extraction rule and the integration used, the transfer file may not clearly indicate that data was extracted from only part of the selected period.
Sometimes it's necessary to prevent rule changes from occurring during a reporting period. Here's how to do that:
  * Define the ruleset at the working community level or at the top setting group level (the setting group that has all other setting groups as subgroups): When all integration rules are defined at the same level, changing setting groups will not change the rules used.
By using the UserInfo table, you can extract only the time entries when a person belonged to, for example, a particular salary group. Setting group filtering is also possible, though conditions can only be set for subgroups.
  * Schedule changes between reporting periods: If rule changes are required, use the validity tool to ensure the change takes place between reporting periods. For example, if data is transferred monthly, the rule change should be scheduled to take effect at the beginning of the month.


## Difference in time amounts between UserEventData and UserSalaryData tables
When an event is marked in the system, the recorded time is stored in the UserEventData table, and the processed time information is stored in the UserSalaryData table. Both tables have a field called MarkedTime, but their values may differ depending on whether the event was logged in real-time ("clocked") or not
For events marked in real time, the start and end times include seconds (e.g., start 08:02:57 and end 16:13:12). A corresponding non-real-time entry would be start 08:02:00 and end 16:13:00. The Amount field in UserEventData would be 08h10min15sec, while in UserSalaryData it would be 08h11min00sec—i.e., 45 seconds more. This rarely matters, but if data is queried from both tables, it may be necessary to unify the time amount regardless of the logging method.
Here’s an example to get the same time amount from both tables, regardless of how the event was recorded:
[code]
    CAST(strftime('%s', strftime('%Y-%m-%d %H:%M:00', EndDateTime)) AS INT)
    - CAST(strftime('%s', strftime('%Y-%m-%d %H:%M:00', StartDateTime)) AS INT)
[/code]
## Time and time zones
Start and end times for events and salary data are stored and retrieved "as recorded"—i.e., based on user intent. Note: the time zone used during recording may not be known unless specified in the service.
You can find examples in the article [Time, language and region](<https://support.nepton.com/hc/en-gb/articles/360003994357>).
It’s also important to know that the query engine uses SQLite, where date and time functions default to the UTC standard.
This means that if you use the keyword 'now' or CURRENT_TIMESTAMP in a query to get the current time, it may show as 2–3 hours behind your local time (assuming you're in Finland and depending on daylight savings).
For example, the following query only returns data on the 1st day of the month:
[code]
    SELECT * FROM UserEventData WHERE strftime('%d', 'now') = '01'
[/code]
Since the time zone isn’t specified, it uses UTC time, and this query won’t return results if run between 00:00 and 02:00 on the 1st (in Finland). To correct this with the service’s local time zone:
[code]
    SELECT * FROM UserEventData WHERE strftime('%d', 'now', 'localtime') = '01'
[/code]
For more on UTC and time zones in SQLite, see [SQLite’s official documentation](<https://www.sqlite.org/lang_datefunc.html>).
## Limitations
### Case sensitivity matters with non-ASCII characters
For example, when filtering by event type code such as YÖ, the second character (Ö) must be in the same case as it was set in the event type. The following expression works because the letter Ö is uppercase in the query. If lowercase, the query would fail:
[code]
    SELECT * FROM UserSalaryData
    
    WHERE CompensationType = 'BasicTime' AND ActivityTypeCode = 'YÖ'
[/code]
You can read more about ASCII characters and character sets in [Wikipedia's article](<https://en.wikipedia.org/wiki/ASCII>).
### New data types may be added later
Some database tables may receive new rows and data types during service updates. If your query filters based on a type, it's good practice to make sure it won’t unintentionally include future additions.
For example, the following clauses are at risk of selecting a later-added time interpretation:
[code]
    SELECT * FROM UserSalaryData WHERE CompensationType != 'BasicTime';
    
    SELECT * FROM UserSalaryData WHERE CompensationType NOT IN ('PublicHoliday', 'MarkedTime');
[/code]
