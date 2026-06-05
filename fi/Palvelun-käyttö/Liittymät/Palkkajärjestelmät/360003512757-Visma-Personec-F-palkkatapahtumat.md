---
id: 360003512757
title: Visma Personec F palkkatapahtumat
url: https://support.nepton.com/hc/fi/articles/360003512757-Visma-Personec-F-palkkatapahtumat
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
edited_at: '2023-09-11T10:02:36Z'
---

# Visma Personec F palkkatapahtumat

Nepton voidaan määrittää tuottamaan kirjatuista tapahtumista tulkittu palkka-aineisto Personec F järjestelmään.
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/21077293385629)
**2\. Liittymän asetukset**
Liittymässä käytettävän sovelluksen tunnuksen, ilmoittajan käyttäjätunnuksen ja palkanlaskentayksikön voi määrittää liittymän asetuksista,**Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Visma Personec F**
![](https://support.nepton.com/hc/article_attachments/11467024776477)
**3\. Sääntöjoukon luominen**
Liittymässä voidaan käyttää integraation sääntöjoukkoja. Sääntöjoukon poiminnan ohje löytyy artikkelista [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
Asettamalla tietuelajin (PersonecRecordType) poimintasäännössä voidaan muodostaa tietuelajin 2 ja 3 rivejä.
## Tiedostomuoto
Siirtotiedosto on ISO-8859-1 muotoista positioeroteltua tekstimuotoista dataa. Aineisto ei sisällä otsikoita. Numeeriset kentät täytetään etunollilla, tyhjät merkit täytetään välilyönneillä oikeasta laidasta, jollei kentässä ole toisin mainittu.
Siirtotiedostossa olevat rivit järjestetään tietuelajin mukaan. Jos siirtotiedosto esimerkiksi sisältää tietuelajeja 1, 2 ja 3, olisi järjestys seuraava:
  1. Kaikki tietuelajin 1 rivit
  2. Kaikki tietuelajin 2 rivit
  3. Kaikki tietuelajin 3 rivit


## Rajaukset
Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa.
## Aineiston tietueet 
Tieto | Kenttä | Sääntöjoukon kentän nimi | Muoto | Positio | Pituus | Kuvaus  
---|---|---|---|---|---|---  
1 | Tunnus | PersonecRowType | merkki | 1 | 1 | Oletusarvo `T`, voidaan korvata poimintasäännön kentällä `PersonecRowType`  
2 | Ansaintakausityyppi | PersonecSalaryType | merkki | 2 | 1 |  Oletuksena henkilölle asetetun palkkauksen mukaan.
  * `T` \- tuntipalkkainen, oletus jos henkilön palkkausta ei ole asetettu
  * `K` \- kuukausipalkkainen

Voidaan korvata poimintasäännön kentällä `PersonecSalaryType`  
3 | Palkanlaskentayksikkö | PersonecPayrollUnit | merkkijono | 3 | 6 |  Asetetaan _Liittymät → Personec asetukset_ (Työyhteisö-taso) Voidaan korvata poimintasäännön kentällä `PersonecPayrollUnit`  
4 | Henkilötunnus / henkilönumero | OverrideUserIntegrationId | merkkijono | 9 | 11 | Oletuksena henkilön henkilötunnus, voidaan korvata poimintasäännön kentällä `OverrideUserIntegrationId`  
5 | Palvelussuhteen tunnus | PersonecEmploymentIdentifier | merkki | 20 | 1 | Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecEmploymentIdentifier`  
6 | Työaikaryhmä | PersonecWorkTimeGroup | merkkijono | 21 | 6 | Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecWorkTimeGroup`  
7 | Palkka- / työaikatekijäkoodi | SalaryCode | merkkijono | 27 | 4 | Esim. palkkatekijä, jolla suorite tullaan maksamaan  
8 | Lisätunnisteen tunnus | PersonecAdditionalIdentifier | merkkijono | 31 | 20 |  Oletuksena tapahtumaan liittyvän tapahtuman yksilöllinen tunnus, tarvittaessa. Muutoin jätetään tyhjäksi. Voidaan korvata poimintasäännön kentällä `PersonecAdditionalIdentifier`  
9 | Aikaleima, päivä | StartDateTime | päivämäärä | 51 | 10 | Formaatti `VVVV.KK.PP`  
10 | Aikaleima, aika | StartDateTime | merkkijono | 61 | 8 | Muoto `HH.MM.SS`  
11 | Alkupäivä | StartDateTime | päivämäärä | 69 | 10 | Muoto `VVVV.KK.PP`  
12 | Loppupäivä | EndDateTime | päivämäärä | 79 | 10 | Muoto `VVVV.KK.PP`  
13 | Muutoslaji | PersonecChangeType | merkki | 89 | 1 | 
  * `M` \- koko perusteen lisäys tai muutos, oletus
  * `P` \- koko perusteen poisto.

Voidaan korvata poimintasäännön kentällä `PersonecChangeType`  
14 | Tietuelaji | PersonecRecordType | numero | 90 | 1 | 
  * `1` \- palkkaperusteen ensimmäinen tietue, oletus
  * `2` \- palkkaperusteen kaikki seuraavat tietueet (jos lähetetään esim. arkipäivä ja viikonloppukorvaukset samalla palkkatekijäkoodilla)
  * `3` \- perustekohtaiset poikkeustilitietueet

Voidaan korvata poimintasäännön kentällä `PersonecRecordType`  
### Seuraavat tiedot (15-17), kun tietuelaji on 1 tai 2:
Tieto | Kenttä | Sääntöjoukon kentän nimi | Muoto | Positio | Pituus | Kuvaus  
---|---|---|---|---|---|---  
15 | Perusarvon nimi | PersonecBaseValueName | merkkijono | 91 | 12 | 
  * `EUROPERUSTE` \- rahamääräinen data (EUR)
  * `TUNNIT` \- tuntimääräinen data
  * `KAPPALEET` \- päivät, desimaalit ja kappaleet

Tulee oletuksena rivin yksikön mukaan, voidaan korvata poimintasäännön kentällä `PersonecBaseValueName`  
16 | Perusarvon sisältö | Amount | merkkijono | 103 | 50 |  Tuntien/kappaleiden/ym. määrä rivillä. Käytetään seuraavia muotoiluja: Jos arvo ei ole rahamääräistä dataa, käytetään etunolla täyttöä 6 merkkiin ilman desimaalierotinta. Esimerkiksi `1,50` esitetään `000150`. Negatiivisia arvoja ei tueta ja ne siirretään arvona `000000`. Jos arvo on rahamääräistä dataa, etuliitteenä on välilyönti positiivisille arvoille ja `-` negatiivisille arvoille. Käytetään etunolla täyttöä 10 merkkiin ilman desimaalierotinta. Esimerkiksi `-9001,42` esitettäisiin `-0000900142`. Muotoilun jälkeen kenttä täytetään välilyönneillä vaadittuun pituuteen. Huomaathan, että muita muotoiluja paitsi täyttöä välilyönneillä ei huomioida, jos valitset arvon `1` kenttään `PersonecIsAmountFormatted`. Tällä mahdollistetaan asiakaskohtainen formaatti.  
17 | Perusarvon tyyppi | PersonecValueUnit | merkkijono | 153 | 2 | 
  * A-hinta - `03` (eurot)
  * Tunnit - `04` (tunnit)
  * Kappaleet - `05` (kappaleet)
  * Euroa - voi jättää tyhjäksi

Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecValueUnit`  
### Seuraavat tiedot (18-25), kun tietuelaji on 3:
  * Huomio: tarvitaan vain, jos myös tiliöintitiedot tulevat tietueella

Tieto | Kenttä | Sääntöjoukon kentän nimi | Muoto | Positio | Pituus | Kuvaus  
---|---|---|---|---|---|---  
18 | Muodostumistapa | PersonecMethodOfFormation | merkki | 91 | 1 | 
  * `Y` \- yksi kombinaatio
  * `O` \- osuus

Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecMethodOfFormation`  
19 | Osuuden järjestysnro | PersonecSequenceOfPortion | numero | 92 | 2 |  Tilikombinaation numero, voi olla `01` \- `10` Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecSequenceOfPortion`  
20 | Osuuslaji | PersonecIsPercentageOrFraction | merkki | 94 | 1 | 
  * `P` \- prosentti
  * `M` \- murtoluku
  * `F` \- euromäärä

Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecIsPercentageOrFraction`  
21 | Prosenttiosuus | PersonecPercentageValue | numero | 95 | 5 | Oletusarvo on `0`, voidaan korvata poimintasäännön kentällä `PersonecPercentageValue`  
22 | Murtolukuosuus | PersonecFractionValue | merkkijono | 100 | 9 | Oletuksena tyhjä, voidaan korvata poimintasäännön kentällä `PersonecFractionValue`  
23 | Euromääräinen osuus | PersonecEuroValue | numero | 109 | 10 | Oletusarvo on `0`, voidaan korvata poimintasäännön kentällä `PersonecEuroValue`  
24 | Tililuokan lyhenne (tunniste) | PersonecAccountGroupAbbr | merkkijono | 119 | 3 |  Esimerkkejä lyhenteistä
  * Tili- lyhenne (TIL)

Huom. Lyhenteet kantakohtaisia. Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecAccountGroupAbbr`  
25 | Tililuokan arvo | PersonecAccountGroupValue | merkkijono | 122 | 20 | Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecAccountGroupValue`  
### Seuraavat tiedot (26-36), kun tietuelaji on 1:
Tieto | Kenttä | Sääntöjoukon kentän nimi | Muoto | Positio | Pituus | Kuvaus  
---|---|---|---|---|---|---  
26 | Onko laskenta-arvo | PersonecIsCalculationValue | merkki | 155 | 1 | 
  * `K` \- kyllä
  * `E` \- ei

Oletusarvona ei (`E`), voidaan korvata poimintasäännön kentällä `PersonecIsCalculationValue`  
27 | Onko osatieto | PersonecIsPercentageOrFraction | merkki | 156 | 1 | 
  * `P` \- on prosentti
  * `M` \- on murtoluku
  * `E` \- ei

Oletusarvona ei (`E`), voidaan korvata poimintasäännön kentällä `PersonecIsPercentageOrFraction`  
28 | Laskenta-arvo | PersonecCalculationValue | numero | 157 | 11 | Oletusarvo on `0`, voidaan korvata poimintasäännön kentällä `PersonecCalculationValue`  
29 | Osaprosentti | PersonecPercentageValue | numero | 168 | 5 | Oletusarvo on `0`, voidaan korvata poimintasäännön kentällä `PersonecPercentageValue`  
30 | Osamurtoluku | PersonecFractionValue | merkkijono | 173 | 9 | Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecFractionValue`  
31 | Onko epäilyttävä | PersonecIsSuspiciousRow | merkki | 182 | 1 | 
  * `K` \- kyllä
  * `E` \- ei

Oletusarvona ei (`E`), voidaan korvata poimintasäännön kentällä `PersonecIsSuspiciousRow`  
32 | Epäilyn syy | PersonecReasonForSuspicion | merkkijono | 183 | 2 | Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecReasonForSuspicion`  
33 | Aikaisin käsittelypäivä | PersonecEarliestHandlingDay | päivämäärä | 185 | 10 |  Muotona `VVVV.KK.PP`. Kenttään voi valita päivämäärän muodossa `VVVV-KK-PP`, se muotoillaan oikein riville. Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecEarliestHandlingDay`  
34 | Ilmoittavan sovelluksen tunnus | PersonecReportingAppId | merkkijono | 195 | 4 |  Asetetaan _Liittymät → Personec_ (Työyhteisö-taso) Voidaan korvata poimintasäännön kentällä `PersonecReportingAppId`  
35 | Tekijän käyttäjätunnus | PersonecCreatorUsername | merkkijono | 199 | 8 |  Asetetaan _Liittymät_ _→ Personec_ (Työyhteisö-taso) Voidaan korvata poimintasäännön kentällä `PersonecCreatorUsername`  
36 | Sopimuksen numero | PersonecContractNumber | numero | 207 | 9 | Oletuksena tyhjä, voidaan asettaa poimintasäännön kentällä `PersonecContractNumber`  
## Esimerkit
Esimerkki vientitiedoston sisällöstä
[code] 
    TT564022090480-hetu       503527590520            2020.01.2816.54.142020.01.202020.01.20M1TUNNIT      000050                                              EE0000000000000000         E            NORL857713           
    
[/code]
