---
id: 7982660700189
title: Export persons - JSON data format
url: https://support.nepton.com/hc/en-gb/articles/7982660700189-Export-persons-JSON-data-format
locale: en-gb
category: Support
category_id: 360000446658
section: HR data
section_id: 360001070377
section_path:
- Integration
- HR data
labels: []
promoted: false
updated_at: '2026-05-28T07:47:59Z'
edited_at: '2026-05-28T07:47:59Z'
---

# Export persons - JSON data format

Person data can be exported from Nepton into an external service. This article describes the person export fields contained when exporting in JSON data format. A detailed description about person export can be found [here](<https://support.nepton.com/hc/articles/360002489357>).
## Fields in person export file in JSON format
**Field name** | **Format of contents** | **Can be used to identify person**  
---|---|---  
Email | E-mail address | No  
Last name | Text contents | No  
First name | Text contents | No  
IBAN | [IBAN formatted bank account number](<https://en.wikipedia.org/wiki/International_Bank_Account_Number>) | No  
Username | Text contents (unique) | Yes  
External identifier 1 | External identifier 1 |  Yes  
Street address | Text contents | No  
Postcode | Text contents | No  
Phone number | Telephone number | No  
Web page | Text contents | No  
City | Text contents | No  
Employee number | Text contents (unique) | Yes  
Personal identity code | [Finnish personal identity code](<https://dvv.fi/en/personal-identity-code>) | No  
Default project | Code of the default project | No  
Employment start date | Date in format "YYYY-MM-DD" | No  
Employment end date | Date in format "YYYY-MM-DD" | No  
Hourly wage | Decimal number | No  
Reason for ending employment | Text contents | No  
Additional administrative information | Text contents | No  
Default cost group | Text contents | No  
RFID tag identifier | Text contents | No  
BIC | [ISO 9362 BIC code](<https://en.wikipedia.org/wiki/ISO_9362>) | No  
Trial period end date | Date in format "YYYY-MM-DD" | No  
Short term loan permit | true/false | No  
Full name | Full name of the person in the format  
Last name, First name | No  
Role |  | [**Role**](<https://support.nepton.com/hc/en-gb/articles/360002425637>)  
---  
Employee  
Supervisor  
Unit Manager  
Salary Management  
HR Management  
Administrator  
No  
List of employee numbers of supervisors | Employee numbers of the [supervisors](<https://support.nepton.com/hc/en-gb/articles/360002430618>), primary supervisor first | No  
Job title | Text contents | No  
Work area | Text contents | No  
Aastra | Text contents | No  
Heeros | Text contents | No  
DL Software | Text contents | No  
Fivaldi | Text contents | No  
Mepco | Text contents | No  
Oscar | Text contents | No  
Personec W | Text contents | No  
Sedab | Text contents | No  
Sonet | Text contents | No  
Tikon | Text contents | No  
Visma | Text contents | No  
Worktime setting group | Code of the [setting group](<https://support.nepton.com/hc/en-gb/articles/360002558758>) | No  
User account enabled | true/false | No  
Scala | Text contents | No  
Additional information for reports | Text contents | No  
Kieku | Text contents | No  
Tax number | 12-digit [Finnish tax number](<https://www.vero.fi/en/detailed-guidance/guidance/48791/individual-tax-numbers-and-the-public-tax-number-register2/#2.1-tax-number>) | No  
Next of kin | Text contents | No  
Next of kin phone number | Telephone number | No  
Person group | Code of the [person group](<https://support.nepton.com/hc/en-gb/articles/360002553457>) | No  
Hogia | Text contents | No  
Elisa Ring | Text contents | No  
Personec F | Text contents | No  
Primary task | Name of the primary [task](<https://support.nepton.com/hc/en-gb/articles/360010504757>) | No  
Primary supervisor |  [Nepton ](<https://support.nepton.com/hc/articles//articles/8017902121885>)[Id](<https://support.nepton.com/hc/en-gb/articles/8017902121885>) of the primary [supervisor](<https://support.nepton.com/hc/en-gb/articles/360002430618>) (UUID) | No  
Secondary supervisors |  [Nepton Ids](<https://support.nepton.com/hc/en-gb/articles/8017902121885>) of the secondary [supervisors](<https://support.nepton.com/hc/en-gb/articles/360002430618>) (UUID) | No  
IFS | Text contents | No  
Lessor-5 | Text contents | No  
Service usage language |  | **Selected language of person** | **Field value**  
---|---  
Danish | da-DK  
English | en-GB  
Estonian | et-EE  
Finnish | fi-FI  
Polish | pl-PL  
Swedish | sv-SE  
Norwegian | nb-NO  
No  
Emce | Text contents | No  
Microsoft AX hourly cost | Decimal number | No  
Weekly hours MIN | Decimal number | No  
Weekly hours MAX | Decimal number | No  
Visma cost centre | Text contents | No  
Work time percentage | Decimal number | No  
Worktime roles | Names of [worktime roles](<https://support.nepton.com/hc/en-gb/articles/360002554338>) | No  
Units | Codes of [units](<https://support.nepton.com/hc/en-gb/articles/360002590317>) | No  
Deputy |  [Nepton Ids](<https://support.nepton.com/hc/en-gb/articles/8017902121885>) of the [deputies](<https://support.nepton.com/hc/en-gb/articles/360002430678>) | No  
Mobile link | Url | No  
NeptonPersonGUID |  [Nepton Id](<https://support.nepton.com/hc/en-gb/articles/8017902121885>) (UUID) | Yes (recommended)  
Monthly wage | Decimal number | No  
Classification of occupations | 5-digit [Incomes Register´s Classification of Occupations (TK10)](<https://www.stat.fi/en/luokitukset/ammatti/ammatti_17_20210101/>) | No  
Payment group | Id of the [payment group](<https://support.nepton.com/hc/en-gb/articles/4406602996625>) (UUID) | No  
All [persons additional fields](<https://support.nepton.com/hc/en-gb/articles/360002430918>) | Formatted according to each field type | No  
## Data format details
  * Character encoding of the exported file is always [UTF-8](<https://en.wikipedia.org/wiki/UTF-8>) (a common Unicode encoding).
  * Line separator is standard Windows line separator (CR+LF 0x0D 0x0A).
  * In [JSON](<https://en.wikipedia.org/wiki/JSON>) data format person information is exported as an array of person objects.
  * Each person object represents one person.
  * Person object consists of name–value pairs where each name represents field name and value is an array of one or more value objects.
  * Each value object consists of three name–value pairs:
**Name** | **Value**  
---|---  
Valid from | null or date "YYYY-MM-DD" of first date the value was or is valid  
Valid to | null or date "YYYY-MM-DD" of last date the value was or is valid  
Value | Decimal number or boolean value (true/false) without quotes or any other value enclosed in quotes (")  
  * If a field is not in use or not set yet the field is not included at all.
  * [Nepton Id](<https://support.nepton.com/hc/articles//articles/8017902121885>) (field name NeptonPersonGUID), External Identifier 1, Username, and Employee number are all unique identifiers for a person and can be used to identify an individual. We recommend using the Nepton Id, as it is guaranteed not to change. All of the other identifiers—except for the field **“External Identifier 1”** —will always have a value in the export data.
  * Date fields are using the format "YYYY-MM-DD" (year, month and day separated by hyphens (-), enclosed in quotes).
  * Possible additional fields of type Date and time are using the format "YYYY-MM-DD HH:MM:SS" (year, month and day separated by hyphens (-), a space, hours, minutes and seconds separated by colon (:), enclosed in quotes).
  * Decimal number fields are using dot (.) as decimal separator when the decimal part is not zero. Otherwise value is only integer number. Negative numbers are prefixed with hyphen (-).
  * UUID fields are represented as strings consisting of 32 hexadecimal digits separated by four hyphens: 8 digits - 4 digits - 4-digits - 4 digits - 12 digits. Letters are in upper case. The code is enclosed in quotes (").
  * Any other values than true, false, null or decimal numbers are always enclosed in quotes. Certain characters are escaped with a backslash (\\):
**Escaped character** | **Original character**  
---|---  
\" | "  
\\\ | \  
\/ | /  
\b | backspace  
\f | form feed  
\r | carriage return  
\n | line feed  
\u hexadecimal code | any Unicode character out of valid range 0x0020 - 0x10FFFF is displayed with \u prefix and hexadecimal code of 4 digits or more  


## Example file
[code]
    [
    	{
    		"Email": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "email@compa.ny"
    			}
    		],
    		"Last name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Last"
    			}
    		],
    		"First name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "First"
    			}
    		],
    		"Username": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "First Last"
    			}
    		],
    		"Street address": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Street address 1"
    			}
    		],
    		"Postcode": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "01234"
    			}
    		],
    		"Phone number": [
    			{
    				"Valid from": null,
    				"Valid to": "2022-10-28",
    				"Value": "019581928"
    			},
    			{
    				"Valid from": "2022-10-29",
    				"Valid to": null,
    				"Value": "08855150015"
    			}
    		],
    		"City": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "City"
    			}
    		],
    		"Employee number": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "1"
    			}
    		],
    		"Personal identity code": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "111111-111C"
    			}
    		],
    		"Employment start date": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "2022-11-01"
    			}
    		],
    		"Full name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Last, First"
    			}
    		],
    		"Role": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Employee"
    			}
    		],
    		"User account enabled": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": true
    			}
    		],
    		"Service usage language": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "en-GB"
    			}
    		],
    		"Weekly hours MIN": [
    			{
    				"Valid from": null,
    				"Valid to": "2022-11-15",
    				"Value": 40
    			},
    			{
    				"Valid from": "2022-11-16",
    				"Valid to": null,
    				"Value": 37.55
    			}
    		],
    		"Weekly hours MAX": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": 40
    			}
    		],
    		"Work time percentage": [
    			{
    				"Valid from": "2022-12-01",
    				"Valid to": null,
    				"Value": 50
    			}
    		],
    		"Worktime roles": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Omien sekä alaisten tietojen muokkausoikeus"
    			}
    		],
    		"NeptonPersonGUID": "37F7EAFE-046F-ED11-81FD-A0510B65B142",
    		"AdditionalDecimal": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": 4.5
    			}
    		],
    		"AdditionalDateTime": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "2022-11-20 12:20:00"
    			}
    		]
    	},
    	{
    		"Last name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Account"
    			}
    		],
    		"First name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Disabled"
    			}
    		],
    		"Username": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Disabled Account"
    			}
    		],
    		"Full name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Account, Disabled"
    			}
    		],
    		"Role": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Employee"
    			}
    		],
    		"User account enabled": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": false
    			}
    		],
    		"Service usage language": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "fi-FI"
    			}
    		],
    		"Worktime roles": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Omien sekä alaisten tietojen muokkausoikeus"
    			}
    		],
    		"NeptonPersonGUID": "FA1A79A9-126F-ED11-81FD-A0511B65B142"
    	}
    ]
[/code]
