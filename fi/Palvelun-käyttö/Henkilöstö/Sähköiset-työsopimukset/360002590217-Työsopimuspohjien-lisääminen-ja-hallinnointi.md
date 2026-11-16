---
id: 360002590217
title: Työsopimuspohjien lisääminen ja hallinnointi
url: https://support.nepton.com/hc/fi/articles/360002590217-Ty%C3%B6sopimuspohjien-lis%C3%A4%C3%A4minen-ja-hallinnointi
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sähköiset työsopimukset
section_id: 360000708617
section_path:
- Henkilöstö
- Sähköiset työsopimukset
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-11-16T13:54:48Z'
edited_at: '2026-11-11T12:14:51Z'
---

# Työsopimuspohjien lisääminen ja hallinnointi

Neptonissa sähköiset työsopimukset luodaan täytettävien työsopimuspohjien perusteella. Työsopimuspohjia voidaan muokata organisaation tarpeisiin, ja niiden kenttiä voidaan yhdistää työntekijän tietoihin.
Työsopimuspohjien hallinnointi tapahtuu kohdassa **Työsuhde > Sopimukset > Sopimuspohjat**.
Työsopimuspohjien luominen ja muokkaaminen edellyttää **Ylläpitäjä-oikeuksia**.
Olemme luoneet yleisen työsopimuspohjan esimerkkitiedoston helpottamaan ominaisuuden käyttöönottoa. Suosittelemme käyttämään esimerkkipohjaa uuden työsopimuspohjan lähtökohtana. Pohjan voi ladata [tästä](<https://support.nepton.com/hc/fi/article_attachments/11444518799389/working-contract.zip>) ja muokata organisaation tarpeisiin tämän ohjeen avulla.
Valmiista työsopimuspohjista voidaan muodostaa [työsopimuspaketteja](<https://support.nepton.com/hc/fi/articles/360002590237>), joiden perusteella varsinainen työsopimus luodaan, täydennetään ja allekirjoitetaan.
## Työsopimuspohjat ja liitteet
**Työsuhde > Sopimukset > Sopimuspohjat** -näkymässä hallitaan sähköisten työsopimusten pohjia ja niihin liitettäviä tiedostoja.
Käytettävissä olevia pohjatyyppejä ovat:
  * **Työsopimus**
    * Täytettävä HTML-muotoinen työsopimuslomake. Sen perusteella Neptoniin luodaan sähköisesti täytettävä työsopimus.
  * **Työsopimusliite**
    * Staattinen tiedosto, joka voidaan liittää työsopimukseen. Työsopimusliite voi olla esimerkiksi vaitiolovelvollisuus- tai etätyösopimus.
  * **Provisioliite**
    * Staattinen tiedosto, joka voidaan liittää työsopimukseen.


Varsinainen täytettävä työsopimuspohja on HTML-tiedosto. Staattiset liitetiedostot voivat olla esimerkiksi PDF-tiedostoja.
## Työsopimuspohjan luominen
  1. Siirry kohtaan **Työsuhde > Sopimukset > Sopimuspohjat**.
  2. Valitse **Lisää työsopimuspohja**.
  3. Anna pohjalle nimi ja kuvaus.
  4. Valitse pohjan tyyppi.
  5. Valitse tietokoneeltasi haluamasi tiedosto.
  6. Valitse **Tallenna**.


Kun luot täytettävää työsopimusta, valitse tyypiksi **Työsopimus** ja käytä **HTML-muotoista tiedostoa**.
Uutta työsopimuspohjaa ei yleensä tarvitse rakentaa alusta. Voit käyttää [Neptonin esimerkkipohjaa](<https://support.nepton.com/hc/fi/article_attachments/11444518799389/working-contract.zip>) lähtökohtana ja muokata sen organisaatiosi tarpeisiin.
![Työsopimuspohjan lisääminen](https://support.nepton.com/hc/article_attachments/40409576072605)
## Työsopimuspohjan muokkaaminen
Työsopimuspohjan perustietoja muutetaan seuraavasti:
  1. Siirry kohtaan **Työsuhde > Sopimukset > Sopimuspohjat**.
  2. Valitse halutun työsopimuspohjan kohdalta **kynäkuvake**.
  3. Muokkaa tarvittaessa pohjan nimeä, kuvausta tai tyyppiä.
  4. Valitse **Tallenna**.


![Työsopimuspohjan tietojen muokkaaminen](https://support.nepton.com/hc/article_attachments/20600408591901)
Jos kyseessä on täytettävä **Työsopimus** -tyyppinen pohja, sen sisältöä voidaan muokata valitsemalla **Muokkaa pohjaa**.
Työsopimuspohjaa voidaan muokata joko graafisella editorilla tai suoraan HTML-koodina.
![Muokkaa pohjaa -painike](https://support.nepton.com/hc/article_attachments/25680495740957)
### Graafisen editorin käyttäminen
Graafinen editori soveltuu erityisesti tekstien, otsikoiden ja muiden yksinkertaisten sisältöjen muokkaamiseen sekä uusien täytettävien tekstikenttien lisäämiseen.
![Työsopimuspohjan graafinen editori](https://support.nepton.com/hc/article_attachments/25680495749021)
Uusi täytettävä tekstikenttä lisätään seuraavasti:
  1. Siirry työsopimuspohjassa kohtaan, johon haluat lisätä kentän.
  2. Valitse työkaluriviltä **Textbox / abc**.
  3. Määritä kentän nimi (**Name**).
  4. Määritä kentän täyttöoikeus (**ID**).
  5. Lisää kenttä valitsemalla **OK**.
  6. Tallenna lopuksi työsopimuspohjaan tekemäsi muutokset.


Jos kentän sisältö halutaan yhdistää työntekijän tietoihin, kentän nimen tulee vastata Neptonin tukemaa tietokentän tunnistetta. Tunnisteet on kuvattu tarkemmin tämän ohjeen lopussa.
![Textbox-kentän lisääminen](https://support.nepton.com/hc/article_attachments/25680495745309)
### HTML-editorin käyttäminen
Vaativammat muutokset kannattaa tehdä suoraan HTML-koodiin.
HTML-näkymään pääsee valitsemalla editorissa **HTML**.
![HTML-editorin avaaminen](https://support.nepton.com/hc/article_attachments/25680495752221)
HTML-editorissa voidaan esimerkiksi:
  * muuttaa olemassa olevia lomakekenttiä
  * lisätä uusia HTML-elementtejä
  * määrittää kenttien ominaisuuksia
  * muuttaa sopimuksen ulkoasua inline CSS -tyyleillä
  * lisätä kuvia Base64-muodossa


HTML-editorin käyttäminen edellyttää HTML:n perusteiden tuntemista.
HTML-koodia voidaan muokata suoraan Neptonissa. Pohjan HTML-koodin voi myös kopioida ja tallentaa omalle tietokoneelle `.html`-tiedostoksi, jota voidaan muokata erillisellä tekstieditorilla.
## Työsopimuspohjan tietokentät
Työsopimuspohjaan voidaan lisätä tavallisten kenttien lisäksi kenttiä, jotka on yhdistetty Neptonissa oleviin työntekijän tietoihin.
Työsopimuspohjaan tarvitsee määrittää vain ne lomakekentät, joihin tietoa syötetään. Nepton täydentää lomakkeeseen sen toiminnan edellyttämät muut rakenteet ja elementit, kuten tallennuspainikkeet.
Täytettävälle lomakekentälle tulee määrittää vähintään kentän nimi (`name`) ja täyttöoikeus (`id`).
Kun kentälle käytetään Neptonin määrittelemää `data_`-tunnistetta, kentän arvo voidaan esitäyttää työntekijän tiedoista. Työsopimuksen hyväksymisen yhteydessä kenttään syötetty tieto voidaan vastaavasti tallentaa työntekijän tietoihin.
Kenttä voi näyttää HTML-koodissa esimerkiksi tältä:
[code] 
    <input type="text" name="data_etunimi" size="40" id="tt">
[/code]
Tässä `data_etunimi` yhdistää kentän työntekijän etunimeen ja `tt` määrittää kentän työntekijän täytettäväksi.
Tämän ohjeen kohdassa **Työntekijän tietoihin yhdistettävät tietokentät** on lueteltu käytettävissä olevia tunnisteita.
Palveluun luoduille lisätietokentille voidaan lisäksi määrittää oma `data_`-tunniste.
### Kentän nimi
Kentän `name`-arvo määrittelee lomakekentän nimen.
Kun `name`-arvona käytetään Neptonin esimääriteltyä `data_`-tunnistetta, kenttä voidaan yhdistää vastaavaan työntekijän tietoon.
Jos työsopimuksella kerätään tietoa, jota ei tarvitse yhdistää työntekijän tietoihin, kentälle voidaan antaa vapaamuotoinen nimi.
Kentän nimessä ei tule käyttää välilyöntejä, skandinaavisia merkkejä tai muita erikoismerkkejä.
### Kentän täyttöoikeus
Lomakekentän `id`-attribuutilla määritellään, kuka voi täyttää kentän.
Täyttöoikeudet ovat:
  * `id="ta"` = työnantaja täyttää kentän
  * `id="tt"` = työntekijä täyttää kentän
  * `id="ta,tt"` = sekä työnantaja että työntekijä voivat täyttää kentän


Kenttään voidaan lisäksi määrittää `opt_`-lisämääre silloin, kun kentän täyttäminen ei ole pakollista. Muussa tapauksessa kenttä tulee täyttää ennen kuin työsopimus voidaan hyväksyä.
### Sallitut lomakekenttätyypit
Työsopimuspohjissa voidaan käyttää täytettäviä tekstikenttiä.
Radio-tyyppisiä lomakekenttiä tai pudotusvalikoita ei tueta. Pudotusvalikon sijaan voidaan käyttää tekstikenttää, johon käyttäjä kirjoittaa valintansa lomakkeessa annettujen ohjeiden mukaisesti.
## Tyylit, muotoilu ja kuvat
Työsopimuspohja kannattaa pitää HTML-rakenteeltaan mahdollisimman yksinkertaisena. Yksinkertainen taulukkopohjainen rakenne soveltuu hyvin työsopimuspohjaksi.
Neptoniin tuotavasta HTML-koodista poistetaan:
  * `<style>`-elementit
  * viittaukset ulkoisiin CSS-tyylitiedostoihin
  * `<body>`-elementin ulkopuolinen sisältö


Työsopimuspohjan ulkoasua voidaan muokata **inline CSS -tyyleillä** , jolloin muotoilu määritellään suoraan HTML-elementin `style`-attribuutissa.
Esimerkiksi:
[code] 
    <table style="font-family: Arial, Helvetica, sans-serif; color: #000;">
[/code]
Inline CSS:n avulla voidaan määrittää esimerkiksi:
  * fontti
  * tekstin koko ja väri
  * taustaväri
  * elementtien leveys
  * reunukset
  * tasaus
  * välit ja marginaalit


### Kuvien ja logon lisääminen
Työsopimuspohjaan voidaan lisätä kuvia, kuten organisaation logo. Kuva lisätään HTML-tiedostoon **Base64-koodattuna** , jolloin kuva sisältyy suoraan työsopimuspohjaan eikä sitä tarvitse ladata ulkoisesta kuvatiedostosta.
#### Kuvan muuntaminen Base64-muotoon
Muunna ensin haluamasi kuva Base64-muotoon tähän soveltuvalla työkalulla. Muunnoksen tuloksena saat kuvan sisältöä vastaavan Base64-merkkijonon.
Kuva kannattaa pienentää ja optimoida ennen muuntamista, jotta työsopimuspohjan koko ei kasva tarpeettomasti. Base64-koodaus kasvattaa datan kokoa tyypillisesti noin kolmanneksella.
#### Base64-kuvan lisääminen HTML-koodiin
Base64-koodattu kuva lisätään HTML:n `<img>`-elementin `src`-attribuuttiin.
Esimerkiksi PNG-kuva:
[code] 
    <img src="data:image/png;base64,BASE64-KOODATTU-KUVA" alt="Logo">
[/code]
`src`-attribuutin sisältö muodostetaan muodossa:
[code] 
    data:image/png;base64,BASE64-KOODATTU-KUVA
[/code]
Siinä:
  * `image/png` määrittää kuvan tiedostotyypin
  * `base64` kertoo sisällön olevan Base64-koodattu
  * pilkun jälkeen lisätään kuvan varsinainen Base64-merkkijono


Tämä vastaa HTML:ssä käytettävän Data URL:n rakennetta `data:[mediatype];base64,[data]`.
Käytä kuvan tiedostomuotoa vastaavaa mediatyyppiä. Esimerkiksi:
  * PNG: `image/png`
  * JPEG/JPG: `image/jpeg`


Base64-merkkijono voi olla erittäin pitkä. Tämä on normaalia. Koko merkkijono lisätään `src`-attribuuttiin `base64,`-tekstin jälkeen.
#### Kuvan koon muuttaminen
Kuvan kokoa voidaan määrittää inline CSS -tyyleillä. Esimerkiksi logon leveydeksi voidaan määrittää 180 pikseliä:
[code] 
    <img src="data:image/png;base64,BASE64-KOODATTU-KUVA"
         style="width: 180px; height: auto;"
         alt="Logo">
[/code]
`width: 180px` määrittää kuvan leveydeksi 180 pikseliä ja `height: auto` säilyttää kuvan alkuperäisen kuvasuhteen.
## Olemassa olevan työsopimuspohjan käyttäminen uuden pohjana
Jos uusi työsopimuspohja eroaa vain vähän olemassa olevasta pohjasta, pohjaa ei tarvitse rakentaa kokonaan uudelleen. Olemassa olevaa pohjaa voidaan käyttää uuden pohjan lähtökohtana.
  1. Avaa olemassa oleva työsopimuspohja muokattavaksi.
  2. Avaa **HTML** -näkymä.
  3. Kopioi pohjan HTML-koodi.
  4. Liitä HTML-koodi tekstieditoriin.
  5. Tee tarvittavat muutokset.
  6. Tallenna tiedosto `.html`-muodossa.
  7. Siirry takaisin Neptoniin kohtaan **Työsuhde > Sopimukset > Sopimuspohjat**.
  8. Valitse **Lisää työsopimuspohja** ja lisää tallentamasi HTML-tiedosto uutena pohjana.


Näin olemassa olevan pohjan rakennetta ja muotoiluja voidaan hyödyntää ilman uuden pohjan rakentamista alusta.
## Työntekijän tietoihin yhdistettävät tietokentät
Kun työsopimuksen kentän `name`-arvona käytetään jotakin alla olevista tunnisteista, kenttä voidaan yhdistää vastaavaan työntekijän tietoon.
Työsopimusta luotaessa tietoja voidaan esitäyttää työntekijän tiedoista. Työsopimuksen hyväksymisen yhteydessä kenttiin syötetyt tiedot voidaan tallentaa työntekijän tietoihin.
Tietokenttä | Tunniste  
---|---  
Etunimi | `data_etunimi`  
Sukunimi | `data_lastname`  
Henkilötunnus | `data_hetu`  
Sähköposti | `data_email`  
Puhelinnumero | `data_puhelinnumero`  
Tilinumero (IBAN) | `data_tilinumero`  
BIC | `data_BIC`  
Katuosoite | `data_katuosoite`  
Postinumero | `data_postinumero`  
Postitoimipaikka | `data_kaupunki`  
Työsuhteen alkupäivä | `data_aloituspvm`  
Työsuhteen päättymispäivä | `data_lopetuspvm`  
Viikoittainen työaika | `data_viikkotunnit`  
Tuntipalkka | `data_tuntipalkka`  
Oletuskustannuspaikka | `data_oletuskustannuspaikka`  
Koeajan päättymispäivä | `data_koeaika_paattyy`  
Ammattinimike | `data_jobtitle`  
Työskentelyalue | `data_alue`  
Työaikaprosentti | `data_worktimepercentage`  
Työsopimuksella voidaan käyttää myös palveluun luotuja lisätietokenttiä. Lisätietokentän perustamisen yhteydessä sille voidaan määrittää oma `data_`-tunniste.
## Seuraavat vaiheet
Kun tarvittavat työsopimuspohjat ja liitteet on luotu, niistä muodostetaan **työsopimuspaketti**. Työsopimuspaketti määrittelee varsinaisen sähköisen työsopimuksen yhteydessä käytettävän pohjan ja siihen kuuluvat liitteet.
Katso seuraavaksi:
  * [Työsopimuspaketit](<https://support.nepton.com/hc/fi/articles/360002590237>)
  * [Työsopimuksen täyttäminen ja allekirjoittaminen](<https://support.nepton.com/hc/fi/articles/360002590277>)
