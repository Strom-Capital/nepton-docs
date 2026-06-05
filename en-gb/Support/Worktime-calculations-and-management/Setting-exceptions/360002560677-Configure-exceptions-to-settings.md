---
id: 360002560677
title: Configure exceptions to settings
url: https://support.nepton.com/hc/en-gb/articles/360002560677-Configure-exceptions-to-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Setting exceptions
section_id: 360000708398
section_path:
- Worktime calculations and management
- Setting exceptions
labels:
- sdsql
- pyhäkalenteri
- mayday
- sääntöeditori
- juhannus
- pääsiäissunnuntai
- poikkeusase
promoted: false
updated_at: '2026-04-20T07:39:51Z'
edited_at: '2026-04-20T07:39:51Z'
---

# Configure exceptions to settings

The setting [validity control](<https://support.nepton.com/hc/en-gb/articles/360002559358>) can be used to create exceptions on the settings that are used . A setting exception can be set by rule commands that are defined separately. Rule commands can be used for public holidays or freely in any day/days. This article describes rule commands in more detail with examples.
If exceptions are configured, they are checked first before the setting value without exceptions. 
  * A setting may have multiple exceptions and they are handled in order from top to bottom.
  * The first rule that matches is the one whose value is used.
  * These can be reordered by using the drag handle that appears on the left hand side when you hover over the row.
  * Every day is checked against the rule separately.


If a setting does not have a value and no setting exception is valid, the setting used by the service is fetched from parent. Read more about [hierarchy of calculation settings here](<https://support.nepton.com/hc/en-gb/articles/360002559178>). If only an exception is defined for a sub-setting group level, both this exception and any exception rules inherited from the higher level are valid in that setting group. The inheritance of an exception rule can be prevented by giving a different value to the same exception rule, or by giving a value to the main setting itself.
## Defining setting exceptions
Exception for a setting is defined with the [validity controls](<https://support.nepton.com/hc/en-gb/articles/360002559358>). Exception is added by clicking **Add** under **exceptions.**
  * The exceptional setting value is defined into the **Value** -field.
  * The rule command (see below for examples) that should match for the exception is defined in the **Rule** -field.
  * If the setting needs to be valid for only a certain time, the **Valid from and Valid to** -fields can be used to set up the start and end time of when the setting exception is valid. One example where this might be required is if the setting needs to be valid for a time period which is defined in a working contract.


In the example below, length of work day on Monday is 7,5 hours, except on epiphany it is 4 hours.
![](https://support.nepton.com/hc/article_attachments/35360048664861)
The most common rule commands, such as setting value exceptions based on dates, public holidays and event types, can be viewed and selected by clicking the magic wand icon next to the rule input. This will open up a selection panel as shown below.
![en-1.PNG](https://support.nepton.com/hc/article_attachments/4972479325597)
Each rule command that is added to a rule builds on the previous one. For example, if you select "[CHRISTMAS-DAY]" and "Monday", then it must be both Christmas day AND a Monday, for the setting exception to be used. If each rule command should be fulfilled to match the rule, the commands must be separated by space such as "[CHRISTMAS-DAY] Monday", which means rule is valid on a day that is Christmas day AND Monday. If one rule command should be fulfilled to match the rule, the commands must be separated by comma such as "[CHRISTMAS-DAY], Monday", which means rule is valid on a day that is Christmas day OR Monday.
Selecting certain rule commands will prompt you for more information, for example if you want to have a different setting value based on a particular event type being recorded on the day, then you might select the "[WORK-DAY-HAS-ANY-OF-EVENT-TYPES]" command and the tool will then ask which event types you wish to specify. Once you have selected the desired types, click "Ok" and the command will be added with the codes for the correct types e.g. "[WORK-DAY-HAS-ANY-OF-EVENT-TYPES|100|101|etc]"
Note: this does does not support SQL-based rules e.g. "FROM UserEventData WHERE..."
### Settings that do not support exceptions
Some settings do not support setting value exceptions at all or have limited support for them. If a setting does not support setting value exceptions at all, a warning is displayed in the setting validity control:
![](https://support.nepton.com/hc/article_attachments/35360037757213)
If a setting has limited support for setting value exceptions, a warning is displayed in the setting validity control:
![](https://support.nepton.com/hc/article_attachments/35360048668445)
## Date rule commands
Rule commands are defined in English but they behave by Finnish and some other public holidays. Available rule commands (in brackets) are:
  * `[ANY-PUBLIC-HOLIDAY]` \- Any day that is calculated as a public holiday, i.e. the public holiday is set to be calculated as a public holiday, regardless of whether it shortens work week length or not.
  * `[ANY-PUBLIC-HOLIDAY-IN|HOLIDAYNAME]` \- Any day that is calculated as a public holiday which is defined after the IN| - characters. Public holidays that are included are written by their names listed in this list without brackets and separated by | - sign. E.g. if a rule needs to be valid on ascension day and epiphany, the rule command will be set as [ANY-PUBLIC-HOLIDAY-IN|ASCENSION-DAY-GREGORIAN|EPIPHANY]
  * `[ANY-PUBLIC-HOLIDAY-EXCEPT|HOLIDAYNAME]` \- Any day that is calculated as a public holiday except holidays that are defined after the EXCEPT| - characters. Public holidays that are excluded are written by their names listed in this list without brackets and separated by | - sign. E.g. if a rule needs to be valid on ascension day and epiphany, the rule command will be set as [ANY-PUBLIC-HOLIDAY-EXCEPT|ASCENSION-DAY-GREGORIAN|EPIPHANY]
  * `[ALL-SAINTS-DAY]` \- All Saints Day
  * `[ANNIVERSARY-OF-THE-CORONATION-OF-KING-MINDAUGAS]` \- Anniversary of the Coronation of King Mindaugas (6.7.)
  * `[ARMISTICE-DAY]` \- Armistice Day (11.11.)
  * `[ASCENSION-DAY-GREGORIAN]` \- Ascension Day
  * `[ASSUMPTION-DAY]` \- Assumption Day (15.8.)
  * `[AUSTRIAN-NATIONAL-DAY]` \- Austrian National Day (26.10.)
  * `[BELGIAN-ALL-SAINTS-DAY]` \- All Saints Day in Belgium (1.11.)
  * `[BELGIAN-NATIONAL-DAY]` \- Belgian National Day (21.7.)
  * `[BOXING-DAY]` \- Boxing Day
  * `[CHRISTMAS-DAY]` \- Christmas Day
  * `[CHRISTMAS-EVE]` \- Christmas Eve
  * `[EASTER-JULIAN]` \- Easter Day according to Julian calendar. Orthodox (except Finnish) church uses the Julian calendar for easter day.
  * `[EASTER-MONDAY-GREGORIAN]` \- Easter Monday
  * `[EASTER-SUNDAY-GREGORIAN]` \- Easter Sunday
  * `[EPIPHANY]` \- Epiphany
  * `[ESTONIAN-INDEPENDENCE-DAY]` \- Estonian Independence Day (24.2.)
  * `[ESTONIAN-INDEPENDENCE-DAY-EVE]` \- Estonian Independence Day's Eve (23.2.)
  * `[ESTONIAN-INDEPENDENCE-RESTORATION-DAY]` \- Estonian Independence Restoration Day (20.8.)
  * `[ESTONIAN-ST-JOHNS-DAY-EVE]` \- Estonian St. John's Day's Eve (22.6.)
  * `[ESTONIAN-VICTORY-DAY]` \- Estonian Victory Day (23.6.)
  * `[FATHERS-DAY]` \- Fathers Day
  * `[FEAST-OF-CORPUS-CHRISTI]` \- Feast Of Corpus Christi (60 days after Easter)
  * `[GERMAN-ALL-SAINTS-DAY]` \- German All Saints Day (1.11.)
  * `[GOOD-FRIDAY-GREGORIAN]` \- Good Friday
  * `[GREAT-PRAYER-DAY]` \- Great Prayer Day in Denmark (fourth Saturday after Easter)
  * `[HOLY-SATURDAY-GREGORIAN]` \- Holy Saturday
  * `[INDEPENDENCE-DAY]` \- Finnish Independence Day
  * `[INDEPENDENCE-DAY-EVE]` \- Finnish Independence Day's Eve (5.12.)
  * `[LITHUANIAN-ALL-SAINTS-DAY]` \- Lithuanian All Saints Day (1.11.)
  * `[LITHUANIAN-FATHERS-DAY]` \- Lithuanian Fathers Day (first Sunday of June)
  * `[LITHUANIAN-INDEPENDENCE-RESTORATION-DAY]` \- Lithuanian Independence Restoration Day (11.3.)
  * `[LITHUANIAN-MOTHERS-DAY]` \- Lithuanian Mothers Day (first Sunday of May)
  * `[LITHUANIAN-RESTORATION-OF-THE-STATE-DAY]` \- Lithuanian Independence Day (16.2.)
  * `[MAUNDY-THURSDAY-GREGORIAN]` \- Maundy Thursday
  * `[MAY-DAY]` \- May Day
  * `[MAY-DAY-EVE]` \- May Day Eve
  * `[MIDSUMMERS-DAY]` \- Midsummer's Day
  * `[MIDSUMMERS-EVE]` \- Midsummer's Eve
  * `[MOTHERS-DAY]` \- Mothers Day
  * `[NEW-YEARS-DAY]` \- New Years Day
  * `[NEW-YEARS-EVE]` \- New Years Eve
  * `[NORWEGIAN-CONSTITUTION-DAY]` \- Norwegian Constitution Day (17.5.)
  * `[ST-JOHNS-DAY]` \- St. John's Day (24.6.)
  * `[ST-JOHNS-DAY-EVE]` \- St. John's Day's Eve (23.6.)
  * `[SWEDISH-NATIONAL-DAY]` \- Swedish National Day (6.6.)
  * `[WHIT-SUNDAY-GREGORIAN]` \- Whit Sunday
  * `[WHIT-MONDAY]` \- Whit Monday
  * `[WEEK-HAS-PUBLIC-HOLIDAYS|SHORTENS-WEEK]` \- Rule is valid for the whole week if some working day of the week has a public holiday that shortens work week. The work week start date set in settings is noted while reading this setting, so a work week can be for example from Wednesday to Tuesday, based on what is set.
  * `[WEEK-HAS-PUBLIC-HOLIDAYS|COMPENSATED]` \- Rule is valid for the whole week if some working day of the week has a public holiday that is compensated. The work week start date set in settings is noted while reading this setting, so a work week can be for example from Wednesday to Tuesday, based on what is set.
  * `[WEEK-HAS-PUBLIC-HOLIDAYS|SHOWN-AS-PUBLIC-HOLIDAY]` \- Rule is valid for the whole week if some day of the week has a public holiday. Public holiday is regarded as being on the week regardless of it shortening the work week or not, or being compensated or not. The work week start date set in settings is noted while reading this setting, so a work week can be for example from Wednesday to Tuesday, based on what is set.
  * `[LEVELLING-PERIOD-HAS-PUBLIC-HOLIDAYS|SHORTENS-WEEK]` \- Rule is valid for the whole levelling period if there is a public holiday that shortens work week.
  * `[LEVELLING-PERIOD-HAS-PUBLIC-HOLIDAYS|COMPENSATED]` \- Rule is valid for the whole levelling period if there is a public holiday that is compensated.
  * `[LEVELLING-PERIOD-HAS-PUBLIC-HOLIDAYS|SHOWN-AS-PUBLIC-HOLIDAY]` \- Rule is valid for the whole levelling period if there is a public holiday on any day of the levelling period. Public holiday is regarded as being in the levelling period regardless of it shortening the work week or not, or it being compensated or not.
  * `[EMPLOYMENT-LASTED-LESS-THAN-12-MONTHS-AT-END-OF-ANNUAL-HOLIDAY-YEAR]` \- The rule is valid when it is required that a person does not earn full annual leave days if their working contract has lasted less 12 months at the end of holiday earning period (31.3.). If person's working contract end date is not known, service will assume person's working contract to continue to the next holiday earning period.
    * If a person's working contract start date is 1.4. and there is no working contract end date, this setting exception will not do anything.
      * If in this example person's working contract end date is added for April or later after this setting exception has been created, calculations for the person need to be updated for the setting to be accounted for.
    * If person's working contract start date is in January previous year, and their working contract end date is empty, this setting exception will be valid from January to the beginning of next holiday earning period. In this case it is assumed that the person will work for the next holiday earning period earning the normal amount of annual holiday, i.e. this setting has no effect for the next holiday earning period).
      * If in this example person's working contract end date is later added for August, the persons holiday earnings are not correct from April to August. Calculations for the person need to be updated for the calculations work correctly respective to this setting.
  * `[ACCRUAL-EARNING-PERIOD-START-DATE|ACCRUALNAME]` \- Rule is valid on the earning period start date of the defined accrual. At the moment this rule supports the following accruals:
    * Levelling period hours
      * set as _[ACCRUAL-EARNING-PERIOD-START-DATE|levellingperiodhours]_
    * Flexible work hours balance
      * set as _[ACCRUAL-EARNING-PERIOD-START-DATE|flexibleworkhours]_
    * Rule can be used to target multiple accruals, e.g.
      * _[ACCRUAL-EARNING-PERIOD-START-DATE|flexibleworkhours|levellingperiodhours]_
  * `[ACCRUAL-EARNING-PERIOD-END-DATE|ACCRUALNAME]` \- Rule is valid on the earning period end date of the defined accrual. At the moment this rule supports the following accruals:
    * Levelling period hours
      * set as _[ACCRUAL-EARNING-PERIOD-END-DATE|levellingperiodhours]_
    * Flexible work hours balance
      * set as _[ACCRUAL-EARNING-PERIOD-END-DATE|flexibleworkhours]_
    * Rule can be used to target multiple accruals, e.g.
      * _[ACCRUAL-EARNING-PERIOD-END-DATE|flexibleworkhours|levellingperiodhours]_


If a setting exception is wanted for targeting all Finnish **public holidays on weekdays** , the following rule command can be used:
[ANY-PUBLIC-HOLIDAY-IN|EPIPHANY|GOOD-FRIDAY-GREGORIAN|EASTER-MONDAY-GREGORIAN|ASCENSION-DAY-GREGORIAN|MAY-DAY|MIDSUMMERS-EVE|INDEPENDENCE-DAY|CHRISTMAS-EVE|CHRISTMAS-DAY|BOXING-DAY|NEW-YEARS-DAY]
If a setting exception is wanted for targeting all Finnish **public holiday's eves** , the following rule command can be used:
[ANY-PUBLIC-HOLIDAY-IN|INDEPENDENCE-DAY-EVE|MAY-DAY-EVE|MAUNDY-THURSDAY-GREGORIAN|MIDSUMMERS-EVE|NEW-YEARS-EVE|CHRISTMAS-EVE], [EPIPHANY] - 1 day, [ASCENSION-DAY-GREGORIAN] - 1 day, [ALL-SAINTS-DAY] - 1 day
Please note that public holiday's eves must be defined as public holidays for the rule to work
If a setting exception is wanted for targeting all Finnish **public holidays** , the following rule command can be used:
[ANY-PUBLIC-HOLIDAY-IN|EPIPHANY|GOOD-FRIDAY-GREGORIAN|HOLY-SATURDAY-GREGORIAN|EASTER-SUNDAY-GREGORIAN|EASTER-MONDAY-GREGORIAN|ASCENSION-DAY-GREGORIAN|MAY-DAY|WHIT-SUNDAY-GREGORIAN|MOTHERS-DAY|MIDSUMMERS-EVE|MIDSUMMERS-DAY|ALL-SAINTS-DAY|FATHERS-DAY|INDEPENDENCE-DAY|CHRISTMAS-EVE|CHRISTMAS-DAY|BOXING-DAY|NEW-YEARS-DAY]
See also instructions about [public holiday management](<https://support.nepton.com/hc/en-gb/articles/360002558797>).
Aside from public holidays also the following commands are available:
  * `[YEAR]` \- Used to replace year in a date where it can mean any year
  * `[MONTH]` \- Used to replace month in a date where it can mean any month on given year
  * `[DAY]` \- Used to replace day in a date where it can mean any day on given month and year
  * `[YEAR-EPIPHANY-ON-WEEKEND]` \- Used to replace year in a date where Epiphany is on weekend `[YEAR-EPIPHANY-NOT-ON-WEEKEND]` \- Used to replace year in a date where Epiphany is not on weekend
  * `[YEAR-LEAP-YEAR]` \- Used to replace year in a date where the year is a leap year
  * `[YEAR-NOT-LEAP-YEAR]` \- Used to replace year in a date where the year is not a leap year
  * `[LAST-FRIDAY-IF-ON-WEEKEND]` \- Used as an addition for a date or public holiday rule. It matches the last friday of the date, if the day is on weekend.
  * `[NEXT-MONDAY-IF-ON-WEEKEND]` \- Used as an addition for a date or public holiday rule. It matches the next monday of the date, if the day is on weekend. 
  * `[ODD-WEEK-NUMBERS]` \- Used in checking if day is on a week which has an odd week number
  * `[EVEN-WEEK-NUMBERS]` \- Used in checking if day is on a week which has an even week number
  * `[WEEK-NUMBERS|1|2|5]` \- Used in checking if day is on a week with a certain week number. Week numbers to check are separated with a | character. In the example the rule matches on dates with week numbers 1, 2 or 5.


Setting exception can be set with the rule commands above or directly as a date format (dd.mm.yyyy). Rule can also have commands after them for defining the setting exception to be valid calculating days from a public holiday:
  * **+1 day** exception is valid one day after a public holiday (e.g. `[BOXING-DAY] +1 day`)
  * **-1 day** exception is valid one day before a public holiday (e.g. `[ASCENSION-DAY-GREGORIAN] -1 day`)
  * **+1 week** exception is valid one week (7 days) after a public holiday
  * **-1 week** exception is valid one week (7 days) before a public holiday
  * **next Saturday** exception is valid on the next saturday (e.g `[NEW-YEARS-EVE] next Saturday`). Rule works with any day name. Day name must be in english.
  * **previous Saturday** exception is valid on the previous saturday (e.g. `[MAY-DAY] previous Saturday`). Rule works with any day name. Day name must be in english.


Day-value can be any number depending on how many days forwards or backwards the setting needs to be defined.
These rule commands are useful in situations where for example the day preceeding Epiphany should have an exceptional rule such as workday length. In this case the rule would be set as `[EPIPHANY] -1 day`.
The setting exception can have the change to target some days of the week. E.g. an exception that is valid on the Christmas week can be defined with the following rule:
`23.12.[YEAR] monday this week,`  
`23.12.[YEAR] tuesday this week,`  
`23.12.[YEAR] wednesday this week,`  
`23.12.[YEAR] thursday this week, `  
`23.12.[YEAR] friday this week,`  
`23.12.[YEAR] saturday this week,`  
`23.12.[YEAR] sunday this week`
Settings regarding days can also be used with the rules `[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS]` and `[WORK-WEEK-HAS-PUBLIC-HOLIDAYS]`. Because the work week start date defined in the settings is taken accounted for, 'next' or 'this week' commands should not be used but use day names only. E.g. exceptions for each day in a week which has a public holiday could be defined like this:
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Monday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Tuesday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Wednesday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Thursday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Friday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Saturday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Sunday`
## Event type rule commands
These rule commands allow you to create setting exceptions based on the types of events on the day.
By clicking on the magic wand button next to each rule field, the tool can help guide you through setting the correct event type codes or categories.
Here is an explanation of the event type and category based rule commands.
  * `[WORK-DAY-HAS-ANY-OF-EVENT-TYPES|101|102]`
    * Matches the setting exception if the work day¹ has an event with the event type code of 101 **or** 102.
  * `[WORK-DAY-HAS-ALL-OF-EVENT-TYPES|101|102]`
    * Matches the setting exception if the work day¹ has an event with the event type codes of 101 **and** 102.
  * `[WORK-DAY-HAS-NONE-OF-EVENT-TYPES|101|102]`
    * Matches the setting exception if the work day¹ does not have any event with either code 101 **or** 102.
  * `[WORK-DAY-HAS-EVENT-TYPES-OTHER-THAN|101|102]`
    * Matches the setting exception if the work day¹ does have any event that does not have either code 101 **or** 102.
  * `[WORK-DAY-HAS-ANY-OF-ABSENCE-TYPES|1|2]`
    * Matches the setting exception if the work day¹ has an absence type event with the absence type code of 1 **or** 2.
  * `[WORK-DAY-HAS-ABSENCE-TYPES-OTHER-THAN|1|2]`
    * Matches the setting exception if the work day¹ does have an absence event that does not have either absence type with code 1 **or** 2.
  * `[WORK-DAY-HAS-ANY-OF-PLANNED-EVENT-TYPES|101|102]`
    * Matches the setting exception if the work day¹ has a planned work shift with planned event code being code 101 **or** 102.
  * `[WORK-DAY-SHIFT-TYPE-ADDITIONAL-INFO-CONTAINS-ANY|I1430-2230]`
    * Matches the setting exception if the work day¹ has a planned work shift that contains `I1430-2230` in the shift type additional information.
  * `[WORK-DAY-HAS-ANY-OF-PLANNED-EVENT-ALIASES|M|E]`
    * Matches the setting exception if the work day¹ has a planned work shift with alias M **or** E.
  * `[WORK-DAY-HAS-ANY-OF-EVENT-CATEGORIES|WORK|ABSENCE]`
    * Matches the setting exception if the work day¹ has events belonging to the category of "work" **or** "absence". The full list of categories are "WORK", "ABSENCE", "ADMINISTRATION", AND "OTHER" but note these should be written in English. Which event types belong to which category is visible from the Event editing page.
  * `[WORK-DAY-HAS-NONE-OF-EVENT-CATEGORIES|ABSENCE]`
    * Matches the setting exception if there are no events on the day belonging to the category of absence e.g. sick leave, annual holiday etc.
  * `[WORK-DAY-HAS-EVENTS-WITH-BASE-PART|balance|bank]`
    * Matches the setting exception if there are events on the work day¹ which have overtime's base target part as either "balance" or bank".
    * The magic wand tool described above can be used to pick the desired overtime target selections.
  * `[WORK-DAY-HAS-EVENTS-WITH-OVERTIME-PART|balance|bank]`
    * Matches the setting exception if there are events on the work day¹ which have overtime's overtime target part as either "balance" or bank".
    * The magic wand tool described above can be used to pick the desired overtime target selections.
  * `[WORK-DAY-BEGINS-BEFORE|06:00]`
    * Matches the setting exception if there are events on the work day¹ which begin before 06:00. The 06:00 in the example can be replaced with any time that is wanted to check the event begin time with. Any logged event activates this exception, including, for example, a Notes event or a Correction event.
    * The work day begins before - value can be negative for targeting previous days' events. For example if rule needs to be valid if work is started on previous day before 22:00, the rule must be written [WORK-DAY-BEGINS-BEFORE|-02:00].
    * The work day begins before - value can be over 24 for targeting next days' events. For example if rule needs to be valid if work is started on next day before 2:00, the rule must be written [WORK-DAY-BEGINS-BEFORE|26:00].
  * `[WORK-DAY-BEGINS-AFTER|06:00]`
    * Matches the setting exception if there are events on the work day¹ which begin at exactly 06:00 or after 06:00. The 06:00 in the example can be replaced with any time that is wanted to check the event begin time with. Any logged event activates this exception, including, for example, a Notes event or a Correction event.
    * The work day begins after - value can be negative for targeting previous days' events. For example if rule needs to be valid if work is started on previous day from 22:00 or after that, the rule must be written [WORK-DAY-BEGINS-AFTER|-02:00].
    * The work day begins before - value can be over 24 for targeting next days' events. For example if rule needs to be valid if work is started on next day at 2:00 or after that, the rule must be written [WORK-DAY-BEGINS-AFTER|26:00].
  * `[WORK-DAY-BEGINS-BEFORE-BY-CATEGORY|06:00|WORK|ABSENCE]`
    * Works like `[WORK-DAY-BEGINS-BEFORE|06:00]` but the day needs to begin with an event type that belongs to one of the categories defined in the rule.
  * `[WORK-DAY-BEGINS-AFTER-BY-CATEGORY|07:00|WORK]`
    * Works like `[WORK-DAY-BEGINS-AFTER|06:00]` but the day needs to begin with an event type that belongs to one of the categories defined in the rule.
  * `[WORK-DAY-BEGINS-BEFORE-BY-EVENT-TYPE|06:00|101|102]`
    * Works like `[WORK-DAY-BEGINS-BEFORE|06:00]` but the day needs to begin with an event that is one of the defined event types. Event types are defined with event type codes.
  * `[WORK-DAY-BEGINS-AFTER-BY-EVENT-TYPE|06:00|101]`
    * Works like `[WORK-DAY-BEGINS-AFTER|06:00]` but the day needs to begin with an event that is one of the defined event types. Event types are defined with event type codes.


These can also be combined together and with most date rule commands e.g.
  * `[WORK-DAY-HAS-ANY-OF-EVENT-TYPES|101] Monday`
    * Matches the setting exception if the work day¹ has any event types with a code of 101 AND it's a Monday.
  * `[WORK-DAY-HAS-EVENTS-WITH-BASE-PART|salary|bank] [WORK-DAY-HAS-EVENTS-WITH-OVERTIME-PART|salary|bank]`
    * Matches the setting exception if the work day¹ has any events with overtime's base target part is salary or bank AND if the work day¹ has any events with overtime's overtime target part is salary or bank.


¹Work day in this context means all events in the work shifts belonging to the day that inherits it's start and end times from the "TES work week start time" setting. Important: Certain settings such as permitted work times, expected work times, and work rise times, do not have a perfect concept of the "Work day" as these settings form part of the calculations used to determine that. This will be improved in future versions.
## Absence type rule commands
An absence type can be set to a setting exception by using the following SQL clause:
FROM  
UserEventData  
WHERE  
ActivityTypeCode = 4  
AND AbsenceTypeId = the desired absence type ID
or if you need to define more than one absence type (123 and 124 are imaginary codes):
FROM  
UserEventData  
WHERE  
ActivityTypeCode = 4  
AND AbsenceTypeId IN (123, 124)
## Examples of possible setting exceptions
In addition to rule commands which target public holidays directly, an exception can be defined based on rules targeting days, months or years.
  * If the setting is always the same, except for **some certain day** , the rule can be defined as:  
`19.2.2017`  
Date format must be `dd.mm.yyyy`


  * If the setting is always the same, except for **some certain day each year** , the rule can be defined as:  
`25.12.[YEAR]`


  * If the setting is always the same, except for **5th day of every month** , the rule can be defined as:  
`05.[MONTH].[YEAR]`


  * If the setting is always the same, except for **any day of a specific month** , the rule can be defined as:  
`[DAY].01.2016`


  * If the setting is always the same, except for **leap day** , the rule can be defined as:  
`29.02.[YEAR-LEAP-YEAR]`


  * If the setting is always the same, except for **last day of February when the year is not a leap year** , the rule can be defined as:  
`28.02.[YEAR-NOT-LEAP-YEAR]`


  * If the setting is always the same, except for **epiphany which is on weekend** , the rule can be defined as:  
`06.01.[YEAR-EPIPHANY-ON-WEEKEND]`


  * If the setting is always the same, except for **epiphany which is not on weekend** , the rule can be defined as:  
`06.01.[YEAR-EPIPHANY-NOT-ON-WEEKEND]`


  * If the setting is always the same, except for **the Friday before Christmas Eve if Christmas Eve is on weekend** , the rule can be defined as:  
`[CHRISTMAS-EVE] [LAST-FRIDAY-IF-ON-WEEKEND]`


  * If the setting is always the same, except for **the next Monday after Independence Day if Indepence Day is on weekend** , the rule can be defined as:  
`[INDEPENDENCE-DAY] [NEXT-MONDAY-IF-ON-WEEKEND]`


  * If the setting is always the same, except on **certain day or days** , the rule can be defined for example like this:  
`Sunday` or `Monday,Tuesday,Wednesday,Thursday,Friday`  
NOTE! Brackets are not used in day names


  * If the setting is always the same, except for **last day of the month** , the rule can be defined as:  
`[DAY].[MONTH].[YEAR] last day of this month`


  * Jos asetusarvo on muuten aina sama, paitsi **launtaina ja sunnuntaina viikoilla, joilla jollain viikon työpäivänä on juhlapyhä** , voidaan säännöksi määrittää:
  * If the setting is always the same, except for **saturdays and sundays on weeks that have a public holiday on a weekday** , the rule can be defined as:  
`[WORK-WEEK-HAS-PUBLIC-HOLIDAYS] Saturday, [WORK-WEEK-HAS-PUBLIC-HOLIDAYS] Sunday`


## Exception as a SQL clause
An exception can be created also as an **SQL-clause**. This is meant for situations where there is no other way of defining the setting exception rule. Creating the setting like this requires sufficient knowledge of SQL-language.
Settings that use SQL are less performant than using rule commands, so to avoid slowness in the usage of service SQL-clauses should not be used unless there is no other way to achieve the desired results for a setting.
![](https://support.nepton.com/hc/article_attachments/35360048668957)
Exceptions can be made e.g. in situations where the setting needs to be different based on the events marked in the service or the information of a user. Possible exceptions can have any SQL-clause that uses UserEventData, UserData or UserInfoData - tables. The SQL-clause is written beginning with the FROM - keyword.
More information about the contents of the tables and the functions available can be found in [Setting up integration rulesets](<https://support.nepton.com/hc/en-gb/articles/360002489257>) \- article. Also keyword ':SalaryRenderingDate', can be used, this keyword is replaced in the SQL - clause with the date (YYYY-MM-DD) of the day which the settings are checked against.
An example where exception should match when the earliest working event on the date starts on the current date (i.e. work starts at earliest 00:00 on the day or after that), and the working event begins before or at 22:00. 
The recommended way in this situation is to use the rule commands WORK-DAY-HAS-ANY-OF-EVENT-TYPES and WORK-DAY-BEGINS-BEFORE
Note that WORK-DAY-BEGINS-BEFORE applies for the times before the given value, so if we want to include work starting **before 22:00 or exactly at 22:00** , we would have in the rule [WORK-DAY-BEGINS-BEFORE|22:01] like below:
[code]
    [WORK-DAY-HAS-ANY-OF-EVENT-TYPES|1] 
    [WORK-DAY-BEGINS-AFTER|00:00] 
    [WORK-DAY-BEGINS-BEFORE|22:01]
[/code]
SQL-clause example for the rule above. In these kind of sql examples it makes sense to also limit the start date in a way that an event that has started on the previous date does not affect the rules results.
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 1
      AND StartDateTime <= :SalaryRenderingDate || ' ' || '22:00'
      AND StartDateTime >= :SalaryRenderingDate || ' ' || '00:00'
[/code]
An example where exception should match when the earliest working event starts at 22:00 or after it and before 24:00 or at 24:00:
The recommended way in this situation is to use the rule commands WORK-DAY-HAS-ANY-OF-EVENT-TYPES and WORK-DAY-BEGINS-BEFORE
Note that WORK-DAY-BEGINS-BEFORE applies for the times before the given value, so if we want to include work starting **before 24:00 or exactly at 24:00** , we would have in the rule [WORK-DAY-BEGINS-BEFORE|24:01] as we want to include midnight and the helper supports having values over 24 to target work starting on the next day. Rule would be like below:
[code]
    [WORK-DAY-HAS-ANY-OF-EVENT-TYPES|1] 
    [WORK-DAY-BEGINS-AFTER|22:00] 
    [WORK-DAY-BEGINS-BEFORE|24:01]
[/code]
SQL-clause example for the rule above:
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 1
      AND StartDateTime >= :SalaryRenderingDate || ' ' || '22:00'
      AND StartDateTime <= :SalaryRenderingDate || ' ' || '24:00'
[/code]
An example where the exception is valid when the persons default cost center group code on the current date is 1011:
[code]
    FROM
      UserInfoData
    WHERE
      datetime(:SalaryRenderingDate) BETWEEN ValidFrom AND ValidTo
      AND InfoTypeName = 'DefaultCostGroupCode'
      AND Value = 1011
[/code]
An example where the exception is valid when the day has a certain event type and the day is either Saturday or Sunday. Weekday in %w format is from 0-6, where Sunday = 0.
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 100
      AND strftime('%w',:SalaryRenderingDate) IN (0, 6)
[/code]
Example, where the earning of annual holiday is defined to earn 2.5 annual holiday days a month except 2 days a month if employment has lasted less than 12 months based on Annual Holidays Act.
Rule command:
![](https://support.nepton.com/hc/article_attachments/35360048669853)
SQL-clause 2,5 days/month (note that this does not take working contract end date to account):   

[code] 
    FROM
      UserInfoData
    WHERE
      InfoTypeName = 'LastWorkingContractBeginDate' AND datetime(:SalaryRenderingDate) BETWEEN ValidFrom AND ValidTo
      AND
       ((Value <= substr(:SalaryRenderingDate, 1,4) || '-04-01' -- contract starts earlier than 1.4 or exactly on 1.4 the salaryRenderingDate year
         AND :SalaryRenderingDate >= substr(:SalaryRenderingDate, 1,4) || '-04-01') -- and we live date exact or later than 1.4 on the salaryRenderingdate
        OR
         (Value < CAST(CAST(substr(:SalaryRenderingDate, 1,4) AS Integer) - 1 AS Char(4)) || '-04-01')) -- contract starts earlier than last year 1.4 
[/code]
Example which defines e.g. KVTES requirement that 3 annual holiday days a month are earned if working relations have lasted for at least 15 years. Note! If you are also using the 2.5 annual holiday rule described above, this rule needs to be above that rule so that this rule is checked first and have the higher priority if both of the rules match. 
[code]
    FROM
      UserInfoData
    WHERE
      InfoTypeName = 'LastWorkingContractBeginDate'
      AND datetime(:SalaryRenderingDate) BETWEEN ValidFrom AND ValidTo
      AND
       ((Value <= CAST(CAST(substr(:SalaryRenderingDate, 1,4) AS Integer) - 14 AS Char(4)) || '-04-01' -- contract starts 1.4. or earlier on a year 14 years ago from day we are calculating earned annual leave days for
         AND :SalaryRenderingDate >= substr(:SalaryRenderingDate, 1,4) || '-04-01') -- and day we are getting this setting for is 1.4. or later
        OR
        (Value <= CAST(CAST(substr(:SalaryRenderingDate, 1,4) AS Integer) - 15 AS Char(4)) || '-04-01')) -- contract started earlier or on 1.4. on a year 15 years ago from day we are calculating earned annual leave days for
[/code]
Example where exception is valid if there is a marking of certain event type on the day, and the year and week number are on the defined list. Week numbers are in the range of 00-53.
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 100
      AND strftime('%Y',:startdatetime) = 2019
      AND strftime('%W',:startdatetime) IN ('00','01','10','11')
[/code]
Example where exception is valid if there is a marking of certain event type on the day, and the marking time is over 3 hours (= 3 * 3600 seconds).
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 1
      AND DATE(startDateTime) = :SalaryRenderingDate
    GROUP BY
      ActivityTypeCode
    HAVING
      SUM(Amount) >= 3 * 3600
[/code]
Example where exception is valid on weeks which have an odd week number. E.g. weeks 1, 3, 5, etc.
[code]
    [ODD-WEEK-NUMBERS]
[/code]
Example where exception is valid on weeks which have an even week number. E.g. weeks 2, 4, 6, etc.
[code]
    [EVEN-WEEK-NUMBERS]
[/code]
Example where the exception is valid for the week if the week has Independence Day on a weekday (Mon-Fri).
[code]
    FROM
      UserData
    WHERE
      strftime('%W', :salaryRenderingDate) = strftime('%W', strftime('%Y', :salaryRenderingDate) || '-12-06')
      AND CAST(strftime('%w', strftime('%Y', :salaryRenderingDate) || '-12-06') AS INTEGER) IN (1,2,3,4,5)
      /* this will set the rule to apply on the week of independence day if the independence
      day is on monday-friday */
      
[/code]
Example where the exception is valid if persons working contract start date is less than 3 months ago from the date the rule is being handled on. In the comparison value strftime('%s', :SalaryRenderingDate, '**-3 months** '). The last **highlighted** part can be replaced with the needed value.
[code]
    FROM 
      UserInfoData 
    WHERE 
      InfoTypeName = 'LastWorkingContractBeginDate' 
      AND strftime('%s', Value) > strftime('%s', :SalaryRenderingDate, '-3 months')
[/code]
Example, where any person information field is selected. A rule can be made where exception is set if the date input to a field is smaller than the day the rule is applied on + 3 months. This example can be used in a situation where persons last working contract start date has been input to a persons HR field. This information can be used as an exception if we don't want work rise (for example bank holiday compensation) to be calculated when the last working contract has started less than 3 months ago. UserInfoTypeName needs to be replaced with a field name used to store the information about the date. Note: If using other than date-field it is necessary to input date in American format '2022-06-01'.
[code]
    FROM 
      UserInfoData 
    WHERE 
      UserInfoData.InfoTypeName = '236_ViimeisinTyosuhdeAlkoi' 
      AND  :salaryrenderingdate >= UserInfoData.ValidFrom
      AND :salaryrenderingdate <= UserInfoData.ValidTo 
      AND strftime('%s', :SalaryRenderingDate) < strftime('%s', value, '+3 months')
    
[/code]
Example where the exception is valid if person has Annual leave marked on the day and it is a saturday. Weekday-function returns a value in the range of 0-6, where 0 is Monday and 6 is Sunday.
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 'VL'
      AND Weekday(Startdatetime) = 5
[/code]
## Spotting problems
If you see the following icon on the settings page, it means there is a problem with a setting that needs investigating. Open the control and look for mentions of the word "INVALID" e.g. "INVALID-CODE: 123"
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4419773868433)
