---
id: 4408626793105
title: Archived release notes
url: https://support.nepton.com/hc/en-gb/articles/4408626793105-Archived-release-notes
locale: en-gb
category: Platform Status and versions
category_id: 22476701377821
section: Platform status and versions
section_id: 360000934197
section_path:
- Platform status and versions
labels: []
promoted: false
updated_at: '2025-10-02T05:31:16Z'
edited_at: '2025-10-02T05:31:16Z'
---

# Archived release notes

Older release notes are listed on this article so that the release notes page dosn't grow too long. You can read the latest release notes [here](<https://support.nepton.com/hc/en-gb/articles/360006615478>).
##  **11.09.2025** release (2.16.38)
###  __ Improvements
  * #### Worktime Custom absence types now support translations
[ref 15103]
  * #### Worktime Quick start events now support translations
[ref 15653]


###  __ Fixes
  * #### Worktime calendar did not correctly display exceptional entries related to planned shifts from work schedules
[ref 15980]
  * #### Worktime rulesets UserSalaryData table had problems exposing the Public holiday compensation
[ref 15945]
  * #### In the Worktime calendar view, adding or viewing events could sometimes trigger an error
[ref 15932]
  * #### Worktime integration rulesets UserInfoData table failed to expose data in some cases
[ref 15953]


##  **28.08.2025** release (2.16.37)
###  __ Improvements
  * #### Worktime Public holiday compensation supports configuring a fixed number of hours
[Guidance](<https://support.nepton.com/hc/articles/360002558797>)  
[ref 15922]
  * #### Worktime IFS salary data integration supports the ADDINFO field
The field is only exported if used in a ruleset
[ref 15903]
  * #### The person import validation is now more forgiving. Processing of import files can continue in more situations where data errors are non-critical.
[ref 15841]


###  __ Fixes
  * #### The user's preference for mobile or desktop view was not always remembered after signing in.
[ref 15845]
  * #### Employees > Persons, "Email" column heading corrected.
[ref 15928]
  * #### Worktime reports did not always correctly order people alphabetically
[ref 15915]


##  **21.08.2025** release (2.16.36)
###  __ Improvement
  * #### Worktime settings with time inputs (HHMM) can now be cleared even if there are values which would normally be inherited.
[ref 15851]


###  __ Fixes
  * #### Performance issues causing person integrations to fail have been addressed
[ref 15873]
  * #### In Worktime setting exceptions, the rule '[WORK-DAY-HAS-EVENTS-WITH-OVERTIME-PART|uncompensated]' was incorrectly evaluated. This meant even days with events which cannot earn uncompensated overtime, such as planned work, would trigger the exception.
[ref 15812]
  * #### All of the fields in employment contract stay visible after signing
[ref 15781]
  * #### Worktime workrise settings were incorrectly hidden in some situations
[ref 15876]


##  **15.08.2025** release (2.16.35)
###  __ Improvements
  * #### Improved the person import reliability
[ref 15797]
  * #### The Worktime integration rulesets UserInfoData table has been extended with the following data fields:
    * Primary and Secondary Units
    * Primary & Secondary Supervisors
    * Length of work day
    * TES work week length
    * Worktime percentage
[ref 15798]
  * #### Public project notes are now included in Worktime > Project work totals by person report
Optionally, internal project notes can also be included in the report
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002548957>)  
[ref 15800]


###  __ Fixes
  * #### Desktop view works on mobile
[ref 15870]
  * #### The behaviour of the Worktime settings "In use" checkboxes is now consistent
[ref 14056]
  * #### Work rise settings were incorrectly hidden in some situations
[ref 15839]
  * #### The Worktime 'Mass set event locking dates' feature now loads people from a longer period by default to avoid confusion due to their employment relationship dates
[ref 15842]
  * #### Hour-based supplement values are shown correctly in the Worktime > Project work totals by person report
[ref 15800]
  * #### The Worktime > Supplement settings field 'Default value when added' was incorrectly hidden in some situations
[ref 15800]


##  **12.08.2025** release (2.16.34)
###  __ Fix
  * #### Resolved multiple login related issues


##  **09.08.2025** release (2.16.33 - Login Page)
###  __ New
  * #### Login page redesign
    * Login page has a lighter and cleaner appearance.
[ref 15406]
  * #### RFID login on desktop version
    * New setting available under Employees > Administration > Login which allows signing in with RFID tag on workstations.
    * For security, entering a personal PIN code is also required.
    * Ideal solution for shared workplace computers used for logging work hours.
[ref 15406]


##  **05.08.2025** release (2.16.32)
###  __ Fix
  * #### Deleted setting groups and person groups can be restored
[ref 15810]


##  **31.07.2025** release (2.16.31)
###  __ Fixes
  * #### Planned work remains visible in the mobile view when lunch hour is marked. 
[ref 15793]
  * #### In planning view, the filter for primary supervisor works correctly
[ref 15782]


##  **24.07.2025** release (2.16.30)
###  __ Improvement
  * #### Year leave report performance improvements
[ref 15780]


###  __ Fixes
  * #### Assumed lunch break is paid correctly in cases when there is a planned shift and overtime is earned from the whole day
[ref 15786]
  * #### In event import file, '24:00:00' can be used as a start or end time
[Guidance](<https://support.nepton.com/hc/fi/articles/4419484517521-Tapahtumien-tuonti-k%C3%A4ytt%C3%B6liittym%C3%A4n-aineistolatauksella-ennalta-m%C3%A4%C3%A4ritetty-rakenne>)  
[ref 15779]
  * #### Nepton Touch terminal performance improvements
[ref 15787]


##  **10.07.2025** release (2.16.29)
###  __ Improvements
  * #### Mass enter settings view user interface enhancements
[ref 15323]
  * #### Improvements to location management in shift planning
    * Locations can no longer be deleted, as deletion affects previously planned shifts. Locations that were deleted before this change remain hidden in the system.
    * Locations can now be hidden by marking them as ended.
[ref 15584]
  * #### More flexibility on calculating work contributing to levelling period per event or absence type
    * Work done towards levelling period can be configured to use TES settings by enabling "Use TES settings for event type contribution towards period" in Levelling period settings 
      * If set to yes, event and absence types will contribute towards levelling period based on the TES settings "Event types that contribute to work week" and "Absence types that contribute towards work week"
      * This allows for configuring work calculated towards levelling period per event and absence type
      * By default this setting is not enabled
[Levelling period other calculation settings](<https://support.nepton.com/hc/en-gb/articles/4405550013981>)  
[Event types that contribute to work week](<https://support.nepton.com/hc/en-gb/articles/25639644303645>)  
[Absence types that contribute to work week](<https://support.nepton.com/hc/en-gb/articles/28576011538077>)  
[ref 15769, 15238]
  * #### Absence contribution towards work week can be configured by absence type
    * If a paid or an unpaid absence is set to contribute towards work week, it can be set that which absence types contribute towards work week
    * By default all absence types are calculated towards work week, if absence event types are configured to contribute towards work week
[Guidance](<https://support.nepton.com/hc/en-gb/articles/28576011538077>)  
[ref 15769, 15320]
  * #### New setting option to set hour to hour overtime contribute to only work week length
[ref 15575]


###  __ Fixes
  * #### Start-up or termination work is earned correctly from accrual leave
[Guidance](<https://support.nepton.com/hc/en-gb/articles/15073908826909>)  
[ref 15772]
  * #### Permission set with a right to view worktime events allows to select related person groups in project reporting
[Guidance](<https://support.nepton.com/hc/en-gb/articles/17842757043613>)  
[ref 15774]
  * #### It's now possible to mass set event locking dates for users whose work contract has ended
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002521158>)  
[ref 15775]
  * #### Work rise and TES settings have proper setting titles in setting history control
[ref 15776]
  * #### Setting inheritance is shown correctly in setting "Assumed lunch calculated from event types"
[ref 15778]


##  **04.07.2025** release (2.16.28)
###  __ Fix
  * #### Fix for error in SD Worx integration
[ref 15770]


##  **03.07.2025** release (2.16.27)
###  __ New
  * #### New SD Worx salary data integration format which only sends changes
    * New salary data integration format for SD Worx called 'SD Worx (Difference)'.
    * This integration only sends changes, as opposed to sending all data for a chosen time period.
    * This is substantially easier for third party systems to consume and makes recovery from interruptions and errors easier.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/28022676814109>)  
[ref 15489]


###  __ Improvement
  * #### Priima can now utilise any personal information data from Nepton. Please contact your Nepton or Priima representative if you would like to include more of your data for use in Priima.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/10402517130653>)  
[ref 15287]


###  __ Fixes
  * #### Exceptional entry "Scheduled shift but no work entry" is now shown correctly in the worktime calendar
[ref 15762]
  * #### In certain situation a work rise targeting an accrual did not change the accrual
[ref 15740]


##  **27.06.2025** release (2.16.26)
###  __ Change
  * #### Internal changes to support Nepton workflow. No affect for customers.


##  **26.06.2025** release (2.16.25)
###  __ Fixes
  * #### Returned accrual settings accidentally hidden in recent updates
    * Rounding settings related to balances
    * Name & unit settings related to some accruals
[ref 15718]
  * #### Workrise settings loading was very slow
    * We have made changes to improve the loading times of these settings.
[ref 15746]
  * #### The Worktime calendar and salary calculations are loaded correctly when the selected date range includes a levelling period and the person's work contract begins after the start of that range
[ref 15753]


##  **18.06.2025** release (2.16.24)
###  __ Fixes
  * #### Validity controls related to additional person information fields would be incorrectly hidden in some situations.
[ref 15666]
  * #### The levelling period calculations are now correct in the planning view
[ref 15719]
  * #### Annual leave balance changes and resets can be imported via the API
[InsertActivitiesV4](<https://support.nepton.com/hc/articles/27550371952925>)  
[UpdateActivitiesV4](<https://support.nepton.com/hc/articles/27550929491869>)  
[ref 15709]


##  **12.06.2025** release (2.16.23)
###  __ Fixes
  * #### Work rises no longer cause duplicate events in the calendar
[ref 15694]
  * #### Solved problems saving working community settings with custom event types
[ref 15703]


##  **06.06.2025** release (2.16.22)
###  __ Fix
  * #### Saving a travel invoice works correctly
[ref 15704]


##  **05.06.2025** release (2.16.21)
###  __ Improvements
  * #### Improvements in viewing additional details of shifts and legends in planning view
[ref 15453]
  * #### Paid until and paid after date and time can be set in event import
    * Value can be set for sick leave events and absence events that allow changing the compensation type.
    * The change applies to event import via the user interface and event imports with scheduled runs.
[Importing events with scheduled runs](<https://support.nepton.com/hc/en-gb/articles/4403974690321>)  
[Manual event import](<https://support.nepton.com/hc/en-gb/articles/4419484517521>)  
[ref 11656]
  * #### Accrual balance changes and resets can now be imported via API
[InsertActivitiesV4](<https://support.nepton.com/hc/en-gb/articles/27550371952925>)  
[UpdateActivitiesV4](<https://support.nepton.com/hc/en-gb/articles/27550929491869>)  
[GetActivitiesV4](<https://support.nepton.com/hc/en-gb/articles/27551218873757>)  
[ref 15541]
  * #### Work time shortening leave can be earned according to work time percentage
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002559837>)  
[ref 14934]


###  __ Fixes
  * #### Planners can only publish shifts they have access to
[ref 15453]
  * #### Work rises are calculated correctly when using "Salary earned is shown on the day the shift ends" rendering mode
[ref 15633]
  * #### Work schedule shift deviations planned for another unit will be shown correctly in the planning view
[ref 15691]


##  **22.05.2025** release (2.16.20)
###  __ Fixes
  * #### The performance of calculating the flexible work hours accrual has been improved in cases where no earning period dates were defined
[ref 15654]
  * #### The rulesets' UserSalaryData table now includes the event type code of events that earn a work rise increase from weekly rest
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257>)  
[ref 15655]


##  **15.05.2025** release (2.16.19)
###  __ Fix
  * #### Nepton touch terminals fixes
    * Resolved RFID reader jamming issue
    * Increased scrollbar size in the Supplements view
    * Support for reading variable-length RFIDs also for external readers
[ref 15524, 15556, 15438]


##  **08.05.2025** release (2.16.18)
###  __ Improvements
  * #### The person import type "Kieku (New accounts)"
Employee numbers will only be used instead of missing Usernames for people who do not already exist in Nepton.
[ref 15085]
  * #### Planning view performance improvements
[ref 15415]
  * #### The '24h' label has been removed from full-day activities
[ref 15004]
  * #### In manual integration run view context selection is available for integrations which can create deletion and insertion rows
[Populus guidance](<https://support.nepton.com/hc/articles/25674625747869#h_01JNR75A23ZKWAYJ7HA3TM89JE>)  
[Mepco guidance](<https://support.nepton.com/hc/articles/23700503323933#h_01JEZV3MKT3MS9JX1BJPYZT8N2>)  
[ref 14961]
  * #### Worktime styling improvements
[ref 15539]
  * #### Mepco absence export and Populus absence export integrations can be scheduled
Absences can be stored in a queue and scheduled to be sent later. This prevents synchronisation issues during network and destination server interruptions.
[Mepco guidance](<https://support.nepton.com/hc/articles/23700503323933>)  
[Populus guidance](<https://support.nepton.com/hc/articles/25674625747869>)  
[ref 15008]


###  __ Fixes
  * #### Worktime and planning events are in sync
[ref 15572]
  * #### When shift coming from work schedule is removed, overnight events are displayed correctly in Worktime calendar
[ref 15316]
  * #### Events in table report can be downloaded in Excel
[ref 15558]
  * #### Accruals were calculated incorrectly when daily earning limit and maximum limit were used
[ref 15561]
  * #### Supervisors can edit their subordinates' shifts when linked to work schedule location
[Guidance](<https://support.nepton.com/hc/articles/360015675918>)  
[ref 15544]
  * #### Nepton Touch terminals support tags of different lengths when external reader is used
[ref 15438]


##  **29.04.2025** release (2.16.17)
###  __ Fix
  * #### Supervisor can select location in planning view
[ref 15565]


##  **29.04.2025** release (2.16.16)
###  __ Fixes
  * #### Line break added on the last line of the export file on Populus absence export
[ref 15550]
  * #### Planning view location selection hierarchy is shown correctly
[ref 15540]
  * #### Editing a shift or a group of shifts that includes a removed person is working correctly
[ref 15545]


##  **28.04.2025 18:00** release (2.16.15)
###  __ Change
  * #### Nepton SSO Service Provider certificate update
[ref 15532]


##  **24.04.2025** release (2.16.14)
###  __ Fixes
  * #### Fixes on work shift related tasks in Worktime views
    * Tasks for work schedule shifts were not displayed in calendar view in certain situations
    * Planned work shifts or work schedule related tasks were not displayed in mobile
    * Planned work shifts or work schedule related tasks were not displayed in Worktime shift lists
[ref 15496]
  * #### Locations are ordered alphabetically in planning view and location tree only shows active ones
[ref 15506]
  * #### Events in table report can be loaded as an Excel-file
[ref 15508]


##  **11.04.2025** release (2.16.13)
###  __ Fix
  * #### Person selection in events in calendar is working correctly
[ref 15521]


##  **10.04.2025** release (2.16.12)
###  __ Improvements
  * #### Improvements for accrual earning
    * Increased number of rows in accrual earning tables
    * Added ability to set start date for accrual earning tables
[ref 15416]
  * #### When using integrations that send data in real-time, day-level overrides trigger re-sync of the previous day only when necessary
[ref 15459]


###  __ Fixes
  * #### Multiple minor styling corrections for reports
[ref 15387]
  * #### Person selection is displayed in manual integrations and project reports according to worktime role permissions
[ref 15491]
  * #### Save button is displayed correctly in report person selection options
[ref 15495]
  * #### Fixes to Populus absence export integration
[ref 15511]
  * #### Fixes in downloading Excel files from reports
    * Hours by event type
    * EU / ELY-centre project report
    * Project work totals by person
[ref 15505]
  * #### Fixes to custom reports
    * Custom reports are generated correctly when two or more persons with setting exception rules that have SQL are included in the report
    * Published custom reports are now visible as published for non-admin users who have access to custom reports
[ref 15499]


##  **08.04.2025** release (2.16.11)
###  __ Fix
  * #### Fix for SAML SSO login issues
[ref 15507]


##  **04.04.2025** release (2.16.10)
###  __ Fix
  * #### Long running person data related integrations won't time out
[ref 15501]


##  **03.04.2025** release (2.16.9)
###  __ Improvements
  * #### Custom reporting user interface enhancements
[ref 15445]
  * #### Added setting for showing public holiday compensation in worktime calendar and events in table views
[ref 15326]


###  __ Fixes
  * #### Sick leaves by person group report includes people whose employment had ended after the reporting period
[ref 15482]
  * #### Corrections to supervisors use of planning
    * Supervisors can view their own shifts in the Planning view
    * Supervisors correctly gain access to locations and work schedules based on their location relationships
    * Supervisors can no longer configure work schedules when linked to work schedule related locations
    * Shifts from other locations or schedules appear differently and include information based on the viewer's permissions
[ref 15337]


##  **27.03.2025** release (2.16.8)
###  __ Fixes
  * #### In planning view, people added to locations set as not visible will be hidden
[ref 15450]
  * #### Fixes to permitted work times
    * In settings "Permitted work start time comes from planned shift" and "Permitted work end time comes from planned shift" settings exceptions work correctly.
    * Start-up and termination work were not limited by permitted work times in some cases.
[ref 15462]
  * #### Levelling period counting on days with annual leave works correctly
[ref 15470]
  * #### "Project work totals by person" and "EU / ELY-centre project report" excel exports are generated correctly
[ref 15461]


##  **22.03.2025** release (2.16.7)
###  __ Improvements
  * #### Improvements to levelling period calculations
    * Levelling period calculations performance improvements which will speed up retrieving salary data with levelling periods, reports, approval and use of Worktime calendar
    * Configuring Levelling period settings has been clarified 
      * Levelling period calculations are centralised under levelling period accrual settings
    * If levelling period calculations on a day do not match with calculations recorded earlier, an attention triangle will be displayed in Worktime calendar in a similar way as is done for balance accruals
    * Same improvements have been added for Flexible work hours accrual
[Levelling period calculation improvements](<https://support.nepton.com/hc/en-gb/articles/25649119586717>)  
[Configuring levelling period overtime calculations](<https://support.nepton.com/hc/en-gb/articles/4410630282257>)  
[ref 15236, 14875]
  * #### Retired method of configuring levelling periods has been removed of use
    * This method was used by a limited number of customers, and these customers have been contacted separately
    * Levelling periods are now always configured in the same way
    * If levelling periods have previously been defined using the retired method and need to be recalculated retroactively, the new method must also be configured so that it is in use retroactively
[Setting up a levelling period](<https://support.nepton.com/hc/en-gb/articles/360002559537>)  
[Retired method for setting up a levelling period](<https://support.nepton.com/hc/en-gb/articles/4405550230173>)  
[ref 8961]
  * #### Levelling period compensations can be included in salary data grouped by work done by project
    * Overtime compensations for the levelling period will be grouped to correspond with work performed under different projects in the levelling period
    * Previously, certain old integration setups processed this breakdown without a specific setting, but now this will be configured separely if needed. Enabling this functionality will slightly impact calculation performance
    * Implementing this functionality will slightly slow down the calculation performance
[Configuring levelling period overtime calculations](<https://support.nepton.com/hc/en-gb/articles/4410630282257>)  
[ref 15236]


###  __ Fix
  * #### Working hours were not correctly calculated towards the hours worked during the levelling period when the length of a workday during the period was determined by scheduled shifts and the day included both a public holiday and a scheduled shift
[ref 15316]


##  **20.03.2025** release (2.16.6)
###  __ Improvement
  * #### It is possible to earn work rise from fixed compensation start-up and termination work
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560978>)  
[ref 15363]


###  __ Fixes
  * #### Additional work percentage is correct when "TES additional work rise percentage" > "Only earn after total weekly hours" is set
[ref 15217]
  * #### Overtime breakdown can be opened in Events in calendar report
[ref 15425]
  * #### When selecting dates for manual integration run, people are loaded correctly for the selected period
[ref 15432]
  * #### Adding a setting group based on a system identifier works correctly
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002557537>)  
[ref 15435]
  * #### Empty columns can be hidden in the project hours by salary type report
[ref 15384]
  * #### Locations are ordered alphabetically in locations management location tree
[ref 15414]
  * #### In the online work contract editing, "ä" and "ö"-characters are shown and saved correctly
[ref 15439]
  * #### Overtime settings can be defined in person settings
[ref 15440]
  * #### Excel exports of project reports are no longer missing data
    * Affected reports 
      * EU/ELY-centre project report
      * Project work totals by person
[ref 15426]
  * #### In planning, hiding of the locations and the people added to the locations works
[ref 15450]
  * #### Nepton Flexim terminal version updates work correctly
[ref 15436]
  * #### Fixes for missing and unconfigurable accrual settings
[ref 15452]


##  **14.03.2025** release (2.16.5)
###  __ Fixes
  * #### Persons can successfully login using Microsoft login
[ref 15420]
  * #### Events in table report is working correctly when multiple persons are selected for the report
[ref 15413]
  * #### Overtime breakdown is shown in calendar correctly when overtime is paid as fixed salary
[ref 15411]


##  **13.03.2025** release (2.16.4)
###  __ New
  * #### New real-time integration "Populus absence export"
    * Integration transfers only new and edited absence events.
    * Integration allows absences to be exported with indicator for new rows "U" and with indicator for deletion rows "P". When editing both are sent.
    * New and edited absence events are transferred in real time when the event is saved.
    * Integration can be run also manually.
    * The method used in the integration can be potentially implemented with other integrations as well in the future.
[ref 15186]


###  __ Fixes
  * #### Optimisations to improve performance and alleviate issues such as slow login and mobile page availability
[ref 15393]
  * #### Changing the length of work day and work week with an exception works correctly in Worktime calendar view
[ref 15394]
  * #### Persons with recent employment start date can be selected in manual integration
[ref 15405]
  * #### People are only displayed in the work schedules they are currently assigned to
[ref 15349]
  * #### Employees page works correctly
[ref 15390]
  * #### The Approve hours view no longer displays duplicate overtime hours after approval
[ref 15353]
  * #### Files in integration scheduler history are now downloadable again
[ref 15401]
  * #### Planned shift emails now correctly specify whom the shifts are assigned to
[ref 15403]
  * #### Multiple minor styling corrections
[ref 15391]


##  **11.03.2025** release (2.16.3)
###  __ Fix
  * #### Manual run of some integrations could get stuck in waiting state.
[ref 15397]


##  **10.03.2025** release (2.16.2)
###  __ Fixes
  * #### Exceptional entries report results can be sent by email
Exceptional entries report results are correct when loading report for multiple persons
[ref 15381]
  * #### Employees > Persons page now loads correctly for all customersIn some cases Persons page did not load correctly
[ref 15368]
  * #### Planning view shows all the resources correctly now
[ref 15383]
  * #### Presence view did not load correctly in some occurrences


##  **08.03.2025** release (2.16.1)
###  __ Fixes
  * #### The planning view opens correctly when there is an overlapping planning period
[ref 15377]
  * #### Small fixes and updates related to the version release we performed earlier today, March 8, 2025


##  **08.03.2025** release (2.16.0)
###  __ New
  * #### Custom reports
Create reports based on your choice of Nepton data, with the option to share these reports with others in your organisation.
This feature is part of the new paid "Insights" service, which offers broader reporting options than the standard reports. Contact customer service to take it into use!
[ref 14588]
  * #### Accrual capabilities
    * Accruals now support automatically transferring hours over the maximum balance limit into another accrual or paying them as salary  
[Guidance](<https://support.nepton.com/hc/fi/articles/360010514358-Liukuvan-ty%C3%B6ajan-saldon-maksimi-ja-minimim%C3%A4%C3%A4r%C3%A4n-asettaminen> "Guidance")
    * Custom accruals now support monthly earning tables similar to the Annual leave absence accrual
[ref 14141]


###  __ Improvements
  * #### New setting "Work rise earning times based on" can be used to select how work rise earning times are interpreted
    * The recommended and default option is "Day the shift belongs to" which reads work rise earning times only from the day they are set, not from the days the shift might also overlap. For better service performance and clarity, it is advised to migrate to the "Day the shift belongs to" option.
    * If work rises have been in use before this update, a new option "Days the shift overlaps" has been set to avoid any changes in previous calculations.
[ref 14291]
  * #### Setting and setting group history control has been modernized and their functionality has been enhanced
[ref 14291]
  * #### New setting "Permitted work times based on" can be used to select how permitted work times are interpreted
    * The recommended and default option is "Day the shift belongs to" which reads permitted times only from the day they are set, not from the days the shift might also overlap. For better service performance and clarity, it is advised to migrate to the "Day the shift belongs to" option.
    * If permitted work times have been in use before this update, a new option "Days the shift overlaps" has been set to avoid any changes in previous calculations.
[ref 12726]
  * #### Worktime reports have been renamed and the UI refreshed
The new naming is now standardised and better describes the content of each report. The changes are as follows:
    * Work hours reports 
      * Annual leave, usage follow-up -> Annual leave usage by season
      * Annual leave, rolling month analysis -> Annual leave usage by month
      * Annual leave, earned days -> Annual leave earning by month
      * Sick leaves per person -> Sick leaves by person
      * Sick leaves per group -> Sick leaves by person group
      * Absences per person -> Absences by person
      * Balance events -> Managerial balance changes
      * Event report -> Event listing
      * Overtime report -> Overtime hours by person
      * Dining sum up report -> Dining totals by person
      * Dining report -> Dining by person
    * Project reports 
      * Project overtime report -> Project overtime hours
      * Project invoicing report -> Project work totals by person
[ref 15180]
  * #### Worktime settings default and inherited values are now visualised so the effective value can easily be seen at all levels
[ref 14318]
  * #### Permitted work times now have "Enabled" setting
By using this setting it is easier to manage days when permitted work times are in use.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002558597>)  
[ref 14625]
  * #### Email addresses may now contain special letter characters supported by UTF-8 encoding (For example Ä, Ö, and Å)
[ref 15268]
  * #### Improvements to UI styling
We have begun the use of a new component library for the development of our user interface. As a result, there will be many subtle differences in the appearance of the service in this version. In the future, this helps speed development and standardisation.
[ref 15075]
  * #### Empty Worktime Workrise settings inputs are now collapsed to improve usability
[ref 14555]
  * #### Online work contracts support now check box and multiline text-fields
[ref 15350, 15328]
  * #### The Nepton touch terminal application performance and security have been improved by migrating to the .NET 8 framework
This change affects all Nepton Touch devices issued after September 2022.
[ref 13964]
  * #### Minor performance improvement to Microsoft SSO login authentication
[ref 14850]
  * #### Standardisation of the technology behind different accrual types has resulted in subtle setting and naming improvements
[ref 14141]
  * #### Improvements to project search
[ref 15259]


###  __ Changes
  * #### Changes to accruals
    * Accrual balance reset event types will now be applied at the beginning of the day for all accruals, even in the past. Accrual balance change events at the end.
    * All accrual leave event types (holiday pay leave, worktime shortening leave, etc) are now treated as accrual leave regardless of whether the accrual is actually enabled or not. This can affect how these event types are reported on and exported.
    * Time created due to rounding up is now excluded from the "Worked time incl. absences" row in the calendars.
[ref 14141]
  * #### The term 'Sairausloma' has been changed to the term 'Sairauspoissaolo' everywhere in Nepton
[ref 15185]


###  __ Fixes
  * #### In rare situations, planned shifts could be duplicated when being Published
[ref 13744]
  * #### In rare situations, saving event edits could cause incorrect Year-leave accrual values
[ref 14061]


##  **03.03.2025** release (2.15.23)
###  __ Fixes
  * #### Public holiday compensation is not shown as a separate value in Worktime calendar or table view
[ref 15325]
  * #### Shifts from work schedule didn't always appear in Worktime calendar if those shifts were scheduled before the date Nepton had been taken to use
[ref 15324]
  * #### The IFS event approvals integration will no longer send data if the IFS integration ID and employee number are missing or set to 0
[ref 15327]


##  **27.02.2025** release (2.15.22)
###  __ Improvements
  * #### Following integrations have a setting to include line break on the last line of the export file:
    * Accountor Mepco HRM
    * Accountor Mepco HRM absence export
    * Custom export
[Mepco](<https://support.nepton.com/hc/en-gb/articles/360003473498>)  
[Custom export](<https://support.nepton.com/hc/en-gb/articles/10758741671581>)  
[ref 13441]
  * #### Work rise validity can be set according to a shift in work schedule with setting exception rules
[Setting exceptions](<https://support.nepton.com/hc/en-gb/articles/360002560677>)  
[ref 14935]
  * #### Configure work rises to earn an additional increment part, for example Sunday raise for evening work rise
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560978>)  
[ref 14932]
  * #### Improvements to start-up and termination work
    * Fixed compensation start-up and termination work can be earned without shifts
    * Start-up and termination work can be limited by permitted work times
[Guidance](<https://support.nepton.com/hc/en-gb/articles/15073908826909>)  
[ref 14933]
  * #### Public holiday calculation improvements
Public holiday calculations are now split to three settings:
    * Show public holiday - whether public holiday is shown in calendar or not
    * Earn compensation from public holiday - whether compensation is earned from a public holiday
    * Public holiday shortens work week - whether public holiday shortens work week or not
Setting exception rules [WORK-WEEK-HAS-PUBLIC-HOLIDAYS], [CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS], [LEVELLING-PERIOD-WORK-DAYS-HAVE-PUBLIC-HOLIDAYS] & [LEVELLING-PERIOD-CALENDAR-DATES-HAVE-PUBLIC-HOLIDAYS] have been replaced with new rules.
The new rules are:
    * [WEEK-HAS-PUBLIC-HOLIDAYS|SHOWN-AS-PUBLIC-HOLIDAY]
    * [WEEK-HAS-PUBLIC-HOLIDAYS|COMPENSATED]
    * [WEEK-HAS-PUBLIC-HOLIDAYS|SHORTENS-WEEK]
    * [LEVELLING-PERIOD-HAS-PUBLIC-HOLIDAYS|SHOWN-AS-PUBLIC-HOLIDAY]
    * [LEVELLING-PERIOD-HAS-PUBLIC-HOLIDAYS|COMPENSATED
    * [LEVELLING-PERIOD-HAS-PUBLIC-HOLIDAYS|SHORTENS-WEEK]
[Public holiday management](<https://support.nepton.com/hc/en-gb/articles/360002558797>)  
[Setting exceptions](<https://support.nepton.com/hc/en-gb/articles/360002560677>)  
[ref 15114]
  * #### It is possible to configure the calculation of the work week so that work hours on holidays that shorten the work week are calculated after normal work days
[ref 15216]
  * #### Added a setting for managing how absence hours are earned on days with a planned shift
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002558617>)  
[ref 15218]
  * #### "Assign people to needs automatically" -feature is now able to plan on public holidays
[ref 15256]


##  **20.02.2025** release (2.15.21)
###  __ Improvements
  * #### Nepton Flexim terminals quick recording now supports offline mode
[ref 15196]
  * #### Nepton Flexim terminals now supports Swedish language
[ref 15245, 15282]
  * #### Improved person import warning messages
[ref 14639]


###  __ Fixes
  * #### Planning tool "Assign people to needs automatically", now assigns shifts with tasks correctly
[ref 15275]
  * #### Terminal clocked events continued on other devices are no longer displayed as terminal clocked events.
[ref 14370]


##  **13.02.2025** release (2.15.20)
###  __ Improvements
  * #### Work schedule performance optimisation
[ref 15124]
  * #### "Assign people to needs automatically" -feature now supports over 30 day long periods
[ref 15253]
  * #### Accountor Mepco HRM absence export integration can be now configured to skip "P" or "U" rows based on SQL rule.
[ref 15235]


###  __ Fix
  * #### Accountor Mepco HRM absence export integration processes now all the events during the selected period when approving events
    * Previously only the first event of the approved period was processed
[ref 15249]


##  **06.02.2025** release (2.15.19)
###  __ Improvements
  * #### Compensation type "OnCall" now has "baseparttarget" set to "salary" when exporting data with rulesets
[ref 14732]
  * #### Maximum amount of work rises is now 100
[ref 15115]
  * #### Improvements to Nepton Flexim terminals project search
Support for searching in project name and code with partial match
[ref 15194]


##  **31.01.2025** release (2.15.18)
###  __ Improvement
  * #### Nepton Flexim terminals now support adding events in the past and the future
[ref 15195]


###  __ Fixes
  * #### Nepton Flexim Terminals correctly handle names with special characters
[ref 15220]
  * #### Person imports with empty values for the work schedule group no longer removes work schedule groups from the person
[Guidance](<https://support.nepton.com/hc/articles/360003762577>)  
[ref 15143]


##  **30.01.2025** release (2.15.17)
###  __ Fixes
  * #### In Employees->Persons view the role is now displayed based on the selected language.
[ref 13256]
  * #### When exporting data, the compensation type 'OnCall' now uses 'Salary' as the base part target.
[ref 14732]
  * #### Project creation and targeting works correctly when using a barcode reader with Nepton Flexim terminals.
A new permission "Can create missing projects via terminal barcode reader"
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002554338>)  
[ref 15171]
  * #### Work time calendar and table views now include annual leaves in the "Worked time incl. absences" row.
[ref 15174]
  * #### Accountor Mepco HRM absence export integration does not create anymore multiple files when deleting absences from multiple persons at the same time.
[ref 15197]
  * #### Service log performance optimisation.
[ref 15215]


##  **23.01.2025** release (2.15.16)
###  __ Improvements
  * #### Simplified menu structure in the employees section by removing unnecessary drop downs.
You are now taken directly to the related page (Affects Competencies, Units, Employers, and Payment groups).
[ref 15175]
  * #### Improvements to Accountor Mepco HRM absence export integration.
    * Support for multiple rulesets.
    * Setting for date format.
[ref 15135]


###  __ Fixes
  * #### Recording events in real-time no longer creates an unnecessary warning when using Accountor Mepco HRM absence export integration.
[ref 15135]
  * #### Persons' competencies can now be removed as intended.
[ref 11883]
  * #### Minor corrections to time and duration inputs in Worktime settings.
[ref 12472]
  * #### Competencies related spelling mistakes fixed.
[ref 13073]
  * #### Supplement salary codes using zero ("0") are now loaded correctly via rulesets.
[ref 15164]


##  **16.01.2025** release (2.15.15)
###  __ Improvement
  * #### When planning shifts for a person who does not have the required competencies a warning message is displayed.
[ref 14589]


###  __ Fixes
  * #### Stability improvement to Nepton Payroll integration where large data volume could cause the integration to fail.
[ref 15155]
  * #### Accountor Mepco HRM absence export integration won't process absence if it's marked to the calendar without end time. When open-ended absence is stopped and end time is set, the integration will run normally.
[ref 15153]


##  **07.01.2025** release (2.15.14)
###  __ Improvements
  * #### Concurrent integrations
Integrations that do not process the same data can now run simultaneously. This speeds up processing compared to the previous approach, where all integrations had to wait their turn in a queue.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/10510800700573-Scheduling-worktime-import-export-integrations#h_01HMEFD4EMGHZMGK8KYR3WR43Y>)  
[ref 15145]
  * #### Performance optimisations
[ref 15076]


###  __ Fixes
  * #### Worktime API methods InsertActivities and UpdateActivities now handle currency supplement correctly
The decimal part of supplements were omitted and the value was rounded down to the nearest integer.
[ref 15148]


##  **03.01.2025** release (2.15.13)
###  __ Improvement
  * #### Upgraded to newer SFTP library
[ref 15122]


##  **23.12.2024** release (2.15.12)
###  __ Improvement
  * #### Database performance optimisations
[ref 15000]


##  **17.12.2024** release (2.15.11)
###  __ New
  * #### Nepton has new integration "Accountor Mepco HRM absence export" which utilizes rulesets
    * Integration transfers only new and edited absence events while previously all events were transfered. This reduces manual work from payroll.
    * Integration allows absences to be exported to Mepco with indicator for new rows "U" and with indicator for deletion rows "P". When editing both are send.
    * New and edited absence events are transfered from Nepton to Mepco in real time when the event is saved.
    * Integration can be run also manually.
    * The method used in the integration can be potentially implemented with other integrations as well in the future.
[ref 15006]


##  **13.12.2024** release (2.15.10)
###  __ Fix
  * #### Accessing the person group information view or the deleted settings group view no longer shows an 'Access denied' message, even though access has been granted
[ref 15125]


##  **12.12.2024** release (2.15.9)
###  __ Improvement
  * #### Security improvements
[ref 15043]
  * #### Nepton Payroll now supports the transfer of work time project allocation information to Payroll.
[ref 15013]


###  __ Fixes
  * #### Sum of the night shifts in planning view is calculated correctly
[ref 14456]
  * #### Flexim terminals now display the correct error message if barcode scanning fails due to insufficient permissions
[ref 15064]
  * #### Assumed lunch is reduced from night shifts in planning view
[ref 15079]


##  **05.12.2024** release (2.15.8)
###  __ Fixes
  * #### Planning view filters now persist after a work schedule is published
[ref 15090]
  * #### Balance from accrual can be borrowed even though balances minimum amount has been reached at the start of the day (addition to fix released on 28.11.2024)
[ref 15045]
  * #### File based person imports done on Nepton user interface have been fixed (addition to fix released on 28.11.2024)
[ref 15044]


##  **02.12.2024** release (2.15.7)
###  __ New
  * #### We will collect feedback from Nepton users through a simple survey that measures the respondent's satisfaction with Nepton and the service they have received.
The survey will be displayed on both browser and mobile devices after the first work time entry of the day. Responses are given on a scale of 1–10, where 1 is the lowest rating and 10 the highest. Additionally, there is an opportunity to provide open-ended feedback. Skipping the survey is quick and easy.
[ref 15028]


##  **28.11.2024** release (2.15.6)
###  __ Improvement
  * #### Database performance optimisations
[ref 14214]


###  __ Fixes
  * #### Balance from accrual can be borrowed even though balances minimum amount has been reached at the start of the day
[ref 15045]
  * #### File based person imports done on Nepton user interface have been fixed
[ref 15044]
  * #### Planning filters have been fixed and are now working correctly after issues caused by the latest Chromium update
[ref 14990]
  * #### The "Default time of lunch breaks" setting now works correctly when lunch is assumed for events spanning multiple days
[ref 15063]


##  **26.11.2024** release (2.15.5)
###  __ Improvement
  * #### Internal optimization of integration from Nepton to Saarni EXP
[ref 15025]


##  **21.11.2024** release (2.15.4)
###  __ Improvements
  * #### New rule commands added for defining exceptions to settings:
New rule commands added for defining exceptions to settings: [WORK-DAY-BEGINS-BEFORE-BY-CATEGORY], [WORK-DAY-BEGINS-AFTER-BY-CATEGORY], [WORK-DAY-BEGINS-BEFORE-BY-EVENT-TYPE] & [WORK-DAY-BEGINS-AFTER-BY-EVENT-TYPE]
    * These rule commands allow you to create setting exceptions that apply when a workday starts with a specific event type or with an event type within a certain category, and the workday has started either before or after a specified time.
    * Rule commands replace work day length exceptions you were able to set in worktime settings: Work hours > Length of work day > Exceptions. The new rule commands apply to all events, regardless of how they are recorded.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560677>)  
[ref 14387]
  * #### The performance of integration rulesets has been improved for some use cases
[ref 14984]
  * #### Travel invoices maximum per diems payable for foreign daily allowances for 2025 have been added
[ref 13941]
  * #### Improved user experience in case the login expires on Worktime-section
[ref 13757]
  * #### Service log entries for scheduled person imports has been improved
[ref 13196]
  * #### Project search performance optimisations
[ref 14868]


###  __ Fixes
  * #### IFS Salary Data Integration timeout limit has been increased from 1 minute to 5 minutes
[ref 14988]
  * #### Calculation of additional work and overtime has been corrected when work is split in multiple periods
[ref 14983]
  * #### Missing shift deviations or shifts shown as duplicate are corrected in work shift planning view
[ref 14967]
  * #### Saving work week length exception in the calendar view with default system value "Inherit from parent" caused error
[ref 14997]


##  **14.11.2024** release (2.15.3)
###  __ Improvements
  * #### Added support for more absence codes in Mepco event import and standardised codes to better reflect their type in Mepco
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003773337>)  
[ref 14948]
  * #### Improvements to Flexim terminal project selection
[ref 14956]
  * #### Task scheduler performance optimisations
[ref 14971]
  * #### Database performance optimisations
[ref 14975]


###  __ Fixes
  * #### An empty value couldn't be added to the Work schedule group in Employees
[ref 14976]
  * #### Using certain settings with worktime shortening leave caused errors in several places, including the calendar view and when running integrations
[ref 14977]
  * #### It was possible to stop events in worktime calendar even when permissions to do so were not granted
[ref 14980]


##  **07.11.2024** release (2.15.2)
###  __ Improvements
  * #### It is now possible to have multiple RFID tags per person
[ref 14796]
  * #### In Netvisor integration, it is now possible to include multiple dimensions in one work hour row
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360007534058>)  
[ref 14965]
  * #### Personal ID can be saved in other formats than only in Finnish ID format
[ref 13200]


###  __ Fixes
  * #### When work rise increase based on weekly rest was earned from an unapproved work rise, unapproval was not shown correctly in UserSalaryData isApproved-field for the work rise increase
[ref 14937]
  * #### Adding new items to existing person additional drop down list user interface throws error message
[ref 14938]
  * #### The old version of Nepton Payroll had problems displaying the payslip in the salary view of Worktime calendar for some customers
[ref 14966]
  * #### Overtime increment part was not calculated for start-up or termination work done as overtime if the overtime targeted an accrual


##  **31.10.2024** release (2.15.1)
###  __ Change
  * #### The employee survey platform formerly known as Kiva Work is now called Saarni EXP. The Kiva Work tab in Nepton's top menu is now Saarni EXP
[ref 14887]


###  __ Fixes
  * #### Event request notification emails get sent multiple times
[ref 14816]
  * #### When typing characters into the search box for dropdown selections (such as subordinate selection list), the input response might become increasingly slow, especially as the dataset size grows
[ref 14862]
  * #### Scheduled person export returns wrong employer code
[ref 14930]
  * #### All manually started integrations now respect any settings that state which user the integration should run as e.g. users to import events as.
[Scheduling worktime import/export integrations](<https://support.nepton.com/hc/en-gb/articles/10510800700573>)  
[ref 14925]


##  **24.10.2024** release (2.15)
###  __ New
  * #### Nepton Payroll has been overhauled
    * Manage your payroll independently or with an accounting firm’s specialists.
    * Quick, transparent, and reliable payroll software that everyone can understand.
    * Avoid mistakes, corrections, and manual work by integrating HR data, payroll, work time, and absences in one service.
    * You can easily access Nepton Payroll from the Payroll tab in Nepton's top menu.
    * Learn more and get started: [Nepton Payroll](<https://nepton.fi/palkat/>)
[Guidance](<https://support.nepton.com/hc/en-gb/articles/4406269604113>)  
[ref 14034]


###  __ Improvements
  * #### Improvements for Nepton Flexim terminals
    * Project targeting
    * PIN-login option
    * Quick recording-feature
    * Supplements recording
    * Multiple small usability improvements
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003685277>)  
[ref 14449]
  * #### Added possibility to earn work rise increment based on weekly rest
    * Weekly rest increase can be earned according to work during work rise so that work rises on Sunday will be increased if weekly rest is formed
    * Work rise increase will be compensated on the same day weekly rest is compensated
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560978>)  
[ref 14553]
  * #### Security improvements
[ref 14860]


###  __ Fixes
  * #### Event request notification emails get sent multiple times
[ref 14816]
  * #### Embedded PDF in iframe are not displayed inside our trusted services pages
[ref 14861]


##  **17.10.2024** release (2.14.52)
###  __ Improvements
  * #### Visma LTR integration ruleset has gained support for new fields
    * Field "letter" can be transferred by selecting its value as VismaLTRLetter in the integration rule
    * Field "ts_directed" can be overridden by selecting its value as VismaLTRDirectedTimestamp in the integration rule
[Guidance](<https://support.nepton.com/hc/articles/11166111654685>)  
[ref 14792]
  * #### Security improvements
[ref 14743]


###  __ Fixes
  * #### Work schedule schedule group shift patterns couldn't be edited in case work schedule had schedule groups removed from use
[ref 14851]
  * #### Work schedule schedule group shift pattern changes could not be published
[ref 14855]


##  **10.10.2024** release (2.14.51)
###  __ Improvement
  * #### Nepton Flexim terminal remote-control tools for Nepton customer service use
[ref 14787]


###  __ Fix
  * #### It was not possible for a person planning work shifts to publish the shifts for a resource in case the work shift planner didn't have Worktime permissions to create events for the allocated resource
[ref 14849]


##  **09.10.2024** release (2.14.50)
###  __ Improvement
  * #### Needs are listed last, rather than first in Planned shifts by location levels -report
[ref 14817]


###  __ Fix
  * #### Planning tools did not always correctly consider work obligation contributions from events recorded in Worktime
[ref 14834]


##  **04.10.2024** release (2.14.49)
###  __ Improvement
  * #### Updated loading animation in the Approve event requests section to align with Nepton's modern visual identity
[ref 14198]


###  __ Fixes
  * #### Corrections have been made in checking permissions to copy own events
[ref 14723]
  * #### Overtime targets are now shown correctly in terminal
[ref 14737]
  * #### Fixed several issues in the Planning tool 'Assign people to needs automatically'
The following topics are now correctly considered when the tool is used
    * Absences
    * Unpaid lunch reductions
    * Daily work obligation
[ref 13391, 14809]
  * #### Opening planned shifts Excel gives error about corrupted pivot table
[ref 14810]
  * #### The supervisor lacked subordinates, the situation has now been corrected
[ref 14744]
  * #### Shift planning table doesn't set correct scroll bar position after making changes to shifts
[ref 14462]


##  **26.09.2024** release (2.14.48)
###  __ New
  * #### Nepton now supports Flexim terminals
[ref 14448]


###  __ Improvement
  * #### Security improvements
[ref 14651] [ref 14660]


###  __ Fixes
  * #### When events were approved in the Events in calendar view, if an event started before the selected week or ended after it, the approval was sent to the external system only for the selected week
    * A similar issue occurred in the Events in table view when approving events that started before the selected month or ended after it
[ref 14733]
  * #### Showing "Success" instead "Failed" on some Priima sync operations
[ref 14736]
  * #### The old version of Nepton Payroll had problems downloading the payslip in the salary view of Worktime calendar
[ref 14741]
  * #### Old primary supervisors will be removed from the person when targeting new ones
Duplicate primary supervisors has been cleaned up from database
[ref 14744]
  * #### Some actions not working in Priima via Nepton
[ref 14791]


##  **19.09.2024** release (2.14.47)
###  __ Fix
  * #### Corrections have been made in checking permissions to copy own events
[ref 14723]


##  **12.09.2024** release (2.14.46)
###  __ Fixes
  * #### Priima person sync is now successful even when the HR data field 'username' is an email address and the HR data field 'email address' is missing
A warning is shown instead of an error, when not all Priima persons are synced
[ref 14679]
  * #### Weekly rest compensation was not always calculated correctly when weekly rest had work week offsets set and compensation earning period was week day with the least work
[ref 14354]


##  **09.09.2024** release (2.14.45)
###  __ Improvement
  * #### Nepton Payroll preliminary release for selected customers. Trial use will continue through September and the official release will be done in October.
[ref 14034]


##  **05.09.2024** release (2.14.44)
###  __ Improvement
  * #### Earning threshold settings of Worktime shortening leave and Annual absence now support hours and minutes when they are earned based on hours.
[Setting up work time shortening leave](<https://support.nepton.com/hc/articles/360002559837>)  
[ref 14416]


###  __ Fixes
  * #### Deputies of supervisors could not edit events of subordinates if supervisor had access to person groups with limited permissions.
[ref 14643]
  * #### Fix for a problem causing some of Nepton mobile users having to login multiple times per day. In case the problem persists after the release of this fix, we recommend trying to create the Nepton-shortcut again using our renewed guidance.
[Renewed guidance](<https://support.nepton.com/hc/en-gb/articles/360002596437>)  
[ref 14520]


##  **29.08.2024** release (2.14.43)
###  __ Improvement
  * #### Presence view now always shows the dates of annual leaves and planned shifts
[ref 14629]


###  __ Fixes
  * #### Overtime targets are now shown correctly in terminal
[ref 14515]
  * #### Publish button in shift planning view is giving Page not found 404 error when too many persons or filters are selected
[ref 14556]
  * #### Mass copy with option "Delete original events after copying" was ending up situation where calendar view was showing ghost activities
[ref 14573]
  * #### Self help window opens normally in idesco terminals
[ref 14574]
  * #### Fixed a minor issue in project hierarchy in terminal
[ref 14587]
  * #### Day-based accrual value could not be changed by using supplement
    * Day-based accrual value can now be changed with supplement which has days as unit type. This change does not affect Worktime shortening leave and annual absence accruals. Same functionality will be added for these accruals in Nepton version 2.1.5.
[ref 14605]
  * #### Weekly rest time did not contain ts_accepted field when exported in Visma LTR format
[Guidance](<https://support.nepton.com/hc/en-gb/articles/11166111654685>)  
[ref 14648]


##  **22.08.2024** release (2.14.42)
###  __ Improvement
  * #### Work time shortening leave and annual absence accruals have new earning settings
    * "Earned only from regular time" can be used for setting that accrual is earned only from worked regular time, excluding overtime 
      * This setting is by default "No" which is how calculations functioned before adding the new setting
    * "Earn from time borrowed from accrual" can be used for setting that accrual is earned by time borrowed from accrual, e.g. time borrowed from balance 
      * This setting is by default "No" which is how calculations functioned before adding the new setting
[ref 13434]


###  __ Fixes
  * #### Start-up and termination work were not calculated towards earning of work time shortening leave and annual absence
[ref 13434]
  * #### Minutely scheduled integrations could have been skipped occasionally if they were enabled on equal hour
    * For example, schedule with settings schedule enabled: 13/08/2024 00:00:00, schedule type: minutely and minutely interval rule: 60 minutes, could have been skipped.
[ref 14121]
  * #### Sick leaves per group report was incorrectly showing an error about insufficient permissions when downloaded in Excel format
[ref 14608]


##  **08.08.2024** release (2.14.41)
###  __ Improvements
  * #### Automatic updating of the ongoing day in calendar view
Events in calendar and in table views now update the ongoing day automatically when the date changes. This allows real-time clocking on the correct ongoing day without manual page reload.
[ref 14539]
  * #### Added person contract type column to the integration ruleset UserData table
Contract type is set in worktime settings TES > Salary type
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257>)  
[ref 14535]


###  __ Fix
  * #### Current status page did not show overtime targets for other event types than Work
Now calendar and current status page show the same overtime targets
[ref 14541]


##  **01.08.2024** release (2.14.40)
###  __ Fixes
  * #### Currency values in Visma Personec F export format were not correctly formatted when custom base value name (PersonecBaseValueName) was used
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003512757>)  
[ref 14519]
  * #### Planned shifts caused issues with levelling period compensations
    * Compensations displayed approval value incorrectly when fetching salary data with integration rulesets
    * When running an integration, a warning would appear stating that events were unapproved despite all of the events in the period being approved
[ref 14523]


##  **18.07.2024** release (2.14.39)
###  __ Fix
  * #### Fixes to supplements entered in hours
    * The form no longer gives an error about an incorrect value when the value is correctly entered.
    * The width of the field has been increased so that the entered value is fully visible.
[ref 14371]


##  **11.07.2024** release (2.14.38)
###  __ Improvement
  * #### Internal optimization of software and terminals


###  __ Fixes
  * #### Fixes to worktime current status page when logged in with a PIN code
    * Project selection didn't always work.
    * After a certain time, the person could be automatically logged out in the middle of selecting a project or writing event notes.
[ref 14508]
  * #### In shift planning, the minimum target hours for the planned period were incorrectly calculated based on the maximum weekly hours.
[ref 14512]


##  **04.07.2024** release (2.14.37)
###  __ Improvement
  * #### We have extended the salary export format from Nepton to Populous to support all custom fields that Populous does
These are named CustomData1 to CustomData12 in Nepton
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003355918>)  
[ref 14487]


###  __ Fixes
  * #### When the day's worked time was below the regular working time, the time borrowed from the bank accrual was not included in the levelling period worked time
Now this can be done with the use of a new setting "Time automatically borrowed from accrual calculated as worked time"
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002559537>)  
[ref 14237]
  * #### Work rise could increase accrual during future planned shift even though work rise was set to be earned only from work event
[ref 14480]
  * #### The default method of transportation was sometimes wrong when creating a new travel invoice
To simplify use, "Car" is now always the default transportation method when creating a new travel invoice
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360004788238>)  
[ref 14473]


##  **27.06.2024** release (2.14.36)
###  __ Fix
  * #### Some users experienced slowness in workshift planning
[ref 14446]


##  **27.06.2024** release (2.14.35)
###  __ Improvements
  * #### Terminal quality of life changes & freezing fixes
Fixes to address some locking and freezing issues, plus a new self-help menu for easier restarting of the hardware and access to support and troubleshooting information. This version will be gradually rolled out to all Nepton terminals over the coming months.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/19809803596317>)  
[ref 14394, 14306]
  * #### User listing in the Employees section now loads faster for unit managers
[ref 14409]
  * #### Worktime reports updated to include start-up and termination work
[ref 14353]
  * #### Future accrual predictions can now be disabled
    * In Work hours > Accruals and overtime hours > Calculation settings, the future accrual predictions can now be disabled by setting "Calculate future accrual predictions" to "No" 
    * The default value for the "Calculate future accrual predictions" setting is "Yes"
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360005073918>)  
[ref 14442]


###  __ Fixes
  * #### In "Worktime > Work hours > Approve project hours"-view, an error would sometimes occur when clicking "View project hours to approve"
[ref 14377]
  * #### Levelling period compensations displayed approval value incorrectly when fetching salary data with integration rulesets
[Guidance](<https://support.nepton.com/hc/articles/360002559537>)  
[ref 14445]


##  **25.06.2024** release (2.14.34)
###  __ Fixes
  * #### Some users experience slowness in workshift planning
We have applied multiple fixes to address performance issues seen in Planning.
[ref 14446]
  * #### Events coming from Mepco are not visible in planning
Planning did not show events that were recorded before their event type was set to be displayed in planning.
[ref 14180]


##  **13.06.2024** release (2.14.33)
###  __ Improvement
  * #### It is now indicated that the "Salary"- section on events in the calendar view can be expanded
[ref 14381]


###  __ Fixes
  * #### Project approval had inconsistent behavior when assumed events were present in the approval view
[Guidance](<https://support.nepton.com/hc/articles/360002561477>)  
[ref 14127]
  * #### Fixed work schedule group and holiday schedule group importing issue
[ref 14343]
  * #### It was not possible to configure settings in "Persons > Person settings > Work Hours > Accruals and overtime hours"
[ref 14399]
  * #### Terminal slowness has been fixed. This fix also fix the terminals those get offline frequently.
[ref 14402]
  * #### Old events showed up in the shift planning if their event type was changed to one that, according to event type settings, should not be displayed in shift planning.
[ref 14414]
  * #### Event rounding method 'Up' or 'Down' did not round events spanning overnight
[ref 14417]
  * #### Realized work hours report did not show accrual values correctly if accrual unit type was days
[ref 14420]


##  **06.06.2024** release (2.14.32)
###  __ Improvements
  * #### In the management of worktime event types, it is now possible to set the event type behaviour to be the following for different accruals:
    * Accrual leave
    * Accrual value reset
    * Accrual value change
[ref 14380]
  * #### Start-up and termination work is now shown in the following worktime views:
    * Work hours > Events in table
    * Work hours > Approve hours
    * Work hours > Approve project hours
[ref 14358]
  * #### Worktime "Work hours > Approve project hours" has been optimised for better performance
[ref 14249]
  * #### The performance of integration rulesets has been improved
[ref 14378]


###  __ Fix
  * #### Start-up and termination work wasn't calculated correctly if Shifts > "Worked time over work obligation is earned primarily outside of planned shifts" worktime setting was not set to "Yes"
[ref 14390]


##  **30.05.2024** release (2.14.31)
###  __ Fixes
  * #### An error would sometimes occur when calling Worktime API RunIntegrationRulesetV2 method for running a ruleset that had return/export format as "Custom export"
[ref 14335]
  * #### If there is an absence spanning multiple days, and there is no planned shift or expected work to dictate the time it should be compensated on the day, event default start time is used
    * This allows weekly rest time to be calculated correctly when long absence is calculated as non-rest time
    * If event default start time is not set in settings, it defaults to 8 AM
[ref 14360]
  * #### Work rise was not earned from termination work when termination work filled the deficit at the end of the shift
[ref 14373]
  * #### It was not possible to earn on call during a planned shift
[ref 14365]


##  **23.05.2024** release (2.14.30)
###  __ Improvements
  * #### Improvements to start-up and termination work
    * Start-up and termination work fixed compensation can now be earned even when there is a deficit at the beginning or at the end of the shift. The amount of allowed deficit can be set in start-up and termination work settings.
    * Overtime targets in start-up and termination work can now overridden. 
    * Start-up and termination work can be set to reduce the threshold to earn weekly 100% overtime on the week.
    * It is now possible to define which event types and which event type and overtime target combinations can earn start-up and termination work.
    * Work rises breakdown in worktime calendar now shows the amount that comes from start-up and termination work.
    * Worktime calendar shows a breakdown of whether start-up and termination work consists of regular time, 50% overtime or 100% overtime.
    * Start-up and termination work can be exported in salary exports using integration rulesets.
[Start-up and termination work](<https://support.nepton.com/hc/en-gb/articles/15073908826909>)  
[ref 14244]
  * #### Improvements to permitted work times in worktime
    * Added the possibility to define whether work time limits are active per event type and overtime target
    * Added the possibility to allow a specific amount of work per event type before and after shift
[ref 14342]


###  __ Fixes
  * #### When weekly rest time calculations were in use, start-up or termination work could lead to an error in worktime calendar
[ref 14307]
  * #### Start-up and termination work was incorrectly created for an empty day in work schedule calendar
  * #### When using work schedules, start-up and termination work created an excessive amount of overtime for days when there was no shift
[ref 14295]
  * #### A warning has been added when trying to unapprove events to prevent events from being accidentally unapproved
[ref 14352]
  * #### Displaying day periods in weekly rest time breakdown has been clarified
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360007389978>)  
[ref 14355]
  * #### Event rounding method did not always work correctly depending on event start and end time
[ref 14361]
  * #### When using work schedules, days that were planned as having no shift would not form assumed lunch if work was done on that day
[ref 14359]


##  **16.05.2024** release (2.14.29)
###  __ Improvements
  * #### Levelling periods and flexible work hour periods can now be configured to automatically repeat
[Guidance](<https://support.nepton.com/hc/articles/360002559537>)  
[ref 13936]
  * #### New rule commands [ACCRUAL-EARNING-PERIOD-START-DATE] and [ACCRUAL-EARNING-PERIOD-END-DATE] added for defining exceptions to settings
    * These rule commands can be used to define a setting exception for the start date or end date of levelling period or flexible work hour period
[Guidance](<https://support.nepton.com/hc/articles/360002560677>)  
[ref 13936]
  * #### Event rounding method can be now set to round event times up or down
    * Options are: not in use, down, normal and up.
[ref 14339]
  * #### Added a setting to deactivate annual leave accrual
    * When the accrual is disabled, the annual leave accrual will no longer appear in annual leave requests or event approval views. The setting is useful in situations where the annual leave accruals are managed in an external system.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560698>)  
[ref 14308]
  * #### We have extended our HR data sync to Priima. Now we support exporting person role, unit, job title, default project and employee number. This extended sync is turned off by default
[ref 14322]


###  __ Fixes
  * #### Support for multiple web service endpoints has been added to IFS event approvals integration
    * It is now possible to approve events from users with different web service endpoints at the same time.
    * Previously the approvals would get sent to the web service endpoint of the user doing the approvals. The approvals are now sent to the web service end points of the users whose events are being approved.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003501757>)  
[ref 14333]
  * #### Events approved with the bulk actions tools of the Worktime calendar view were not synchronized with external systems when approving events for the entire day
    * Synchronization now works when approving entire days with bulk actions tools in Worktime calendar, if the setting "Approve full days instead of individual events" is set to "Yes".
    * Approving individual events with event editing form can not be done if "Approve full days instead of individual events" setting is set to "Yes" for the person whose event is being edited
[ref 14336]
  * #### Usersalarydata was missing approvedbyuserid and modifieddatetime values for certain compensations
    * Approvedbyuserid and modifieddatetime added to levelling period compensations
    * Modifieddatetime added to weekly rest time compensation
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257>)  
[ref 14337]


##  **07.05.2024** release (2.14.28)
###  __ Change
  * #### Nepton SSO Service Provider certificate update


##  **29.04.2024** release (2.14.27)
###  __ Fix
  * #### Issues with event approvals not being synchronized to external systems
Activities will sometimes not be synchronized to the external system. A fix has been applied to gain better visibility into this issue.
[ref 14332]


##  **25.04.2024** release (2.14.26)
###  __ Improvement
  * #### It is now possible to define more than 3 event imports in Worktime > Administration > Integrations
[Guidance](<https://support.nepton.com/hc/en-gb/articles/4419484517521>)  
[ref 14326]


###  __ Change
  * #### The absence type "Job alternation leave" was using its old name "Sabbatical leave" in other languages than Finnish. The name has been updated.
[ref 14315]


###  __ Fix
  * #### Accrual leave could cause unintended overtime during levelling period
This happened if in levelling period settings:
    * The setting "Handle broken levelling period according to AKT kuorma-autoalan TES" was in use and
    * Accrual leave type was listed in the setting "Absences that do not break levelling period according to AKT kuorma-autoalan TES". 
[ref 14324]


##  **23.04.2024** release (2.14.25)
###  __ Fix
  * #### Logging in with a mobile device was leading to the desktop view
[ref 14329]


##  **19.04.2024** release (2.14.24)
###  __ Fix
  * #### Not getting forward from company selection
The company selection was not working for some of our customers leading to situation where selecting a company returned them back to the company selection view.
[ref 14301]


##  **18/04/2024** release (2.14.23)
###  __ Improvements
  * #### Integration rulesets now expose the information about persons' work time roles in UserInfoData table
[ref 14223]
  * #### Performance improvements to worktime "Events in calendar" and "Events in table" views
[ref 14309]
  * #### Service log search now remembers the search criteria used, and also highlights the last log marking viewed
[ref 14156]
  * #### Person listing now highlights the person last viewed
[ref 14156]


###  __ Fixes
  * #### Custom event type with Emergency Work behavior did not behave like Emergency work
Now custom event types with Emergency Work behavior inherit the behavior of standard Emergency Work event type.  
NOTE: Behavior "No change" is shown for custom Emergency Work event types created before this release. Their calculation is not changed unless they are re-saved as Emergency Work. In that case they start to follow calculation logic of standard Emergency Work event type.
[Event types](<https://support.nepton.com/hc/en-gb/articles/360002520778-Event-types>)  
[Adding, enabling and editing event types](<https://support.nepton.com/hc/en-gb/articles/360002519157-Adding-enabling-and-editing-event-types>)  
[ref 14288]
  * #### Microsoft Login has been expanded to better support persons who have multiple Microsoft credentials active at the same time
[ref 13995]
  * #### The user's company was occasionally forgotten and had to be selected on the company selection page
[ref 14113]
  * #### Missing error messages on login
On the login page, when the username or password was mistyped, the related error message was not shown. Also on some occasions, error messages related to failed SSO logins were not shown.
[ref 14113]


##  **15/04/2024** release (2.14.22.1)
###  __ Fixes
  * #### Empty Work shift planning-view
When the view tried to load more than 2500 work shifts/needs, the view was showing only an empty page.
[ref 14301]
  * #### Work shift planning mass deletion-feature didn't work
[ref 14301]
  * #### Possible problems on Employees- and Work shift planning-sections
Configuration fault may have caused some user interface level problems.
[ref 14301]


##  **11/04/2024** release (2.14.22)
###  __ Fixes
  * #### The Visma LTR integration did not include the cost center from the project code if configured to do so
[ref 14250]
  * #### Fixed an issue where permitted work times didn't work correctly when using setting exceptions and overnight shifts
[ref 14289]


##  **04/04/2024** release (2.14.21)
###  __ Fixes
  * #### Several fixes and improvements to Enhanced Permission Management released on 02.04.2024
[Permission sets guidance](<https://support.nepton.com/hc/en-gb/articles/17842757043613-Permission-sets>)  
[ref 14248]
  * #### When trying to approve hours, there was an error preventing them from being approved
[ref 14247]
  * #### Recording events via the Nepton mobile link was not working
The disruption did not affect the mobile version of Nepton accessed via go.nepton.com.
[ref 14251]


##  **02/04/2024** release (2.14.20)
###  __ New
  * #### Enhanced Permission Management in Nepton
We have significantly improved permission management. The new release introduces customizable Permission Sets, enabling precisely defined permission management tailored to the enterprise-level needs. This simplifies administration while also improving data security, allowing for precise permission management based on organizational structure, for example. The new functionality needs to be enabled separately and does not affect the configurations of existing customers.
[Permission sets guidance](<https://support.nepton.com/hc/en-gb/articles/17842757043613-Permission-sets>)  
[ref 14161]


###  __ Improvement
  * #### Worktime Project hours by person - report has been optimised for better performance
[5 Project hours by person guidance](<https://support.nepton.com/hc/en-gb/articles/360002548957-Project-reporting#h_01H97R7ZXHZ8Y9AS18KCDG5V79>)  
[ref 14221]


###  __ Fix
  * #### When trying to take a project report, the user selection list did not show all of the users, despite the person taking the report having the 'Can report project events for all persons'
[ref 14242]


### 
##  **21/03/2024** release (2.14.19)
###  __ Improvements
  * #### Visma L7 project import can now be configured to include cost center received from L7 in projects code
This can be configured in Working Community Settings Integrations Projects Visma L7 project import having "Add cost centre into imported project code" set to "Yes". When this setting is on, Visma LTR export will automatically send the cost centre to Visma LTR from project code. When setting is set to "Yes", projects must be imported again to Nepton before sending data to LTR so that cost centres get sent correctly to LTR.
[Project import guidance](<https://support.nepton.com/hc/articles/360003751058>)  
[Salary export guidance](<https://support.nepton.com/hc/articles/11166111654685>)  
[ref 14126]
  * #### It is now possible to distinct work rise earned from additional work to be earned from additional work 0% and additional work over 0% separately
No action is required from customers. If work rise was earned from additional work before the change, it is now automatically set that work rise is earned from both additional work 0% and additional work over 0%.
[Guidance](<https://support.nepton.com/hc/articles/360002560978/>)  
[ref 14219]


###  __ Fixes
  * #### When additional work was earned at different percentages during the leveling period, it was not always shown in the correct order in the calendar
Now the additional work is arranged in ascending order according to the percentage.
[ref 14212]
  * #### In a previous release, the default for some accrual limit settings were changed and caused issues for some existing deployments
Default settings have been retroactively set to the old behavior for these existing customers.
[ref 14224]
  * #### Translations for some event type and accrual names were not displayed correctly
[ref 14210]


### 
##  **19/03/2024** release (2.14.18)
###  __ Fix
  * #### A problem preventing opening of the planning page in some cases has been fixed.
[ref 14225]


### 
##  **15/03/2024** release (2.14.17)
###  __ Fixes
  * #### The shift planning view gave an error message when an employee in the view didn't have both Weekly hours MIN and Weekly hours MAX set in the personal information.
[ref 14220]
  * #### Terminals show a proper error message if someone tries to log in using an unrecognized RFID tag.


### 
##  **14/03/2024** release (2.14.16)
###  __ Fixes
  * #### When calculating public holiday hours in shift planning, a person's maximum weekly work hours were not properly considered if they had differing values on different dates.
[ref 14206]
  * #### Prohibited HTML characters could be included in Document file names resulting in an error when downloading them.
[ref 14200]
  * #### The manual event import did not correctly import the begin time when multiple are events imported for the same day.
[ref 14193]
  * #### In some editing situations, events incorrectly lost the "Clocked in real-time via a terminal" icon, when they were still clocked in real-time via terminals (e.g. when only the event note was edited from a mobile device)
[ref 14199]
  * #### Supervisors were not sent emails about new messages on requested events that had already been approved.
[ref 14179]


### 
##  **07/03/2024** release (2.14.15)
###  __ Improvements
  * #### Levelling period additional work for part-timers can now be differentiated between them earning 0% additional work when full-time obligation is not reached and after that additional work will be earned according to TES additional work rise percentage.
    * This can be achieved by defining Levelling period settings "Use work time percentage to calculate additional work earning threshold" and "Part-time workers should earn additional work 0% under their full-time threshold" to be on.
[Guidance](<https://support.nepton.com/hc/articles/14849123960989>) [ref 13999]
  * #### The project settings that where located under Project type "Project work", have been moved to where the other project settings are located
[ref 14139]


###  __ Fixes
  * #### Shift list per day and Shift list per hour views caused error if end date was set before start date.
Now day picker automatically corrects faulty date inputs.
[ref 14190]
  * #### System no longer considers an empty locked day as approved (green background) if employee's contract has expired
[ref 14166]
  * #### Previously, supervisors didn't always receive email notifications for the subordinates' event requests because some subordinates didn't have an assigned primary supervisor. The system's data has been corrected so that each subordinate now has at least one primary supervisor selected. All primary supervisors will receive notifications from now on.
  
[Person import fields Guidance](<https://support.nepton.com/hc/en-gb/articles/360015933397-Person-import-fields>)  
[Bulk import supervisor information Guidance](<https://support.nepton.com/hc/en-gb/articles/360002430658-Bulk-import-supervisor-information>)  
[Adding supervisor Guidance](<https://support.nepton.com/hc/en-gb/articles/360002430618-Adding-supervisor>)  
[Person information fields Guidance](<https://support.nepton.com/hc/en-gb/articles/360004769718-Person-information-fields>)  
[Delete Person Guidance](<https://support.nepton.com/hc/en-gb/articles/360002424617-Delete-person>)  
[ref 14104]
  * #### In a previous release, the default for some settings were changed and caused issues for some existing deployments. The settings have been retroactively set to the old behavior for these existing customers.
[ref 14189]
  * #### Return Wait a moment...... (loader) message while loading content into the screen
[ref 14160]
  * #### Some accrual leaves were not calculated towards levelling period worked hours
[ref 13999]
  * #### In an earlier release, integration rulesets support for Start-up & Termination did not get released even though it should have. This has now been fixed.
[ref 14131]
  * #### The bulk action editing view now respects the 'Show the project duration input' setting. Before, it would always show the duration inputs.
[ref 14139]


### 
##  **06/03/2024** release (2.14.14)
###  __ Fix
  * #### Locations are accepted like work targets when checking the required minimum and maximum number of projects limits on Terminals.
The required limits are checked both when starting and ending activity.
[ref 14195]


### 
##  **04/03/2024** release (2.14.12)
###  __ Fix
  * #### A problem in storing Terminal information offline in case of connection problems affecting some Terminal device models has been fixed.
The problem did not affect the current Nepton Touch Terminal device model.


### 
##  **02/03/2024** release (2.14.11)
###  __ Fix
  * #### Styling of the icons has been fixed in the user interface
  * #### Opening the events in table view would in some cases give an error. This has now been fixed.
[ref 14187]


### 
##  **29/02/2024** release (2.14.10)
###  __ New
  * #### We will start collecting regular feedback from Nepton users through a simple survey that measures the respondent's satisfaction with Nepton and the service they have received.
The survey will be displayed on both browser and mobile devices after the first work time entry of the day. Responses are given on a scale of 1–10, where 1 is the lowest rating and 10 the highest. Additionally, there is an opportunity to provide open-ended feedback. Skipping the survey is quick and easy.
The first survey will be released gradually to different roles:
    * Mon 4.3. Administrators
    * Mon 11.3. HR, Payroll, Unit Manager
    * Mon 18.3. Planners, Work Schedule Planners, Supervisors
    * Mon 25.3. Employees and others not included in the aforementioned roles
[Guidance](<https://support.nepton.com/hc/en-gb/articles/16439727874717-Your-feedback-is-important-to-us>) [ref 13857]


###  __ Improvements
  * #### Accrual leaves will now pay and export salary on future dates
[ref 14110]
  * #### Added additional configuration options for earning weekly rest compensation only on Sunday and falling back to the rest shortfall if there was no work on the Sunday
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360007389978-Weekly-rest-time-compensation>) [ref 13920]
  * #### Selecting another project on terminal no longer requires clicking a separate confirmation button.
[ref 13817]
  * #### The project codes are shown for all the selected projects on terminal.
[ref 13817]


###  __ Fixes
  * #### In some instances, the task scheduler has inaccurately reported that the import has failed.
[ref 14158]
  * #### On terminal, switching a project to another using a code finds any acceptable projects by code.
Previously the search was limited to latest used projects.
[ref 13817]
  * #### Settings restricting the number of projects per event now work on terminals.
[ref 13994]


### 
##  **22/02/2024** release (2.14.9)
###  __ New
  * #### Previously released reporting by person groups has been extended with additional access rights
    * It is now possible to give permissions to edit and approve events or to manage settings and projects of persons belonging to these groups.
[Person information fields guidance](<https://support.nepton.com/hc/en-gb/articles/360004769718-Person-information-fields>)  
[Worktime roles guidance](<https://support.nepton.com/hc/en-gb/articles/360002554338-Worktime-roles>)  
[ref 13914]
  * #### The Worktime calendar and event approval view now show a building icon with the events that have been clocked in real-time with using a terminal device
[Recording event in real-time guidance](<https://support.nepton.com/hc/articles/16574372856221>)  
[Approving events and working hours guidance](<https://support.nepton.com/hc/articles/360002519197>)  
[ref 13930]
  * #### The balance accrual can now be configured so that the minimum/maximum balance limits can be exceeded
In this case, only a warning is shown
[ref 13931]
  * #### Custom and bank accruals now support the minimum/maximum balance limits and borrowing rules
[Guidance](<https://support.nepton.com/hc/articles/360005073918>)  
[ref 13931]
  * #### If levelling period has work done under levelling period maximum work hours, it is displayed in red in Worktime calendar
    * Amount of deficit from work under maximum work hours can be fetched using integration rulesets from UserSalaryData - table with condition CompensationType = 'LevellingPeriodUnderTarget'. This requires that levelling periods are configured in levelling period accrual settings.
[Setting up a levelling period guidance](<https://support.nepton.com/hc/articles/360002559537>)  
[Setting up integration rulesets guidance](<https://support.nepton.com/hc/articles/360002489257#h_01ESQQ0WBQTAC978EXHKYNGV27>)  
[ref 14000]


###  __ Fixes
  * #### Changing custom event type behaviour to certain event types was not possible in event type editing view
[Guidance](<https://support.nepton.com/hc/articles/360002519157>)  
[ref 14015]
  * #### The 'WorkRiseEarnedAtCompensationType' field, in the integration rulesets, was wrong when using accrual leave event types. This has now been fixed.
[ref 14146]
  * #### Lunch quick start event set the starting time incorrectly when the timezone in the settings was something other than Helsinki.
[ref 14144]
  * #### Event request approval view did not load correctly in some situations where persons selected had "Assumed event type on empty work days" set to "not inherit parent level setting".
[ref 14138]
  * #### Fixed a filter issue where selecting "All subordinates" showed all users in the organization. Filter now correctly displays only the subordinates of the current user.
[ref 14130]
  * #### Add event popup allowed creating duplicates of an event
    * The issue was present in both desktop view and mobile
[ref 13950]


### 
##  **15/02/2024** release (2.14.8)
###  __ Changes
  * #### New virtu meta data url is in use. Check [https://wiki.eduuni.fi/display/CSCVIRTU/Virtu-metadata for further details.](<https://wiki.eduuni.fi/display/CSCVIRTU/Virtu-metadata>)
[ref 13991]


### 
##  **12/02/2024** release (2.14.7)
###  __ New
  * #### New setting "Calculate threshold based on" has been added for work rises.
This setting makes it possible to calculate work rise's thresholds in two different ways:
    * Based on the duration of all work types that earned work rise.
    * Based on the duration of regular work hours done on the day.
By default, the thresholds are calculated according to the first method, which is based on the duration of all work types that have earned a work rise. This is the same calculation method that was used before the new setting was added.
[Guidance](<https://support.nepton.com/hc/articles/360002560978>) [ref 14129]


###  __ Fixes
  * #### Despite the setting that a certain type of event should not be included in the leveling period hours, the overtime for this event was mistakenly deducted from the leveling period hours.
[ref 14132]
  * #### It is now possible to select the value "None" for the settings "Earned if worked for" and "Earned" for the calculation settings of Worktime shortening leave and Annual abcense in the settings groups to ensure that the values are not inherited from the parental level settings.
[ref 14102]
  * #### Changed wording from "Terminal" to "Real-time" in overtime settings to prevent confusion.
[ref 14103]


### 
##  **08/02/2024** release (2.14.6)
###  __ New
  * #### It is now possible to defer the work rise compensation so that it is paid on the last day of the week.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560978-Work-rises>) [ref 14100]
  * #### Overtime can be targeted to different accruals and the overtime targeting options can be selected on Terminals.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360021083038-Recording-overtime-using-a-terminal>) [13471]


###  __ Improvement
  * #### We have added a compatibility setting for Nepton Touch terminal devices for our customers that have used 8-character RFID tags with Idesco Access Touch 4.0 devices.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/16619514736413-Adding-support-for-transitioning-from-Idesco-Access-Touch-to-Nepton-Touch>) [ref 14013]


###  __ Fixes
  * #### Quick starting work with mandatory projects enabled did not set the begin and end time correctly in the popup window.
[ref 14025]
  * #### Tools > Import events. Event type code validation could fail when event type had multiple codes set for different options.
    * For example, Sick leave (Certificate received) and Sick leave (Not received) both had codes set in integrations settings. If import file contained codes for Sick leave (Certificate received), validation failed. Validation took only in account one code event type for Sick Leave.
[ref 14112]
  * #### The notification on the planning page didn't work properly, leading to inaccuracies in the displayed information
[ref 14045]


### 
##  **01/02/2024** release (2.14.5)
###  __ New
  * #### Work rises can be configured to be earned from projects. This supports the use case where work rises can only be earned from events which are targeted to specific projects.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560978-Work-rises>) [ref 13935]


###  __ Improvements
  * #### Person group code can now be up to 255 characters long
[ref 13934]
  * #### Start-up & Termination work has been improved
    * It is now more clear in the calendar view what the compensation is and what the actual working time that the compensation has been earned from is.
    * Support for integration rulesets have been added
[ref 14030]


###  __ Fixes
  * #### Creating a new quick start event from calendar will now use the date selected by the user.
[ref 14090]
  * #### Start-up & Termination work calculations were incorrect when the fixed compensation was higher than the earning amount limit for hourly-based compensation.
[ref 14030]
  * #### Cafeteria managers could not access the worktime calendars.
[ref 14101]
  * #### Work increment and supplement settings didn't show setting history icon when there was expired setting values.
[ref 14082]


### 
##  **25/01/2024** release (2.14.4)
###  __ Improvements
  * #### The functionality, appearance and usability of the Calendar view in Work time has been improved.
    * Projects from lunch breaks are no longer directly visible in the calendar view. You can see the project by clicking on the lunch event
    * Assumed events can now be edited from the calendar by clicking on them
    * Creating a new lunch from a template will now use the default lunch times, not the current time
    * The appearance of the date range picker has been improved
[ref 14072]


###  __ Fixes
  * #### Fixed an issue where the arrow symbol wasn't displayed for ongoing events on some phones. The arrow is now displayed properly, so you can easily see when an event is in progress.
[ref 14052]


  * #### Missing emergency work icon is restored in work time calendar.
[ref 14074]
  * #### Users couldn't view shifts from persons in their person group when they had permissions to view them.
[ref 14077]
  * #### Assumed lunches now display as approved if their parent event is approved.
[ref 14072]
  * #### Event import resulted in a failure if event import file contained persons whose working contract was not active.
    * Returned the earlier behaviour where it is not considered an error if import file contains persons whose working contract has ended.
[ref 14088]
  * #### Filtering to subordinates in worktime person selection didn't display your own subordinates but included deputy derived subordinates as well
[ref 14086]
  * #### Email notifications to deputies were sent incorrectly to persons who had been at some point a deputy but who were not deputies anymore.
[ref 14080]
  * #### Setting a parent project for a project caused an error. This has now been fixed.
[ref 14075]
  * #### Creating an event request caused an error in some occasions where request duration was prefilled to be 0 minutes.
[ref 14042]


### 
##  **18/01/2024** release (2.14.3)
###  __ Improvements
  * #### Irrelevant exceptional entry warnings are now skipped when saving events.
[ref 14058]
  * #### Added missing setting for "Leave/holiday ignored if public holiday" to earned accrual leave accruals.
[ref 14058]


###  __ Fixes
  * #### Current status project selection was disabled incorrectly for certain users.
[ref 14068]
  * #### Salary type filter in worktime person selection didn't work when filtering to selected supervisor's subordinates.
[ref 14065]
  * #### Filtering person selection in worktime to subordinates only didn't display correct tree in some cases.
[ref 14064]
  * #### Project managers were unable to report project hours of their projects from all persons.
[ref 14063]
  * #### Project details Project managers in worktime did not show all selected persons.
[ref 14059]
  * #### Opening an email link to the approve event requests view could give an error in some cases.
[ref 14048]
  * #### User defined event type translations were not displayed in all sections of the system
    * Worktime webservice method GetActivityTypes now returns the user defined translations
    * Calendar synchronisation (Ical/ics) now uses the user defined translations for event type names
[ref 14032]
  * #### Person couldn't see themselves in worktime person selection when it was filtered to subordinates only
[ref 14066]
  * #### Worktime person selection displayed nothing in some cases
[ref 14067]
  * #### Entering a wrongly formatted date would cause a unexpected error when saving a project
    * Relevant error message is now shown to the user.
[ref 14055]
  * #### An issue that caused some users to see an error in the Current Status view was fixed
[ref 14057]


### 
##  **16/01/2024** release (2.14.2)
###  __ Fixes
  * #### Worktime calendar person selection didn't show all person groups in some cases
[ref 14053]
  * #### Accrual related events spend accrual also on public holidays by default
    * For example, work time shortening leave was not spending work time shortening leave accrual on public holiday
[ref 14050]
  * #### Worktime public web service RunIntegrationRuleset or RunIntegrationRulesetV2 responded with unknown error if ruleset contained invalid rules
[ref 14038]
  * #### Invalid customer ID gave unknown error response with worktime public web services
[ref 14038]


### 
##  **15/01/2024** release (2.14.1)
###  __ Improvement
  * #### New setting for configuring an accrual code which can be used to identify accruals in exports and imports
[ref 12840]


###  __ Fixes
  * #### Worktime person selection "Filter to supervisor's subordinates" did not work in some cases
[ref 14040, 14041]
  * #### An issue that caused some users to see an error in the Current Status view was fixed
[ref 14043]
  * #### Worktime integrations scheduling settings did not allow using setting exceptions based on date rules
[ref 14046]
  * #### User selection in Mass enter settings did not load correctly in some situations
[ref 14039]
  * #### Continuing an absence event gave an error in worktime calendar and in mobile view
[ref 14044]


### 
##  **13/01/2024** release (2.14.0) - Worktime UI refresh
###  __ New
  * #### All Nepton users will be able to give feedback about the service after login.
    * Users can rate service from range 1 to 10 in lightweight survey. This is easy and effortless way to express thoughts about the service.
    * Goal is to understand users better and improve user experience of the service. We value user feedback and we will be using the feedback in development of the service.
    * Surveys are published regularly and they will be open for certain period. Survey will be shown to all users after login. Answering to the survey will be optional and can be skipped. 
    * If survey is skipped, it won't be shown again during that survey period.
    * First survey will be published during January 2024.
  * #### Start-up & Termination work compensations have been added
The purpose Start-up & Termination work is to compensate employees for extra work done before and after a shift.
[Guidance](<https://support.nepton.com/hc/articles/15073908826909>) [ref 11788]
  * #### Reporting by person groups. It is now possible to give a person rights to report worktime events and hours of any person groups.
In this case, the events and hours of persons belonging to these groups and their subgroups can be viewed and reported.
[ref 10977]
  * #### Custom event types can now be translated from the settings.
[ref 13880]
  * #### Basic custom accruals (bank, balance etc.) can now be added to the system.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360005073918-Accruals>) [ref 12835]
  * #### Weekly rest calculations support evaluating the rest before the first shift of next week.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360007389978-Weekly-rest-time-compensation>) [ref 13698]
  * #### Weekly rest calculations support evaluating work after Friday's last shift.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360007389978-Weekly-rest-time-compensation>) [ref 13870]


###  __ Improvements
  * #### Integration ruleset results now include fields for identifying the person who has approved an event, when selecting data from UserEventData or UserEventHistoryData table.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257-Setting-up-integration-rulesets>) [ref 13804]
  * #### Project import supports new optional fields:
    * External identifier
    * Project managers
    * Visibility to user groups
    * Visibility to users
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003737078-Project-import>) [ref 12104]
  * #### Project list view has been modernized and functionality improved:
    * Projects can be exported to a file which is already in import format and contains new supported fields.
    * Project is not updated during import if more than one project exists with the same code in the service. This prevents possibility to update incorrect project.
    * Project is not imported or updated if more than one project exists with the parent project code in the service. This prevents possibility to add project under incorrect project structure.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002561017-Project-management>) [ref 12104]
  * #### Worktime settings now show which have setting exceptions and which setting exceptions can be used.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560677-Configure-exceptions-to-settings>) [ref 13023]
  * #### The validity calendar button associated with settings now shows blue history icon if setting has historical values.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560677-Configure-exceptions-to-settings>) [ref 13023]
  * #### The Worktime > "Current status" page has received a face-lift. Some changes to be aware of:
    * New project selection controls allows for all projects to be browsed and searched.
    * New overtime controls means all overtime options can be selected, not just balance and salary.
[ref 13803]
  * #### The functionality, appearance and usability of the Calendar view in Work time has been improved.
    * The layout of the view has been improved. The calendar is now uniform in width.
    * Quick start events familiar from the Mobile view have been added to the Calendar view. Now it's easy to start, stop and continue events. Quick start events are displayed by pressing the desired day from the calendar.
    * You can continue past events and projects easily by clicking the "Continue" button on the past event.
    * Event icons, styles and colors have been refreshed.
    * Comprehensive legends for the various events appearing in the calendar have been added to the tools.
    * The user experience has been improved in many respects. For example, accepting or rejecting an event no longer takes you to a new page, but only a notification is displayed about the action.
    * The menu displayed when clicking on the event has been expanded and now displays more information. If one of the functions you've been using cannot be found in a familiar place, it is probably in the refreshed event menu.
    * More functions and information related to shifts have been added to the menu. Reserving a shift need, canceling a shift and reserving a shift is now possible from the menu. In addition, shift information such as tasks and description is displayed.
    * The less used functions of the menu have been moved under the new "Tools" selection to improve the user experience.
    * The entire day will now turn green when all events for the day have been approved. The approval or disapproval of the projects does not affect this. Also, if a day without events is locked, it will be shown green.
    * Similar changes have been made to "Events in calendar" report, "Events in table" view, and "Approve hours" view as in the Calendar view.
    * In addition many other improvements have been made related to for example styles, colors and font sizes.
[ref 13840]
  * #### Help tips is now shown in events in calendar view.
[ref 13823]
  * #### Help tips in events in calendar and work shift planning views is not automatically shown again if it's already shown once.
Information about whether the help tips has been displayed is stored in the user's browser.
[ref 13823]
  * #### Users will now receive a warning when attempting to save or edit an event if it is detected that the event has a potential issue.
For instance, a notification will be triggered if the total working time on projects exceeds the daily working hours or the event is overlapping with another event.
[Guidance](<https://support.nepton.com/hc/articles/360002520998>) [ref 13748]
  * #### Changed how the system handles ruleset rule changing during the reporting period.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257-Setting-up-integration-rulesets>) [ref 11967]


###  __ Fixes
  * #### Event request approval view did not indicate a request with dashes when event request overlapped with a planned shift
[ref 13965]
  * #### Event request approval now has a date range picker making the process more straightforward and prevent errors like selecting end date that is before start date
[ref 12756]
  * #### Managing On Call settings in setting group level did not work correctly
[ref 14009]
  * #### In user setting group and person group administration, moving a group to root level resulted in an error
[ref 14004]
  * #### When a new person is created by person import via automated schedule, and a setting group membership is not provided, the person will be created without a setting group relationship.
The default setting group is _not_ used in this situation.
[ref 13884]


### 
##  **04/01/2024** release (2.13.38)
###  __ Improvement
  * #### Event import integration now supports importing the event duration
[Guidance](<https://support.nepton.com/hc/articles/4419484517521>) [ref 13739]


###  __ Fix
  * #### In person import, empty value in the "Classification of occupations"-field was erroneously interpreted as an invalid value
[ref 13977]


### 
##  **02/01/2024** release (2.13.37)
###  __ Fix
  * #### ANY-PUBLIC-HOLIDAY date rules did not work correctly as exceptions when configuring overtime targets in web creation and when recording real-time events
[ref 13985]


### 
##  **21/12/2023** release (2.13.36)
###  __ Fixes
  * #### Online work contract check box-field values were not getting saved
[ref 13980]
  * #### Running RunIntegrationRulesetV2 API method resulted in an error with some formats when providing a return format different from what is set in ruleset settings
[Guidance](<https://support.nepton.com/hc/articles/360014449458>) [ref 13963]
  * #### Approve event requests view would sometimes display the wrong amount of annual leave days earned in an earning period (e.g. 2022), if more than one earning period was displayed
[ref 13943]
  * #### Improvements have been made to the Estonian translations
[ref 13747]
  * #### Improved error message for Visma LTR integration when it was configured to an end point that did not provide response in JSON format
[ref 13956]
  * #### In "_Work hours > Approve hours_" view, if approving with locking was enabled, approval options were not displayed correctly in the view if there were multiple persons selected for approval
[ref 13947]


### 
##  **07/12/2023** release (2.13.35)
###  __ Improvement
  * #### Travel invoices maximum per diems payable for foreign daily allowances for 2024 have been added
[ref 13206]


###  __ Fix
  * #### Fixes to travel invoice calculation
When the travel event has a trip abroad and then continues back in Finland, the system no longer sets foreign daily allowance on travel days taking place in Finland.
Certain compensations are now offered as per regulations when the duration exceeds the stipulated threshold and not when the duration is exactly on the threshold (e.g. half domestic daily allowance when duration is **over** 6 hours)
[ref 13174]


### 
##  **04/12/2023** release (2.13.34)
###  __ Fix
A fix to whether being on on call is counted as rest time by default or not.
  * On November 16th an option was added to determine whether or not on call time is calculated as rest time or not. Before the update on call was always counted as rest time.
  * When the update was made the default setting for the feature was that on call is not counted as rest time. The new default setting was in conflict with the previous logic and would have required several customers to change the setting.
  * A fix has now been made to the default setting. By default, being on call will continue to be counted as rest time in the calculation of weekly rest.
  * If you do not want on call time to be counted as rest time, you must make a change to the setting in: _Work hours Weekly rest period Event types treated as rest time On call_
[ref 13946]


### 
##  **01/12/2023** release (2.13.33)
###  __ Fix
  * #### Travel invoice form crashed if a supplement used in daily allowance calculation had no unit-text
[ref 13942]


### 
##  **30/11/2023** release (2.13.32)
###  __ Improvements
  * #### Work time levelling period has a new setting "Handle broken levelling period according to AKT kuorma-autoalan TES". Setting is available on working community and setting group levels.
    * When setting is in use, levelling period is interpreted broken according to collective agreement AKT kuorma-autoalan TES and overtime of broken levelling period is calculated as described in the collective agreement.
[Guidance](<https://support.nepton.com/hc/fi/articles/4410630282257-Tasoittumisjakson-ylity%C3%B6laskennan-m%C3%A4%C3%A4rittely>) [ref 13564]


###  __ Fixes
  * #### Travel invoice might have calculate the allowances incorrectly when a trip went over the travel time
    * The calculation now uses only the trip duration which falls inside the travel time
    * The user-interface will show a warning if a trip has been marked under or over the travel time
[ref 13902]
  * #### Excel version of Realized work hours report contained day values in string format which prevented summarizing the values with Excel functions.
[ref 13922]
  * #### Users were always redirected to Events in calendar view after login.
    * Service should remember which one is the preferred view for user: Events in table or Events in calendar. User is redirected to either one of these pages after login depending which one of them was visited last.
[ref 13924]
  * #### Project hour summary of Events in table view did not show decimal values of supplement correctly.
[ref 13915]


### 
##  **23/11/2023** release (2.13.31)
###  __ Improvement
  * #### Levelling periods additional work earning threshold can be configured to scale to part-time worker's worktime percentage
[Guidance](<https://support.nepton.com/hc/en-gb/articles/14849123960989-Defining-levelling-period-for-part-timers>) [ref 13893]


###  __ Fix
  * #### The planning filter did not function properly when filtering tasks and persons
[ref 13917]


### 
##  **16/11/2023** release (2.13.30)
###  __ Changes
  * #### The IP address for actions such as the IP address a work event was created from has been hidden from the UI
[ref 13802]
  * #### Setting "Exclude additional work from levelling period overtime calculations" has been replaced with the new setting "Additional work calculated as worked time" in the view Worktime > Settings > Work hours > Levelling period
Change requires no action from customers


###  __ Fixes
  * #### Weekly rest time can now be earned when a non-rest event occupies 100% of the the full period
[ref 11562]
  * #### Spending half a day of work time shortening leave or annual absence was not possible when accrual was earned in days
[Guidance](<https://support.nepton.com/hc/articles/360002559837>) [ref 13876]
  * #### Annual leave balance change event did not alter person's annual leave balance in certain situations
[ref 13882]
  * #### On Call could not be configured to act as non-resting time in Weekly rest calculations
[ref 11885]
  * #### Calculating weekly rest time earning did not always work correctly when earning period was based on week day with the least work and week start time was other than midnight in Monday
[ref 13891]
  * #### Employment start and end dates were not integrated correctly into Priima when their values were left empty
[ref 13898]
  * #### When IFS work hours export was run, the request sent to IFS and the response from IFS were not saved correctly into the service log
[ref 13890]


### 
##  **09/11/2023** release (2.13.29)
###  __ Fixes
  * #### Event request e-mail notification was not sent to supervisors if it was added from a terminal or from the current status page.
[ref 13839]
  * #### Issue with payment group payment days
When setting up payment group payment days, some days were automatically avoided as payment dates even if the days were banking days. These incorrectly avoided days were: 6.4.2023, 28.3.2024, 30.4.2024, 31.12.2024, 17.4.2025, 30.4.2025, 31.12.2025.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/4406602996625-Payment-groupst>) [ref 13871]


### 
##  **02/11/2023** release (2.13.28)
###  __ Improvements
  * #### Usability improvements to work schedules
    * Changes to work schedule calendars needs to be now separately published
      * Before this update, changes were taking effect immediately after saving
    * It is now easier to notice that the work schedule period has unpublished changes
      * Schedule period calendar "Publish"-button now indicates the number of unpublished changes
      * Schedule period listing now indicates if unpublished changes exists
    * Shift pattern offset zero now, instead of one, means that the shift cycle starts from the first shift of the shift pattern 
      * Positive shift pattern offset values now delay the start of the shift cycle (previously delaying was done by using negative numbers)
    * Publishing now tells what is being published and what publishing means
    * The work schedule period calendar setup view can now be maximized
    * Legend, print, and maximize buttons have been moved into the tools menus in views having many view-related functionalities
[Guidance](<https://support.nepton.com/hc/en-gb/articles/12039347959581>) [ref 13667]
  * #### Added a setting for controlling the threshold at which rounding weekly rest compensation occurs
Setting can be found in Worktime Administration Working community settings/Setting group settings Work hours Weekly rest period Compensation when weekly rest period is not met Additional options.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360007389978>) [ref 13778]
  * #### Fixed rounding down working unintuitively with the threshold for all rounding settings
Rounding down will now only occur if the threshold is not set, or the remainder over the rounding interval is less than the threshold. For example, this can be used to ensure overtime is only paid once they work a particular number of minutes of overtime.
[ref 13778]


###  __ Fixes
  * #### In certain situations, calendar displayed a part of a shift on the wrong day
[ref 13814]
  * #### Targeting several projects to an event, leaving the duration of the last project empty, could lead to a situation where the project targeting didn't fill the duration of the event.
[ref 13877]


### 
##  **26/10/2023** release (2.13.27)
###  __ Fixes
  * #### Copying of permitted or expected work times did not work correctly
[ref 13853]
  * #### Events in table report did not show multiple users correctly
[ref 13854]


### 
##  **19/10/2023** release (2.13.26)
###  __ Improvements
  * #### Worktime calendar has now a separate popup which shows week level breakdown of rest times related to weekly rest compensations.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360007389978-Weekly-rest-time-compensation>) [ref 13711]
  * #### Planning view now lets the user to change view filters if it detects that loading the view might take a long
[ref 13728]
  * #### Naming of scheduled tasks of trusted services is now unified. They are renamed as:
    * Henkilöiden vienti Kiva Work -palveluun to **Synchronization with Nepton trusted service Kiva Work**
    * Export Person to Priima to **Synchronization with Nepton trusted service Priima**
    * Nepton Palkat - Maksuryhmien vienti on jatkossa **Payment group synchronization for Nepton Payroll**
    * Nepton Palkat - Henkilövienti (päivittäinen) on jatkossa **Daily person synchronization for Nepton Payroll**
    * Nepton Palkat - Henkilövienti (reaaliaikainen) on jatkossa **Real-time person synchronization for Nepton Payroll**
[ref 13763]
  * #### Events in table view has now weekly rest column and separate popup which shows week level breakdown of rest times related to weekly rest compensations.
[ref 13783]
  * #### Changes to worktime setting _Work Rises_ >_Force time earned during work rise to overtime_ >_Force overlapping regular time to percentage_ , if work week calculation mode "KVTES" is in use.
Regular time is not automatically forced to overtime on weekend if there are weekly leave events on weekdays.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560978-Work-rises>) [ref 13836]


###  __ Fixes
  * #### Visma LTR integrations in the ruleset testing tool now display the result generated after running the queries and allow the result to be downloadable.
[ref 13770]
  * #### Work time shortening leave exceptions for both paid and unpaid event types did not work. The issue has now been fixed.
[ref 13799]
  * #### The support page was not accessible from the Nepton top menu. The issue has been fixed.
[ref 13821]
  * #### Weekly patches, fixes, minor changes and maintenance jobs only occur on Thursdays as of 1.10.2023. However Nepton still prevented scheduled jobs from running at 13:00-13:30 from Monday to Friday instead of just Thursdays. This issue has now been fixed.
See Platform status-page for further information on maintenance windows.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360006554777-Platform-status>) [ref 13835]
  * #### If the scheduled worktime event import had a problem in some of the import rows, marking in the service log was shown faultily as successful. The problem has been fixed and the marking in these situations is shown as a warning in the future.
[ref 13837]


### 
##  **11/10/2023** release (2.13.25)
###  __ Fix
  * #### Project search in event editing did not work correctly in Android mobile devices
[ref 13832]


### 
##  **09/10/2023** release (2.13.24)
###  __ Fix
  * #### Worktime help tips temporarily disabled
Help tips have temporarily been disabled whilst we address usability issues
[ref 13822]


### 
##  **07/10/2023** release (2.13.23)
###  __ New
  * #### Kiva Work is added to Nepton as a trusted service
    * Kiva Work is an easy-to-use personnel survey and analytics platform that makes it possible to develop personnel experience in Nepton.
    * You can easily access Kiva Work from the Kiva Work button in Nepton's top menu.
    * A free Lite version is available to all Nepton customers.
    * Campaign! A 3-month trial period of the Premium version is offered free of charge to Nepton customers. Please contact [Kiva Work sales](<https://kivawork.com/en/about-us/>) to activate. Campaign valid until October 31st, 2023.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/13388325078557>) [ref 13755]


###  __ Improvements
  * #### Improvements to Worktime > Work hours > Events in calendar view
    * The week tables are no longer getting unnecessarily wide when viewing long periods.
    * View now fills the whole browser window horizontally, making the content aligned to the left side.
    * When a long view is scrolled down, a floating "Back to top" button appears.
    * Legend toggle button moved under tools menu.
    * Help embedded to the page added to explain how to add events, view info of a day and what is under tools menu.
[ref 13795] [ref 13800]
  * #### Two new columns added to Visma Fivald CSV salary export
    * Vacation start date
    * Vacation end date
New columns are used for reporting absences to the Incomes Register.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003272618>) [ref 13807]


###  __ Fixes
  * #### The permissions to record "Hour to hour" and "Overtime" is now applied more strictly to the current status page/legacy web terminal, and the InsertActivities+UpdateActivities web services
If the overtime and balance MAX buttons incorrectly disappear from the current status page, please ensure the permission to set overtime and hour to hour is correctly set for each worktime role:
![](https://support.nepton.com/hc/article_attachments/22653735609117)
[ref 13797]
  * #### Worktime calendar's date range picker did not work if it was used on mobile devices
[ref 13796]
  * #### Fixed bug where the "Maximum balance that can be earned per day" setting did not always work correctly with the min/max allowed balance at the beginning of the day
[ref 12226]
  * #### Overtime rounding did not affect calculated on call time
Applies only to overtime rounding, no issues seen with event rounding.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002558557>) [ref 13787]
  * #### Absence type list on worktime event editing view was incorrect in some cases
[ref 13809]
  * #### In some specific cases, Sympa API user import failed without reporting about the problem properly
[ref 13810]
  * #### When permitted work hours came from work shift planning, they were set only based on the first event of the day, even though there were more events planned on the day
[ref 13813]


### 
##  **27/09/2023** release (2.13.22)
###  __ Fixes
  * #### Sign-in with Google works now with the latest version of the Google Chrome browser
[ref 13785]
  * #### Project invoicing report "Paid time off" column was missing in some cases
[ref 11583]


### 
##  **26/09/2023** release (2.13.21)
###  __ New
  * #### Support for paying weekly rest time compensation into balance/accrual
Support for paying weekly rest compensation into a balance/accrual that can be spent later as weekly rest leave.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360007389978-Weekly-rest-time-compensation>) [ref 13695]


###  __ Improvements
  * #### Worktime TES section's setting Work week calculation mode has new setting option "KVTES"
Calculation mode interprets overtime and accruals according to TES Kunta-alan yleinen virka- ja työehtosopimus (KVTES).
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002559438-Additional-work-formation>) [ref 13732]
  * #### IFS work hours export now supports exporting assumed events salary data to IFS
Assumed events are synchronised to IFS when they are approved
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003504177>) [ref 13777]
  * #### Improvements have been made to the Estonian translations
[ref 13747]


###  __ Fixes
  * #### Integration history panel and service log did not display a warning about an export with empty rows in some manual imports
[ref 13609]
  * #### When setting multiple permitted work times or expected work times on a single day, only one of them would be displayed in the calendar pop up menu. This issue has now been fixed.
[ref 13789]
  * #### Visma L7/LTR project import integration via REST API was not functional
    * It was not possible to schedule the integration as the schedule tried to run the import via SFTP
    * All sub numbers from Visma L7/LTR were not imported as projects
[Guidance](<https://support.nepton.com/hc/articles/360003751058>) [ref 13769]
  * #### Levelling period hours were not calculated accurately in planning view, as it only displayed hours for the visible period in the planning calendar
[ref 13781]
  * #### If travel invoice had mandatory fields, they were not clearly indicated when creating new travel invoices
Mandatory comment fields, like daily allowance comment fields, were not properly indicated and highlighted when trying to save travel invoice. Fields were hidden behind collapsed menu item which gave an impression that Save-button didn't work.
[ref 11784]


### 
##  **18/09/2023** release (2.13.20)
###  __ New
  * #### The default language for terminals can also be Swedish or Norwegian.
If necessary, contact Saarni Nepton to get the default languages changed for your working community terminals.
[ref 13684]


###  __ Fix
  * #### Permitted work times issue
Permitted work times based on planned work shifts were set incorrectly in some situations.
[ref 13450]


### 
##  **14/09/2023** release (2.13.19)
###  __ Improvements
  * #### Public holiday settings now include Austrian national day.
Guidance [1](<https://support.nepton.com/hc/en-gb/articles/360002558797-Public-holiday-management>), [2](<https://support.nepton.com/hc/en-gb/articles/360002560677-Configure-exceptions-to-settings>) [ref 13764]
  * #### Worktime > Work hours > Approve project hours:
    * Table outlook is modernized and functionality improved.
    * More detailed information about project related events and hours is highlighted and shown in popup window when table cell is clicked.
    * 0 duration events, such as notes, corrections and supplements, are now also shown in the view.
    * Admin users and supervisors have possibility to directly open events from the view.
[ref 12986]
  * #### Changes to travel invoice approvals:
    * Earlier travel invoices with unapproved projects might have caused notifications about unapproved events before reporting period. They could have been accidentally approved without seeing them. Now the view does not affect travel invoices in any way and their approval is done separately outside of this view.
    * Projects related to travel invoices can be approved only by approving the travel invoice. Approving travel invoice always approves related projects regardless of value in the setting "Approving an event approves all attached projects". Same logic is applied to unapproving.
[ref 12986]
  * #### Possibility to override project type in IFS work hours export.
If a project has an external identifier, by default "Project_sequence" is used as project type in the work entry. Now this can be overridden by setting project type value in IntegrationProjectType field in integration rule
[Guidance](<https://support.nepton.com/hc/articles/360003504177>) [ref 13750]


###  __ Fixes
  * #### Worktime > Work hours > Reports > Event report did not calculate total duration in hours correctly when report was saved as a spreadsheet.
[ref 13771]
  * #### The PIN code bulk generation tool didn't work for customers who had lot of the PIN codes already in use.
[ref 13760]


### 
##  **07/09/2023** release (2.13.18)
###  __ Improvements
  * ####  **On call hours are now visible in work time reports**  
On call hours have been added to the following reports in Worktime > Work hours > Reports:
    * Hours by salary type
    * Hours by event type
#### On call hours have been added to the following reports in Worktime > Projects > Reports:
    * Project hours by salary type
    * Project invoicing report (when reporting by salary type)
    * Project hours by person (when reporting by salary type)
    * Project hours by event type
[Worktime reports](<https://support.nepton.com/hc/fi/articles/360002548557-Tuntiraportit>)  
[Project reporting](<https://support.nepton.com/hc/fi/articles/360002548957-Projektien-raportointi>)  
[ref 13752]
  * #### The integration history panel has been updated. The panel now also displays ruleset name and export period. Data exports made with another username are shown in light grey text.
[ref 13608]


###  __ Fixes
  * #### Various accessibility fixes to Events in calendar -view
    * The notification that appears after approving events was not accessible. It is now accessible.
    * The date picker and the date picker arrows were not accessible to screen readers. They are now accessible.
    * The "Approve" and "Unapprove" buttons have drop down menus and they were not properly accessible to screen readers. This issue has been fixed.
    * The color contrast was quite low. The contrast has been improved.
    * The "Bulk actions" button was not accessible at all, it could not be accessed via keyboard navigation. This issue has been fixed.
    * The search box for selecting a different users calendars made it difficult to navigate the site with a keyboard. This issue has been fixed.
[ref 13716]
  * #### In the planning view of shift planning, it was not possible to display all locations using the filter. When "-" is selected from the dropdown menu, all locations are now displayed.
[ref 13761]


### 
##  **31/08/2023** release (2.13.17)
###  __ Improvements
  * #### Login with Nepton username/email and password can now be disallowed to ensure centralized access management, e.g. if all users are using single sign on.
[Guidance](<https://support.nepton.com/hc/articles/13194036455325>) [ref 12714]
  * #### Login settings have been separated into their own section on the Employees-section administration page.
[Guidance](<https://support.nepton.com/hc/articles/13194906030365>) [ref 12714]
  * #### Weekly rest time support added for KVTES: Earning based on the week day with the least amount of work.
Can be defined by settings in _"Worktime" > "Settings" > "Weekly rest period" > "Compensation when weekly rest period is not met"_ \- section by setting _"How compensation is earned"_ to _"Earned based on worked time"_ and _"If compensation based on worked time" > "Earning period based on"_ to _"Week day with the least work"_.
[ref 13699]
  * #### New Worktime Projects API method EnsureProjectsExistV3 added which allows projects project managers to be updated for a project.
EnsureProjectsExistV3 also supports all capabilities of EnsureProjectsExistV2 API method.
[EnsureProjectsExistV3-method](<https://support.nepton.com/hc/articles/13106403486109>)  
[API-examples](<https://support.nepton.com/hc/articles/360004861578>)  
[ref 13706]
  * #### The projects and notes that appear in the calendar view do not have good visual separation after the 2.13.0 release.
This has been improved by making the project headlines bold.
[ref 13749]


###  __ Fixes
  * #### Overnight work events in some situations were not correctly picked up by on call calculations.
[ref 13727]
  * #### The assumed lunch break used to show both the time and duration, but after the work schedules release it only shows the duration if no specific start time was set for assumed lunch.
This has now been fixed such that both the time and duration is shown.
[ref 13741]


### 
##  **28/08/2023** release (2.13.16)
###  __ Improvements
  * #### New setting option "Earned based on rest deficit" added for weekly rest period in _Worktime > Settings > Weekly rest period > Compensation when weekly rest time is not met > How compensation is earned_
    * With this option selected weekly rest periods can be compensated based on the weekly rest period deficit.
  * #### Some terms and setting for weekly rest period improved.
[ref 13697]
  * #### Weekly rest periods can be configured as number of weeks in _Worktime > Settings > Weekly rest period > Weekly rest period calculations > Number of weeks to check_
    * Number of weeks defaults to 1 if not set.
    * If multiple weeks are checked, "Starting date if multiple weeks checked" needs to have a date set.
    * Change requires no action from customers for existing weekly rest calculations.
[ref 13696]


###  __ Fixes
  * #### An issue that caused some users to see an error in the Current Status view was fixed.
[ref 13737]
  * #### Long expected work times could cause issues with calculating long year leaves and absences.
[ref 13725]


### 
##  **24/08/2023** release (2.13.14)
###  __ Fixes
  * #### Work hours Events in calendar / Events in table. Day or event specific menu popup could sometimes open outside browser's visible area.
[ref 13729]
  * #### In the planning view, the dropdown menu for filtering work schedule locations was not working as expected.
[ref 13734]


### 
##  **23/08/2023** release (2.13.13)
###  __ Improvements
  * #### A new setting in 'supplements' and 'work rises' has been added that makes it easy to enable/disable them. The new setting can be used for example to easily prevent the settings from being inherited from a higher level.
Existing supplements and work rises that were in use before this change are enabled by default and this needs no action from customers
Guidance: [Supplements](<https://support.nepton.com/hc/en-gb/articles/360002559637>), [Work rises](<https://support.nepton.com/hc/en-gb/articles/360002560978>) [ref 13357]
  * #### Work schedules fixes and improvements
    * The missing translation that occurred when removing shifts in shift planning has been added.
    * The brief appearance of a Purple "Deviation" cell during the creation of a new shift in planning, even when filtered for a "normal" planning location, has been addressed.
    * While in bulk actions mode, menus and drop-downs for Alias shifts no longer remain open, because bulk tools cannot interact with alias shifts. Interaction with Alias shifts is now suspended during bulk mode.
    * The issue where selecting a non-work schedule location offered the option to create template shifts has been fixed.
    * Alias and Template shifts added from the planning view will now only be displayed on the day they start.
    * Fine planning now accurately displays shifts. The problem of displaying shifts as overlapping when they are not has been fixed.
    * Work schedule aliases are no longer available for selection in planning if the schema is not published for that period.
    * The error caused by selecting "-" in the planning view, which sometimes created an unusual 00:00 - 00:00 shift, has been fixed. This option has been removed from the planning dropdown.
    * When removing a deviation from shift planning, an empty shift was generated incorrectly. Issue has been fixed and removal now results the shift reverting to the original work schedule shift.
    * Changing an alias back and forth (e.g., A - Y - A) lead to the alias becoming unpublished, even if it was originally published from the schema without changes. Issue has been fixed.
    * Both day and shift level notes from the schema are now correctly displayed in the shift details.
    * Clicking on a date period outside the schema period will no longer result in a pink background and a visible alias dropdown before the general shift template opens.
    * Alias duplication within the same scheduling period is now properly prohibited.
[ref 13668]


###  __ Fixes
  * #### "Special Node 0" is not displayed as user group for users with no user group. Column is now empty in these cases.
[ref 2404]
  * #### When editing the Integration Scheduling setting "Schedule Type" with the validity controls, the dropdown would always contain all possible settings, even if the particular integration did not support that setting. This issue has been fixed.
[ref 13636]
  * #### Start-button is now hidden for assumed lunch breaks in mobile view if lunch break event is not in use in the worktime calendar.
Previously in this scenario Start-button was visible but didn't start the event.
[ref 13724]


### 
##  **15/08/2023** release (2.13.11)
###  __ Improvements
  * #### Improved handling of long continuous shifts in work time calculations.
Long shifts lasting more than two days were treated as one continuous shift. This caused a situation where work hours from the third date of the shift were not calculated at all.
[ref 13622]
  * #### The number of configurable work rises have been increased from 30 to 50.
[ref 13712]


###  __ Fixes
  * #### In the planning view of shift planning, the hours were not calculated correctly if the person had overnight shifts. The bug has been fixed.
[ref 13717]
  * #### "Work hours > TES > Earning percentages by event types" calculation for 0-minute events caused an error.
[ref 13707]
  * #### Work time role access right "Can edit all users dining events" did not give permission to view and edit every person's dining events in Work time Events in calendar view. Viewing and editing dining events in Events in table view worked normally.
[ref 13710]
  * #### Opening calendar from the "Work hours > Approve hours" view and removing an event from the calendar redirected to your own calendar instead of staying in the opened calendar.
[ref 13708]
  * #### Opening "Work hours > Events in calendar" when viewing someone else's calendar opened your own calendar. This concerned situations when the calendar was opened to a new tab.
[ref 13708]


### 
##  **09/08/2023** release (2.13.10)
###  __ Improvements
  * #### In worktime persons can be now searched by employee number.
Employee number is also included in search results. This helps to differentiate employees with the same name.
[ref 13688]


###  __ Fix
  * #### In some cases, when attempting to view another user's calendar in the calendar view (not table view though), the content may fail to load, resulting in a loading spinner that never stops. The issue has been fixed.
[ref 13685]


### 
##  **31/07/2023** release (2.13.9)
###  __ Improvements
  * #### The right to edit own event requests has been split to its own permission, separate from allowing edits to all own personal entries. This enables more restrictive Worktime roles to be configured.
    * New Worktime role permission "Can edit own requests" introduced.
    * All roles with "Can edit own personal entries" permission have been automatically granted the new "Can edit own requests" permission. This is so that there is no change to behaviour unless permissions are edited by customers.
[Worktime roles](<https://support.nepton.com/hc/en-gb/articles/360002554338>) [ref 13462]
  * #### Messaging via event requests is no longer considered an event edit. Therefore messaging is always possible, even after approval and locking.
    * This better reflects real-world situations where discussion is needed about past events.
    * It is planned that all event types will get the messaging feature eventually.
    * The "Can edit own request message" permission is respected and as such, the user must have this permission to add a request message.
[Event requests](<https://support.nepton.com/hc/en-gb/articles/360017787717-Event-requests>) [ref 13462]


###  __ Fix
  * #### Employee number "0" was not correctly showing in worktime calendar.
[ref 13687]


### 
##  **27/07/2023** release (2.13.8)
###  __ New
  * #### Service can be now used also in Norwegian language, excluding terminals.
[ref 13591]


###  __ Fixes
  * #### "Filter to supervisor's subordinates" was missing in work time calendar person selection.
[ref 13674]
  * #### Improved the wording of the last two options for the "Increase accrual in accordance with rate of increase" -work rise setting to better match what the action does.
[ref 12695]
  * #### Opening the editing page for a unapproved multi-day event requests in the past caused excessive notifications by showing the same message for all of the days.
[ref 12684]


### 
##  **27/07/2023** release (2.13.7)
###  __ Fixes
  * #### Employee number of the selected user is now correctly displayed in the calendar view.
[ref 13682]
  * #### Events that span 20+ years can now be deleted without any errors.
[ref 13678]
  * #### Event context menu gave the option to edit the event in some cases when the person did not have rights to edit the event
[ref 13673]
  * #### If a person did not have the rights to edit any data in an event request, opening its details gave an error
[ref 13673]
  * #### Some setting labels for worktime role permission where changed to better reflect what they do.
[ref 10603]


### 
##  **25/07/2023** release (2.13.6)
###  __ Fixes
  * #### Deleting an event in the event editing view now properly shows a loading indicator.
[ref 13107]
  * #### Employee number has been added back to the top of the events in calendar view.
[ref 13675]
  * #### Quick start event could include incorrect project duration in some cases.
[ref 13639]


### 
##  **21/07/2023** release (2.13.5)
###  __ Fixes
  * #### The locations management view was not working for some of our customers.
[ref 13677]


### 
##  **20/07/2023** -release (2.13.4)
###  __ Improvement
  * #### Some Worktime work rise setting labels have been updated to better reflect what they do
[ref 12419]


###  __ Fixes
  * #### The Nepton Payroll manual integration will no longer return a ZIP-file if the total file size of the export exceeds 0.5MB
It will only return a ZIP-file if there are multiple export files.
[ref 13659]
  * #### In some cases, Nepton Payroll didn't synchronize recorded annual leave correctly
[ref 13660]
  * #### Custom shifts from planning are now marked as deviations in worktime calendar and mobile view if they override work schedule shift
[ref 13662]
  * #### Styling was missing for the buttons in the approve hours view
[ref 13665]
  * #### Editing of the work schedules related to locations removed from locations management
Editing of the work schedules related to locations could cause problems in planning, and thus the editing possibilities were restricted.
[ref 13666]
  * #### On call hours were not calculated correctly if the hours of an overlapping work event were rounded
[ref 13658]


### 
##  **13/07/2023** -release (2.13.3)
###  __ Fixes
  * #### In planning, planning hour targets based on persons weekly hours were miscalculated as too high.
[ref 13664]
  * #### Missing work schedule saving validation
Changing a code of the work schedule should have only update the projects code related to the works schedule, but it did create a new project with the new code instead.
Check for if the work schedule code was already in use was missing.
[ref 13663]


### 
##  **10/07/2023** -release (2.13.1 & 2.13.2)
###  __ Fix
  * #### Error in the calendar view
The calendar view gave an error when the selected person and time period contained a travel invoice


### 
##  **08/07/2023** release (2.13.0) \- Work Schedules
###  __ New
  * #### New Work Schedules feature available in Planning on Complete service level
Work Schedules make shift planning easy. Work shifts and holidays can be planned quickly for the entire year. Work schedules are based on work schedule groups with employees. The groups follow customized shift patterns.
Shifts can be easily modified and commented. Modified shifts are shown on purple highlight color in the worktime calendar which makes them easy to notice. Employees will always have a clear picture about their upcoming shifts.
Want to see Work Schedules in action? [See recording (in Finnish)](<https://nepton.fi/yleinen/katso-tallenne-nepton-news-vuorokalenterit/>) about Work Schedules.


###  __ Improvements
  * #### Worktime calendar appearance update
Updated worktime calendar view is clearer and lighter. Appearance of multiple elements has been updated.
Calendar date range is now selected by clicking the date range on upper part of the calendar. After that date range can be modified. Print and Calendar syncing can be found behind Tools-menu.
Calendar event appearance has been updated with following colors:
    * Assumed event: Grey
    * Approved event: Green
    * Exceptional event: Yellow
    * Work schedule deviation: Purple
Events can be created by clicking date and by selecting “Add event”. Other sections also have small changes in appearance.
  * #### Changed how event imports set event beginning and ending times when the import data defines only the date where to import an event.
This fix gives better support in cases where absences take place in night time.
[Guidance](<https://support.nepton.com/hc/articles/360003773337>) [ref 13426]


###  __ Fixes
  * #### When using a terminal to create/edit a shift, overtime target behavior was incorrect in some cases.
Even though overtime target was correct in settings, service did not calculate the overtime correctly until the event was manually edited in desktop view.
[ref 12187]
  * #### When running an ’Hours by period’-project report, the service gave an error message when period selection was ’Monthly on same weekday’. The issue has been fixed.
[ref 12006]


### 
##  **06/07/2023** release (2.12.18)
###  __ Improvement
  * #### Work rise settings are now collapsible making their controlling more user friendly.
[Guidance](<https://support.nepton.com/hc/articles/360002560978>) [ref 13623]


###  __ Fixes
  * #### Some Worktime projects setting labels have been updated to better reflect what they do.
[Guidance](<https://support.nepton.com/hc/articles/360002562658>) [ref 6674]
  * #### If integration created a single file bigger than 0.5MB, file was automatically zipped in API calls that ran the integration and in service log.
This happened after the release of version 2.12.13 but has now been reverted. In future, single files will always be provided in the intended format.
[ref 13656]
  * #### 'Minimum work time before lunch is assumed' setting did not work correctly in certain situations.
[ref 13655]


### 
##  **05/07/2023** release (2.12.17)
###  __ Fixes
  * #### The Lemonsoft work hours integration incorrectly rounded work hours to a single decimal place. It now correctly rounds to two decimal places for the greater accuracy Lemonsoft supports.
[ref 13654]
  * #### Worktime realised work hours report could show accruals data in the incorrect column.
[ref 13649]


### 
##  **03/07/2023** release (2.12.15 & 2.12.16)
###  __ Fixes
  * #### The Worktime validity setting calendar was sometimes off-screen.
[ref 13635]
  * #### Some data columns in the "Realized Work Hours" report were under the wrong headers.
[ref 13647]
  * #### Project hierarchy for selected projects did not display selected child projects correctly in person or person group projects when their parent level was selected.
[ref 13645]


### 
##  **28/06/2023** release (2.12.14)
###  __ Improvements
  * #### Report names in Worktime > Projects > Reports have been clarified.
[Guidance](<https://support.nepton.com/hc/articles/360002548957>) [ref 13638]
  * #### Employee number, person goup name and additional reporting info - columns were added in Worktime reports where they were missing.
[Guidance](<https://support.nepton.com/hc/sections/360005870318>) [ref 10073]


###  __ Fixes
  * #### Some scheduled integrations start date settings with rules like "First of January" did not work correctly.
Issue has been fixed.
[ref 13642]
  * #### Project hours by event type -report did not load correctly when time allocated for projects was over the recorded event duration and event type was sick leave.
[ref 13638]
  * #### Unified the Project hours by event type -report to display time allocated for projects that is over the recorded event's duration in the same way for work, absences and sick leave.
Earlier absences showed only time allocated to projects that matched the recorded event's duration.
[ref 13638]


### 
##  **26/06/2023** release (2.12.13)
###  __ Improvement
  * #### New Worktime setting "Export files as zip" added. Setting defines whether salary data that is split to several files will export the files to SFTP server as a single zip file or unzipped individual files.
    * For existing customers the setting is on and files will be exported as a zip file.
    * For new customers the setting is off and files will be exported as unzipped individual files by default.
[Guidance](<https://support.nepton.com/hc/articles/360006255458>) [ref 13567]


###  __ Fix
  * #### Worktime > List projects -page generated an error when imported projects did not have a name set correctly.
Problem has been fixed. List projects -page opens now even if one of the project names is not correct.
[ref 13629]


### 
##  **19/06/2023** release (2.12.12)
###  __ Fixes
  * #### Assumed lunch breaks function and on call did not work correctly together in certain situations.
[ref 13619]
  * #### Integration rule testing and development tool did not always show results correctly when testing fetching of data from other persons than the authenticated person.
[ref 13610]
  * #### A supplement that was no more active was not available for editing an activity in a period when the supplement was active.
[ref 13585]
  * #### When a person had a travel invoice open for editing, and a supervisor approved the travel invoice at the same time, an error occurred when travel invoice was saved.
This happened because the person didn't have access to edit an approved travel invoice anymore. In this situation a message is now shown that there is no access to edit the travel invoice.
[ref 12906]


### 
##  **14/06/2023** release (2.12.11)
###  __ Improvements
  * #### It could take up to a minute for a manually started integration to run. The delay has been fixed and the runs now start faster.
[ref 13605]


###  __ Fixes
  * #### Internal id was shown in the code column for Event types under Person settings. Now the event type code is shown like in Working community settings.
[ref 5294]
  * #### In some rare cases a decimal value could get rounded wrong in an Personec F integration file.
[ref 13616]


### 
##  **12/06/2023** release (2.12.10)
###  __ Improvement
  * #### Improved the readability of Realized Work hours by moving the summary columns to the beginning of the report.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360016836978-Realized-work-hours>) [ref 13502]


###  __ Change
  * #### Changed the format of accruals for Realized Work Hours and Hours by salary type to be a decimal number.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360016836978-Realized-work-hours>) [ref 13502]


###  __ Fixes
  * #### The 'Sympa Absence import' integration setting 'Import event times' is no longer ignored.
[ref 13611]
  * #### Prevented users with an integration ID of "0" being synchronised to IFS and other real-time salary integrations.
[ref 13601]


### 
##  **07/06/2023** release (2.12.9)
###  __ Fix
  * #### Nepton Payroll and IFS synchronization resulted in an error when editing an event more than a week in the future
[ref 13600]


### 
##  **06/06/2023** release (2.12.8)
###  __ New
  * #### Added new setting for the 'Sympa Absence import' integration 'Import event times'. This enables importing of the start and end times of absences.
#### Removed setting 'Import duration' from the 'Sympa Absence import' integration. This setting has been replaced by the setting mentioned previously.
#### The change does not affect existing integrations.
[Guidance](<https://support.nepton.com/hc/articles/360003736798>) [ref 13501]


###  __ Improvements
  * #### Added support for re-running integrations that import multiple files.
[ref 13555]


###  __ Fixes
  * #### Preview mode did not work correctly when running integrations manually.
[ref 13576]
  * #### After the release done on 13.5. setting group settings for integrations were not always saved correctly when saving the setting with validity control.
[ref 13578]
  * #### Setting API key on setting group level for IFS integrations did not work correctly.
[ref 13577]
  * #### Adding new columns in Worktime > Administration > Integration > Event import settings did not work.
[ref 13579]
  * #### Nepton Payroll did not always synchronize enough data when editing an event of a person who does not accrue balance.
[ref 13594]
  * #### Files formed by SD Worx (Työ) - integrations (previously Personec W in Nepton) were served by default with .dat file extension when the correct file extension is .csv.
[ref 13580]
  * #### Clicking on "Select All" was not resulting in all payment groups getting selected, issue has been fixed.
[ref 13371]


### 
##  **02/06/2023** release (2.12.7)
###  __ Changes
  * #### Nepton SSO Service Provider certificate update
[ref 8037]


### 
##  **29/05/2023** release (2.12.6)
###  __ New
  * #### Salary data export - Visma LTR
Sending salary data to Visma LTR from Nepton is now possible. Export can now be configured in a ruleset where Nepton sends data to LTR via LTR REST API.
[Guidance](<https://support.nepton.com/hc/articles/11166111654685>) [ref 13393]


###  __ Improvements
  * #### IFS Activity approval integration now supports apikey authentication.
[ref 13519]
  * #### The next upcoming/scheduled job is now shown in the schedule history table in Worktime > Administration > Working community settings > Integrations > Integration scheduling.
[ref 13539]


###  __ Fixes
  * #### Parsing spreadsheets in the system did not correctly support csv-files that had .txt file extension.
[ref 13555]
  * #### Elisa Ring integration was not running correctly after the release done in 13.5.
[ref 13571]
  * #### Some salary export files downloaded from service log that should have been in .dat format were in .txt format.
[ref 13570]
  * #### Export files from Personec F-integration missed data that was set in Personec F settings.
[ref 13562]


### 
##  **23/05/2023** release (2.12.5)
###  __ Improvements
  * #### If an integration would be running during a possible maintenance window, it will wait for the maintenance window to end before running, which is displayed in the integrations scheduling view
Integration will run after maintenance window has closed. Read more about maintenance windows from [Platform status - page](<https://support.nepton.com/hc/articles/360006554777>).
[Guidance](<https://support.nepton.com/hc/articles/10510800700573>) [ref 13539]
  * #### Person's HR role can be changed without affecting person's Priima Learning Management -role. The learning management role can be defined separately. [ref 13531]


###  __ Fixes
  * #### Sympa absence import did not import sick leave events correctly if a sick leave with different absence code with same begin and start time existed in Nepton
[ref 13479]
  * #### In Administration > Integrations, CGI Sonet short interface and CGI Sonet parameterised interface buttons were mixed up
This occurred after release done on 13.5. which resulted on short interface getting run when parameterised interface was clicked and vice versa.
[ref 13548]
  * #### Old Visma L7 project import integration did not support txt file format after release done on 13.5.
Support for txt file format has been added back to the integration.


### 
##  **17/05/2023** release (2.12.3 & 2.12.4)
###  __ Fix
  * #### Saving the person's information in the user info page caused an error message if the employment end date field was left blank. Issue has been fixed.
[ref 13546]


### 
##  **16/05/2023** release (2.12.2)
###  __ Fixes
  * #### Manually run exports did not always include data from all persons. The issue has now been fixed
Manual exports that have potentially ran into issues have been flagged as failed runs, and should be ran again to export data correctly
[ref 13540]


  * #### Visma Fivaldi salary integration was not visible in the list of integrations that can be run manually in Worktime > Administration > Integrations
[ref 13541]


  * #### IFS Activity integration was not syncing correctly after the release of Nepton version 2.12.0 done on 13.5.
Issue has been fixed, but any approvals done between 00:00 13.5. - 13:00 16.5. 2023 need to be done again so that they will be synchronized correctly to IFS
[ref 13542]


### 
##  **15/05/2023** release (2.12.1)
###  __ Fix
  * #### Service provided incorrect direct login links for Microsoft login under Employees > Administration > Single sign-on (SSO) > Microsoft login > Direct login link.
Please provide new updated links for your employees.
[ref 13528]


### 
##  **13/05/2023** release (2.12.0)
###  __ New
  * It is now possible to schedule a specific time when the worktime export or import integration runs. Previously, the time was fixed. Thanks to the new ability it is possible for example to tansfer work time information to another system or via email at the desired time. After the release the old integrations will continue to function as before if changes are not made to them.
[Guidance](<https://support.nepton.com/hc/articles/10510800700573>) [ref 5430, 12854]
  * In the work time section you can now create custom exports where you can select the desired columns for the spreadsheet export. You can export the spreadsheet right into the desired e-mail address. Now for example work time information can be delivered easily to third parties while taking data protection into account. Only information relevant to the recipient can be selected for the spreadsheet and delivered to them by e-mail at the desired time.
[Guidance](<https://support.nepton.com/hc/articles/10758741671581>) [ref 12913]
  * Identification information of the terminals is now imported into Nepton. Identification information can be used with integrations and dining and event reports, which makes it possible to track which terminal a person has used. New information can also be used for example in rulesets. The identification information can also be used for creating a meal report from which you can identify which restaurant the dining took place. The report can be delivered by e-mail to the [restaurant staff or other third parties](<https://support.nepton.com/hc/en-gb/articles/360002548278>).
[ref 13454]
  * A new function has been added to Nepton's Employees section and with it employer information can be added to the system. Employers can be defined for persons. This information can be used to control for example the integrations.
[Guidance](<https://support.nepton.com/hc/articles/10847746064797>) [ref 13401]


###  __ Improvements
  * The on-call event now behaves more predictably and logically. Previously, the on-call event did not correspond to the actual use. Event type behavior, calculations and settings have been improved. The event now better supports collective agreements and local agreements.
    * When work is started during on-call on a terminal or in the Nepton service, the on-call now continues in the background until the predefined end time.
    * With the new settings, it can be defined whether an event made during on-call constitutes on-call compensation. This selection can be made per event type.
    * With the new settings, it is possible to define whether the amount of on-call compensation is shown in the person's worktime calendar.
    * In addition, the on-call compensation that is formed can be used in salary integration.
[Guidance](<https://support.nepton.com/hc/fi/articles/8040695057821>) [ref 12183]
  * Nepton can be integrated to several different services. Outdated service names have now been updated to up-to-date ones in Nepton's user interface. The changes made are specified in [the guidance](<https://support.nepton.com/hc/fi/articles/360002494538-Vakioidut-liittym%C3%A4t>).
[Guidance](<https://support.nepton.com/hc/fi/articles/360002494538-Vakioidut-liittym%C3%A4t>) [ref 7209]
  * The selections for the shift planning copy function have been clarified.
[Guidance](<https://support.nepton.com/hc/articles/9892247685917>) [ref 13405]


##  **11/05/2023** release (2.11.42)
###  __ Improvement
  * #### Improved the performance of exporting personnel data to Excel from the Employees section
[Guidance](<https://support.nepton.com/hc/articles/360002430478>) [ref 13518]


###  __ Fix
  * #### Correction to HR data sync behaviour for trusted services (Priima & Nepton Payroll)
    * The problem was that information was being sent more times than necessary. This did not impact security
    * The change is transparent to customers and requires no action
[ref 13510, 13213]


##  **09/05/2023** release (2.11.41)
###  __ Fixes
  * #### A public holiday event could cause errors in calculations on a single day after the public holiday.
[ref 13512]
  * #### Improved service performance in the export of person data to Excel.
[Guidance](<https://support.nepton.com/hc/articles/360002430478>) [ref 13518]


##  **03/05/2023** release (2.11.38 - 2.11.39)
###  __ Improvements
  * #### Worktime setting group and work time percentage fields in person's information form can be filled from work contract
[ref 13446]


  * #### Performance improvements to user information handling in Worktime
[ref 13448]


###  __ Fixes
  * #### Publishing shifts to locked calendar was failing. Now publishing to locked calendars has been made possible
[ref 13372]


##  **26/04/2023** release (2.11.37)
###  __ New
  * #### Priima learning management system is now part of Nepton and available for all customers
[Learn more here (Finnish)](<https://store.priimalms.com/priima-neptonin-asiakkaille/>)
[Guidance (Finnish)](<https://support.nepton.com/hc/articles/10402517130653>) [ref 12979]


##  **24/04/2023** & **25/04/2023** releases (2.11.34 - 2.11.36)
###  __ Changes
  * #### Added technical settings for joining Priima into Nepton.
Priima learning management system will become available for all Nepton customers on 26/04.
[ref 12979]


##  **24/04/2023** release (2.11.33)
###  __ New
  * #### Added technical capabilities for joining Priima into Nepton and performing necessary data synchronizations.
Priima learning management system will become available for all Nepton customers on 26/04.
[ref 12979]


###  __ Improvement
  * #### Direct Microsoft login link can now be used even if customer has multiple Microsoft logins.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002590137>) [ref 13447]


###  __ Fix
  * #### When the public info from a workshift contained multiple lines, worktime event description displayed extra "br" texts.
[ref 12820]


##  **12/04/2023** release (2.11.32)
###  __ Fixes
  * #### Multiple translation corrections.
[ref 12026, 12146]
  * #### Performance improvement for mass approvals when using Nepton Payroll service.
    * Optimised the transfer of salary data to the Payroll provider.
[ref 13440]
  * #### Correction to rounding logic behind Total hours calculated from decimal work hour amounts in, Project hours by period, Realized work hours, and Hours by salary type, reports.
    * The previous approach could lead to confusing results as the rounding was applied incorrectly.
[ref 13443]
  * #### When creating or approving event requests the calculated balance could be too large for part-time employees in some cases.
[ref 13453]
  * #### Customers with multiple salary data exports scheduled could encounter failures like "SFTP operation failed ... file size mismatch for '/tmp/", due to conflicting temporary file names.
    * This fix ensures temporary file names are always unique and therefore the issue is avoided.
    * No action is needed by customers.
[ref 13458]


##  **30/03/2023** release (2.11.31)
###  __ Fix
  * #### A problem with some settings prevented use of the login page.


##  **30/03/2023** release (2.11.30)
###  __ Improvements
  * #### It is now possible to override the data in all of the columns in EmCe salary export using rules defined in an integration ruleset.
[Guidance (in Finnish)](<https://support.nepton.com/hc/fi/articles/360019119337>) [ref 13445]
  * #### It is now possible to override the data in all of the columns in Visma Fivaldi CSV salary export using rules defined in an integration ruleset.
[Guidance (in Finnish)](<https://support.nepton.com/hc/fi/articles/360003272618>) [ref 12155]


###  __ Change
  * #### Login with Google credentials has been upgraded to use the latest Sign in with Google functionality supported by Google.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360016713117>) [ref 13342]


###  __ Fixes
  * #### Fixes for the EmCe salary export
    * There was currency amount in a wrong column.
    * The following missing columns have been added: 
      * Earning period start date, column O
      * Earning period end date, column P
      * Absence start date, column Q
      * Absence end date, column R
[Guidance (in Finnish)](<https://support.nepton.com/hc/fi/articles/360019119337>) [ref 13445]
  * #### It was not possible to clear event notes in Visma Fivaldi CSV salary export.
[Guidance (in Finnish)](<https://support.nepton.com/hc/fi/articles/360003272618>) [ref 12155]


##  **27/03/2023** release (2.11.29)
###  __ Improvements
  * #### Manual person data imports can now also be done using JSON data via Employees > Persons > Import persons
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003762577>)  
[ref 13425]
  * #### Sympa absence import can now import absences with exact durations - Previously only full days were possible
    * Precise absence durations can be defined by the new optional "Partial day absence length in hours" column.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003736798>)  
[ref 13436]


###  __ Fixes
  * #### To support the correct earning of overtime for 'Collective labour agreement of salaried employees in the real estate sector', new settings have been added.
    * The new settings are available at Working community and setting group levels under, Worktime > Administration > "Settings" > Work hours > TES > Collective labour agreement for the salaried employees in the real estate sector
[Guidance (FIN)](<https://support.nepton.com/hc/en-gb/articles/360005058217>)  
[ref 13437]
  * #### Work time setting "Allow earning hour to hour overtime from sick leave" in Work hours > Accruals and overtime hours didn't work in all cases
[ref 13444]


##  **20/03/2023** release (2.11.28)
###  __ Fixes
  * #### Removed setting group basic template duplicates
[ref 13433]
  * #### An error occurred when trying to mass enter permitted or expected work times
[ref 13435]


##  **13/03/2023** release (2.11.27)
###  __ Fixes
  * #### Weekly leave events could prevent the "Borrow at the end of the week if weekly obligation not fulfilled" setting from reducing balance correctly at the end of the work week.
[ref 13427]


  * #### Accrual leave hours recorded outside of a work shift or expected work times did not accumulate hours correctly (e.g. towards bank leave).
[ref 13423]
  * #### Work shift records that are zero minutes long incorrectly impacted calculations of travel time and absences.
[ref 13423]


##  **09/03/2023** release (2.11.26)
###  __ Fixes
  * #### In planning, having weekly hours defined only for part of the planning period caused an error
[ref 13383]
  * #### A recent change to project handling caused newly created units and locations to be hidden from recording terminals by default
    * The visibility of affected units and locations has been corrected - no action is needed from customers
    * All project types can now be shown or hidden from recording terminals, using the related project settings found under, Worktime > Projects
[Add project](<https://support.nepton.com/hc/articles/360002560877>)  
[Project management](<https://support.nepton.com/hc/articles/360002561017>)  
[Managing locations](<https://support.nepton.com/hc/articles/360005539397>)  
[ref 13376]
  * #### Editing projects of selected events did not work in all cases
[ref 13418]
  * #### In the Employees section, Persons' additional fields which were flagged as mandatory, were not adequately enforced when making edits on a Person's information pages
[ref 13390]


##  **09/03/2023** release (2.11.25)
###  __ Fixes
  * #### Projects were not correctly updated when being moved/edited to having no parent projects in the hierarchy.
[ref 13407]
  * #### SFTP file transfers timeout increased to 120 seconds.
[ref 13139]


##  **06/03/2023** release (2.11.24)
###  __ Fixes
  * #### Quick start events were not available for users who only had permissions to record real-time events.
[ Quick start events](<https://support.nepton.com/hc/en-gb/articles/7074461491101>)  
[Add an event using Nepton mobile](<https://support.nepton.com/hc/en-gb/articles/360002602638>)  

[13363]
  * #### SFTP file transfers could occasionally fail with the following error message in the service log "Unexpected error, the service provider has been informed. (ecode: 0)".
[ref 13139]


##  **02/03/2023** release (2.11.23)
###  __ Fix
  * #### Project hours approval did not display project hours to approve
[ref 13416]


##  **01/03/2023** release (2.11.22)
###  __ Fixes
  * #### Planning did not correctly show similar needs that had been grouped, in the editing pop-up. This made editing the needs very difficult.
[ref 12810]
  * #### Some setting options in Worktime section did not have translations.
[ref 13411]
  * #### Previously set setting values were not always visible in Worktime setting group settings after yesterday's hotfix release. This has been fixed and requires no action from users.


##  **28/02/2023** release (2.11.21)
###  __ Improvements
  * #### Performance improvements related to login
[ref 13305]
  * #### Added support for scheduled import of projects from the new Visma L7 REST API. This is now the preferred method of project import from Visma.
    * Updated the old Visma project import which uses SFTP, to generate project external IDs like the new import via REST API - No action is needed from customers.
    * **Important note!** When switching from using the Visma SFTP project import, to the new approach via REST API, please first confirm that the old SFTP import has been run at least once to generate external identifiers which are required for the new approach.
[Guidance (FIN)](<https://support.nepton.com/hc/fi/articles/360003751058>) [ref 11616]
  * #### Public holidays can now be configured to reduce the maximum weekly obligation by a 5th, as required by some TES.
    * When using this option every public holiday that shortens the work week, shortens the maximum weekly obligation by a 5th of its total value.
    * See the new setting under Worktime > Administration > Working community / Setting group settings > Work hours > Public holidays - Setting "Public holidays shortens work week by" and the new option "Max weekly obligation".
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002558797-Public-holiday-management%20>) [ref 11596]


###  __ Fix
  * #### In Worktime > Administration > Setting groups. Selecting the action 'setting group settings', was blocking the selection of another action until all the topics on the page were loaded.
[ref 12765]


##  **20/02/2023** release (2.11.20)
###  __ Improvements
  * #### Performance improvements
[ref 13304, 13309]


###  __ Fixes
  * #### Setting handling was incorrect on some terminal devices. Affected terminals will be automatically updated with this fix.
[ref 12866]
  * #### In deployments using Nepton Payroll; The "All payslips" link in the Worktime calendar would not work for supervisors.
[ref 13036]
  * #### Persons' absences (e.g. annual leaves) were in some cases incorrectly calculated in workshift planning when there was a public holiday during the absence.
[ref 13284]
  * #### Worktime > Work hours > Reports > Realized work hours report, produced an error when no working days were selected
End users are now informed if they need to revise their reporting choices
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360016836978>) [ref 13339]
  * #### Problems with the Planning > Bulk actions
    * "Copy also to weekends" did not work correctly
    * Validation has been added to prevent incorrect or missing dates
    * Overnight shifts could not be selected for bulk actions
    * Copy to unpaid public holidays should not have been affected by the copy option "Copy also to public holidays".
[ref 13374]
  * #### Payslips were not visible to all roles who should have seen the payslips
[ref 13384]


##  **13/02/2023** release (2.11.19)
###  __ Fixes
  * #### Projects were not ordered correctly when project name was prefixed with project code
[ref 13358]


##  **09/02/2023** release (2.11.18)
###  __ Changes
  * #### Absence details hidden in workshift planning
    * Events for Absence types are only shown as "Absence" in workshift planning.
    * Event notes are not shown in planning for absence types or health care, union steward work or health and safety work types.
[Guidance](<https://support.nepton.com/hc/fi/articles/360010081678#360010081678-toc-5>)  
[Event types](<https://support.nepton.com/hc/articles/360002520778>)  
[ref 13367]


##  **07/02/2023** release (2.11.17)
###  __ Improvements
  * #### Use of the Worktime API now appears in the Service log for review and troubleshooting (Employees > Administration > Service log).
[ref 13352]
  * #### Worktime reports, project and person selections, are now updated whenever the reported date range is changed
    * This is to ensure relevant data and prevent confusion with reporting results
[ref 13175]


###  __ Fixes
  * #### When starting a planned work shift via mobile, the default "Work" event type would be used, regardless of the event type chosen by the user.
[ref 12983]
  * #### The default "Work" event type could be started even if it had been hidden via Worktime event type settings
[ref 12983]
  * #### Printout for "Work shift list per hour" and "Work shift list per day" reports was empty
[ref 13356]
  * #### Login didn't work for usernames with apostrophes (')
[ref 13364]


##  **26/01/2023** release (2.11.16)
###  __ Improvements
  * #### Improvements in changing Worktime role name
    * You can now change the name of the "Kaikki oikeudet" (All rights) worktime role
    * You can no longer give a worktime role a name that is used by another role
[ref 13203]
  * #### Optimisation of user data requests and user selection controls in Worktime
[ref 13318]


###  __ Fixes
  * #### Creating a new event type with temporary lay-off behavior didn't copy the default compensation to the new event type
[ref 13192]
  * #### Person selection in Worktime reports when grouping by setting group did not work correctly
[ref 11338]
  * #### In Worktime > Projects > Reports - section, user list did not always load when project manager proceeded to project and user selection with 'Managed projects' option selected and there were no persons with marked time against projects
[ref 13340]
  * #### Fetching events for Titania via web service returned an error when requesting data with an empty personnel number
[Guidance](<https://support.nepton.com/hc/articles/360008827678/>) [ref 13347]
  * #### Clarified event approval settings and ensured they work correctly
[Guidance](<https://support.nepton.com/hc/articles/360005378238>) [ref 13159]
  * #### If editing an event removed the approval of other events, it also removed the approval of event requests
    * Fixed so that event request approval will remain in these situations
[ref 13177]
  * #### Filtering persons to subordinates wasn't working correctly in worktime reports and mass set event locking dates person selection
[ref 11587, 13345]
  * #### Person selection in calendar view did not load correctly for some users
[ref 13355]


##  **19/01/2023** release (2.11.15)
###  __ Improvements
  * #### Optimisation of user data requests and user selection controls in Worktime
[ref 13318]


  * #### Performance improvements to project handling
[ref 13321]


  * #### Loading the pending project approvals "pip" is now significantly faster.
[ref 13322]


###  __ Fixes
  * #### Project import did not always update imported project correctly
Import did not update a project when only its parent project, project type name or show in terminals - fields were changed
If imported project was set to not be shown in terminals, it did not update correctly
[Guidance](<https://support.nepton.com/hc/articles/360003737078/>) [ref 13331]


  * #### Mepco salary export did not always include persons user setting group code correctly
[ref 13337]


  * #### In the work shift planing, the task name was inaccurately listed in the location table
[ref 13338]


  * #### In the work shift planing, using bulk actions to edit the shifts resulted in duplication of the shifts in the work-time calendar after publishing it
[ref 13341]


##  **17/01/2023** release (2.11.14)
###  __ Fixes
  * #### Addressed some problems related to person import:
    * Unit name or code is now accepted even if upper case or lower case letters are not matching the casing in the unit in Nepton.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360015933397-Person-import-fields>) [ref 13334]
    * Improved reliability of the SFTP connection in person imports.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489357-Scheduled-task-person-export>) [ref 13336]


##  **16/01/2023** release (2.11.13)
###  __ Improvements
  * #### Performance improvements to user information handling in Worktime
[ref 13260]


###  __ Fixes
  * #### Planning > Bulk selection of unpublished shifts/needs, incorrectly included published shifts/needs.
[ref 13325]


  * #### A problem in person imports prevented some imports to work. Delayed imports were re-run after the release of this fix. The re-run synchronized the person data to be up to date.
[ref 13332]


##  **13/01/2023** release (2.11.12)
###  __ Fixes
  * #### Person import did not work in some situations if the password field was included in the import file
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360015933397>) [ref 13324]
  * #### Grouping persons by setting group in person selection did not work correctly
[ref 13319]


##  **12/01/2023** release (2.11.11)
###  __ Improvements
  * #### General performance improvements
[ref 13300, 13304, 13297, 13310]


###  __ Fixes
  * #### Some new Nepton Touch terminals had activation issues which are now fixed
[ref 13295]
  * #### Visma L7 project import resulted in an error in cases where import set project managers for projects as well
[ref 13280]
  * #### It was not possible to set a setting value for "Default event type when creating a new event" and "Assumed event type on empty work days" settings.
[ref 13317]
  * #### The project listing under project reports did not display all available project options in certain cases
[ref 13315]


##  **10/01/2023** release (2.11.10)
###  __ Improvements
  * #### General performance improvements
[ref 13291, 13313]


###  __ Fix
  * #### Event import did not import overnight events end time correctly when end time and end date were set in their own columns
[Guidance](<https://support.nepton.com/hc/articles/360002868137>) [ref 13298]


##  **05/01/2023** release (2.11.9)
###  __ Improvements
  * #### General performance improvements
[ref 13285, 9221]


##  **04/01/2023** release (2.11.8)
###  __ Fix
  * #### Worktime event import could skip the first day of data when "import events from date" option was set.
[Guidance](<https://support.nepton.com/hc/articles/360002868137>) [ref 12999]


##  **03/01/2023** release (2.11.7)
###  __ New
  * #### New worktime setting rules for targeting week numbers
    * Odd week numbers: [ODD-WEEK-NUMBERS]
    * Even week numbers: [EVEN-WEEK-NUMBERS]
    * Specific week numbers: [WEEK-NUMBERS|1|2|18|52]
[Guidance](<https://support.nepton.com/hc/articles/360002560677>) [ref 13235]


###  __ Improvements
  * #### Several performance improvements to the service
    * Project handling improvements
    * Event supplement handling improvements
    * Event attachment handling improvements
    * Person information handling improvements
[ref 13282, 13247, 13254, 13258]


##  **02/01/2023** release (2.11.6.1)
###  __ Fix
  * #### Adding travel invoices caused an error message.
[ref 13281]


##  **31/12/2022** release (2.11.6)
###  __ Improvements
  * #### Performance improvements


##  **30/12/2022** release (2.11.5)
###  __ Improvements
  * #### Several performance improvements to the service.
[ref 13269, 13275, 13277]


###  __ Fixes
  * #### Percentage character (%) in project search caused an error.
[ref 13274]
  * #### A problem in an old API prevented use of Nepton HR API for importing persons for some implementations.
We recommend using only the documented public web service methods.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360004855857-HR-API-general-description>) [ref 13278]
  * #### Validation could fail when having generated a PIN code for a person and saving.
[Guidance](<https://support.nepton.com/hc/articles/360002430798>) [ref 13279]


##  **30/12/2022** release (2.11.4)
###  __ Fixes
  * #### A problem in person listing "Persons supervisor" filter selection prevented use of Employees section for some users in Administrator role.
[ref 13270]


##  **29/12/2022** release (2.11.3)
###  __ Improvement
  * #### Performance in many features in the Worktime section has been improved.
[ref 13267]


###  __ Fix
  * #### A search problem prevented use of Employees section for some users in Administrator role.
[ref 13270]


##  **28/12/2022** release (2.11.2)
###  __ Improvements
  * #### Performance improvements
[ref 9222]


###  __ Fixes
  * #### Mobile calendar could show project duration of 00:00 regardless of the actual project duration.
[ref 13242]


  * #### Long texts in shifts caused usability problems in the work shift planning view.
[ref 13265]


##  **27/12/2022** release (2.11.1)
###  __ Improvements
  * #### Text fixes for work shift planning
[ref 13135]


###  __ Fixes
  * #### Shift made for deleted user caused an error in work shift planning
[ref 13135]


##  **27/12/2022** release (2.11.0) \- Planning usability & Performance
###  __ New
  * #### 2023 Nepton Touch terminal hardware
An updated version of the Nepton touch terminals hardware is now available. A sleek design, modern OS, more processing power, and a more flexible onboard reader, make this our most secure and capable terminal to date.
This device supersedes previous Idesco and Nepton touch models. It will be used in all new orders and when replacements are needed.
[Terminal types & information](<https://support.nepton.com/hc/en-gb/articles/360003685277-Terminal-Types>)
  * #### Quick help
A new in-platform help tool that will get you started on new features, inform you about important changes, answer daily use questions, and get you the help you need quicker than ever.
This new feature will debut in the Planning section and gradually roll out elsewhere as we modernise our user interface. Find it in the bottom right corner on supported pages.
[How to get help](<https://support.nepton.com/hc/en-gb/articles/8037285675677>)


###  __ Improvements
  * #### Planning usability
The planning view has been modernised, including many quality-of-life improvements and new features to improve efficiency
    * **New look and feel** \- Much of the planning section has been updated to modern styles. Easier to navigate, and more space for your work, we hope you love it as much as we do! Work will continue on this topic in future versions, for planning and also other sections.
    * **Bulk actions** \- Get your planning done quicker and easier than ever. Edit, Copy, Move and Delete your way to victory, hundreds of shifts at a time. Is someone sick and you need to reassign all their shifts to someone else? It's now only a few clicks!
    * **Right-click context menu** \- That's right, your mouse has two buttons (maybe even more)! Right-click to get the full information about a shift and quick actions on it, including delete. This lets you reduce the information you load into the view and free up space to see more of your plan.
    * **Quick assign** \- A shortcut instead of the full-blown bulk actions menu, switch into assignment mode by hovering the mouse over a person's name and clicking the new button. Pick the shifts and needs you want to assign them and save.
    * **Identify planning problems** \- Planning problems found in the selected date range are now highlighted at the top of the view. Click to expand and jump to each problem for quick solving.
    * **Maximise** \- Found in the top right of the planning view, a new legend, and the option to toggle expanding the planning view to fill your whole screen.
    * **Removed planning hours/day view** \- We have decided to remove this feature as it was very rarely used and did not align with our new usability guidelines.
[Quick actions](<https://support.nepton.com/hc/en-gb/articles/8268008050717>), [Bulk actions](<https://support.nepton.com/hc/en-gb/articles/8271501506973>), [Right-click menu](<https://support.nepton.com/hc/en-gb/articles/8267765001501>) [ref 12409]
  * #### Performance improvements
We have made many improvements to reduce wait times and load on the servers. The impact should be noticeable in many features around the platform.
    * A complete rewrite of project handling and storing
    * Query optimisations for high-traffic pages and features
  * #### Configurable mobile quick start events
Save your employees time and improve accuracy, by configuring prefilled events they can start from mobile with one click of a button.
    * Primarily intended for frequent or complex work recordings, quick start events can now be configured for the working community and setting groups, and are a great time saver for common events.
    * We plan to expand on this feature making it available in more places in a future version.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/7074461491101>) [ref 8819]
  * #### Reorderable Worktime setting exceptions
Worktime setting exception rules are evaluated in the order they are listed, from top to bottom, acting on the first one that matches. This improvement allows you to easily change the order of these exceptions by dragging and dropping.
[Configure exceptions to settings](<https://support.nepton.com/hc/en-gb/articles/360002560677-Configure-exceptions-to-settings>) [ref 12734]
  * #### Public web service endpoint simplified
A long overdue clean-up of our endpoint, which makes it easier to understand and utilise. Much of the supporting documentation has also been overhauled during this version. Work will continue on our API guidance during early 2023.
[ref 13122]
  * #### More intuitive person field value validity editing
We added a "01.01.1900" watermark on date input when it contains no value to signify value is in use from start of times
  * #### New mobile artwork
We heard you love the artwork we added to the mobile view. So we added more of it! Check back each week to see a new image. There might even be some special images if you login on special dates :)


###  __ Changes 
  * #### More straight forward usage of person identifier fields
From now on, re-using an employee number or a username, requires removing it completely from the previous user. Previously re-using required only ending the validity of username or employee number for the previous user.
[ref 12465]


###  __ Fixes
  * #### Worktime "Most frequently used" projects could, under certain circumstances, contain the wrong projects for individuals
[ref 7571]
  * #### A person's default project would still be added to new events even if it had been marked completed or had passed its project end date.
[ref 11913]
  * #### Travel invoice reimbursement information is now correctly translated into the user's language in the mobile view
[ref 12408]
  * #### Technical correction to URL generation for admins browsing Worktime administrative areas
End-users are not impacted by this change.
[ref 12620]
  * #### During the import of person (HR) data, it was possible to get duplicates even when identifying by employee number
[ref 12465]
  * #### Accrual balances in the Approve event requests view do no-longer disappear after pressing "Send message only" or "Reject" button
[ref 12857]
  * #### The incorrect amount of supplement hours was displayed in the mobile view
[ref 12863]
  * #### Technical problem in terminal settings encryption
[ref 12866]
  * #### Employees > Export to importable Excel, had fields which prevented it from being imported easily
[ref 13114]
  * #### Planning > Location selection, is updated with the correct information when a unit is changed, or locations are added or removed
[ref 13148]
  * #### Corrections to work contract handling
    * Approve and Fill buttons were not working in the list of all work contracts.
    * User could not log out when work contract was not filled in.
[ref 13185]
  * #### Corrections to some Worktime public web service error messages
[ref 13234]


##  **21/12/2022** release (2.10.31)
###  __ Fix
  * #### Reading RFID tags worked incorrectly with some of the terminals.
[ref 13248]


##  **20/12/2022** release (2.10.30)
###  __ Improvement
  * #### Terminal software has been updated to support more tag configurations.
[ref 13205]


##  **15/12/2022** release (2.10.29)
###  __ Fixes
  * #### Validity control has been added for setting Worktime > Work hours > Administration > Working community / Setting group settings > Work shifts > "Worked time over work obligation is earned primarily outside of planned shifts"
[ref 13218]
  * #### Worktime > Work hours > Approve hours - view could crash if there were unapproved activities before report period and activities had started earlier than 12 months before the report period end date
[ref 13225]
  * #### Fixes for Worktime > Projects > Reports > Hours by person - report
    * In some cases report could crash if reported events had started before selected reporting period
    * Report could incorrectly show information from previous day for events that span overnight
[ref 13219]
  * #### Annual leave earning calculation did not work correctly in some situations when work contract end date was set and work contract lasted for less than 12 months
[ref 13216]
  * #### Person import person identification did not work correctly when no user name was provided
[ref 13224]


##  **08/12/2022** release (2.10.28)
###  __ Improvement
  * #### Travel invoices maximum per diems payable for foreign daily allowances for 2023 have been added
[ref 12423]


###  __ Fixes
  * #### Worktime > Work hours > Approve hours view crashed if there were unapproved and ongoing activities outside report period
[ref 13211]
  * #### Adding Balance leave event request in the past caused event editing page to crash
[ref 13207]
  * #### Worktime > Work hours > Approve hours view could show redundant overtime hours if days had exceptionally long events
[ref 13204]


##  **29/11/2022** release (2.10.27)
###  __ Fixes
  * #### Worktime event editing form could be missing the "Projects" heading
[ref 13190]
  * #### User calendar view did not show weekly rest times in some cases
[ref 13165]


##  **24/11/2022** release (2.10.26)
###  __ Improvement
  * #### CGI Prima integration has been updated to the latest standards agreed with CGI
[Guidance](<https://support.nepton.com/hc/articles/5358790925853>) [ref 13021]


###  __ Fixes
  * #### Missing translations added to mobile pages
[ref 13173]
  * #### In some situations, On Call hours were not correctly represented in the data collected by rulesets
[ref 13124]


##  **10/11/2022** release (2.10.25)
###  __ Fix
  * #### Correction to HR data export to Excel
The role related permissions under Employees > Administration > Settings > General, now further limit the export of HR data to Excel. The exported Excel will only ever include people who's extended data you can view, as defined by your role and relations to them.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002425637-Roles>) [ref 13026]


##  **31/10/2022** release (2.10.24)
###  __ Fixes
  * #### The Balance events report in Worktime > Work hours > Reports, was not working in some situations.
[Guidance](<https://support.nepton.com/hc/fi/articles/360002548917-Saldon-tapahtumat>) (in Finnish) [ref 13096]


  * #### Approval of travel invoices in Worktime was not working in some situations.
There was a problem opening the view when there were travel invoices on locked dates and the user approving the work hours did not have rights to approve travel invoices.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360005381337-Approving-travel-invoices>) [ref 13101]


  * #### Worktime projects and events import file handling has been corrected.
If the setting "SFTP relative directory path for archiving" under Event import options or Project imports options of the import is left empty, Worktime will delete the imported file after processing the file.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/4403974690321-Importing-events-with-scheduled-runs>) [ref 13070]


##  **11/10/2022** release (2.10.20)
###  __ Fixes
  * #### People with unpaid events could have the wrong amount of work hours calculated
Recent corrections to the Worktime settings unintentionally impacted many customers because the default behaviours of some event types changed. This could result in fewer hours being considered as work for people who have recorded unpaid events, leading to more borrowing from balance.
  
To correct this situation, by default, unpaid event types will now contribute to weekly work hours, but not towards overtime earning. If you still have people with unpaid events that have incorrect work hour calculations, please review your settings related to this matter, in Worktime > Administration > Working community & Setting group level settings, then: 
    * Work hours > TES > Event types that contribute to work week.
    * Work hours > Accruals and overtime hours > Balance > Borrow at the end of the week if weekly obligation not fulfilled.
[ref 13901]
  * #### Worktime > Work time shortening leaves report, could crash in some situations
[ref 13077]
  * #### In some situations, customer Setting group names were being automatically translated by the platform. This was unintentional and made identifying them difficult
[ref 13030]


##  **29/09/2022** release (2.10.18)
###  __ Improvements
  * #### The calculation of setting exceptions based on public holidays has been optimized.
[ref 13025]
  * #### Added a new option for event types to contribute to the work week, but not towards overtime earning.
This is useful when configuring event types such as absences which should fulfill work obligations, but not count towards overtime earning.
This new setting is available at working community and setting group levels respectively under the Work hours > TES > Event types that contribute to work week, heading.
[ref 11823]


###  __ Fixes
  * #### The Employees > Administration, pages were very slow to load for some customers.
[ref 13405]
  * #### Absence and sick leave reports showed the wrong number of absence days in some cases where there were multiple overlapping work events with sick leave or absence on the same day.
[ref 13064]
  * #### The Worktime calendar view failed to load and showed an error for some people if they had earned a work rise from overtime targeted to an accrual.
[ref 13028]
  * #### The Worktime exceptional entry warning "Day has work obligation but no entry has been made" could appear on the current day, even if an event had been started.
[ref 10381]


##  **19/09/2022** release (2.10.17)
###  __ Fixes
  * #### The shift planning view was sometimes incorrectly warning about conflicts.
[ref 13022]
  * #### Projects > Reports > Hours by person report, could crash when very large amounts of data are loaded.
Large reports are now detected and offered directly as Excel downloads instead of being shown in the browser. This change also reduces loading times.
[ref 13019]
  * #### Work hours > Reports > Absences per person report, was showing incorrect compensation types when no grouping option was selected.
[ref 13015]
  * #### Added option to set whether unpaid sick leave contributes to work week.
[Guidance](<https://support.nepton.com/hc/articles/360005058217>) [ref 11821] [ref 11699]
  * #### Fixed a calculation issue with unpaid sick leave contributing to the work week and automatic borrowing at the end of the week.
[Guidance](<https://support.nepton.com/hc/articles/360005058217>) [ref 11821] [ref 11699]


##  **08/09/2022** release (2.10.16)
###  __ Improvement
  * #### Mepco absence import now more intelligently handles events where the begin time has not been set.
In the past, situations like this could result in events falling outside of permitted hours.
[ref 12995]


###  __ Fixes
  * #### In specific configurations, levelling period overtime calculations could encounter errors which blocked integrations, exports, and viewing of the affected person's calendar.
[ref 13014]
  * #### Worktime > Work hours > Reports > Hours by event type and Hours by salary type, could crash when very large amounts of data are loaded.
Large reports are now detected and offered directly as Excel downloads instead of being shown in the browser. This change also reduces loading times.
[ref 13009]
  * #### Bank accrual earned from overtime was not always calculated correctly on days with a planned shift
[ref 12963]


##  **25/08/2022** release (2.10.15)
###  __ Fixes
  * #### A mistake in our previous hotfix release caused several problems. We will investigate how these changes slipped past our quality assurance process
    * Adding and editing of work shifts was not possible
    * Some parts of the platform were not accessible for some people


##  **25/08/2022** release (2.10.14)
###  __ Improvement
  * #### Exported report Excel filenames are simplified and shortened
[ref 12943]


###  __ Fixes
  * #### Person SSN's were not correctly included in CGI Prima and eFina integrations
Integration ID in CGI Prima can also now be overwritten with a ruleset
[ref 12976]
  * #### Safety check limits were incorrectly affecting 100% daily overtime hours in some long continuous events
[ref 12975]
  * #### Worktime > Work hours > Reports > Event reports could crash when very large amounts of data are loaded
Large reports are now detected and offered directly as Excel downloads instead of being shown in the browser. This change also reduces loading times.
[ref 12962]
  * #### The Work hours > Reports > Hours by salary type report had some misleading column titles
Absence compensation headings incorrectly included the words "reduced compensation" and "unpaid".
[ref 12967]


##  **11/08/2022** release (2.10.13)
###  __ Improvements
  * #### Worktime 'Absences per person' report now has the option to report all individual absences as they were marked to the calendar or to group absences together which are considered as continuing
Previously, the report always grouped absences which were considered continuing. This improvement makes the report useful for multiple purposes.
[Guidance](<https://support.nepton.com/hc/articles/4404282746641>) [ref 11249]
  * #### Viewing the details of a service log entry is now significantly faster
Before this improvement service log entries with large amounts of log data could be very slow to open.
[ref 12918]


###  __ Fixes
  * #### Worktime levelling period calculations for maximum overtime were incorrect when a public holiday and absence fell on the same day
[ref 12915]
  * #### The Worktime calendar could show warnings about Midsummer Eve missing work entries even if the day had no work obligation
[ref 12890]


##  **03/08/2022** release (2.10.12)
###  __ Fixes
  * #### Certain rulesets returning specific data caused manual integrations to not be able to run
[ref 12940]
  * #### Improved the logging of Microsoft login errors in the Employees > Administration > Service log
[ref 12944]


##  **02/08/2022** release (2.10.11)
###  __ Fix
  * #### The Worktime calendar view failed to load and showed an error for some people who had zero value balance resets
[ref 12950]


##  **27/07/2022** release (2.10.10)
###  __ Fix
  * #### Person creation was not possible after 2.10.9
[ref 12945]


##  **27/07/2022** release (2.10.9)
###  __ Improvements
  * #### Integration logs found in Employees > Administration > Service log, were accidentally simplified in a previous update and therefore lacked the usual detailed breakdown for troubleshooting. From this version onwards the logs will again contain the usual level of detail.
[ref 12929]


###  __ Fixes
  * #### In some situations, the Worktime > Calendar view and Worktime > Events in Calendar report could crash.
[ref 12931]
  * #### Work start and end time rounding settings now take priority over event rounding settings, which prevents problems when both are in use.
[ref 12927]
  * #### Online work contract values filled by an employee were cleared whenever they approved any related attachments. Forcing them to fill in the contract details multiple times.
[ref 12865]


##  **18/07/2022** release (2.10.8)
###  __ Improvements
  * #### Kieku event import service log report has been simplified.
[ref 12919]


###  __ Fixes
  * #### Project list export to excel was not working in certain specific cases.
[ref 12922]


##  **12/07/2022** release (2.10.7)
###  __ Improvements
  * #### Annual leaves can be treated as work days of leveling period in maximum overtime calculations
[ref 12903]


###  __ Fixes
  * #### Event report did not work when it included travel invoices without start and end times
[ref 12917]


  * #### Fixes to event import integrations scheduling
[ref 12914]


  * #### Setting fields with sensitive data can now be obscured in all browsers.
[ref 12862]


##  **05/07/2022** release (2.10.6)
###  __ Fixes
  * #### In person import report, in some cases instead of names of fields containing faulty values, field id number was shown instead
[ref 12901]


  * #### SSO configuration page was not working correctly and was causing an error.
[ref 12909]


##  **30/06/2022** release (2.10.5)
###  __ Fix
  * #### Logging in on the terminals did not work in some cases
Some terminals were stuck in a state where the offline/online state kept constantly changing.
[ref 12898]


##  **29/06/2022** release (2.10.4)
###  __ Improvement
  * #### Enhancements to Worktime import integrations to run them faster
[ref 12752]


###  __ Fixes
  * #### Worktime pages errored in specific situations
[ref 12891, ref 12893]
  * #### In some cases, custom work week start time and assumed activities caused error message on empty days in permitted work times popup in calendar view
[ref 12875]
  * #### In the projects section of add event view, loading spinner of clear-button was not disappearing
[ref 12867]


##  **27/06/2022** release (2.10.3)
###  __ Fixes
  * #### In planning, planning template dates are now shown correctly
[ref 12881]
  * #### Exporting work shift list per day and Exceptional entries reports in Excel-format did not always work correctly
[ref 12879]
  * #### Additional fix for opening Worktime calendar and events in table views when there was a decimal value of Worktime shortening leave (e.g. 0.5 days)
Fix in the previous version did not handle all problematic cases.
[ref 12872]


##  **22/06/2022** release (2.10.2)
###  __ Improvement
  * #### Worktime events default start and end times can now be set to be on the previous, current, or next day
This is useful for nightshift workers who's events often straddle two days.
[ref 12842]


###  __ Fix
  * #### The Worktime calendar did not open correctly in situations where there was a decimal value of Worktime shortening leave (e.g. 0.5 days)
[ref 12872]


##  **21/06/2022** release (2.10.1)
###  __ Fixes
  * #### Event and project imports did not work correctly in certain situations after the version 2.10.0 release
No actions are needed from customers and the integrations will recover on the night after the release. Todays integrations that have failed will be ran again after the version update.
[ref 12869]
  * #### The following Worktime reports did not load correctly after version 2.10.0: Work hours > Reports > Presence view & Dining sum up reports, and Work shifts > Workshift list reports.
[ref 12873]


##  **18/06/2022** release (2.10.0)
###  __ New
  * #### Added support for CGI Prima integration
Nepton now supports the export of working times, absences, and year leave to CGI Prima
[ref 9553]
  * #### Support for the Finnish 2022 family leave reform
    * New absence types, Pregnancy leave, Parental leave, and Family care leave, as well as the renaming of the existing Parental leave type to "Parental leave (pre-form)", to support the changes in family leave
    * Please see the dedicated [2022 Family leave reform](<https://support.nepton.com/hc/articles/5513696094749>) article for more information
[ref 12648]


###  __ Improvements
  * #### Upgrade to the use of PHP 8.1 which brings new technical opportunities and minor performance improvements to Worktime pages, reports, and calculations
[ref 11666]
  * #### The Planning > Planning view, can now be filtered by individuals
This makes detailed planning more convenient and also makes the planning assistants and tools more flexible
[ref 12799]
  * #### The Planning > Planning view, Supervisor filter is now a much more useful tool
The planning view supervisor filter can now pick multiple supervisors at once, can be searched using the first and last names, username, or employee number, and can also find any person with active subordinate relations. Previously, the filter would only list people who have the "Supervisor" role assigned in the HR data.
[ref 12801]


###  __ Fixes
  * #### Worktime settings regarding default suggested work start and end times for work shifs, allowed invalid values
    * Incorrect setting values have been automatically fixed, and no action is needed by customers.
    * Improved translations regarding worktime workshifts settings so they are more easily understood.
[ref 12660]
  * #### Some Worktime terminals were reporting log in errors after the Nepton 05/03/2022 release
[ref 12601]
  * #### Network connection failures could cause long delays instead of the terminal switching to offline mode in a timely manner
In rare situations, updating terminals with new settings could cause crashes and long delays.
[ref 12582]
  * #### Incorrectly configured terminals could show misleading messages about login failures
There are now dedicated messages to indicate if a login failure is due to incorrect configuration.
[ref 12786]
  * #### A number of minor usability problems with the online working contract templates have been fixed
[ref 12702]
  * #### Mepco manual absence import was not working correctly
This issue did not affect scheduled Mepco absence imports, and no actions are needed from customers.
[ref 11642]
  * #### Unpaid time was incorrectly taken into calculations when doing rounding for total work time
This issue could result in longer total work times than expected. No actions are needed from customers.
[ref 12833]
  * #### In some situations, the setting controlling times when 50 percent overtime is not earned, was not working as intended
[ref 12770]
  * #### The Worktime > Projects > Reports -> Hours by Person report with data grouping by event type and salary type breakdown could show incorrectly summarized overtime values
[ref 12836]


##  **09/06/2022** release (2.9.16)
###  __ Improvement
  * #### Event locking and approval settings validity controls
Controls for administering validities for each Worktime setting under _Work hours > Event locking and approval_ have been added
[ref 11939]


##  **01/06/2022** release (2.9.15)
###  __ Fixes
  * #### Event times were not saving correctly on some Apple devices
[ref 12761]
  * #### The use of override fields in rule sets did not always work correctly if the original field was also present
[ref 12721]
  * #### Permitted work times did not always work correctly when splitting overnight work into separate shifts
[ref 12786]
  * #### The Worktime > Work hours > Approve hours, initial balance value could be based on a different date than the chosen range
[ref 12809]


##  **23/05/2022** release (2.9.14)
###  __ Fix
  * #### Person search in setting validity control was not always working correctly
[ref 12785]


##  **19/05/2022** release (2.9.13)
###  __ Fixes
  * #### The event import was missing the option to import accrual changes or resets using decimal values
[ref 12725]
  * #### Several minor usability tweaks and corrections to the custom event types setting administration
[ref 10307]
  * #### Salary data exports using a non-UTF-8 encoding integration format, such as CGI Palkat, could be corrupted when containing specific special characters and/or emojis
All affected customers have been informed and no further actions are needed.
[ref 12751]


##  **09/05/2022** release (2.9.12)
###  __ Improvements
  * #### Mepco salary export has possibility to include new additional columns for custom data in CustomData4 - CustomData9 fields
[Guidance](<https://support.nepton.com/hc/articles/360003473498>) [ref 12742]
  * #### Added Excel support to the manual project import integration and improved validation handling
[ref 12731]


###  __ Fixes
  * #### Visible HTML br tags have been removed from description text area
Line breaks appear now without extra mark-up. Fix relates to description field in pages such as Person group information, Setting group information and Project details.
[ref 12603]
  * #### Assumed lunch was not always marked between worked hours if day only had marked work outside of planned shift time
[ref 12750]
  * #### In event import setting administration setting up person used to create event or additional column titles did not work correctly
[ref 12754]
  * #### Rule helpers [WORK-DAY-HAS-EVENTS-WITH-BASE-PART] and [WORK-DAY-HAS-EVENTS-WITH-OVERTIME-PART] did not work correctly when overtime pay targets came from event type's Exceptional overtime pay target default or defaults that weren't event type specific
[ref 12735]


##  **28/04/2022** release (2.9.11)
###  __ Improvements
  * #### Creating a work event from an individual work shift has been changed to open the Add Event window
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002602638>) [ref 12631]
  * #### The service logs for Nepton Payroll salary data synchronization have been clarified to make the log more readable and easier to investigate for possible issues in the integration
[ref 12538]
  * #### Setting exceptions gain new helpers that are faster and easier to understand
    * Setting exceptions make workhour calculations very flexible, but they also slow down calculations and can be difficult to understand. Setting exception helpers are human-readable terms that simplify checking for conditions, whilst also avoiding slowdowns.
    * We will migrate existing customers to use these new helpers over the coming months. No action is needed from you at this time. See the guidance page for all setting exception helpers and their use.
    * More helpers will be added in future releases.
[Guidance](<https://support.nepton.com/hc/articles/360002560677>) [ref 12561]


###  __ Fixes
  * #### When not using the retired levelling period configuration method, summary in events in calendar and events in table views displayed levelling period hours incorrectly
[ref 12687]
  * #### Description texts for some work shift related settings did not work correctly
Default hour span and default accuracy settings now also applied for Work shift list per hour -page
[ref 12177]
  * #### Balance caches were not re-calculated when creating events from work shifts
[ref 12715]
  * #### Day total hours were not shown correctly in project hours by person report
[ref 12661]
  * #### Event report did not load correctly if users who have inactive work conract were selected for the report
[ref 11764]
  * #### Microsoft Excel file download issue has been resolved
[ref 12691]
  * #### Project hours by person report gave an error if the report had annual holiday events
[ref 12153], [ref 12738]
  * #### Approve hours -view errored in certain situations
[ref 12727]
  * #### Approve hours view now correctly displays the event codes
[ref 12615]
  * #### Using the same project multiple times on the same event will now no longer lead to the incorrect duration being shown in certain situations
[ref 12700]


##  **13/04/2022** release (2.9.10)
###  __ Fixes
  * #### After the initial Microsoft or SSO logins, users would be redirected automatically to the identity providers' login page until users log out by clicking the logout link
[ref 12531]


  * #### Impossible to select a user in external services settings
[ref 12676]


##  **11/04/2022** release (2.9.9)
###  __ Fixes
  * #### Work events created from planned shifts could be missing the project, even if projects are mandatory
Projects are now correctly added and mandatory project checks are respected.
[Guidance](<https://support.nepton.com/hc/fi/articles/360006781437>) [ref 12631]
  * #### Terminal offline records were sometimes not being processed correctly and could impact device performance
A processing loop could cause processing of offline events to fail, which in turn could degrade performance of terminal hardware over time.
[ref 12645]
  * #### Visma Nova work hours export file headers were incorrect, which prevented the file being processed correctly by Visma.
[ref 12690]


##  **04/04/2022** release (2.9.8)
###  __ Improvements
  * #### Default start and end times can now be configured per event type via Worktime > Administration > Setting group/Working community settings > Work hours > Rendering options
This can be a great time saver when employees record the same event times most days
[Guidance](<https://support.nepton.com/hc/articles/360008777997>) [ref 11899]


###  __ Fixes
  * #### Multiple minor event request related tweaks to make everyday use more comfortable
[ref 12314]


##  **31/03/2022** release (2.9.6+2.9.7)
###  __ Improvements
  * #### Request Approvals quality of life improvements
User interface, workflow, and performance improvements, to the event request approval tools
[Guidance](<https://support.nepton.com/hc/articles/360017787717>) [ref 12652]
  * #### Setting exceptions gain new helpers that are faster and easier to understand
    * Setting exceptions make workhour calculations very flexible, but they also slow down calculations and can be difficult to understand. Setting exception helpers are human-readable terms that simplify checking for conditions, whilst also avoiding slowdowns.
    * We will migrate existing customers to use these new helpers over the coming months. No action is needed from you at this time. See the guidance page for all setting exception helpers and their use.
    * More helpers will be added in future releases.
[Guidance](<https://support.nepton.com/hc/articles/360002560677>) [ref 12561]


###  __ Fixes
  * #### Permitted and expected work times displayed in the Worktime > Workhours > Calendar view > 'Info' button for each day, could be incorrect if they were affected by setting exceptions
[ref 12267]
  * #### Having multiple Microsoft login configurations per customer is now possible
    * It is now possible to have multiple different Microsoft login buttons for the same customer environment
    * Customers who wanted this in the past but had to use a workaround instead will be contacted in the near future
[Guidance](<https://support.nepton.com/hc/articles/360002590137>) [ref 12549]
  * #### Annual leave reports could trigger the synchronisation of salary data to external systems
In some cases, this resulted in an error making users unable to run any annual leave reports. This only occurred if real-time synchronisation of salary data was configured in the working community.
[ref 12673]
  * #### Person import from Sympa API was not always saving Employment end date changes, leaving the field empty instead
[ref 12646]


##  **22/03/2022** release (2.9.5)
###  __ Fixes
  * #### Creating a new service request in Employees > Service requests, could result in an error
[ref 12650]
  * #### Spelling corrections in Worktime settings
[ref 12651]


##  **17/03/2022** release (2.9.4)
###  __ Fixes
  * #### Trying to edit an event or view its details in Worktime > Workhours > Events in calendar, did not always work if the related events' comment or details contained special characters
[ref 12619]
  * #### Worktime UpdateActivities web service function could not remove event approvals as it should be able to
[ref 12639]


##  **16/03/2022** release (2.9.3)
###  __ Improvements
  * #### It is now possible to set the assumed event type for empty workdays of individuals from their Worktime > Administration > Persons > Person settings. Previously this was only possible for setting groups and the entire working community.
[ref 11901]


###  __ Fixes
  * #### Gaps in a persons' Payment group assignment caused that person's information page to crash.
[ref 12616]
  * #### A mistake in RFID code comparisons meant that the person import could create new entries for the same RFID and person with each import. The problem did not affect end users.
[ref 12623]
  * #### The Planning > Planning view, could fail to load and inform that there was an error with loading data, with an error id for contacting customer service. This was caused by a problem in the "Maximum consecutive workdays" settings behaviour.
[ref 12633]
  * #### Worktime integrations could finish very long after they were scheduled to start
[ref 11702]


##  **10/03/2022** release (2.9.2)
###  __ Fixes
  * #### Work contract files can no longer be viewed after the page has been refreshed
[ref 12514]
  * #### Events in table - report had wrong text in the page title
[ref 12545]
  * #### Fixed an issue which caused the person selection in the calendar view to be reverted into a past selection.
[ref 12607]
  * #### External services settings were not always opening in setting group settings due to caching issues.
[ref 12610]
  * #### Weekly rest time compensation settings were not visible in setting group settings.
[ref 12614]
  * #### Minus selection button for negative values was not showing in planned event type permitted work time settings.
[ref 12618]


##  **09/03/2022** release (2.9.1)
###  __ Fixes
  * #### Fix for terminal login problems
Login with RFID tag or PIN code was not possible with many of the terminals after some incorrect settings saved during last Saturday. This update will fix these settings and login is possible at 15:00 at the latest or after the Terminal has been restarted.
[ref 12597]
  * #### Approve hours-view did not work correctly, but was for example not showing some of the persons in the view in certain cases.
[ref 12594]


##  **05/03/2022** release (2.9.0) \- Performance improvements
###  __ Improvements
  * #### Performance improvements
A large collection of changes that will improve performance of most features. Work will continue on this topic in future releases.
[ref 9027]
  * #### Work time shortening leave settings are more flexible (Support for Energiateollisuuden TES)
Work time shortening leave can now be configured to have month-long or year-long earning periods, and to only be earned after employment has lasted a number of months, with the option to backpay those months.
These new capabilities directly support configurations needed for the Energiateollisuuden TES and alike.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002559837>) [ref 12496]
  * #### Worktime event edits and deletions can be undone
Worktime events can now be restored to an earlier state via the event history controls.
Deleted events can be restored by first taking the event report and then clicking through to the desired event's history.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/4422686840733>) [ref 12266]
  * #### Event request approvals loading
Users are now offered a chance to change filtering options before the view loads. This avoids waiting for data loading that possibly wasn't needed.
[ref 9027]


###  __ Fixes
  * #### The person import could fail when processing names which are very long or accidentally included double white space characters
[ref 12503]
  * #### For customers with SSO or Microsoft Login configured, using the direct login URL could sometimes drop users at the select deployment page instead of logging them in
[ref 12544]


##  **28/02/2022** release (2.8.33)
###  __ Improvement
  * #### Activity related APIs now support more of their related data and are therefore more useful
    * Identification by event type codes
    * Details about absences and sick leaves
[ref 12571]


##  **24/02/2022** release (2.8.32)
###  __ Improvement
  * #### Rulesets for Visma Nova work hours export can now target all supported columns with data
An earlier limitation meant some columns were always empty.
[ref 12400]


##  **18/02/2022** release (2.8.31)
###  __ Fixes
  * #### A previous change for performance improvement caused problems with setting exceptions for customers who had duplicate event codes configured
This fix addresses the problem and requires no actions from customers.
[ref 12553]
  * #### In some situations events recorded via the mobile view could result in unintended overlapping entries.
[ref 8825]
  * #### Project hours by person report with salary type breakdown did not group work rises correctly if multiple work rises earned the same compensation
[ref 12469]
  * #### Maximum compensation settings did not work correctly when work week calculations were set to calculate regular time for whole week before calculating additional work and overtime
[ref 12535]
  * #### Approving hours showed the wrong year in the table headline
Wrong year was shown when the selected date range end date was the last date of the year.
[ref 12506]


##  **10/02/2022** release (2.8.29)
###  __ Improvements
  * #### Added support for using API-key authentication with IFS integration
[Guidance](<https://support.nepton.com/hc/articles/360003504177>) [ref 11525]


###  __ Fix
  * #### Fix for an issue where work rises and setting exceptions did not work together correctly with events that span multiple days
The previous fix did not fix all use cases.
[ref 12524]


##  **09/02/2022** release (2.8.28)
###  __ Fix
  * #### Fixed an issue where setting exceptions based on event categories could cause an error
[ref 12537]


##  **08/02/2022** release (2.8.27)
###  __ Fix
  * #### Fix for issues where validity rule did not work correctly
[ref 12529]


##  **03/02/2022** release (2.8.26)
###  __ Improvement
  * #### Performance & setting exceptions
The performance of many features has been improved by handling common setting exceptions differently. The improvement includes a new approach for creating setting exception rules based on event types on the day, and many existing exceptions have been updated to this approach where possible. This will lead to better performance for customers using the setting exceptions.
Added a tool that helps in adding setting exceptions based on common use cases such as public holidays, and based on events on the day.
[Guidance](<https://support.nepton.com/hc/articles/360002560677>) [ref 12470]


###  __ Fixes
  * #### Fix for an issue where work rises and setting exceptions did not work together correctly with events that span multiple days
[ref 12498]
  * #### Travel invoice exceptional entry did not show missing trip locations if no trip data was saved for the travel invoice
[ref 12352]
  * #### Fix for an issue in editing travel invoice start and end dates
[ref 12520]


##  **02/02/2022** release (2.8.25)
###  __ Improvements
  * #### Added support for configuring "Energiateollisuuden TES" work time shortening leave earning
Earning can be configured to happen on monthly basis and from the beginning of employment when the employment has lasted for 3 months or more.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002559837>) [ref 12496]


###  __ Fixes
  * #### Limiting for maximum compensation per event and per event type per day was done before lunch deduction
This resulted in limiting too much if assumed lunch was generated
[Guidance](<https://support.nepton.com/hc/en-gb/articles/4418364072465>) [ref 12001]
  * #### Fix for the scheduler task when the parameters are missing.
[ref 12508]


##  **26/01/2022** release (2.8.24)
###  __ Improvement
  * #### Performance optimisation when fetching work rise settings
[ref 11450]


###  __ Fixes
  * #### Fixed an issue with event report when travel invoice trip was missing trip timezone data
[ref 12495]
  * #### Fixed an issue with fetching payslips for Nepton Payroll
[ref 12464]
  * #### Fixes for issue where setting exceptions were not fetched correctly
[ref 11450, ref 12498]


##  **20/01/2022** release (2.8.23)
###  __ Improvements
  * #### Working contract improvement
Now all the person info types are supported.
[ref 12429]


  * #### Planning view page performance improvement
[ref 12467]


  * #### Exceptional entry performance improvement
Exceptional entry warnings will no longer be shown on approved days except for in the dedicated Exceptional Entry report (when enabled with the report filters). This improves the performance of multiple features and also makes it quicker and easier to identify important information in the calendar and approval views.
[ref 12489]


###  __ Fixes
  * #### Fix in workshift planning
In case of an error updating the annual holidays and other absences shown in workshift planning according to worktime data, the information is automatically updated again when opening the planning view or clicking the Update View button.
[ref 8069]


##  **18/01/2022** release (2.8.22)
###  __ New
  * #### GetActivities and GetActivitiesV2 APIs changed to return events for deactivated persons as well
[ref 10782]


###  __ Improvements
  * #### Performance improvements
[ref 9209]


###  __ Fixes
  * #### Fix in splitting salary data into multiple files
The value by which the salary data is divided into several files is no longer converted to lowercase in the file name.
[ref 12319]
  * #### Fix for an issue with running Heeros integration when there is no salary code set for an integration row
[ref 12480]


##  **13/01/2022** release (2.8.21)
###  __ New
  * #### The old EU/ELY-centre report returned with a new name
The new report name is "Invoicing report"
[ref 12468]


###  __ Improvements
  * #### Performance of hours approval improved
[ref 11450]


###  __ Fixes
  * #### Fixed bug preventing removal of planned shifts
[ref 12458]
  * #### When Heeros integration was renamed, integration ruleset queries were not updated accordingly
[ref 12463]


##  **04/01/2022** release (2.8.20)
###  __ Improvements
  * #### EU/ELY project report updated to conform to the requirements
An additional worktime role permission has been added for granting permission to use the report for managed project.
[Guidance](<https://support.nepton.com/hc/articles/360002548957>) [ref 7645]
  * #### Service log improvement
In case of errors in person import via Sympa API there might be additional error information in the data that can be downloaded in the service log view. Now this is also pointed out in the service log error message.
[Guidance](<https://support.nepton.com/hc/articles/360002575478>) [ref 12442]


###  __ Fixes
  * #### Fix in workshift planning
Events ending at midnight do not show in workshift planning view for the next day or as reserved time for the next day for the person when a workshift is planned.
[ref 9496]
  * #### Fix in person export for Nepton Payroll
An error has been fixed that prevented exporting person data for Nepton Payroll service.
[ref 12447]
  * #### Fix in worktime calculations
Fixed calculation issue when work and sick leave were earned on a day with expected working times.
[ref 12451]


##  **29/12/2021** release (2.8.19)
###  __ New
  * Travel invoice foreign allowances added for 2022
[ref 11498]


###  __ Improvement
  * Aboa integration in work time has been renamed to Heeros and export data can be fully overridden by ruleset rules
[Guidance](<https://support.nepton.com/hc/fi/articles/360003270078>) [ref 12344]


###  __ Fixes
  * Changes in selected tasks for a workshift or shift need can be published in work shift planning.
[ref 11575]
  * Fix for error in annual leave, earned days report
[ref 12337]
  * Fix for checkbox value not saved in working contract
[ref 12425]


##  **16/12/2021** release (2.8.18)
###  __ Fix
  * Fixes to lunch break calculations
[ref 12405]


##  **15/12/2021** release (2.8.17)
###  __ Improvements
  * #### All deputies are included in person export to Excel
We are now exporting all deputies for a person when exporting person data using "Export to Excel" button. Note that the Deputy field is not exported when exporting data using the "Export importable Excel" button.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002590217>) [ref 12058]
  * #### Generic working contract template
Generic working contract template, to be use as a base for making custom working contracts, is now available on the guidance.
[Guidance](<https://support.nepton.com/hc/articles/360002590217>) [ref 12348, ref 12406]


###  __ Fixes
  * Persons' EventsLockedDate-field is now available in integration rulesets UserInfoData table.
[Guidance](<https://support.nepton.com/hc/fi/articles/360015612638>) [ref 11904]
  * If a dropdown value is deleted from an custom info type, it is shown in the UI, only on the person who has that value already saved.
[ref 11987]
  * Fix for persons additional fields dropdown list item selection when two items have the same value.
[ref 12396]
  * #### Location selection demanded when trying to access locations management
When customers were trying to access the locations management from the "Locations"-tab, they were shown a location selection page, even if location selection was not needed. Now clicking the "Locations"-tab leads to location management listing.
[ref 12412]
  * #### Fixes in setting primary task on person form
Setting a primary task doesn't cause any more error when saving the person. It is now also possible to save a task without a unit set for persons belonging to a unit.


##  **13/12/2021** release (2.8.16)
###  __ Improvement
  * #### Presentation of service log entries from person imports have been improved
All imported person data is now presented in a table row by row. If there were problems with some of the data, the details are presented in another table.
[ref 12390]


###  __ Fixes
  * #### Fixes for person information form validity editing
Person information selectable by on/off checkboxes had some problems in the validity edit view to show the correct checkbox value after edit and save if validity information was added or removed. In addition, it was not shown after saving if two consecutive same values were automatically combined into one value. These errors have been fixed.
[Guidance](<https://support.nepton.com/hc/articles/360004856937>) [ref 11369]
  * #### Fields to import can be defined for person imports in Excel format
The fields filtered in person imports can be defined in Fields to import setting instead of previous Header row setting.
[Guidance](<https://support.nepton.com/hc/articles/360002489317>)
  * #### Login fixes
Fixed some problems related to our previous security fix.
[ref 12009]


##  **09/12/2021** release (2.8.15)
###  __ Improvements
  * #### The use of annual leave can now be reported two years into the future
[ref 12349]
  * #### Bulk deletion of related events from multiple persons is now possible when work time is exported to an external system in real time
[ref 12402]
  * #### Service login disabled after too many failed login attempts
Service login cannot be retried for a while if there have been multiple invalid login attempts.
[ref 12009]


###  __ Fixes
  * #### Work time setting history view didn't have correct scrollbars in some cases
[ref 12389]
  * #### Fix for person import error message about validity field format
If the valid from date is in incorrect format, the error message shown in the service log clarifies it is an error in the date format.
[ref 12398]
  * #### When modifying an event type, its behavior was not displayed in all cases
  * #### Fix for viewing payslips in Employees
Viewing payslips led to an error in some cases.


##  **30/11/2021** release (2.8.14)
###  __ Improvements
  * #### Integration ruleset improvements
It is now possible to add API user and API business ID for web service export in integration rulesets.
[Guidance](<https://support.nepton.com/hc/articles/360007534058>) [ref 12371]
  * #### Rule based setting exceptions
Added support for rule based setting exceptions to the default event start/end times and default event type settings.
[ref 12372]


###  __ Fixes
  * #### Fix for unit manager permissions
Fixed unit manager permissions to view and edit information of their own subordinates according to the supervisor permissions.
[ref 11848]
  * #### Fix for Netvisor integration ruleset
Calling RunIntegrationRulesetV2 did not include response data when running a ruleset in Netvisor format. It is now included.
[ref 12109]
  * #### Fix for person import type selections
When importing persons manually, there were two Default options for person import type. The duplicate option has been removed.
[ref 12322]


##  **25/11/2021** release (2.8.13)
###  __ Fix
  * #### Customer specific maintenance job to remove incorrect data
[ref 12225]


##  **23/11/2021** release (2.8.12)
###  __ Improvements
  * #### Usability improvement on ruleset definition tool
When using current time (now) on rulesets, tool warns if UTC time might be used unintentionally instead of local time.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257>) [ref 12370]
  * #### Added French public holidays (Victory day, National day and All Saint's day)
[ref 12185]
  * #### Improved browser support for the Nepton Payroll-service information dialog
[ref 12284]
  * #### Added ordering by last name for person list type user info fields on person information form
Also now the persons are listed last name first, to make it ordering more obvious.
[ref 12361]
  * #### Added support for importing custom user info fields with validities using Sympa HR API
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360014650697>) [ref 12339]
  * #### Security improvement
Contact details about security issues added to the site (standardized security.txt).
[ref 12330]


###  __ Fixes
  * #### Work shift planning didn't respect person weekly worktimes correctly in some cases.
[ref 11576]
  * #### Fix for issues with payment groups where payment group description was not set.
[ref 12302, 12311]
  * #### Some Inoptics terminals did not take daylight saving into account when recording events.
[ref 12333]
  * #### In some cases work shifts not belonging on selected locations were showing on work shift publishing.
[ref 12345]
  * #### Users could create unsuitable type of working contract documents.
[ref 12345]
  * #### Running scheduled task manually did not properly tell if it failed due to wrongly defined folder paths.
[ref 12356]
  * #### Balance reset, balance change and balance lock can be set as hidden separately.
[ref 12373]
  * #### Fix for Aboa salary export issue.
[ref 12377]
  * #### Work rise "maximum amount compensated" as zero does not work.
After this fix, no work rise is earned if maximum amount compensated is 0.
[ref 12356]


##  **11/11/2021** release (2.8.11)
###  __ Fixes
  * #### Customer specific bug fixes
[ref 12350]


##  **09/11/2021** release (2.8.10)
###  __ Fixes
  * #### Fix for the user export : Integration failure
[ref 12324]


##  **08/11/2021** release (2.8.9)
###  __ Improvements
  * #### Improved scheduled event import to allow importing events with no end time
[Guidance](<https://support.nepton.com/hc/en-gb/articles/4403974690321>) [ref 12336]


###  __ Fixes
  * #### Work rise salary codes were automatically overridden in integration ruleset rules
[ref 12338]


##  **04/11/2021** release (2.8.8)
###  __ Fixes
  * #### More versatile lunch break settings
Now it is possible to limit assumed lunches, lunch hour duration and if lunch is paid by paid worktime.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002558757>) [ref 12198]


##  **03/11/2021** release (2.8.7)
###  __ New
  * #### Update to Nepton Payroll-service introduction
Recording of the Nepton Payroll-service introduction webinar has been added to the Nepton Payroll introductory popup.
[ref 12326]


###  __ Improvements
  * #### Security improvement: Clear browsing data on logout
On logout, Nepton service will ask the browser to clear all locally stored browsing data related to Nepton-service.
[ref 11973]


###  __ Fixes
  * #### Fix for connection issue between Inoptics-terminals and Nepton service
[ref 12317]
  * #### Nepton Touch terminal device update
Nepton Touch terminals are updated to latest version to prevent switch between normal time and daylight saving time occurring a few days before or after the correct night.
[ref 12323]
  * #### Fixed an issue with viewing certain service log entries with attached files
[ref 12320]
  * #### Fix for issue with sending text messages
[ref 12133]


##  **01/11/2021** release (2.8.6)
###  __ New
  * #### Delete multiple workshifts at once
There is a new tool in workshift planning that makes it possible to delete all workshifts in the visible planning view at once.
[Guidance](<https://support.nepton.com/hc/fi/articles/4409910812305>) [ref 11611]


###  __ Improvements
  * #### Worktime login disabled after too many failed login attempts
Worktime login cannot be retried for a while if there have been multiple invalid login attempts
[ref 12009]


###  __ Fixes
  * #### Fixed an issue in opening supervisor's own salary slips in Own info > Documents
[ref 12075]
  * #### Using the same event type abbreviations everywhere
Same event type abbreviations are used in all event approval views.
[ref 12310]
  * #### Fixed an issue with integration rule
Rule workriseearnedatcompensationtype produced an incorrect value for some overtime types.
[ref 12313]


##  **28/10/2021** release (2.8.5)
###  __ Fixes
  * #### Fixed issue with scheduled imports not running.
[ref 12294]


##  **28/10/2021** release (2.8.3)
###  __ Fixes
  * #### Fixed Elisa Ring integration not running.
[ref 12301]
  * #### Fixed error with insertActivities web service with real-time salary export.
[ref 12303]
  * #### Fixed out of date caches that might have resulted in the event editing page popup from still not opening in older browsers.


##  **26/10/2021** release (2.8.2)
###  __ Fixes
  * #### Deleting event attachments did not work correctly.
[ref 12163]
  * #### Pop-up windows did not open correctly in Internet Explorer 11 or Edge in IE compatibility mode.
[ref 12285]


##  **25/10/2021** release (2.8.1)
###  __ Improvements
  * #### Enhancements to Nepton Payroll - video
[ref 11811], [ref 12284]


###  __ Fixes
  * #### Fix for user interface issue when weekly rest time compensation was set to be earned based on worked time but the earning period based on - setting was not set.
[ref 12224]


##  **23/10/2021** release (2.8.0) - Nepton Payroll
###  __ New
  * #### Nepton can now pay salaries as a service
With the launch of our new product Nepton Payroll, salary calculation and payment are handled as a service based on the data within Nepton. Customers can achieve fast, reliable, and transparent payroll, in real-time, based directly on their HR and Worktime data.
As part of this update, new salary and payslip controls become visible to all customers. If you do not yet use Nepton payroll, these will advertise the new capabilities of the service.
Sales begin on 28.10 with a product launch webinar at 09:00. Invitations and details about registration will be made public soon. Save the date!
  * #### Payment groups
HR data has been extended with Payment groups. These are used to group people who should be paid something on the same schedule (e.g. a salary, wage, bonus, etc). A persons' membership to a group, indicates they should be compensated according to its payment periods. In a future version, this concept will be used to make approval recommendations to supervisors, more intelligent and proactive. Payment groups can be used to select and filter people for Worktime reports and integrations.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/4406602996625-Payment-groups>) [ref 11156]
  * #### Export HR data whenever it is edited
HR data exports can now be configured to occur whenever there are edits to the data within Nepton, effectively allowing for real-time HR data integration.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489357-Scheduled-task-person-export>) [ref 11771]
  * #### Import & Export past and future HR data values for people, using JSON format
All past, present, and future values of HR data fields can now be imported and exported in the action by using the newly supported JSON format.
Using the JSON format, it is also possible to send HR data directly to a receiving REST webservice.
[ref 11771]


###  __ Improvements
  * #### New HR data fields and improvements
    * **Hourly wage** \- The ‘Hourly wage’ field has been replaced with a new and improved field of the same name, that allows decimal values only. Data that can be converted automatically, has been as part of this update. Where information could not be updated automatically, a warning will be shown in the person’s data, with instructions on how to correct and move it.
    * **Monthly salary** \- A new ‘Monthly salary’ field has been added so more accurate salary information can be stored about an individual.
    * **Classification of occupations (Ammattiluokka)** \- The Classification of occupations field has been added to support payment of salaries in Finland.
    * **Nepton person identifier** \- This read-only field has been added to provide a more robust and permanent way of identifying Nepton personal data globally. This value is available in imports and exports of HR data, including salary exports via Worktime rulesets and is controlled by Nepton. Once a person has been added to Nepton, this identifier is generated and will never change.
[ref 12060]


###  __ Fixes
  * #### Service logs more readable
Multiple improvements have been made to the service logs to improve readability and usefulness.
[ref 11399]
  * #### Person information > Language selection, was not translated
The selection of a persons’ preferred language, and the language shown in Nepton UI is now properly translated
[ref NONE]
  * #### SSO error reporting
In some cases, SSO errors that could not be related to a specific customer were still shown to customers. These are now reported directly to Nepton, for further investigation.
[ref NONE]
  * #### SMS sending more reliable
SMS messages would not be delivered reliably in all situations.
[ref 12133]


##  **18/10/2021** release (2.7.47)
###  __ Improvements
  * #### New settings for earning work rises from standalone TES overtime
[ref 12261]


###  __ Fixes
  * #### Improved support for SQL based setting exceptions on permitted and planned work settings
[ref 12252], [ref 11842]
  * #### Fixed time being borrowed from balance before a person's work contract has started
[ref 12260]


##  **14/10/2021** release (2.7.46)
###  __ Fixes
  * #### Customer Management Portal had issues in creating a new customer
[ref 12229]


##  **13/10/2021** release (2.7.45)
###  __ Improvements
  * #### Salary export performance enhancement
[ref 12200]


###  __ Fixes
  * #### Fix for event import via the user interface
Accrual value change in +HH:MM did not work correctly in import.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002868137>) [ref 12218]
  * #### Fix in project administration for an issue occurring while moving projects


##  **12/10/2021** release (2.7.44)
###  __ New
  * #### New settings supporting real estate collective agreements
Added settings for more options to control additional work and overtime:
    * TES > Daily additional earned over the additional rise threshold contributes to weekly additional rise threshold
    * TES > TES overtime earned separately to weekly overtime (e.g. up to 8h of TES 50% THEN up to 8h of weekly overtime 50%)
    * TES > Event types which marked for the week will cause overtime on days off to be compensated as weekly overtime following the Collective Labour Agreement for the Salaried Employees in the Real Estate Sector
Please see guidance on [Additional work](<https://support.nepton.com/hc/fi/articles/360002559438>) and [calculation of daily and weekly working hours](<https://support.nepton.com/hc/en-gb/articles/360005058217>).
Added possibility to limit setting exception validity rules `[WORK-WEEK-HAS-PUBLIC-HOLIDAY]` and `[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAY]` to only apply on a certain week day, e.g. `[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAY] Saturday`. Please see guidance on [exceptions to settings](<https://support.nepton.com/hc/en-gb/articles/360002560677>).
[ref 11604]


###  __ Improvements
  * #### Stricter server rules to improve file security
[ref 12011]


##  **11/10/2021** release (2.7.43)
###  __ Improvements
  * #### Performance improvements
The performance of handling large numbers of projects in integrations in certain situations has been improved.
[ref 12195]
  * #### Service log improvements
The technical details provided in the service logs in case of problem situations are more relevant to administrators.
[ref 11287]


##  **27/09/2021** release (2.7.42)
###  __ Improvements
  * #### Limiting lunch break length
Stamps for long lunch breaks can be reduced to the desired length with "Reduce long lunches to length" setting. In this case, the lunch break will not exceed the desired length.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002558757>) [ref 11501]


###  __ Fixes
  * #### Fixes to overtime rounding
Overtime rounding caused handling of overtime not to always happen by earning priorities.
[ref 12067]


##  **24/09/2021** release (n/a) - Support portal update
###  __ Improvements
  * #### Updated support portal look and feel
The support portal has been updated with a new look and feel, and now has dedicated news and events sections. Check out the new [Home page](<https://support.nepton.com/hc/en-gb>).
[ref 11303]


##  **22/09/2021** release (2.7.41)
###  __ Fixes
  * #### There were issues opening the service request list for some customers
[ref 12172]


##  **20/09/2021** release (2.7.40)
###  __ Fixes
  * #### Inaccurate realised work hours report
The following leave types should not have been included into this report, but were.
    * Flexible bank leave
    * Flexible work hours balance leave
    * Bank leave
    * Work time shortening leave
    * Overtime leave
[ref 12145]


##  **15/09/2021** release (2.7.39)
###  __ Improvements
  * #### Reusing names and codes of removed units
It is now possible to reuse a name or code of a removed unit by temporarily returning a removed unit into use for renaming.
[Guidance](<4405365426833-Reuse-unit-name-or-unit-code>) [ref 11739]


###  __ Fixes
  * #### Handling large amounts of workshifts
Fixed an issue permanently preventing the use of workshift planning if there were very large amounts of workshifts for the selected location planning period. Now it is possible to change the selections even if the loading of all the data would not be possible with the original selections.
[ref 12136]
  * #### Handling large amounts of projects
Improved handling of issues when handling large amounts of projects is taking more time than expected.
[ref 11918]


##  **14/09/2021** release (2.7.38)
###  __ Improvements
  * #### Performance of project hierarchy edits and updates
Optimisation to the saving logic and queries, reduce the number of writes and delays from table locking. These improvements will be most noticeable on large project hierarchies, but are in use for all customers.
[ref 8952]


###  __ Fixes
  * #### Incorrect button colours in Employees and Planning
Buttons appeared disabled even when available.
[ref 10711]


##  **30/08/2021** release (2.7.37)
###  __ Fixes
  * #### Worktime > 'Presence view' permissions corrections
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002548178-Presence-view-Roll-call->) [ref 11761]
  * #### Worktime > 'Mass enter settings' were not being saved
[ref 12045]
  * #### Personnel numbers were not showing in Worktime > 'Events in table' view
[ref 12100]
  * #### Customer Management Portal allowed configuration that caused login issues
[ref 12084]


##  **23/08/2021** release (2.7.36)
###  __ Improvements
  * #### Improvements to levelling period calculations
The settings page has been clarified and added settings to control how a public holiday shortens the maximum amount of additional work and 50% overtime during the levelling period.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002559537>) [ref 12064]


###  __ Fixes
  * #### Fixes to communication notifications
In some cases it was possible to modify notifications even when person did not have the permissions to do so.
Trying to modify or view a notification gave an error in some cases.
[ref 12070, 12071, 12072]
  * #### It was not possible to view person's information
In some cases you could not open person's information in Employees section.
[ref 11876]
  * #### Editing integration ruleset rule fix
Updating the rule from history control did not update the rule to the setting field.
[ref 12046]


##  **17/08/2021** release (2.7.35)
###  __ New
  * #### New setting exception validity rules
Added two new setting exception validity rules:
    * `[LEVELLING-PERIOD-WORK-DAYS-HAVE-PUBLIC-HOLIDAYS]` \- valid for whole levelling period if there is a public holiday on levelling period work days
    * `[LEVELLING-PERIOD-CALENDAR-DATES-HAVE-PUBLIC-HOLIDAYS]` \- valid for whole levelling period if there is a public holiday on levelling period calendar days
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560677>) [ref 11898]


###  __ Fixes
  * #### Fix to displaying work time setting values
Setting value was incorrectly shown from setting exceptions in setting pages.
[ref 12059]


##  **13/08/2021** release (2.7.34)
###  __ Fixes
  * #### Fixed invalid license in SFTP client library


##  **12/08/2021** release (2.7.33)
###  __ New
  * #### Added setting field to set salary code for work rises
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560978>) [ref 11774]


###  __ Fixes
  * #### Fixes to Fivaldi XML billing export
Export used the wrong character set encoding. Setting all data in the export was made available through integration ruleset rules.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360020620958>) [ref 11963]


##  **10/08/2021** release (2.7.32)
###  __ New
  * #### Added support for DL Prime DLWPLPT8 salary export format
[ref 11459]


###  __ Fixes
  * #### Fixes to Swedish language in the user interface
[ref 11560]
  * #### Travel time days that earned hour to hour overtime were counted incorrectly in realized work hours report
[ref 12033]
  * #### Fixed "go back" link in salary data export
[ref 12055]
  * #### Removed merging of footer cells in travel invoice approval excel export
[ref 11989]


##  **02/08/2021** release (2.7.31)
###  __ Fixes
  * #### Fix to confirmation dialogs
Update to Chrome and Edge browsers stopped showing confirmation dialog for actions in work time.
[ref 12030]


##  **29/07/2021** release (2.7.30)
###  __ Fixes
  * #### Fix to event removal
It was not possible to remove events in Chrome and Edge browsers as the latest update stopped showing confirmation dialog for deletion.
[ref 12030]


##  **28/07/2021** release (2.7.29)
###  __ New
  * #### New setting exception validity rule to ease configuration of annual leave earning
`[EMPLOYMENT-LASTED-LESS-THAN-12-MONTHS-AT-END-OF-ANNUAL-HOLIDAY-YEAR]` \- Valid when person's employment relationship/contract does not exceed 12 months at the end of the annual holiday credit year (March 31st)
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560677>) [ref 12028]


###  __ Improvements
  * #### Added CAPTCHA to forgot password page
[ref 11844]


###  __ Fixes
  * #### It was not possible to manually execute scheduled tasks in Employees section
This was an issue with scheduled task that used REST API.
[ref 12027]


##  **20/07/2021** release (2.7.28)
###  __ Improvements
  * #### CSV person import improvement
Added the possibility to import semicolons (`;`) and new line characters as part of person information.
[ref 11589]


###  __ Changes
  * #### Changed the integration filename wildcards (e.g. <SplittingValue>, <vvvvkkpp>) to use square brackets
[ref 12021]


###  __ Fixes
  * #### Salary export "Go back" link resulted in messed up values for export begin and end times
[ref 12016]
  * #### Fixed problem with SFTP user import
Problem was caused by older version of SFTP client library.
[ref 11866]
  * #### Work time percentage was setting work week to 0 when no work week length was set
[ref 11875]
  * #### Absence report was displaying sick leave and absence information to supervisors who didn't have permissions to view it
  * #### Fixed web service error when trying to insert activities without end time


##  **13/07/2021** release (2.7.27)
###  __ Fixes
  * #### Multiple internal and previous release regression fixes


##  **13/07/2021** release (2.7.26)
###  __ Improvements
  * #### Proper indication on work time setting pages when a setting has setting exceptions
[ref 12004]
  * #### Clarifications on how annual leave earning change and earning reset work
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003736798>) [ref 11862]
  * #### Sensitive information is now hidden behind eye icon
[ref 7694]


###  __ Fixes
  * #### Comma separated event type code mapping creates duplicates in Sympa absence import
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003736798>) [ref 11998]
  * #### Weekly work time for part-time percentage was rounded up, corrected to follow normal rounding rules
[ref 11149]
  * #### Users could approve own events when imported even if they lacked permission
[ref 11852]


##  **05/07/2021** release (2.7.25)
###  __ Changes
  * #### Renewed single sign-on service provider certificate
[ref 8037]


##  **05/07/2021** release (2.7.24)
###  __ Improvements
  * #### Round agreed 100% overtime separately from normal overtime
[ref 11871]
  * #### Accrual resets and changes can new be imported in scheduled event import
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002868137>) [ref 11606]


###  __ Fixes
  * #### Events with no begin and end time had started using default begin and end times in event import
A setting was added to control that behavior, allowing to either use default times or use start time of 00:00 and end time of 24:00.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/4403974690321>) [ref 11644]


##  **27/06/2021** release (2.7.23)
###  __ Fixes
  * #### Working community level event type translations had stopped working
[ref 11984]
  * #### Work time calendar would not open
This happened when work rise was earned from additional work but no pay was earned from the actual additional work itself.
[ref 11964]


##  **22/06/2021** release (2.7.22)
###  __ Fixes
  * #### Event report crashed if there were travel invoices in it
[ref 11948]
  * #### It was not possible to open work time calendar
This happened if person had additional work with additional work percentage from a setting exception.
[ref 11949]
  * #### Hour-to-hour overtime from travel time was included in "Realized work hours" report
Hours earned from travel time should not be included in the report.
[ref 11491]
  * #### RunIntegrationRuleset web service call returned non well formed UTF-8 characters
This happened when running salary exports that use other character set than UTF-8.
[ref 11804]
  * #### Fetching work events to Titania was not working
It didn't work when fetching by user's social security number. No work events were returned in that case.
[ref 11947]


##  **21/06/2021** release (2.7.21)
###  __ New
  * #### Support for storing external identifier for work time events
External identifier can be set or seen in:
    * Integration ruleset rules
    * Web service calls related to events, GetActivitiesV2, TerminalLoginV2, InsertActivitiesV2, UpdateActivitiesV2, BeginActivityV2, EndActivityV2
    * Event import
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257>) [Guidance](<https://support.nepton.com/hc/en-gb/articles/360002868137>) [ref 11435]


##  **17/06/2021** release (2.7.20)
###  __ Improvements
  * #### Multiple improvements to travel invoices
[ref 11374]


##  **16/06/2021** release (2.7.19)
###  __ Fixes
  * #### Removed person was as supervisor in person excel export
[ref 11792]


##  **16/06/2021** release (2.7.18)
###  __ Fixes
  * #### Ensured that only secure (HTTPS) cookies are used
[ref 11846]


##  **09/06/2021** release (2.7.17)
###  __ Improvements
  * #### Improvements to session cookie security
[ref 11847]


##  **08/06/2021** release (2.7.16)
###  __ Improvements
  * #### Ensured that only secure (HTTPS) cookies are used in work time
[ref 11846]


###  __ Fixes
  * #### Fixed an error in travel invoice approval excel export
[ref 11874]


##  **01/06/2021** release (2.7.15)
###  __ Improvements
  * #### Time input improvements in travel invoices
[ref 11873]
  * #### Improvements to Titania work event export
[ref 11375]


##  **27/05/2021** release (2.7.14)
###  __ Fixes
  * #### Fixes to "Hours by salary type" report
[ref 11841]
  * #### Fixed a fault in salary data exports
The occurrence of this fault was rare and required specific settings for work rises.
[ref 11858]


##  **26/05/2021** release (2.7.13)
###  __ Fixes
  * #### Fixed a fault in Visma L7 project import
[ref 11785]
  * #### Fixes to "Annual leave, usage follow-up" report
[ref 11697]
  * #### Fixes to Estonian language in the user interface


##  **25/05/2021** release (2.7.12)
###  __ Fixes
  * #### Fixed a fault in Fivaldi Billing salary export
[ref 11850]
  * #### Fixed the presentation of decimal numbers in annual leave reports
[ref 11843]


##  **24/05/2021** release (2.7.11)
###  __ New
  * #### Added Fivaldi Billing export format to salary exports
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360020620958>) [ref 11423]


###  __ Improvements
  * #### Setting exception validity rules added for Belgian and German public holidays
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560677>) [ref 11839]
  * #### Multiple improvements to event requests and event request approval
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360017787717>) [ref 11687]


###  __ Fixes
  * #### Person import did not display any errors when trying to import deputies
Importing deputies is not supported in person import.
[ref 11550]


##  **18/05/2021** release (2.7.10)
###  __ New
  * #### Belgian and German public holidays added
[ref 11544, 11574]


###  __ Improvements
  * #### Improvements to annual leave and annual leave balance settings
[ref 11531]


##  **06/05/2021** release (2.7.9)
###  __ Fixes
  * #### Work rise negative percentage part was displayed incorrectly in calendar
[ref 11745]
  * #### Fixes to overtime breakdown
    * Hours approval view didn't display breakdown of work rises earned from overtime correctly
    * The order of overtime breakdown wasn't correct in all views
    * Project hours by person report didn't display additional work breakdown by additional work percentage
[ref 11711]
  * #### Fixed a fault in absence types management
[ref 11786]


##  **05/05/2021** release (2.7.8)
###  __ Fixes
  * #### Fixes to event request e-mail notifications
[ref 11780]
  * #### Fixed several typos in the UI


##  **04/05/2021** release (2.7.7)
###  __ Improvements
  * #### Event request related improvements to reports and integration ruleset rules
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257>) [ref 11310]


###  __ Fixes
  * #### Fixes to event request e-mail notifications
[ref 11780]


##  **03/05/2021** release (2.7.6)
###  __ Improvements
  * #### Enhancements to starting work related to work shift in mobile view
[ref 11763]


###  __ Fixes
  * #### Fixes to event request e-mail notifications
[ref 11759, 11730]


##  **29/04/2021** release (2.7.5)
###  __ Fixes
  * #### It was not possible to set accrual value to be a decimal number with accrual reset event
[ref 11746]
  * #### Fixes to travel invoice input view
[ref 11741]


##  **24/04/2021** release (2.7.4)
###  __ Fixes
  * #### Fixed a fault in work time event copying
[ref 11731]
  * #### Fixed a fault in viewing events in work time
[ref 11745]
  * #### It was not possible to set annual leave reset or change value in days in event import
[ref 11728]


##  **20/04/2021** release (2.7.3)
###  __ Fixes
  * #### Event request approval was not functioning properly
[ref 11729]


##  **17/04/2021** release (2.7.2)
###  __ Fixes
  * #### Fixed a fault in work time service


##  **17/04/2021** release (2.7.1)
###  __ Fixes
  * #### Fixed a fault in work time service


##  **17/04/2021** release (2.7.0)
###  __ New
  * #### Event requests – Smoother workflow
Event types can be configured so they must be requested from line managers in advance. The primary supervisor and acting deputies are informed of new requests from their subordinates and can choose to approve or reject them.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360017787717>) [ref 11518]
  * #### In project targeting settings you can define if the work is targeted to planned work shift project or to the default project of the person
With new exception methods it is possible to define exceptional values to be valid in for example international holidays, and a possibility to define an exceptional entry to be valid, if there is a bank holiday in the week.
[Guidance](<https://support.nepton.com/hc/fi/articles/360002562658>) [ref 11508]


###  __ Improvements
  * #### More exceptions to settings
With new exception methods it is possible to define exceptional values to be valid in for example international holidays, and a possibility to define an exceptional entry to be valid, if there is a bank holiday in the week.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560677>) [ref 11455]
  * #### Expected work times based on planned work shift can be set to enable overtime earning when working before planned shift start
In the platform it is now possible to define the validity periods of expected work times to be based on planned work shifts.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360016103758>) [ref 11275]
  * #### Possibility to deliver data manually directly to SFTP server
In the platform it is now possible to deliver the data based on Rulesets defined under External integrations (e.g. Salary data) to SFTP server manually, too.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002492898>) [ref 11157] 
  * #### Additions to Visma L7 interface
[Guidance](<https://support.nepton.com/hc/fi/articles/360003316037>) [ref 11255]


##  **12/12/2020** release (2.6.0)
###  __ New
  * #### Person import via API integration
Allows future changes to be imported into the service in advance and the import interval to be set to a minimum of one hour
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360014650697>) [ref 10592]
  * #### Rulesets gain 'Deleted events' data
Can be used to retrieve deleted events and use them to generate various reports
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257>) [ref 11217,11297]
  * #### Work rises have a new setting
Possibility to set a new earning threshold, in which case earnings will only start after a certain time
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002560978>) [ref 11154]


###  __ Improvements
  * #### Support for Personec F export types 2 & 3 in integration
It is now possible to export all types in Personec F integration
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003512757>) [ref 10498]
  * #### Monitoring of annual working time
It is possible to set the annual working time monitoring with the levelling period settings
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002559537>) [ref 11027]
  * #### Project Hours by Person report improvement
Added grouping option "By Event". In addition, internal and public notes on the event and project will be included in the report.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002548957>) [ref 11107]
  * #### Rulesets gain 'Information on the accumulation of annual leave'
Can retrieve information on the accumulation of annual leave for all event types
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002489257>) [ref 10752]


##  **04/11/2020** release (2.5.1)
###  __ Improvements
  * #### Travel invoice
It is now more visual and easier to use. For example, we added travel method icons and route indications. Also domestic trips do not require time entries, which saves time and extra clicking.
[Guidance](<https://support.nepton.com/hc/fi/articles/360004788238>) [ref 10929]


##  **24/10/2020** release (2.5.0)
###  __ New
  * #### Rulesets gain ‘Person Group’ data
This is so that, for example, a customer can query their event data and include the hierarchy of Person group information including names, codes, etc.
[Guidance](<https://support.nepton.com/hc/fi/articles/360011704397>) [ref 10466]


###  __ Improvements
  * #### Naming standardisation and improvements for Worktime
In UI, for example, the terms that appear in calendar and reports correspond to each other. We have changed the following terms, among others:
    * Work hours -> Worked time incl. absences
    * Basic time -> Regular time
[ref 10935]
  * #### Microsoft Login security & stability
We have improved Microsoft Login, so that our customers can log in to our service on all browsers and devices.
[Guidance](<https://support.nepton.com/hc/fi/articles/360011745557>) [ref 10755]


##  **12/09/2020** release (2.4.0)
###  __ New
  * #### Digia Enterprise salary integration
We now support exporting salary data to this salary system. The information is transferred in Digia Enterprise format and can be used by all customers.
[Guidance](<https://support.nepton.com/hc/fi/articles/360011704397>) [ref 10075]


###  __ Improvements
  * #### Project report ”Hours per person”
Report has been added an Event type column to the report to allow better filtering and pivoting of the information. For example, you can now easily determine how many project hours were related to meetings, travel, etc.
Travel invoices and other supplements now appear in this report.
Several data selections on the report have been clarified to make it easier to understand its capabilities.
[Guidance](<https://support.nepton.com/hc/fi/articles/360002548957>) [ref 10041]
  * #### Worktime rounding
When compensated time is rounded there is now a clear distinction between work hours that were registered and time which is paid.
This corrects issues in reports such as the Overtime and Hours by salary type report, which were earlier unable to show the correct amount of worked hours.
It also improves the accuracy of data gathered by rulesets for exports and integrations. They can now be extended to consider whether compensation exists because of rounding or not. A good example of where this might be useful is when creating a ruleset for invoices, which should be based on actually worked hours, vs a ruleset for salary integrations, which should include rounded times.
The change also addresses situations where work rises were being incorrectly earned due to rounding. A good example of this are evening and night compensations as these should be awarded for the actual time worked, not rounded time used for salary calculations. There is a new Work rise setting to enable this method of calculation, which can be found in the Work rise settings section.
[Guidance](<https://support.nepton.com/hc/fi/articles/360002558557>) [ref 8841]
  * #### Integration rulesets are extended to include project data
We have added the ability to fetch project data as part of rulesets. With this you can create a variety of reports from recorded events.
[Guidance](<https://support.nepton.com/hc/fi/articles/360002489257>) [ref 10465]


##  **16/07/2020** release (2.3.0)
###  __ New
  * #### It is possible to add internal and public notes to each project added to an event
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002597857>) [ref 9011]
  * #### SSO identity provider encryption certificates can be installed from UI
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002590097>) [ref 8088]
  * #### Microsoft Azure AD SSO can be configured from UI
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360010602957>) [ref 10414]


###  __ Improvements
  * #### Travel invoices enhancements
Travel invoice report can be exported into excel.
Following travel invoices' fields are exposed in integration rule sets. Linked Guide heading 'Poimitaan matkalaskun matkan tietoja'
    * Trip start and end address
    * Trip reason
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360008045337>) [ref 10178]
  * #### Enhanced options for public holiday and work week length on obligated days
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002558797>) [ref 10472]
  * #### Worktime roles can be imported and exported
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003762577>) [ref 10425]


##  **20/05/2020** release (2.2.0)
###  __ New
  * #### Titania integration
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360008828298>) [ref 9824, 9372]
  * #### Persons additional fields can now have default values
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360008763537>) [ref 10189]


###  __ Improvements
  * #### Outdated API domain ramp-down
The new domain for events, projects and worktime calculations API is https://time.nepton.com. Old domain https://tyoaika.tyoteho.fi is obsolete and should no longer be used. Please switch to using new domain as soon as possible.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360004861558>) [ref 10211]
  * #### Service API now supports deleting events by using the UpdateActivities method
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360004861558>) [ref 10211]


##  **29/04/2020** release (2.1.0)
###  __ New
  * #### InTime integration
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360006707237>) [ref 8824]
  * #### 'Actual worktime' report (old report Work hours daily view)
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360002548557>) [ref 9537]


###  __ Improvements
  * #### Netvisor integration guidance
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360007534058>) [ref 8717]
  * #### Terminal guidance
[Guidance](<https://support.nepton.com/hc/fi/sections/360000921838-Kirjausp%C3%A4%C3%A4tteet>) [ref 8567]


##  **15/04/2020** release (2.0.0)
###  __ New
  * #### Travel invoice capabilities
Use supplements to define travel invoice rows, travel expenses or daily allowances - [Guidance](<https://support.nepton.com/hc/en-gb/articles/360002559637>)
Support for multiple routes per travel invoice.
Automatically calculated allowances, including foreign allowances, based on the routes
[Guidance](<https://support.nepton.com/hc/en-gb/sections/360001387477-Travel-invoices->) [ref 8831]
  * #### Platform status page launched
[Here](<https://support.nepton.com/hc/en-gb/articles/360006554777>) [ref 9283]
  * #### It is possible to use an external system's identifier to recognize projects in the API
In addition to the project code, projects can be recognized by identifiers used by a third party system. This permits user friendly codes and unique system identifiers to be different.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360006768998>) [ref 9426]


###  __ Improvements
  * #### Employees person information page
Usability and browser compatibility improved.
[ref 8834]
  * #### Wall terminal branding
[ref 9908]
  * #### Behaviour of primary and secondary supervisor data in person integrations
If this requires actions, you have been contacted.
[Guidance](<https://support.nepton.com/hc/en-gb/articles/360003762577>) [ref 5765]
  * #### Stability and performance issues solved
The previous version included many complicated changes, some of which did not go according to plan. We sincerely apologise for these issues! Stability and performance have now been restored, and we have made process changes to ensure this kind of situation will not reoccur.
[ref 8834, 9217]
