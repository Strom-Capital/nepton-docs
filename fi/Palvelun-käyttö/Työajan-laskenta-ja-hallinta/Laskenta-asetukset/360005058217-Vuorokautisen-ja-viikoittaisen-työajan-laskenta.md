---
id: 360005058217
title: Vuorokautisen ja viikoittaisen työajan laskenta
url: https://support.nepton.com/hc/fi/articles/360005058217-Vuorokautisen-ja-viikoittaisen-ty%C3%B6ajan-laskenta
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- Ylityöviikon laskentamallit
- vuorokausiraja
- yleistyöaika
- overtime
- tes
- collective agreement
- daily and weekly working hours
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2025-11-20T11:43:39Z'
---

# Vuorokautisen ja viikoittaisen työajan laskenta

Ylityötä muodostuu työpäiväkohtaisesti, ei tapahtumakohtaisesti, eli kaikki muodostunut ylityö lasketaan yhteen.  
Tämän jälkeen tulkitaan asetusten mukaisesti, onko kyseessä 50% vai 100% ylityö.  
Jos ylityöhön kohdistuu pyöristys, pyöristys muodostuu ajallisesti viimeiseen ylityöjaksoon.  
Poikkeus tähän on Sovittu 100% ylityö, joka pyöristyy itsenäisesti, eikä vaikuta päivän muuhun ylityölaskentaan.
Henkilön vuorokautinen- sekä viikoittainen työaika muodostuu henkilölle liitetyn asetusryhmän sekä henkilön työaikaprosentin perusteella. Käytettävä työpäivän sekä työviikon pituus on nähtävissä **Tapahtumat kalenterissa-** ja **Tapahtumat taulukossa** -näkymässä klikatessa päivämäärää (kuva alla).
![](https://support.nepton.com/hc/article_attachments/20551921841053)![](https://support.nepton.com/hc/article_attachments/20551921847581)
Työaikaa laskiessa henkilölle muodostuu säännöllistä työaikaa niistä työaikakirjauksista, jotka alittavat työpäivän pituuden sekä työviikon pituuden. Tulkinnassa säännöllinen työaika ajoittuu siten, että sitä korvataan asetuksissa olevan työvuorokauden alkuajasta alkaen. Säännöllinen työaika korvataan tämän jälkeisille tapahtumille aikajärjestyksessä. Säännöllisen työajan ajoittumista voidaan ohjata antamalla palveluun [oletetut työajat](<https://support.nepton.com/hc/fi/articles/360002558617>).
Alla mainitut asetukset löytyvät asetuksista kohdasta **Työtunnit** > **TES**.
Säännöllisen työajan ylittävältä osalta laskenta tarkastelee ensin työviikon pituutta. Työaika käsitellään viikoittaisen työajan ylittävänä siltä osin kuin se ylittää asetuksen 'Työviikon pituus työehtosopimuksessa' arvon, mutta kuitenkin alittaa työpäivän pituuden.
Työviikon pituuden ylittävä aika voidaan kohdistaa kertymiin tai maksaa ylityönä. Mikäli työviikon ylittävä aika korvataan ylityönä, niin aika korvataan viikoittaisena lisätyönä asetuksen 'TES enimmäistyöaika viikossa' saakka. Katso tarkempi kuvaus lisätyöstä [täältä](<https://support.nepton.com/hc/fi/articles/360002559438>). Viikoittaisena 50% ylityönä korvataan asetuksen 'TES viikoittaisen 50% ylityön maksimimäärä' saakka. Tämän jälkeen muodostuva viikoittainen ylityö korvataan 100% korotuksella.
Silloin kun viikon enimmäistyöaikaa ei ole saavutettu, voidaan viikoittainen ylityö asettaa muodostuvaksi asetuksella 'Kynnysarvo viikkoylityölle jos ansaittu ennen TES:n päivän maksimipituutta'. Tällöin viikoittaisen työajan ylittävä työ korvataan TES-ylityönä silloin kun kynnysarvon määrä työtä on viikolla ylittynyt. Tässä tapauksessa viikoittaista lisätyötä ei muodostu. Kynnysarvon tulee olla pienempi kuin työviikon pituus työehtosopimuksessa jotta se astuu voimaan. Tätä asetusta voidaan hyödyntää osa-aikaisten ylityön ansainnassa.
Työaika käsitellään vuorokautisen työajan ylittävänä siltä osin kuin se ylittää asetuksen 'työpäivän pituus'. Päivän pituuden ylittävä aika voidaan kohdistaa kertymiin tai maksaa ylityönä. Mikäli työpäivän ylittävä aika korvataan ylityönä, niin aika korvataan vuorokautisena lisätyönä asetuksen 'TES enimmäistyöaika vuorokaudessa' saakka. Katso tarkempi kuvaus lisätyöstä [täältä](<https://support.nepton.com/hc/fi/articles/360002559438>). Vuorokautisena 50% ylityönä korvataan asetuksen 'TES vrk 50% ylityö korvattavat tunnit' saakka. Tämän jälkeen muodostuva vuorokautinen ylityö korvataan 100% korotuksella.
Asetuksella "Viikkoylityön jälkeen ylityö korvataan 100% korotuksella" voidaan määrittää, milloin 100% ylityön tulkinta alkaa. Mikäli asetukseen on määritelty:  
-"Ei", 100% ylityön ansainta menee määritysten mukaan.  
-"Kyllä", alkaa 100% ylityön muodostuminen heti, kun viikkoylityötä on ansaittu ansaitusta määrästä huolimatta. Eli jos keskiviikkona on ansaittu 3h viikko50%, alkaa torstaina jo 100% ylityön ansainta.  
-"TES viikoittaisen 50% ylityön maksimäärän jälkeen", alkaa 100% ylityön muodostuminen sitten, kun viikoittainen 50% ylityön maksimimäärä on saavutettu. Esimerkiksi, jos maksimiksi on määritelty 8h, alkaa 100% ylityön ansainta heti, kun tämä 8h 50% viikkoylityötä on ansaittu.
Silloin kun päivän enimmäistyöaikaa ei ole saavutettu, voidaan vuorokautinen ylityö asettaa muodostuvaksi asetuksella 'Kynnysarvo päiväylityölle jos ansaittu ennen TES:n päivän maksimipituutta'. Tällöin vuorokautisen työajan ylittävä työ korvataan vuorokautisena TES-ylityönä heti kun vuorokaudelta korvattava aika ylittää kynnysarvon. Tässä tapauksessa vuorokautista lisätyötä tai viikkoylityötä ei muodostu. Kynnysarvon tulee olla pienempi kuin työpäivän maksimipituus jotta se astuu voimaan. Tätä asetusta voidaan hyödyntää osa-aikaisten ylityön ansainnassa.
Tapahtumatyyppien korvausta ja niiden huomiointia toteutuneen viikkotyöajan laskennassa voi muuttaa asetuksissa **Työtunnit > TES > Tapahtumatyypit, jotka lasketaan työviikkoon.**
Huom! Oletuksena vain palkalliset tapahtumatyypit lasketaan työviikkoon.
Jos tapahtumatyyppikohtaisia asetuksia ei ole muutettu, seuraavia palkallisia tapahtumatyyppejä ei lasketa työviikkoon:
  * Koulutus
  * Luottamusmiestyö
  * Matka-aika
  * Terveydenhoito
  * Työsuojelutyö


## Työviikon enimmäistyöajan lyhentäminen
Työviikon enimmäistyöaikaa voidaan vähentää silloin kun viikolla on juhlapyhä, tai silloin kun henkilöllä on poissaoloja. Viikon enimmäistyöaikaa vähentävät poissaolot määritellään TES-asetuksissa otsikon 'vähennettävä lisäaika viikon maksimipituudesta poissaolopäivinä' alla.
![](https://support.nepton.com/hc/article_attachments/9860714411293)
Jos esimerkiksi halutaan, että sairausloma lyhentää työviikkoa merkinnän mukaisesti 7 tunnilla ja 30 minuutilla ja lyhentää enimmäistyöaikaa päivältä kokonaisuudessaan 8 tunnilla, asetuksen arvoksi sairausloman osalta annettaisiin 30 minuuttia.
## Työviikon pituuden lyhentäminen arkipyhäviikolla
Arkipyhä voidaan asettaa lyhentämään viikoittaista työaikaa seuraavasti:
  1. Päivittäisen velvoitteen mukaan. Tässä vaihtoehdossa yksi päivä lyhentää työviikkoa enintään 8 tuntia, vaikka päivän pituus olisi pidempi. 
  2. Viikottaisen velvoitteen mukaan. Tässä vaihtoehdossa työviikon pituus jaetaan viidellä. Esimerkiksi 30 tunnin viikkotyöajalla jokainen arkipyhä lyhentää viikkotyöaikaa sekä viikon enimmäistyöaikaa 6 tuntia. Lisäksi TES-asetuksista tulee asetukseen "_Juhlapyhät ja vuosilomat lyhentävät ensin koko viikon_ " määrittää '_Kyllä_ ', jotta juhlapyhän lyhentävä vaikutus käsitellään myös juhlapyhää edeltävinä viikonpäivinä.
  3. Viikottaisen enimmäistyöajan mukaan. Tässä vaihtoehdossa työviikon pituus sekä enimmäistyöaika viikossa jaetaan viidellä. Jos käytössä on esimerkiksi 30 tunnin viikkotyöaika ja 40 tunnin enimmäistyöaika viikossa, niin jokainen arkipyhä lyhentää viikkotyöaikaa 6 tuntia ja enimmäistyöaikaa 8 tuntia.


Lyhennystapa voidaan määritellä työyhteisön tai asetusryhmän asetuksissa kohdassa**Työtunnit - > Juhlapyhät -> Juhlapyhät lyhentävät viikkoa** asetuksella. 
![mceclip1.png](https://support.nepton.com/hc/article_attachments/9491931340189)
Lyhennystavan lisäksi tulee määritellä, miten viikoittaista työaikaa lyhennetään. Lyhennys voi koskea työviikon pituutta (työviikon pituus työehtosopimuksessa) sekä työviikon enimmäistyöaikaa.
![mceclip3.png](https://support.nepton.com/hc/article_attachments/360005839497)
Viikoittainen ylityö korvataan lisätyönä, mikäli työviikon pituus ylittyy, mutta viikon enimmäistyöaika ei ylity. Mikäli työviikon enimmäistyöaikaa ei lyhennetä, maksetaan viikoittainen ylityö lisätyönä enimmäistyöaikaan saakka, jonka jälkeen maksetaan viikoittaista ylityötä. Tarkemmat ohjeet lisätyön määrittelyyn [täällä](<https://support.nepton.com/hc/fi/articles/360002559438>).
## Viikkoylityön muodostuminen ennen viikkotuntien täyttymistä
Työehtosopimuksessa saattaa olla tulkinta, että viikoittaista ylityötä muodostuu jo ennen viikkotuntien täyttymistä. Asetuksella 'kynnysarvo viikkoylityön muodostumiselle' voidaan ohjata, että asetetun työmäärän jälkeen ansaitaan viikkoylityötä riippumatta työviikon pituudesta.
Työehtosopimuksessa saattaa myös olla tulkinta, että tiettyjen tapahtumatyyppien esiintyessä viikolle ei muodostu viikoittaista lisätyötä, vaan vapaapäivänä tehty työ korvataan viikkoylityönä. Asetuksella "Kiinteistöalan toimihenkilöiden TES" > "Tapahtumatyypit, jotka käynnistävät ylityön viikonloppuna" voidaan valita nämä tapahtumatyypit. Tämän lisäksi juhlapyhille, jotka lyhentävät työviikkoa, voidaan valita sama toiminnallisuus.
![](https://support.nepton.com/hc/article_attachments/10067876249501)
Jos TES:n mukaista ylityötä muodostetaan ennen viikkotuntien täyttymistä, voidaan asettaa tämä ylityö erilliseksi viikoittaisesta ylityöstä asetuksella 'Viikoittaisesta ylityöstä erillisenä ansaittu TES:n mukainen ylityö'. Tällöin TES:n mukainen ylityö lasketaan erikseen viikoittaisesta ylityöstä, ja on mahdollista ansaita ensin TES:n mukaista ylityötä viikon kynnykseen asti sekä vastaavasti viikoittaista ylityötä.
Kun 'Viikoittaisesta ylityöstä erillisenä ansaittu TES:n mukainen ylityö' on asetettu arvoon kyllä ja viikolla on poissolopäiviä, jotka käynnistävät ylityön viikonloppuna kiinteistöjen TES-sääntöjen mukaisesti, viikonloppuna laskettaisiin ylitöitä seuraavasti:
![](https://support.nepton.com/hc/article_attachments/10022820353821)
## Työpäivän/työviikon pituus ja enimmäistyöika
Tulkinnassa työpäivän tai työviikon pituus katsotaan täytetyksi kun enimmäistyöaika on täytetty, vaikka työpäivän tai työviikon pituus ei olisi vielä täytettynä. Tämän jälkeen työaika tulkitaan ylityöksi.
Jos työpäivän/työviikon enimmäistyöaika on asetuksissa lyhyempi kuin työpäivän/työviikon pituus, enimmäistyöaika kasvatetaan täsmäämään työpäivän/työviikon pituutta.
## Asetus 'Tunti tunnista -ylityö lasketaan viikkovelvoitteiseen työaikaan'
Oletuksena tunti tunnista -ylityötunteja ei lasketa viikkovelvoitteseen työaikaan.
Asetuksella ei ole merkitystä tapahtumatyypeille, joilta ei voi ansaita viikkovelvoitteisia työtunteja. 
Asetuksella voi tarvittaessa määrittää, että ne säännöllisen työajan ylittävät tunnit, jotka korvataan tunti tunnista, lasketaan viikkovelvoitteiseen työaikaan jollain seuraavista tavoista:  
\- Viikon työaikaan ja enimmäistyöaikaan  
\- Vain viikon työaikaan  
\- Vain viikon enimmäistyöaikaan  
\- Vain päivillä joilla ei ole työvelvoitetta (tällä asetuksella tunti tunnista tulkittu aika huomioidaan vain enimmäistyöajassa)
![](https://support.nepton.com/hc/article_attachments/31936618420125)
Viikon työaika ja viikon enimmäistyöaika määritellään TES-osiossa seuraaviin asetuksiin:
![](https://support.nepton.com/hc/article_attachments/31936618421789)
