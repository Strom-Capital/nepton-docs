---
id: 26673418239901
title: Personal and employment data in Reporting
url: https://support.nepton.com/hc/en-gb/articles/26673418239901-Personal-and-employment-data-in-Reporting
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
updated_at: '2025-09-01T09:02:01Z'
edited_at: '2025-09-01T09:02:00Z'
---

# Personal and employment data in Reporting

# Basic Principles
In the service, personal and employment data can be added to the query as follows:
  * Nearly all personal data fields are added to the query
    * See exceptions below
    * For every field with a validity function, you can also extract the value’s validity period
      * Useful, for example, if you need to report all assignment groups a person has had over time
    * Data entered in additional information fields can also be included in the report
  * A person’s employment start and end date
    * The duration can be derived as well
      * It isn’t stored as a single database field, but the report can include a calculated field that computes duration as of the report run date


## Grouping Options
Personal and employment data can be grouped:
  * By individual
  * By person group
  * By setting group


## Available Fields
  * Validity periods of data (date & time when a value’s validity begins or ends)
    * Only for fields with a validity function
  * First name
  * Last name
  * Contact information (address, email, phone number, bank details)
  * Next-of-kin information
  * RFID identifier code
  * Username
  * Employment role
  * Working-time role (internal identifier and/or name)
  * Person group (code, internal identifier and/or name)
  * Top-level person group (code, internal identifier and/or name)
  * Primary and secondary supervisor
  * Work area
  * Job title
  * Default project (code, internal identifier and/or name)
  * Assignment group (code, internal identifier and/or name)
  * Cost class
  * Default cost center
  * Compensation (monthly or hourly)
    * Extract from either the “Contract type” field in the person record or the “Compensation” field in the assignment group
    * Use the assignment group’s Compensation field by default—unless the Nepton Salaries service is enabled, in which case the Contract type field takes precedence
    * The Contract type field overrides the Compensation field in integrations
  * Salary amount (numeric)
    * Mandatory only when the Salaries service is enabled
    * Pulled from the monthly salary and hourly salary fields in the person record
  * Employment start and end date
  * Reason for contract termination
  * Shift-planning data stored under employment:
    * Daily working hours
    * Weekly hours MIN and MAX
  * Unique identifier in the person’s integration (depends on the chosen integration; may be):
    * Person number
    * National ID number
    * An integration-specific identifier
  * Any data recorded in additional information fields


## Can not be added to a query
  * Competencies
