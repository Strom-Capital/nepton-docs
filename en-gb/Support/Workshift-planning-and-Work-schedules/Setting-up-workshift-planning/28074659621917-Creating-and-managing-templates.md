---
id: 28074659621917
title: Creating and managing templates
url: https://support.nepton.com/hc/en-gb/articles/28074659621917-Creating-and-managing-templates
locale: en-gb
category: Support
category_id: 360000446658
section: Setting up workshift planning
section_id: 360003275658
section_path:
- Workshift planning and Work schedules
- Setting up workshift planning
labels:
- vuorosuunnittelu
- työvuoropohja
- Vuoropohja
promoted: false
updated_at: '2026-06-08T07:57:13Z'
edited_at: '2026-06-08T07:57:13Z'
---

# Creating and managing templates

Templates are an efficient tool for planning regular work shifts. They allow you to create ready-made shift models that can be used in the planning view when creating shifts. A template can include any number of days and shifts - for example, shifts for a full week or just a few days. Once a template has been created and linked to a location, its contents can be imported directly into the planning view without manually adding shifts for each day. This significantly speeds up the planning of recurring shifts and reduces manual work. Templates are located under **Planning > Templates**.
## Creating a Template
Create a template in the planning section as follows:
1\. Open **Planning > Templates.**
2\. Select **Add** to create a new template.
![Screenshot 2025-09-11 152518.png](https://support.nepton.com/hc/article_attachments/30261343584669)
3\. Enter a **name** for the template. The name helps identify the template.
4\. Add a description if needed. The description is optional but helps clarify the purpose of the template. Information added to the Shift information field is shown to the employee in the Worktime calendar. Information added to the Planner info field is shown only in the planning view.
![Screenshot 2026-06-08 105259.png](https://support.nepton.com/hc/article_attachments/36671803185821)
5\. Add the required number of shifts by selecting **Add Shift** and the required number of days by selecting **Add Day**. Fill the shift details. You can change the order of days using the arrow buttons. Days can also be left empty to represent days off, such as weekends in a two-week rotation. No shifts are added to empty days.
![Screenshot 2025-09-11 160936.png](https://support.nepton.com/hc/article_attachments/30261350438429)
6\. Fill in the following details for each shift:
  * **Alias** : Shift alias shown in the planning view. Optional.
  * **Shift information** : Public shift information shown in both planning view and the employees calendar view. Optional.
  * **Shift information for planners** : Information shown only in the planning view. Optional.
  * **Amount** : Number of shifts to be added from the template.
  * **Event type** : Event type representing the planned shift.
  * **Start** : Shift start time.
  * **End** : Shift end time.
  * **Cancellation deadline** : Number of days before the shift starts when cancellation must be made. For example, a value of 7 means that the shift must be cancelled at least 7 days in advance. Optional.
  * **Time** : Time of day by which the shift must be cancelled on last allowed day. Optional.
  * **Tasks** : Tasks assigned to the shift. Optional.


![Screenshot 2025-09-11 162151.png](https://support.nepton.com/hc/article_attachments/30261405216797)
7\. **Save** the template once all details are filled in.
### Example 1 - One-week template
This example shows a one-week planning period with shifts on each day.
![Screenshot 2025-09-11 163551.jpg](https://support.nepton.com/hc/article_attachments/30261843953693)
### Example 2 - One-week template, work week starts on Sunday
This example shows a one-week planning period where the work week starts on Sunday at 22:00.
![Screenshot 2025-09-11 164547.jpg](https://support.nepton.com/hc/article_attachments/30262558244381)
### Example 3 - Two-week template
This example shows a two-week planning period with weekends left empty.
![Screenshot 2025-09-11 164951.png](https://support.nepton.com/hc/article_attachments/30262536621341)
## Adding a Template to a Location
A shift template can be added to a location in two different ways:
### During the creation of the shift template
A template can be added to a location directly during its creation, provided that the planner has planning permission granted via a [permission group](<https://support.nepton.com/hc/en-gb/articles/17842757043613-Permission-sets>).
When the planner has the rights to add locations, the **Location** field appears in the template details. Locations can be searched by name or selected from a dropdown menu, which displays the location hierarchy. The template can be added either to the main location (making it available for all sub-locations) or directly to selected sub-locations.
![Screenshot 2025-09-11 165850.png](https://support.nepton.com/hc/article_attachments/30262558251165)
### On the Planning Locations page
If a shift template was not linked to a location at the time of creation, it can be done later on the Shift Planning Locations page as follows:
1\. Select **Planning → Locations**.
2\. Select the desired **location** from the drop-down menu.
3\. Select **Location Templates**.
4\. Add a shift to the location by selecting **Add**.
![Screenshot 2026-04-29 083752.png](https://support.nepton.com/hc/article_attachments/35716615875229)
## Editing and Deleting a Template
Template details are edited under **Planning > Templates**. Open the intended template using the magnifying glass icon. Edit the necessary details or add new shifts and days. Save the changes when done.
![Screenshot 2025-09-11 170355.png](https://support.nepton.com/hc/article_attachments/30262822285597)
To delete a template, select the **Delete** button in the top right corner. The system will ask for confirmation before deletion. Deletion is permanent and the template cannot be restored.
![Screenshot 2025-09-11 170535.png](https://support.nepton.com/hc/article_attachments/30262833749917)
