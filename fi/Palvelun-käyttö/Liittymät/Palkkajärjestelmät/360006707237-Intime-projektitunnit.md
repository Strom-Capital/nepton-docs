---
id: 360006707237
title: Intime projektitunnit
url: https://support.nepton.com/hc/fi/articles/360006707237-Intime-projektitunnit
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
edited_at: '2023-09-11T12:10:57Z'
---

# Intime projektitunnit

## Määrittäminen
Aineistoa voidaan käyttää vain määritetyllä integraation sääntöjoukolla. Lue lisää integraation sääntöjoukoista [täällä](<https://support.nepton.com/hc/fi/articles/360002492278>) ja sääntöjoukon poimintasääntöjen käsittelystä [täällä](<https://support.nepton.com/hc/fi/articles/360002489257>).
Työyhteisökohtaisen yritystunnuksen voi asettaa työyhteisön asetuksista: Työaika -> Hallinta -> Työyhteisön asetukset -> Liittymät -> Intime
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360007755637)
## Tiedostomuoto
Siirtotiedosto on ISO-8859-1 muotoista positioeroteltua tekstimuotoista dataa. Käytetty tietuepituus on 400. Tietueet päättyvät `CR`+`LF` -merkkeihin. Aineisto ei sisällä otsikoita.
## Rajaukset
Henkilöt henkilönumerolla 0 eivät tule osaksi aineistoa.
## Aineiston tietueet
Ellei toisin mainittu, kentät täydennetään oikeaan pituuteen välilyöntimerkeillä oikealle puolelle.
Desimaaliluvut esitetään ilman desimaalierotinta ja viimeinen merkki kertoo, onko luku negatiivinen vai positiivinen. Negatiivisella luvulla viimeinen merkki on miinus-merkki (`-`) ja positiivisella luvulla välilyöntimerkki. Desimaaliluvut täydennetään oikeaan pituuteen nolla-merkillä (`0`) vasemmalle puolelle.
Desimaaliluvun tarkkuus esitetään formaatti-sarakkeessa, esimerkiksi _Desimaaliluku (9,2)_ tarkoittaa että luvun kokonaislukuosa sisältää 9 merkkiä ja luku on 2 desimaalin tarkkuudella. Kentän kokonaispituus viimeinen merkki mukaan luettuna olisi 12.
Esimerkiksi desimaalin arvo -123,86 esitettäisiin seuraavasti, Desimaaliluku (9,2): `00000012386-`
Kenttä | Formaatti | Pituus | Alkupositio | Loppupositio | Kuvaus  
---|---|---|---|---|---  
Yritystunnus | Merkkijono | 2 | 1 | 2 | Yritystunnus työyhteisön asetuksissa. Voidaan asettaa poimintasäännön kentällä `IntimeCompanyIdentifier`  
Palkkalajikoodi | Merkkijono | 2 | 3 | 4 | Palkkatiedon palkkalajikoodi  
Tositenumero | Numero | 8 | 5 | 12 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeVoucherNumber`. Täydennetään nolla-numeroilla (`0`) vasemmalle puolelle.  
Kausi | Merkkijono | 4 | 13 | 16 | Tapahtumakauden vuosi ja kuukausi, muotona `YYMM`. Tulee oletuksena palkkatiedon päivämäärästä. Voidaan asettaa poimintasäännön kentällä `IntimeEventPeriod`. Kenttään voi valita päivämäärän muodossa `YYYY-MM-DD`, se muotoillaan oikein riville.  
Alv-kausi | Merkkijono | 4 | 17 | 20 | Alv-kauden vuosi ja kuukausi, muotona `YYMM`. Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeVATPeriod`. Kenttään voi valita päivämäärän muodossa `YYYY-MM-DD`, se muotoillaan oikein riville.  
Tositepvm | Päivämäärä | 6 | 21 | 26 | Päivä, mille palkkatieto kuuluu. Jos palkkatieto kuulu esimerkiksi maanantaille, maanantain päivämäärää ja aikaa käytetään. Formaatti `YYMMDD`  
Tositeselite | Merkkijono | 30 | 27 | 56 | Tapahtuman kommentti.  
Kirjanpitotili | Numero | 8 | 57 | 64 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeAccountingAccount`. Täydennetään välilyöntimerkeillä vasemmalle puolelle.  
Alatili | Numero | 6 | 65 | 70 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeSubAccount`. Täydennetään nolla-numeroilla (`0`) vasemmalle puolelle.  
Alv-koodi | Numero | 3 | 71 | 73 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeVATCode`. Täydennetään nolla-numeroilla (`0`) vasemmalle puolelle.  
Summa | Desimaaliluku (9,2) | 12 | 74 | 85 | Määrä, esimerkiksi yksikkömäärä tai tunnit desimaalilukuna.  
Valuutta-1 | Desimaaliluku (9,2) | 12 | 86 | 97 | Valuuttamäärä-1. Oletuksena tyhjä. Tyhjä arvo esitetään välilyöntimerkkeinä, muutoin esitetään desimaalilukuna. Voidaan asettaa poimintasäännön kentällä `IntimeCurrencyAmountOne`.  
Valuuttalyhenne | Merkkijono | 3 | 98 | 100 | Valuutan 3-merkkinen lyhenne, esimerkiksi EUR. Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeCurrencyType`.   
Vientiselite | Merkkijono | 30 | 101 | 130 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeExportComment`.   
Sovellus | Merkkijono | 2 | 131 | 132 | Viennin synnyttäneen sovelluksen tunnus. Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeSourceSystemIdentifier`.   
Sisäisen laskennan tilinro | Numero | 8 | 133 | 140 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeInternalAccountingAccount`. Täydennetään välilyöntimerkeillä vasemmalle puolelle.  
Laskentatunniste | Merkkijono | 30 | 141 | 170 |  Täytetään oletuksena projektikoodista. Projektikoodi voi sisältää kustannuspaikan ja toiminnon erotettuna kauttaviivalla (`/`). Kustannuspaikan maksimipituus on 4 merkkiä ja toiminnon 3 merkkiä. Lyhyempi kustannuspaikka tai toiminto täydennetään välilyöntimerkillä vasemmalle puolelle. Kustannuspaikan ja toiminnon yhdistelmä täydennetään lopuksi välilyöntimerkeillä oikealle puolelle. Esimerkkejä:
  * `1234/889` => `1234889`
  * `32/45` => ` 32 45`
  * `8765` => `8756 `

Voidaan asettaa poimintasäännön kentällä `IntimeSourceSystemIdentifier`.  
Määrä1 | Desimaaliluku (7,4) | 12 | 171 | 182 | Oletuksena tyhjä. Tyhjä arvo esitetään välilyöntimerkkeinä, muutoin esitetään desimaalilukuna. Voidaan asettaa poimintasäännön kentällä `IntimeAmountOne`.  
Määrä2 | Desimaaliluku (7,4) | 12 | 183 | 194 | Oletuksena tyhjä. Tyhjä arvo esitetään välilyöntimerkkeinä, muutoin esitetään desimaalilukuna. Voidaan asettaa poimintasäännön kentällä `IntimeAmountTwo`.  
Toimituskausi | Merkkijono | 4 | 195 | 198 | Toimituskauden vuosi ja kuukausi, muotona `YYMM`. Oletuksena tyhjä. vVoidaan asettaa poimintasäännön kentällä `IntimeManagementPeriod`. Kenttään voi valita päivämäärän muodossa `YYYY-MM-DD`, se muotoillaan oikein riville.  
Valuutta-2 | Desimaaliluku (12,2) | 15 | 199 | 213 | Oletuksena tyhjä. Tyhjä arvo esitetään välilyöntimerkkeinä, muutoin esitetään desimaalilukuna. Voidaan asettaa poimintasäännön kentällä `IntimeCurrencyAmountTwo`.  
Alv-prosentti | Desimaaliluku (4,4) | 9 | 214 | 222 | Oletuksena tyhjä. Tyhjä arvo esitetään välilyöntimerkkeinä, muutoin esitetään desimaalilukuna. Voidaan asettaa poimintasäännön kentällä `IntimeVATPercentage`.  
Summa-2 | Desimaaliluku (12,2) | 15 | 223 | 237 | Oletuksena tyhjä. Tyhjä arvo esitetään välilyöntimerkkeinä, muutoin esitetään desimaalilukuna. Voidaan asettaa poimintasäännön kentällä `IntimeSumTwo`.  
Määrä1-2 | Desimaaliluku (10,4) | 15 | 238 | 252 | Oletuksena tyhjä. Tyhjä arvo esitetään välilyöntimerkkeinä, muutoin esitetään desimaalilukuna. Voidaan asettaa poimintasäännön kentällä `IntimeAmountOneTwo`.  
Määrä2-2 | Desimaaliluku (10,4) | 15 | 253 | 267 | Oletuksena tyhjä. Tyhjä arvo esitetään välilyöntimerkkeinä, muutoin esitetään desimaalilukuna. Voidaan asettaa poimintasäännön kentällä `IntimeAmountTwoTwo`.  
Lisätunniste | Merkkijono | 30 | 268 | 297 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeAdditionalIdentifier`.  
Jaksotustili 1 | Numero | 8 | 298 | 305 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimePeriodicityAccountOne`. Täydennetään välilyöntimerkeillä vasemmalle puolelle.  
Jaksotustili 2 | Numero | 8 | 306 | 313 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimePeriodicityAccountTwo`. Täydennetään välilyöntimerkeillä vasemmalle puolelle.  
Jaksotuskausien lukumäärä | Numero | 2 | 314 | 315 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeNumberOfPeriods`. Täydennetään välilyöntimerkeillä vasemmalle puolelle.  
Jaksotuksen alkukausi | Merkkijono | 4 | 316 | 319 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimePeriodicityStartingPeriod`.  
Jakson tositenumero | Numero | 8 | 320 | 327 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimePeriodVoucherNo`. Täydennetään välilyöntimerkeillä vasemmalle puolelle.  
Eurokoodi | Merkkijono | 1 | 328 | 328 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeEuroCode`.  
Omaisuuslaji | Merkkijono | 10 | 329 | 338 | Oletuksena tyhjä. Voidaan asettaa poimintasäännön kentällä `IntimeAssetType`.  
_Tyhjä_ |  | _62_ | _339_ | _400_ | _62 välilyöntimerkkiä_  
## Esimerkki
[code] 
    53480000003519091909190903Oiottu.virheet                    4600000000024            00000000000                                  KP    46005231510           50       10 00000000000 00000000000 190900000000000000 00240000 00000000010005-00000000000000 00000000000000                                                             0                                                                        
    53480000003519091909190903Tehty.jotain.mielenkiintoista     4860000000024            00000000000                                  KP    48605230510    5002   50       10 00000000000 00000000000 190900000000000000 00240000 00000000010005 00000000000000 00000000000000                                                             0                                                                        
    53480000003519091909190903                                  4600000000024            00000000000                                  KP    46005231510           50       10 00000000000 00000000000 190900000000000000 00240000 00000000008218 00000000000000 00000000000000                                                             0                                                                        
[/code]
