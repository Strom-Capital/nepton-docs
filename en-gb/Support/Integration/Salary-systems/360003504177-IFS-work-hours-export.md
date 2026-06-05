---
id: 360003504177
title: IFS work hours export
url: https://support.nepton.com/hc/en-gb/articles/360003504177-IFS-work-hours-export
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
updated_at: '2025-08-28T11:53:35Z'
edited_at: '2025-08-28T11:51:58Z'
---

# IFS work hours export

Nepton can be configured to send work hour, project/work order, and salary data to IFS. Data is sent when saving activities and when doing other calendar related actions (see Export Trigger section for more information). Events will not be saved unless IFS returns a positive response, otherwise any errors from IFS will be shown to the user.
If [assumed events](<https://support.nepton.com/hc/en-gb/articles/360002558717>) are used, their data will get sent to IFS when they are approved.
The data that is sent is configured using an integration ruleset in the settings. A SOAP web service on IFS (or an intermediate system such as BizTalk) is required to send the data to. The WSDL schema for this web service is described below.
## Setup instructions
**1) Set up employees**
The person IDs for the export can be set up in Employees by editing a person's information and clicking on the Identifiers tab and then editing the IFS field. Note that if person's IFS ID is not set, personnel number is used instead.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360004728197)
**2) Set up what is sent to IFS**
Integration ruleset guidance is available in [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>). To enable a ruleset to be used with IFS work hours export, please contact Nepton support [platform-support@nepton.com](<mailto:platform-support@nepton.com>).
**3) Configure sending data to the web service**
The following information needs to be set on working community settings or setting group settings. You can find the settings by opening the created integration ruleset settings and scrolling down to Export options.
  * Export format - Select "IFS Salary data"
  * Export web service address - The web service endpoint address where data is sent to


You can additionally set API key to be used for authentication. The information is sent in HTTP headers as `TOKEN` header.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/4419579094417)
## Limitations
  * Persons with personnel number 0 will not be included
  * If response returns a failure, saving the event is prevented


## Export trigger
The export is not scheduled but is triggered in real-time for a user whenever they make certain changes to data. We *simulate* what the changes to the calculations will be so we can check with IFS that the changes are ok before sending them. Here is a list of the currently supported triggers:
  * Whenever an event is saved from any source, except when approving events
  * When work day length is overridden on the calendar for a day
  * When work week length is overridden on the calendar for a week
  * When permitted or expected work times are overridden on the calendar for a day


## Sent data
Salary data is queried and sent per user for an entire salary week. This is because if there are changes at the beginning of the week, this can affect salary earned at the end of the week. In certain situations, a change made to the current day may affect calculations for the previous day. In this case, the previous day will also be sent. Most often, this is related to a situation where entries falling under an overnight shift / assumed working hours are calculated according to the shift start date.
The format of a typical piece of salary data of a user salary event is listed below (please refer to their WSDL for the exact specification):
Level | Field name | Ruleset field | Format | Occurs | Notes  
---|---|---|---|---|---  
Root,  
under SOAP body | SALARY_EXPORTS |  | XML element | 1 |   
1 | EXPORT_START_DATE |  | datetime | 1 | Exported period start datetime, format `YYYY-MM-DD'T'HH:MM:SS[Z|(+|-)hh:mm]`  
1 | EXPORT_END_DATE |  | datetime | 1 | Exported period start datetime, format `YYYY-MM-DD'T'HH:MM:SS[Z|(+|-)hh:mm]`  
1 | EMP_ID | _Added automatically, can't be replaced_ | string (100) | 1 | Employee ID of the employee whose events are exported  
1 | SALARY_EXPORT |  | XML element | 0..n |   
2 | SALARY_DATE | SalaryRenderingDate | datetime | 1 | The date is used that the shift belongs to e.g. if it is a Monday shift that goes overnight, Monday's datetime is used. Format `YYYY-MM-DD'T'HH:MM:SS[Z|(+|-)hh:mm]`  
2 | COMPANY_ID |  | string (20) | 0..1 | Root user group code of the child user group person belongs to  
2 | AMOUNT | Amount | decimal | 1 | For example amount of units or decimal hours  
2 | PROJECT_CODE | ProjectCode1 | string (200) | 0..1 |  If project has an external identifier (`ProjectExternalIdentifier1`) set and project code (`ProjectCode1`) is not "DEFAULT", uses project's external identifier. In other cases project code (`ProjectCode1`) is used.  
2 | PROJECT_TYPE |  | string (10) | 0..1 |  If project has an external identifier (`ProjectExternalIdentifier1`) set and project code (`ProjectCode1`) is not "DEFAULT", transferred value will be "Project_sequence". If project has an external identifier and Project_sequence should not be set as the project type, project type can be overridden in the rule with IntegrationProjectType e.g. `SELECT *, CASE WHEN ProjectType1 != 'project_work' AND ProjectExternalIdentifier1 NOT NULL THEN ProjectType1 ELSE null END AS IntegrationProjectType FROM UserSalaryData` In other case project type internal name is used, such as "project_work".  
2 | SALARY_CODE | SalaryCode | string (100) | 0..1 | This will come from the dynamic salary code rules to identify the type of salary information we are sending.  
2 | COMMENT | Comment | string (2000) | 0..1 | Event comment / description  
2 | CRAFTREPORT_CODE | UserCostGroup | string (100) | 0..1 | Person's default cost group  
2 | ADDINFO |  | string (2000) | 0..1 | This field will not be sent by default, you have to use it in a rule set, e.g. 'SELECT ExternalIdentifier AS AddInfo'  
Request example:
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wo="http://WO.fi.TyoTeho.Schemas.Salary_Export">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <wo:SALARY_EXPORTS>  
          <EXPORT_START_DATE>2019-06-01T00:00:00+03:00</EXPORT_START_DATE>  
          <EXPORT_END_DATE>2019-06-03T00:00:00+03:00</EXPORT_END_DATE>  
          <EMP_ID>1240</EMP_ID>  
          <SALARY_EXPORT>  
            <SALARY_DATE>2019-06-01T00:00:00+03:00</SALARY_DATE>  
            <COMPANY_ID>CompanyID</COMPANY_ID>  
            <AMOUNT>7.50</AMOUNT>  
            <PROJECT_CODE>PRJ01</PROJECT_CODE>  
            <PROJECT_TYPE>project_work</PROJECT_TYPE>  
            <SALARY_CODE>100</SALARY_CODE>  
            <COMMENT>Saturday work</COMMENT>  
          </SALARY_EXPORT>  
          <SALARY_EXPORT>  
            <SALARY_DATE>2019-06-02T00:00:00+03:00</SALARY_DATE>  
            <COMPANY_ID>CompanyID</COMPANY_ID>  
            <AMOUNT>7.50</AMOUNT>  
            <PROJECT_CODE>PRJ02</PROJECT_CODE>  
            <PROJECT_TYPE>project_work</PROJECT_TYPE>  
            <SALARY_CODE>100</SALARY_CODE>  
            <COMMENT>Sunday work</COMMENT>  
          </SALARY_EXPORT>  
        </wo:SALARY_EXPORTS>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Expected response
This API requires a direct response for the sent request. Request format is the following:
Level | Field name | Format | Occurs | Notes  
---|---|---|---|---  
Root,  
under SOAP body | Response | XML element | 1 |   
1 | Success | boolean | 1 | Whether processing the sent salary data was successful or not  
1 | Message | string | 0..1 | Optional message, mainly used for error message in case of a failure  
Response example:
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://WO.fi.TyoTeho.Schemas.TimeReportResponse">  
      <SOAP-ENV:Body>  
        <ns1:Response>  
          <Success>true</Success>  
          <Message>MESSAGE</Message>  
        </ns1:Response>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
