---
id: 360011704397
title: Digia Enterprise
url: https://support.nepton.com/hc/fi/articles/360011704397-Digia-Enterprise
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels: []
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2021-07-14T07:40:47Z'
---

# Digia Enterprise

Nepton voidaan määrittää tuottamaan kirjatuista tapahtumista tulkittu palkka-aineisto Digia Enterprise -järjestelmään.
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip2.png](https://support.nepton.com/hc/article_attachments/360008665398/mceclip2.png)
**2\. Sääntöjoukon luominen**
Liittymää varten pitää luoda integraation sääntöjoukko. Sääntöjoukon poiminnan ohje löytyy artikkelista [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
## Tiedostomuoto
Siirtotiedosto on välilyöntimerkillä erotettua tekstimuotoista dataa. Rivinvaihto on `CR` & `LF`. Merkistökoodauksena on UTF-8.
Eri tietuemuodot muotoillaan seuraavasti:
  * **Merkkijono (teksti)** \- Ympäröidään pystysuorilla lainausmerkeillä (`"`), myös silloin kun merkkijono on tyhjä. Jos merkkijono sisältää pystysuoran lainausmerkin, lisätään sen eteen koodinvaihtomerkkinä pystysuora lainausmerkki.
  * **Kokonaisluku** \- Sellaisenaan ilman ympäröintiä. Tyhjä arvo viedään nollana (`0`)
  * **Desimaaliluku** \- Ilman ympäröintiä, kahden desimaalin tarkkuudella. Desimaalierottimena on pilkku (`,`). Tyhjä arvo viedään nollana (`0`)
  * **Päivämäärä** \- Ilman ympäröintiä, muotona `KK-PP-VVVV`. Jos päivämäärä on tyhjä, näytetään se kysymysmerkkinä (`?`). Esimerkiksi 31.1.2019 olisi 01-31-2019


## Rajaukset
Henkilöt henkilönumerolla 0 eivät tule osaksi aineistoa
## Aineiston tietueet
Sarake | Kenttä | Sääntöjoukon kentän nimi | Muoto | Selite  
---|---|---|---|---  
A | Maksuryhmä | DigiaEnterpriseSalPayGrp | merkkijono | Oletuksena tyhjä merkkijono, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseSalPayGrp`  
B | Palkkakausi | DigiaEnterpriseSalPeriod | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseSalPeriod`  
C | Henkilönumero | OverrideUserIntegrationId | kokonaisluku | Henkilön henkilönumero. Voidaan ohittaa poimintasäännön kentällä `OverrideUserIntegrationId`  
D | Palkkalaji | SalaryCode | merkkijono | Palkkalajin koodi  
E | Aikamäärä | OverrideHourAmount | desimaaliluku | Tunnit desimaalilukuna kun rivin yksikkötyyppi on tunteja tai sekunteja. Voidaan ohittaa poimintasäännön kentällä `OverrideHourAmount`, jolloin arvo näytetään rivin yksikkötyypistä riippumatta.  
F | Aikamäärän yksikkö | DigiaEnterpriseTimeUnit | merkkijono | Jos rivin yksikkötyyppi on tunteja tai sekunteja, oletuksena `H`, muissa tapauksissa oletuksena tyhjä merkkijono. Voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseTimeUnit`  
G | Yksikköhinta | UnitPrice | desimaaliluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `UnitPrice`  
H | Summa | TotalPrice | desimaaliluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `TotalPrice`  
I | Määrä | OverrideUnitAmount | desimaaliluku | Määrä desimaalilukuna kun rivin yksikkötyyppi ei ole tunteja tai sekunteja. Voidaan ohittaa poimintasäännön kentällä `OverrideUnitAmount`, jolloin arvo näytetään rivin yksikkötyypistä riippumatta.  
J | Määrän yksikkö | DigiaEnterpriseQuantityUnit | merkkijono | Jos rivin yksikkötyyppi ei ole tunteja tai sekunteja, oletuksena `kpl`, muissa tapauksissa oletuksena tyhjä merkkijono. Voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseQuantityUnit`  
K | Määrän yksikköhinta | DigiaEnterpriseUnitQuantityPrice | desimaaliluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseUnitQuantityPrice`  
L | Tapahtuman päivä | SalaryRenderingDate | päivämäärä | Päivä, mille palkkatieto kuuluu (SalaryRenderingDate). Jos palkkatieto kuulu esimerkiksi maanantaille, maanantain päivämäärää käytetään.  
M | Päättymispäivä | DigiaEnterpriseEndDate | päivämäärä | Oletuksena tyhjä (`?`), voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseEndDate`. Arvoa ohitettaessa täytyy käyttää SQL:n päivämäärämuotoa `VVVV-KK-PP`.  
N | Maksupäivä | DigiaEnterprisePaymentDate | päivämäärä | Oletuksena tyhjä (`?`), voidaan ohittaa poimintasäännön kentällä `DigiaEnterprisePaymentDate`. Arvoa ohitettaessa täytyy käyttää SQL:n päivämäärämuotoa `VVVV-KK-PP`.  
O | Huomiot / kommentti | DigiaEnterpriseNote | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseNote`  
P | Kerroin | DigiaEnterpriseMultiplier | desimaaliluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseMultiplier`  
Q | Tapahtuman tunnus | DigiaEnterpriseEventKey | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseEventKey`  
R | Kuormitusryhmä | DigiaEnterpriseResourceGroup | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseResourceGroup`  
S | Kuormituspiste | DigiaEnterpriseResource | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseResource`  
T | Tapahtumanro | DigiaEnterpriseConstEvent | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseConstEvent`  
U | Tapahtuman tyyppi | DigiaEnterpriseEventType | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseEventType`  
V | ALV-koodi | DigiaEnterpriseVATCode | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseVATCode`  
W | Työnumero | DigiaEnterpriseWorkOrderNum | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseWorkOrderNum`  
X | Työvaihe | DigiaEnterpriseOperation | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseOperation`  
Y | Projekti | DigiaEnterpriseProject | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseProject`  
Z | Seurantakohde1 | ProjectCode1 | merkkijono | Projektin 1 koodi  
AA | Seurantakohde2 | ProjectCode2 | merkkijono | Projektin 2 koodi  
AB | Tulosyksikkö | DigiaEnterpriseProfitUnit | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseProfitUnit`  
AC | Toimintayksikkö | DigiaEnterpriseLocation | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseLocation`  
AD | Työluokka | DigiaEnterpriseWorkClass | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseWorkClass`  
AE | TVR | DigiaEnterpriseWorkRequirementGroup | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseWorkRequirementGroup`  
AF | Tapahtuman kloaika | DigiaEnterpriseEventTime | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseEventTime`  
AG | Päättymisaika | DigiaEnterpriseEndTime | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseEndTime`  
AH | Jatkokirjaus | DigiaEnterpriseContinuationEvent | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseContinuationEvent`  
AI | Perustesumma | DigiaEnterpriseBaseSum | desimaaliluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseBaseSum`  
AJ | Poissaolosyy | DigiaEnterpriseAbsenceReason | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseAbsenceReason`  
AK | Linkki tuot.tilaukseen | DigiaEnterpriseProdResKey | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseProdResKey`  
AL | Linkki työvaiheen tote | DigiaEnterpriseActOperKey | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseActOperKey`  
AM | Debit-tili | DigiaEnterpriseDebitAccount | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseDebitAccount`  
AN | Kredit-tili | DigiaEnterpriseCreditAccount | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseCreditAccount`  
AO | Tositelinkki | DigiaEnterpriseLinkKey | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseLinkKey`  
AP | Selite palkkalaskelmalla | DigiaEnterprisePayslipNote | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterprisePayslipNote`  
AQ | Tapahtuman hyväksyjä | DigiaEnterpriseAcceptor | kokonaisluku | Oletuksena `0`, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseAcceptor`  
AR | Hyväksymisaika | DigiaEnterpriseAcceptTime | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseAcceptTime`  
AS | Suojausavain | DigiaEnterpriseSecurityKey | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseSecurityKey`  
AT | Suojauskenttä | DigiaEnterpriseSecurityField | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseSecurityField`  
AU | Todellinen maksupvm | DigiaEnterpriseActualPaymentDate | päivämäärä | Oletuksena tyhjä (`?`), voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseActualPaymentDate`. Arvoa ohitettaessa täytyy käyttää SQL:n päivämäärämuotoa `VVVV-KK-PP`.  
AV | Seurantakohde3 | ProjectCode3 | merkkijono | Projektin 3 koodi  
AW | Seurantakohde4 | ProjectCode4 | merkkijono | Projektin 4 koodi  
AX | Työaikamuoto | DigiaEnterpriseWorkTimeForm | merkkijono | Oletuksena tyhjä, voidaan ohittaa poimintasäännön kentällä `DigiaEnterpriseWorkTimeForm`  
### Esimerkki
[code] 
    "1" 2008120 21477 "100" 15 "H" 24,68 370,2 0 "" 0 31-12-2008 ? ? "" 1 100830 "" "" 0 "" "" 0 "" "" "17" "3" 2 "" "" 0 0 0 0 0 "" 0 0 "5010" "2940" 0 0 0 "" "" "" ? "" "" ""  
    "1" 2008120 21477 "100" 8 "H" 24,68 197,44 0 "" 0 31-12-2008 ? ? "" 1 100832 "" "" 0 "" "" 0 "" "" "17" "3" 2 "" "" 0 0 0 0 0 "" 0 0 "5010" "2940" 0 0 0 "" "" "" ? "" "" ""  
    "1" 2008120 21477 "160" 0 "" 1500 1500 1 "kpl" 0 31-12-2008 ? ? "Provisio koko vuodelta" 1 100834 "" "" 0 "" "" 0 "" "" "17" "3" 2 "" "" 0 0 0 0 0 "" 0 0 "5010" "2940" 0 0 0 "" "" "" ? "" "" ""
[/code]
