---
id: 4409389747601
title: Taking project targeting into use
url: https://support.nepton.com/hc/en-gb/articles/4409389747601-Taking-project-targeting-into-use
locale: en-gb
category: Support
category_id: 360000446658
section: Project management
section_id: 360000707398
section_path:
- Project management
labels:
- projektitoiminnallisuus
promoted: false
updated_at: '2026-06-08T05:55:37Z'
edited_at: '2022-04-27T07:35:15Z'
---

# Taking project targeting into use

It is possible to target all events to projects. 'Project' in Nepton service can be a target, customer, order, unit, etc. Targeted events can be reported in Project reporting and/or in integrations.
Project targeting functionality is included in Pro and Complete service levels.
## Where to start with project targeting feature
To make sure project targeting feature is taken into use as smoothly as possible it's good to make sure following steps has been taken in the organization.
### 1\. Make sure the goal for project targeting is clear
Identify targets to which you want to target events. These can be for example projects, customers, units, orders or other, to which targeting events can produce beneficial data. This data can be utilized for example in reporting, invoicing, payroll or other use.
[Targets are added](<https://support.nepton.com/hc/en-gb/articles/360002560877>) to Nepton as projects. Projects are shown as a sequenced tree structure, in which the visibility can be defined based on [person group](<https://support.nepton.com/hc/en-gb/articles/360002553457>). It may be beneficial to limit visibility of some projects to only for a specfic person groups to make sure events are targeted to correct targets.
### 2\. Familiarize yourself with the project targeting feature in Nepton
To benefit for the feature with it's full potential you need to understand how the feature is planned to be used in Nepton. There are 3 important parts in the feature: Adding and managing projects, targenting events to projects and reporting. Events targeted to projects can also be approved separately from event approval.
Managing project in Nepton is easy. Full description can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002561017>). Different ways of adding and importing projects to Nepton can be found from **Technical implementation: 3. Adding projects to Nepton**).
Targeting work to projects may vary depending on how events are added. Different options for adding events can be found from these articles:
[Targeting event to a project in mobile view](<https://support.nepton.com/hc/en-gb/articles/4410486932497>)
[ Targeting event to a project in calendar view or table view](<https://support.nepton.com/hc/en-gb/articles/360002597857>)
[ Recording an event with a project using the terminal](<https://support.nepton.com/hc/en-gb/articles/360002593398>)
[Targeting event to project on current status page](<https://support.nepton.com/hc/en-gb/articles/360002604478>)
Events targeted to projects can be reported. Data can also be exported as a part of salary data, invoising data or for example to a external reporting service. More info about project reports can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002548957>). It is very important to identify if Nepton's standard reports support organization's goals in event targeting process, or should you use external service for project reporting.
It is possible to include project hour approval in the process. Project hours can be approved separately from event hours. This can be done by project manager which [can be set](<https://support.nepton.com/hc/en-gb/articles/360018588898>) to every project. More information about approving project hours can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002561477>).
### 3\. Plan integrations between Nepton and other services
If projects are managed in other service projects and tree structure can be imported to Nepton. It is recommended to plan and identify all services from where data can be imported, or to which data can be exported. If there will be automated and scheduled in use these must be planned beforehand.
If no data is imported to or from Nepton all data can be managed in Nepton.
### 4\. Prepare for launch
When you have defined list of projects, tree structure and possible integrations project targeting can be taken into use. Prepare your organization by deciding suitable date for the launch. Make sure everyone are trained to the processes.
Project targeting can be taken into use by sequencing the launch. For example so one person group uses feature first and later other start using it also.
## Technical implementation
When you are ready to take project targeting unto use you must take following steps in Nepton.
Please note: Even these settings are available in the service project targeting functionality is included in Pro and Complete service levels.
### 1\. Active feature 
Project targeting feature can be activated into use in **Worktime - > Administration -> Working community settings -> Projects -> Service enabled -> Yes.**
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4996773389853/mceclip0.png)
When Projects feature is in use Projects manu will be visible. 
![mceclip1.png](https://support.nepton.com/hc/article_attachments/4996793817629/mceclip1.png)
### 2\. Settings for project targeting 
All setting for the feature can be defined in this same working community level setting menu. It's not mandatory to have all fields filled. Some of the settings can also be defined to the Setting group level but please not not all settings are available on setting group level. 
More information about project settings can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002562658>).
### 3\. Adding projects to Nepton
To target events to projects there must be projects in Nepton. Projects can be added [one by one](<https://support.nepton.com/hc/en-gb/articles/360002560877>), import to Nepton in bulk [manually](<https://support.nepton.com/hc/en-gb/articles/360003737078>), with [scheduled project import](<https://support.nepton.com/hc/en-gb/articles/360002492518>), from[ Visma L7](<https://support.nepton.com/hc/en-gb/articles/360003751058>) or with [API](<https://support.nepton.com/hc/en-gb/articles/360019840237>).
If project hierarchy is important and it needs to be saved when projects are imported or exported we recommend project hierarchy is included in project codes. For example project code could be '10/30', from which '10' would be unit code and '30' would be project code. This way reports can be done based in events targeted to a specific unit. Project code can be as long as needed and it can include as many levels as needed. 
### 4\. Project visibility 
In order to users to be able to target their work to a project you need to make sure they have a visibility to all needed projects. If in project settings it has been defined all projects are not visible to all users and person groups visibility must be defined for users one by one or a person group. More information can be found [here](<https://support.nepton.com/hc/en-gb/articles/360006776758>).
