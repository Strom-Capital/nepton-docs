---
id: 360003733858
title: Henkilötietojen tuonti - Sympa
url: https://support.nepton.com/hc/fi/articles/360003733858-Henkil%C3%B6tietojen-tuonti-Sympa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Järjestelmäkohtaiset henkilötietojen tuonnit
section_id: 7976634441629
section_path:
- Liittymät
- Henkilötiedot
- Järjestelmäkohtaiset henkilötietojen tuonnit
labels:
- Person Import
promoted: false
updated_at: '2026-04-23T08:50:26Z'
edited_at: '2026-04-23T08:49:59Z'
---

# Henkilötietojen tuonti - Sympa

SFTP-palvelimelle tulee muodostaa CSV-, Excel- (XLS- tai XLSX-), XML- tai JSON-muotoinen aineisto. Muodostettavan aineiston tulee tiedostonimessä sisältää luontihetken aikaleima. Tällä varmistetaan, että mikäli aineistossa siirtyy vain muuttunut tieto, aiempaa tietoa ei missään tilanteessa ylikirjoiteta.
Tiedosto on tallennettava joko UTF-8- tai ISO-8859-1-merkistökoodauksella. CSV-tiedoston tietueet on erotettava puolipisteillä ( ; ). Rivinvaihdon merkkinä voidaan käyttää joko Windows-tyylistä ( \r\n ) tai UNIX-tyylistä ( \n ) rivinvaihtoa. Jompikumpi rivinvaihtomerkki muodostuu oletuksena lähes kaikista tietojärjestelmistä.
Otsikkorivi voidaan määrittää ajastetun tehtävän määrityksissä tai osana tiedostoa. Mikäli otsikkorivi ei sisälly aineistoon, tulee sen olla määritelty ajastetulla tehtävällä. Sarakkeet voivat olla aineistossa missä tahansa järjestyksessä. Tiedon vastaavuus määritellään ajastetun tehtävän säännöissä. Ohjeet ajastetun tehtävän muodostamiseen löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360002489317>).
Aineistossa yhden henkilön tiedot esitetään yhdellä rivillä. Aineiston perusteella uudet henkilöt luodaan automaattisesti ja olemassa olevia henkilötietoja päivitetään. Aineistossa voidaan tuoda kaikki palvelun kiinteät tietokentät, sekä mitä tahansa henkilötietoihin perustettuja lisätietokenttiä.
Tuonnissa voi käyttää mitä tahansa [yleisen](<https://support.nepton.com/hc/fi/articles/360003762577>) tiedontuonnin kenttiä pois lukien "käyttäjätili aktiivinen". Tämän tietokentän arvo asetetaan automaattisesti perustuen siihen, onko henkilön työsuhde aktiivinen tiedon tuontipäivänä. Esimerkkinä, jos 31.10. aineistossa käyttäjän työsuhteen päättymispäivä on 31.10., seuraavan päivän aineistossa 1.11. käyttäjätili on muuttunut ei-aktiiviseksi, koska työsuhteen päättymispäivä on menneisyydessä. Ei-aktiivinen käyttäjätili voidaan palauttaa käyttöön asettamalla "Työsuhteen päättymispäivä" tulevaisuuteen tai poistamalla se tuomalla tyhjä arvo.
Huomaathan, että käyttäjätunnusta ei voi muuttaa liittymällä.
Alla on luettelo tähän tuontitapaan liittyvistä erikoiskentistä.
**Tietue** | **Kuvaus**  
---|---  
Määräaikaisen työsopimuksen lopetus pvm | Tuontitiedoston ja Neptonissa olevan työsuhteen päättymispäivä -kenttää verrataan toisiinsa. Se, kummassa on myöhäisempi arvo, jää voimaan.  
Ensisijainen esimies | Ensisijainen esimies.  
Esimies1 | Tämä tieto yhdistyy 'Esimies 2' -kentän kanssa ja muodostaa toissijaiset esimiehet.  
Esimies2 | Tämä tieto yhdistyy 'Esimies 1' -kentän kanssa ja muodostaa toissijaiset esimiehet.  
Organisaatiotaso1Koodi | Nämä kentät asettavat henkilön oikeaan henkilöryhmään työyhteisön hierarkiassa. Hierarkiatiedot on jaettu tasoihin 1-10. Kun näitä kenttiä käytetään, tulee myös Organisaation nimet olla käytössä.  
Organisaatiotaso2Koodi | N/A  
Organisaatiotaso3Koodi | N/A  
Organisaatiotaso4Koodi | N/A  
Organisaatiotaso5Koodi | N/A  
Organisaatiotaso6Koodi | N/A  
Organisaatiotaso7Koodi | N/A  
Organisaatiotaso8Koodi | N/A  
Organisaatiotaso9Koodi | N/A  
Organisaatiotaso10Koodi | N/A  
Organisaatiotaso1Nimi | Nämä kentät asettavat henkilön oikeaan henkilöryhmään työyhteisön hierarkiassa. Hierarkiatiedot on jaettu tasoihin 1-10. Kun näitä kenttiä käytetään, tulee myös Organisaation koodit olla käytössä.  
Organisaatiotaso2Nimi | N/A  
Organisaatiotaso3Nimi | N/A  
Organisaatiotaso4Nimi | N/A  
Organisaatiotaso5Nimi | N/A  
Organisaatiotaso6Nimi | N/A  
Organisaatiotaso7Nimi | N/A  
Organisaatiotaso8Nimi | N/A  
Organisaatiotaso9Nimi | N/A  
Organisaatiotaso10Nimi | N/A  
Työsopimuksen aloitus pvm | (DD.MM.YYYY) Työsopimuksen alkamispäivä. Huomioi, että voimassaolevan työsopimuksen alkamispäivä voidaan päivittää vain aikaisemmaksi arvoksi kuin olemassaoleva tieto.  
Työsopimuksen lopetus pvm | (DD.MM.YYYY) Työsopimuksen päättymispäivä. Huomioi, että voimassaolevan työsopimuksen päättymispäivä voidaan päivittää vain myöhäisemmäksi arvoksi kuin olemassaoleva tieto.  
## Työsuhteen keston muuttaminen
  * Työsuhteen alkupäivä
    * Jos henkilön työsuhteen alkupäivää ei ole asetettu, tallennetaan tuonnissa oleva uusi arvo.
    * Jos henkilön työsuhteen alkupäivä on jo asetettu, tallennetaan tuonnissa oleva arvo ainoastaan, jos se on aikaisempi kuin olemassa oleva arvo tai arvo on tyhjä.
  * Työsuhteen päättymispäivä
    * Jos henkilön työsuhteen päättymispäivää ei ole asetettu, tallennetaan tuonnissa oleva uusi arvo.
    * Jos henkilön työsuhteen päättymispäivä on jo asetettu, tallennetaan tuonnissa oleva arvo ainoastaan, jos se on myöhäisempi kuin olemassa oleva arvo tai arvo on tyhjä.


Tällä rajoituksella taataan, että henkilöt, joilla on useampi Työsuhteen alkupäivä, käsitellään ja näytetään palvelussa oikein.
Jos henkilöitä tuodaan käyttöliittymän kautta, Työsuhde->Henkilöt->Tuo henkilöitä, mahdolliset tyhjät arvot näissä kentissä jätetään huomioimatta.
Huom: Kun henkilön työsuhteen päättymispäivä merkitään Sympaan viimeisenä työpäivänä tai tämän jälkeen, tulisi näissä tilanteissa Sympan ohjeiden mukaan Sympan Valid until -päiväksi merkitä kirjauspäivää seuraava päivä, jotta tieto siirtyy.
## Tiedon yhdenmukaisuus
**Henkilöryhmän nimet ja koodit**
Siirrettävässä aineistossa voidaan siirtää jokaiselle henkilölle heidän sijaintinsa henkilöryhmä-rakenteessa ja tätä rakennetta vastaavat koodit. Mikäli aineistossa siirretään ristiriitaista tietoa siten, että eri riveillä samoille organisaation koodeille annetaan eri nimiä niin siirtolokissa esitetään tästä virhe. Tällöin henkilöryhmän nimeä ei voida päivittää, sillä aineistossa on samalla ryhmälle useita eri nimiä. Muilta osin aineisto luetaan palveluun.
Kaikkien henkilöryhmäkoodien on oltava yksilöllisiä. Samaa henkilöryhmäkoodia ei siis voi olla kahdella eri henkilöryhmällä, vaikka ne olisivat eri organisaatiotasolla tai eri hierarkioiden alla.
