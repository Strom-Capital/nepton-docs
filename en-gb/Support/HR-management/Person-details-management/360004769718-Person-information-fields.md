---
id: 360004769718
title: Person information fields
url: https://support.nepton.com/hc/en-gb/articles/360004769718-Person-information-fields
locale: en-gb
category: Support
category_id: 360000446658
section: Person details management
section_id: 360004485937
section_path:
- HR management
- Person details management
labels:
- IsNewUser
- kustannusryhmä
promoted: false
updated_at: '2026-11-06T10:36:08Z'
edited_at: '2026-10-14T12:16:11Z'
---

# Person information fields

All users and their person information can be managed in the service. Every organization can decide which fields are taken into use and which are left empty. To see persons information page navigate to Employees > Persons > Persons. Then view person information by searching the person from the list and clicking the view-icon on person row.
Person's information section has been divided into subcategories, which can vary depending on the service level that is used. 
Work Shift Planning is visible only in organizations that have Work Shift Planning functionality enabled.
In addition to the standard fields, it is possible to add additional information fields. Additional information fields are shown under the subheading Additional information. You can find more information about managing additional information fields [here](<https://support.nepton.com/hc/en-gb/articles/360002430918>).
Some fields work with the [validity function](<https://support.nepton.com/hc/en-gb/articles/360004856937>). The validity period can be defined for all fields except the following fields:
  * Worktime roles
  * Person group
  * Subordinates
  * Supervisors
  * Units
  * Default project
  * Person lists
  * Primary task


Some fields are [mandatory](<https://support.nepton.com/hc/en-gb/articles/4408898681233>). 
## Basic information
Person's basic information can be maintained in the basic information category. [Required fields](<https://support.nepton.com/hc/en-gb/articles/4408898681233>) are First Name, Last Name and Password when adding a new person. Other fields can be left blank.
First name, Last Name
  * A person's first and last name fields can contain one or more names. Names can contain letters (in any spelling), numbers, and the following special characters:
\- (hyphen)  
. (dot)  
_ (underscore)  
'(apostrophe)


Email
  * If this field is left blank, the person will not be able to request a new password, and e-mail notifications can not be sent to the person via the Communication function in the Employees section or the Shift Planning section. If the person doesn't have an e-mail address they also won't receive any event request related e-mails.


Phone number
  * If this field is left blank, text message notifications can not be sent to the person via the Communication function in the Employees section or the Shift Planning section.


Street address, Post code, City
  * Person's home address information.
  * These fields must be filled if Nepton Payroll is in use.


Password
  * The password field is only displayed when a new person is added, and it must be set for a new person. Password can be later edited in the Additional functions section, or a new password can be ordered from the login page.
  * Password is a [mandatory field](<https://support.nepton.com/hc/en-gb/articles/4408898681233>).


IBAN, BIC
  * These fields are filled with the person's bank contact information. The service checks that the account number is in the form of a genuine IBAN account number and the BIC in the form of a genuine BIC.
  * IBAN must be filled in if Nepton Payroll is in use.


Personal identity code
  * A Finnish personal identity number is filled in the personal identification number field (date of birth with six digits DDMMYY and a five-character identification part).
  * The personal identity code must be filled in if Nepton Payroll is in use.


Tax number
  * The person's tax number is a 12-digit code issued by the Finnish Tax Administration. It is used by construction workers.
  * If the person works on a construction site and Nepton Payroll (LikeIt) is in use, the tax number must be provided in this field.


Other fields in this category are informative and have no effect on the work time calculations or the functionality of the service.
## Employment Information
Person's employment related information can be managed under the categorey Employment information.
Job title
  * Can be filled freely in accordance with the company's own practices.


Classification of occupations
  * The occupational classification defines a person's occupation in accordance with the Finnish Income Register's TK10 occupational classification.
  * You can enter either the occupational classification code or part of the occupational classification name in the search field, in which case Nepton will display the occupational classifications that match the search criteria, from which you can select the person's occupational classification.
  * The job classification must be filled in if the Nepton Payroll is in use.


Employment start date
  * The person will be visible in reports and in the calendar view in the Worktime section starting from this date.
  * The person will not appear in person listings when retrieving reports for any time period before the employment start date.
  * If this field is left blank, the person will appear in the listings indefinitely in the past.
  * The start date of the employment must be filled in if Nepton Payroll is in use.


Employment end date
  * The person will be visible in reports and in the calendar view in the Worktime section until this date.
  * The person will not appear in person listings when retrieving reports for any time period after the employment end date.
  * If this field is left blank, the person will appear in the listings indefinitely in the future.
  * The end date of the employment must be filled in if Nepton Payroll is in use.


Worktime setting group
  * Set the correct worktime setting group for the person in this field. The worktime calculations are done based on the settings in the setting group. If the field is left blank, the default work community settings are used for the person’s worktime calculations.


Work time percentage
  * Indicates the person's percentage of working time. This field affects the calculations of the person's worktime in the Worktime section.
  * The service calculates the lengths of days and weeks according to the part-time percentage from the setting group settings and processes the person's worktime accordingly. More about the work time percentage [here](<https://support.nepton.com/hc/en-gb/articles/360003961118>).


Monthly salary, hourly wage
  * A person's salary is given as a numeric; integer or decimal number.
  * Either the monthly or hourly wage must be filled in in euros if the Nepton Payroll is in use.


Note! If the employment settings are changed afterwards to apply to the past, the worktime calculations will not be automatically updated unless the events at that time are also changed after the changes in the settings. Instructions for recalculating a person’s calendar can be found [here](<https://support.nepton.com/hc/en-gb/articles/4411220910865>).
Other fields in this category are informative and have no effect on the work time calculations or the functionality of the service.
## Permissions
The user's rights to different parts and functions of the service can be defined in the Permissions-section.
Role
  * Defines person's rights in the Employees-section. A person can only have one role.
  * A role is a [mandatory field](<https://support.nepton.com/hc/en-gb/articles/4408898681233>).
  * More information and detailed descriptions can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002425637>).


Worktime roles
  * Defines person's rights in the Worktime section. This field defines which worktime roles the person has, but the roles' rights are defined in Worktime.
  * A person can have multiple worktime roles at the same time.
  * More information and detailed descriptions can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002554338>).


Access to person groups
  * Defines which person groups the user has access to and with what permissions.


Short term loan permit
  * This field is informative and has no effect on the work time calculations or the functionality of the service.
  * This field can be used to indicate whether the user has a right for advanced salary.


## Organization
Organization related information can be managed in Organization-section.
Person group
  * Determines to which person group the user belongs.
  * The person group tells you where the person appears in different person lists, for example when taking reports.
  * A person can only be in one person group at a time.
  * Person groups are purely informative in nature and do not affect the worktime calculations in any way. More information about person groups can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002553457>).


Subordinates
  * This field allows you to specify the person's subordinates.
  * The person acquires supervisor rights in the worktime section for all subordinates added to this field, based on their worktime role.
  * A person can have an unlimited number of subordinates. The information updated in this field is also updated in the subordinate’s information page (in Supervisors field).


Supervisors
  * Indicates who is the supervisor of that person.
  * A person can have an unlimited number of supervisors, but only one primary supervisor. The primary supervisor is displayed in the service next to the supervisor's name.
  * Please note that notifications of sensitive actions, such as requests for sick leave, balance and annual leave, are only sent to primary supervisors.


Units
  * Indicates which unit the person belongs to in the Employees and Shift Planning sections.
  * A person can belong to more than one unit at a time. The primary unit is displayed in the service next to the unit name.
  * Information of the primary unit is informative and has no effect on any functions or worktime calculations.


Default project
  * Indicates what the person's default project is when creating a new event.
  * All events are targeted to this project by default, regardless of the type of event or absence or the reimbursement of the event (paid / unpaid / deducted salary).
  * The default project can be any sub-project that is visible to the person when recording events. The project is either linked to the person directly or through person group, or the person has visibility to all projects.


Default cost group
  * This field is purely informative. The information can be used for example, for person data automations and integrations.


Payment group
  * The payment group determines which payment periods are used to pay the user’s salary.
  * The field must be used with Nepton Payroll.


## Planning
The fields in this category are only shown if Work Shift Planning is in use in the organization.
Daily work obligation
  * Indicates a person's daily work time obligation. This value can be used in shift planning as a target number to support planning.
  * The value set here is displayed in the shift planning view on the right side next to the person.


Weekly hours MIN and MAX
  * Indicates a person's weekly minimum and maximum work time obligation. These values can be used in shift planning as a target number to support planning.
  * The values set here are displayed in the shift planning view on the right side next to the person.


Person lists
  * Indicates to which shift list the person belongs. Person lists can be used in the planning view of the Shift Planning section to sort people (Shift Planning > Planning View > Filters > Person List).
  * A person can belong to more than one person list at the same time.
  * Person lists can be added in Employees > Persons > Person Lists.


Primary task
  * Determines the person's primary task in shift planning.
  * The information informative and has no effect on any functions or worktime calculations.


Work Schedule Group
  * Determines which work schedule and schedule periods the person belongs to.


Holiday Schedule group
  * Determines which holiday schedule and holiday periods the person belongs to.


## Additional Information
The additional information shows both standard and added information fields. As standard, everyone has the following fields:
New person
  * This field is displayed if the new employment contract tracking functionality is enabled. Functionality cannot be taken into use in new environments. When a person signs their first electronic work contract, they will be marked as a new person, in which case the person will be included in the data submitted to the payroll system as a new person. After integration to the payroll system, the person will no longer appear as a new person. Changes to personal information are then submitted to the payroll system automatically, along with the change material.


Additional administrative information
  * Additional information field, where any relevant information can be saved. However, we recommend that you create separate [additional information fields](<https://support.nepton.com/hc/en-gb/articles/360002430918>) for more information. 
  * This field is visible to people who have Administrator, Payroll or HR rights in Employees section. The field does not show to persons with unit manager, supervisor, or employee roles.
  * If the Nepton Payroll is in use and there are several collective agreements in use in the working community, the name of the collective agreement applicable to the person's employment must be entered in this field for the payroll’s knowledge.


Additional information for reports
  * The information entered in the field is displayed as a separate column in some worktime reports.


Service usage language
  * Defines the person's language of use in the service.
  * The user can also change the language at the top right corner of the service.The usage language is a [mandatory field](<https://support.nepton.com/hc/en-gb/articles/4408898681233>) when a person is manually created by another user.


Microsoft AX hourly cost
  * This field specifies the value of the person's hourly rate for the field that is defined in the integration to match this field in Microsoft AX interface. This field is shown in every organization but is only in use if you have a Microsoft AX interface.


Visma cost centre
  * This field specifies the person's cost group for the field that is defined in the integration to match this field in Visma interface. This field is shown in every organization but is only in use if you have a Visma integration.


## Identifiers
A variety of different tags is shown in the Identifiers category. These identifiers are used either in the Nepton and / or in any integrations between Nepton and a third party.
Nepton Id
  * An automatically generated identifier by Nepton to identify a person. It can be used to identify users for example in person imports.


Employee number
  * Indicates the person's employee number. This is an identifier used, for example, in the creation of payroll data and the transfer of person data.
  * A person will not be included in any of the reports in Worktime section if the personal number is 0.


Username
  * Specifies the username the person uses to log in to Nepton.
  * Username is a [mandatory field](<https://support.nepton.com/hc/en-gb/articles/4408898681233>).
  * The following conditions must be taken into account when setting up a username:
    * Username must be between 1 and 100 characters long.
    * There must be no spaces at the beginning or end of the username.
    * Username cannot contain more than one consecutive space.
    * Allowed special characters:
      * @
      * .
      * ,
      * -
      * '
      * _
    * The field supports UTF-8 character encoding, which means that it supports most languages.


PIN code
  * This field must be filled when you want to allow a person to be able to record events via terminal using a PIN code.


RFID tag identifier
  * RFID tag is a physical access card identifier.
  * It is used when you want to allow a person to be able to record events via terminal using RFID tag.
  * One person can have multiple RFID tag identifiers. In this case, they need to be separated by pipe symbol. For example, if a person has 3 different RFID tags, the identifiers would be marked like this:  
5831023962|34591203239|593100795


All other fields in the Identifiers category are integration-specific identifiers. If no integration-specific identifier has been set, the person's employee number will be used for identification.
