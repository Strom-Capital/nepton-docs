---
id: 15468480461085
title: Tuetut tiedostomuodot ReturnFormat - kentälle
url: https://support.nepton.com/hc/fi/articles/15468480461085-Tuetut-tiedostomuodot-ReturnFormat-kent%C3%A4lle
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels: []
promoted: false
updated_at: '2023-12-14T10:53:20Z'
edited_at: '2023-12-14T10:53:18Z'
---

# Tuetut tiedostomuodot ReturnFormat - kentälle

[RunIntegrationRulesetV2](<https://support.nepton.com/hc/fi/articles/360014449458>) \- metodilla ja sen myöhemmillä versioilla on mahdollista suorittaa sääntöjoukko halutussa tiedostomuodossa määrittämällä muoto lähetetyn pyynnön ReturnFormat - kentässä. Jos ReturnFormat -kenttään määritetään `formatDefinedInRulesetSettings`, käytetään sääntöjoukolle käyttöliittymässä asetettua tiedostomuotoa.
Seuraavat arvot ovat sallittuja tiedostomuodon määrityksiä ReturnFormat -kentälle:
  * `CgiPalkat_format_absences` \- CGI Palkat poissaolot
  * `CgiPalkat_format_salary` \- CGI Palkat palkka-aineisto
  * `CgiPalkat_format_vacations` \- CGI Palkat lomat
  * `CgiPrima_format_prabsences` \- CGI Prima poissaolot
  * `CgiPrima_format_prsalary` \- CGI Prima palkka-aineisto
  * `CgiPrima_format_prvacations` \- CGI Prima lomat
  * `CustomExport_format_csv` \- Mukautettu vienti csv-muodossa. Vaatii että [mukautettu vienti](<https://support.nepton.com/hc/fi/articles/10758741671581>) on määritetty.
  * `CustomExport_format_xlsx` \- Mukautettu vienti xlsx-muodossa. Vaatii että [mukautettu vienti](<https://support.nepton.com/hc/fi/articles/10758741671581>) on määritetty.
  * `DigiaEnterprise`
  * `DLSoftware_format_DLWPLPT3`
  * `DLSoftware_format_DLWPLPT8`
  * `Efina` \- Administer eFina
  * `Emce`
  * `Fivaldi_format_CSV` \- Visma Fivaldi, tapahtumat CSV-muodossa
  * `Fivaldi_format_XML` \- Visma Fivaldi, tapahtumat XML-muodossa
  * `Heeros`
  * `Hogia`
  * `Intime`
  * `Lemonsoft`
  * `Lessor5`
  * `Liksa`
  * `Mepco` \- Accountor Mepco palkka-aineisto
  * `Mepco_format_absences` \- Accountor Mepco poissaolot
  * `Mepco_format_yearleave` \- Accountor Mepco lomat
  * `MicrosoftAx_format_balance` \- Microsoft AX saldotapahtumat
  * `MicrosoftAx_format_bookkeeping` \- Microsoft AX kirjanpito
  * `MicrosoftAx_format_invoice` \- Microsoft AX myyntilasku
  * `NeptonPayroll`
  * `Netvisor`
  * `PalkkaFi`
  * `Pegasos` \- CGI Pegasos
  * `Populus`
  * `Procountor_format_1` \- Accountor Procountor tapahtumien nouto (poistunut käytöstä)
  * `Procountor_format_2` \- Accountor Procountor tapahtumien nouto erittelytasolla
  * `Scala` \- Epicor Scala
  * `SDWorx_format_W` \- SD Worx tapahtumat
  * `SDWorx_format_W_absence` \- SD Worx poissaolot
  * `SDWorx_format_W_holiday` \- SD Worx lomat
  * `Sedab` \- Digia Sedab
  * `Sgwi` \- Safeguard Global
  * `Sonet` \- CGI Sonet lyhytliittymä
  * `SonetCSV` \- CGI Sonet parametroitu liittymä
  * `Tikon` \- Accountor Tikon
  * `Visma_format_csv` \- Visma Nova työtunnit
  * `Visma_format_csv-payroll-absences` \- Visma Payroll poissaolot
  * `Visma_format_csv-payroll` \- Visma Payroll palkka-aineisto
  * `Visma_format_csv-salary` \- Visma Nova palkka-aineisto
  * `Visma_format_fixed-width` \- Visma L7
  * `Visma_format_xml` \- Visma Lön
  * `VismaLTR` \- Visma LTR
  * `VismaPersonecF` \- Visma Personec F tapahtumat
