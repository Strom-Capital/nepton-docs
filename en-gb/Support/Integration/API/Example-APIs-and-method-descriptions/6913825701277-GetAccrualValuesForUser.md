---
id: 6913825701277
title: GetAccrualValuesForUser
url: https://support.nepton.com/hc/en-gb/articles/6913825701277-GetAccrualValuesForUser
locale: en-gb
category: Support
category_id: 360000446658
section: Example APIs and method descriptions
section_id: 4410135708433
section_path:
- Integration
- API
- Example APIs and method descriptions
labels: []
promoted: false
updated_at: '2026-06-01T14:44:17Z'
edited_at: '2025-09-15T07:00:22Z'
---

# GetAccrualValuesForUser

## Interface overview
The service retrieves the values ​​of a person's accruals from a specific date. The accruals returned are those that have been specified to be calculated for the person.
Some of the accruals are enabled by default for every customer. These include "balance", "flexible bank" and "bank". Customers can also define their own custom accruals. The names of these accruals are visible in the query results, if they are enabled. All accruals are returned by the call. In addition to the accrual value, the method also returns the change in the accrual for that day.
The WSDL schema of the web service is publicly available [here](<https://time.nepton.com/WebService.php?WSDL>). The interfaces are described in general [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).
The occurrences column in the description determines whether a piece of information is mandatory in the call or not. Occurrences 0 means that the information in question does not need to be passed in the call. Occurrences 1 means that the information must appear once in the call. Occurrences 0..n means that the information in question can appear any number of times in the call. Occurrences 1..n means that the information in question must appear in the data at least once, but can appear more often.
## Sent data
**Level** | **Field name** | **Format** | **Occurences** | **Description**  
---|---|---|---|---  
0 | ParametersForGetAccrualValues | XML element | 1 | Root element below SOAP body  
1 | CallerAuthentication | XML element | 1 | Authentication details. See [authentication in worktime API](<https://support.nepton.com/hc/en-gb/articles/360019983978>).  
1 | UserPersonnelNumber | string | 1 | Personnel number of the person, whose accruals are being retrieved.  
1 | SalaryDate | date | 0..1 | Date on which the accrual values ​​are returned, in the format YYYY-MM-DD, e.g. "2016-12-31". Note: returns accrual values ​​at the end of all shifts on that day.  
### Call example
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForGetAccrualValuesForUser>  
          <CallerAuthentication /> <!-- Authentication is needed but not shown in this example -->  
          <UserPersonnelNumber>2345</UserPersonnelNumber>  
          <SalaryDate>2020-01-01</SalaryDate>  
        </tyo:ParametersForGetAccrualValuesForUser>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Response
**Level** | **Field name** | **Format** | **Occurences** | **Description**  
---|---|---|---|---  
0 | ReturnValueForGetAccrualValues | XML element | 1 | Root element below SOAP body  
1 | ResponseCode | int | 1 | A code that describes the success or failure of the request  
1 | ResponseString | string | 1 | A string description of the success or failure of the request  
1 | AccrualList | XML element | 1 | List of accruals  
2 | Accrual | XML element | 0..n | Accrual  
3 | InternalName | string |  | Internal string ID of the accrual  
3 | Name | string | 1 | The name of the accrual defined for the customer/according to the language used  
3 | Amount | string | 1 | Accrual value  
3 | ChangeAmount | string | 0..1 | Amount of change in the accrual from the previous day's value (not returned if there is no change)  
### Response example
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ReturnValueForGetAccrualValuesForUser>  
          <ResponseCode>?</ResponseCode>  
          <ResponseString>?</ResponseString>  
          <AccrualList>  
            <Accrual>  
              <InternalName>bank</InternalName>  
              <Name>pankki</Name>  
              <Amount>18</Amount>  
              <ChangeAmount>10</ChangeAmount>  
            </Accrual>  
          </AccrualList>  
        </tyo:ReturnValueForGetAccrualValuesForUser>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
