---
id: 360007389978
title: Viikkolepokorvaus
url: https://support.nepton.com/hc/fi/articles/360007389978-Viikkolepokorvaus
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- viikkovapaakorvaus
- kertapalkkio
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2026-02-02T06:24:34Z'
---

# Viikkolepokorvaus

## Yleistä
Palveluun voidaan määritellä työntekijälle korvaus siitä, että määriteltyä _keskeytymätöntä_ lepoaikaa ei olla saavutettu viikon sisällä tai keskimäärin useamman viikon (=määritellyn lepojakson) aikana, kuten on määritelty Työaikalain (27 §) mukaan.
Viikoittainen lepoaika arvioidaan tarkasteltavan jakson viimeisenä päivänä, huomioon ottaen työntekijän aiemmat työviikot ja mahdollinen lepoajan aloituspäivämäärä.
Jos viikkolevon aikana ansaitun työkorotuksen tulee olla korotettua, ohjeet löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360002560978>).
## Viikkolepokorvauksen ansainnan käyttöönotto
Viikkolepokorvaus voidaan määritellä käyttöön työyhteisön asetuksissa **Työaika > Hallinta > Työyhteisön asetukset > Työtunnit > Viikkolepokorvaus** tai vastaavasti asetusryhmän asetuksissa **Työaika > Hallinta > Asetusryhmät > Työtunnit > Viikkolepo**.
### Viikkolepoajan laskenta -asetukset
![](https://support.nepton.com/hc/article_attachments/13275913565469)
Tässä osiossa määritellään, onko työntekijä oikeutettu viikkolepokorvaukseen (määrää ei määritellä tässä).
  * **Korvaa kun vapaa-aikana ei täyty** \- Määrittelee keskimääräisen keskeytyksettömän lepoajan, joka työntekijälle tulee muodostua viikoittaisen ansaintakauden aikana. Tämä arvo on tyypillisesti 35 tuntia.
  * **Ajanjakso, jolta lepoaika tarkistetaan (viikoissa)** \- Määrittelee lepoajan seurantajakson keston viikoissa.
  * **Aloituspäivä, jos tarkistetaan useita viikkoja** \- Jos ajanjakso, jolta lepoaika tarkistetaan on pidempi kuin yksi viikko, järjestelmä tarvitsee tiedon siitä, mitä päivämäärää käytetään laskennan aloituksessa. Viikkolepolaskennat arvioidaan ja korvataan (jos on tarve) moniviikkoisen jakson lopussa. Esimerkiksi, jos aloituspäivä on 02.01.2023 ja kyseessä on kahden viikon jakso, tällöin ensimmäinen lepolaskentajakso on 02.01.2023-15.01.2023 ja jos keskimääräinen viikoittainen lepoaika ei täyty, korvaus annetaan päivälle 15.01.2023 (+/- poikkeamat). Jos aloituspäivä ei osu työntekijän normaalin työviikon ensimmäiselle päivälle, aloituspäivä automaattisesti pyöristetään alaspäin, jotta korvaus osuu kyseisen työntekijän viikon loppuun.
  * **Työviikon aloitus- ja päättymisajan poikkeamat** \- Työviikon aloitus- ja päättymisaikoihin voidaan asettaa poikkeamat, jos halutaan, että viikkolepokorvauksen laskenta perustuu työviikon aloitus- ja päättymisajasta poikkeavaan kellonaikaan. Eli esim. työviikko kestää maanantaista 00:00:sta sunnuntaihin 24:00:ään, mutta lepoajan tarkistukseen tulisi ottaa mukaan seuraavan viikon ensimmäisen päivän 6 ensimmäistä tuntia (eli klo 06:00 asti), tällöin päättymisajan poikkeama olisi +6 tuntia. Poikkeama voi olla sekä aloitus- että päättymisajassa samanaikaisesti. Kun käytetään positiivisia työviikon lopun poikkeamia, viikoittaisen lepokorvauksen kompensointipäivä siirtyy poikkeaman osoittamaan laskentapäivään. Tällöin esimerkiksi, jos työviikko päättyy sunnuntaina klo 24:00, viikkolepokorvaus maksetaan maanantaisin, koska poikkeama +6 tuntia siirtää korvauksen maanantain puolelle. Vastaavasti myös asetus **Työtunnit - > Näytön asetukset -> Työtapahtumien näyttö** vaikuttaa siihen, milloin viikkolepokorvaus maksetaan. Jos asetus on **Tapahtumat ja laskenta näytetään päivänä, milloin työvuoro loppuu** , maksetaan korvaus maanantaina.
  * **Tapahtumatyypit, jotka lasketaan lepoajaksi** \- Tällä asetuksella voidaan määritellä, mitkä tapahtumatyypit lasketaan lepoajaksi viikkolepokorvausta laskettaessa, kuten esim. saldovapaa, vuosiloma jne.
  * **Kertymään tehty tunti tunnista -ylityö lasketaan lepoajaksi** \- Tällä asetukealla määritellään, lasketaanko tehdyt "tunti tunnista" -ylityöt lepoajaksi.
  * **Ylityö lasketaan lepoajaksi** \- Tällä asetuksella määritellään, lasketaanko tehdyt ylityötunnit lepoajaksi.


### Korvaus, kun viikkolepoaikaa ei saavuteta -asetukset
Tässä osiossa määritellään, miten työntekijälle korvataan yllämainittujen asetusten määräämän lepoajan puute.
  * **Korvauksen kohde** \- Oletuksena korvaus maksetaan palkassa, mutta se voidaan myös määrittää pidettäväksi vapaana. Aloita valitsemalla kertymä, johon korvaus maksetaan, yleensä tämä on "Viikkolepo". Tämän jälkeen tulee varmistaa, että viikkolepokertymä on käytössä ja että "Viikkolepovapaa" -tapahtumatyyppi on saatavilla kun tapahtumia kirjataan. Lisätietoa löytyy [Kertymien käyttöönotto](<https://support.nepton.com/hc/fi/articles/360005073918-Kertymien-k%C3%A4ytt%C3%B6%C3%B6notto>) -artikkelista.  
_Huom: kun viedään viikkolepokorvausta ulos toiseen järjestelmään käyttäen poimintasääntöjä, tämä asetus voidaan määritellä käyttämällä "basePartTarget" -kenttää._
  * **Kuinka korvaus ansaitaan:**
    * Ei asetettu - asetuksen arvo peritään ylemmältä tasolta (Työyhteisön asetuksissa "Ei asetettu " tarkoittaa, ettei toiminto ole käytössä).
    * Ei ansaita - korvausta ei makseta työntekijälle, vaikka viikkolepo ei täyty.
    * Ansaitaan kiinteänä arvona - määritellään kiinteä korvaus tunneissa/minuuteissa (katso "Jos kiinteän korvauksen määrä")
    * Ansaitaan työaikaan perustuen - korvaus perustuu toteutuneeseen työaikaan lepojakson aikana (katso kohta "Jos ansainta perustuu työaikaan")
    * Ansaitaan lepoajan lyhennykseen perustuen - esim. jos lepoajan laskennassa käytetään 35 tuntia ja työntekijän pisin keskeytyksetön lepoaika on 30 tuntia, tällöin ansaitaan 5 tuntia viikkolepoa.
    * Ansaitaan työaikaan perustuen (tai lepoajan poikkeamaan, jos työtä ei ole) - Sama kuin yllä, mutta jos ansaintajakson sisällä ei ole työtä, käytetään "Lepoajan lyhennykseen perustuen" -laskentaa.


  * **Jos kiinteän korvauksen määrä** \- Jos ylempi asetus on "Ansaitaan kiinteänä arvona" eikä työntekijällä ole tarpeeksi lepoaikaa, hänelle korvataan tähän määritelty korvaus. Jos käytetään usean viikon ajanjaksoa, korvaus maksetaan kerran jakson lopussa.


  * **Jos ansainta perustuu työaikaan**
    * **Ansaintakauden peruste**  

      * Ei asetettu/Peri ylemmältä tasolta - Asetuksen arvo peritään ylemmältä tasolta (Työyhteisön asetuksissa "Ei asetettu " tarkoittaa ettei toiminto ole käytössä)
      * Työ laskentaviikon päätteeksi - Työ, joka on tehty "viikon loppupuolella" korvataan ajan mukaan. Jakso, joka katsotaan "viikon loppupuoleksi", määritellään "Ansaintakauden pituus" asetuksessa. Jos lepojakso sisältää useamman viikon, jokaisen viikon lopusta tarkistetaan lepovaje ja vajeet lasketaan yhteen ja ne muodostavat lopullisen korvauksen. Esimerkiksi jos ansaintakauden pituudeksi on määritetty 24h, lasketaan kauden viimeisen 24:n tunnin aikana tehty työ korvauksen määräksi.
      * Työ perjantain vuoron jälkeen tai ennen viikon loppumista - Perjantain työvuoron jälkeen tehty työmäärä (ansaintajakson kestoon saakka), ja työ laskentaviikon päätteeksi (kuten ylläolevassa kuvattu) molemmat tarkistetaan. Laskenta, josta seuraa vähemmän korvattavaa on se, jota käytetään. Jos käytät tätä laskentatapaa, niin täytä myös**perjantain vuoron loppuaika** -asetuskenttä.  

      * Työ ennen seuraavan viikon ensimmäistä vuoroa - Ansaintajakso tarkistetaan ennen ensi viikon ensimmäisen työvuoron alkua. Jos päivänä ei ole vuoroa tai on pyhäpäivä, käytetään oletustyön alkamisaikaa. Huom: tämä ohittaa myös lepoarviointijakson ja tarkistaa 7 päivää taaksepäin samasta pisteestä.  

      * Päivä, jolloin vähiten töitä - Päivää, jolloin on tehty vähiten töitä, käytetään korvaamisen perusteena. Esim. jos kaikilla muilla päivillä on 10 tuntia työtä lukuunottamatta keskiviikkoa, jolla on 8 tuntia työtä, on korvauksena 8 tuntia. Jos lepojakso sisältää useamman viikon, jokaiselta viikolta tarkistetaan päivä, jolloin on tehty vähiten töitä ja nämä tunnit lasketaan yhteen ja ne muodostavat lopullisen korvauksen. Oletuksena yövuoron koko aika sellaisena päivänä, jona on vähiten työtä, korvataan, mutta tämä voidaan yliajaa asettamalla ansaintakausi 24 tunniksi ja tällöin korvataan vain se osa päivän työtunneista, joka osuu päällekkäin kyseisen päivän kanssa.
      * Työskentely sunnuntain jälkeen klo 00:00 - Korvaus maksetaan sunnuntain puolenyön (eli sunnuntain ensimmäisen minuutin) jälkeen tehdystä työstä. Jos ansaintajakson kesto on asetettu, tällä asetetaan ansaintajakson loppu, esimerkiksi 24h asettaisi ansaintajakson sunnuntaista 00:00 sunnuntaihin 24:00. Jos ansaintajakson kestoa ei ole asetettu, kaikki sunnuntain työvuorot ansaitsevat korvauksen, myös ne, jotka menevät yön yli maanantaihin.
    * **Ansaintakauden pituus** \- Niiden tuntien määrä, joilta tarkistetaan mahdollista korvattavaa, eli tarkistetaan, kuinka paljon töitä on tehty sillä ajanjaksolla, jolle lepokorvaus on asetettu. Esim. kun käytetään asetusta "Työ laskentaviikon päätteeksi" ja jos normaali työviikko päättyy sunnuntaina klo 24:00 ja on asetettuna +6:00 tunnin poikkeama, jolloin tarkistetaan viikkolevon määrä maanantaihin klo 6:00 saakka, tällöin tarkistetaan 35 tunnin ansaintajakson työt maanantaista klo 6:00:sta taaksepäin ja korvataan tämä määrä. Jos tällä jaksolla on 5 tuntia työtä, 5 tuntia viikkolepokorvausta korvataan kyseiseltä viikolta.
    * **Lisävalinnat**
      * Pyöristyksen tapa/aikaväli - Pyöristää korvauksen kokonaismäärän asetuksen mukaisesti.
      * Pyöristyksen kynnys - Kynnysarvos pyöristykselle
        * Ylös pyöristystavavalla pyöristetään vain kun jakojäännös ylittää kynnysarvon
        * Normaalilla pyöristystavalla pyöristetään alaspäin, kun jakojäännös alittaa kynnysarvon, muussa tapauksessa pyöristetään ylöspäin
        * Alaspäin pyöristäminen tapahtuu vain jos kynnysarvoa ei ole asetettu, tai pyöristyksen jakojäännös on vähemmän kuin kynnysarvo
      * Korvauksen vähimmäismäärä/enimmäismäärä - Asettaa korvauksen vähimmäis- ja enimmäismäärät.


Myös Näytön asetus 'Työtapahtumien näyttö' (osiossa **Työtunnit - > Näytön asetukset**) vaikuttaa siihen, milloin viikkolepokorvaus maksetaan. Jos asetus on **Tapahtumat ja laskenta näytetään päivänä, milloin työvuoro loppuu** , muodostetaan korvaus viikon viimeisen päivän jälkeen, yleensä maanantaina.
## Esimerkkejä
### Esimerkki 1. Yhden viikon tarkastelu, kiinteä korvaus saldoon
Alla esimerkki tapauksesta, jossa tarkastellaan viikkolevon täyttymistä yhden viikon jakson aikana. Tässä esimerkissä tarkastellaan, onko 35 tunnin lepoaika täyttynyt viikon sisällä.
![](https://support.nepton.com/hc/article_attachments/19814852797725)
Korvaukseksi on asetettu kiinteä 10h, joka korvataan saldokertymään.
![](https://support.nepton.com/hc/article_attachments/19814868995869)
Vähimmäislepoaika 35h ei ole täyttynyt, joten sunnuntaille muodostuu 10h viikkolepokorvaus, joka ohjautuu suoraan saldokertymään asetusten mukaan. Viikkolepokorvauksen vieressä olevaa info-palluraa klikkaamalla saadaan auki vielä tarkempi yhteenveto viikkolevon laskennasta:  
![](https://support.nepton.com/hc/article_attachments/19814869000605)
Avautuvasta ikkunasta nähdään, mikä on kyseisen viikkolepokorvauksen tarkastelujakso, eli tässä tapauksessa viikko 10.-16.6. Vähimmäislepoaika on 35h, mutta jakson pisin lepoaika on ollut 22h, eli jäänyt 13h vajaaksi tavoitteesta. Koska asetuksiin on määritelty kiinteä korvaus, on korvauksen määrä 10h, joka ohjautuu saldokertymään.
### Esimerkki 2. Yhden viikon tarkastelu, korvaus perustuu lyhimpään lepoaikaan
Mikäli asetuksissa on määritelty, että korvaus ei olekaan kiinteä, vaan perustuu tarkastelujakson lyhimpään lepoaikaan, näyttäisi saman tilanteen korvaus tältä:
![](https://support.nepton.com/hc/article_attachments/19814852806813)
  
![](https://support.nepton.com/hc/article_attachments/19814852808733)
Viikkolepokorvaus on 13h, sillä jakson pisin lepoaika on ollut 22h, eli 13h vähemmän kuin 35h. Korvaus maksetaan tässä tapauksessa palkassa, eli se ei siirry saldokertymään.
### Esimerkki 3. Yhden viikon tarkastelu, päättymisajan poikkeama +6h, korvaus perustuu työaikaan
Tässä esimerkissä työviikon päättymisajan poikkeamaksi on asetettu +6h, eli tarkasteluaika päättyykin vasta maanantaina klo 06:00.
![](https://support.nepton.com/hc/article_attachments/19814852812829)
Tarkasteluajanjakso on siis 10.6. klo 00 - 17.6. klo 06:00. Korvaus perustuu työaikaan, ja muodostuu sen mukaan, kuinka paljon on tehty töitä laskentaviikon päätteeksi, 24h taaksepäin laskettuna.
![](https://support.nepton.com/hc/article_attachments/19814852815133)
Koska lepoajan poikkeamaan on asetettu +6h, siirtyy tarkastelujakson loppu maanantain puolelle. Tästä syystä myös viikkolepokorvaus näkyy kalenterissa vasta maanantaina. 
![](https://support.nepton.com/hc/article_attachments/19814852817053)
Info-palluraa painamalla saadaan taas auki tarkempi selitys korvauksen muodostumiselle.
![](https://support.nepton.com/hc/article_attachments/19814852819869)
Tässä tapauksessa korvaus on 5h, sillä maanantaiaamusta klo 06:00 24h taaksepäin laskettuna, eli sunnuntaiaamuun klo 06:00 asti, on tehty töitä yhteensä 5h.
### Esimerkki 4. Kahden viikon tarkastelu, korvaus perustuu työaikaan, päivä jolloin vähiten töitä
Seuraavassa esimerkissä on viikon sijaan tarkastelujakson pituus kaksi viikkoa. Kahden viikon lepoajan tarkastelussa palvelu tarkistaa aikajakson kaksi viikkoa taaksepäin, ottaa huomioon kummankin viikon pisimmän lepoajan ja päättelee onko lepoaikaa ollut keskimäärin riittävästi. Mikäli ei ole, korvaus tulee asetusten mukaan, tässä tapauksessa korvaus perustuu työaikaan, ja muodostuu sen päivän tuntien mukaan, jolloin on tehty vähiten töitä tarkastelujaksolla.
![](https://support.nepton.com/hc/article_attachments/19814869016349)
Kalenterissa tulkinta näyttää tältä:
![](https://support.nepton.com/hc/article_attachments/19814852823837)
Viikkolepokorvaus näytetään vasta kahden viikon tarkastelujakson lopussa. Info-palluran tiedoista selviää, että tarkastelujakso on ollut 3.-16.6. välinen aika. Kumpikin viikko on eriteltynä omissa osioissaan. Ensimmäisellä viikolla pisin lepoaika on ollut 21h (la-su välinen pätkä), kun taas toisella viikolla lepoaika on ollut 20:00. 35h viikkolepo ei ole siis täyttynyt kummallakaan viikolla. Koska korvaus perustuu sen päivän työtunteihin, jolloin on tehty vähiten töitä, tulee yhteensä viikkolepokorvausta 7h: 3h muodostuu ensimmäisen viikon lauantailta ja 4h seuraavan viikon lauantailta.
Mikäli toisena viikonloppuna ei oltaisi tehty mitään töitä (viimeinen työkirjaus perjantain kirjaus), olisi tarkastelujakson keskimääräinen vähimmäislepoaika täyttynyt, eikä korvausta olisi tullut. Mikäli töitä olisi tehty vain sunnuntaina niin, että toisen viikon lepoaika täyttyy, mutta toisen ei, lasketaan korvaus kahden viikon tarkastelujakson mukaan kummankin viikon lyhimmän työpäivän mukaan:  
![](https://support.nepton.com/hc/article_attachments/19814869020829)
## Viikkolepokorvauksen ansainnan poistaminen käytöstä
Tietyissä asetusryhmässä saattaa olla tarvetta määrittää viikkolepokorvaus pois käytöstä, niin ettei asetukset periydy asetusryhmään ylemmästä asetusryhmästä. Määritä tällöin asetusryhmän viikkolepoasetuksissa Korvaus, kun viikkolepoaikaa ei saavuteta, kohdassa Kuinka korvaus ansaitaan arvoon **Ei ansaita**. 
![](https://support.nepton.com/hc/article_attachments/21472126626205)
