---
id: 4408264552977
title: HR data for payroll
url: https://support.nepton.com/hc/en-gb/articles/4408264552977-HR-data-for-payroll
locale: en-gb
category: Support
category_id: 360000446658
section: Nepton Payroll
section_id: 4406259955345
section_path:
- Nepton Payroll
labels: []
promoted: false
updated_at: '2025-02-20T08:00:36Z'
edited_at: '2024-10-08T08:12:25Z'
---

# HR data for payroll

The Nepton Payroll service uses personal data entered in the "Employees" section. By adding and maintaining this data, Nepton Payroll operates smoothly and salaries can be paid. Edits are synchronised in real-time, including changes based on validity date (e.g. changes that occur in the future).
## Payment groups
[Payment groups](<https://support.nepton.com/hc/en-gb/articles/4406602996625>) are required for Nepton Payroll to function correctly. They are used to automatically generate payroll lists during the payroll process.
Define in Nepton's Employees section:
  * Payment groups - Separate groups for at least monthly and hourly employees, more separation if you wish. 
    * A name for easy identification
    * Code - Provided by the payroll specialist. It links the payment group with payroll ("Payroll template ID" in Palkat)
    * (optional) A supporting description of the group
  * Payment group periods - Each represents a payment to employees 
    * The date range the payment is for
    * The date employees in this payment group will be paid
    * (optional) The date on which this payment is considered in bookkeeping
    * Coming soon: To help with the payroll flow, we plan to add a new date field which represents when events and approvals should be finalised so that payroll specialists can finalise a payroll.
    * Please note: Additional one-off payments are handled by payroll specialists and should not be added to payment group periods.
  * Payment group memberships for the employees 
    * These can be added manually via the person information pages, or with the person import feature, manually or via scheduled integration.


## Person information
The following information is used in payroll processing. These fields must be filled in Nepton for payroll to function correctly. It is recommended to use all the following fields, even if they are not marked as mandatory.
In Nepton's payroll processing, Nepton is considered the master data system. These fields should always be kept up to date in Nepton's Emplyees section, either manually or via integration from another HR system.
Although it is important to keep all personal information up to date at all times, when taking Nepton payroll into use, please make sure that Employment dates, Employee numbers, and Payment groups, are correctly set for everyone, **including past and deleted employees**. This information is used to determine which employees should be included in payroll calculations.
People with employee number 0 (Zero) will not be synchronised for Payroll. This employee number is reserved for special cases, such as accounts used for automation or administration, who do not need to be considered in payroll. It is **not** intended for deleted or past employees. Please read more about deleting people [here](<https://support.nepton.com/hc/en-gb/articles/360002424617>).
**Infromation group  
** | **Field name  
** | **Mandatory** | **Notes**  
---|---|---|---  
Basic information | First name | x |   
Last name | x |   
Email | x |   
Phone number |  |   
Street address |  |   
Postcode |  |   
City |  |   
IBAN | x | Used for payments.  
Personal identity code | x |   
Employment information | Job title |  | Shown on the payslip.  
Classification of occupation | x | Needed for insurance purposes in Payroll.  
Contract type | x |  Monthly salary OR Hourly salary Used for automatic calculations in Payroll.  
Employment start date | x |   
Employment end date |  | If set, employment in Payroll will be ended.  
Work time percentage |  |  Not synced yet! Coming in future release. Used for automatic calculations in Payroll.  
Monthly salary | x | Both monthly and hourly salary are needed for monthly paid persons. Hourly is used for monthly salary employees when hourly deductions and corrects are needed etc.  
Hourly salary | x | Required for hourly paid contracts  
Organization | Payment group | x | Will define which payroll the person belongs to. Used for generating payrolls and defining payment periods.  
## Troubleshooting
If a person's HR data is missing the required information for payroll, that will be indicated as a warning in the [Service log](<https://support.nepton.com/hc/en-gb/articles/360002575478>). A full list of the required fields is detailed in the table above.
In the event of missing, invalid, or rejected, values being reported for some fields, all valid information about a person will still be used by Payroll.
If the service log reports an error regarding permissions, such as "Unauthorised" or "Write denied", it indicates the service has not been correctly configured. Please contact customer service and provide them with the date and time of the log indicating the problem.
