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
updated_at: '2025-03-07T15:06:08Z'
edited_at: '2025-03-07T15:06:08Z'
---

# Työsopimuspohjien lisääminen ja hallinnointi

Tämä artikkeli sisältää osin vanhentunutta tietoa. Artikkelia ollaan päivittämässä. Pahoittelemme tilannetta.
Tämä toiminnallisuus on käytettävissä, jos käytössä on HR Complete -palvelutaso. 
## Mikä on työsopimuspohja?
Neptonin Työsuhde-osiossa käytettäviä työsopimuspohjia on kahta perustyyppiä:
  * **Työsopimus**
    * Täytettävä HTML-muotoinen työsopimuslomake
    * Kutsutaan myös "**täytettäväksi työsopimuslomakkeeksi** "
  * **Työsopimusliite, Työtodistus, Palkkakuitti, Provisioliite**
    * Staattinen liite työsopimuksen teon yhteydessä, jota ei voi muokata
    * Työtekijä lukee ja hyväksyy nämä liitteet työsopimusta allekirjoitettaessa


Täytettävien HTML-muotoisten työsopimuslomakkeiden pohjalta, palveluun luodaan sähköisesti täytettäviä työsopimuksia. Voit ladata geneerisen täytettävän työsopimuslomakkeen pohjan (katso ohje alla), jota muokkaamalla, se voidaan personoida asiakaskohtaisiin tarpeisiin. Valmiit työsopimuspohjat liitetään [ työsopimuspaketteihin](<https://support.nepton.com/hc/fi/articles/360002590237>), joilla  [ luodaan työntekijöille sähköisiä työsopimuksia.](<https://support.nepton.com/hc/fi/articles/360002590277>)
### Täytettävä työsopimuslomake
**Voit ladata geneerisen täytettävän työsopimuslomakkeen pohjan sivun alalaidasta.**
  
**Esimääritellyt lomakekentät**  
Työsopimuspohjia tehtäessä on suositeltavaa käyttää Työsuhde-osioon esimääriteltyjä lomakekenttiä. Käyttämällä työsopimuspohjan lomakkeissa esimääriteltyjä lomakekenttien nimiä, Nepton noutaa työsopimuspohjaan henkilön tiedot tarvittaessa esimerkiksi Työsopimuksen tiedot -sivulta.  
  
**Tarvittavat lomaketoiminnot**  
Työsopimuspohjaan tarvitsee merkitä vain lomakekentät, joihin tietoa syötetään. Työsuhde täydentää luotuihin lomakkeisiin tarvittavat rakenteet ja elementit, kuten tallennuspainikkeet. Merkitessä lomakekenttiä pakollisia tietoja ovat name ja id, esimerkiksi seuraavasti: <input type="text" name="data_kokonimi" size="20" id="tt,ta">  
  
**Lomakekentän nimi**  
Edellisessä esimerkissä Työsuhde noutaa esimääriteltyyn lomakekenttään 'data_kokonimi' henkilön nimen kun hänelle luodaan uusi työsopimus. Jos työsopimuksessa kerätään tietoa, jota varten ei ole esimääriteltyä lomakekenttää, kentän voi nimetä vapaamuotoisesti. Älä käytä välilyöntejä ja skandinaavisia merkkejä.  
  
**Lomakekentän täyttöoikeus**  
Lomakekentän ID-arvossa määritellään, onko kentän täyttöoikeus työntekijällä, työnantajalla vai molemmilla sopijapuolilla.  
Merkitse tarpeen mukaan: id="tt,ta" jos sekä työntekijä että työntekijä voivat täyttää kentän. id="ta" jos vain työnantaja täyttää.  
id="tt" jos vain työntekijä täyttää.  
  
**Sallitut lomakekenttätyypit**  
Työsopimuspohjissa ei tällä hetkellä tueta checkbox-, radio- tai textarea-tyyppisiä lomakekenttiä tai pudotusvalikoita. Valintaruutujen ja -painikkeiden sijasta käyttää voi tekstikenttiä, joihin työntekijä täyttää kirjoittamalla kyllä/ei tai muita vaihtoehtoja.  
  
**Tyyleistä ja muotoilusta**  
Työsopimuspohjaksi soveltuu parhaiten yksinkertainen taulukolla muotoiltu lomake. Sopimuspohjaa laadittaessa kannattaa huomioida, että Työsuhteeseen tuotavasta HTML-koodista karsitaan <style>–elementit, linkit ulkoisiin tyylitiedostoihin, sekä kaikki <body>–elementin ulkopuolelle jäävät osat. CSS-muotoilut ovat mahdollisia merkitsemällä muotoilu suoraan haluttuun elementtiin, esimerkiksi:  
<table style=”font-family: Arial, Helvetica, sans-serif;color: #000;”>Työsopimuspohjan luominen / muokkaus
Käyttäjällä tulee olla [Ylläpitäjä-oikeustaso](<https://support.nepton.com/hc/fi/articles/360002425637>) palveluun.
## Hallinta
### Työsopimuspohjan luominen
  1. Siirry Työsuhde -> Sopimukset -> **Sopimuspohjat**.
  2. Siirry sivun yläosassa kohtaan **Lisää työsopimuspohja**.
  3. Valitse pohjan tiedostomuoto 
     * Työsopimus tarkoittaa täytettävää HTML-muotoista työsopimuslomaketta
     * Työsopimusliite, Työtodistus, Palkkakuitti, Provisioliite tarkoittaa staattista tiedostoa, joita ei voi muokata, vaan ovat liitteitä työsopimusta tehtäessä
  4. Valitse tietokoneelta haluamasi **tiedosto**. Anna pohjalle **nimi** ja **kuvaus**. 
     * Työsopimuksen tapauksessa, huomaa sivun alalaidassa malli. Muokkaamalla pohjaa, voidaan se personoida asiakaskohtaisiin tarpeisiin.
  5. Paina "**Tallenna** "


![mceclip0.png](https://support.nepton.com/hc/article_attachments/4410543688721)
### Työsopimuspohjan muokkaus
  1. Siirry Työsuhde -> Sopimukset -> **Sopimuspohjat**
  2. Voit **kynä -kuvakkeen** kautta muuttaa työsopimuspohjan **nimeä,** **kuvausta ja pohjan tyyppiä****.**
  3. Mikäli kyseessä on **Työsopimus** , voit muokata täytettävää HTML-lomaketta painamalla "**Muokkaa pohjaa** " 
     * Katso lisätietoja alta kohdasta "Täytettävä lomake (HTML) luonti ja muokkaus"
  4. Muutosten jälkeen paina **Tallenna**.


![mceclip3.png](https://support.nepton.com/hc/article_attachments/21077146462109)
### Täytettävän työsopimuslomakkeen muokkaus
  1. Työsopimuspohjat -sivulta täytettäviä työsopimuksia voi muokata valitsemalla työsopimuspohjan kohdalta **Muokkaa pohjaa** josta aukeaa Työsopimuspohjan muokkausnäkymä.
  2. Sivun yläosassa on työkalurivi, jonka avulla voit määrittää työsopimuspohjan muotoilua.
  3. Luodaksesi uuden täytettävän tekstikentän, siirry työsopimuspohjassa haluamaasi kohtaan ja valitse 'Textbox'/'abc'-painike työkaluriviltä.
  4. Työsopimuspohjan päälle aukeaa INPUT-ikkuna, johon tulee määritellä tekstikentän nimi (Name) sekä täyttöoikeus (ID). Mikäli tietokentän sisältö tulee siirtää henkilön tietoihin, tulee kentän nimenä olla jokin esimääritellyistä tietokenttien nimistä. Lista käytettävistä tietokentistä esitetään alempana. 
     * **HUOM** : Kentän nimessä ei saa käyttää skandinaavisia tai muita erikoismerkkejä.
  5. Täyttöoikeudet (ID): kentälle tulee määrittää täyttöoikeus, joka kertoo ohjelmalle, kenellä on oikeus täyttää kyseinen kenttä. **ta** = työnantaja täyttää, **tt** = työntekijä täyttää **ta,tt** = molemmat voi täyttää.
  6. ID-kenttään voidaan merkitä lisämääre opt_ , joka tarkoittaa sitä että kenttä voidaan jättää täyttämättä esimiehen tai työntekijän toimesta. Muussa tapauksessa kenttä täytyy täyttää ennen kuin työsopimus voidaan hyväksyä.
  7. Tekstikenttä luodaan työsopimuspohjaan painettaessa **OK** -painiketta.
  8. Olemassa olevien täytettävien tekstikenttien muokkaus kannattaa tehdä lähdekoodi-näkymässä. 
     * Lähdekoodinäkymä on tarkoitettu edistyneemmille käyttäjille
     * Pääset lähdekoodinäkymään painamalla 'HTML'-painiketta näkymän alaosasta
  9. Kun työsopimuspohja on valmis **muista tallentaa** muutokset sivun alalaidassa olevalla **Tallenna** \- painikkeesta.


## Työntekijän tietoihin liitetyt tietokentät
Mikäli täytettävän työsopimuslomakkeen täytettävän tekstikentän nimenä käytetään jotakin alla olevista, tallentuu kentän sisältö työntekijän tietoihin, kun työsopimus hyväksytään. Työsopimusta luodessa nämä tietokentät esitäytetään työntekijän tietokenttien perusteella.  
  
Alla olevan listan lisäksi työsopimuksella voidaan vapaasti käyttää palveluun perustettuja lisätietokenttiä. Lisätietokenttien perustamisen yhteydessä kentälle voidaan antaa oma data_-tunnisteensa.  
  
  

**Tietokentän nimi** | **Tietokentän tunniste**  
---|---  
Etunimi  | data_etunimi  
Sukunimi | data_lastname  
Henkilötunnus | data_hetu  
Sähköposti | data_email  
Puhelinnumero | data_puhelinnumero  
Tilinumero (IBAN) | data_tilinumero  
BIC | data_BIC  
Katuosoite | data_katuosoite  
Postinumero | data_postinumero  
Postitoimipaikka | data_kaupunki  
Työsuhteen alkupäivä | data_aloituspvm  
Työsuhteen päättymispäivä | data_lopetuspvm  
Viikottainen työaika | data_viikkotunnit  
Tuntipalkka | data_tuntipalkka  
Kuukausipalkka | data_monthlySalary  
Oletuskustannuspaikka |  data_oletuskustannuspaikka  
Koeajan päättymispäivä |  data_koeaika_paattyy  
Ammattinimike |  data_jobtitle  
Työskentelyalue |  data_alue  
Työaikaprosentteina |  data_worktimepercentage
