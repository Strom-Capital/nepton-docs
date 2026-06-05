---
id: 360019119337
title: EmCe työajanhallinta  - Siirrot työaikatoteutumiksi ja lomatositteiksi
url: https://support.nepton.com/hc/fi/articles/360019119337-EmCe-ty%C3%B6ajanhallinta-Siirrot-ty%C3%B6aikatoteutumiksi-ja-lomatositteiksi
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
edited_at: '2023-03-29T12:15:39Z'
---

# EmCe työajanhallinta  - Siirrot työaikatoteutumiksi ja lomatositteiksi

Nepton voidaan määrittää tuottamaan kirjatuista tapahtumista tulkittu palkka-aineisto EmCe-järjestelmään.
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![](https://support.nepton.com/hc/article_attachments/21081131263773)
Jos henkilön EmCE tunnistetta ei ole määritetty, käytetään henkilönumeroa.
**2\. Sääntöjoukon luominen**
Liittymässä voidaan käyttää integraation sääntöjoukkoja. Sääntöjoukon poiminnan ohje löytyy artikkelista [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257>).
## Tiedostomuoto
Siirtotiedosto on puolipisteellä (`;`) erotettua tekstimuotoista dataa. Rivinvaihto on `CR` & `LF` ja merkistökoodauksena on ISO-8859-1.
Siirtotiedostossa ei ole otsikkoriviä.
## Rajaukset
Henkilöt henkilönumerolla 0 eivät tule osaksi aineistoa
## Aineiston tietueet
Sarake | Kenttä | Muoto | Maksimipituus  
(merkkeinä) | Selite  
---|---|---|---|---  
A | Henkilön tunniste | merkkijono | 9 | Henkilön EmCe tunniste tai henkilönumero. Voidaan ohittaa sääntöjoukon säännön kentällä `OverrideUserIntegrationId`.  
B | Päivämäärä | päivämäärä | 10 | Muoto: `PP.KK.VVVV`. Voidaan ohittaa sääntöjoukon säännön kentällä `OverrideSalaryRenderingDate`.  
C | Palkkalajin koodi | merkkijono | 4 | Palkkalajin koodi, esimerkiksi `1200`. Voidaan ohittaa sääntöjoukon säännön kentällä `OverrideSalaryCode`.  
D | Määrä | desimaaliluku | - | Määrä, esimerkiksi yksikkömäärä tai tunnit desimaalilukuna. Desimaalierottimena on pilkku (`,`).  
E | Kappalehinta | desimaaliluku | - |  Määrä, jos yksikkönä on valuutta. Tällöin sarakkeen D arvoksi oletuksena asetetaan 1,00. Jos määrän halutaan aina olevan sarakkeessa D, se onnistuu valitsemalla arvo sääntöjoukon säännössä kenttään `UnitPrice`.  Jos kappalehinnan halutaan aina olevan tyhjä, se onnistuu seuraavalla poiminnalla:
[code] 
    '' AS UnitPrice
[/code]  
F | Palkkalajin kuvaus | merkkijono | - |  Sääntöjoukon sääntöjen asetuksissa annettu palkkalajin kuvaus. Voidaan ohittaa sääntöjoukon säännön kentällä `OverrideRowDescription`.  
G | Projektin 1 koodi | merkkijono | 8 |   
H | Projektin 2 koodi | merkkijono | 8 |   
I | Projektin 3 koodi | merkkijono | 8 |   
J | Projektin 4 koodi | merkkijono | 8 |   
K | Projektin 5 koodi | merkkijono | 8 |   
L | Projektin 6 koodi | merkkijono | 8 |   
M | Projektin 7 koodi | merkkijono | 8 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `OverrideProjectCode7`.  
N | Projektin 8 koodi | merkkijono | 8 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `OverrideProjectCode8`.  
O | Ansaintajakson alkupäivä | päivämäärä | - |  Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `EarningPeriodStartDate`. Muoto: `PP.KK.VVVV`  
P | Ansaintajakson loppupäivä | päivämäärä | - |  Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `EarningPeriodEndDate`. Muoto: `PP.KK.VVVV`  
Q | Poissaolon alkupäivä | päivämäärä | - |  Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `AbsenceStartDate`. Muoto: `PP.KK.VVVV`  
R | Poissaolon loppupäivä | päivämäärä | - |  Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `AbsenceEndDate`. Muoto: `PP.KK.VVVV`  
### Esimerkki
[code] 
    123456;14.03.2016;1234;7,50;;Perustunnit;1200;;;;;;;;;;;  
    123456;14.03.2016;1500;0,50;;Lisätyö;1200;;;;;;;;;;;  
    123456;14.03.2016;4200;1,00;6,40;Puhelinkuluja;1500;;;;;;;;;;;
[/code]
