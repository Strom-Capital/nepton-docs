---
id: 360016649598
title: Vuorotarpeiden luominen suunnitelmalle (Avustajat-osio)
url: https://support.nepton.com/hc/fi/articles/360016649598-Vuorotarpeiden-luominen-suunnitelmalle-Avustajat-osio
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Vuorojen suunnittelu
section_id: 360003240537
section_path:
- Vuorosuunnittelu ja vuorokalenterit
- Vuorojen suunnittelu
labels: []
promoted: false
updated_at: '2025-12-02T10:20:58Z'
edited_at: '2022-12-20T07:50:01Z'
---

# Vuorotarpeiden luominen suunnitelmalle (Avustajat-osio)

Tätä ohjetta ei ole päivitetty sisältämään muutoksia jotka julkaisemme 27.12.2022.
Katso lisätiedot [versiotiedotteestamme](<https://support.nepton.com/hc/articles/360006615478>).
Katso myös ohjeet [vuorojen jakamiseksi henkilöille automaattisesti](<https://support.nepton.com/hc/fi/articles/360016727798>)
## Johdanto
Tämä ohje kuvaa miten vuorotarpeet luodaan suunnitelmalle. Usein vuorotarpeiden luominen isolle määrälle toimipisteitä on epämukava toimenpide, ja näiden ohjeiden avulla pystytäänkin luomaan vuorotarpeita massa-ajona suunnitelmatyökalun avulla.
Taulukko1 : Termistö
**Termi** | **Määrite**  
---|---  
Vuorotarve | Suunnittelunäkymässä varattu aikaväli, jota ei ole vielä jaettu kenellekään henkilölle  
Vuoro | Suunnittelunäkymässä varattu aikaväli, joka on jaettu henkilölle  
Tehtävä | Toimenpide joka henkilöltä vaaditaan osana työtä. Tehtävä voidaan mitata tunneissa tai kappaleissa.  
Tehtäväryhmä | Yhteenkuuluvat tehtävät voidaan määrittää samaan tehtäväryhmään, jolloin tehtävien käsittely on helpompaa, jos tehtäviä on useita.  
Osaaminen |  Taito tai kyky, jota tarvitaan tehtävän suorittamiseen. Osaamisia hyödynnetään automaattisessa vuorojen jakamisessa, jotta vuorot pystytään jakamaan oikeille henkilöille. Osaamisia voi asettaa sekä henkilölle että tehtävälle. Näiden tietojen välistä suhdetta käytetään apuna sopivan henkilön löytämisessä vuorolle.  
Suunnitelma | Yhdistelmä tehtävistä, jotka tulee saavuttaa. Suunnitelmia voi olla useampi yhtä aikaa. Kohde/Tarjottu/Sovittu arvot asetetaan jokaiselle toimipisteelle per suunnitelma. Suunnitelman tarkoitus on luoda vuorotarpeita automaattisesti massana.  
Henkilötyöpäivä (HTP) | Tätä käytetään vuoron kustannuksen laskemiseen. Sen pituus on normaalisti henkilön työpäivän pituus, esimerkiksi 7 tuntia 30 minuuttia.  
Tavoite | Termi viittaa suunnitelmatyökalussa haluttuun henkilötyöpäivien määrään yhdelle tehtävälle. Se viittaa tehtävälle tavoiteltujen henkilötyöpäivien määrään. Jos tehtävä mitataan kappaleissa, tavoitteen määrä on kappaleina.  
Tarjottu | Termi viittaa suunnitelmatyökalussa määrään, joka esimiehen mielestä on saavutettavissa tehtävälle.  
Sovittu | Termi viittaa suunnitelmatyökalussa määrään, jonka esimies on sopinut suunnittelijan/ylläpitäjän kanssa. Arvoa käytetään automaattisten vuorotarpeiden ja vuorojen luomisessa.  
## Mitä suunnitelmatyökalut ovat
Suunnitelmatyökalut sisältävät Tavoitesuunnittelu-, Karkeasuunnittelu- ja Resurssisuunnittelu-näkymät. Suunnitelmatyökaluja käytetään automaattiseen vuorotarpeiden ja vuorojen suunnitteluun suunnitelman mukaisesti. Suunnitelmatyökalut helpottavat tavoitteiden määrittämistä tehtävien saavutettavaksi määrätyllä aikavälillä.
### Karkeasuunnittelu
Karkeasuunnittelu-näkymää käytetään nimensä mukaisesti asettamaan karkeat arviot tehtäville jokaiselle toimipisteelle. Tämä näkymä on saatavilla osiossa Vuorosuunnittelu > Suunnitelmat kun klikataan suunnitelman vieressä olevaa Karkeasuunnittelu-painiketta (ks. kuva alla).
![20210120-wsp-planningtool-fi-1.png](https://support.nepton.com/hc/article_attachments/360016043837/20210120-wsp-planningtool-fi-1.png)
### 
### Tavoitesuunnittelu
Tavoitesuunnittelu-näkymässä voidaan asettaa tavoitteita jokaiselle toimipisteelle.
Tämä näkymä on saatavilla osiossa Vuorosuunnittelu > Suunnitelmat kun klikataan suunnitelman vieressä olevaa Tavoitesuunnittelu-painiketta (ks. kuva alla).
![20210120-wsp-planningtool-fi-2.png](https://support.nepton.com/hc/article_attachments/360016110838/20210120-wsp-planningtool-fi-2.png)
### Resurssisuunnittelu
Resurssisuunnittelu-näkymässä tavoitteet asetetaan suoraan henkilöille. Arvot, jotka ovat asetettu sovituiksi ovat käytössä automaattisen vuorojen luonnin työkalussa.
Tämä näkymä on saatavilla osiossa Vuorosuunnittelu > Suunnitelmat kun klikataan suunnitelman vieressä olevaa Resurssisuunnittelu-painiketta (ks. kuva alla).
![20210120-wsp-planningtool-fi-3.png](https://support.nepton.com/hc/article_attachments/360016111298/20210120-wsp-planningtool-fi-3.png)
## Kuinka vuorotarpeet luodaan automaattisesti suunnitelman mukaan
Vuorotarpeiden automaattinen luonti edellyttää seuraavat vaiheet:
  * Luo tehtäviä. Tehtäviä voidaan luoda näkymästä "Vuorosuunnittelu" > "Tehtävät"
  * Luo suunnitelma.
  * Aseta Kohteet/Tarjotut/Sovitut - arvot käyttäen Karkeasuunnitelma- tai Tavoitesuunnitelma-näkymää
  * Mene näkymään Vuorosuunnittelu > Suunnittelunäkymä
  * Valitse Työkalut-osio ja klikkaa "Luo vuorotarpeet suunnitelmalle" -painiketta.


![20210120-wsp-planningtool-fi-4.png](https://support.nepton.com/hc/article_attachments/360016046957/20210120-wsp-planningtool-fi-4.png)
  * Tämän jälkeen aukeaa popup-ikkuna, jossa määritetään vuorotarpeiden luonti. Vuorotarpeiden luonti on kaksivaiheinen prosessi. 
    * Vaihe 1: "Laske vuorotarpeet"-painike laskee vuorotarpeet valintojen mukaan
    * Vaihe 2: "Luo vuorotarpeet"-painike luo vuorotarpeet ja lisää ne palveluun


Vuorotarpeet luodaan jokaiselle toimipisteelle, joille suunnitelmalla on sovittuja arvoja. Vuorotarpeen pituus määritetään Henkilötyöpäivä-tehtävälle asetetun pituuden mukaan. Yleisesti tämä on 7 tuntia 30 minuuttia, mutta tätä voidaan muuttaa osiossa Vuorosuunnittelu > Tehtävät.
![20210120-wsp-planningtool-fi-5.png](https://support.nepton.com/hc/article_attachments/360016048577/20210120-wsp-planningtool-fi-5.png)
### Asetukset
  1. **Suunnitelma** : Valitse suunnitelma, jonka mukaan vuorotarpeet luodaan
  2. **Päivämääräväli** : Aikaväli jolle vuorot halutaan luoda. Esimerkiksi jos suunnitteluaikaväli on 20 päivää, voit luoda vuorot 20 päivälle valitsemalla aikavälin alun ja lopun niin että niiden välillä on 20 päivää.
  3. **Toimipiste:** Valitse toimipiste jolle vuorotarpeet luodaan. Jos ylätason toimipiste valitaan, vuorot luodaan myös kaikille toimipisteen alla oleville toimipisteille.
  4. **Tehtävät** : Valitse tehtävä(t) joille vuorotarpeet luodaan
  5. **Luo vuorotarpeet viikonlopulle** : Jos valittu, vuoroja luodaan myös viikonlopun päiville
  6. **Luo vuorotarpeet juhlapyhille** : Jos valittu, vuoroja luodaan myös juhlapyhille
  7. **Korvaa olemassa olevat tarpeet** : Jos valittu, vanhat vuorotarpeet valituille toimipisteille poistetaan ja luodaan uudet tilalle
  8. **Perumisikkuna** : Arvo jolla määritetään voiko henkilö perua vuoronsa. Valittavissa on kolme asetusta
[code] a. Nollaa suurempi luku: Henkilö voi perua vuorovarauksensa x päivää ennen vuoron alkua. Esimerkiksi jos on syötetty 10, henkilön tulee perua vuoro 10 päivää ennen sen alkamista.  
         
         b. Nolla (0): Jos arvoksi annetaan 0, vuoron varaus voidaan perua vuoron alkamispäivään asti.  
         
         c. Jos kenttä jätetään tyhjäksi, vuoron varausta ei voi perua.
[/code]


### Kuinka vuorotarpeet lasketaan
[code] 
    **Huomio:** Vuorojen luontityökalu käyttää toimipisteen työvuoron oletukseksi   
    asetettua alku- ja päättymisaikaa vuorotarpeiden luontiin.
[/code]
Vuorojen automaattiluontia kuvataan alla olevassa esimerkkitapauksessa.
Käytössä on suunnitelma "Suunnitelma A" jonka suunnitteluväli on 20 päivää ja halutaan luoda vuorotarpeet 10 päivän aikavälille (selvyyden vuoksi esimerkissä ei puhuta päivämääristä vaan päivistä). Sovittu työmäärä toimipisteen "Toimipiste A" tehtävälle "Tehtävä 1" on 700. Tehtävän "Tehtävä 1" suorittamiseen vaaditaan 30 minuuttia (tehtävän kustannus). Henkilötyöpäivä-arvo on 7 tuntia ja 30 minuuttia (eli yhteensä 450 minuuttia) ja lounaan kesto on 60 minuuttia.  
  
Laskenta menee seuraavalla tavalla:  
  
Koko ajanjaksolle yhteensä "Tehtävä 1" henkilötyöpäivät = (Sovittu työn määrä * tehtävän kustannus) / (Henkilötyöpäivä minuutteina + lounaan kesto) eli "Tehtävä 1" henkilötyöpäivät = (700 * 30) / (450 + 60) = 41,17 joka pyöristetään 41 henkilötyöpäivään.
Yhden päivän vuorotarpeet = ("Tehtävä 1" henkilötyöpäivät / päivät yhteensä suunnitelmassa "Suunnitelma A") eli (41 / 20) = 2.
Vuorotarpeet jotka luodaan valitulle aikavälille suunnitelman mukaan = (Valitun aikavälin päivien määrä * yhden päivän vuorotarpeet) eli (10 * 2 ) = 20.
