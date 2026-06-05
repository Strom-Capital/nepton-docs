---
id: 360006768998
title: Project identification
url: https://support.nepton.com/hc/en-gb/articles/360006768998-Project-identification
locale: en-gb
category: Support
category_id: 360000446658
section: Project management
section_id: 360000707398
section_path:
- Project management
labels: []
promoted: false
updated_at: '2026-05-22T07:34:17Z'
edited_at: '2022-04-26T06:02:09Z'
---

# Project identification

For many customer deployments projects are an important part of daily use. It is therefore essential that people can easily find the project they need, both in daily use, and for salary calculations, integrations and via our API. This article details the various ways a project can be identified, and where.
Travel invoice functionality is included in Pro and Complete service levels.
## Project name
Names are the most human friendly way to identify a project, and can be used when browsing the project hierarchy, or when searching for a project. The project name is visible in all areas of the platform.
## Project code
A project code is a quick method of identifying a project, generally shorter than the name, and often unique. Especially useful in customer environments where many of the same type of project are used in different areas.
For example, a "Cleaning" project could easily appear under many city projects. With codes, each of these can easily be identified despite having the same name
  * Helsinki > Cleaning, could have a code of "HEL/Clean"
  * London > Cleaning, could have a code of "LON/Clean"


The project code can be used to search projects in customer environments, and to identify projects in integrations and the API. It is visible in the project information and project hierarchy views.
## External identifier
The external identifier works in a similar manner to the project code, but it is specifically intended for identifying projects integrated between Nepton and another system in the following situations:
  * The external system's identifier is not know to the end users
  * The external system's identifier is not friendly enough for end users
  * The project code cannot be used to uniquely identify integrated projects


The external identifier is used via the API, and can be viewed from the project information page.
Please note that the external identifier has to be unique when it is set.
