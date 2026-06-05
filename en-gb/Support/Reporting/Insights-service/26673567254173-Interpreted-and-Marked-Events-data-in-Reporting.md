---
id: 26673567254173
title: Interpreted and Marked Events data in Reporting
url: https://support.nepton.com/hc/en-gb/articles/26673567254173-Interpreted-and-Marked-Events-data-in-Reporting
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
updated_at: '2025-09-01T08:58:06Z'
edited_at: '2025-09-01T08:58:06Z'
---

# Interpreted and Marked Events data in Reporting

# Basic Principles
Time-attendance data can be added to the query as follows:
  * Raw marked events, unchanged
  * Marked events, including:
    * Previous versions
    * Deleted events
    * Events modified within the specified time range
  * Interpreted time-attendance records


## Available data from Interpreted and Marked Events
You can add, for example:
  * Various pay codes (e.g. regular hours, compensatory hours, overtime types such as extra work, statutory overtime, collective-agreement overtime, balancing-period overtime)
  * Shift differentials and allowances (start-of-shift, end-of-shift, and related overtime)
  * The overtime category assigned to each event
  * Running/cumulative balances and the day-over-day change in each balance
  * Hours automatically trimmed from balances
  * Meal breaks (showing how they are calculated and placed within the day)
  * On-call duty (actual hours; overlapping marked events reduce this)
  * Hours limited by working-time regulations (e.g. permissible working windows)
  * Hours trimmed by balance limits (including “administrative balance adjustments” in the standard report)
  * Information on who approved each event
  * Unapproved events


## Grouping Options
Data can be grouped in many ways, commonly:
  * By event type
  * By marked event category (e.g. long-term absence)
  * By the queried time period
  * By compensation type
  * By pay code
  * By the actual work date
    * For example, you can choose to display work spanning midnight on the previous day (SalaryRenderingDate)
    * Or to group results within the queried range: e.g. fetch a six-month span but show monthly totals


## Available Fields
  * Duration (event length)
    * Default unit is seconds (except for integer-only fields)
    * Can be output as integer, decimal, seconds, hours, days, or currency
  * Start date & time for:
    * When interpreted time was earned
    * When a related marked event occurred
  * End date & time for:
    * When interpreted time was earned
    * When a related marked event occurred
  * Event creation and last-modified timestamps
  * Unique event identifier (used for grouping, e.g. annual leave pay)
  * Event comment (up to 2000 characters)
  * Payroll or shift date
  * Logged time details
    * Clock-in and clock-out times
    * Excludes public-holiday entries and balance-adjustment events
  * Payment date (Nepton Payroll)
  * Event type code
  * Pay-increase sequence number (Nepton settings)
  * Pay-increase payroll code
  * Pay-increase balance target (salary, balance, or other accrual)
    * Can break out base overtime vs. premium portion
  * Pay-increase percentage and minute-/hour-based uplift
  * Overtime rate that generated the increase
  * Allowance name
  * Allowance sequence number (Nepton settings)
  * Allowance pay-code number (Nepton settings)
  * Allowance date field
  * Allowance comment
  * Allowance type (normal, correction, meal-break allowance, etc.)
  * Allowance percentage (when targeted to an accrual)
    * Useful for tracking how much balance has been paid out
  * Base-part allocation (e.g. to balance)
  * Interpreted time based on base-part allocation (BasePartTarget)
  * Interpreted time based on premium allocation (OvertimeTarget)
  * Approval status (approved or not)
  * Whether the event is a request type
  * Event approver details (internal ID, first & last name and/or person number)
    * For balancing-period and weekly-rest compensations, the last approver of the period’s final week is used
  * Terminal ID where the event was started
    * If started at one terminal but ended via another method (e.g. mobile), the terminalID is lost on closing


## Can not be added to a query
  * Project-hours approver
  * Event attachments
  * Annual‐leave accrual amounts
