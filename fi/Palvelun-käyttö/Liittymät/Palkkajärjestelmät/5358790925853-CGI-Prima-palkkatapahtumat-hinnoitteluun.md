---
id: 5358790925853
title: CGI Prima palkkatapahtumat hinnoitteluun
url: https://support.nepton.com/hc/fi/articles/5358790925853-CGI-Prima-palkkatapahtumat-hinnoitteluun
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
edited_at: '2022-11-24T08:49:01Z'
---

# CGI Prima palkkatapahtumat hinnoitteluun

# Tiedostomuoto  
Siirtotiedosto on tekstimuotoinen CSV-tiedosto, jossa kentät on erotettu puolipisteellä (;). Rivinvaihto on CR+LF. Merkijonoja ei ole suljettu lainausmerkeillä. Merkistökoodaus on ISO-8859-1. Tiedostoon ei muodostu otsikkoriviä vaan sisältö alkaa suoraan ensimmäiseltä riviltä. Tiedoston desimaaliluvut käyttävät pistettä (.) desimaalierottimena.
# Aineiston tietueet
Sarake | Tieto | Sääntöjoukon kentän nimi | Muoto | Kuvaus  
---|---|---|---|---  
1 | Henkilötunnus tai henkilönumero | OverrideUserIntegrationId | merkkijono | Oletuksena suomalainen henkilötunnus. Voidaan ylikirjoittaa sääntöjoukolla (katso ohjeet [tästä](<https://support.nepton.com/hc/fi/articles/6447944970909>))  
2 | Alkupäivä | OverrideStartDate | päivämäärä | Siirretään muodossa pp.kk.vvvv  
3 | Loppupäivä | OverrideEndDate | päivämäärä | Siirretään muodossa pp.kk.vvvv  
4 | Palkkakoodi | OverrideSalaryCode | merkkijono | Pakollinen, Priman palkkalaji. Poimitaan asetuksista.  
5 | Tunnit | OverrideAmount | merkkijono | Ei pakollinen, esitysmuoto 5.2, esim. 4.00, ei etunollia; jos ei jollain palkkalajilla ole käytössä yksiköt, on tiedostossa tyhjä. Ylikirjoitettavissa.  
6 | Kerroin | Multiplier | desimaali | Ei pakollinen, esitysmuoto 5.2, esim. 4.00, ei etunollia; jos ei jollain palkkalajilla ole käytössä yksiköt, on tiedostossa tyhjä. Ylikirjoitettavissa.  
7 | A-hinta | PricePerUnit | desimaali | Ei pakollinen, esim. 234.56, ei etunollia. Ylikirjoitettavissa.  
8 | Tunniste | EmploymentIdentifier | merkkijono | Ei pakollinen, palvelujakson yksilöivä tunniste. Ylikirjoitettavissa.  
9 | Tili | Account | merkkijono | Ei pakollinen, jos siirretään pitää tulla Priman tiliöinnin näköisenä, mikäli ei voida käyttää palvelujakson ja/tai palkkalajiohjauksen mukaista tiliöintiä, jonka hinnoittelu tekee. Ylikirjoitettavissa.
