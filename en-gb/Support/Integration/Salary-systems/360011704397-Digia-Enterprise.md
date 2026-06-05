---
id: 360011704397
title: Digia Enterprise
url: https://support.nepton.com/hc/en-gb/articles/360011704397-Digia-Enterprise
locale: en-gb
category: Support
category_id: 360000446658
section: Salary systems
section_id: 360000964297
section_path:
- Integration
- Salary systems
labels: []
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2020-08-13T09:09:54Z'
---

# Digia Enterprise

Nepton can be configured to export payroll data interpreted from recorded events, in a format the Digia Enterprise system can understand. It is possible to request this as a downloadable file or to schedule and send the information to a Digia Enterprise end-point automatically.
## Setup instructions
**1\. Set person identifiers (Employee number)**
Data in the export is identified by a person's Employee number. Employee numbers can be set by editing persons' information in Employees > Person's information view, under the Identifiers heading.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360008596217/mceclip0.png)
**2\. Create an integration ruleset**
An integration ruleset must be configured in order to export the data. You can read more about what an integration ruleset is, and how to define one [here](<https://support.nepton.com/hc/en-gb/articles/360002489257>).
## File format
The used file format is text data where columns separated by a space. Row separator is `CR` & `LF` and character encoding is UTF-8.
The column types are formatted as follows:
  * **String (Text)** \- Enclosed within double-quote characters (`"`), even when a string is empty (e.g.`""`). Double-quote characters in these strings are escaped with double-quote character (e.g.`"She said """hello world""" out loud"`)
  * **Integer (Whole number)** \- Without enclosing. Empty values are exported as a zero (`0`)
  * **Decimal** \- Without enclosing, with a precision of two decimal places. The decimal separator is a comma character (`,`). Empty value is exported as a zero (`0`)
  * **Date** \- Without enclosing, format `DD-MM-YYYY`. If empty, it is exported as a question mark character (`?`). E.g. the date 31.1.2019 would be formatted as 01-31-2019


## Limitations
Persons with Employee number "0" (zero) will not be included in the export data.
## Data columns
Column | Field | Format | Notes  
---|---|---|---  
A | Salary pay group | string | Empty as default string, can be overridden with rule field `DigiaEnterpriseSalPayGrp`  
B | Salary period | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseSalPeriod`  
C | Personnel number | integer | Person's personnel number. Can be overridden with rule field `OverrideUserIntegrationId`  
D | Salary type | string | Salary type code  
E | Time quantity | decimal | Hours as decimal when the row unit type is seconds or hours. Can be overridden with rule field `OverrideHourAmount`. When overridden, the amount will be shown regardless of the row unit type.  
F | Time quantity unit | string | If the row unit type is seconds or hours, the default value is `H`, otherwise, the default value is an empty string. Can be overridden with rule field `DigiaEnterpriseTimeUnit`  
G | Unit price | decimal |  `0` as default, can be overridden with rule field `UnitPrice`  
H | Total price | decimal |  `0` as default, can be overridden with rule field `TotalPrice`  
I | Quantity | decimal | Amount as decimal when the row unit type is not seconds or hours. Can be overridden with rule field `OverrideUnitAmount`. When overridden, the amount will be shown regardless of the row unit type.  
J | Quantity unit | string | If the row unit type is not seconds or hours, the default value is `kpl`, otherwise, the default value is an empty string. Can be overridden with rule field `DigiaEnterpriseQuantityUnit`  
K | Quantity unit price | decimal |  `0` as default, can be overridden with rule field `DigiaEnterpriseUnitQuantityPrice`  
L | Event date | date | Row's salary date (SalaryRenderingDate).  
M | End date | date | Empty as default (`?`), can be overridden with rule field `DigiaEnterpriseEndDate`. Overridden date must be selected in SQL date format `YYYY-MM-DD`.  
N | Payment date | date | Empty as default (`?`), can be overridden with rule field `DigiaEnterprisePaymentDate`. Overridden date must be selected in SQL date format `YYYY-MM-DD`.  
O | Notes | string | Empty as default, can be overridden with rule field `DigiaEnterpriseNote`  
P | Multiplier | decimal |  `0` as default, can be overridden with rule field `DigiaEnterpriseMultiplier`  
Q | Event key | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseEventKey`  
R | Resource group | string | Empty as default, can be overridden with rule field `DigiaEnterpriseResourceGroup`  
S | Resource | string | Empty as default, can be overridden with rule field `DigiaEnterpriseResource`  
T | Const event | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseConstEvent`  
U | Event type | string | Empty as default, can be overridden with rule field `DigiaEnterpriseEventType`  
V | VAT code | string | Empty as default, can be overridden with rule field `DigiaEnterpriseVATCode`  
W | Work order number | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseWorkOrderNum`  
X | Operation | string | Empty as default, can be overridden with rule field `DigiaEnterpriseOperation`  
Y | Project | string | Empty as default, can be overridden with rule field `DigiaEnterpriseProject`  
Z | Calculation object 1 | string | Project 1 code  
AA | Calculation object 2 | string | Project 2 code  
AB | Profit unit | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseProfitUnit`  
AC | Location | string | Empty as default, can be overridden with rule field `DigiaEnterpriseLocation`  
AD | Work class | string | Empty as default, can be overridden with rule field `DigiaEnterpriseWorkClass`  
AE | Work requirement group | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseWorkRequirementGroup`  
AF | Event time | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseEventTime`  
AG | End time | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseEndTime`  
AH | Continuation event | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseContinuationEvent`  
AI | Base sum | decimal |  `0` as default, can be overridden with rule field `DigiaEnterpriseBaseSum`  
AJ | Absence reason | string | Empty as default, can be overridden with rule field `DigiaEnterpriseAbsenceReason`  
AK | Prod res key | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseProdResKey`  
AL | Act oper key | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseActOperKey`  
AM | Debit account | string | Empty as default, can be overridden with rule field `DigiaEnterpriseDebitAccount`  
AN | Credit account | string | Empty as default, can be overridden with rule field `DigiaEnterpriseCreditAccount`  
AO | Link key | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseLinkKey`  
AP | Payslip note | integer |  `0` as default, can be overridden with rule field `DigiaEnterprisePayslipNote`  
AQ | Acceptor | integer |  `0` as default, can be overridden with rule field `DigiaEnterpriseAcceptor`  
AR | Accept time | string | Empty as default, can be overridden with rule field `DigiaEnterpriseAcceptTime`  
AS | Security key | string | Empty as default, can be overridden with rule field `DigiaEnterpriseSecurityKey`  
AT | Security field | string | Empty as default, can be overridden with rule field `DigiaEnterpriseSecurityField`  
AU | Actual payment date | date | Empty as default (`?`), can be overridden with rule field `DigiaEnterpriseActualPaymentDate`. Overridden date must be selected in SQL date format `YYYY-MM-DD`.  
AV | Calculation object 3 | string | Project 3 code  
AW | Calculation object 4 | string | Project 4 code  
AX | Work time form | string | Empty as default, can be overridden with rule field `DigiaEnterpriseWorkTimeForm`  
### Example
[code] 
    "1" 2008120 21477 "100" 15 "H" 24,68 370,2 0 "" 0 31-12-2008 ? ? "" 1 100830 "" "" 0 "" "" 0 "" "" "17" "3" 2 "" "" 0 0 0 0 0 "" 0 0 "5010" "2940" 0 0 0 "" "" "" ? "" "" ""  
    "1" 2008120 21477 "100" 8 "H" 24,68 197,44 0 "" 0 31-12-2008 ? ? "" 1 100832 "" "" 0 "" "" 0 "" "" "17" "3" 2 "" "" 0 0 0 0 0 "" 0 0 "5010" "2940" 0 0 0 "" "" "" ? "" "" ""  
    "1" 2008120 21477 "160" 0 "" 1500 1500 1 "kpl" 0 31-12-2008 ? ? "Provision from entire year" 1 100834 "" "" 0 "" "" 0 "" "" "17" "3" 2 "" "" 0 0 0 0 0 "" 0 0 "5010" "2940" 0 0 0 "" "" "" ? "" "" ""
[/code]
