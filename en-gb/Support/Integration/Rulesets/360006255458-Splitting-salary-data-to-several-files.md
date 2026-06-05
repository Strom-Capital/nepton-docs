---
id: 360006255458
title: Splitting salary data to several files
url: https://support.nepton.com/hc/en-gb/articles/360006255458-Splitting-salary-data-to-several-files
locale: en-gb
category: Support
category_id: 360000446658
section: Rulesets
section_id: 360000827378
section_path:
- Integration
- Rulesets
labels: []
promoted: false
updated_at: '2024-11-01T11:58:17Z'
edited_at: '2023-10-25T06:56:39Z'
---

# Splitting salary data to several files

It is**** possible to split ruleset results to several files. It could be needed for example to:
  * _Create results as file per cost group_ \- each cost group would have its own file, see example 1
  * _Create results as file per project_ \- each project would have its own file
  * _Specific files contain results for specific cost groups_ \- see Example 2
  * _Create results as file per payment group_ \- each payment group would have its own file, see example 3


Please note that no empty files are generated. If you split by default cost group and one doesn't have any data for it, there will be no file.
## Configuring export file splitting
![export_file_splitting.png](https://support.nepton.com/hc/article_attachments/360013885897)
Settings for export file splitting can be found right after data query configuration fields in integration ruleset settings. At least settings "Split to file by values" and "Group salary table data by" must be defined.
Note: Settings cannot be empty for tables used in data query configuration fields. If, for example, UserEventData table is used in data query configuration fields, then also Group event table data by setting has to be used. Otherwise data query does not return results related to this table.
Follow these steps to configure it:
  1. "Split to file by values" - This setting defines the specific values/concepts that we will use to split the data on. This doesn't have to be an actual value in the export/rules but must be a single column of unique value that we can use for comparison in the subsequent setting queries.  
  

  2. "Group salary table data by", "Group event table data by" and "Group event history table data by" - These settings define the data that is available to our integration ruleset for _each_ file, and so we need to filter that data based on the list of values we produced in step 1. The values from step 1 are accessible with `:splittingValue`and the query is repeated for every value in the list.  
  



"Name for split files" - Optional: Configure filename pattern. Use `[SplittingValue]` as a replace pattern. If you split data to files by default cost group, that pattern will be replaced with default cost group.  
  
If you for example want to have a file name that starts with the splitting value: `[SplittingValue]_exportToSomeSystem.csv`  
  
If you export data for example for two cost groups (with codes 1200 and 9001), the file names would be `1200_exportToSomeSystem.csv` and `9001_exportToSomeSystem.csv`  
Replace patterns in use. Please note that all time formats are in Finnish format.
_**[vvvvkkpphhmmss]**_ \- Date & time, for example _20181201120000_
_**[vvvvkkpphhmm]**_ \- Date & time without seconds, for example _201812011200_
_**[vvvvkkpp]**_ \- Date, for example _20181201_
_**[SplittingValue]**_ \- Value that is selected by query in "Split to files by values"
"Export files as zip" controls whether the split files will be exported to the SFTP server as a single zip file or unzipped individual files.
## Example 1 - Splitting data from any/all cost groups into separate files
This configuration will split the results of an ruleset into a single file for each cost group found from the ruleset query results. For example, if a results contained data for persons belonging to cost groups **A** , **B** , and **D** then those persons data will be divided into 3 files:
File "**A** _xxxxx.csv" containing data of persons belonging to cost group A
File "**B** _xxxxx.csv" containing data of persons belonging to cost group B
File "**D** _xxxxx.csv" containing data of persons belonging to cost group D
No other files are generated for users from other cost groups that weren't picked up by the original export. Likewise, file "**A** _xxxxx.csv" would not be created if the original export didn't contain data for people in cost group A.
"Split to files by values*" query:
[code] 
    SELECT DISTINCT IFNULL(DefaultCostGroup, '') FROM UserData
[/code]
"Group Salary table data by*" query:
[code] 
    SELECT * FROM UserSalaryData WHERE IFNULL(UserCostGroup, '') = :splittingValue
[/code]
"Group Event table data by*" query:
[code] 
    SELECT * FROM UserEventData WHERE IFNULL(UserCostGroup, '') = :splittingValue
[/code]
"Group Event history table data by*" query:
[code] 
    SELECT * FROM UserEventHistoryData WHERE IFNULL(UserCostGroup, '') = :splittingValue
[/code]
## Example 2 - Splitting by specific cost groups into specific files
This configuration will allow a results to be split into 2 files with:
  * "FileOne" containing results for cost groups **A** , **B** , and **C** ,
  * "FileTwo" containing results data for cost groups **D** and **E**


"Split to files by values*" query:
[code] 
    SELECT DISTINCT CASE   
    WHEN DefaultCostGroup IN('A', 'B', 'C') THEN 'FileOne'   
    WHEN DefaultCostGroup IN('D', 'E') THEN 'FileTwo'  
    END  
    FROM UserData
[/code]
"Group Salary table data by*" query:
[code] 
    SELECT   
    *   
    FROM UserSalaryData   
    WHERE   
    CASE   
    WHEN UserCostGroup IN('A', 'B', 'C') THEN 'FileOne'   
    WHEN UserCostGroup IN('D', 'E') THEN 'FileTwo'  
    END = :splittingValue
[/code]
Note: Both "Split to files by values*" and "Group Salary table data by*" queries should be defined in configuration.
Note: the list of cost groups can be changed, the number of files can be changed, the 'FileOne' and 'FileTwo' (which end up as prefixes to the filename) can be changed, but the query conditions and filenames must match in both queries.
## Example 3 - Splitting data from any/all payment groups into separate files
"Split to files by values*" query:
[code] 
    SELECT DISTINCT IFNULL(uid.Value, '')   
    FROM UserData as u   
    LEFT JOIN userinfodata AS uid ON (  
        u.userId = uid.userId AND  
        uid.InfoTypeName = 'NeptonPaymentGroupName_SDSQL'  
    )
[/code]
"Group Salary table data by*" query:
[code] 
    SELECT usd.*   
    FROM UserSalaryData AS usd   
    LEFT JOIN UserInfoData as uid ON (  
        usd.userId = uid.userId AND  
        uid.InfoTypeName = 'NeptonPaymentGroupName_SDSQL' AND  
        datetime(usd.salaryrenderingdate) BETWEEN uid.ValidFrom AND uid.ValidTo  
    )   
    WHERE IFNULL(uid.value, '') = :splittingValue
[/code]
"Group Event table data by*" query:
[code] 
    SELECT ued.*  
    FROM UserEventData AS ued   
    LEFT JOIN UserInfoData as uid ON (  
        ued.userId = uid.userId AND  
        uid.InfoTypeName = 'NeptonPaymentGroupName_SDSQL' AND  
        datetime(ued.startdatetime) BETWEEN uid.ValidFrom AND uid.ValidTo  
    )   
    WHERE IFNULL(uid.value, '') = :splittingValue
[/code]
"Group Event history table data by*" query:
[code] 
    SELECT ued.*   
    FROM UserEventHistoryData AS ued   
    LEFT JOIN UserInfoData as uid ON (  
        ued.userId = uid.userId AND  
        uid.InfoTypeName = 'NeptonPaymentGroupName_SDSQL' AND  
        datetime(ued.startdatetime) BETWEEN uid.ValidFrom and uid.ValidTo  
    )   
    WHERE IFNULL(uid.value, '') = :splittingValue
[/code]
In this example, the name of the payment group is used as the splitting value of the files, but with small modifications (some other InfoTypeName) you could, for example, use the code of the payment group as the splitting value.
In the statement: `IFNULL(uid.value, '')` the latter parameter sets an empty string as the splitting value for the rows without a payment group, but you can use some other string instead if you prefer.
Please note that both presented change options must be set in the same way for all splitting queries
## Example 4 - Splitting by fixed values
This configuration will allow a results to be split into 2 files with:
  * "monthly" containing results of montly paid persons
  * "hourly" containing results of hourly paid persons


"Split to files by values" query:
[code] 
    SELECT * FROM (VALUES ('monthly'), ('hourly'));
[/code]
"Group Salary table data by" query:
[code] 
    SELECT *   
    FROM UserSalaryData  
    WHERE EmployeeSalaryType = :splittingValue
[/code]
"Group Event table data by" query:
[code] 
    SELECT *   
    FROM UserEventData  
    WHERE EmployeeSalaryType = :splittingValue
[/code]
"Group Event history table data by" query:
[code] 
    SELECT *   
    FROM UserEventHistoryData  
    WHERE EmployeeSalaryType = :splittingValue
[/code]
## Handling of several files in export
Manual export from UI - files are served in a ZIP archive
Scheduled export - files are served in a ZIP archive
Public web service - _ResponseString_ element will contain the ZIP archive data in base64 encoded format
### How it works
When splitting to several files, there basically are 3 steps on how the data is generated:
Getting values to split by, for example default cost group (one file for one cost group)
Create new temporary tables for UserSalaryData and UserEventData and populate them with data specific for split by value (for example a specific default cost group). This is done for each selected value in step 1
Execute ruleset queries on tables created in step 2.
