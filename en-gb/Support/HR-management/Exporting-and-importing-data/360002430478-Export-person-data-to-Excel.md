---
id: 360002430478
title: Export person data to Excel
url: https://support.nepton.com/hc/en-gb/articles/360002430478-Export-person-data-to-Excel
locale: en-gb
category: Support
category_id: 360000446658
section: Exporting and importing data
section_id: 360004488578
section_path:
- HR management
- Exporting and importing data
labels: []
promoted: false
updated_at: '2026-05-28T07:44:01Z'
edited_at: '2026-05-28T07:44:01Z'
---

# Export person data to Excel

You can export person data to an Excel sheet if you have rights to access other people's data using the persons search. For example, supervisors can export their own data and the data of their subordinates to for reporting purposes, storing the addresses and working contract details etc. You can also use the export functionality to edit certain details for many users at once in Excel and then import the updated data into Nepton or an external system.
Due to technical limitations, there are differences between the data fields supported by the person export and import. Please check the documentation carefully for the latest information.
## Export to Excel
  1. Navigate to **employees, persons, persons** -page,
  2. Filter the persons list by search terms and search for the persons whose data you want to export.
  3. Select Export to Excel to save the results to your computer.
  4. You can open the saved Excel file on Excel, LibreOffice or another spreadsheet program. 


## Export to importable Excel
  1. Navigate to **employees, persons, persons** -page.
  2. Filter the persons list by search terms and search for the persons whose data you want to export.
  3. Select **Export to importable Excel** to save the results to your computer.
  4. You can open the saved Excel file on Excel, LibreOffice or another spreadsheet program.
  5. Edit existing data and/or add new data.
  6. Navigate to **employees, persons, import persons** -page.
  7. Import the modified file into Nepton.


## Columns in importable Excel file
The name of the export file is including the date and time first, followed by "PERSONS" and the name of the working community - in the format: YYYYMMDD_HHMM_PERSONS_COMMUNITY.xlsx. All persons are on the first sheet/tab. The name of the sheet is "Henkilölista".
The columns are displayed in the following order. The column title is displayed on the first row, other rows contain information for one person each.
**Column in default Excel file** | **Column in importable Excel file** | **Column title** | **Description**  
---|---|---|---  
A | A | First name | First name of the person  
B | B | Last name | Last name of the person  
C | C | Email | E-mail address of the person  
D | D | Phone number | Phone number of the person (as text)  
E | E | Street address | Street address of the person's address  
F | F | Postcode | Postal code of the person's address (as text)  
G | G | Town/city | Town/city of the person's address  
H | H | IBAN | IBAN code of person's bank account without spaces  
I | I | BIC | BIC code of person's bank details  
J | J | Personal identity code | Personal identity code of the person  
K | K | Tax number | The tax number of the person (as text)  
L | L | Next of kin | Person's next of kin  
M | M | Next of kin phone number | The phone number of person's next of kin (as text)  
N | N | Web page | Person's web page address  
O | O | Job title | The job title of the person  
P | P | Classification of occupations | Classification of occupations code (always 5 digits). Defines the code of Income register's classification of occupations (TK10) for the person's occupation.  
Q | Q | Contract type | Monthly or hourly paid  
R | R | Employment start date | Start date of person's current or latest employment (in format DD.MM.YYYY)  
S | S | Employment end date | End date of person's latest employment (in format DD.MM.YYYY)  
T | T | Reason for ending employment | The reason for ending of the latest employment  
U | U | Reason for employment ending | Text field for reason of employment ending  
V | V | Trial period end date | The end date of person's trial period (in format DD.MM.YYYY)  
W | W | Worktime setting group | The code of the setting group person belongs to  
X | X | Work time percentage | Person's work time percentage (as a decimal number in text field with comma (,) as the decimal separator)  
Y | Y | Monthly salary | Working contract monthly salary (numeric string which allows decimal values, but cannot start with zero)  
Z | Z | Hourly wage | Hourly wage of the person (as text)  
AA | AA | Work area | Person's work area  
AB | AB | Employer | Employer  
AC | AC | Role | Person's assigned Nepton role ("Employee", "Supervisor", "Unit Manager", "Salary Management", "HR Management" or "Administrator")  
AD | AD | Worktime roles | The names of worktime roles person has, separated by pipe character (|)  
AE | AE | Access to person groups | A list of person groups the person has access to  
AF | AF | Short term loan permit | "Kyllä" if the person has the short term loan permit, "Ei" otherwise.  
AG | AG | Person group | The code of the person group the person is a member of  
AH | AH | Units | The names of the units the person belongs to (in no particular order), separated by pipe character (|)  
AI | AI | Default project | The code of person's default project (as text)  
AJ | AJ | Default cost group | The person's default cost group  
AK | AK | Payment group | The name of payment group the person belongs to (in no particular order), separated by pipe character (|)  
AL | AL | Weekly hours MIN | Person's minimum weekly work time as hours (as a decimal number in text field with comma (,) as the decimal separator)  
AM | AM | Weekly hours MAX | Person's maximum weekly work time as hours (as a decimal number in text field with comma (,) as the decimal separator)  
AO | AO | Work schedule group |   
AP | AP | Holiday schedule group |   
AQ | AQ | Additional administrative information | Additional administrative information entered for the person  
AR | AR | Additional information for reports | Additional information for reports entered for the person  
AS | AS | Service usage language | English name of the language person uses Nepton in "English", "Finnish", "Swedish", "Danish", "Polish", "Estonian", "Norwegian"  
AT | AT | Microsoft AX hourly cost | The Microsoft AX hourly cost (as a decimal number in text field with comma (,) as the decimal separator)  
AU | AU | Visma cost centre | Visma cost centre field contents (as text)  
AV | AV | Nepton Id | An automatically generated identifier by Nepton to identify a person. It can be used to identify users.  
AW | AW | Employee number | The employee number of the person (as text)  
AX | AX | Username | The Nepton username of the person   
AY | AY | External Identifier 1 | Unique external identifier  
AZ | AZ | RFID tag identifier | The RFID tag identifier of the person  
BA | AA | Aastra | The person's identifier for Aastra (as text)  
BB | AB | DL Software | The person's identifier for DL Software (as text)  
BC | BC | Elisa Ring | The person's identifier for Elisa Ring (as text)  
BD | BD | Emce | The person's identifier for Emce (as text)  
BE | BE | Fivaldi | The person's identifier for Fivaldi (as text)  
BF | BF | Heeros | The person's identifier for Heeros (as text)  
BG | BG | Hogia | The person's identifier for Hogia (as text)  
BH | BH | IFS | The person's identifier for IFS (as text)  
BI | BI | Kieku | The person's identifier for Kieku (as text)  
BJ | BJ | Lessor-5 | The person's identifier for Lessor-5 (as text)  
BK | BK | Liksa | The person's identifier for Liksa (as text)  
BL | BL | Mepco | The person's identifier for Mepco (as text)  
BM | BM | Oscar | The person's identifier for Oscar (as text)  
BN | BN | Personec F | The person's identifier for Personec F (as text)  
BO | BO | SD Worx | The person's identifier for Personec W (as text)  
BP | BP | ProCountor | The person's identifier for ProCountor (as text)  
BQ | BQ | Scala | The person's identifier for Scala (as text)  
BR | BR | Sedab | The person's identifier for Sedab (as text)  
BS | BS | Sonet | The person's identifier for Sonet (as text)  
BT | BT | Tikon | The person's identifier for Tikon (as text)  
BU | BU | Visma | The person's identifier for Visma (as text)  
BV | BV | Full name | The last name and first name of the person, separated by comma (,) and space  
BW | BW | User account enabled | "Kyllä" if the user account of the person is enabled, "Ei" otherwise.  
BX | BX | Person group code path in hierarchy |   
BY | BY | Person group name path in hierarchy |   
BZ | BZ | Primary supervisor | The employee numbers of primary supervisors of the person, separated by pipe character (|)  
CA | CA | Secondary supervisors | The employee numbers of secondary supervisors of the person, separated by pipe character (|)  
|  | List of employee numbers of supervisors | (Empty column, see previous columns)  
| Not included in importable Excel | Mobile link | Link to person's old mobile page.  
Column is only available for non-importable Excel and only if the old mobile link feature is in use  
CB |  | Valid from date | [(Empty column - for filling in manually information for person import, see Field validities in person imports)](<https://support.nepton.com/hc/articles/360015807338>)  
| Not included in importable Excel | PrimarySupervisorFullNames | The last name and first name of the person's primary supervisor, separated by comma (,) and space. If there are multiple persons marked as the primary supervisor, they are all displayed separated by pipe character (|).  
| Not included in importable Excel | SecondarySupervisorFullNames | The last name and first name of the person's secondary supervisor, separated by comma (,) and space. If there are multiple persons not marked as the primary supervisor, they are all displayed separated by pipe character (|).  
At the end of excel - one column for each |  | (Name fields of Persons additional fields) | One column for each additional field in the order listed in Employees > Administration > Persons additional fields. Contents is what has been chosen from drop-down menu and is displayed as text. Format depends on field type:  
For integer fields the number is displayed without any separator characters if the value is between 0 and 2147483647. Negative numbers between -2147483648 and -1 are displayed with a hyphen minus sign (-) prefix. Numbers outside these ranges are not displayed.  
For decimal fields the decimal separator is comma (,)  
For yes/no fields the value is "Kyllä" for yes, "No" for no  
For date and time fields the format is DD.MM.YYYY HH:MM  
For date fields the format is DD.MM.YYYY  
For other fields the value is formatted as displayed on the person form.  
After persons additional fields | Not included in importable Excel | Deputy | The last name and first name of the person's current deputies, separated by comma (,) and space.
