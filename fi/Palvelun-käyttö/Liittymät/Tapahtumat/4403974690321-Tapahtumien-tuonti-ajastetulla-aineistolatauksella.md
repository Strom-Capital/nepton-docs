---
id: 4403974690321
title: Tapahtumien tuonti ajastetulla aineistolatauksella
url: https://support.nepton.com/hc/fi/articles/4403974690321-Tapahtumien-tuonti-ajastetulla-aineistolatauksella
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumat
section_id: 360001061298
section_path:
- Liittymät
- Tapahtumat
labels: []
promoted: false
updated_at: '2026-01-19T05:19:27Z'
edited_at: '2026-01-19T05:19:27Z'
---

# Tapahtumien tuonti ajastetulla aineistolatauksella

**Tapahtumien tuontia ajastetulla aineistolatauksella suositellaan silloin kun tapahtumia tuodaan palveluun säännöllisesti ja lähettävä järjestelmä voi muodostaa aineiston automaattisesti.**
Aineisto voidaan tuoda näissä tiedostomuodoissa: CSV, XLSX, XLS, tai ODS.
Siirron määrittely ja aineiston valmistelu tehdään samalla tavalla kuin käyttöliittymästä suoritettava aineistolataus.
Ajastetun aineistolatauksen tapauksessa käytettävät tietosisällöt ovat hieman erilaisia ja määrittelyssä asetetaan myös aineiston ajastukseen liittyvät tiedot. Käytettävä tietosisältö sekä ajastuksen määrittely on esitetty alla. Aineiston valmistelu ja tapahtumien tuonnin määrittely tehdään, kuten on kuvattu käyttöliittymästä tehtävän aineistotuonnin artikkelissa [täällä.](<https://support.nepton.com/hc/fi/articles/4419484517521>)
Siirrettävälle aineistolle määritellään tapahtumien luoja (kts. asetus alla). Siirrettävän aineiston perusteella tehdyt muokkaukset muodostetaan palveluun tapahtumien luojan tekemänä. Kun siirtoaineiston tapahtumia käsitellään, niin palvelu vertaa onko tapahtuma perustettu henkilölle jo aiemmin tapahtumien luojan tekemänä. Mikäli henkilön tapahtumat eivät sisällä aineistolla muodostettavaa tapahtumaa, niin tapahtuma luodaan henkilön kalenteriin. Tapahtumat, jotka eivät ole siirrettävällä aineistolla, mutta ovat henkilön kalenterissa tapahtuman luojan tekemänä poistetaan henkilön kalenterista.
Siirrettävän aineiston tulee sisältää kaikki henkilön tapahtumat siirrettävältä ajanjaksolta ja muutokset henkilöiden tapahtumiin joko lisätään tai poistetaan aineiston osoittamalla tavalla. Tämä tarkoittaa esimerkiksi sitä, että aineistolla aiemmin tuotu rivi poistuu henkilön tapahtumista, mikäli aineisto ei enää sisällä sitä. Tällä tavalla kalenterissa esitettävät tapahtumat sisältävät aina saman tiedon kuin siirrettävällä aineistolla on esitetty. Lähdejärjestelmän tulee muodostaa siirrettävä aineisto myös silloin, kun aineistossa välitettäisiin ainoastaan poistuvia tapahtumia, eli aineisto olisi tyhjä.
Mikäli tuot aineistoa sellaisessa muodossa, että aineisto sisältää riveinä vain poistot ja lisäykset tapahtumiin niin katso Sympa - muotoisen aineiston ohje [täältä](<https://support.nepton.com/hc/fi/articles/360003736798>)
Aineiston asetuksissa määritellään kuinka monta päivää historiaan aineiston rivejä huomioidaan. Tällä asetuksella mahdollistetaan se, että aineisto ei sisällä kaikkea henkilön tapahtumahistoriaa, vaan ainoastaan esimerkiksi 60 päivää menneeseen. Tällöin lähettävä järjestelmä voi lähettää tapahtumat tältä ajalta.
Huomioi että vaikka aineistossa olisi vanhempia tapahtumia kuin mitä on asetettu Menneiden päivien määrä siirtotiedostossa - kenttään päivämäärärajaksi, myös näistä tapahtumista tarkistetaan löytyykö henkilönumeroa järjestelmästä ja annetaan varoitus.
Nepton lukee aineiston tapahtuman tuonnin asetusten mukaisesti. Luettu aineisto siirretään arkistointikansioon, silloin kun arkistointikansio on asetettu. Mikäli arkistointikansiota ei ole asetettu, niin tiedosto poistetaan. Siinä tapauksessa jos tiedoston luennassa on sisällöllinen virhe, niin tiedosto jätetaan kansioon.
## Siirtoaineiston tietosisällöt
Palveluun voidaan tuoda seuraavia tietosisältöjä. Siirrettävän aineiston sarakkeet ja sarakejärjestys määritellään tapahtumien tuonnin asetuksissa. Tietosisällöt ovat samat kuin [tapahtumien tuonnissa käyttöliittymän manuaalisella aineistolatauksella](<https://support.nepton.com/hc/fi/articles/4419484517521>).
## Tapahtumien tuonnin automatisointi ja ajastaminen
Tapahtumien tuonti voidaan määritellä toistumaan automaattisesti tiettyinä päivinä, mikäli sinulla on SFTP-palvelin, josta palvelu voi noutaa tiedoston. Ajastuksen tarkemmat ohjeet [täällä](<https://support.nepton.com/hc/fi/articles/10510800700573-Ty%C3%B6ajan-vienti-tuonti-liittymien-ajastus>).
Seuraavassa kuvataan ajastetun tuonnin asetukset. Kun nämä asetukset on määritelty, suoritetaan ajastettu tuonti seuraavana päivänä. Tuonnin tulokset tallennetaan [palvelulokiin](<https://support.nepton.com/hc/fi/articles/360002575478>). 
Asetuksen nimi | Kuvaus  
---|---  
Henkilö, joka näytetään tapahtumien luojana | Henkilö, joka merkitään tuotujen tapahtumien luojaksi. **Huom:** jokaiselle tuonnille pitää olla yksilöllinen ylläpitäjä-tason käyttäjä, joka suorittaa tuonnin. Näin voidaan varmistaa, että jos halutaan poistaa tuotuja tapahtumia, ovat ne vain yhden käyttäjän tuomia tapahtumia. Eli esimerkiksi voidaan luoda käyttäjä "Nepton Import", jolla on ylläpito-oikeudet ja jota käytetään vain yhteen ajastettuun tietojen tuontiin määrittämällä Nepton Import -käyttäjä tähän kohtaan.  
Tuontitiedoston nimi |  Asetusta voidaan käyttää kolmella tapaa:
  * Tarkka tiedostonimi - vain annetulla tiedostonimellä oleva tiedosto tuodaan
  * Tiedostonimi jokerimerkillä - tuo kaikki tiedostot, jotka vastaavat suodatinta. Suodatin voi esimerkiksi olla: event_import*.csv
  * Ei annettua tiedostonimeä - kaikki tuontihakemistossa olevat tiedostot luodaan

  
SFTP-palvelimen osoite | Osoite SFTP-palvelimelle josta tiedosto haetaan. Palvelimen tulee pystyä hyväksymään SFTP-yhteyksiä.  
SFTP käyttäjätunnus | Käyttäjätunnus SFTP-palvelimelle kirjautumista varten.  
Käytä public key-autentikointia |  Jos SFTP-palvelimelle käytetään autentikointia julkisilla avaimilla, asetetaan tähän valinnaksi "Kyllä". Lisätietoa public key-autentikoinnista: <https://support.nepton.com/hc/fi/articles/360015591697-Public-key-autentikointi>  
SFTP salasana | Salasana SFTP-palvelimelle kirjautumista varten.  
SFTP suhteellisen hakemiston polku | Hakemistopolku josta tuotavia tiedostoja haetaan. Tämä on suhteellinen suhteessa oletushakemistoon joka avataan kun SFTP-palvelimelle otetaan yhteys, esimerkiksi absences/to-nepton/  
SFTP arkistoinnin suhteellisen hakemiston polku | Kun tuotava tiedosto on käsitelty, se poistetaan jotta sitä ei käsitellä enää uudestaan. Suosittelemme arkistoimaan tiedostot ja asettamaan arkistointikansion , esim. absences/to-nepton/processed. Tiedostot arkistoidaan päivämäärän mukaan. Jos arkistointia ei oteta käyttöön, tämä kohta jätetään tyhjäksi.  
Menneiden päivien määrä siirtotiedostossa |  Asetuksella määritetään, kuinka monta mennyttä päivää käsitellään. **Huom** : Tapahtuman päättymispäivää käytetään katsomaan, kuuluuko se käsiteltävien tapahtumien joukkoon. Jos menneiltä päiviltä löytyy aiemmin tuotu tapahtuma jota ei enää ole siirtotiedostossa, se merkitään poistetuksi. Näin voidaan poistaa tapahtumia jotka on tuotu Neptoniin mutta sittemmin poistettu lähdejärjestelmästä. Tämän asetuksen oletusarvo on nolla, jos sitä ei ole asetettu. Asetuksen maksimiarvo on 120 päivää. **Huom:** On tärkeää että "Henkilö, joka näytetään tapahtumien luojana"-asetukseen on määritetty käyttäjä joka tekee tapahtumia vain tuonnin kautta. Eli esimerkiksi voidaan luoda käyttäjä "Nepton Import" jolla on ylläpito-oikeudet ja jota käytetään vain ajastettuun tietojen tuontiin.  
Hyväksy tapahtumat tuonnin yhteydessä | Jos valinnaksi on annettu "Kyllä", tapahtumat hyväksytään tuonnin yhteydessä.  
Jos aikoja ei ole annettu, käytä oletusarvoista aloitus- ja lopetusaikaa |  Jos valinnaksi on annettu "Kyllä" ja tapahtumalla ei ole aloitus- tai lopetusaikaa, eikä päivällä ole työvuoroa tai oletettuja työaikoja, käytetään oletusaikoja jotka on asetettu osiossa Työtunnit > Näytön asetukset. Jos valintaa ei ole annettu tai valinnaksi on annettu "Ei" ja tapahtumalla ei ole aloitus- tai lopetusaikaa, eikä päivällä ole työvuoroa tai oletettuja työaikoja, käytetään aloitusaikana 00:00 ja lopetusaikana 24:00.  
Tuonnin aikavälin sääntö #n |  Nämä säännöt määrittävät minä päivinä tuonti ajetaan, esimerkiksi:
  * _now_ = Tapahtumien tuonti ajetaan joka päivä
  * _Monday_ = Tapahtumien tuonti ajetaan joka maanantai
  * _12 day_ = Tapahtumien tuonti ajetaan joka kuun 12:ntena päivänä
  * _second Wednesday of this month_ = Tapahtumien tuonti ajetaan kuukauden joka toisena keskiviikkona

Säännöillä ei ole mahdollista määrittää tarkkaa kellonaikaa tuonnin ajautumiselle. Tuonnit ajetaan aamuyöstä, useimmiten 03:00-12:00 välillä.  
Päivämäärän muoto | Tiedoston päivämäärän muoto, jos tiedostossa käytetään kenttää jossa ilmoitetaan päivämäärä. Oletuksena _Y-m-d_(esim. 2021-08-04)*. [Muoto määritetään samalla tavalla kuin PHP:n date-funktiossa.](<https://www.php.net/manual/en/function.date.php#refsect1-function.date-parameters>)  
Ajan muoto | Tiedoston ajan muoto, jos tiedostossa käytetään kenttää jossa ilmoitetaan kellonaika. Oletuksena _H:i:s_ (esim. 12:30:00)*. [Muoto määritetään samalla tavalla kuin PHP:n date-funktiossa.](<https://www.php.net/manual/en/function.date.php#refsect1-function.date-parameters>)  
Päivämäärän ja ajan muoto | Tiedoston päivämäärän ja ajan muoto, jos tiedostossa käytetään kenttää jossa ilmoitetaan kellonaika. Oletuksena  _Y-m-d H:i:s_ (esim. 2021-08-04 12:30:00)*. [Muoto määritetään samalla tavalla kuin PHP:n date-funktiossa.](<https://www.php.net/manual/en/function.date.php#refsect1-function.date-parameters>)  
Merkistö |  Tiedoston merkistö, oletuksena `UTF-8`. Seuraavat arvot ovat tuettuja:
  * `UCS-4`
  * `UCS-4BE`
  * `UCS-4LE`
  * `UCS-2`
  * `UCS-2BE`
  * `UCS-2LE`
  * `UTF-32`
  * `UTF-32BE`
  * `UTF-32LE`
  * `UTF-16`
  * `UTF-16BE`
  * `UTF-16LE`
  * `UTF-8`
  * `UTF-7`
  * `UTF7-IMAP`
  * `ASCII`
  * `EUC-JP`
  * `SJIS`
  * `eucJP-win`
  * `EUC-JP-2004`
  * `SJIS-win`
  * `SJIS-Mobile#DOCOMO`
  * `SJIS-Mobile#KDDI`
  * `SJIS-Mobile#SOFTBANK`
  * `SJIS-mac`
  * `SJIS-2004`
  * `UTF-8-Mobile#DOCOMO`
  * `UTF-8-Mobile#KDDI-A`
  * `UTF-8-Mobile#KDDI-B`
  * `UTF-8-Mobile#SOFTBANK`
  * `CP932`
  * `CP51932`
  * `JIS`
  * `ISO-2022-JP`
  * `ISO-2022-JP-MS`
  * `GB18030`
  * `Windows-1252`
  * `Windows-1254`
  * `ISO-8859-1`
  * `ISO-8859-2`
  * `ISO-8859-3`
  * `ISO-8859-4`
  * `ISO-8859-5`
  * `ISO-8859-6`
  * `ISO-8859-7`
  * `ISO-8859-8`
  * `ISO-8859-9`
  * `ISO-8859-10`
  * `ISO-8859-13`
  * `ISO-8859-14`
  * `ISO-8859-15`
  * `ISO-8859-16`
  * `EUC-CN`
  * `CP936`
  * `HZ`
  * `EUC-TW`
  * `BIG-5`
  * `CP950`
  * `EUC-KR`
  * `UHC`
  * `ISO-2022-KR`
  * `Windows-1251`
  * `CP866`
  * `KOI8-R`
  * `KOI8-U`
  * `ArmSCII-8`
  * `CP850`
  * `JIS-ms`
  * `ISO-2022-JP-2004`
  * `ISO-2022-JP-MOBILE#KDDI`
  * `CP50220`
  * `CP50220raw`
  * `CP50221`
  * `CP50222`

  
CSV erotinmerkki |  Millä merkillä CSV-tiedostossa tiedot on eritelty. Oletuksena `;` Esimerkiksi jos tiedoston tiedot on eritetty pilkuilla, tulee tähän asettaa `,`  
CSV ympyröintimerkki | Millä merkillä CSV-tiedostossa ympyröidään tietue niin että se tulkitaan yhdeksi tietueeksi. Oletusympyröintimerkki on `"`  
  
Esimerkiksi jos tietue on _"Tässä, on; esimerkki"_ tulkitsee tuonti " merkkien sisällä olevan tekstin yhdeksi tiedoksi silloin kun ympyröintimerkiksi on asetettu `"`  
Ohita rivit joissa tuntematon henkilö | Jos arvona kyllä, rivit joissa on tuntematon henkilö, ohitetaan sen sijaan että tuonti merkittäisiin epäonnistuneeksi.  
Ohitettavat henkilönumerot | Pilkulla eroteltu lista henkilönumeroista, jotka halutaan jättää huomiotta ajastetussa tuonnissa. Esimerkiksi määritys 1234,5678,1995 tarkoittaa että henkilöt, joiden henkilönumerot ovat 1234, 5678 tai 1995 jätetään huomiotta ajastetussa tuonnissa.  
Ohitettavat tapahtumatyyppien koodit | Pilkulla eroteltu lista tapahtumattyypien koodeista, jotka halutaan jättää huomiotta ajastetussa tuonnissa. Esimerkiksi määritys 1234,5678,1995 tarkoittaa että tapahtumatyypit joiden koodi on 1234, 5678 tai 1995 jätetään huomiotta ajastetussa tuonnissa.  
Sarakkeiden järjestyksellä on väliä | Kyllä/Ei valinta. Jos tuontitiedosto sisältää otsikkorivin sarakkeille, aseta **Sarakkeiden järjestyksellä on väliä** arvoon **Ei**. Lue lisää alta sarakkeiden otsikoiden määrittämisestä. Jos tuontitiedot eivät sisällä sarakkeiden otsikkoriviä, aseta **Sarakkeiden järjestyksellä on väliä** arvoon **Kyllä**  
*Y= vuosi, m = kuukausi,d = päivä, H = tunti, i = minuutti, s = sekuntti
Jos tuontitiedosto sisältää otsikkorivin sarakkeille, aseta **Sarakkeiden järjestyksellä on väliä** arvoon **Ei**. Tällöin tiedoston kunkin sarakkeen otsikon nimen on vastattava sarakkeen otsikkoa ja kentän määritelmää asetuksissa. Esimerkiksi: 
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21079132729885)
Jos tuontitiedot eivät sisällä sarakkeiden otsikkoriviä, aseta **Sarakkeiden järjestyksellä on väliä** arvoon **Kyllä** ja valitse sarakkeen otsikkokenttä siinä järjestyksessä, jossa sarakkeet näkyvät tiedostossa. Esimerkiksi:
![mceclip1.png](https://support.nepton.com/hc/article_attachments/21079102841245)
Huomioita tuonnin sarakkeista:
![](https://support.nepton.com/hc/article_attachments/18210792328733) | 
  * Tapahtumatyypin tunnus / Event type ID = vanha tapa viitata tapahtumaan, ei käyttöön uusissa toteutuksissa
  * Tapahtumatyypin sisäinen nimi / Event type internal name = vanha tapa viitata tapahtumaan, ei käyttöön uusissa toteutuksissa
  * **Merkitty tapahtumatyyppi** / **Customer defined event type code** = käytä tätä saraketta tapahtumien tuonneissa merkitsemään tuotavaa tapahtumaa (sairaspoissaolo, loma, jne)
  * Poissaolotyypin tunnus / Absence type ID = vanha tapa viitata tapahtumaan, ei käyttöön uusissa toteutuksissa
  * Poissaolo tai sairauspoissaolo palkallinen päivämäärään/aikaan saakka sekä palkallinen päivämäärän/kellonajan jälkeen = sarakkeille voi antaa arvon vain poissolotapahtumille, joiden palkallisuutta voi muuttaa.

  
---|---
