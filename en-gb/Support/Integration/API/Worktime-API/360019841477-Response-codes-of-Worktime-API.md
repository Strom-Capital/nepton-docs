---
id: 360019841477
title: Response codes of Worktime API
url: https://support.nepton.com/hc/en-gb/articles/360019841477-Response-codes-of-Worktime-API
locale: en-gb
category: Support
category_id: 360000446658
section: Worktime API
section_id: 360005706218
section_path:
- Integration
- API
- Worktime API
labels:
- API
- vastauskoodit
- response code
promoted: false
updated_at: '2025-09-08T07:42:25Z'
edited_at: '2025-09-08T07:42:15Z'
---

# Response codes of Worktime API

This article describes the response codes and handling error responses of [Worktime API](<https://support.nepton.com/hc/articles/360004861558>) methods.
## Response codes
These are the response codes that can be returned in the ResponseCode field. See Handling error responses for more details.
  * 1000: All clear. No errors.
  * 1001: Authentication failed. Please check that the [CallerAuthentication](<https://support.nepton.com/hc/articles/360019983978#CallerAuthentication>) credentials provided are correct and the CustomerId is present.
  * 1002: The event was not found with the identifier given.
  * 1003: Person was not found with the identifier given.
  * 1004: Project was not found with the identifier given.
  * 1005: All settings required were not provided in the request.
  * 1006: Setting was not valid because of a missing identifier.
  * 1007: Setting was invalid.
  * 1008: Processing of the current setting failed.
  * 1009: Project was invalid.
  * 1010: Failure during database communication.
  * 1011: Delete operation failed in database.
  * 1012: Parameters were invalid.
  * 1013: Target dates were not found.
  * 1014: Setting was not recognised or is not supported.
  * 1015: No permission to access or modify the requested object.
  * 1016: Parameter provided is not supported.
  * 1017: Requested functionality is not supported by Nepton service.
  * 1018: There were too many failed login attempts by person or from IP. Login is temporarily locked.
  * 1019: One or more of the items listed failed processing - see Handling error responses.
  * 1020: Login failed because the account of the person is disabled.
  * 1021: Project module is not active
  * 1022: The user's calendar is locked or approved blocking the requested action
  * 1023: Unable to start activity, see full response for reason
  * 1024: Unable to end activity, see full response for reason
  * 1025: Validating the request has failed, check web service specific guidance and response details
  * 1026: Nepton service has been unable to sync changes to configured external systems
  * 999: An unexpected error occurred. The ResponseString of the message may provide more details. Please check that all the parameters given were correct. This may be also be due to an internal error in Nepton. You may need to report this error to Nepton.


## Handling error responses
When updating data to Nepton it is important to check that the ResponseCode is 1000. If the ResponseCode is anything but 1000, there is something that was not updated correctly. See the code explanations above. The ResponseString may contain general information, but to get information about where the problem exactly occurred, you need to check the details of the response.
For example, [InsertActivities](<https://support.nepton.com/hc/articles/360019840217#InsertActivities>) request returns a list of events as [Activity elements](<https://support.nepton.com/hc/articles/360019840217#ActivityInserted>) matching the [Activity elements in the request](<https://support.nepton.com/hc/articles/360019840217#ActivityToInsert>) with a Success field with value true for each field that was successfully added and false for events with any problems. Then the ErrorMessage element will contain the details of an individual problem related to that field.
It is the responsibility of the calling software to properly display or log the error messages related to individual messages. The error messages might not be found in Nepton later on.
