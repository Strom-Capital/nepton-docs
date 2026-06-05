---
id: 360002559837
title: Työajan lyhennysvapaan asetusten määrittely
url: https://support.nepton.com/hc/fi/articles/360002559837-Ty%C3%B6ajan-lyhennysvapaan-asetusten-m%C3%A4%C3%A4rittely
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
- työajanlyhennys
- työajan lyhennys
- työajanlyhennysvapaa
- pekkanen
- pekkaset
- lisävapaapäivä
- työlyhennysvapaa
- tasaamispäivä
promoted: false
updated_at: '2025-06-05T11:05:32Z'
edited_at: '2025-06-03T13:10:03Z'
---

# Työajan lyhennysvapaan asetusten määrittely

## Yleistä työajan lyhennysvapaasta
Palveluun voidaan aktivoida työajan lyhennysvapaan laskenta. Yleensä työajan lyhennysvapaata ansaitaan, mikäli työehtosopimuksen mukainen säännöllinen työaika on sama kuin työaikalain mukainen säännöllinen työaika, kahdeksan tuntia vuorokaudessa tai 40 tuntia viikossa. Alla olevassa ohjeessa kuvataan kuinka työajan lyhennysvapaan asetukset määritellään palveluun ja kuinka ansaittu työajan lyhennysvapaa esitetään henkilön kertymässä.
Jos kertymä laitetaan henkilölle päälle kesken vuoden, niin se laskee ansaintaa vuoden alusta asti kaikissa tapauksissa. Tämän takia on manuaalisesti laskettava, kuinka monen kuukauden tunnit/päivät pitää työskennellä, jotta ansaitsee vuoden ensimmäiset työajan lyhennysvapaat oikein. Asetukset voi tehdä henkilön taakse (Työaika > Hallinta > Henkilöt, valitse henkilön asetuksista Työtunni > Kertymät ja ylityöt > Työajan lyhennysvapaa), mutta ne pitää tehdä voimassaolotoiminnon (kalenterikuvakkeen näköinen painike) kautta, jotta ne ovat voimassa vain kuluvan vuoden ajan:
![](https://support.nepton.com/hc/article_attachments/25639125880733)
Esimerkissä työntekijä on aloittanut työnsä 1.3. asetusryhmässä, jossa työajan lyhennysvapaa on käytössä. Tämän takia ensimmäiset kynnykset ansainnalle on jätetty pois (17 ja 34 päivää), kuin myös niiden aikana ansaitut 16 tuntia.
## Työajan lyhennysvapaan määritykset
Palvelu laskee työajan lyhennysvapaata tässä kappaleessa kuvattujen määritysten mukaisesti. Työajan lyhennysvapaan kertymään huomioidaan valituista tapahtumatyypeistä muodostuva työaika (myös ylityö).
Asetuksissa on mahdollista valita tapahtumatyyppikohtaisesti sen huomiointi työajan lyhennysvapaan ansaintaan. Mikäli tapahtumatyypille ei ole toisin asetettu, niin työajan lyhennysvapaata ansaitaan kaikista tapahtumatyypeistä pois lukien:
  * palkaton poissaolo
  * palkaton sairausloma
  * vuosiloma
  * saldovapaa
  * työajan lyhennysvapaa
  * vuosivapaa


Työajan lyhennysvapaan määritykset voidaan määrittää joko Työyhteisö-tasolla tai Asetusryhmät-tasolla. Mikäli lyhennysvapaan ansaintaperuste on pääsääntöisesti kaikilla yrityksen työntekijöillä samanlainen, ansainnan perusteet on helpointa määrittää Työyhteisö-tason asetuksiin, jolloin ne koskevat myös kaikkia asetusryhmiä.
**Työaika > Hallinta > Työyhteisön asetukset > Työtunnit > Kertymät ja ylityötunnit > Laskennan asetukset > Työajan lyhennysvapaa**
tai
**Työaika > Hallinta > Asetusryhmät > Asetusryhmä-valikko: Haluttu asetusryhmä > Toiminto-valikko: Asetusryhmän asetukset > Työtunnit > Kertymät ja ylityötunnit > Laskennan asetukset > Työajan lyhennysvapaa**.
### Yleiset asetukset
Kertymä asetetaan päälle Kertymä käytössä -kohdasta **Työajan lyhennysvapaa: Asetus päällä**. Laskenta alkaa palvelun käyttöönottopäivästä katsottuna kyseisen ansaintakauden (kalenterivuosi tai kalenterikuukausi) alusta - ellei Voimassa alkaen -päivämäärää aseteta [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta jollekin toiselle ansaintakaudelle. Yksittäisen henkilön osalta laskenta alkaa henkilön ensimmäisestä kirjauksesta palvelun ollessa käytössä. Laskenta nollautuu jokaisen kalenterivuoden alussa.
![](https://support.nepton.com/hc/article_attachments/20897644871581)
Jos Työajan lyhennysvapaan ansainnan määrä ei ole sama joka kuukausi, esimerkiksi työsuhteen ja kalenterivuoden ensimmäisenä kuukautena ansaitaan enemmän kuin muina kuukausina, tällöin palvelun **käyttöönoton** yhteydessä Neptoniin tulee tuoda aikaisemmasta työnajanhallintajärjestelmästä tehdyt tapahtumat vuoden alusta. Tällöin Nepton tietää henkilön työskentelyn kalenterivuoden alusta alkaen ja voi laskea oikean ansainnan käyttöönoton alkaessa.
### Lainaussäännöt
**Kertymä lainaa automaattisesti kertymän saldosta** \- "Kyllä/Ei" - valinta sille, lainataanko aikaa kertymästä, jos päivän työvelvoite ei ole täyttynyt.
**Älä lainaa saldosta, jos työvelvoite on käsinasetettu** \- "Kyllä/Ei" - valinta sille, lainataanko aikaa kertymästä, jos päivän työvelvoite on asetettu manuaalisesti. Työvelvoite voidaan asettaa manuaalisesti kalenterinäkymässä muuttamalla päivän "Työpäivän pituus" - arvoa.
**Täytä työviikon tunnit saldosta työviikon viimeisenä päivänä** \- "Kyllä/Ei" - valinta sille, lainataanko aikaa kertymästä viikon päätteeksi, jos viikon työvelvoite ei ole täyttynyt.
### Ansainnan säännöt
**Vuoden alkamispäivä** -kohdassa voidaan määrittää ansaintatulukon nollaus jollekin muulle päivälle kuin kuun alkuun tai nollaus jollekin muulle kuulle kuin tammikuuhuun.
**Ansaintataulukko nollautuu joka** -kohta voidaan määritellä olemaan joko vuosi tai kuukausi. Jos ansaintakautena on vuosi, työajan lyhennysvapaan ansaita tapahtuu ansaitataulukon mukaisesti kalenterivuoden aikana. Jos ansaitakautena on kuukausi, ansainta tapahtuu joka kalenterikuukauden ajalta ansaintataulukon mukaisesti. Jos asetuksen arvoa ei ole asetettu, ansaintakautena käytetään vuotta.
**Ansaintaperuste** voidaan määritellä joko tunteina, päivinä tai kuukausina, oletus on tunteina.
Jos ansaintaperuste on kuukausina, vuosiloma-ajan laskennan työpäivien määrää tai työtuntien määrää käytetään katsomaan, ansaitaanko työkuukaudelta työajan lyhennysvapaata. Lue lisää vuosiloman ansainnan käyttöönotosta [täällä](<https://support.nepton.com/hc/fi/articles/360002560698>).
Jos ansaintaperuste on tunteina, ansaintakynnys voidaan asettaa minuuttien tarkkuudella.
Huom! Ansaintaperusteena ei voi käyttää kuukausina, jos ansaintakautena on kuukausi. Jos näin on asetettu, työajan lyhennysvapaata ei ansaita lainkaan.
**Ansaitaan** -kohtaan valitaan ansaitaanko vapaat tunteina vai päivinä, alla olevassa esimerkkikuvassa molemmat on asetettu päivinä.
**Ansaitaan työaikaprosentin mukaan** -kohdassa voidaan määrittää ansainnan tulevan henkilölle määritetyn työaikaprosentin mukaan. Jos työntekijät esimerkiksi ansaitsisivat 17 työpäivän jälkeen 8 tuntia työajanlyhennysvapaata, 50% työaikaprosentilla työntekijä ansaitsisi 17 työpäivän jälkeen 4 tuntia työajanlyhennysvapaata.
**Ansaintaprosentti** -kohdassa voidaan määrittää ansainnan tulevan jonkin tietyn prosentin mukaan, esimerkiksi jos ansaintaprosentin tarvitsee olla eri kuin työntekijän työaikaprosentti.
**Vapaa/loma jätetään huomiotta juhlapyhinä** -kohdassa voidaan määrittää, lasketaanko juhlapyhänä oleva loma tai vapaa työpäiväksi.
**Ansaitse jos työsuhteen kesto ylittää** -kohdassa voidaan määritellä työsuhteen vähimmäiskesto lyhennysvapaan ansaitsemiselle. Tämä on käytössä vain, jos Työsuhde-osiossa on määritelty työsuhteen alkamispäivä.
**Ansaitaan työsuhteen alusta** -kohdassa voidaan määrittää, että työajan lyhennysvapaata ansaitaan työsuhteen alusta lähtien. Jos arvona on "Ei" tai arvoa ei ole asetettu, työajan lyhennysvapaan ansainta alkaa vasta sen jälkeen, kun työsuhde on kestänyt kohdassa **Ansaitse jos työsuhteen kesto ylittää** määritettyjen kuukausien verran.
**Ansaitaan vain säännölliseltä työajalta** -kohdassa voidaan määrittää, että työajan lyhennysvapaata ansaitaan vain säännölliseltä työajalta, eli siten että ylityötä ei oteta huomioon.
**Ansaitse kertymästä lainatusta ajasta** -kohdassa voidaan määrittää, ansaitaanko kertymää ajasta joka on lainattu kertymästä, kuten esimerkiksi aika joka on lainattu saldosta.
**Kun työskennelty** -kohtaan lisätään kynnysarvot, joiden ylittyessä ansaitaan viereisessä sarakkeessa määritelty "ansaitaan" arvo.
**Ansaitaan** -kohtaan määritellään ansainnan määrä, viereisen "Kun työskennelty" sarakkeen arvon ylittyessä. Sarakkeiden arvo nousee sitä mukaa mitä enemmän tunteja siihen mennessä koko ansaintakaudella on ansaittu työajan lyhennysvapaita. Eli arvo ei ole joka kuukausi sama esimerkiksi 8 tuntia, vaan nouseva esimerkiksi 8 tuntia, 16 tuntia, 24 tuntia jne.
![](https://support.nepton.com/hc/article_attachments/27865625081501)
**Tapahtumatyyppi (Palkallinen)** ja **Tapahtumatyyppi (Palkaton)** -kohdissa voidaan määritellä tapahtumatyyppikohtaisesti, ansaitaanko tapahtumista työajan lyhennysvapaata. Muista kuin luetelluista palkallisista tapahtumatyypeistä ansaitaan oletusarvoisesti työajan lyhennysvapaata. Tapahtumatyyppi (Palkaton) -kohdassa luetelluille tapahtumatyypeille ei oletusarvoisesti ansaita työajan lyhennysvapaata ellei asetusta erikseen laiteta päälle.
![](https://support.nepton.com/hc/article_attachments/21806948509725)
Huom! Jos "Kun työskennelty" kynnysarvot on määritelty myös työyhteisön asetuksissa tai ylemmällä asetusryhmätasolla, periytyvät kynnysarvot alempien asetusryhmien tyhjiin kynnysarvokenttiin, ellei niihin valita arvoa "älä käytä ylemmän tason ryhmän asetusta".
## Työajan lyhennysvapaan ansainta ja käyttö
Palvelu laskee työajan lyhennysvapaan ansaintaa voimassa olevien asetuksien mukaan automaattisesti. Kun työajan lyhennysvapaan kertymisen peruste, esimerkiksi tietty työskentelymäärä on ansaittu, tulee työajan lyhennysvapaa-kertymään sille päivälle automaattisesti plussaa.
Työajan lyhennysvapaata käytetään tapahtumatyypillä 'työajan lyhennysvapaa'. Tämä tapahtumatyyppi vähentää automaattisesti tapahtumapäivältä työajan lyhennysvapaan kertymää.
Jos työajan lyhennysvapaata ansaitaan päivinä, ja lyhennysvapaata halutaan pitää puoli päivää, työajan lyhennysvapaan kestoksi merkitään puolet työpäivän kestosta. Järjestelmä pyöristää käytetyn lyhennysvapaan sille annetun keston mukaisesti puolikkaisiin päiviin. Eli esimerkiksi jos työpäivän pituus on 8 tuntia, jos työajan lyhennysvapaan kestoksi merkitään 3,5 tuntia, tämä pyöristyy niin että työajan lyhennysvapaata käytetään puoli päivää.
Jos työajan lyhennysvapaata halutaan pitää puolikkaita päiviä yli yhden vuorokauden keston, tulee puolikkaan päivän lyhennysvapaa merkitä omana tapahtumanaan. Eli esimerkiksi jos halutaan pitää 1,5 päivää työajan lyhennysvapata, merkitään yksi päivän mittainen työajan lyhennysvapaa ja yksi puolen päivän mittainen työajan lyhennysvapaa.
## Työajan lyhennysvapaiden raportointi
Työajan lyhennysvapaan kertymiä ja käytettyjä vapaita voi seurata raportilla Työajan lyhennysvapaat, missä näkyy valitun vuoden ja sitä edeltävän vuoden kertymät ja pidetyt vapaat. Tarkemmat tiedot työajan lyhennysvapaiden raportista löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002548777>).
