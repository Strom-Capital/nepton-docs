---
id: 360002489317
title: Henkilötietojen ajastettu tuonti
url: https://support.nepton.com/hc/fi/articles/360002489317-Henkil%C3%B6tietojen-ajastettu-tuonti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötiedot
section_id: 360001070377
section_path:
- Liittymät
- Henkilötiedot
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-09-21T11:19:04Z'
edited_at: '2026-09-21T10:58:57Z'
---

# Henkilötietojen ajastettu tuonti

Henkilöitä voidaan lisätä palveluun manuaalisesti [yksitellen ](<https://support.nepton.com/hc/articles/360002427618>)tai [massana](<https://support.nepton.com/hc/fi/articles/360018767498>), tai ajastetulla henkilötietojen tuonnilla. Tässä ohjeessa kerrotaan, miten henkilöitä voi lisätä palveluun ajastetulla henkilöiden tuonnilla. Määritys tehdään valikossa **Työsuhde > Hallinta > Ajastetut tehtävät**. Lisätäksesi automaattisen tuonnin määritykset valitse **Lisää tehtävä**.  

  
Nyt pääset määrittelemään uuden tehtävän. Alla on listattu kenttien kuvaukset. Täytettävien kenttien valikoima riippuu valitusta tehtävätyypistä (Tuo henkilöitä), tiedoston tyypistä ja henkilötuonnin tyypistä. 
### Yleiset tiedot
**Tyyppi:** Tuo henkilöitä  
**Nimi:** Valitse haluamasi nimi siirrolle, esimerkiksi "Henkilötuonti Mepcosta". Tällä tekstillä ei ole teknisesti vaikutusta toimintaan. Suosittelemme aina lisäämään aikaleiman tuontitiedoston nimeen, jotta mahdollisissa tuontien katkoksissa tiedostot voidaan ajaa jälkikäteen sisään oikeassa järjestyksessä.  
**Kuvaus:** Valitse haluamasi kuvaus siirrolle, esimerkiksi "Henkilötuonti Mepcosta". Tällä tekstillä ei ole teknisesti vaikutusta toimintaan, eikä se näy muualla kuin siirtojen hallinnassa.  
**Suorita ylläpitäjänä:** Tässä kentässä valitaan, millä tunnuksella siirto tehdään ja millä tunnuksella se näkyy listauksessa. Tähän valitun käyttäjän tulee olla ylläpitäjä. Suosituksena on, että perustetaan tätä varten kokonaan uusi henkilö (esimerkiksi "Mepco admin"). Tähän ei suositella valittavan todellista käyttäjää, koska se voi aiheuttaa sekaannuksia siinä, onko kyseessä oikeasti manuaalinen vai automaattinen siirto.
### Henkilötiedot
**Henkilötuonnin tyyppi:** Valitaan siirrettävän tiedon rakenne. Henkilötuonnin tyyppi määrittelee miten tuotava aineisto haetaan, sekä minkälaista aineiston rakennetta ja sisältöä tuetaan. Katso lisätiedot tuetuista henkilötuontityypeistä [täältä](<https://support.nepton.com/hc/fi/sections/7976634441629-J%C3%A4rjestelm%C3%A4kohtaiset-henkil%C3%B6tietojen-tuonnit>).
**Merkistökoodaus:** Valitaan saapuvan aineiston merkistökoodaus. Oleellista skandinaavisten merkkien toimivuuden osalta.
**Tiedostomuoto:** Valitaan tuotavan aineiston tyyppi. Tuetut tiedostomuodot ovat [CSV](<https://fi.wikipedia.org/wiki/CSV>), [XML](<https://fi.wikipedia.org/wiki/XML>), [Excel](<https://fi.wikipedia.org/wiki/Microsoft_Excel>) (XLS tai XLSX) ja [JSON](<https://fi.wikipedia.org/wiki/JSON>).
**Henkilön tunniste:** Henkilön tunniste tarkoittaa sitä henkilötietoa, jonka perusteella etsitään löytyykö tuotava henkilö jo olemassa olevista henkilöistä. Jos henkilö samalla henkilön tunnisteella löytyy, päivitetään tämän henkilön tietoja tuotavalla tiedolla.
Kun käytetään arvoa "Oletus", käytetään ensimmäistä näistä henkilötiedoista, jolle löytyy arvo tuotavista henkilötiedoista: Nepton-tunniste, Ulkoinen tunniste 1, Käyttäjätunnus, Henkilönumero.
Vinkki: Kun valitset muun arvon kuin "Oletus", voit päivittää tuotavan aineiston avulla näitä tunnisteita, "Ulkoinen tunniste 1", "Käyttäjätunnus" ja "Henkilönumero", lukuunottamatta tunnistetta jonka olet valinnut henkilön tunnisteeksi.
**Otsikkorivi:** Valinnainen asetus on käytettävissä CSV-tiedostojen kanssa. Tarkista, onko saapuvan aineiston ensimmäisellä rivillä lueteltu niiden henkilötietokenttien nimet, joihin tiedot tuodaan. Jos aineistossa on lueteltu nämä tiedot, Otsikkorivi-asetus on jätettävä tyhjäksi. Jos kenttien nimiä ei aineistossa ole, Otsikkorivi-asetuksessa on lueteltava henkilötietokenttien nimet piippumerkeillä (|) eroteltuina. Piippumerkillä erotettuina arvoina voidaan käyttää kaikkia [henkilötuonnin kenttiä](<https://support.nepton.com/hc/fi/articles/360015933397>). Yksittäinen kenttä voidaan jättää huomioimatta tuonnissa asettamalla kentän nimeksi suuraakkosin **IGNORE.**
**Tuotavat kentät:** Valinnainen asetus on käytettävissä Excel-tiedostojen kanssa. Jos Excel-tiedostossa on sarakkeita, joiden tietoja ei pidä tuoda, Tuotavat kentät -asetuksella voidaan luetella piippumerkeillä (|) eroteltuina vain niiden henkilötietokenttien nimet, jotka halutaan sisällyttää tuontiin. Näin erikseen luettelemattomat tiedot jätetään pois tuonnista. Piippumerkillä erotettuina arvoina voidaan käyttää kaikkia [henkilötuonnin kenttiä](<https://support.nepton.com/hc/fi/articles/360015933397>). Jos kaikkien sarakkeiden tiedot halutaan tuoda, Tuotavat kentät -asetus on jätettävä tyhjäksi.
### Tiedostopalvelin (SFTP)
Tiedostopalvelinasetukset on määriteltävä niille henkilötuonnin tyypeille, joissa Nepton hakee tiedot SFTP-siirrolla tiedostopalvelimelta (tällä hetkellä kaikille muille henkilötuonnin tyypeille Sympa HR Integraatio API -tyyppiä lukuunottamatta).  
  
**Palvelimen osoite:** Merkitään palvelimen osoite, josta aineisto noudetaan.  
**Portti:** Merkitään käytettävä portti.  
**Käyttäjätunnus:** Merkitään käytettävä käyttäjätunnus, jolla pääsee noutamaan aineiston SFTP-palvelimelta.  
**Salasana:** Merkitään käytettävä salasana, jolla pääsee noutamaan aineiston SFTP-palvelimelta. Huomaa, että HTML-koodi (esim. **<** tekstin edellä) ei ole sallittua salasanakentässä. Jos kenttä on tyhjä, salasanaa ei ole asetettu ja salasanan voi kirjoittaa kenttään. Jos kentässä lukee: "Salasana on asetettu", palvelimen salasana on tallennettu ja voit vaihtaa salasanaa valitsemalla valikosta "Vaihda salasana". Muutokset salasanaan tallennetaan aina Tallenna-painikkeella.  
**Työkansio:** Jos SFTP-kansiossa on tietty kansio, josta aineisto noudetaan merkitään sen nimi tähän (kuvassa merkitty 1). Valinnainen kenttä.  
**Arkistointikansio:** Onnistuneesti käsitellyt tiedostot siirretään tähän kansioon SFTP-palvelimella. Nepton ei poista tiedostoja arkistointikansiosta. Arkistointikansio voi olla myös esim. sama kansio, josta tiedostoja haetaan, jos käytössä on asiakkaan oma SFTP-palvelin ja jos käsiteltyjen tiedostojen poisto voidaan toteuttaa niin, että kansiossa on ajon aikana vain käsittelemättömiä tiedostoja. Käytettävällä käyttäjätunnuksella on oltava sekä luku- että kirjoitusoikeudet sekä työkansioon että arkistointikansioon.  
**Tiedostonimen suodatin:** Voidaan määrittää, että vain ne tiedostot, joissa on tässä merkitty sana siirretään. Esimerkiksi vain tiedostot, joissa on sana "henkilotiedot". Huomaathan, että suodatin kirjoitetaan ilman "-merkkejä (kuvassa merkitty 2). Muodostettavan aineiston tulee tiedostonimessä sisältää luontihetken aikaleima. Tällä varmistetaan, että aiempaa tiedostoa tietoa ei ylikirjoiteta esimerkiksi sellaisessa tilanteessa, jossa aineiston lukua ei ole suoritettu ajastuksen mukaisena.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360014402298)
### REST-rajapinta
REST-rajapinta-asetukset on määriteltävä niille henkilötuonnin tyypeille, joissa Nepton hakee tiedot http-protokollalla API-rajapinnan kautta (tällä hetkellä henkilötuonnin tyypille Sympa HR Integraatio API).
**REST API -osoite:** Kutsuttavan REST API -palvelun sovellusliittymän URL, johon voi osoitteen perään lisätä tarvittaessa URL-parametrejä.
**Autentikaatiotyyppi:** Aseta autentikaatio REST API -palvelun vaatimusten mukaisesti:
  * **Ei autentikointia:** Palvelu ei vaadi minkäänlaista tunnistautumista pääsyä varten.
  * **Perus-HTTP-autentikointi:** Palvelu vaatii tavanomaisen tunnistautumisen käyttäjätunnuksella ja salasanalla. Aseta käyttäjätunnus ja salasana REST APIlle **Parametri** -asetuksissa käyttäen kenttiä "username" ja "password" paremetrin **Nimi** -asetuksiin ja niille sopivia arvoja **Arvo-** asetuksiin.
  * **OAuth 2.0 (perus-HTTP-autentikointi):** Palvelu vaatii erillisen OAuth 2.0 -protokollaa käyttävän valtuutuspalvelimen käyttöä. Aseta vaadittu **valtuutuspalvelimen osoitteen** arvo. Aseta  _valtuutuspalvelimen_ käyttäjätunnus ja salasana **Parametri** -asetuksissa käyttäen kenttiä "username" ja "password" parametrin **Nimi** -asetuksiin ja niille sopivia arvoja **Arvo-** asetuksiin.
  * **Tunnussanavaltuutus:** Palveluun tunnistaudutaan käyttäen erityistä avainta. Aseta vaadittu avain **parametrin** asetuksiin: **Nimi** -kenttään "apikey" ja avaimen arvo **Arvo** -kenttään.


**Valtuutuspalvelimen osoite:** Mikäli valitsit autentikaatiotyypiksi "OAuth 2.0 (perus-HTTP-autentikointi)", lisää tähän autentikointiserverin osoite, johon lähetetään tunnistautumiskutsu.
**Parametri 1 - Parametri 4:** Ks. yllä parametrit, joita autentikaatio vaatii. Näihin kenttiin voi lisätä tarvittaessa rajapintakutsun mukana HTTP-otsikkotiedoissa lähetettäviä parametrejä. Kirjoita parametrin nimi vasempaan ja arvo oikeaan kenttään.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21082413188253)
### Virheelliset asetukset
Jos vaihdat (ajastetun tehtävän) tyyppiä, henkilötuonnin tyyppiä, tiedoston tyyppiä tai autentikaatiotyyppiä ja olet jo täyttänyt kenttiä, joita ei uudelle valinnalle ole mahdollista tallentaa, saattaa lomakkeelle tulla näkyviin kohta "Virheelliset asetukset". Tarkista, että olet tehnyt tyyppivalinnat oikein ja joko korjaa tyyppivalinnat tai tyhjennä virheelliset kentät.
![mceclip3.png](https://support.nepton.com/hc/article_attachments/360012841777)
### Ajastus
Näissä kentissä määritellään, milloin aineisto siirretään ja miten ajastusta toistetaan. Suosittelemme ajastuksen ajastamista yöajalle, kuitenkin välttäen palvelun säännöllisten huoltotoimenpiteiden ajankohtia. Katso huoltotoimenpiteiden ajankohdat [palvelun tila](<https://support.nepton.com/hc/articles/360006554777>)-sivun lopusta.
**Suorita:** Näissä kentissä määritellään milloin tehtävä ajastetaan suoritettavaksi.
  * **Vain manuaalisesti:** Jos et halua käyttää tehtävän automaattista ajastusta, valitse tämä vaihtoehto. Tehtävä suoritetaan vain, jos valitset **Suorita nyt** -painikkeen tehtävän tallennuksen jälkeen.
  * **Kerran** : Tehtävä ajastetaan suoritettavaksi vain yhden kerran. Valitse suoritushetken päiväys ja kellonaika **Suoritusaika** -kentässä.
  * **Kerran tunnissa:** Tehtävä suoritetaan joka tunti sillä minuutilla, joka on asetettu **Tällä minuutilla** -kentässä. Esim. jos "tällä minuutilla" on 30, tehtävä suoritetaan 0:30, 1:30, 2:30 jne.
  * **Päivittäin:** Tehtävä suoritetaan joka päivä sinä kellonaikana, joka on asetettu **Kellonaikana** -kenttään.
  * **Viikoittain:** Tehtävä suoritetaan vain niinä viikonpäivinä, jotka on määritelty **Viikonpäivinä** -kentässä. Aseta kellonaika suoritukselle **Kellonaikana** -kenttään.
  * **Kuukausittain:** Tehtävä suoritetaan **Kuukausina-** ja **Päivinä** -kentissä valittuina kuukausina ja päivinä. **Päivinä** -kentässä on valittavissa päivät numeron mukaan tai kuukauden viimeinen päivä. Aseta **kellonaika** -kenttään suoritusajankohta suorituspäivänä. 


**Käytössä:** Valitse säännöllisesti suoritettaviksi ajastetuille tehtäville aikaväli, jolla ajastus on käytössä. Tehtävä suoritetaan muiden asetusten mukaisesti, mutta ei kuitenkaan ennen **Alkaen** -kentän päiväystä ja kellonaikaa eikä **Päättyen** -kentän päiväyksen ja kellonajan jälkeen. **Alkaen** -kentän oletusarvona tehtävä on heti käytössä. **Päättyen** -kenttä on valinnainen.
Kun määritykset on tehty, valitse **Tallenna**. Palvelu ilmoittaa tallennuksen onnistuneen, jos kaikki kentät on täytetty asianmukaisesti. Huomaa, että jos yhdestäkin kentästä raportoidaan virheitä, mitään muutettuja tietoja ei tallenneta ennen kuin virheet on korjattu.
Kun tallennus on onnistunut, voit testata siirtoa valitsemalla **Suorita nyt**.
Uusi luotu ajastettu tehtävä näkyy nyt myös päävalikossa.
Huomioithan, että ajastetut tuonnit voivat näkyä palvelulokissa muutaman minuutin viiveellä. Vaikka tuonti käynnistyy asetettuun aikaan (esimerkiksi klo 04:00), itse käsittely ja lokimerkinnän päivittyminen voi kestää hetken. Tämän vuoksi tuonti saattaa näkyä käyttöliittymässä esimerkiksi klo 04:01 tai 04:02. Tämä on normaalia toimintaa. Jos on tärkeää, että ajastus näkyy käyttöliittymässä mahdollisimman lähellä tiettyä kellonaikaa, ajastuksen voi halutessaan asettaa hieman aiemmaksi (esimerkiksi klo 03:58 tai 03:59).
