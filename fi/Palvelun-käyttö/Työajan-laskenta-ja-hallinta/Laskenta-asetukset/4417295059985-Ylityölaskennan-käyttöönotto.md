---
id: 4417295059985
title: Ylityölaskennan käyttöönotto
url: https://support.nepton.com/hc/fi/articles/4417295059985-Ylity%C3%B6laskennan-k%C3%A4ytt%C3%B6%C3%B6notto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- vrk-ylityö
- ylityöleikkuri
- ylityöohje
promoted: false
updated_at: '2026-04-17T10:38:17Z'
edited_at: '2026-04-17T10:38:16Z'
---

# Ylityölaskennan käyttöönotto

Ylityön laskentaan palvelussa vaikuttaa lukuisa määrä asetuksia ja niitä voidaan vielä hienosäätää poikkeusasetuksilla.
Ohjeet perusasetusten tekemiseksi työpäivän - ja työviikon pituuksille löytyvät artikkeleista [Työpäivän pituuden määrittäminen](<https://support.nepton.com/hc/fi/articles/360002558417>) ja [Työviikon pituuden määrittäminen.](<https://support.nepton.com/hc/fi/articles/360002558537>)
Tässä artikkelissa kuvataan tärkeimmät ylityölaskentaan vaikuttavat asetukset ja ne löytyvät Työyhteisön - tai Asetusryhmän asetuksista kohdasta **Työtunnit >TES**, ellei toisin mainita.
## TES enimmäistyöaika
TES enimmäistyöaika määrittää ylityörajan sekä vuorokautiselle että viikoittaiselle ylityölle.
Tarkemmin lisätyön laskennasta artikkelissa [Lisätyön muodostuminen](<https://support.nepton.com/hc/fi/articles/360002559438>) ja ylityön laskennasta artikkelissa [Vuorokautisen ja viikoittaisen työajan laskenta](<https://support.nepton.com/hc/fi/articles/360005058217>)
### TES enimmäistyöaika vuorokaudessa
Asetus tehdään kaikille viikonpäiville erikseen.
Työpäivän pituuden ja vuorokautisen enimmäistyöajan välinen aika on oletuksena lisätyötä, jos muilla asetuksilla ei ole määritetty vuorokautisen lisätyön määrän rajoituksia.
Työpäivän työtuntien ylittäessä vuorokautisen enimmäistyöajan, alkaa muodostua vuorokautista ylityötä. Jos ei haluta, että vuorokautista ylityötä muodostuu lainkaan esim. viikonloppuisin, vaan ainoastaan viikkoylityötä, niin lauantain ja sunnuntain TES enimmäistyöajaksi vuorokaudessa asetetaan 24:00.
![](https://support.nepton.com/hc/article_attachments/35369680374301)
### TES enimmäistyöaika viikossa
Työviikon pituuden ja enimmäistyöajan viikossa välinen aika on oletuksena lisätyötä, ellei muilla asetuksilla ole määritetty viikoittaisen lisätyön määrän rajoituksia.
Työviikon työtuntien ylittäessä viikoittaisen enimmäistyöajan, alkaa muodostua viikoittaista ylityötä.
![](https://support.nepton.com/hc/article_attachments/33384265472925)
## Vuorokautinen ylityö (Vrk-ylityötunnit)
![](https://support.nepton.com/hc/article_attachments/35369648621213)
**Suurin sallittu määrä lisätyötä päivässä**  
Voidaan asettaa enimmäismäärä lisätyön ansainnalle päivässä. Tällä voi olla merkitystä esim. arkipyhäviikolla tai jos viikolla on sairaus- tai muita poissaoloja.
**TES vrk 50% ylityö korvattavat tunnit**  
Työaikalain mukaan kahdelta ensimmäiseltä vuorokautiselta ylityötunnilta tulee maksaa 50% korotettu palkka, jonka jälkeisiltä tunneilta maksetaan 100% korotettu palkka. Tämä on myös palvelun oletusasetus.
TES:ssä voi olla tästä poikkeavia määräyksiä.
**Viikkoylityön jälkeen ylityö korvataan 100% korotuksella**  
Kun päivän aikana on ansaittu viikkoylityötä, ja TES enimmäistyöaika vuorokaudessa ylitetään, korvataan vuorokautinen ylityö 50%:n sijaan 100%:na. TES:ssä voi olla määräys, että tällaisessa tapauksessa ansaitaan 100% korotettua palkkaa.
Asetukseen on myös mahdollista asettaa, että 100% korotettua palkkaa ansaitaan vasta TES viikottaisen 50% ylityön maksimimäärän jälkeen.
![](https://support.nepton.com/hc/article_attachments/35369680377885)
**Laske sovittu ylityö TES enimmäistyöaikaan vuorokaudessa**  
Koskee tilanteita, joissa kirjataan tapahtumatyyppiä, joka käyttäytyy kuin Sovittu ylityö. Tällaista ei ole oletuksena palvelussa, mutta voidaan luoda uusi tapahtumatyyppi, joka käyttäytyy kuin Sovittu ylityö.
Esimerkiksi työpäivän pituus on 7h30min ja TES enimmäistyöaika vuorokaudessa on 8h. Kun työ-tapahtumatyypillä on kirjattu 7h30min ja Sovittu ylityö -tapahtumatyypillä 30min, katsotaan työpäivän enimmäispituus täytetyksi, kun tämä asetus on 'Kyllä'.
## Viikkoylityö
![](https://support.nepton.com/hc/article_attachments/35369680381469)
**Suurin sallittu määrä lisätyötä viikossa**  
Voidaan asettaa enimmäismäärä lisätyön ansainnalle viikossa. Tällä voi olla merkitystä esim. arkipyhäviikolla tai jos viikolla on sairaus- tai muita poissaoloja. Kun raja ylitetään, ansaitaan lisätyön sijaan viikkoylityötä.
**TES viikottaisen 50% ylityön maksimimäärä**  
Työaikalain mukaan viikottaisesta ylityöstä tulee maksaa 50% korotettu palkka. TES:ssä voi olla tästä poikkeavia määräyksiä. Asetukseen voidaan määrittää maksimimäärä 50% viikkoylityön ansainnalle viikossa.
**TES viikottaisen 50% ylityön maksimimäärä päivässä**  
Asetukseen voidaan asettaa päivittäinen enimmäismäärä viikottaiselle 50% ylityölle.
**Viikkoylityötä ansaitaan päiviltä joilla ei ole vuoroa / työvelvoitetta**  
Jos päivälle ei ole määritetty työpäivän pituutta tai päivälle ei ole suunniteltua työvuoroa, ansaitaan päivän työtunneista viikkoylityötä. Mikäli arvoksi valitaan 'Kyllä' niin vapaapäivänä tehty työ on aina viikkoylityötä, eikä siitä muodostu lisätyötä.
**Viikkoylityö juhlapyhinä jotka lyhentävät työviikkoa lasketaan ylityörajoihin**  
Asetuksella otetaan kantaa siihen, huomioidaanko juhlapyhinä tehty viikkoylityö myöhemmin viikolla tehdyn viikkoylityön määrässä.
Esimerkikisi jos on tehty kuusi tuntia 50% viikkoylityötä juhlapyhänä ja TES viikottaisen 50% ylityön maksimimäärä on kahdeksan tuntia, onko jäljellä enää kaksi tuntia 50% viikkoylityötä, jonka jälkeen ansaitaan 100% viikkoylityötä.
**Päivittäinen korotettu lisätyö lasketaan mukaan korotetun lisätyön viikoittaiseen työaikarajaan**  
0% lisätyö vaikuttaa aina viikkotuntirajaan, joka on asetettu kohdassa ”Lisätyön korotusprosentti – Ansaitse viikkotuntien jälkeen”. Tällä asetuksella voidaan määrittää, vaikuttaako myös korotettu (esim. 50%) lisätyö kyseiseen viikkotuntirajaan. Alla olevassa esimerkissä on käytetty seuraavia korotetun lisätyön asetuksia.  
![](https://support.nepton.com/hc/article_attachments/35369648622749)  
![](Skip,%20since%20insertion%20is%20handled%20via%20gallery)  
Asetuksen arvo ”Ei” tai ”Ei asetettu”. Lisätyötä on tehtävä lauantaina 5 tuntia ja 30 minuuttia ennen kuin korotetun lisätyön viikkotuntimäärä on täynnä. Neljän edellisen päivän aikana on tehty töitä yhteensä 32 tuntia ja 30 minuuttia, joista 2 tuntia 0% lisätyötä ja 30 minuuttia 50% lisätyötä. 50% lisätyö ei vaikuta korotetun lisätyön viikkotuntimäärään, joten 37 tunnin ja 30 minuutin rajaan on vielä 5 tuntia ja 30 minuuttia.  
  
![](https://support.nepton.com/hc/article_attachments/35369680383261)  
  
Asetuksen arvo ”Kyllä”. Lisätyötä on tehtävä lauantaina 5 tuntia ennen kuin korotetun lisätyön viikkotuntimäärä on täynnä. Neljän edellisen päivän aikana on tehty töitä yhteensä 32 tuntia ja 30 minuuttia, joista 2 tuntia 0% lisätyötä ja 30 minuuttia 50% lisätyötä. 50% lisätyö vaikuttaa nyt korotetun lisätyön viikkotuntimäärään, joten 37 tunnin ja 30 minuutin rajaan on vielä 5 tuntia.  
  
![](https://support.nepton.com/hc/article_attachments/35369648623901)
## Sunnuntaiylityö
**Sunnuntaiylityön alkamisaika**  
Voidaan määrittää kellonaika sekä kohdistusarvo, josta alkaen sunnuntaiylityö alkaa muodostua. Syötetty kellonaika ja kohdistusarvo yhdessä määrittävät, kummalle päivälle sunnuntaiylityö kohdistuu.
**50% sunnuntaiylityön maksimimäärä sunnuntaisin ja juhlapyhinä**  
Voidaan asettaa enimmäismäärä 50% sunnuntaiylityön määrälle. Jos tässä on asetus, muodostuu sunnuntaisin ja juhlapyhinä tehdystä ylityöstä sunnuntaiylityötä. Jos TES:ssä on määräys, että sunnuntaiylityöstä maksetaan aina 100% korvaus, asetetaan tähän arvoksi 0 minuuttia.
**Raja-arvon laskentatapa**  
Voidaan määrittää, miten 50 % sunnuntaiylityön raja-arvon täyttymistä tarkastellaan. Raja-arvona käytetään asetuksessa "50 % sunnuntaiylityön maksimimäärä sunnuntaisin ja juhlapyhinä" määritettyä arvoa. Kun raja-arvo on täynnä, muodostuu kaikki sen ylittävä ylityö 100 % sunnuntaiylityönä. Päivittäin-asetuksella raja-arvon täyttymistä tarkastellaan päivittäin, jolloin useampana päivänä voi muodostua 50 % sunnuntaiylityötä. Kalenteriviikoittain-asetuksella tarkastelu kattaa koko kalenteriviikon. Oletus-arvo toimii samalla tavalla kuin Päivittäin-arvo.
**Juhlapyhinä ansaitaan sunnuntaiylitöitä viikkovelvoitteen täyttämisen jälkeen**  
Voidaan määrittää, ansaitaanko juhlapyhinä sunnuntaiylityötä vasta viikoittaisen työaikavelvoitteen täyttymisen jälkeen.
**Juhlapyhät, jolloin ansaitaan sunnuntaiylityötä**  
Voidaan määrittää, mistä juhlapyhistä ansaitaan sunnuntaiylityötä. Juhlapyhät periytyvät asetusryhmään työyhteisön TES-asetuksista (Työyhteisön asetukset > Työtunnit > TES), mutta niitä voidaan tarvittaessa muokata asetusryhmäkohtaisesti.
![Screenshot 2026-03-25 102754.png](https://support.nepton.com/hc/article_attachments/34876705934493)
## TES ylityö
TES ylityötä muodostuu seuraavissa tapauksissa.
Työpäivän pituus ylittyy, mutta TES enimmäistyöaika vuorokaudessa ei ylity eikä tehty työ ole lisätyötä.
Viikkotyöaika ylittyy, mutta TES enimmäistyöaika viikossa ei ylity eikä tehty työ ole lisätyötä.
Tyypillisesti TES ylityötä muodostuu arkipyhäviikoilla, kun tullaan esim. lauantaina töihin.
Asetuksella “Tunti tunnista -ylityö huomioidaan TES-ylityön laskennassa” voidaan määrittää, vaikuttaako päivällä tai viikolla aiemmin kirjattu tunti tunnista -ylityö siihen, onko ennen TES enimmäistyöajan täyttymistä kirjattu ylityö TES-ylityötä vai ei.
Tunti tunnista -ylityö huomioidaan TES-ylityön laskennassa oletuksena jos se lasketaan viikoittaiseen työaikaan. 
## Ajat, jolloin ei ansaita 50% ylityötä
On mahdollista asettaa päiväkohtaiset ajat, milloin normaalisti 50% ylityönä korvattava työ korvataan 100% ylityönä. Asetus vaikuttaa päivänä, milloin työ [näytetään](<https://support.nepton.com/hc/fi/articles/360008777997>). Jos Työtapahtumien näyttö -asetus on vakio eli "Tapahtumat ja laskenta näytetään päivänä milloin työvuoro alkaa", maanantaille on merkitty ao. esimerkin mukaiset ajat, jolloin ei ansaita 50% ylityötä, työ on alkanut maanantaina ja sama työ jatkuu tiistain puolelle, niin maanantain asetus vaikuttaa myös tiistaihin 07:00 asti. Mikäli tänä aikana muodostuu 50% ylityötä, muuttuu se 100% ylityöksi.
Koska esimerkissä ei tiistaille ole asetettu aikoja, niin tiistain puolella _alkaneeseen_ työhön ei tässä tapauksessa sovelleta näitä asetuksia. 
![mceclip0.png](https://support.nepton.com/hc/article_attachments/5511074831389)
#### Ajat, jolloin ansaitaan ylityötä 50% ulkopuolella
**![](https://support.nepton.com/hc/article_attachments/21649221298973)**
Tällä määrityksellä voidaan muuttaa ylityön laskentajärjestystä silloin, jos ylityöt osuvat samaan aikaan ”**Ajat, jolloin ei ansaita 50% ylityötä”** -kohdassa määritellylle ajanjaksolle. Oletuarvo on "Ei".
Asetusarvolla “Kyllä” lasketaan ensin noiden aikojen ulkopuolelle jäävät ylityöt normaalien ylityömääritysten mukaisesti ja sitten vasta rajoitettu aika.
Esimerkiksi jos on määritelty, että klo 16 -18 ei ansaita 50% ylityötä ja tehdään ylityötä 16:00 – 19:00, niin ensin lasketaan ylityö klo 18-19 väliseltä ajalta normaalin ylityölaskennan mukaisesti, jolloin muodostuu 1 tunti päivä 50% ylityötä ja sen jälkeen 2 tuntia päivä 100% ylityötä, koska klo 16-18 väliseltä ajalta ei ansaita 50% ylityötä:
![](https://support.nepton.com/hc/article_attachments/21649342853277)
Jos määritys on “Ei”, niin ylityö muodostuu aikajärjestyksessä ja koska klo 16-18 ei ansaita 50% ylityötä, niin muodostuu 3 tuntia päivä 100% ylityötä:
![](https://support.nepton.com/hc/article_attachments/21649342855453)
