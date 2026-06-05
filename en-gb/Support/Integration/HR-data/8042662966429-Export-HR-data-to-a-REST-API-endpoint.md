---
id: 8042662966429
title: Export HR data to a REST API endpoint
url: https://support.nepton.com/hc/en-gb/articles/8042662966429-Export-HR-data-to-a-REST-API-endpoint
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
updated_at: '2024-08-23T09:59:00Z'
edited_at: '2022-12-13T11:21:28Z'
---

# Export HR data to a REST API endpoint

This article describes technical details on how to set up an external REST API endpoint for receiving HR data exported from Nepton via a scheduled person export. Details about setting up a scheduled task for person export including the REST API settings are described in [Scheduled task – person export](<https://support.nepton.com/hc/articles/360002489357>) page and data format specific pages for [CSV](<https://support.nepton.com/hc/articles/4405423095953>) and [JSON](<https://support.nepton.com/hc/articles/7982660700189>).
# Request message
This section describes the HTTP requests sent by Nepton platform when contacting an external REST API endpoint for exporting HR data. The contents of the data sent – according to selected data format – are described in [Export persons - Default CSV data format](<https://support.nepton.com/hc/en-gb/articles/4405423095953>) and [Export persons - JSON data format](<https://support.nepton.com/hc/en-gb/articles/7982660700189>) pages.
## REST API address
Scheduled person export task is using [HTTP PUT method](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT>) when contacting the REST API endpoint. The endpoint must support [TLS](<https://developer.mozilla.org/en-US/docs/Glossary/TLS>) protocol (address must be defined with https:// prefix).  
  
![mceclip4.png](https://support.nepton.com/hc/article_attachments/8043302516765)
## Authentication type
The selected authentication method determines the [Authorization header](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization>) value used when contacting the REST API service.
### No authentication
If "No authentication" is selected as the authentication type, the data is sent to service and no authentication options are expected to be required.
![mceclip6.png](https://support.nepton.com/hc/article_attachments/8211391152285)
### Basic HTTP authentication
Basic HTTP authentication adds an [Authorization header](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization>) with value "Basic" followed by a space and the "username" and "password" parameter values separated by colon – in username:password format – encoded as [UTF-8](<https://en.wikipedia.org/wiki/UTF-8>) bytes converted to [Base64](<https://en.wikipedia.org/wiki/Base64>) string.  
  
![mceclip5.png](https://support.nepton.com/hc/article_attachments/8043327434013)  
Example:
[code] 
    Authorization: Basic c2FtcGxldXNlcm5hbWU6YW0jbWFhNmZtMjh2bWYmR2xo
[/code]
where c2FtcGxldXNlcm5hbWU6YW0jbWFhNmZtMjh2bWYmR2xo is the _sampleusername:am#maa6fm28vm &Glh_ (parameter values username and password from scheduled task settings combined with colon) converted to Base64 string.
### OAuth 2.0 (Basic HTTP authentication)
OAuth 2.0 authorization contacts the given authorization service with [HTTP POST method](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST>) first, using [Authorization header](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization>) similar to Basic HTTP authentication. Authorization server must support [TLS](<https://developer.mozilla.org/en-US/docs/Glossary/TLS>) protocol (address must be defined with https:// prefix).
  
![mceclip6.png](https://support.nepton.com/hc/article_attachments/8043606311069)  
A successful response from authorization server should have a [JSON object](<https://en.wikipedia.org/wiki/JSON#Data_types>) as the body of the response. The object should have at least _access_token_ field defined. The format of the response (there may be more HTTP headers):
[code] 
    HTTP/1.1 200 OK
    Content-Type: application/json;charset=utf-8
    Content-Length: 119
    
    {
    	"access_token": "secret_access_token_value",
    	"token_type": "token_type",
    	"expires_in": 999999,
    	"scope": "scope"
    }
[/code]
The access_token field value is then passed to the given REST API service in Authorization header:
[code] 
    Authorization: Bearer _secret_access_token_value_
[/code]
where _secret_access_token_value_ is the _access_token_ field value from the authorization server response.
### Token authorization
Token authorization adds the parameter _apikey_ value to [Authorization header](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization>) with TOKEN prefix.
![mceclip7.png](https://support.nepton.com/hc/article_attachments/8044600701725)
Example Authorization header:
[code] 
    Authorization: TOKEN _secret_api_key_provided_
[/code]
where _secret_api_key_provided_ is the value of the _apikey_ parameter from scheduled task settings.
Scheduled task for person export will contact the service defined in REST API address using [HTTP PUT method](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT>) and adding an authorization header value based on the selected authentication type of the scheduled task.
## Security protocols
Endpoint and possible OAuth 2.0 authorization service must support [TLS protocol](<https://developer.mozilla.org/en-US/docs/Glossary/TLS>) and their addresses must be defined with https:// prefix. Currently we support TLS 1.2 and TLS 1.1 security protocols.
## 100-Continue behaviour
Before sending data, an initial request with [HTTP PUT method](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT>) is made with an [Expect header](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expect>) with value "100-continue", with all the other request headers included but without data as request body:
[code] 
    Content-Length: 25959
    Expect: 100-continue
[/code]
A [HTTP response 100](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100>) (continue) is expected as indication for successful authentication and acceptance of the details in the headers before sending the actual data:
[code] 
    HTTP/1.1 100 Continue
[/code]
If the server cannot accept the request, it can respond with [HTTP response 417](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/417>) (expectation failed):
[code] 
    HTTP/1.1 417 Expectation Failed
[/code]
or another appropriate response, e.g., [HTTP response 401](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401>) (unauthorized):
[code] 
    HTTP/1.1 401 Unauthorized
[/code]
## Content type
Content type of the request is presented as [Content-Type header](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type>) value as the [media type](<https://developer.mozilla.org/en-US/docs/Glossary/MIME_type>) of the contents to be sent ("application/json" for [JSON](<https://support.nepton.com/hc/en-gb/articles/7982660700189>) format, "text/csv" for [CSV](<https://support.nepton.com/hc/en-gb/articles/4405423095953>) format), followed by ";charset=" and the encoding of the contents (either "utf-8" for [UTF-8](<https://en.wikipedia.org/wiki/UTF-8>) (Unicode character set) encoding or "iso-8859-1" for [ISO-8859-1](<https://en.wikipedia.org/wiki/ISO/IEC_8859-1>) ("Latin 1") encoding).
Examples:
[code] 
    Content-Type: application/json;charset=utf-8
[/code]
[code] 
    Content-Type: text/csv;charset=iso-8859-1
[/code]
## Content length
The length of the exported HR data file in bytes is sent as [Content-Length header](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Length>) value.
Example:
[code] 
    Content-Length: 3909
[/code]
# Response message
This section describes the HTTP responses expected by Nepton platform when it has exported HR data to an external REST API endpoint.
## Responses for sending a JSON file
### Transport was successful – reports by individual entries
Nepton platform expects an [HTTP response status code of a success](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses>) (status code in range 200 – 299) (e.g. status code 200: OK), if the service handling the remote endpoint received the transported data successfully.
The response body must be [a JSON object](<https://en.wikipedia.org/wiki/JSON#Data_types>) – and the object must contain statuses for the individual person entries in the export message. The key names expected in the JSON object response:
  * "Status" key. It should have a matching value with text "Success" to indicate the export file could be processed – there could still have been problems in handling individual persons' information entries. If the Status value is "Error" – or anything else than "Success" – then it is reported to platform that no information could be processed.
  * "StatusByEmployee" key as an array of JSON objects matching each individual person included in the person export file. Each person JSON object should then contain the following key names:  

    * "EmployeeNeptonId" – mandatory key with a matching string value containing the [Nepton Id](<https://support.nepton.com/hc/en-gb/articles/8017902121885>), NeptonPersonGUID field value from the person export file.
    * If the handling of the individual person's information was successful, there should be **one or more of the following key names** in the StatusByEmployee object so that the individual person export is considered a success. The values for these keys should be JSON objects with at least one key name. Format of information of the values is currently not limited: 
      * Added
      * Modified
      * NoChanges
      * RemovedInfo
    * If the handling of the individual person's information was a failure or there were any kinds of warnings, one or both of the following key names should be included. Their values are logged in the [service log](<https://support.nepton.com/hc/en-gb/articles/360002575478>) warning entry and the export for the individual person is considered a failure: 
      * FatalError (errors preventing the whole handling)
      * Warnings
  * There may be other keys included either in the main object or within the StatusByEmployee objects. This information is not currently handled, but _any_ information in the response may end up in a corresponding [service log](<https://support.nepton.com/hc/en-gb/articles/360002575478>) entry.


Example (there may be more HTTP headers):
[code] 
    HTTP/1.1 200 OK
    Content-Type: text/plain; charset=utf-8
    Content-Length: 917
    
    {
    	"Status": "Success",
    	"StatusByEmployee": [
    		{
    			"EmployeeNeptonId": "206894AF-E2E6-5F11-B988-DD9E52BD067A",
    			"Added": {
    				"Field1": "Success",
    				"Field2": "Success",
    				"Field3": "Success"
    			},
    			"Modified": {
    				"Field4": "Success"
    			},
    			"NoChanges": {
    				"Field5": "Success"
    			},
    			"RemovedInfo": {
    				"Field6": "Success"
    			},
    			"AnyInformation": "There may be additional member fields - they won't interfere with the interpretation"
    		},
    		{
    			"EmployeeNeptonId": "D9D6AA30-58A9-43E4-A66A-12193A71C25E",
    			"Modified": {
    				"Field1": "Success"
    			},
    		},
    		{
    			"EmployeeNeptonId": "2CA5D9DF-5B57-446A-879B-FC8F704FA0F7",
    			"FatalError": "Mandatory field missing: \"Personal identity code\" is required by the XX system",
    		},
    		{
    			"EmployeeNeptonId": "FEE31CF4-B4BF-4DDF-ADAD-5ACB1B8CD130",
    			"Warnings": "Invalid value: \"Additional administrative information\" (\"1CC\")"
    		}
    	]
    }
[/code]
### Transport failed
It is recommended that a [HTTP response status code of a success](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses>) (status code in range 200 – 299) is sent if there was no transport related error and inform about the specific details in the format described below. If the server just needs to inform that receiving failed or the service could not process information at all, it may alternatively send an error response – [HTTP client error response](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses>) (status code in range 400 – 499), a [HTTP server error response](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses>) (in range 500 – 599) or any other response classified as an error – and it will be logged in [service log](<https://support.nepton.com/hc/articles/360002575478>) error entry.
If the response body consists of a JSON object with "Status" key name with matching value of "Error" – or anything else than "Success" – or if there is a message included in the matching value for "ErrorMessage" key name, the whole export operation is considered as failed. Any error message in "ErrorMessage" value will be logged in [service log](<https://support.nepton.com/hc/articles/360002575478>) error entry.
Example (there may be more HTTP headers):
[code] 
    HTTP/1.1 200 OK
    Content-Type: application/json; charset=utf-8
    Content-Length: 64
    
    {
    	"Status": "Error",
    	"ErrorMessage": "Error message for log"
    }
[/code]
Errors and warnings for individual person entries within the person export file should not be reported as a failure in general but using the "FatalError" and "Warnings" keys within "StatusByEmployee" array objects, see Transport was successful – reports by individual entries.
## Responses for sending a CSV file
### Transport and handling were successful
If the service handling the remote endpoint received and could process the contents like expected, an [HTTP response status code of a success](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses>) (status code in range 200 – 299) is expected (e.g. status code 200: OK. No other information than the successful HTTP status code is required for a successful response when the contents were sent in CSV format. If any information is provided in the message body, it is logged as informational message in [service log](<https://support.nepton.com/hc/articles/360002575478>) success entry.
Example (there may be more HTTP headers):
[code] 
    HTTP/1.1 200 OK
    Content-Type: text/plain; charset=utf-8
    Content-Length: 2
    
    OK
[/code]
### Transport or handling failed
A non-success HTTP code is expected in case there was any problem either in transporting to or handling of the data in the service handling the remote endpoint. That code may be a [HTTP client error response](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses>) (status code in range 400 – 499), a [HTTP server error response](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses>) (in range 500 – 599) or any other response classified as an error. The response code and any information received in the body of result is then included in [service log](<https://support.nepton.com/hc/articles/360002575478>) error entry.
Example (there may be more HTTP headers):
[code] 
    HTTP/1.1 500 Internal Server Error
    Content-Type: text/plain; charset=utf-8
    Content-Length: 54
    
    An unexpected error occurred while processing the data
[/code]
