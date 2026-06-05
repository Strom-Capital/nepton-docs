---
id: 15468480461085
title: Supported file formats for ReturnFormat
url: https://support.nepton.com/hc/en-gb/articles/15468480461085-Supported-file-formats-for-ReturnFormat
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
updated_at: '2023-12-14T10:53:20Z'
edited_at: '2023-12-14T10:53:00Z'
---

# Supported file formats for ReturnFormat

[RunIntegrationRulesetV2](<https://support.nepton.com/hc/en-gb/articles/360014449458>) \- method (and later versions of the method) can be configured to run the integration ruleset with the desired file format by defining the format in the ReturnFormat - field of the request. If ReturnFormat - field value is `formatDefinedInRulesetSettings`, the format configured for ruleset in user interface is used.
Following values are allowed for defining file format in ReturnFormat - field:
  * `CgiPalkat_format_absences` \- CGI Palkat absences
  * `CgiPalkat_format_salary` \- CGI Palkat salary data
  * `CgiPalkat_format_vacations` \- CGI Palkat vacations
  * `CgiPrima_format_prabsences` \- CGI Prima absences
  * `CgiPrima_format_prsalary` \- CGI Prima salary data
  * `CgiPrima_format_prvacations` \- CGI Prima vacations
  * `CustomExport_format_csv` \- Custom export in csv format. Requires that [custom export](<https://support.nepton.com/hc/en-gb/articles/10758741671581>) is defined.
  * `CustomExport_format_xlsx` \- Custom export in xlsx format. Requires that [custom export](<https://support.nepton.com/hc/en-gb/articles/10758741671581>) is defined.
  * `DigiaEnterprise`
  * `DLSoftware_format_DLWPLPT3`
  * `DLSoftware_format_DLWPLPT8`
  * `Efina` \- Administer eFina
  * `Emce`
  * `Fivaldi_format_CSV` \- Visma Fivaldi, events in csv format
  * `Fivaldi_format_XML` \- Visma Fivaldi, events in xml format
  * `Heeros`
  * `Hogia`
  * `Intime`
  * `Lemonsoft`
  * `Lessor5`
  * `Liksa`
  * `Mepco` \- Accountor Mepco salary data
  * `Mepco_format_absences` \- Accountor Mepco absences
  * `Mepco_format_yearleave` \- Accountor Mepco vacations
  * `MicrosoftAx_format_balance` \- Microsoft AX balance events
  * `MicrosoftAx_format_bookkeeping` \- Microsoft AX bookkeeping
  * `MicrosoftAx_format_invoice` \- Microsoft AX invoice
  * `NeptonPayroll`
  * `Netvisor`
  * `PalkkaFi`
  * `Pegasos` \- CGI Pegasos
  * `Populus`
  * `Procountor_format_1` \- Accountor Procountor events (decommisioned)
  * `Procountor_format_2` \- Accountor Procountor events breakdown
  * `Scala` \- Epicor Scala
  * `SDWorx_format_W` \- SD Worx events
  * `SDWorx_format_W_absence` \- SD Worx absences
  * `SDWorx_format_W_holiday` \- SD Worx vacations
  * `Sedab` \- Digia Sedab
  * `Sgwi` \- Safeguard Global
  * `Sonet` \- CGI Sonet short interface
  * `SonetCSV` \- CGI Sonet parameterised interface
  * `Tikon` \- Accountor Tikon
  * `Visma_format_csv` \- Visma Nova working hours
  * `Visma_format_csv-payroll-absences` \- Visma Payroll absences
  * `Visma_format_csv-payroll` \- Visma Payroll salary data
  * `Visma_format_csv-salary` \- Visma Nova salary data
  * `Visma_format_fixed-width` \- Visma L7
  * `Visma_format_xml` \- Visma Lön
  * `VismaLTR` \- Visma LTR
  * `VismaPersonecF` \- Visma Personec F events
