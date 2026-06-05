---
id: 360002560698
title: Vuosiloman asetukset
url: https://support.nepton.com/hc/fi/articles/360002560698-Vuosiloman-asetukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Esimerkkejä asetusryhmien perustamiseksi
section_id: 360001483898
section_path:
- Työajan laskenta ja hallinta
- Asetusryhmät
- Esimerkkejä asetusryhmien perustamiseksi
labels:
- lomakalenteri
- lomat
- lomalaskenta
- vuosilomalaskenta
- loma
- lomamäärä
promoted: false
updated_at: '2026-02-16T11:10:16Z'
edited_at: '2026-02-16T11:10:15Z'
---

# Vuosiloman asetukset

Vuosiloman laskenta otetaan käyttöön alla kuvatulla tavalla.
## Määritä säännöt lomaoikeuden ansaitsemiseksi
Vuosiloma-ansainnan määritykset voidaan määrittää joko **Työyhteisö** -tasolla tai **Asetusryhmät** -tasolla.
Asetukset löytyvät valitsemalla **Työaika >** **Hallinta > Työyhteisön/Asetusryhmän asetukset > Työtunnit > Vuosiloma.**
## Vuosiloman ansainnan aloituspäivä
Vuosiloman ansainta alkaa päivästä, jolloin henkilölle on kirjattu ensimmäinen työn kaltainen tapahtuma ja henkilö ansaitsee vuosilomaa asetuksien mukaan.
Huomioithan, että oletettu tapahtuma tyhjänä työpäivänä ei aloita vuosiloman ansainnan laskentaa.
## Vuosiloman asetukset
Alla on esitetty kaikki vuosiloman asetukset ja niiden käyttäytyminen. 
![](https://support.nepton.com/hc/article_attachments/19205465321373)
### Kertymä käytössä
Asetuksella vuosilomakertymän voi ottaa käyttöön tai pois käytöstä.
  * "Ei asetettu" - Olemassa olevien asiakkaiden oletuksena on "Ei asetettu", joka toimii samalla tavalla kuin "Kyllä".
  * "Kyllä" - Vuosilomakertymä on käytössä.
  * "Ei" - Vuosilomakertymä ei ole käytössä. Vuosilomalaskentaa ei enää suoriteta, eikä vuosilomakertymää näytetä vuosilomapyynnöissä tai tapahtumapyyntöjen hyväksymisnäkymässä. 


Asetusta voidaan hyödyntää esimerkiksi tilanteissa, joissa vuosilomapäivien kertymää hallitaan jossain ulkoisessa järjestelmässä.
### Piilota vuosiloman kirjauksen ohjeistus tapahtuman muokkausikkunassa
Asetuksella ohjataan näytetäänkö kirjaajalle ohje, jossa muistutetaan kirjaamaan myös lauantait lomapäiväksi. 
### Ansaitun vuosiloma-ajan laskenta
Asetuksilla ohjataan kuinka monta vuosilomapäivää ansaitaan perustuen joko tehtyihin työtunteihin tai työpäivien määrään.
Tuntipalkkaiselle, jotka säännöllisesti tekevät alle 14 päivää kuukaudessa töitä (tarvittaessa töihin kutsuttavat), määritetään asetus "Jos kuukaudessa alle xx tuntia niin ansaitaan vuosilomaa 0 päivää, muuten ansaitaan lomaa 2,5 päivää"
Kuukausipalkkaisten työntekijöiden vuosiloman ansainta määritetään muodostuvan tehtyjen työpäivien perusteella. Kuukausipalkkaiselle asetetaan sääntö muodossa 'jos kuukaudessa alle 14 työpäivää, ansaitaan vuosilomaa 0 päivää, muuten ansaitaan lomaa 2,5 päivää.
Kummassakin tilanteessa poikkeussäännöllä voidaan määritellä ne tilanteet, jolloin henkilö ansaitsee lomasaldoa 2 päivää kuukaudessa. Asetukseen '... muulloin ansaitaan vuosilomaa' määritetään ansaittavaksi seuraavan kuvan mukaisesti. Tällöin henkilö ansaitsee 2,5 päivää vuosilomaa jollei poikkeussääntö ole voimassa jolloin ansaitaan 2 päivää. Poikkeussääntö on voimassa jos työsuhde on kestänyt alle 12kk lomakauden alkamisesta.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4404610234257)
[Täältä](<https://support.nepton.com/hc/fi/articles/360002560677>) löydät lisätietoja poikkeusasetuksen määrittelyistä.
## Käyttämisen säännöt
### Päivät, jotka lasketaan vapaaksi/lomaksi
Asetuksella ohjataan mitkä päivät pitkistä lomista kuluttavat vuosilomaa. Vaihtoehdot ovat 'maanantaista perjantaihin', 'maanantaista lauantaihin', 'maanantaista sunnuntaihin'. Mikäli arvoa ei ole asetettu eikä arvo periydy ylemmiltä ryhmiltä niin käytetään arvoa 'maanantaista lauantaihin'.
Huomioithan, että esimerkiksi pääsiäislauantaita ei vuosilomalain 4§ mukaan lasketa vuosilomapäiväksi.
### Vain päivät, joilla on työvelvoite, lasketaan vapaaksi/lomaksi
Asetuksella ohjataan, että vain ne päivät luetaan vuosilomiksi, joille on asetettu työpäivän pituus.
### Vapaa/loma jätetään huomiotta päivinä, joilla on työtä / juhlapyhänä
Jos asetuksiin on määritetty 'kyllä', ei merkattua vuosilomaa lasketa vuosilomapäiväksi jos päivälle on kirjattu työtä / kyseinen päivä on juhlapyhä. 
### Korvaus vapaa/lomapäivänä
Kuinka lasketaan kulutettavan vuosiloman määrä, kun henkilö on vuosilomalla.
  *     * "Ei asetettu" - Arvo peritään ylemmältä tasolta, jos se on asetettu. Jos arvoa ei ole asetettu ylemmällä tasolla, vuosilomaa ei kulu.
    * "Käytetty velvoitteen määrä" - Vuosilomaa kuluu henkilön työpäivän työvelvoitteen verran kultakin päivältä
    * "Kiinteä määrä / päivä" - Vuosilomaa kuluu kiinteä määrä päiväkohtaisesti kahden seuraavan asetuksen mukaisesti (Määrä päivinä joilla on/ei ole työpäivän pituus). Kulutettavan vuosiloman määrä lasketaan automaattisesti "Määrä päivinä joilla on/ei ole työpäivän pituus" -asetuksen mukaisesti, jos se on asetettu. Jos sitä ei ole asetettu, määrä lasketaan henkilön asetusryhmässä määritetyn työpäivän pituudesta. Jos työpäivän pituutta ei ole määritetty, määrä lasketaan olevan viidesosa henkilön asetusryhmässä määritetyn työviikon pituudesta.
    * "Työpäivän pituus" - Vuosilomaa kuluu perustuen henkilön työpäivän pituuteen kultakin päivältä.
    * "Viidesosa työviikon pituudesta" - Vuosilomaa kuluu henkilön työviikon pituuden / työvelvoitteen määrän viidesosa päivää kohden.
    * "Työpäivän enimmäispituus" - Vuosilomaa kuluu henkilön työpäivän enimmäispituuden verran kultakin päivältä.
    * "Perustuen vanhoihin vuosilomasääntöihin" - Asetus laskee vuosiloman arvoksi 1/5 työviikon pituudesta.  
  
Jos puolestaan työpäivän ja työviikon pituutta ei ole asetettu eikä siksi kulutetettavan vuosiloman määrää voida laskea, oletusarvona käytetään 8 tuntia. Tälläinen tilanne voi esiintyä tilanteessa, jossa henkilön Työajan asetusryhmä ja työajan laskenta on toteutettu tarkoituksellisesti ilman vakioituja työvelvoitteita.
Yllä listatut asetukset määrittelevät tavan, jolla vuosiloma kuluu. Niillä määritellään  
myös, kuinka vuosilomapäivät lyhentävät työviikon pituutta. Vuosilomapäivät eivät  
kuitenkaan lyhennä työviikon pituutta niinä päivinä, joina työvelvoitteeksi on  
asetettu nolla tuntia. Mikäli vuosilomapäivän halutaan lyhentävän työviikkoa  
tällaisina päivinä, tulee kyseiselle päivälle tehdä [poikkeusasetus](<https://support.nepton.com/hc/fi/articles/360002560677>) työpäivän pituuteen.


### Määrä päivinä joilla on työpäivän pituus
Koskee tilannetta, jolloin asetukseen "Korvaus vapaa/lomapäivänä" on määriteltynä "Kiinteä määrä/päivä". Kiinteä määrä, joka vuosilomaa kuluu vuosilomapäiviltä, joilla olisi työpäivän pituus / työvelvoite. 
 _Huom: Tätä asetusta ei huomioida, jos arvo "Perustuen työpäivän pituuteen" on valittu._
###  Määrä päivinä joilla ei ole työpäivän pituutta
Koskee tilannetta, jolloin asetukseen "Korvaus vapaa/lomapäivänä" on määriteltynä "Kiinteä määrä/päivä" tai "Työpäivän pituus". Kiinteä määrä, joka vuosilomaa kuluu vuosilomapäiviltä, joilla ei ole työvelvoitetta / työpäivän pituus on 0.
Jos korvaus vapaa/lomapäivänä perustuu vanhoihin vuosilomasääntöihin, ja määrää päivinä joilla ei ole työpäivän pituutta ei ole asetettu, järjestelmä yrittää päätellä määrän edellispäivien työpäivän pituudesta. Jos määrän päätteleminen edellispäivistä ei onnistu, käytetään oletuksena 8 tuntia.
### Viikkotyöaikaan vaikuttava määrä vapaa/lomapäivänä
Asetuksella voidaan määrittää, miten vuosiloma täyttää työviikkoa. Oletuksena yksi vuosilomapäivä voi täyttää työviikkoa vain 8h ajan (Jos TES-osion asetuksiin on määritelty, että vuosiloma lasketaan mukaan työviikkoon, tämä tarkoittaa siis max. 8h). Tällä asetuksella voidaan kuitenkin määrittää erilaisia vaikuttavia määriä. 
Voidaan sanoa, että vuosiloma täyttää työviikkoa **kiinteän määrän** verran, jolloin asetukseen valitaan "kiinteä määrä". Tällöin myös seuraava asetus, "Määrä päivinä, joilla on työpäivän pituus" tulee määrittää halutulla kiinteällä määrällä. Esimerkiksi jos tehdään 12h työvuoroja, ja vuosiloman halutaan vaikuttaa viikkotyöaikaan tällä kestolla, määriteltäisiin asetukseen näin:
![](https://support.nepton.com/hc/article_attachments/33376818267549)
Ilman tätä asetusta viikkotyöajan ollessa 36h ja vuorojen pituuden 12h, viikolla jolle on suunniteltu 3 x 12h vuoroa ja näiden velvoite täytetty vuosilomalla, jäisi viikkotyö vajaaksi, sillä yksi vuosilomapäivä täyttäisi vain yhden viidesosan työviikon määrästä:
![](https://support.nepton.com/hc/article_attachments/33376825848477)
Jos asetusryhmässä on päällä automaattinen miinustus vajaasta työvelvoitteesta työviikon päätteeksi, miinustetaan sunnuntaina 14h24min sillä vuosilomaa lasketaan työviikkoon sen verran, mitä asetukseen "Korvaus vapaa/lomapäivänä" on määritelty, maksimissaan kuitenkin 8h. Tässä tapauksessa vuosiloma täyttää työviikkoa siis päivittäin 7h12min asetuksen "korvaus vapaa/lomapäivinä" mukaan.
Jos vuosilomalle asetetaan, että se kattaa 12h työviikosta, häviää tämä lainaus, sillä kirjattu vuosiloma kattaa 3 x 12 = 36h:
![](https://support.nepton.com/hc/article_attachments/33376825849117)
Voidaan myös sanoa, että vuosiloma lasketaan työviikkoon perustuen "**Vapaa/lomapäivän palkallinen kesto** " määriteltyyn arvoon. Tällöin asetuksen "Korvaus vapaa/lomapäivänä" valittu määritys vaikuttaa siihen, miten vuosiloma lasketaan työviikkoon mukaan. Esimerkiksi, jos asetukseen "Korvaus vapaa/lomapäivänä" on asetettu yksi viidesosa työviikosta, laskettaisiin myös vuosilomasta yhdeltä päivältä viikkotyön viidesosa viikkotyöaikaan.
![](https://support.nepton.com/hc/article_attachments/33376825850141)
Vuosiloman vaikutus viikkotyöhön on tärkeä esimerkiksi tilanteissa, joissa työn lopussa miinustetaan automaattisesti viikon velvoite, joka ei ole täyttynyt viikolla, tai tilanteessa, jossa alkuviikosta on ollut vuosilomaa ja loppuviikosta tehdään ylitöitä.
### Tapahtumatyypit, joista ansaitaan vuosilomapäiviä
Ne tapahtumatyypit, jotka luetaan vuosilomaa kerryttäväksi. Ympäristöön kustomoidut tapahtumatyypit esitetään tähti - etuliitteellä.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4417861374225)
## Varmista vuosilomasääntöjen voimassaolo takautuvasti
Mikäli vuosiloma-asetusten muutoksia on tehty takautuvasti, tulee henkilöiden laskenta päivittää kalenterista. Laskennan päivittämisen jälkeen oikea lomaoikeus on esillä vuosiloman raporteilla.
