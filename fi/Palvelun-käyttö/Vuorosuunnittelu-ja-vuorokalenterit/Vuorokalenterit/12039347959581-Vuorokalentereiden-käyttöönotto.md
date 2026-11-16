---
id: 12039347959581
title: Vuorokalentereiden käyttöönotto
url: https://support.nepton.com/hc/fi/articles/12039347959581-Vuorokalentereiden-k%C3%A4ytt%C3%B6%C3%B6notto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Vuorokalenterit
section_id: 10363010715933
section_path:
- Vuorosuunnittelu ja vuorokalenterit
- Vuorokalenterit
labels:
- Work schedules
promoted: false
updated_at: '2026-07-09T08:09:24Z'
edited_at: '2024-07-26T10:52:36Z'
---

# Vuorokalentereiden käyttöönotto

Tässä artikkelissa kerrotaan, miten Vuorokalenterit-toiminnallisuus otetaan käyttöön Neptonissa.
# Edellytykset
## Vuorosuunnittelu-toiminto
Jotta voit käyttää Vuorokalenterit-toimintoa, sinulla on oltava pääsy Neptonin Vuorosuunnittelu-toimintoon asiaankuuluvalla Vuorosuunnittelu-palvelutasolla. Viimeisimmän tiedon Neptonin palvelutasoista ja hinnoittelusta saat [Asiakaspalvelusta](<https://support.nepton.com/hc/fi/articles/7077076926237-Asiakaspalvelun-yhteystiedot>).
## Vuorosuunnittelun oikeudet
Kun Vuorokalenterit ollaan ottamassa käyttöön, on päätettävä mitä oikeuksia tarvitaan vuorosuunnitteluun ja päivittäisiin toimintoihin. Vaikka kyseistä prosessia ohjaa pitkälti organisaation rakenne, seuraavanlainen määrittely on suositeltavaa:
  * Hallinnoijarooleilla (ylläpitäjä ja palkkahallinto) on pääsy kaikkiin Vuorosuunnittelun ja Vuorokalentereiden toimintoihin koko ympäristössä. Tämä on hyvin käytännöllistä määrittelyiden, ongelmanratkaisun ja hallinnoinnin kannalta.
  * Yksikön johtaja-roolilla on pääsy kaikkiin Vuorosuunnittelun ja Vuorokalentereiden toimintoihin niiden yksiköiden osalta, joihin kyseisellä käyttäjällä on kytkös.
  * Käyttäjillä, joilla on alaisia (Esimies-rooli, esim. tiimin johtajat), on oikeus nähdä ja hallinnoida alaistensa työvuoroja ja vuorokalentereita riippuen toimipisteestä, johon heidät on liitetty. 
    * Lisätietoa [täällä](<https://support.nepton.com/hc/fi/articles/360011258978>).
  * Työntekijöillä ei ole pääsyä Vuorosuunnittelu- ja Vuorokalenterit -toimintoihin, mutta he näkevät työvuoronsa Työaika-osion kalenterissa.


## Yksiköt
Jotta Vuorokalentereita voidaan käyttää, täytyy vähintään yksi Yksikkö olla määriteltynä osiossa Työsuhde > Yksiköt. Jotta käyttäjä voi nähdä työvuoroja, tulee hänen olla yksikön jäsen.
Yksiköt ovat Neptonissa perustietoa. (Lue aiheesta lisää [täältä](<https://support.nepton.com/hc/fi/articles/360002590317-Yksik%C3%B6t>).) Vuorokalenteri linkitetään aina Yksikköön, mikä mahdollistaa eri vuorokalenterien näyttämisen jokaiselle yksikölle.
# Vuorokalenterien luominen
Lisätietoa Vuorokalentereiden perusideasta ja niiden käyttökohteista löydät [täältä](<https://support.nepton.com/hc/fi/articles/12038486266909-Mit%C3%A4-ovat-Vuorokalenterit->).
## Vuorokalenterin luominen
  1. Kun haluat luoda Vuorokalenterin, valitse Vuorosuunnittelu > Vuorokalenterit ja klikkaa "Lisää".
  2. Täytä kalenterin perustiedot kuten Vuorokalenterin tyyppi ja koodi. Koodin tulee olla uniikki. Valitse Tallenna.
  3. Lisää vuororyhmät, jotka edustavat työntekijäryhmiä ja vuoromallia tämän kalenterin osalta.  

     * On suositeltava antaa ryhmälle yksilöllinen koodi, jotta massatoimintoja voidaan käyttää liittyen ryhmiin.


Kalenterit eivät näy Vuorosuunnittelun Suunnittelunäkymässä tai Työaika-näkymässä ennen kuin vähintään yksi vuorokalenterijakso on määritelty ja julkaistu.
## Lomakalenterin luominen
Kun on tarve jakaa vuororyhmä lomasuunnitelmaa varten, tulee tätä varten luoda lomakalenteri. Lomakalenterin suunnitellut tapahtumat yliajavat Vuorokalenterin tapahtumat. Käyttäjien tulee olla lomakalenteriryhmän jäseniä oman vuororyhmänsä lisäksi, jotta lomakalenterin tapahtumat yliajavat vuorokalenterin tapahtumat.
Esimerkiksi, jos työntekijä tekee normaalisti vuorotyötä mallilla A A A - - Y - V - - - mutta he ovat samaan aikaan sellaisen lomakalenterin jäseniä, mihin on suunnitelty ylimääräisiä lepo- ja lomapäiviä (E on tyhjä päivä lomakalenterissa) - - E H H H H E E E E. Näiden yhdistelmä työntekijälle näyttäisi tältä: - - A H H H H V - - -.
  1. Kun haluat luoda Lomakalenterin, valitse Vuorosuunnittelu > Vuorokalenteri ja klikkaa "Lisää".
  2. Täytä kalenterin perustiedot, valitse Vuorokalenterin tyypiksi Lomakalenteri. Valitse Tallenna.
  3. Lisää vuororyhmät, joiden jäsenille lomia on tarkoitus suunnitella. 
     * On suositeltava antaa ryhmälle yksilöllinen koodi, jotta massatoimintoja voidaan käyttää liittyen ryhmiin.


Kalenterit eivät näy Vuorosuunnittelun Suunnittelunäkymässä tai Työaika-näkymässä ennen kuin vähintään yksi kalenterijakso on määritelty ja julkaistu.
## Vuorokalenterin suunnittelu jaksopohjaisesti
Kalenterit suunnitellaan ja julkaistaan tietyille ajanjaksoille etukäteen. Näitä ajanjaksoja kutsutaan Vuorokalenterijaksoiksi. Yleisesti ottaen, TES-vaatimukset tai suunnittelujakso määrittelevät tämän jakson. Useimmiten jakso on 6-12 kuukautta.
Kun olet lisännyt jakson ja sen perustiedot kalenteriin, määrittele vuoro- ja/tai poissaolotyypit, valitse ne vuororyhmät, joille jakso on tarkoitettu, heidän vuoromallinsa ja mahdolliset siirtymät.
Tässä vaiheessa Vuorokalenterijakson kalenteri tulee näkyviin näkymän alaosaan. Tämän jälkeen kalenteriin on mahdollista tehdä suoraan muokkauksia, (joita kutsutaan Vuoropoikkeamiksi) ja huomautuksia ennen julkaisemista. Lisätietoa näiden tekemisestä löytyy alta.
### Vuorotyyppien määrittely
Erityyppiset suunnitellut tapahtumat määritellään kullekin vuorokalenterijaksolle erikseen. Jokaiselle suunnitellulle tapahtumalle määritellään lyhenne, jolla tapahtumaan viitataan Vuorosuunnittelussa ja Työaika-näkymässä. Tämä helpottaa niiden löytämistä ja suunnittelua.
Ennalta määritelty vuorotyyppi _Ei vuoroa (-)_ löytyy jokaisesta Vuorokalenterijaksosta valmiina ja sitä tulee käyttää lepopäivien osalta.
Esimerkiksi, lyhenne A, voi tarkoittaa aamuvuoroa (jonka nimi on "Aamu"), sen alkamisajankohta on 06:00, loppumisajankohta 14:00 ja lisätiedoissa määritellään aamuvuoron tehtävät.
Oletetut lounasvähennykset suunnitelluille tapahtumille (eli vuorotyypeille) määräytyvät seuraavien asetusten perusteella: 
  * Koko ympäristöä koskeva asetus: Työsuhde > Hallinta > Asetukset > Vuorosuunnittelu.
  * Tietty Vuorokalenteri: Vuorosuunnittelu > Toimipisteet > Valitse suunnittelutaso > Suunnittelutason asetukset > Oletetun ruokatauon vähennys


### Ryhmien, vuorokierron ja vuorokierron siirtymien lisääminen
Vuororyhmiin lisätään sellaiset käyttäjät, joille on suunniteltu vuoroja kyseiselle ajanjaksolle. Kun ryhmiin on lisätty käyttäjät, määritellään ryhmälle toistuva vuorokierto perustuen vuorotyyppeihin, jotka määriteltiin edellisessä kohdassa. Vuorokierron määrittelyssä käytetään erotinmerkkinä välilyöntejä.
Vuorokierron siirtymä määrittää mistä kohtaa vuorokiertoa ryhmän vuorokierto alkaa. Arvo nolla aloittaa vuorokierron ensimmäisestä vuorosta. Positiiviset arvot siirtävät kierron ensimmäistä vuoroa myöhemmäksi ja negatiiviset arvot aiemmaksi.
Esimerkiksi kun haluat käyttää vuorokiertoa A A A - - Y - V - - - kaikille viidelle ryhmälle, siten että seuraava ryhmä aloittaa kierron aina kaksi päivää jäljessä, voit määrittää siirtymät näin:
  * **Ryhmä, siirtymä = muodostuva vuorokierto jakson ensimmäisestä päivästä alkaen**
  * Ryhmä 1, siirtymä 0 = A A A - - Y - V - - -
  * Ryhmä 2, siirtymä 2 = - - A A A - - Y - V -
  * Ryhmä 3, siirtymä 4 = V - - - A A A - - Y -
  * Ryhmä 4, siirtymä 6 = Y - V - - - A A A - -
  * Ryhmä 5, siirtymä 8 = - - Y - V - - - A A A


### Vuoropoikkeamat
Vuoropoikkeamat ovat vuororyhmälle tai työntekijälle tehtäviä muutoksia, mitkä poikkeavat tavallisista työvuoroista ja lomakalenterista. Ne voidaan tehdä Vuorokalenterijakson kalenterissa tai Vuorosuunnittelun Suunnittelunäkymässä. Poikkeamat korostetaan violetilla, jotta sekä työntekijät että suunnittelijat huomaavat ne helposti.
Esimerkkejä poikkeamien käytöstä:
  * **Suunniteltu huoltokatko** \- On tiedossa tarvittava huoltokatko tuotantolinjalla, mikä koskee yhtä tai useampaa vuororyhmää. Tässä tilanteessa suunniteltuja päiviä muokataan tarvittavien ryhmien osalta, ja lisätään heille esimerkiksi koulutus normaalin vuoron sijasta. Tämä näkyy vuoropoikkeamana näille ryhmille.
  * **Odotettu lisäys tilauksissa** \- Suunnitellun myynnin ja markkinoinnin takia on odotettavissa, että tarvitaan lisää työntekijöitä töihin tiettynä päivänä. Vuororyhmän, jolla normaalisti olisi lepopäivä, tietoja muokataan niin, että heillä onkin työpäivä. Lepopäivä siirretään myöhemmäksi.


### Suunnitteluhuomautukset
Vaikka suunnitelluissa vuoroissa ja lomamerkinnöissä voi olla lisätietoa, joskus on tarpeen antaa lisää informaatiota koskien suunnitelmaa tai tiettyä päivää. Näissä tapauksissa voidaan lisätä suunnitteluhuomautus Vuorokalenterijakson kalenterissa kaikille tai yksittäisille ryhmille.
Esimerkiksi, suunnitteluhuomautus voi olla hyödyllinen, kun halutaan selittää, miksi tietyllä päivällä on vuoropoikkeamia esim. huoltokatkon takia.
## Ryhmäjäsenyyksien hallinnointi
Kun Vuorokalenteri on luotu ja vähintään yksi jakso on julkaistu, tulee varmistaa, että oikeat työntekijät näkevät suunnitellut tapahtumat ja vuorot.
Vuororyhmän jäsenyyksiä voidaan hallinnoida vasta, kun vähintään yksi jakso, jossa kyseistä ryhmää käytetään, on julkaistu.
### Hallinnointi massatoiminnoilla (Käyttäen henkilötuontia)
Jos ollaan määrittelemässä uutta työvuoro- tai lomakalenteria, tai on tarve suurelle määrälle muutoksia kalenteria seuraavien työntekijöiden suhteen, on suositeltavaa käyttää Excel-tuontia ryhmäjäsenyyksien uudelleenmäärittelyssä. Vaihtoehtoisesti näitä muutoksia voidaan tehdä käyttöliittymän kautta, jonka kuvaus löytyy tästä samasta artikkelista.
  1. Luo tuontitiedosto 
     * Vaihtoehto 1: Ota käyttäjälistaus tiedostoon täällä: Työsuhde > Henkilöt > Vie sisäänluettavaan Exceliin. **Huomaa** : Kun käytetään sisäänluettavaa Excel-tiedostoa, tulee ottaa kaikki sarakkeet näkyviin.
     * Vaihtoehto 2: Luo manuaalisesti Excel-tiedosto, jossa on tarvitsemasi käyttäjät ja sarakkeet
  2. Sisällytä tiedostoon vain vaadittavat sarakkeet henkilön tunnistamiseen, vuororyhmätieto ja tieto ryhmän jäsenyyden alkamisesta. Esim. Henkilönumero, Vuororyhmä, Lomavuororyhmä ja Voimassa alkaen.
  3. Varmista, että oikea Voimassa alkaen -päivämäärä on määritetty, jotta aiempi tieto vuororyhmästä säilyy.
  4. Tuo tiedosto täällä: Työsuhde > Henkilöt > Tuo henkilöitä


Ohje henkilötietojen tuomiseen löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360018767498-Henkil%C3%B6iden-manuaalinen-tuonti>).
### Hallinnointi Vuorokalenterit-näkymässä & ryhmättömien käyttäjien haku
Kun tehdään pieniä muutoksia jäsenyyksiin tai sinulla ei ole oikeuksia tuoda henkilötietoja, jäsenyyksiä voidaan hallinnoida käyttöliittymän kautta. Siirry näkymään Vuorokalenteri > valitse kalenteri > Jäsenet. Tässä näkymässä näet myös yksikön jäsenet, joita sinulla on oikeus hallinnoida ja joilla ei ole vielä jäsenyyttä missään Vuororyhmässä.
Käytä hakukenttää etsiäkseni käyttäjää tai selaa ja laajenna Vuororyhmät-näkymä, jotta voit muokata olemassaolevaa jäsenyyttä.
Kun lisäät jäseniä tai muokkaat jäsenyyttä, on suositeltavaa, että jäsenyydelle asetetaa alkamispäivämäärä, jotta muutos ei vaikuta käyttäjän työaikaan, kalenteriin ja laskentoihin.
## Julkaisu
Kun vuorokalenteri on määritetty ja mahdolliset vuoropoikkeamat lisätty, voit julkaista vuorokalenterijakson. Kun jakso on julkaistu, suunnitellut tapahtumat, poikkeamat ja suunnitteluhuomiot näkyvät heti Vuorosuunnittelun Suunnittelunäkymässä ja vuororyhmiin liitettyjen henkilöiden työaikakalenterissa työpöytä- sekä mobiiliversiossa.
Kun julkaisu on tehty, voit hallinnoida, seurata ja reagoida mahdollisiin muutostarpeisiin. Tutustu myös "Vuorokalenterin päivittäinen käyttö ja seuranta" -artikkeliin [täällä](<https://support.nepton.com/hc/fi/articles/12063496680349>)
