---
id: 11166111654685
title: Visma LTR salary export
url: https://support.nepton.com/hc/en-gb/articles/11166111654685-Visma-LTR-salary-export
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
updated_at: '2025-06-18T08:12:32Z'
edited_at: '2025-06-18T08:12:32Z'
---

# Visma LTR salary export

Salary data can be exported from Nepton to Visma LTR system. Export uses REST API which is provided by Visma.
## Requirements
  * [Project targeting needs to be enabled in Nepton](<https://support.nepton.com/hc/en-gb/articles/4409389747601>).
  * For the export to be done to Visma LTR through REST API, it is required that projects in Nepton match the projects in Visma L7 and this is why it is advisable to import projects from Visma L7 to Nepton. Read more about [Visma L7 project import](<https://support.nepton.com/hc/en-gb/articles/360003751058>).
  * All events that are exported must have at least one project recording.
  * Fields that are transferred need to be defined in Visma LTR settings to be in row level.


## Purpose and limitations
  * When a salary period's work has been recorded, it's interpretation will be transferred from Nepton to LTR's REST API. Transfer will be started in Nepton, and the interpretation of the selected period will be exported to be handled by LTR. Export will form the data to transfer based on the ruleset that is selected to be transferred.
  * If the transfer needs to be done again for a period that has already been transferred to LTR, this period's events need to be first removed in LTR before transferring the period again.


## Settings
Export settings are done with the help of [rulesets](<https://support.nepton.com/hc/en-gb/articles/360002492278>). New ruleset can be added from Worktime > Administration > Integrations > Integration ruleset > Add integration ruleset. When a ruleset has been added, its settings can be opened by clicking the ruleset's name.
### Rules
Rules need to be defined for a ruleset so that the export knows what kind of data and in which format should be sent.
![](https://support.nepton.com/hc/article_attachments/11168491809693)
Rule must be written so that salary codes match the salary codes that are set in LTR. Below is an example of a possible rule, but all the values that get mapped to OverrideSalaryCode by compensation and other attributes must match the correct salary code for that salary type in LTR.
[code] 
    SELECT   
    *,   
    CASE  
    WHEN CompensationType = 'OvertimeDaily100' THEN '0410' -- If 0410 would be salary code for 100% daily overtime in LTR   
    WHEN CompensationType = 'YearLeave' THEN '3600' -- If 3600 would be salary code for year leave in LTR  
    WHEN CompensationType = 'UnpaidBasicTime' THEN '6199' -- If 6199 would be salary code for unpaid basic time  
    WHEN CompensationType = 'BasicTime' THEN '0001' -- If 0001 would be salary code for basic work in LTR  
    WHEN CompensationType = 'WorkRise' THEN WorkRiseSalaryCode -- Salary code is set for Work rises in settings  
    WHEN CompensationType = 'WorkIncrement' THEN WorkIncrementCode -- Salary code is set for Supplements in settings  
    ELSE 'NOT_DEFINED'  
    END as OverrideSalaryCode,  
    CASE   
    WHEN isApproved = 'Y' THEN '2'  
    ELSE '1'  
    END AS VismaLTRStatus, -- If correct license to send approval status updates to LTR  
    CASE  
    WHEN CompensationType = 'BasicTime' THEN '00012' -- If 00012 would be the correct billing code for this compensationtype in LTR  
    ELSE ''  
    END as VismaLTRBillingCode -- If compensationtype would require a specific billing code  
    FROM   
    UserSalaryData  
    WHERE   
    (  
    CompensationType IN (  
    "BasicTime","ReducedRateTime","UnpaidBasicTime",  
    "AdditionalWork","OvertimeDaily50","OvertimeDaily100",  
    "OvertimeWeekly50","OvertimeWeekly100","OvertimeSunday50",  
    "OvertimeSunday100","OvertimeBaseFixed","OvertimeExtraFixed",  
    "LevellingPeriodAdditional","LevellingPeriodOvertime50",  
    "LevellingPeriodOvertime100","LevellingPeriodUnderTarget",  
    "WorkRise","WorkIncrement","PublicHoliday","WeeklyRestTime",  
    "YearLeave","PayLevellingPeriodToSalary",  
    "TESOvertime50","TESOvertime100"  
    )   
    OR (  
    CompensationType = "MarkedTime"   
    AND ActivityTypeCode = 33  
    )  
    )  
    AND OverrideSalaryCode != 0  
    AND SickLeaveTypeId IS NULL  
    AND AbsenceTypeId IS NULL  
    AND IsTimeBorrowedFromBalance = 'N'
[/code]
### Export options
Export options can be found under ruleset rules. Export format needs to be set to Visma LTR. Project information is included in Visma LTR export automatically. If there are multiple API credentials based on an employer, "Split results by" can be selected to be "Employer". More information about splitting by employer in the next chapter.
![](https://support.nepton.com/hc/article_attachments/11169151574301)
After this connection settings need to be set in the section "Export to web service". Export web service address needs to be set as the URL of the Visma LTR Rest API. The customer can obtain this address from Visma. Web service address must use secure protocol (i.e. https:// ). The address uses tasks - endpoint of the API. This means that the end of the address must contain _/tasks/_.  
  
For example if web service address is https://interface.domain.com/ltrws/REST/ , address must be defined as https://interface.domain.com/ltrws/REST/tasks/
API user needs to be set as the identifier of the company that is used in the REST API - call (_hash_ in [LTR documentation](<https://demoltr1.visma.fi/ltrws/LTRRESTapi/#/tasks/post_tasks_>)) and API key needs to have the authentication token of the REST API - call (_authkey_ in [LTR documentation](<https://demoltr1.visma.fi/ltrws/LTRRESTapi/#/tasks/post_tasks_>)). If API credentials are different depending on a person's employer, it can be set so that Split by results is set to Employer and for example API user or API key will be set to have a field name of an employer surrounded by curly brackets {} so that the value will be fetched from the persons employer's info field. Example:
  * Employer "Yritys Oy" has an additional info field named LTRApiUser which has the value "exampleuserhash"
  * Employer "Yritys 2 Oy" has an additional info field named LTRApiUser which has the value "esimerkkikayttaja"
  * Field API user is set to be {LTRApiUser}, and the integration will use API user information from the employer info. 
  * Field API key is set to be {LTRApiUser}, and the integration will use API user information from the employer info.
  * This allows that if LTR has multiple user hashes per employer, the information is transferred correctly based on the employer set to a person in Nepton


![](https://support.nepton.com/hc/article_attachments/11169203386781)  
  

Below is an example of employer's info where fields named LTRApiUser and LTRApiKey are set to be in the employer info. Name of the fields can be freely decided, but it is good practice that it is descriptive. Field name must also match what is set in the setting between curly brackets. [Read more about employers here.](<https://support.nepton.com/hc/en-gb/articles/10847746064797>)
![](https://support.nepton.com/hc/article_attachments/11169287687965)
## Starting the transfer
The transfer is started in Worktime > Administration > Integrations > Visma LTR
  * Select the appropriate ruleset
  * "Lock events until the export end date" can be chosen if necessary
  * Select the appropriate dates
  * Select "Send export data by web service"
  * Select users
  * Click Run


![](https://support.nepton.com/hc/article_attachments/14388940412189)
### API request
Integration calls the post_tasks method in Visma LTR REST API. More details can be found in [Visma LTR technical description](<https://demoltr1.visma.fi/ltrws/LTRRESTapi/#/tasks/post_tasks_>). Note that data is sent to API by sending one request per event per user. This means that integration will log a zip-file that contains all the separate JSON-files sent by the integration run.
Level | Field name | Format | Description  
---|---|---|---  
root | id | number | Always 0, integration supports only creation of new items, not updating  
root | personnumber | string | Personnumber of person. Must match person's personnumber in Visma LTR. Primarily person's Visma-identifier is used, if it is not set person's employee number is used.  
root | ts_start | string | Event start time, format YYYY-MM-DD HH:ii:ss  
root | ts_end | string | Event end time, format YYYY-MM-DD HH:ii:ss  
root | workid | numero | Always 0, integration supports only creation of new items, not updating  
root | title | string | Event type name  
root | description | string | Event description  
root | rows | Group of rows | Rows include information related to an event such as worked time by project and salary code, possible supplements etc.  
rows - group | row | A row related to the event | One row includes one item related to the event. For example each project, each salary code and each supplement will be in it's own row  
field under row | id | numero | Always 0, integration supports only creation of new items, not updating  
field under row | type | string |  Type of row
  * HO = hour transaction
  * TR = travel expense claim
  * SR = material event
  * IV = account of expenses

Can be overridden in a ruleset with fieldname `VismaLTRRowType`  
field under row | costcenter | string |  Person's cost centre. If Visma L7 project import has "Add cost centre into imported project code" set to "Yes", cost centre will be automatically set from project code. Can be overridden in a ruleset with fieldname `VismaCostCentre`  
field under row | letter | string |  Letter. Not set by default but can be set in a ruleset with fieldname `VismaLTRLetter` Letter must be found in LTR for export to succeed.  
field under row | wagetype | string |  Salary code  
field under row | ts_start | string |  Start time of item  
field under row | ts_end | string |  End time of item  
field under row | ts_directed | string |  Date that the item will be added to LTR. Can be overidden in a ruleset with fieldname `VismaLTRDirectedTimestamp` format YYYY-MM-DD 00:00:00  
field under row | costamount | number |  Amount of the item. If hour transaction, will contain hours. If row is a currency amount of TR (travel expense claim) or IV (account of expenses), is always 1 and the actual cost amount is set in costprice - field  
field under row | description | string |  Item description  
field under row | costprice | number | Expense currency amount. Used with row types TR (travel expense claim) and IV (account of expenses) when the expense amount is represented as a currency, such as euros.  
field under row | unit | string |  Unit in text format. Can be overridden in a ruleset with fieldname `VismaLTRUnit`  
field under row | project | string |  Main number project identifier. Must match the main number project identifier in Visma LTR. Can be overridden in ruleset rule with fieldname `VismaLTRProject`  
field under row | work | string |  Subnumber project identifier. Must match the sub number project identifier in Visma LTR. Can be overridden in ruleset rule with fieldname `VismaLTRWork`  
field under row | billingcode | string |  Billing code for the item, if in Visma LTR has been defined that the item's salarycode requires a billing code. Can be defined in the ruleset with the value `VismaLTRBillingCode`, if not required then should be left out of the rule  
field under row | status | numero |  State of approval,  
1 = Open  
2 = Accepted  
5 = No transfer  
Requires a license in Visma LTR that allows the changing of a row's approval status. If this should be exported, it must be defined in ruleset to be in the field `VismaLTRStatus`. If approval i transferred, also acceptor ja ts_accepted are exported  
field under row | acceptor | string |  If approved, name of approver. Will be exported automatically if status-row is exported as accepted  
field under row | ts_accepted | string |  If approved, time of approval. Will be exported automatically if status-row is exported as accepted  
field under row | tripreason | string |  Exported if a travel invoice, travel invoice description. Can be overridden in a ruleset with fieldname `VismaLTRTripReason`  
field under row | triproute | string |  Exported if a travel invoice, travel invoice routes. Can be overridden in a ruleset with fieldname `VismaLTRTripRoute`  
field under row | trippassenger | string |  Exported if a travel invoice, travel invoice passenger amount. Can be defined in a ruleset with fieldname `VismaLTRTripPassengerAmount`  
Example in JSON-format:
[code] 
    {  
      "id": 0,  
      "personnumber": "123456",  
      "ts_start": "2023-03-02 08:00:00",  
      "ts_end": "2023-03-02 16:00:00",  
      "workid": 0,  
      "title": "Työ",  
      "description": "",  
      "rows": [  
        {  
          "row": {  
            "id": 0,  
            "type": "HO",  
            "costcenter": "CostCenterName",  
            "wagetype": "40",  
            "ts_start": "2023-03-02 08:00:00",  
            "ts_end": "2023-03-02 16:00:00",  
            "ts_directed": "2023-03-02 00:00:00",  
            "costamount": 8,  
            "description": "",  
            "unit": "H",  
            "project": "SomeProjectCode",  
            "work": "SubProjectCode",  
            "billingcode": "987654321",  
            "status": 2,  
            "acceptor": "Acceptor Name",  
            "ts_accepted": "2023-03-04 16:00:00"  
          }  
        },  
        {  
          "row": {  
            "id": 0,  
            "type": "IV",  
            "costcenter": "CostCenterName",  
            "wagetype": "567890",  
            "ts_start": "2023-03-02 08:00:00",  
            "ts_end": "2023-03-02 16:00:00",  
            "ts_directed": "2023-03-02 00:00:00",  
            "costamount": 1,  
            "description": "",  
            "unit": "C",  
            "costprice": 51,  
            "project": "SomeProjectCode",  
            "work": "SubProjectCode",  
            "billingcode": "12345678",  
            "status": 2,  
            "acceptor": "Acceptor Name",  
            "ts_accepted": "2023-03-04 16:00:00"  
          }  
        }  
      ]  
    }
[/code]
