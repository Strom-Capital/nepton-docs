---
id: 360015741097
title: Person imports without validity information
url: https://support.nepton.com/hc/en-gb/articles/360015741097-Person-imports-without-validity-information
locale: en-gb
category: Support
category_id: 360000446658
section: Field validities in person imports
section_id: 360004603778
section_path:
- Integration
- HR data
- Field validities in person imports
labels: []
promoted: false
updated_at: '2021-12-08T10:36:05Z'
edited_at: '2021-12-08T10:36:05Z'
---

# Person imports without validity information

**Sorry!**
This article has not been translated yet.
Tuonti ilman voimassaoloja on yksinkertaisin tuonti, jossa tuodaan vain kenttien arvot. Tuonnissa arvot tallennetaan henkilötietoihin. Voimassaoloja tukevien kenttien arvot tallennettaan ja arvojen voimassaolo alkaa tuontipäivästä alkaen. Voimassaoloja tukemattomattomien kenttien arvot yksinkertaisesti tallennetaan uudeksi arvoksi.
Lisätietoa:
[Tietojen voimassaolot henkilötuonneissa](<https://support.nepton.com/hc/en-gb/articles/360015807338>)  
[Henkilöiden tuonti](<https://support.nepton.com/hc/en-gb/articles/360003762577>)  
[Henkilötuonnin kentät](<https://support.nepton.com/hc/en-gb/articles/360015933397>)  
[Pakolliset henkilötietokentät](<https://support.nepton.com/hc/en-gb/articles/360003762577#h_01F1F00HRZTD78QCZXSP1KE28P>)
## Aineistoesimerkki
Tietoja voidaan tuoda ilman voimassaoloja esimerkiksi [manuaalisella tuonnilla](<https://support.nepton.com/hc/en-gb/articles/360003762577>) Excel-dokumentin avulla seuraavasti:
Henkilönumero | Etunimi | Sukunimi | Ammattinimike  
---|---|---|---  
1234 | Esa | Esimerkki | Myyjä  
## Tietojen tallennuksen säännöt
Esitiedot:  
[Henkilötuonnin kentät](<https://support.nepton.com/hc/en-gb/articles/360015933397>)  
[Pakolliset henkilötietokentät](<https://support.nepton.com/hc/en-gb/articles/360003762577#h_01F1F00HRZTD78QCZXSP1KE28P>)
### Voimassaoloja tukevat kentät
  * Tuotavat tiedot tulevat voimaan tuontipäivästä alkaen
  * Mahdolliset tulevaisuudessa voimaantulevat arvot poistetaan
  * Mikäli [aina pakollisella kentällä](<https://support.nepton.com/hc/en-gb/articles/360003762577#h_01F1F00HRZTD78QCZXSP1KE28P>) ei ole olemassa olevaa arvoa, esim. uutta henkilöä lisättäessä, ulotetaan voimassaolo myös menneisyyteen. Tämä ei koske pakollisia [henkilöiden lisätietokenttiä](<https://support.nepton.com/hc/en-gb/articles/360002430918>), vaan niiden voimassaolo asetetaan samaan tapaan valinnaisten kenttien kanssa.


### Voimassaoloja tukemattomat kentät
  * Tuotavat tiedot tallennetaan uudeksi arvoksi
  * Voimassaoloja eivät tue kentät: "Ensisijainen esimies", "Toissijaiset esimiehet", "Työajan roolit", "Yksiköt", "Henkilöryhmä", "Oletusprojekti", "Saldo", sekä vaihtoehtoiset näitä tietoja tuovat kentät. Muut kentät tukevat voimassaoloja.


## Esimerkit
### Esimerkki: Uusi henkilö, tuontipäivä 1.1.2020
Tuotava aineisto:
Henkilönumero | Etunimi | Sukunimi | Ammattinimike | Henkilöryhmä  
---|---|---|---|---  
1234 | Esa | Esimerkki | Myyjä | Myynti  
Tulos:
Kenttä | Selitys  
---|---  
Henkilönumero: 1234, alkaen 1.1.2020 | Voimassaolotuki -> Tieto voimaan tuontipäivästä alkaen  
Etunimi *: Esa | Voimassaolotuki, pakollinen kenttä -> Ensimmäisen arvon voimassaolo ulotetaan menneisyyteen  
Sukunimi *: Esimerkki | Sama kuin yllä  
Ammattinimike: Myyjä, alkaen 1.1.2020 | Voimassaolotuki -> Tieto voimaan tuontipäivästä alkaen  
Henkilöryhmä: Myynti | Ei voimassaolotukea -> Tieto tallennetaan uudeksi arvoksi  
### Esimerkki: Henkilötietojen päivitys, tuontipäivä 1.1.2021
Alkutilanne:
Henkilönumero: 1234  
---  
Etunimi *: Esa  
Sukunimi *: Esimerkki  
Ammattinimike: Myyjä, alkaen 1.1.2020, Myyntipäällikkö, alkaen 1.1.2022  
Henkilöryhmä: Myynti  
Tuotava aineisto:
Henkilönumero | Etunimi | Sukunimi | Ammattinimike | Henkilöryhmä  
---|---|---|---|---  
1234 | Esa | Esimerkki | HR-asiantuntija | HR  
Tulos:
Kenttä | Selitys  
---|---  
Henkilönumero: 1234 | Voimassaolotuki. Tuotava arvo on sama -> Ei muutoksia.  
Etunimi *: Esa | Sama kuin yllä  
Sukunimi *: Esimerkki | Sama kuin yllä  
Ammattinimike: Myyjä, alkaen 1.1.2020, HR-asiantuntija, alkaen 1.1.2021 (tuontipäivä) | Voimassaolotuki. Tuotavat tiedot tulevat voimaan tuontipäivästä alkaen ja tulevaisuudessa voimaantulevat arvot poistetaan  
Henkilöryhmä: HR | Ei voimassaolotukea -> Tieto tallennetaan uudeksi arvoksi
