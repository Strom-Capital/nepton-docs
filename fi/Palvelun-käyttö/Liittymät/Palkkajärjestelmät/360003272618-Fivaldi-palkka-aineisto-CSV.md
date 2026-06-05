---
id: 360003272618
title: Fivaldi palkka-aineisto, CSV
url: https://support.nepton.com/hc/fi/articles/360003272618-Fivaldi-palkka-aineisto-CSV
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
edited_at: '2023-10-05T10:57:38Z'
---

# Fivaldi palkka-aineisto, CSV

Nepton voidaan määrittää tuottamaan kirjatuista tapahtumista tulkittu palkka-aineisto Visma Fivaldi-järjestelmään.
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![](https://support.nepton.com/hc/article_attachments/10023975965725)
Jos henkilön Fivaldi tunnistetta ei ole määritetty, käytetään henkilönumeroa.
**2\. Sääntöjoukon luominen**
Liittymässä voidaan käyttää integraation sääntöjoukkoja. Sääntöjoukon poiminnan ohje löytyy artikkelista [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257>).
## Tiedostomuoto
Siirtotiedosto on puolipisteellä (`;`) erotettua tekstimuotoista dataa. Jos jokin kenttä sisältää erikoismerkkejä, kyseinen kenttä ympäröidään pystysuorilla lainausmerkeillä (`"`). Rivinvaihto on `CR` & `LF`. Merkistökoodaus on UTF-8.
Sarakkeeseen A muodostuu Erä-tieto (`FivaldiBatchIdentifier`), jonka arvo on muotoa 'Palkat pp.kk.vv'. Päivämäärä tulee poimintajakson ensimmäisestä päivästä. Esim. poimitaan jaksolta 1.1.2022-15.1.2022 on ko. arvo 'Palkat 01.01.22'.
Aineisto sisältää seuraavan otsikkorivin:
[code] 
    ERA;PVM;HENKILO;PALKKALAJI;MAARA;SK1;SK2;SK3;SK4;KERROIN;HINTA;KULUTILI;SELITE;PAIVITYSTAPA;LOMA_ALKUPVM;LOMA_LOPPUPVM
[/code]
## Rajaukset
  * Fivaldi Business ID tulee olla syötetty Nepton-palveluun valikossa _Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Visma Fivaldi._  
  
![](https://support.nepton.com/hc/article_attachments/21080324510365)
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet
Sarake | Kenttä | Sääntöjoukon kentän nimi | Muoto | Selite  
---|---|---|---|---  
A | Erä | FivaldiBatchIdentifier | merkkijono | Voidaan ohittaa sääntöjoukon säännön kentällä `FivaldiBatchIdentifier`.  
B | Päivämäärä | SalaryRenderingDate | päivämäärä | Muoto: `PP.KK.VVVV`.  
C | Henkilön tunniste | OverrideUserIntegrationId | merkkijono | Henkilön Fivaldi-tunniste tai henkilönumero. Voidaan ohittaa sääntöjoukon säännön kentällä `OverrideUserIntegrationId`.  
D | Palkkalajin koodi | SalaryCode | merkkijono |   
E | Määrä | Amount | desimaaliluku | Määrä kahden desimaalin tarkkuudella. Esimerkiksi yksikkömäärä tai tunnit desimaalilukuna. Desimaalierottimena on pilkku (`,`).  
F | Projektin 1 koodi | ProjectCode1 | merkkijono | Project code 1. Note that if only 1 project is set up with '/' separator it will be split to other project codes.  
G | Projektin 2 koodi | ProjectCode2 | merkkijono |   
H | Projektin 3 koodi | ProjectCode3 | merkkijono |   
I | Projektin 4 koodi | ProjectCode4 | merkkijono |   
J | Kerroin | Multiplier | desimaaliluku | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `Multiplier`. Desimaalierottimena on pilkku (`,`).  
K | Yksikköhinta | UnitPrice | desimaaliluku | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `UnitPrice`. Desimaalierottimena on pilkku (`,`).  
L | Kulutili | ExpenseAccount | merkkijono | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `ExpenseAccount`.  
M | Selite | Comment | merkkijono | Liittyvän tapahtuman selite.  
N | Päivitystapa | FivaldiUpdateMethod | merkki | Oletuksena 1. Voidaan asettaa poimintasäännön kentällä `FivaldiUpdateMethod`.  
O | Loman alkupvm | FivaldiVacationStartDate | päivämäärä |  Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `FivaldiVacationStartDate`. Muoto: `PP.KK.VVVV`. Tietoa käytetään poissaolon ilmoittamisessa tulorekisteriin.  
P | Loman loppupvm | FivaldiVacationEndDate | päivämäärä |  Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `FivaldiVacationEndDate`. Muoto: `PP.KK.VVVV`. Tietoa käytetään poissaolon ilmoittamisessa tulorekisteriin.  
### Esimerkki
[code] 
    ERA;PVM;HENKILO;PALKKALAJI;MAARA;SK1;SK2;SK3;SK4;KERROIN;HINTA;KULUTILI;SELITE;PAIVITYSTAPA;LOMA_ALKUPVM;LOMA_LOPPUPVM  
    Palkat 01.01.12;08.12.2011;78050;101;3,50;63111;81323;;;;;;"TT Iltavuoro";1;;  
    Palkat 01.01.12;08.12.2011;78050;101;1,00;63111;81323;;;;;;;1;;  
    Palkat 01.01.12;05.12.2011;78055;101;4,00;63111;81333;;;;;;"TT Iltavuoro";1;;  
    Palkat 01.01.12;07.12.2011;78055;200;16,00;63111;81333;;;;;;;1;07.12.2011;08.12.2011
[/code]
