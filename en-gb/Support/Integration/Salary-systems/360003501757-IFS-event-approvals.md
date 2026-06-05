---
id: 360003501757
title: IFS event approvals
url: https://support.nepton.com/hc/en-gb/articles/360003501757-IFS-event-approvals
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
edited_at: '2024-05-08T11:26:57Z'
---

# IFS event approvals

## About
Nepton can be configured to send event approvals to IFS. Data is sent when approving or unapproving events. Approval or unapproval will not be saved unless IFS returns a positive response.
A SOAP web service on IFS (or an intermediate system such as BizTalk) is required to send the data to. The WSDL schema for this web service is described below.
## Setup instructions
**1) Set up employees**
The person IDs for the export can be configured in Employees by editing a person's information and clicking on the Identifiers tab and then editing the IFS field. Note that if person's IFS ID is not set, personnel number is used instead.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/11562524707485)
**2) Configure sending data to the web service**
The used web service end point and company name / identifier sent in the web service request can be configured in Worktime > Administration > Working community settings > Integrations > IFS Event approval. If API key authentication is used in the integration, it is set in the same place.
![](https://support.nepton.com/hc/article_attachments/11562499034909)
Web service endpoint and API key can be set on setting group level as well, from Worktime > Administration > Setting group > Setting group dronpdown: Desired setting group > Action drondpon: Setting group settings > Integrations > IFS Event approval.
## Limitations
  * Persons with personnel number 0 will not be included
  * If approving or unapproving a person's hours could not be processed by receiving end, action is not done in Nepton for that person
  * Single event approvals are not supported as approved / unapproved days are sent instead. To disable approval / unapproval of single events you can turn "Approve events by day" on from Worktime -> Administration -> Working community settings -> Work hours -> Event locking and approval.


## Export trigger
The export is not scheduled but is triggered in real-time when approving or unapproving events. Export is not triggered when approving single events.
## Sent data
Level | Field name | Format | Occurs | Notes  
---|---|---|---|---  
Root,  
under SOAP body | AUTHORIZE_REPORT | XML element | 1 |   
1 | COMPANY | string (20) | 0..1 | Company name / identifier which is given in integration settings  
1 | EMP_ID | string (11) | 0..1 | Employee ID of the employee approving / unapproving events  
1 | AUTHORIZE_TRANSACTIONS | XML element | 1 |   
2 | AUTHORIZE_TRANSACTION | XML element | 0..n |   
3 | START_DATE | date | 1 | Approved from date, format `YYYY-MM-DD`  
3 | END_DATE | date | 0..1 | Approved to date, format `YYYY-MM-DD`  
3 | STATE | string (1) | 1 | Approval state: 
  * 1 - approved
  * 0 - not approved

  
3 | AUTH_ID | string (20) | 1 | Employee ID of the employee whose events are being approved / unapproved  
Request example:
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wo="WO.fi.TyoTeho.Schemas.AuthorizationFromTyoTeho">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <wo:AUTHORIZE_REPORT>  
          <wo:COMPANY>CompanyID</wo:COMPANY>  
          <wo:EMP_ID>1230</wo:EMP_ID>  
          <wo:AUTHORIZE_TRANSACTIONS>  
            <wo:AUTHORIZE_TRANSACTION>  
              <wo:START_DATE>2019-06-01</wo:START_DATE>  
              <wo:END_DATE>2019-06-30</wo:END_DATE>  
              <wo:STATE>1</wo:STATE>  
              <wo:AUTH_ID>1240</wo:AUTH_ID>  
            </wo:AUTHORIZE_TRANSACTION>  
            <wo:AUTHORIZE_TRANSACTION>  
              <wo:START_DATE>2019-06-01</wo:START_DATE>  
              <wo:END_DATE>2019-06-30</wo:END_DATE>  
              <wo:STATE>1</wo:STATE>  
              <wo:AUTH_ID>1250</wo:AUTH_ID>  
            </wo:AUTHORIZE_TRANSACTION>  
          </wo:AUTHORIZE_TRANSACTIONS>  
        </wo:AUTHORIZE_REPORT>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Expected response
This API requires a direct response for the sent request. Request format is the following:
Level | Field name | Format | Occurs | Notes  
---|---|---|---|---  
Root,  
under SOAP body | Response | XML element | 1 |   
1 | Success | boolean | 1 | Whether sending approvals / unapprovals was successful or not  
1 | Message | string | 0..1 | Optional message, used for error message in case of a failure or returning a list of IFS IDs / personnel numbers for persons whose event approval / unapproval was successful. Personnel numbers are comma separated.  
Response example:
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://WO.fi.TyoTeho.Schemas.TimeReportResponse">  
      <SOAP-ENV:Body>  
        <ns1:Response>  
          <Success>true</Success>  
          <Message>1011,2011,3011</Message>  
        </ns1:Response>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
