---
id: 360009018778
title: Helper functions for rulesets
url: https://support.nepton.com/hc/en-gb/articles/360009018778-Helper-functions-for-rulesets
locale: en-gb
category: Support
category_id: 360000446658
section: Rulesets
section_id: 360000827378
section_path:
- Integration
- Rulesets
labels:
- pyöristys
- pyöristäminen
promoted: false
updated_at: '2026-03-09T08:30:12Z'
edited_at: '2026-01-08T12:42:46Z'
---

# Helper functions for rulesets

When writing ruleset extraction rules, in addition to SQL Lite functions, auxiliary functions implemented for the service are available. With helper functions, it is easier to handle, for example, strings in SQL Lite.
### List of available helper functions and their operation
  * **substring_part**. Parameters: (sourceString, separator, index). The function splits the given string sourceString with the given separator string separator. The return value consists of as much data content as the index value indicates. If the string does not contain this element, NULL is returned. A negative index returns the element pointed to by the index calculated from the last results. -1 returns the last element, -2 returns the second to last, and so on.  

  * **substring_index()** <https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_substring-index>  

  * **sql_left()** <https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_left>  

  * **sql_right()** <https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_right>  

  * **concat()** <https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_concat>  

  * **if()** <https://dev.mysql.com/doc/refman/8.0/en/control-flow-functions.html#function_if>  

  * **timestamp()** <https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_timestamp>  

  * **strftime(format,timestring)** Returns the 'timestring' formatted according to the 'format' string provided. For example, strftime('%Y %m %d', 'now', 'localtime') would extract the Year Month and Day for the current date.  

  * **curdate()** Returns the current date according the server's local timezone (Finland). Format YYYY-MM-DD  

  * **curtime()** Returns the current time according to the server's local timezone (Finland). Format H:i:s  

  * **now()** Returns the current date and time according to the server's local timezone (Finland). Format YYYY-MM-DD HH:MM:SS  

  * **weekday(date/datetime/timestamp)** Returns the day of the week as a number based on the provided date or time. 0 (for Monday) through 6 (for Sunday). For example, if you want to filter out Saturdays and Sundays, you can add the following line to the code: AND weekday(salaryrenderingdate) NOT IN (5, 6)  

  * **ceil(decimal)** Round a decimal up to the nearest whole number  

  * **floor(decimal)** Round a decimal down to the nearest whole number  

  * **round(decimal)** Round a decimal to a specific amount of digits.  

  * **minutesToHHMM(decimal)** Converts the amount of minutes to HH:MM format. The value is not rounded. For example `minutesToHHMM(270.8)` would return 04:30. If rounding is needed, it needs to be done specifically, for example `minutesToHHMM(round(270.8))`  

  * **minutesToHHMMSS(decimal)** Converts the amount of minutes to HH:MM:SS format. For example `minutesToHHMMSS(270.8)` would return 04:30:48.  

  * **secondsToHHMM(decimal)** Converts the amount of seconds to HH:MM format. The value is not rounded. For example `secondsToHHMM(16248)` would return 04:30. If rounding is needed, it needs to be done specifically, for example `minutesToHHMM(round(16248 / 60.0))`  

  * **secondsToHHMMSS(decimal)** Converts the amount of seconds to HH:MM:SS format. For example `secondsToHHMMSS(16248)` would return 04:30:48.  

  * **isAnniversary(**  
<currentDate>,  
<date to test e.g. birthday, contract start date, etc>,  
<years as string CSV that you want to match e.g. "5,10" for 5th and 10th anniversary>,  
<number of days to match beforehand e.g. 14 could be used to remind about anniversaries 2 weeks before the anniversary> **)**  
It will return the matching year e.g. if the current date is the 5th anniversary of the contract start date it returns 5, if not, it returns null.   
**Example:**  
**![](https://support.nepton.com/hc/article_attachments/33078355689757)**
