---
id: 360008827678
title: Titania fetching events
url: https://support.nepton.com/hc/en-gb/articles/360008827678-Titania-fetching-events
locale: en-gb
category: Support
category_id: 360000446658
section: Events
section_id: 360001061298
section_path:
- Integration
- Events
labels: []
promoted: false
updated_at: '2026-03-04T13:14:53Z'
edited_at: '2024-11-19T13:17:41Z'
---

# Titania fetching events

Nepton offers a SOAP web service endpoint for Titania, that facilitates fetching work events. Your instance of Titania must be configured to support this, which you can inquire from the Titania service provider.
A full description and the address of the related SOAP web service endpoint can be found here: [Worktime, absence and projects API](<https://support.nepton.com/hc/en-gb/articles/360004861558>)  
If Nepton API access has been limited by IP addresses set here Employees > Administration > Security > "Allow calls to Nepton API web services only from IP addresses listed below", the fetching IP needs to be given access to Nepton.
## Event export format
Titania handles events differently from Nepton. Events in Nepton are events of certain event types and have a start and an end time. Events in Titania are either begin or end events with one time.
For this reason, Nepton needs to do a conversion. For example the following events in Nepton:
  * 08:00 - 13:00 Work
  * 13:00 - 14:00 Training
  * 14:00 - 16:00 Work


Are converted into following, which is understood by Titania service:
  * 08:00 Begin (no reason code)
  * 13:00 End (training)
  * 14:00 Begin (no reason code)
  * 16:00 End (no reason code)


## Configuration
**1\. Setting person identifiers  
**
Titania uses personnel number or personal identification number (social security number) as person identifier. In some cases both might be used.
You can set person's personnel number by editing person's information in Employees -> Person's information view, in Identifiers section.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360008596217)
Person's personal identification number can be set by editing person's information in Employees -> Person's information view.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360008596277)
**2. Configuring event type codes and behavior  
**
These can be configured from Titania settings: Worktime -> Administration -> Working community settings -> External services -> Titania.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360008596377)
Following settings can be configured for each event type:
  * **Event type reason code** \- Titania will use this to identify the event type
  * **Treat event type as** \- Whether beginning of events of this event type are treated as in (begin) or out (end) stamp. The default value for this setting is displayed below.
  * **Treat event type as overtime** \- Is event type overtime or not. Recording overtime is explained in the examples below. This setting is only visible for event types that can earn overtime.


By default all events will be transferred even if there is no reason code set. If a certain event type must not be transferred, it's reason code must be defined as 0.
### Export options
The **Export file name** is not needed because a SOAP request is made via API.
## Event type configuration and usage Examples
### Training
In Titania, training is, in terms of stamps, an absence from basic work. When going to training in the middle of the working day, it is always stamped end (training).
Training is configured in the following way in Nepton:
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360008596497)
### Overtime
Overtime in Titania is either overtime done at the beginning of end of work shift and can be both as well. If person is working overtime at the beginning of the shift, he/she starts the day with in (overtime) stamp. There is no need for a separate stamp when starting normal work. The same principle is used when working overtime at the end of the shift. There is no separate stamp for starting overtime, the shift is just ended with out (overtime) stamp.
This can be achieved in Nepton by adding a new overtime event type and configuring it in the following way:
![mceclip2.png](https://support.nepton.com/hc/article_attachments/360008676358)
Overtime at the beginning of shift would be recorded to Nepton in the following way:
  * 06:30 - 08:00 Overtime
  * 08:00 - 16:00 Work


The following stamps would be exported to Titania:
  * 06:30 Begin (YT, overtime)
  * 16:00 End (no reason code)


Overtime at the end of shift would be recorded to Nepton in the following way:
  * 08:00 - 16:00 Work
  * 16:00 - 18:00 Overtime


The following stamps would be exported to Titania:
  * 08:00 Begin (no reason code)
  * 18:00 End (YT, overtime)


### Usage examples
Use case | Events in Nepton | Stamps transferred to Titania  
---|---|---  
Basic work shift, training in the middle of the day | 
  * 08:00 - 13:00 Work
  * 13:00 - 14:00 Training
  * 14:00 - 16:00 Work

|  Note! Reason code for training has been set to be `KO`
  * 08:00 Begin
  * 13:00 End (KO)
  * 14:00 Begin
  * 16:00 End

  
Private affairs at the end of the shift | 
  * 08:00 - 16:00 Work
  * 14:00 - 16:00 Private affairs

|  Note! Reason code for private affairs has been set to be `OA`
  * 08:00 Begin
  * 14:00 End (OA)

  
Private affairs at the beginning of the shift | 
  * 08:00 - 10:00 Private affairs
  * 10:00 - 16:00 Work

|  Note! Reason code for private affairs has been set to be `OA`
  * 10:00 Begin (OA)
  * 16:00 End

  
Private affairs at the beginning and at the end of the shift | 
  * 08:00 - 10:00 Private affairs
  * 10:00 - 14:00 Work
  * 14:00 - 16:00 Private affairs

|  Note! Reason code for private affairs has been set to be `OA`
  * 10:00 Begin (OA)
  * 14:00 End (OA)

  
Full day private affairs | 
  * 08:00 - 16:00 Private affairs

|  Note! Reason code for private affairs has been set to be `OA`
  * 08:00 End (OA)

  
Overtime at the end of the shift | 
  * 08:00 - 16:00 Work
  * 16:00 - 18:00 Overtime

|  Note! Reason code for overtime has been set to be `YT`
  * 08:00 Begin
  * 18:00 End (YT)

  
Overtime at the beginning of the shift | 
  * 06:00 - 08:00 Overtime
  * 08:00 - 16:00 Work

|  Note! Reason code for overtime has been set to be `YT`
  * 06:00 Begin (YT)
  * 16:00 End

  
Overtime at the beginning and at the end of the shift | 
  * 06:00 - 08:00 Overtime
  * 08:00 - 16:00 Work
  * 16:00 - 18:00 Overtime

|  Note! Reason code for overtime has been set to be `YT`
  * 06:00 Begin (YT)
  * 18:00 End (YT)

  
**Overnight shifts**
Use case | Events in Nepton | Stamps transferred to Titania  
---|---|---  
Basic work shift | 
  * Day 1 22:00 - Day 2 06:00 Work

| 
  * Day 1 22:00 Begin
  * Day 1 24:00 End
  * Day 2 00:00 Begin
  * Day 2 06:00 End

  
Overnight sick leave at the end of the shift | 
  * Day 1 22:00 - 23:30 Work
  * Day 1 23:30 - Day 2 06:00 Sick leave

|  Note! Reason code for sick leave has been set to be `SA`
  * Day 1 22:00 Begin
  * Day 1 23:30 End (SA)

  
Overnight sick leave (child sick) at the beginning of the shift | 
  * Day 1 22:00 - Day 2 01:00 Child sick
  * Day 2 01:00 - 06:00 Work

|  Note! Reason code for sick leave (child sick) has been set to be `LS`
  * Day 2 01:00 Begin (LS)
  * Day 2 06:00 End

  
Overnight overtime at the end of the shift | 
  * Day 1 14:00 - 22:00 Work
  * Day 1 22:00 - Day 2 01:15 Overtime

|  Note! Reason code for overtime has been set to be `YT`
  * Day 1 14:00 Begin
  * Day 1 24:00 End (YT)
  * Day 2 00:00 Begin (YT)
  * Day 2 01:15 End (YT)

  
## Request data
Level | Field name | Format | Occurrences | Definition  
---|---|---|---|---  
Root,  
under SOAP body | ParametersForGetTitaniaWorkingTimeEvents | XML element | 1 |   
1 | CallerAuthentication | XML element | 1 | More information about authentication [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).  
1 | organisation | XML element | 0..1 | Organization information. Not used.  
2 | code | string | 1 | Organization code  
2 | name | string | 0..1 | Organization name  
1 | period | XML element | 1 | Event export period.  
2 | beginDate | date | 1 | Period start date, format `YYYYMMDD`  
2 | endDate | date | 1 | Period end date, format `YYYYMMDD`  
1 | schedulingUnit | XML element | 1..n | Scheduling unit, used in Titania, no effect in Nepton  
2 | code | string | 1 | Scheduling unit code, used in Titania, no effect in Nepton  
2 | name | string | 0..1 | Scheduling unit name, used in Titania, no effect in Nepton  
2 | person | XML element | 0..n | Scheduling unit person to get events for.  
3 | SSN | string | 1 | Personal identification number. Can be empty if the person is searched by personnel number.  
3 | employeeId | string | 0..1 | Personnel number.  
3 | name | string | 0..1 | Person's name, not used.  
### Request example
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForGetTitaniaWorkingTimeEvents>  
          <CallerAuthentication /> <!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->  
          <period>  
            <beginDate>20200501</beginDate>  
            <endDate>20200531</endDate>  
          </period>  
          <schedulingUnit>  
            <code>E1100</code>  
            <name>Suunnittelupiste A</name>  
            <person>  
              <SSN/>  
              <employeeId>9001</employeeId>  
              <name>Yli Yhdeksän Tuhatta</name>  
            </person>  
            <person>  
              <SSN>999999-9999</SSN>  
            </person>  
          </schedulingUnit>  
        </tyo:ParametersForGetTitaniaWorkingTimeEvents>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Response data
Level | Field name | Format | Occurrences | Definition  
---|---|---|---|---  
Root,  
under SOAP body | ReturnValueForGetTitaniaWorkingTimeEvents | XML element | 1 |   
1 | ResponseCode | number | 1 |  Response code for request. Possible codes can be found [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>). Please note that code 1019 is only used in cases where one or more requested persons were not found.  
1 | ResponseString | string | 1 | Description for response code / response message.  
1 | schedulingUnit | XML element | 1..n | Scheduling unit. Response will list all requested scheduling units.  
2 | code | string | 1 | Scheduling unit code in request  
2 | name | string | 0..1 | Scheduling unit name in request  
2 | person | XML element | 0..n | Scheduling unit person.  
3 | ResponseCode | number | 1 | Code is either `1000` (everything OK) or `1003` (person not found)  
3 | ResponseString | string | 1 | Response code description.  
3 | SSN | string | 1 | Personal identification number in request.  
3 | employeeId | string | 0..1 | Personnel number in request.  
3 | name | string | 0..1 | Person's name in request.  
3 | stampedWorkingTimeEvents | XML element | 1 | Work hour stamps for person  
4 | event | XML element | 0..n | Work hour stamp  
5 | date | date | 1 | Stamp date, format `YYYYMMDD`  
5 | beginTime | time | 0..1 | Time for in stamps, format `HHMM`. Stamps only have begin or end time.  
5 | beginReasonCode | string | 0..1 | Reason code for begin stamp  
5 | endTime | time | 0..1 | Time for out stamps, format `HHMM`. Stamps only have begin or end time.  
5 | endReasonCode | string | 0..1 | Reason code for end stamp.  
### Response example
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://tyoaika.tyoteho.fi">  
      <SOAP-ENV:Body>  
        <ns1:ReturnValueForGetTitaniaWorkingTimeEvents>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors.</ResponseString>  
          <schedulingUnit>  
            <code>E1100</code>  
            <name>Suunnittelupiste A</name>  
            <person>  
              <ResponseCode>1000</ResponseCode>  
              <ResponseString>All clear. No errors.</ResponseString>  
              <SSN/>  
              <employeeId>9001</employeeId>  
              <name>Yli Yhdeksän Tuhatta</name>  
              <stampedWorkingTimeEvents>  
                <event>  
                  <date>20200505</date>  
                  <beginTime>0800</beginTime>  
                </event>  
                <event>  
                  <date>20200505</date>  
                  <endTime>2000</endTime>  
                  <endReasonCode>YT</endReasonCode>  
                </event>  
              </stampedWorkingTimeEvents>  
            </person>  
            <person>  
              <ResponseCode>1000</ResponseCode>  
              <ResponseString>All clear. No errors.</ResponseString>  
              <SSN>999999-9999</SSN>  
              <stampedWorkingTimeEvents>  
                <event>  
                  <date>20200505</date>  
                  <beginTime>0800</beginTime>  
                </event>  
                <event>  
                  <date>20200505</date>  
                  <endTime>1200</endTime>  
                  <endReasonCode>KO</endReasonCode>  
                </event>  
              </stampedWorkingTimeEvents>  
            </person>  
          </schedulingUnit>  
        </ns1:ReturnValueForGetTitaniaWorkingTimeEvents>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
