---
id: 360015842238
title: Henkilötietojen tuonti voimassa alkaen ja päättyen -tiedolla
url: https://support.nepton.com/hc/fi/articles/360015842238-Henkil%C3%B6tietojen-tuonti-voimassa-alkaen-ja-p%C3%A4%C3%A4ttyen-tiedolla
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tietojen voimassaolot henkilötuonneissa
section_id: 360004603778
section_path:
- Liittymät
- Henkilötiedot
- Tietojen voimassaolot henkilötuonneissa
labels: []
promoted: false
updated_at: '2024-06-03T10:20:25Z'
edited_at: '2024-06-03T10:20:23Z'
---

# Henkilötietojen tuonti voimassa alkaen ja päättyen -tiedolla

Voimassa alkaen ja päättyen -tiedolla tuonti mahdollistaa tulevien henkilötietomuutoksien tuomisen etukäteen. Myös henkilötietojen korjaus historiatietoihin onnistuu kätevästi. Tätä tuontitapaa ei tueta vielä muissa kuin tietyissä lähdejärjestelmäkohtaisissa henkilötuonneissa. Tuonnissa tuodaan henkilötietokenttien arvot, sekä niiden voimassaolot XML- tai JSON-muodossa.
Lisätietoa:
[Tietojen voimassaolot henkilötuonneissa](<https://support.nepton.com/hc/fi/articles/360015807338>)  
[Henkilöiden tuonti](<https://support.nepton.com/hc/fi/articles/360003762577>)  
[Henkilötuonnin kentät](<https://support.nepton.com/hc/fi/articles/360015933397>)  
[Pakolliset henkilötietokentät](<https://support.nepton.com/hc/fi/articles/360003762577#h_01F1F00HRZTD78QCZXSP1KE28P>)
## Aineistoesimerkki
Alla JSON-muotoinen esimerkki, jossa kenttä "Ammattinimike" tuodaan voimassa alkaen ja päättyen-tiedoilla. Etunimi- ja sukunimi-kenttien arvot tallennetaan "[Tuonti ilman voimassaoloja](<https://support.nepton.com/hc/fi/articles/360015741097>)"-tuontitavan mukaan, koska henkilö-solmulle ei ole määritetty "Voimassa alkaen"-kenttää.
"Henkilö": [
{
"Henkilönumero": "1234",
"Etunimi": "Esa",
"Sukunimi": "Esimerkki",
"Ammattinimike": [
{
"Voimassa alkaen": "2000-01-01",
"Voimassa päättyen": "2020-11-30",
"Arvo": "Myyjä"
},
{
"Voimassa alkaen": "2021-01-01",
"Voimassa päättyen": null,
"Arvo": "Myyntipäällikkö"
}
]
}
]
## Tietojen tallennuksen säännöt
Esitiedot:   
[Henkilötuonnin kentät](<https://support.nepton.com/hc/fi/articles/360015933397>)  
[Pakolliset henkilötietokentät](<https://support.nepton.com/hc/fi/articles/360003762577#h_01F1F00HRZTD78QCZXSP1KE28P>)
### Voimassaoloja tukevat kentät
  * Arvot tuodaan tuontiaineistossa määritetyillä voimassaoloilla
  * Kaikki olemassa olevat arvot korvataan tuonnissa määritetyillä arvoilla


### Voimassaoloja tukemattomat kentät
  * Kenttään tallennetaan voimassaolojen perusteella tuontipäivänä voimassa oleva arvo
  * Jos tuontipäivänä voimassa olevaa arvoa ei ole, tallennetaan kenttään tuontipäivästä katsottuna seuraavaksi tulevaisuudessa voimaantuleva arvo
  * Kentän arvoksi tallennetaan tyhjä, jos edellä mainittuja tuontipäivänä voimassa olevaa tai tulevaisuudessa voimaantulevaa arvoa ei ole


## Esimerkit
### Esimerkki: Uusi henkilö, tuontipäivä 12.12.2019
Tuotava aineisto:
"Henkilö": [
{
"Henkilönumero": "1234",
"Etunimi": "Esa",
"Sukunimi": "Esimerkki",
"Ammattinimike": [
{
"Voimassa alkaen": "2000-01-01",
"Voimassa päättyen": "2020-11-30",
"Arvo": "Myyjä"
},
{
"Voimassa alkaen": "2021-01-01",
"Voimassa päättyen": null,
"Arvo": "Myyntipäällikkö"
}
],
"Yksiköt": [
{
"Voimassa alkaen": "2000-01-01",
"Voimassa päättyen": "2020-12-31",
"Arvo": "Myynti"
}
]
}
]
Tulos:
Kenttä | Selitys  
---|---  
Henkilönumero: 1234, alkaen 12.12.2020 | Voimassaoloja tukeva kenttä. Tuotavat tiedot eivät sisällä kuitenkaan voimassaolotietoja, joten tuodaan ilman voimassaoloja tuontitavan mukaisesti -> Arvo voimassa alkaen tuontipäivästä.  
Etunimi *: Esa | Voimassaoloja tukeva pakollinen kenttä. Tuotavat tiedot eivät sisällä kuitenkaan voimassaolotietoja, joten tuodaan ilman voimassaoloja tuontitavan mukaisesti -> Ensimmäisen arvon voimassaolo ulotetaan menneisyyteen.  
Sukunimi *: Esimerkki | Sama kuin yllä.  
Ammattinimike: Myyjä, 1.1.2020 - 30.11.2020, Myyntipäällikkö, alkaen 1.1.2021 | Voimassaoloja tukeva kenttä. Arvot tuodaan tuontiaineistossa määritetyillä voimassaoloilla.  
Henkilöryhmä: Myynti | Voimassaoloja tukematon kenttä. Tuontipäivänä voimassa olevaa arvoa ei ole, tallennetaan kenttään tuontipäivästä katsottuna seuraavaksi tulevaisuudessa voimaantuleva arvo.  
### Esimerkki: Uusi henkilö, tuontipäivä 12.12.2019 - Kenttäryhmien käyttö
Sama lopputulos kuin yllä, saadaan myös tuomalla samat tiedot, mutta käyttämällä kenttäryhmäkohtaisia (alla "Työsuhde_TAULUKKO" ja "Organisaatio_TAULUKKO") voimassaoloja:
"Henkilö": [
{
"Henkilönumero": "1234",
"Etunimi": "Esa",
"Sukunimi": "Esimerkki",
"Työsuhde_TAULUKKO": [
{
"Voimassa alkaen": "2000-01-01",
"Voimassa päättyen": "2020-11-30",
"Ammattinimike": "Myyjä" },
{
"Voimassa alkaen": "2021-01-01",
"Voimassa päättyen": null,
"Ammattinimike": "Myyntipäällikkö" 
}
],
"Organisaatio_TAULUKKO": [
{
"Voimassa alkaen": "2000-01-01",
"Voimassa päättyen": "2020-12-31",
"Yksiköt": "Myynti"
}
]
}
]
