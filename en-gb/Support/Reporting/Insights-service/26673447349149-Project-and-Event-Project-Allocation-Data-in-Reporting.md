---
id: 26673447349149
title: Project and Event Project Allocation Data in Reporting
url: https://support.nepton.com/hc/en-gb/articles/26673447349149-Project-and-Event-Project-Allocation-Data-in-Reporting
locale: en-gb
category: Support
category_id: 360000446658
section: Insights service
section_id: 25746849648925
section_path:
- Reporting
- Insights service
labels: []
promoted: false
updated_at: '2025-09-01T09:00:31Z'
edited_at: '2025-09-01T09:00:31Z'
---

# Project and Event Project Allocation Data in Reporting

# Basic Principles
Project-related data can be added to a query as follows:
  * All fields in the project info
  * Events logged to projects and their allocations


## Filtering Options
You can limit the data, for example, to:
  * A specific project (or a branch of the project hierarchy)


## Available Fields – Project Details
  * Identifiers (internal and external)
  * Name, code, and description
  * Project start and end dates
  * Parent project’s internal identifier
  * Internal name of the project type
  * Whether the project has parent or sub-projects
  * Whether this project can be assigned to an event
    * Returns “no” if the project is a parent of the project already assigned to that event
    * Only leaf-level projects in the hierarchy can be directly assigned
  * Numeric level of the project within the hierarchy


## Available Fields – Events Assigned to Projects
  * Time logged to the project that exceeds the event’s duration
    * e.g. event duration 6 h, logged time 8 h → 2 h excess can be reported
  * For each project at a given ordinal position on the event:
    * Internal and external identifiers, code, name, and project type
  * Logged duration on the project exactly as entered
    * Either as a percentage or time value (minutes), depending on how it was recorded
    * Time-attendance interpretation does not constrain or adjust this (even if logged time exceeds the event duration)
  * Project-entry approver (project time approver)
    * Different from the event approver
    * Approval timestamp itself cannot be extracted
  * Internal and external notes on the project entry
