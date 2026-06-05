---
id: 12039347959581
title: Work schedules requirements & setup
url: https://support.nepton.com/hc/en-gb/articles/12039347959581-Work-schedules-requirements-setup
locale: en-gb
category: Support
category_id: 360000446658
section: Work schedules
section_id: 10363010715933
section_path:
- Workshift planning and Work schedules
- Work schedules
labels:
- Work schedules
promoted: false
updated_at: '2026-02-26T08:49:16Z'
edited_at: '2023-11-02T08:59:10Z'
---

# Work schedules requirements & setup

Everything you need to know to get up and running with Work Schedules in your environment.
# Requirements
## Planning service
To use the Work schedules features, you must first have access to the Nepton Planning service with an appropriate Nepton Planning service level. For the latest information on Nepton service levels and their pricing, please **[contact support](<https://support.nepton.com/hc/en-gb/articles/7077076926237>)**.
## Planning permissions
When taking Work schedules into use, you should decide what access is needed for planning and daily operations. Although these decisions largely be dictated by your organisation structure, a recommended configuration is below:
  * Administrative roles (Administrator and Salary Manager) have rights to all aspects of Planning and Work schedules, for the entire environment. This can be very useful for initial setup, troubleshooting, management, and oversight.
  * The Unit manager role has rights to all aspects of Planning and Work schedules for the Units they have a relationship with.
  * People with subordinates (aka Supervisors or team leaders) have the right to see and manage the shifts and work schedules of their subordinates for the work schedule locations they have been linked to. 
    * Please see more about Setting up work shift planning [here](<https://support.nepton.com/hc/en-gb/articles/360011258978>).
  * Employees do not have access to Planning or work schedules features, but see their work schedule shifts from Worktime.


## Units
To use Work schedules, at least one Unit must be configured via Employees > Units, and the people who will be members of the work schedule(s) should be a member of that Unit.
Units are a core concept that organises the business data (Read more about them **[here](<https://support.nepton.com/hc/en-gb/articles/360002590317>)**). Work schedules are always linked to a Unit, and therefore it is possible to have different schedules visible only to each Unit.
# Creating a work schedule
For more information on what a Work schedule is, and its related workflow, please see the dedicated article **[here](<https://support.nepton.com/hc/en-gb/articles/12038486266909>)**.
## Create a work schedule
  1. To start creating a schedule, visit Planning > Work schedules, and click "Add".
  2. Fill in the basic details of the schedule, choosing the "Work schedule" type, and a unique code it can be identified by, in event and salary exports. Then click "Save" to continue.
  3. Add schedule groups to represent the different groups of people and shift patterns this work schedule will provide. 
     * Providing a unique code for each group is recommended for handling memberships in bulk later on.


Project with name and code of the work schedule will be created automatically. Events of the person following this work schedule can be targeted to this project by using a setting "Target the worktime event to the project of the planned work shift" in the [project targeting settings](<https://support.nepton.com/hc/en-gb/articles/360002562658>).
Schedules do not appear in Planning or Worktime sections until at least one Period has been configured and published.
## Create a Holiday schedule
Whenever work schedule groups need to be divided for holiday planning, a dedicated holiday schedule should be created. Planned events from a Holiday schedule override planned events from a work schedule. It is important to note that even rest days on a holiday schedule will override the work schedule. People must become members of a holiday schedule group in addition to their work schedule group for the override to occur.
For example, if an employee would normally follow a shift pattern A A A - - Y - V - - -, but they are also a member of a holiday schedule that had extra rest days and annual leave planned (Where E is an empty day in the holiday schedule, not a rest day) - - E H H H H E E E E. The resulting work schedule for the person would look like - - A H H H H V - - -.
  1. To start creating a schedule, visit Planning > Work schedules, and click "Add".
  2. Fill in the basic details of the schedule, choosing the "Holiday schedule" type, and a unique code it can be identified by, in event and salary exports. Then click "Save" to continue.
  3. Add schedule groups to represent the different groups of people and times that holidays will be planned for 
     * Providing a unique code for each group is recommended for handling memberships in bulk later on.


Schedules do not appear in Planning or Worktime sections until at least one Period has been configured and published.
## Plan the schedule by time period
Schedules are planned and published in advance for a given date range at a time. This date range is known as a schedule period. The schedule period's date range is usually defined by your TES requirements or planning period. Often 6-12 months in length.
After adding a period and its basic information to a schedule, configure the shift and/or absence types, choose the groups of people the period is for, and their repeating shift patterns, and any offset.
At this point, the schedule period calendar will be populated at the bottom of the form, and it is possible to make edits, known as Deviations, and planning notes, before publishing.  
More details on each of these steps are below.
### Define shift types
The different types of planned events that will be part of the schedule are defined for each period. Each planned event requires an alias that it will be referred to as throughout Planning and Worktime. This facilitates quick recognition and planning.
A premade shift type, "-" No shift, is provided for all schedule periods, and should be used to represent rest days.
For example, Alias "A" could represent a morning shift with the name **"Aamu",** a start time of 06:00, end time of 14:00, and additional information and tasks representing the desired morning shift responsibilities.
Assumed lunch reductions for planned events (aka shift types) are based on settings for 
  * The whole deployment - Employees > Administration > Settings > Planning.
  * A specific work schedule - Planning > Locations > "Desired work schedule" > Location settings > Assumed lunch reduction.


### Add groups, repeating shift patterns, and offsets
Add schedule groups for the people who will have planned events during this period, and then define the group's repeating shift pattern based on the Shift types and aliases you defined earlier. The pattern should be separated by spaces.
The offset allows you to use the same pattern for every group, but offset when it starts by a number of days. Value zero starts the shift cycle from the first shift of the pattern. Positive values move the first shift of the pattern later and negative values earlier.
For example, you wish to use a shift pattern of A A A - - Y - V - - - for all 5 groups in a work schedule, each subsequent group staggered to start the pattern 2 days later.
  * **Group, offset = resulting shift pattern from day 1 of the period**
  * Group 1, offset 0 = A A A - - Y - V - - -
  * Group 2, offset 2 = - - A A A - - Y - V -
  * Group 3, offset 4 = V - - - A A A - - Y -
  * Group 4, offset 6 = Y - V - - - A A A - -
  * Group 5, offset 8 = - - Y - V - - - A A A


### Deviations
Deviations are changes from the usual shift and holiday plan for a work schedule group or individual. They can be made in the schedule period calendar and in the Planning view. Deviations are highlighted in purple to ensure they are noticed by planners and employees alike.
Some examples;
  * **A planned maintenance break** \- There will need to be maintenance that affects a production line of one or more of the schedule groups. As such, the expected dates are edited for the affected groups to have an offsite training day instead of their usual pattern. This appears as a deviation for these groups.
  * **An expected increase in demand** \- Due to planned sales and marketing, you expect to need more employees working on a given date. As such, a schedule group that usually has a rest day is edited to have a work shift and a replacement rest day later in the week or month.


### Planning notes
Although planned shifts and holidays can themselves have additional information text, it is sometimes useful to communicate more details about the plan or a special date. In such cases a planning note can be added via the schedule period calendar, for all groups or individual groups.
For example, a planning note could be helpful when you wish to explain why there are deviations on a given date. E.g. Because of a maintenance break or an expected increase in demand.
## Manage group memberships
With a work schedule created and at least one period published, it's time to ensure the right people can see and follow the planned events and shifts from it.
Schedule group memberships can only be managed once at least one period using the groups for the schedule, has been published.
### For new schedules or bulk changes (Using person import)
If you're setting up a new work or holiday schedule, or there are a lot of changes to the people following the schedule, it is recommended to configure group memberships using an Excel import file. Alternatively, the memberships can be managed from the UI, described in the next heading "Via UI".
  1. Create an import file 
     * Either, take an export of the desired people from Employees > Persons > Export to importable excel  
**Note:** When using the importable Excel, you will need to unhide all columns
     * Or, manually create an Excel import file with the desired people and columns
  2. Only include the columns necessary for identifying the person, setting their schedule group membership, and setting the correct validity (start date) of the membership  
i.e. Employee Number, Work schedule group, Holiday schedule group, and Valid from date
  3. Make sure to set the correct Valid from date for each person to preserve their past schedule group memberships.
  4. Import the file in Employees > Persons > Import persons


Full guidance on importing personnel data is **[here](<https://support.nepton.com/hc/en-gb/articles/360018767498>)**.
### Via UI & Finding people without a membership
When making small changes to memberships or if you do not have permission to import person data, memberships can be managed via the user interface. Visit Work schedules > Your chosen schedule > "Members" tab. This view also shows people in the Unit, who you have permissions to manage, that do not yet have a membership to a schedule group.
Use the search at the top of the form to find and edit memberships of a person, or browse and expand the schedule groups below, to edit the existing memberships of an individual.
When adding or editing the membership, it is recommended to set valid from date of the membership, so that past planned events from the schedule and group, do not affect the person's worktime calendar and calculations.
## Publishing
With the schedule period configured and any deviations and planning notes added, you can publish the period. Once a period is published, the scheduled events, deviations and planning notes, become visible to all work schedule group members in worktime calendar & mobile, immediately, as well as for planners in the Planning view.
Once published, you can manage, follow up, and react to real-world situations. Please see the [**Work schedules daily use and follow up**](<https://support.nepton.com/hc/en-gb/articles/12063496680349>) article
# Follow-up and daily use
Please see the dedicated article, [**Work schedules daily use and follow up**](<https://support.nepton.com/hc/en-gb/articles/12063496680349>).
