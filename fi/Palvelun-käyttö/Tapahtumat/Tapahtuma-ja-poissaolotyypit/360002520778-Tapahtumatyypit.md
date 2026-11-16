---
id: 360002520778
title: Tapahtumatyypit
url: https://support.nepton.com/hc/fi/articles/360002520778-Tapahtumatyypit
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtuma- ja poissaolotyypit
section_id: 360005841257
section_path:
- Tapahtumat
- Tapahtuma- ja poissaolotyypit
labels:
- tapahtumatyyppi
- hälytys
- syykoodi
- publicholidaysforusers
- hälytystyölisä
- ulkomaanpäiväraha
- leimauslaji
- notifikaatio
- kertymä
- hälytysraha
- sairausloma
- lisätiedot
- lisätieto
promoted: false
updated_at: '2026-08-18T09:54:40Z'
edited_at: '2026-08-18T09:54:39Z'
---

# Tapahtumatyypit

Palvelussa on käytössä useita erilaisia tapahtumatyyppejä, joita käytetään tapahtumien kirjaamiseen. Ohessa on lista palvelussa vakiona käytettävissä olevista tapahtumatyypeistä. Tapahtumatyypin nimen perässä sulkeissa oleva numero on tapahtumatyypin koodi (activitytypecode), jota voidaan käyttää [poikkeusasetuksissa](<https://support.nepton.com/hc/fi/articles/360002560677>) sekä [poimintasäännöissä](<https://support.nepton.com/hc/fi/articles/360002489257>). Tapahtumatyypin koodi näkyy myös tapahtumatyyppilistauksissa työyhteisön ja asetusryhmien asetuksissa.
[Tässä](<https://support.nepton.com/hc/fi/articles/360002519157>) tukisivustomme artikkelissa lisää Tapahtumatyyppien lisäämisestä, käyttöönotosta ja muokkaamisesta.
Palvelussa on käytössä myös poissaolotyyppejä. Poissaolotyypeillä tarkoitetaan tapahtumatyypin 'Poissaolo' tarkennetta. Tarkemman kuvauksen poissaolotyypeistä löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002519937>).
Käytettävissä olevat tapahtumatyypit voivat vaihdella ympäristöittäin, sillä ne ovat räätälöitävissä. Tehdyt kirjaukset säilyvät palvelussa, vaikka tapahtumatyyppi poistettaisiin myöhemmin käytöstä.
## Työ-tapahtumatyypit
**Työ (1)**  
Työ-tapahtumatyyppi kartuttaa työtunteja merkinnän aloitusajan ja lopetusajan välisen tuntimäärän.
Säännöllistä työaikaa ansaitaan päivän työvelvoitteeseen saakka, jos päivän työvelvoite on määritelty. Ylimenevä osa kerryttää esim. saldoa tai muodostaa lisä-/ylitöitä. Velvoitetta lyhyemmät päivät vähentävät työaikasaldoa automaattisesti, mikäli saldolaskenta on käytössä.
Kertyviä työtunteja voidaan rajoittaa työaikarajoilla. Automaattisesti vähennetty palkaton ruokatunti vähentää asetetun mukaisesti työtunteja.
**Etätyö (84)**  
Etätyö-tapahtumatyyppi käyttäytyy muutoin kuten Työ-tapahtumatyyppi mutta sillä voi ansaita ylityötä vain tunti tunnista, ei muita ylityön kohdenteita. Ainoa tapa, jolla voidaan lisätä toinen ylityön kohdenne, on määritellä työyhteisö-/asetusryhmätasolta tapahtumatyypille poikkeava ylityön oletuskohdenne. Tällöin tätä kohdennetta tarjotaan aina oletuksena Etätyössä uutta tapahtumaa luodessa.
Mikäli halutaan käyttöön Etätyö-tapahtumatyyppi, johon voi määritellä useampia ylityön kohdenteita, tulee Työyhteisötasolla luoda kokonaan uusi Etätyö-tapahtumatyyppi, asettaa se käyttäytymään kuten työ ja määritellä sille halutut ylityön kohdenteet.
**Hälytystyö (239)**  
Hälytystyö-tapahtumatyyppi on aina vuorokautista ylityötä ja se noudattaa asetettuja ylityöasetuksia, esim. vuorokautisen 50% ylityön rajaa. Hälytystyötä ansaitaan aina vähintään yksi tunti. Hälytystyö ei kerrytä säännöllisen työajan tunteja. Vuosilomapäivinä hälytystyöstä ansaitaan aina 100% korvaus.
**Kokous (31)**  
Kokous-tapahtumatyyppi käyttäytyy kuten Työ-tapahtumatyyppi. Tätä tapahtumatyyppiä käytetään, kun halutaan erottaa kokouksiin käytetty työaika muusta tehdystä työstä. Tapahtumatyyppi kerryttää työntekotunteja koko leimauksen kestolta.
**Koulutus (25)**  
Koulutus-tapahtumatyyppi käyttäytyy kuten Työ-tapahtumatyyppi. Tätä tapahtumatyyppiä käytetään, kun halutaan erottaa koulutuksiin käytetty työaika muusta tehdystä työstä. Tapahtumatyyppi kerryttää työntekotunteja koko leimauksen kestolta. Palvelun käyttöönoton yhteydessä asetetaan Koulutus-tapahtumatyypin käyttäytyminen oletusarvoisesti niin, ettei sitä lasketa mukaan työviikkoon, eikä se tällöin vaikuta viikoittaisen ylityön muodostumiseen. Asetusta voi muuttaa kohdassa Työtunnit -> TES -> Tapahtumatyypit, jotka lasketaan työviikkoon.
**Leirityö (271)**  
Lue lisää leirityöstä [täältä.](<https://support.nepton.com/hc/fi/articles/360017272298>)
**Luottamusmiestyö (5)**  
Palvelun käyttöönoton yhteydessä asetetaan Luottamusmiestyö-tapahtumatyypin käyttäytyminen oletusarvoisesti niin, ettei sitä lasketa mukaan työviikkoon, eikä se tällöin vaikuta viikoittaisen ylityön muodostumiseen. Asetusta voi muuttaa kohdassa Työtunnit -> TES -> Tapahtumatyypit, jotka lasketaan työviikkoon.  
Luottamusmiestyö-tyyppiseen tapahtumaan kirjattuja huomautuksia ei näytetä vuorosuunnittelussa.
**Matka-aika (26)**  
Matka-aika -tapahtumatyypistä ei oletuksena ansaita ylitöitä eikä saldoja. Merkinnän alku- ja loppuajan välinen aika lasketaan omalle rivilleen kalenterinäkymässä. Matka-aikatunneilla täydennetään päivän työtunnit työvelvoitteeseen saakka, mikäli velvoite jäisi vajaaksi muilla työtunteja kartuttavilla merkinnöillä. Palvelun käyttöönoton yhteydessä asetetaan matka-aika -tapahtumatyypin käyttäytyminen oletusarvoisesti niin, ettei sitä lasketa mukaan työviikkoon, eikä se tällöin vaikuta viikoittaisen ylityön muodostumiseen. Asetusta voi muuttaa kohdassa Työtunnit -> TES -> Tapahtumatyypit, jotka lasketaan työviikkoon.
**Matkalasku (27)**  
Matkalaskulla voidaan merkitä matkan alku- ja päättymisajat, kilometrikorvaukset, päivärahat sekä muut mahdolliset kulut. Ulkomaan päivärahan kohdalla kohdemaa voidaan merkitä kommenttiin. Matkalasku voidaan myös kohdentaa projektille. Matkalaskulla voi luoda matka-aikaa vastaavan Matka-aika-tapahtuman. Mikäli matka kerryttää normaaleja työtunteja, tehdään kalenteriin vastaavasti työleimaus.
**Ruokailu (15)**  
Ruokailu-tapahtumatyyppi on käytössä ainoastaan Ruokala-päätteen kanssa. Leimattaessa ruokailutapahtumia päätteellä, muodostuu kalenteriin Ruokailu-tapahtuma ja siihen työlisinä leimatut ruokailutapahtumat.
**Ruokatauko (6)**  
Ruokatauko voi olla palkaton tai palkallinen. Palkallinen ruokatauko kerryttää työtunteja ja palkaton ei. Palkallisella ruokatauolla voidaan asettaa kesto, jonka ylittävä aika on palkatonta. Ruokatauon asetuksista on oma [ohje](<https://support.nepton.com/hc/fi/articles/360002558757>).
**Tauko (28)**  
Tauko-tapahtumatyypillä voidaan merkitä palkalliset virvoketauot ja vastaavat. Merkityt tauot kerryttävät työntekotunteja koko leimauksen kestolta.
**Terveydenhoito (17)**  
Terveydenhoito-tapahtumatyyppi käyttäytyy kuin Työ-tapahtumatyyppi. Terveydenhoito-tapahtumatyyppiä käytetään, kun kyseessä on työaikaan kuuluva terveysasia, kuten työterveystarkastus. Palvelun käyttöönoton yhteydessä asetetaan Terveydenhoito-tapahtumatyypin käyttäytyminen oletusarvoisesti niin, ettei sitä lasketa mukaan työviikkoon, eikä se tällöin vaikuta viikoittaisen ylityön muodostumiseen. Asetusta voi muuttaa kohdassa Työtunnit -> TES -> Tapahtumatyypit, jotka lasketaan työviikkoon.  
Terveydenhoito-tyyppiseen tapahtumaan kirjattuja huomautuksia ei näytetä vuorosuunnittelussa.
**Työ muualla** **(18)**  
Työ muualla -tapahtumatyyppi käyttäytyy kuten Työ-tapahtumatyyppi. Tätä tapahtumatyyppiä voidaan käyttää, kun halutaan erottaa työpaikalla tehty työ muualla tehdystä työstä.
**Työlisä (165)**  
Työlisä-tapahtumatyypin voi kirjata erikseen ja se ei kerrytä tehtyä työaikaa. Tällä tapahtumatyypillä voi kirjata esimerkiksi työolosuhteisiin liittyviä lisiä, kuten likaisen työn lisän.
**Työsuojelutyö (14)**  
Palvelun käyttöönoton yhteydessä asetetaan Työsuojelutyö-tapahtumatyypin käyttäytyminen oletusarvoisesti niin, ettei sitä lasketa mukaan työviikkoon, eikä se tällöin vaikuta viikoittaisen ylityön muodostumiseen. Asetusta voi muuttaa kohdassa Työtunnit -> TES -> Tapahtumatyypit, jotka lasketaan työviikkoon.  
Työsuojelutyö-tyyppiseen tapahtumaan kirjattuja huomautuksia ei näytetä vuorosuunnittelussa.
**Varallaolo (33)**  
Varallaolo-tapahtumatyypillä merkitään varallaoloon käytetty aika. Varallaolo ei kerrytä työtunteja. Lisätietoja Varallaolon käytöstä [täältä](<https://support.nepton.com/hc/fi/articles/8040695057821>).
## Ylityö-tapahtumatyypit
Palvelussa ei ole oletuksena yhtään tähän kategoriaan kuuluvaa tapahtumatyyppiä. Lisättäessä asiakaskohtaista tapahtumatyyppiä se voidaan määrittää käyttäytymään seuraavilla tavoilla.
**Sovittu lisä- / ylityö**  
Tapahtumatyyppi, joka käyttäytyy kuin sovittu lisä- / ylityö ei muodosta säännöllistä työaikaa. Työaika tulkitaan vuorokautisena ylityönä, jos henkilön tekemä työ ylittää asetetun vuorokautisen enimmäistyöajan. Jos henkilön tekemä työ alittaa asetetun vuorokautisen enimmäistyöajan niin ylityö muodostuu ensin lisätyönä, sitten viikoittaisena ylityönä. Kun vuorokautinen enimmäistyöaika on saavutettu, muodostuu ylityö vuorokautisena ylityönä.
Tapahtumatyyppi pyöristyy muiden ylityötapahtumien kanssa ylityöpyöristyssääntöjen mukaan.
**Sovittu ylityö**  
Tapahtumatyyppi, joka käyttäytyy kuin sovittu ylityö ei muodosta säännöllistä työaikaa. Työaika tulkitaan vuorokautiseksi ylityöksi niin kauan, kunnes TES enimmäistyöaika viikossa täyttyy. Tämän jälkeen muodostuu viikoittaista ylityötä.
Tapahtumatyyppi pyöristyy muiden ylityötapahtumien kanssa ylityöpyöristyssääntöjen mukaan.
**Sovittu 100% ylityö**  
Tapahtumatyyppi, joka käyttäytyy kuin sovittu 100% ylityö ei muodosta säännöllistä työaikaa. Työaika tulkitaan aina 100% ylityönä, eikä se vaikuta muun vuorokautisen ylityön laskentaan. Työaika tulkitaan vuorokautisena ylityönä, jos henkilön tekemä työ ylittää asetetun vuorokautisen enimmäistyöajan. Jos henkilön tekemä työ alittaa asetetun vuorokautisen enimmäistyöajan niin ylityö muodostuu viikoittaisena ylityönä.
Tapahtumatyyppi pyöristyy itsenäisesti, muista ylityötapahtumista riippumatta, ylityöpyöristyssääntöjen mukaan.
## Poissaolo-tapahtumatyypit
Kaikkien poissaolotyyppien tapahtumat näytetään vuorosuunnittelussa nimellä "Poissaolo" ilman mahdollisia huomautuksia. Huomioithan, että poissaolo-tapahtumatyypit ja poissaolotyypit tarkoittavat Neptonissa eri asioita. Voit lukea lisää poissaolotyypeistä erillisestä ohjeartikkelista [täältä](<https://support.nepton.com/hc/fi/articles/360002519937-Poissaolotyypit>). Alla luettelo tapahtumatyypeistä, joiden käyttäytyminen Neptonissa on kuin poissaolo. 
**Joustotyötuntivapaa (2291)**  
Joustotyötuntivapaa-tapahtumatyyppiä käytetään, kun halutaan pitää ansaittuja Joustotyötunti-kertymään kertyneitä tunteja vapaana. Tapahtumatyyppi antaa maksimissaan työpäivän pituuden verran säännöllistä työaikaa ja Joustotyötunti-kertymän saldo pienenee saman verran.
**Joustovapaa (1049)**  
Joustotyövapaa-tapahtumatyyppiä käytetään, kun halutaan pitää ansaittuja Joustotyö-kertymään kertyneitä tunteja vapaana. Tapahtumatyyppi antaa maksimissaan työpäivän pituuden verran säännöllistä työaikaa ja Joustovapaa-kertymän saldo pienenee saman verran.
**Juhlapyhä (7)**  
Kalenteriin tuodaan automaattisesti yleisimmät juhlapyhät. Juhlapyhien näkyvyyttä ja laskentatapaa hallinnoidaan tarpeen mukaan joko työyhteisön tai asetusryhmien asetuksissa. Juhlapyhä-tapahtumatyypillä tarkoitetaan palkallista vapaapäivää. Se ei kerrytä tai vähennä saldotunteja. Tapahtumatyypillä voidaan säädellä juhlapyhänä ansaittavia korotuksia ja lisiä.
**Lomarahavapaa (164)**  
Lomarahavapaa-tapahtumatyyppiä käytetään, kun halutaan muuttaa lomarahat vapaiksi. Tapahtumatyyppi antaa maksimissaan työpäivän pituuden verran säännöllistä työaikaa. Jos halutaan sen käyttäytyvän kuten vuosiloma, täytyy perustaa uusi tapahtumatyyppi, esim. Lomarahavapaa (VL), joka käyttäytyy kuten vuosiloma.
**Lomautus (23)**  
Lomautus-tapahtumatyyppi käyttäytyy kuten poissaolo. Se täyttää puuttuvan työvelvoitteen työpäivän pituuteen saakka, mutta ei kerrytä ylityötä eikä saldoa tai muita kertymiä. Lomautus tapahtumatyypin korvauksen oletuksena on "Palkaton". Esimerkkejä erilaisista [Lomautus-tapahtumatyyppien käytöstä](<https://support.nepton.com/hc/fi/articles/360009227298>).
**Pankkivapaa (102)**  
Pankkivapaa-tapahtumatyyppiä käytetään, kun halutaan pitää ansaittuja Pankki-kertymään kertyneitä tunteja vapaana. Tapahtumatyyppi antaa maksimissaan työpäivän pituuden verran säännöllistä työaikaa ja Pankki-kertymän saldo pienenee saman verran.
**Poissaolo (4)**  
Poissaolo-tapahtuma voidaan merkitä palkalliseksi tai palkattomaksi tai osittain korvattavaksi. Merkintätyyppi ei kasvata eikä vähennä saldoa. Merkinnässä voidaan valita erilaisia poissaolon tyyppejä. Merkinnässä voidaan valita myös kerryttääkö poissaolo vuosilomapäiviä. Poissaolotyyppien hallinnasta on erillinen [ohje](<https://support.nepton.com/hc/fi/articles/360002519937>).
**Sairauspoissaolo (2)**  
Sairauspoissaolo-tapahtumatyypillä merkitään sairauspoissaolot. Sairauspoissaoloon voidaan merkitä onko lääkärintodistus vastaanotettu ja onko poissaolo palkallista, palkatonta tai osittain korvattavaa. Sairauspoissaolosta voidaan myös valita kerryttääkö se vuosilomaa vai ei. Oletuksena palvelussa on valmiina valittavissa [Sairausloman lisätieto-kenttään](<https://support.nepton.com/hc/fi/articles/33334659658525-Poissaolojen-kirjaaminen#h_01KFMQ0W4VZ7PVPANS0WK9H9VE>), onko kyseessä Sairas, Lapsi sairas, Työtapatuma, Työmatkatapaturma vaiko Vapaa-ajan tapaturma. Sairauspoissaolo kerryttää työtunteja ja säännöllistä työaikaa työpäivän pituuteen saakka eikä se kerrytä työtuntisaldoa.
**Saldovapaa (16)**  
Saldovapaa-tapahtumatyyppiä käytetään, kun halutaan pitää ansaittuja työtuntisaldoja tai työaikapankista nostettuja saldoja. Tapahtumatyyppi antaa maksimissaan työpäivän pituuden verran säännöllistä työaikaa ja Saldo-kertymän saldo pienenee saman verran.
**Tasoittumisjaksotuntivapaa (2294)**  
Tasoittumisjaksotuntivapaa-tapahtumatyyppiä käytetään, kun halutaan pitää ansaittuja Tasoittumisjaksotunti-kertymään kertyneitä tunteja vapaana. Tapahtumatyyppi antaa maksimissaan työpäivän pituuden verran säännöllistä työaikaa ja Tasoittumisjaksotunti-kertymän saldo pienenee saman verran.
**Työajanlyhennysvapaa (29)**  
Työajanlyhennysvapaa-tapahtumatyypillä merkitään ns. pekkaspäiviä, joilla tasoitetaan vuositasolla 40 h työviikko 37,5 h työviikon mittaiseksi. Tapahtumatyyppi antaa maksimissaan työpäivän pituuden verran säännöllistä työaikaa ja Työajanlyhennysvapaa-saldo pienenee saman verran.
**Viikkovapaa (287)**  
Viikkovapaa-tapahtumalla tallennetaan suunnitellut vapaapäivät. Viikkovapaa-tapahtumatyyppi ei muodosta palkkatulkintaa. Se estää kaikkien kertymien vähenemisen kyseisenä päivänä, mutta ei kuitenkaan täytä viikoittaista säännöllistä työaikaa.
**Vuosiloma (3)**  
Vuosiloma-tapahtumatyypilöl merkitään vuosilomapäivät. Merkintä tehdään yhtenäisenä koko vuosilomajaksolle. Merkintä alkaa vuosiloman ensimmäisenä arkipäivänä ja päättyy vuosiloman viimeiseen sunnuntaihin. Tällöin ohjelma huomioi lauantait laskennassa (pois lukien pääsiäislauantai, Vuosilomalaki 4§) ja jättää sunnuntait huomioimatta. Mikäli vuosilomapäivälle merkitään työtä, jätetään kyseinen päivä huomioimatta vuosilomalaskennassa.
**Vuosivapaa (290)**  
Vuosivapaa-tapahtumatyyppiä käytetään, kun halutaan pitää ansaittuja Vuosivapaasaldoja. Tapahtumatyyppi antaa maksimissaan työpäivän pituuden verran säännöllistä työaikaa ja Vuosivapaasaldo pienenee saman verran.
**Ylityövapaa (278)**  
Ylityövapaa-tapahtumatyyppiä käytetään, kun halutaan pitää ansaittuja Ylityövapaa-kertymään kertyneitä tunteja vapaana. Tapahtumatyyppi antaa maksimissaan työpäivän pituuden verran säännöllistä työaikaa ja Ylityövapaa-kertymän saldo pienenee saman verran.
## Hallinnolliset-tapahtumatyypit
Halinnolliset tapahtumatyypit näkyvät vain pääkäyttäjille.
Kertymiä voidaan hallita asettamalla niille arvo tai muuttamalla arvoa. Kertymien asetus ja muutos voidaan tehdä mille tahansa päivälle.
Asetus mitätöi kaikki aiemmat tapahtumat ja asettaa kertymälle tietyn arvon tiettynä päivänä. Laskentaa jatketaan ko. päivästä alkaen pohja-arvona asetettu arvo. Esim. 31.3. Saldon asetus 10h33min. Saldon asetusta käytetään yleensä palvelun käyttöönoton yhteydessä.
Muutos muuttaa kertymän arvoa halutun määrän haluttuna päivänä. Esim. Saldon muutos 31.3. +3h27min lisää saldon arvoa päivän lopuksi. Tätä voi käyttää tarvittaessa manuaalisiin korjauksiin.
Poikkeuksena edellä mainittuihin on Vuosilomaan liittyvät asetukset ja muutokset. Vuosiloman asetuksissa/muutoksissa on syytä huomata, mihin ansaintajaksoon ko. asetus/muutos vaikuttaa. Esim. 15.5.2026 tehty muutos vaikuttaa ansaintajaksolle 1.4.2026-31.3.2027.
Vuosiloman ansainnan asetus voidaan tehdä vain kuukauden ensimmäiselle päivälle. Vuosiloman ansaintamuutos voidaan tehdä mille tahansa päivälle. Vuosilomasaldon lukitus asetetaan jaksolle alkupäivä-loppupäivä. Tyypillisesti jakso on maaliskuu.
**Jouston arvon asetus (1308)**
**Jouston arvon muutos (1309)**
**Joustotyötuntien arvon asetus (2292)**
**Joustotyötuntien arvon muutos (2293)**
**Lomarahavapaan asetus (500796)**
**Lomarahavapaan muutos (500191)**
**Pankin arvon asetus (103)**
**Pankin muutos (104)**
**Saldon asetus (12)**
**Saldon muutos (13)**
**Tasoittumisjaksotuntien arvon asetus (2295)**
**Tasoittumisjaksotuntien arvon muutos (2296)**
**Työajan lyhennysvapaan asetus (1435)**
**Työajan lyhennysvapaan muutos (30)**
**Vuosiloman ansainnan asetus (9)**
**Vuosilomasaldon lukitus (19)**
**Vuosiloman ansaintamuutos (10)**
**Vuosivapaan asetus (1437)**
**Vuosivapaan muutos (1438)**
**Ylityösaldon asetus (279)**
**Ylityösaldon muutos (280)**
Perustamalla oman kertymän, muodostuu sille myös omat hallinnolliset tapahtumatyypit.
## Muut tapahtumatyypit
**Huomautus (8)**  
Huomautus-tapahtumatyypillä voidaan tehdä erillinen kommentti, jolle voidaan asettaa alku- ja loppuaika. Huomautus-tapahtumatyyppi ei vaikuta laskentaan, eikä se kerrytä työtunteja.
**Korjaus (228)**  
[Korjaus-tapahtumatyyppiä](<https://support.nepton.com/hc/fi/articles/38338011820957>) käytetään yhdessä korjaus-työlisien kanssa. Siten voidaan korjata manuaalisesti tapahtumien tulkintaa ja siirtää korjauksia palkkaintegraatiossa palkanlaskentaan.
**Viikkolepokorvauksen siirto (500853)**  
Tapahtumatyypillä voidaan [ohjata yksittäinen viikkolepokorvaus](<https://support.nepton.com/hc/fi/articles/360007389978>) johonkin muuhun kuin oletuskohdenteeseen. Tapahtumatyyppiä voi kirjata kaikki henkilöt, joilla on [oikeus lisätä ja muokata tapahtumia](<https://support.nepton.com/hc/fi/articles/360002554338>).
**Suunniteltu työvuoro (24)**  
Käytössä ainoastaan Vuorosuunnittelu-osiossa.
**Virheellinen tapahtuma (32)**  
Tätä tapahtumatyyppiä käytetään ilmoittamaan henkilölle tai esimiehelle, että järjestelmä ei hyväksynyt työaikapäätteeltä tulevaa kirjausta. Tämä tapahtumatyyppi näytetään poikkeuksellisena merkintänä kalenterinäkymässä ja poikkeuksellisten kirjausten reportilla. Tätä tapahtumatyyppiä ei ole mahdollista lisätä itse, mutta se on mahdollista poistaa. Tämä tapahtumatyyppi ei vaikuta työajan määrään. tapahtuman huomautustekstissä näkyy päätteeltä vastaanotetut tiedot esim. kirjatun tapahtuman tyyppi, kirjauksen aika/päivä ja projekti. Yleensä näissä tilanteissa työaikapääte on ollut ilman verkkoyhteyttä ja päätteen sisäinen kello on nollautunut tai asetettu väärään aikaan, minkä seurauksena pääte on tallentanut offline-tilan aikana tehdyt merkinnät väärälle ajankohdalle. Järjestelmä normaalisti hyväksyy päätteen lähettämät menneet offline kirjaukset, mutta mikäli kirjauksen aika on liian kaukana nykyhetkestä järjestelmä kirjaa tämän virhetapahtuman.
