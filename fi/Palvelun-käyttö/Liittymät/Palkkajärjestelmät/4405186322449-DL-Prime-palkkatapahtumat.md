---
id: 4405186322449
title: DL Prime palkkatapahtumat
url: https://support.nepton.com/hc/fi/articles/4405186322449-DL-Prime-palkkatapahtumat
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
updated_at: '2025-08-06T09:14:31Z'
edited_at: '2025-08-06T09:12:21Z'
---

# DL Prime palkkatapahtumat

Nepton voidaan määrittää tuottamaan kirjatuista tapahtumista tulkittu palkka-aineisto DL Prime järjestelmään.
Aineistomallit ja siihen liittyvät asetukset löytyvät Neptonista nimellä "DL Software"
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4405182591505/mceclip0.png)
Jos henkilön DL Software -tunnusta ei ole asetettu, käytetään henkilön henkilönumeroa.
**2\. Sääntöjoukon luominen**
Liittymässä voidaan käyttää integraation sääntöjoukkoja. Sääntöjoukon poiminnan ohje löytyy artikkelista [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
## Tiedostomuoto
Siirtotiedosto on UTF-8 muotoista positioeroteltua tekstimuotoista dataa. Aineisto ei sisällä otsikoita. Numeerisia kenttiä **ei** täytetä etunollilla, tyhjät merkit täytetään välilyönneillä oikeasta laidasta, jollei kentässä ole toisin mainittu.
## Rajaukset
Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa.
## Aineistomuodot
Nepton tukee kahta DL Prime aineistomuotoa:
  * DL Prime 2000 - DLWPLPT3
  * DL Prime 3000 - DLWPLPT8


DL Prime 3000 aineistomuoto on laajennettu versio DL Prime 2000 aineistomuodosta.
## Aineiston tietueet
Tieto | Sääntöjoukon kentän nimi | Muoto | Positio | Pituus | Kuvaus  
---|---|---|---|---|---  
Tietuetunnus | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | 1 | 8 | Arvona on jompi kumpi seuraavista: 
  * `DLWPLPT3` \- DL Prime 2000
  * `DLWPLPT8` \- DL Prime 3000

  
_Tyhjä_ |  |  | _9_ | _1_ |   
Henkilönumero | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | 10 | 8 | Henkilön DL Software -tunniste tai henkilönumero  
_Tyhjä_ |  |  | _18_ | _1_ |   
Palkkakausinro | DLSoftwarePayrollPeriodNo | merkkijono | 19 | 5 | Ei käytössä  
_Tyhjä_ |  |  | _24_ | _1_ |   
Palkkalajikoodi |  _Saa arvonsa sääntöjoukon yksittäisen säännön Koodi-kentästä ja voidaan korvata käyttämällä kenttänimeä_ OverrideSalaryCode | merkkijono | 25 | 3 | Palkkalajin koodi, esimerkiksi `412`  
_Tyhjä_ |  |  | _28_ | _1_ |   
Projektinro | ProjectCode1 | merkkijono | 29 | 6 | Projektikoodi 1  
_Tyhjä_ |  |  | _35_ | _1_ |   
Vaihe-1 (kp-1) | DLSoftwarePhase1 | merkkijono | 36 | 4 |   
_Tyhjä_ |  |  | _40_ | _1_ |   
Vaihe-2 (kp-2) | DLSoftwarePhase2 | merkkijono | 41 | 4 |   
_Tyhjä_ |  |  | _9_ | _1_ |   
Vaihe-3 (kp-3) | DLSoftwarePhase3 | merkkijono | 46 | 4 |   
_Tyhjä_ |  |  | _50_ | _10_ |   
Tuntimäärä | OverrideHourAmount | desimaaliluku | 60 | 7 |  Tunnit desimaalilukuna jos määrä on tunteina. Desimaalierottimena on pilkku (`,`) ja määrä on yhden desimaalin tarkkuudella. Arvo voidaan myös antaa sääntöjoukon kentällä.  
_Tyhjä_ |  |  | _67_ | _52_ |   
Kappalehinta | UnitPrice | desimaaliluku | 119 | 12 |  Palkkarivin määrä jos määrä on euromääränä Desimaalierottimena on pilkku (`,`) ja määrä on yhden desimaalin tarkkuudella. Arvo voidaan myös antaa sääntöjoukon kentällä.  
_Tyhjä_ |  |  | _131_ | _1_ |   
Määrä | OverrideUnitAmount | desimaaliluku | 132 | 12 |  Palkkarivin määrä jos määrä ei ole tunteina tai euromäärä Desimaalierottimena on pilkku (`,`) ja määrä on yhden desimaalin tarkkuudella. Arvo voidaan myös antaa sääntöjoukon kentällä.  
### DL Prime 3000 -aineiston lisätietueet
Tieto | Sääntöjoukon kentän nimi | Muoto | Positio | Pituus | Kuvaus  
---|---|---|---|---|---  
_Tyhjä_ |  |  | _144_ | _1_ |   
Kustannuspaikat | DLSoftwareCostCentres | merkkijono | 145 | 14 |  Kustannuspaikat erotettuna pisteellä (`.`). Kustannuspaikkoja 3 ja kustannuspaikkatason maksimipituus 4 merkkiä. Esimerkiksi `10.20.30`  
_Tyhjä_ |  |  | _159_ | _1_ |   
Lisätieto | Comment | merkkijono | 160 | 60 | Tapahtumalle kirjattu huomautus  
_Tyhjä_ |  |  | _220_ | _2_ |   
Varalla |  | merkkijono | 222 | 10 |   
Varalla |  | merkkijono | 232 | 40 |   
_Tyhjä_ |  |  | _272_ | _1_ |   
Poissaolopvm | DLSoftwareAbsencePeriod | merkkijono | 273 | 21 | Esimerkiksi `04.01.2021-05.01.2021`  
## Esimerkki
[code] 
    DLWPLPT8 12345678       999 321012 2000 4000 6000          6,5                                                        0,0          0,0          2000.4000.6000   Lorem ipsum molestie coire heure inceptos pour in voir vulpu                                                     01.01.2021-12.01.2021
[/code]
