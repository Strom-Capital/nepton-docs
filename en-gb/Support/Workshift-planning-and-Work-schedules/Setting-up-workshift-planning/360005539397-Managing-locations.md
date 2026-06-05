---
id: 360005539397
title: Managing locations
url: https://support.nepton.com/hc/en-gb/articles/360005539397-Managing-locations
locale: en-gb
category: Support
category_id: 360000446658
section: Setting up workshift planning
section_id: 360003275658
section_path:
- Workshift planning and Work schedules
- Setting up workshift planning
labels: []
promoted: false
updated_at: '2025-07-31T04:23:57Z'
edited_at: '2025-07-10T13:18:22Z'
---

# Managing locations

All shifts are planned for Locations. Manage locations under the ‘Locations’ heading.
Locations are set up for those [units](<https://support.nepton.com/hc/en-gb/articles/360002590317>) for which planning is done. Locations are created and managed for each unit independently. Employees can be attached to the locations of their own units, so that shifts to these locations can be planned for them. Work shift planners have visibility of the planning in their own unit.
If Worktime project targeting is in use, make sure that [units](<https://support.nepton.com/hc/en-gb/articles/360002590317>) do not share codes with [projects](<https://support.nepton.com/hc/en-gb/articles/360002561017>).
Mandatory fields when creating a location are name and calculation unit. Calculation unit is the identifier for the location and it is inputted as string.
Locations are a nested hierarchy. If location is defined with category, then the location is a child for another location.
Valid from and valid until - fields prevent planning to the location outside these dates. Planning cannot be done to a location to those dates that are earlier than valid from, or to dates that are later than valid until. If the field is empty then planning can be done.
![Screenshot 2025-07-10 153816.png](https://support.nepton.com/hc/article_attachments/28754581502493)
## Creating a Project
The service automatically creates [projects](<https://support.nepton.com/hc/en-gb/articles/360002561017>) corresponding to the locations. Changes made to locations are automatically updated to the corresponding projects. Termination of the location terminates the project. Deleting a location deletes the project. Changes to projects related to locations must be made to the locations, as the data of the corresponding location directly overrides the changes made to the projects. Editing this type of projects is blocked in the Projects menu in the Worktime -section.
The project code will be the unit code that connects the project to the location. Project name will be the location name. Projects are attached to parent project which consists of the data of the unit for which the location are created. The top project is a project with the name of the unit and the project code is the unit code.
A project created in Location can be a person's default project, same as projects created through Projects. If you want to assign a project manager to a project created through a Location, you can do so from the Worktime> Administration> Persons> Projects Managed by person settings.
Units and locations visibility in a recording terminal can be defined in [Worktime project management](<https://support.nepton.com/hc/en-gb/articles/360002561017>). Only visibility in recording terminal can be configured through Worktime project management for units and locations. By default units and locations are created so that they will be visible in a recording terminal.
## Proposal of calculation unit
The bottom of the page shows the next available planning unit. This functionality advertises automatically the next unused planning code. This helps the person editing the data to prevent situations where planning unit is already used on a location in some other unit. Next available code is identified by finding the biggest number used as planning unit in any of the units and this value is incremented with one. Those calculation units that cannot be interpreted as number are ignored.
The next available planning unit shows five levels. Planning units can be set up as a string so that these levels are split by / - character. It is possible to use this to distinguish business identifiers. For example planning unit 50/200 could mean business unit '50' and location '200'. The location creates the worktime project, with project having the planning unit used as the project code. Events that are targeted to projects having project code splitted by sepator character, like '/', can in the data export be targeted to all of these levels. For example salary export could contain work costs that are targeted to a specific customer and to specific location at the same time.
## Updating Location Start and End Dates
When changing the start and end dates for a location, it's crucial to ensure that all child locations have their end dates set before updating the parent location. Likewise, when establishing the start date for a location, all child locations must also share the same start date.
![Screenshot 2025-07-10 153913.png](https://support.nepton.com/hc/article_attachments/28754581505821)
## Deleting a Location
A location cannot be deleted; it can only be marked as ended.
## Filtering Locations
The visibility of ended locations can be controlled with the "Show ended locations" checkbox. When ended locations are selected to be shown, they appear in italics in the location tree.
![Screenshot 2025-07-10 154123.png](https://support.nepton.com/hc/article_attachments/28754581506845)
