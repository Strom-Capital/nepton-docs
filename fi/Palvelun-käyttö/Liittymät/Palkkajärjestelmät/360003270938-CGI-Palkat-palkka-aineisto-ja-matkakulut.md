---
id: 360003270938
title: CGI Palkat, palkka-aineisto ja matkakulut
url: https://support.nepton.com/hc/fi/articles/360003270938-CGI-Palkat-palkka-aineisto-ja-matkakulut
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
edited_at: '2020-10-05T09:48:42Z'
---

# CGI Palkat, palkka-aineisto ja matkakulut

Nepton voidaan määrittää tuottamaan kirjatuista tapahtumista tulkittu palkka-aineisto CGI Palkat -järjestelmään.  
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip2.png](https://support.nepton.com/hc/article_attachments/360008665398/mceclip2.png)
**2\. Sääntöjoukon luominen**
Liittymää varten pitää luoda integraation sääntöjoukko. Sääntöjoukon poiminnan ohje löytyy artikkelista [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
## Tiedostomuoto 
Siirtotiedosto on puolipisteellä erotettua tekstimuotoista dataa. Rivinvaihto on `CR` & `LF`. Merkistökoodauksena on ISO-8859-1.
Matkakulut voidaan siirtää CGI palkkoihin samalla liittymämuodolla.
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet 
Sääntöjoukon kenttien tarkemmat kuvaukset löytyvät artikkelista [Sääntöjoukon poimintasääntöjen muodostaminen](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
Sarake | Kenttä | Sääntöjoukon kentän nimi | Muoto | Selite  
---|---|---|---|---  
A | Henkilön kalleusluokka | UserCostGroup | merkkijono | Voidaan käyttää maksuryhmänä  
B | Henkilönumero | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Henkilön henkilönumero  
C | Palkkalajin koodi |  _Saa arvonsa sääntöjoukon yksittäisen säännön Koodi-kentästä ja voidaan korvata käyttämällä kenttänimeä_ OverrideSalaryCode | merkkijono | Palkkalajin koodi, esimerkiksi `002`  
D | Määrä | Amount | desimaaliluku | Määrä, esimerkiksi yksikkömäärä tai tunnit desimaalilukuna. Desimaalierottimena on pilkku (`,`). Jos arvo halutaan viedä tyhjänä, sen pitää olla tyhjä merkkijono tai NULL. Esimerkiksi: 
[code]
    NULL AS OverrideAmount
[/code]  
E | Hinta | CustomData1 | desimaaliluku | Desimaalierottimena on pilkku (`,`). Arvo tulee poimintasäännön kentästä `CustomData1`  
F | Alkupäivä | StartDateTime | päivämäärä | Muoto: `PP.KK.VVVV.`  
G | Päättymispäivä | EndDateTime | päivämäärä | Muoto: `PP.KK.VVVV.`  
H | Maksuun/ei maksuun | CustomData2 | kokonaisluku | 0 = rivi menee maksuun palkkaohjelman kautta, 3 = rivi on jo maksettu muuta kautta. Arvo tulee poimintasäännön kentästä `CustomData2`. Oletusarvona on 0  
I | Kommentti | Comment | merkkijono | Tapahtuman kommentti, rajataan ensimmäiseen 2000 merkkiin.  
J | Projektin 1 koodi | ProjectCode1 | merkkijono |   
K | Projektin 2 koodi | ProjectCode2 | merkkijono |   
L | Projektin 3 koodi | ProjectCode3 | merkkijono |   
M | Projektin 4 koodi | ProjectCode4 | merkkijono |   
### Esimerkki
[code] 
    1234;123456;123;7,50;;14.03.2016;14.03.2016;0;;;;;  
    1234;123456;123;7,50;;16.03.2016;16.03.2016;0;;;;;
[/code]
