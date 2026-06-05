---
id: 360003291158
title: Visma Payroll, poissaolot
url: https://support.nepton.com/hc/fi/articles/360003291158-Visma-Payroll-poissaolot
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
edited_at: '2020-12-04T05:36:41Z'
---

# Visma Payroll, poissaolot

Nepton voidaan määrittää tuottamaan kirjatuista poissaoloista poissaoloaineisto Visma Payroll -järjestelmään.
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden Visma henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360009211157/mceclip0.png)
HUOM.! Jos henkilön Visma henkilötunnistetta ei ole asetettu, käytetään henkilönumeroa.
**2\. Sääntöjoukon luominen**
Liittymää varten pitää luoda integraation sääntöjoukko. Sääntöjoukon poiminnan ohje löytyy [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
## Maksupäivämäärä
Jos aineistoa ei luoda ajastetulla ajolla, maksupäivämäärä voidaan määrittää integraation lomakkeella.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360009293258/mceclip1.png)
Lomakkeella annettu palkan maksupäivä voidaan ohittaa poimintasäännössä kentällä `PayDate`
## Tiedostomuoto
Siirtotiedosto on puolipisteella erotettua tekstimuotoista dataa. Rivinvaihto on `CR` & `LF`. Merkistökoodauksena on ISO-8815-1.
Aineisto sisältää seuraavan otsikkorivin:
[code] 
    Numero;Maksupvm;Laji;alkupvm;loppupvm;HQY;selite;HOLIDAY_DAYS;BONUS_DAYS;NUMBER_OF_DAYS
[/code]
## Rajaukset
Henkilöt henkilönumerolla 0 eivät tule osaksi aineistoa
## Aineiston tietueet
Sarake | Kenttä | Otsikkorivin nimike | Sääntöjoukon kentän nimi | Muoto | Selite  
---|---|---|---|---|---  
A | Henkilönumero | Numero | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Visma henkilötunniste. Jos Visma henkilötunnistetta ei ole asetettu, käytetään henkilönumeroa  
B | Maksupvm | Maksupvm | PayDate | päivämäärä | Oletuksena Visma integraatio -lomakkeella syötetty päivämäärä. Voidaan asettaa poimintasäännön kentällä `PayDate`. Päivämäärän voi SQL-lausekkeessa valita muodossa `VVVV-KK-PP`. Muoto: `PP.KK.VVVV`  
C | Poissaolon tyyppi | Laji | SalaryCode | merkkijono | Palkkalajin / poissaolon koodi, esim. `85`  
D | Alkupvm | alkupvm | StartDateTime | päivämäärä | Poissaolon alkupäivämäärä. Muoto: `PP.KK.VVVV`. Kenttään voi valita päivämäärän muodossa `VVVV-KK-PP`, se muotoillaan oikein riville.  
E | Päättymispvm | loppupvm | EndDateTime | päivämäärä | Poissaolon päättymispäivämäärä. Muoto: `PP.KK.VVVV`. Kenttään voi valita päivämäärän muodossa `VVVV-KK-PP`, se muotoillaan oikein riville.  
F | Lomavuosi (HQY) | HQY |  SalaryRenderingDate | numero |  Sarakkeessaa on arvo ainoastaan vuosilomilla ja lomarahavapailla. Jos vuosiloman/lomarahavapaan alkupäivän kuukausi on tammi-huhtikuu, arvona on `SalaryRenderingDate` -päivää edeltävä vuosi. Jos vuosiloman/lomarahavapaan alkupäivän kuukausi on touko-joulukuu, arvona on `SalaryRenderingDate` -päivän vuosi.  
G | Selite | selite | Comment | merkkijono | Poissaolotapahtuman kuvaus  
H | Lomapäivät | HOLIDAY_DAYS | VismaPayrollAbsencesHolidayDays | desimaaliluku | Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä. Luku on kahden desimaalin tarkkuudella ja desimaalierottimena on pilkku (`,`).  
I | Bonus päivät | BONUS_DAYS | VismaPayrollAbsencesBonusDays | desimaaliluku | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä. Luku on kahden desimaalin tarkkuudella ja desimaalierottimena on pilkku (`,`).  
J | Päivien määrä | NUMBER_OF_DAYS | Amount | desimaaliluku |  Päivien määrä desimaaleina. Luku on kahden desimaalin tarkkuudella ja desimaalierottimena on pilkku (`,`). Jos sääntöjoukon sääntö valitsee määrän käyttäen muuta yksikköä (`UnitType`) kuin päiviä, määrä tuodaan tyhjänä. Jos sarake halutaan riville tyhjänä, sen saa sääntöjoukon säännön valinnalla `'' AS OverrideAmount`  
### Esimerkki
[code] 
    Numero;Maksupvm;Laji;alkupvm;loppupvm;HQY;selite;HOLIDAY_DAYS;BONUS_DAYS;NUMBER_OF_DAYS
    123;03.09.2017;909;04.07.2016;09.07.2016;2016;Summer vacation;6;;6
    123;03.09.2017;202;01.08.2016;05.08.2016;;Bonus absence;;5;5
    123;03.09.2017;108;08.08.2016;12.08.2016;;Sick leave;;;5
[/code]
