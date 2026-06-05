---
id: 29569021494685
title: Vuosityöajan käyttöönotto
url: https://support.nepton.com/hc/fi/articles/29569021494685-Vuosity%C3%B6ajan-k%C3%A4ytt%C3%B6%C3%B6notto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Vuosityöaika
section_id: 30253701495965
section_path:
- Vuorosuunnittelu ja vuorokalenterit
- Vuosityöaika
labels: []
promoted: false
updated_at: '2026-03-16T08:33:51Z'
edited_at: '2026-03-16T08:33:51Z'
---

# Vuosityöajan käyttöönotto

Tässä ohjeessa kuvataan vuosityöajan käyttöönottoon liittyvät asetukset. Vuosityöajan laskenta on suunniteltu erityisesti teollisuuden ja muiden jatkuvaa tuotantoa vaativien alojen tarpeisiin, joissa työaikaa tarkastellaan koko vuoden ajalta.[ ](<https://nepton.zendesk.com/knowledge/editor/01K5B8SDCEA0J6WF7S9ZJ31KS8/fi?brand_id=114094689392&section_id=4410638658833>)Vuosityöajan seuranta tapahtuu vuorosuunnittelun suunnittelunäkymässä. Sen asetukset ovat kuitenkin käytössä ainoastaan Complete -palvelutasolla.
### Vuosityöajan asetukset
Seuraavat asetukset tulee määrittää vuosityöajan käyttöönottoa varten. Osa asetuksista on pakollisia ja osa määritetään tarvittaessa käyttötarpeen mukaan. Vuosityöajan asetukset voidaan määrittää työyhteisötasolla, asetusryhmätasolla tai henkilön asetuksissa. Asetukset löytyvät valitsemalla **Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Vuorot > Vuosityöaika**. Alla on esitetty kaikki vuosityöajan asetukset ja niiden käyttäytyminen. 
![Screenshot 2025-09-17 114112.png](https://support.nepton.com/hc/article_attachments/30393169985565)
#### Vuosityöajan tavoite
Vuosityöajan tavoite määritetään tunteina, ja se toimii vertailuarvona suunniteltujen työvuorojen kertymälle. Tavoite tulee määrittää, jos halutaan seurata työntekijän suunniteltujen vuorojen toteumaa suhteessa vuosityöaikaan. Jos vuosityöajan tuntimäärä vaihtelee eri vuosina, tulee jokaiselle vuodelle määrittää oma vuosityöajan tavoite [voimassaolotoiminnon ](<https://support.nepton.com/hc/fi/articles/360002559358-Voimassaolotoiminto-Ty%C3%B6aika-osiossa>)kautta, siten että se on voimassa vain kyseisen vuoden ajan.
![Screenshot 2025-09-17 115443.png](https://support.nepton.com/hc/article_attachments/30393709429533)
Lomakalenterilla tehty arkipyhä ei lyhennä vuosityöajan arvoa eikä sen kuulukaan. Vuosityöajan arvoa lyhentää ainoastaan työaikapuolella tehdyt tapahtumat jos niihin on asetuksilla otettu kantaa.
#### Suunniteltu tapahtumatyyppi jätetään pois vuosityöajan suunnitelluista tunneista
Tällä asetuksella määritetään, mitkä tapahtumatyypit jätetään pois vuosityöajan suunnitelluista tunneista, jos ne on asetettu työvuoron tilalle vuorosuunnittelunäkymässä. Asetus määritetään, tilanteissa joissa poissaoloja suunnitellaan etukäteen vuorosuunnittelun suunnittelunäkymässä ennalta luoduilla vuorokalenterin [vuorotyypeillä](<https://support.nepton.com/hc/fi/articles/12209358591773-Vuorokalenterin-luominen-ja-julkaisu>).
Jos poissaolojen suunnittelu tehdään ensisijaisesti vuorosuunnittelunäkymässä, ennen kuin itse tapahtuma tai tapahtumapyyntö on kirjattu työaikakalenteriin, tulee tähän asetukseen määrittää ne tapahtumatyypit, jotka halutaan jättää pois vuosityöajan suunnitelluista tunneista. Estä -arvoon tulee määrittää "Kyllä", jos tapahtuma halutaan jättää pois vuosityöajan suunnitelluista tunneista.
![Screenshot 2025-09-17 120451.png](https://support.nepton.com/hc/article_attachments/30394173956637)
Esimerkiksi jos työntekijän suunnitellun vuoron tilalle asetetaan vuosiloma ja muutos julkaistaan, vuosityöajan suunniteltu arvo pienenee automaattisesti, kun kyseinen tapahtumatyyppi on määritetty tässä asetuksessa.
#### Vuoron kanssa päällekkäinen tapahtumatyyppi jätetään pois vuosityöajan suunnitelluista tunneista
Tällä asetuksella voidaan määrittää, mitkä tapahtumatyypit jätetään pois vuosityöajan suunnitelluista tunneista, jos ne ovat päällekkäin suunnitellun työvuoron kanssa.
Asetus määritetään tilanteissa, joissa poissaolot lisätään ensin työaikapuolelle, esimerkiksi työntekijän toimesta. Tällöin järjestelmä laskee vuosityöajan suunnitellut tunnit uudelleen vasta sen jälkeen, kun poissaolo (esimerkiksi vuosiloma) on kirjattu.
Jos poissaoloja kirjataan ensisijaisesti työaikakalenteriin, ja ne voivat olla päällekkäisiä jo suunniteltujen vuorojen kanssa, tulee tähän asetukseen määrittää ne tapahtumatyypit, jotka halutaan jättää pois vuosityöajan suunnitelluista tunneista. Estä -arvoon tulee määrittää "Kyllä", jos tapahtuma halutaan jättää pois vuosityöajan suunnitelluista tunneista.
![Screenshot 2025-09-17 123119.png](https://support.nepton.com/hc/article_attachments/30394825597085)
Esimerkiksi jos työntekijälle on suunniteltu työvuoro, mutta hänelle kirjataan myöhemmin vuosiloma samalle päivälle, vuosityöajan suunniteltu arvo pienenee automaattisesti, kun kyseinen tapahtumatyyppi on määritetty tässä asetuksessa.
Tapahtumat, jotka jätetään pois vuosityöajan suunnitelluista tunneista, tulee merkitä työaikakalenteriin siten, että ne alkavat joko samaan aikaan kuin suunniteltu työvuoro tai ennen vuoron alkua (esimerkiksi klo 00:00).
Jos tapahtuma alkaa työvuoron jälkeen, se ei poista vuoron alkuun sijoittuvia tunteja vuosityöajan suunnitelluista tunneista.
#### Tapahtumatyypit, jotka lyhentävät jakson vuosityöaika-arvoja
Tällä asetuksella määritetään, mitkä tapahtumatyypit lyhentävät vuosityöajan arvoja. Asetuksen avulla voidaan hallita, miten poissaolot vaikuttavat vuosityöajan tavoitteeseen ja suunnitellun työn arvoihin (Vuorot, Vuorot yhteensä). Asetuksen alla on kaksi vaihtoehtoista määrittelytapaa, joista tulee käyttää vain toista kerrallaan. Lisäksi asetetaan keskimääräinen viikon pituus tunteina, jonka avulla lasketaan päivittäinen lyhennettävä arvo.
![Screenshot 2025-10-28 165929.png](https://support.nepton.com/hc/article_attachments/31371680612125)
Ensimmäinen määrittelytapa otetaan käyttöön, kun halutaan lyhentää **Vuosityöajan tavoitearvoa** , **Vuorot-arvoa** ja **Vuorot yhteensä** -arvoa, jos työntekijän kalenteriin on kirjattu asetukseen määritetty tapahtumatyyppi. Tavoitearvo pienenee niiltä päiviltä, joille tapahtumatyyppi on merkitty. Jos asetuksessa on valittu arvoksi "Keskimääräisen viikon pituuden mukaan", lyhennys lasketaan asetetusta keskimääräisen viikon pituudesta jaettuna seitsemällä, jolloin saadaan päivittäinen lyhennettävä arvo. Jos taas käytetään arvoa "Päällekkäisten vuorojen mukaan", tavoitearvo pienenee vain niiltä päiviltä, joilla on sekä suunniteltu vuoro että tapahtumatyyppi. Lyhennys vastaa tällöin vuoron kestoa. Vuorot-arvo pienenee, kun vuoro ja tapahtumatyyppi ovat samalla päivällä. Lyhennys vastaa tällöin vuoron pituutta, jos tapahtuma alkaa vuoron alussa tai sitä ennen. Vuorot yhteensä -arvo pienenee jos vuoro ja tapahtumatyyppi ovat päällekkäin työntekijän kalenterissa. Vuorot yhteensä -arvo pienenee aina kappaleina (1 kpl). 
Toinen määrittelytapa otetaan käyttöön, kun vuosityöajan tavoitearvo on kiinteä suunnittelunäkymässä, mutta halutaan lyhentää **Vuorot-arvoa** ja **Vuorot yhteensä** -arvoa, jos työntekijän kalenteriin on kirjattu asetukseen määritetty tapahtumatyyppi. Tällöin Vuorot-arvo pienenee kaikilta niiltä päiviltä, joille on merkitty kyseinen tapahtumatyyppi. Vuorot yhteensä -arvo pienenee, jos vuoro ja tapahtumatyyppi ovat päällekkäin työntekijän kalenterissa. Vuorot yhteensä -arvo vähenee aina kappaleina (1 kpl).
Asetuksen yhteydessä määritetään myös keskimääräinen viikon pituus (esimerkiksi 34,6 tuntia), joka toimii pohjana päivittäisen lyhennettävän arvon laskennalle. Tämä arvo jaetaan seitsemällä, ja tulosta käytetään tavoitearvon ja vuorot-arvon vähennyksiin silloin, kun lyhennys perustuu keskimääräiseen viikkopituuteen.
#### Ansaintakausi
Ansaintakausi määrittää vuosityöajan seurantajakson. Tyypillisesti ansaintakausi on kalenterivuosi (esimerkiksi 1.1.-31.12.), mutta se voi olla myös muu kuin 12 kuukauden jakso.
Palvelussa ansaintakaudelle määritetään:
  * Jakson alkupäivä
  * Toistuva jakson pituus päivinä, viikkoina tai kuukausina


Yleisin tapa on käyttää **Toistuvan jakson pituutta kuukausina** , mutta vaihtoehtoisesti voidaan käyttää asetuksia Tosituvan jakson pituus päivinä tai Toistuvan jakson pituus viikkoina. Jos käytetään esimerkiksi Toistuvan jakson pituus päivinä -asetusta, ja karkausvuonna päivien määrä poikkeaa muista vuosista, tulee jakson alkupäivään määrittää voimassaoloaika voimassaolotoiminnon kautta:
  * Voimassa alkaen -päivämäärä
  * Voimassa saakka -päivämäärä


Tämä varmistaa, että vuosityöajan laskenta toimii myös vuosina, jolloin vuoden pituus ei ole vakio.
![Screenshot 2025-09-17 123827.png](https://support.nepton.com/hc/article_attachments/30395223971613)
### Vuosityöajan laskentalogiikka
Vuosityöajan laskenta perustuu päiväkohtaiseen jakoon. Tämä tarkoittaa, että vuosityöajan tavoite jaetaan vuoden kaikille päiville, jolloin jokaiselle päivälle muodostuu laskennallinen arvo. Esimerkiksi vuosityöaika 1706 tuntia vastaa keskimäärin noin 4,67 tuntia päivässä (1706 h / 365 päivää). Kalenteripäiville jakaminen on erityisen tärkeää tilanteissa, joissa henkilö siirtyy asetusryhmästä toiseen ja vuosityöajan tavoite muuttuu.
Jotta vuosityöajan tavoite lasketaan henkilölle oikein, tulee hänellä olla aina määriteltynä oikeat alku- ja loppupäivämäärät kullekin asetusryhmään kuulumiselle tai vuosityöajan arvon voimassaoloajalle henkilön asetuksissa. Näitä ajanjaksoja käytetään laskennassa sen määrittämiseksi, kuinka suuri osa koko vuoden tavoitteesta kuuluu millekin ajanjaksolle.
Suunnitellut työvuorot vertaillaan näihin päiväkohtaisiin arvoihin, ja järjestelmä seuraa kertymää suhteessa tavoitteeseen. Tämä auttaa vuorosuunnittelijaa hahmottamaan, onko työntekijän työaika tasapainossa vai kertyykö ali- tai ylitunteja.
### Vuosityöajan erityistilanteet
Vuosityöajan asetukset ottavat huomioon henkilön työsuhteen alku- ja päättymispäivän sekä työaikaprosentin. Alla on kuvattu yleisimmät tilanteet, joissa vuosityöajan asetuksia tulee tarkistaa tai täydentää.
#### Työsopimus alkaa kesken vuoden
Jos työsopimus alkaa kesken vuoden, tulee työajan asetusryhmän olla voimassa siitä päivästä alkaen, kun työsopimus alkaa. Jos henkilöllä ei ole määritetty asetusryhmän alkamispäivämäärää, vuosityöajan tavoite lasketaan koko vuoden mukaan, eikä alkanutta sopimusta oteta huomioon.
#### Työsopimus päättyy kesken vuoden
Jos työsopimus päättyy kesken vuoden, tulee henkilölle lisätä asetusryhmä, missä vuosityöajan tavoite on 0 tuntia alkaen seuraavasta päivästä, kun työsopimus päättynyt. Vaihtoehtoisesti voidaan määrittää henkilöasetuksiin vuosityöajaksi 0 tuntia alkaen seuraavasta päivästä, kun työsopimus on päättynyt. 
#### Työaikaprosentin muutos
Jos henkilön työaikaprosentti muuttuu kesken vuoden, laskee palvelu vuosityöajan henkilön asetuksissa olevan työaikaprosentin mukaan kultakin ajanjaksolta.
#### Pitkä poissaolo
Jos henkilö jää pidemmälle vapaalle, kuten opintovapaalle, tulee hänet siirtää asetusryhmään, jossa vuosityöajan tavoite on 0 tuntia, tai määrittää henkilöasetuksiin vuosityöajan tavoitteeksi 0 tuntia poissaolon ajaksi.
