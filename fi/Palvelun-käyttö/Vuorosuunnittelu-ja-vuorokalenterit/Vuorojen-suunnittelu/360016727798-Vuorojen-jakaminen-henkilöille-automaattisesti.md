---
id: 360016727798
title: Vuorojen jakaminen henkilöille automaattisesti
url: https://support.nepton.com/hc/fi/articles/360016727798-Vuorojen-jakaminen-henkil%C3%B6ille-automaattisesti
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
edited_at: '2022-12-20T07:49:29Z'
---

# Vuorojen jakaminen henkilöille automaattisesti

Tätä ohjetta ei ole päivitetty sisältämään muutoksia jotka julkaisemme 27.12.2022.
Katso lisätiedot [versiotiedotteestamme](<https://support.nepton.com/hc/articles/360006615478>).
Katso myös ohjeet kuinka voit [Luoda vuorotarpeet suunnitelmalle](<https://support.nepton.com/hc/fi/articles/360016649598>)
## Alkusanat
Tässä artikkelissa kerromme kuinka voit jakaa vuoroja henkilöille automaattisesti Neptonin Vuorosuunnittelu-osiossa.
## Vaatimukset
  * Henkilölle merkittyjä "Viikoittaiset tunnit MIN" ja "Viikoittaiset tunnit MAX" - arvoja käytetään sen laskemiseen, että kuinka monta tuntia henkilö voi tehdä töitä viikossa.
  * "Viikoittaiset tunnit MAX" arvoa käytetään ensisijaisesti maksimiarvona, jos tätä tietoa ei ole saatavilla, minimiarvoa käytetään myös maksimina.
  * Kaikkia niitä vuoroja, jotka ovat jo jaettu henkilölle käytetään sen laskemiseen kuinka paljon henkilö voi vielä tehdä tunteja päivässä ja viikossa
  * Vuorotarve määritetään vain henkilölle, jolla on tarpeeksi työtunteja jäljellä viikossa / päivässä
  * Saatavilla olevat minuutit per viikko perustuu "Viikoittaiset tunnit MIN" ja "Viikoittaiset tunnit MAX" - asetuksiin
  * Saatavilla olevat minuutit per päivä perustuu **henkilötyöpäivän ja lounaan kestoon** viikoittain saatavilla oleviin minuutteihin asti. Esimerkiksi jos henkilötyöpäivä on 8 tuntia ja lounas 1 tunti, työntekijä voi tehdä yhden 9 tunnin vuoron tai minkä tahansa vuorojen yhdistelmän, joista tulee yhteensä 9 tuntia, esimerkiksi 4 tunnin vuoro + 2 tunnin vuoro + 3 tunnin vuoro
  * Kiinteän pituiset vuorotarpeet jaetaan työntekijälle vain jos työntekijällä ei ole muita tapahtumia jotka menevät vuorotarpeen päällekkäin ja vuoro on joko päivän ensimmäinen työntekijälle määritelty tapahtuma tai vuoron ajankohta kokonaisuudessaan joko seuraa tai edeltää olemassa olevaa tapahtumaa
  * Jos vuorotarpeella on osaamisvaatimuksia, se jaetaan vain henkilölle, joka täyttää kaikki osaamisvaatimukset


[code] 
    **Huomio:** Vuorotarpeiden luontityökalu käyttää toimipisteen työvuoron oletukseksi   
    asetettua alku- ja päättymisaikaa vuorotarpeiden luontiin. Jos toimipisteen työvuoron   
    alku/päättymisaika on kestoltaan pidempi kuin **henkilötyöpäivä + lounas** , ei työkalu määritä  
    näitä vuorotarpeita.
[/code]
## Miten vuorotarpeet jaetaan henkilöille automaattisesti
Vuorotarpeiden jakaminen henkilöille automaattisesti vaatii seuraavat vaiheet:
Vuorotarpeiden automaattinen jakaminen asetetaan päälle menemällä "Vuorosuunnittelu" -> "Suunnittelunäkymä" - näkymään, josta avataan kohta "Työkalut" ja painetaan "Jaa vuorot henkilölle automaattisesti"-painiketta.
![20210120-wsp-1-fi.png](https://support.nepton.com/hc/article_attachments/360016028877/20210120-wsp-1-fi.png)
Painikkeen painamisen jälkeen aukeaa popup-ikkuna, josta voi määrittää tarvittavat asetukset henkilöiden automaattiseen vuorotarpeisiin jakamiseen.
![20210120-wsp-2-fi.png](https://support.nepton.com/hc/article_attachments/360016094618/20210120-wsp-2-fi.png)
### Asetukset
  1. **Valitut päivät** : Ajanjakso, jolle automaattinen vuorojen jako halutaan tehdä automaattisesti. Henkilöille jaetaan vuorotarpeet tällä ajanjaksolla.
  2. **Henkilölista** : Valitse henkilölista, jos haluat jakaa vuorot listassa määritetyille henkilöille
  3. **Toimipiste:** Valitse toimipiste, jolle haluat tehdä vuorojen jakamisen. Jos ylätason toimipiste valitaan, vuorot jaetaan myös kaikille toimipisteen alla oleville toimipisteille määritetyllä aikavälillä.**  
**
  4. **Julkaisun tila** : Jaetaanko vuorot vain julkaistuille vuorotarpeille vai kaikille vuorotarpeille  

  5. **Suunnittele päälle** : Jaa vuoro henkilölle, vaikka henkilöllä olisi tämän tyypin tapahtumia samana päivänä. Valittavissa on neljä vaihtoehtoa:
     * **Ei kummankaan** : Jos tämä on valittu, henkilölle ei määritetä vuoroa, jos hänellä on päällekkäin tapahtuma joka on joko tyyppiä "Kommentti" tai "Koulutus"
     * **Kommenttien** : Jos tämä on valittu, henkilölle voidaan määrittää vuoro, vaikka hänellä olisi päällekkäin tapahtuma joka on tyyppiä "Kommentti"
     * **Koulutusten** : Jos tämä on valittu, henkilölle voidaan määrittää vuoro, vaikka hänellä olisi päällekkäin tapahtuma joka on tyyppiä "Koulutus"
     * **Kommenttien ja koulutusten** : Jos tämä on valittu, henkilölle voidaan määrittää vuoro vaikka hänellä olisi päällekkäin tapahtuma joka on tyyppiä "Kommentti" tai "Koulutus"
  6. **Tehtävien jako** : Mahdolliset vaihtoehdot ovat "Tehokkain" tai "Tasaisin"
     * **Tehokkain** : Työkalu järjestää vuorotarpeet ja sitten käy ne läpi yksitellen ja järjestää henkilöt sen mukaan, että kuka henkilö on paras tekemään vuoron
       * Henkilön järjestäminen (järjestys niin että listalla ylempi on vertailussa etusijalla alempana oleviin verrattuna)
         * Voi tehdä vuoron kokonaisuudessaan
         * Henkilön projektikoodi täsmää toimipisteeseen
         * Vuoron osuvuus verrattuna ensisijaisiin tehtäviin: Ensimmäisillä vertailukierroksilla tätä ei hyödynnetä koska tehtävät osuvat täsmällisesti. Tätä hyödynnetään vasta viimeisellä vertailukierroksella, jolloin tarkkaa osumaa ensisijaisiin tehtäviin ei ole löytynyt
         * Voi tehdä suurimman osan vuorosta: Jos ei ole löytynyt yhtään henkilöä, joka voi tehdä koko vuoron, haetaan henkilö joka voi tehdä suurimman osan vuorosta
         * Pienin kustannus vaatimusten täyttämiseen
         * Onko kyseessä kokopäiväinen työntekijä: Esimerkiksi henkilö, joka voi tehdä 40 tuntia viikossa ja jolle on jo jaettu 32 tunnin edestä työtä (eli 8 tuntia vielä käytettävissä) valitaan ennen henkilöä joka voi tehdä 8 tuntia viikossa ja jolle ei ole yhtään työtuntia määritettynä. Eli käytännössä kokopäiväiset työntekijät ovat etusijalla vuorojen jakamisessa.
       * Vuorotarpeiden järjestäminen (järjestys niin että listalla ylempi on vertailussa etusijalla alempana oleviin verrattuna)
         * Korkein prioriteetti
         * Vuoro sisältää tehtäviä
         * Kiinteä kesto
         * Alkamis- ja loppumisaika
     * **Tasaisin** : Työkalu järjestää henkilöt ja sitten käy nämä läpi yrittäen lisätä yksittäisen vuoron jokaiselle parhaan osuman mukaan ja tekee sitten uudelleen järjestämisen jakamista varten. Järjestämisprosessi toistetaan, kunnes vuoroja ei ole enää jaettavissa.
       * Henkilön järjestäminen (järjestys niin että listalla ylempi on vertailussa etusijalla alempana oleviin verrattuna)
         * Eniten työtunteja jäljellä
         * Eniten osaamisia
       * Vuorotarpeiden järjestäminen (järjestys niin että listalla ylempi on vertailussa etusijalla alempana oleviin verrattuna)
         * Korkein prioriteetti
         * Vuoro sisältää tehtäviä
         * Kiinteä kesto
         * Alkamis- ja loppumisaika
       * **Huomio** : Jos useat vuorot eivät ole koko päivän pituisia vuoroja ja aktiviteetteja ei ole tarpeeksi täyttämään kaikkien vuoroja, voidaan päätyä tilanteeseen, jossa usealla henkilöllä on osan päivää kestäviä vuoroja.
