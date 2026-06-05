---
id: 4406446686609
title: Responses and result codes of HR API
url: https://support.nepton.com/hc/en-gb/articles/4406446686609-Responses-and-result-codes-of-HR-API
locale: en-gb
category: Support
category_id: 360000446658
section: HR API
section_id: 4406143245713
section_path:
- Integration
- API
- HR API
labels:
- response code
- Vastauskoodi
promoted: false
updated_at: '2025-09-08T07:36:13Z'
edited_at: '2025-09-08T07:36:13Z'
---

# Responses and result codes of HR API

This article describes the responses of the HR API and information about the different result codes and their meaning. 
Responses are made using XML SOAP. Below is an example of a response and a detailed breakdown of the nodes. Please note that FunctionResponse and FunctionResult would be replaced by real function names.
## Example Response XML
[code] 
    <soap:Envelope xmlns:soap="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:xsd="<http://www.w3.org/2001/XMLSchema>">  
      <soap:Body>  
         <FunctionResponse xmlns="<http://tempuri.org/>">  
            <FunctionResult>  
               <ResultCode>8</ResultCode>  
               <ResultMessage>Failure. Please see breakdown for more details.</ResultMessage>  
               <ResultBreakdown>  
                  <ArrayOfString>  
                     <string>ERROR: Tuontikenttää 'TEST_HEADER_001' ei tunnistettu</string>  
                     <string>ERROR: Tuontikenttää 'TEST_HEADER_002' ei tunnistettu</string>  
                  </ArrayOfString>  
               </ResultBreakdown>  
            </FunctionResult>  
         </FunctionResponse>  
      </soap:Body>  
    </soap:Envelope>
[/code]
## Response breakdown
**Node** |  **Optional** |  **Description**  
---|---|---  
ResultCode |  No |  This code indicates the overall result for the import action. Anything other than result code 100 indicates a problem was encountered. Please see the Result Codes heading below, for more information on specific code meanings.  
ResultMessage |  No |  This is a human-friendly message for the overall result of the import action. It is primarily intended for debugging.  
ResultBreakdown |  No |  A container for the breakdown of any problems or warnings encountered.  
ArrayOfString |  Yes |  List of any problems or warnings encountered. If there are no problems encountered this node may not be present in the response.  
string |  Yes |  Each ArrayOfString node may contain a collection of string nodes. Each of these indicates an error or warning related to the import index.  
## Result Codes
Below are the result codes returned in the ResultCode field. Response code "1000" indicates complete success. Any other value, even an empty one, indicates a problem was encountered and should be investigated using the Nepton Service log, and logs from the software making the request. In case result codes 1 - 10, it can be assumed that the API request failed, and no actions were performed (e.g. no persons were imported).
**Result Code** |  **Result Type** |  **Description**  
---|---|---  
1000 |  Success |  No Errors. A good result  
998 |  Warning |  The result was empty. In most cases, this can be considered an error  
999 |  Error |  Unexpected or unknown error encountered. This usually indicates an unhandled exception was encountered.  
1 |  Error |  Invalid Password  
2 |  Error |  Invalid Deployment Id  
3 |  Error |  Access Denied Check the following if you get "Access Denied" response
  * Check that webservice password is correct. Password is unique to the customer deployment (Provided by Nepton).
  * Customer is active and not deleted
  * Person calling the webservice is active and not deleted

  
4 |  Error |  Invalid parameters. One or more of the parameters were poorly formed, incorrect or missing  
5 |  Error |  Not supported. Generic, target not supported response. Check breakdown for more details if available  
6 |  Error |  Not Found. Generic, target not found response. Check breakdown for more details if available  
7 |  Error |  Deployment settings not found. This usually indicates a poorly configured deployment  
8 |  Error |  Collection contains errors. There were one or more errors encountered in the collection.  
9 |  Error |  Encoding Failure  
10 |  Error |  Not Recognised. Generic, target not recognised response. Check breakdown for more details if available
