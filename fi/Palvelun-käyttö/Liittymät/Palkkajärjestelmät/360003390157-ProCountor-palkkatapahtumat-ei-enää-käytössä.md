---
id: 360003390157
title: ProCountor palkkatapahtumat (ei enää käytössä)
url: https://support.nepton.com/hc/fi/articles/360003390157-ProCountor-palkkatapahtumat-ei-en%C3%A4%C3%A4-k%C3%A4yt%C3%B6ss%C3%A4
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2021-09-24T07:19:56Z'
---

# ProCountor palkkatapahtumat (ei enää käytössä)

Tätä siirtomuotoa ei tueta enää Procountorissa. Tiedostomuotoa käytettiin siirtotiedostoissa ennen Tulorekisterin aikakautta. Tuetun siirtomuodon kuvaus löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360003356978>)  
## Tiedostomuoto
Siirtotiedosto on csv-muotoinen ProCountor – vakiomallin mukainen tiedosto. Tiedostossa on kolmenlaisia tietorivejä.
  * Työntekijätiedot
  * Projektikohdenteet
  * Palkkalajit


Aineisto muodostuu työntekijä kerrallaan seuraavalla tavalla. Alla oleva rakenne toistuu aineistossa kaikille niille työntekijöille, joita aineistossa siirretään.
  * Tiedostoon muodostuu ensin työntekijärivi,
  * Tämän jälkeen muodostuu projektirivit niille projekteille, joihin kohdistusta on tehty.
  * Tämän jälkeen muodostuu palkkalajit niille palkkakoodeille, joita työntekijä on tehnyt palkkajaksolla.


##  Rajaukset
Ei rajauksia
## Aineiston tietueet 
## Row type P - employee row
**Column** |  **Field** |  **Integration query field  
** |  **Type** |  **Notes**  
---|---|---|---|---  
A |  Row type |  Set automatically |  string |  Always with value "P"  
B |  Social security number |  Set automatically |  string |  Employees social security number  
C |  Amount |  Set automatically |  decimal, comma as decimal separator |  Number of hours. For hourly paid the number of hours is transferred. For monthly paid amount of ‘1’ is transferred. ‘Basic work salary code’ in ProCountor settings is used to detect whether user is monthly paid or hourly paid. If salary code is 0, user is treated as monthly paid. Note that this cannot be configured with ruleset nor employee salary type.  
D |  Number of tax days |  ProcounterPRowNumberOfTaxDays |  decimal, comma as decimal separator |  Left empty in export. Overridden by ProcounterPRowNumberOfTaxDays  
E |  Number of work days |  Amount |  decimal, comma as decimal separator |  Amount of worked days  
### 
###  Row type D - project dimension row
**Column** |  **Field** |  **Integration query field  
** |  **Type** |  **Notes**  
---|---|---|---|---  
A |  Row type |  Set automatically |  string |  Always with value "D"  
B |  Dimension type |  ProcounterDRowDimensionType |  string |  Always with value "L". Overridden by ProcounterDRowDimensionType.  
C |  Dimension name |  ProjectCode1 |  string |  Project code  
D |  Payslip title |  ProcounterDRowPayslipTitle |  string |  Left empty in export. Overridden by ProcounterDRowPayslipTitle.  
E |  Percentage |  Amount |  decimal, comma as decimal separator |  Percentage amount of worked hours for this project  
### 
###  Row type R - salary code breakdown row
**Column** |  **Field** |  **Integration query field  
** |  **Type** |  **Notes**  
---|---|---|---|---  
A |  Row type |  Set automatically |  string |  Always with value "R"  
B |  Pay grade code |  SalaryCode |  string |  Salary code  
C |  Pay grade name |  ProcounterRRowPaygradeName |  string |  Left empty in export. Overridden by ProcounterRRowPaygradeName  
D |  Amount |  Amount |  decimal, comma as decimal separator |   
E |  Hourly rate |  ProcounterRRowHourlyRate |  decimal, comma as decimal separator |  Left empty in export. Overridden by ProcounterRRowHourlyRate.
