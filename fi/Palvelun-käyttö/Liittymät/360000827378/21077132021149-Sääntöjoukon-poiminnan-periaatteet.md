---
id: 21077132021149
title: Sääntöjoukon poiminnan periaatteet
url: https://support.nepton.com/hc/fi/articles/21077132021149-S%C3%A4%C3%A4nt%C3%B6joukon-poiminnan-periaatteet
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels:
- poimintasääntöjen muodostaminen
- sääntöjoukkojen määrittely
promoted: false
updated_at: '2026-05-15T06:12:08Z'
edited_at: '2026-05-15T06:10:13Z'
---

# Sääntöjoukon poiminnan periaatteet

Huomoithan, että poimintasääntöjen luominen ja muokkaaminen edellyttää perustason ymmärrystä SQL:stä.  
Sääntöjoukolla määritetään siirrettävään aineistoon poimittava sisältö. Tässä artikkelissa käydään läpi poiminnan perusperiaatteet ja sääntöjoukkoihin useimmiten tarvittavat lisäsäännöt. Muita poimintasääntöjen luomiseen liittyviä, oleellisia ohjeita löydät seuraavien linkkien takaa:
    * [Yleiskuvaus sääntöjoukoista](<https://support.nepton.com/hc/fi/articles/360002492278>)  
Yleistä tietoa siitä, missä muodoissa ja millä tavoin palvelusta voidaan ladata aineistoa sääntöjoukkojen avulla, sekä mistä asetukset löytyvät palvelusta


    * [Tietokantataulujen sisältö](<https://support.nepton.com/hc/fi/articles/360002489257>)  
Sääntöjoukon tietokantataulujen sarakekuvaukset.  
  

    * [Poimintasääntöjen mallit](<https://support.nepton.com/hc/fi/sections/360000827378>)  
Kattava lista sääntöjoukon poimintasääntöjen malleista, esimerkiksi [palkkaliittymälle](<https://support.nepton.com/hc/fi/articles/360008045337>), [poissaoloille](<https://support.nepton.com/hc/fi/articles/360013979998>) ja [henkilötiedoille](<https://support.nepton.com/hc/fi/articles/360015612638>).  
  
Artikkelien malleja voi hyödyntää sellaisenaan, mutta niihin tulee huomioida kohdejärjestelmän vaatimukset esimerkiksi tiedon ryhmittelyn ja mahdollisten järjestelmäkohtaisen tietokenttien osalta. Mallit eivät siis toimi sellaisenaan kaikkiin tapauksiin. Tukipalvelusta löytyviin valmiisiin malleihin tulee usein lisätä tässä artikkelissa käsiteltyjä ryhmittelyn ja rajaamisen sääntöjä.


## SQLite muoto yleisesti
Sääntöjoukossa esitetään 100 riviä poimintasäännöille. Kullakin rivillä on poimintasäännön nimi, käytettävä palkkalaji, poimintasääntö ja yksikkötieto (tuntia, kappaletta, desimaalia), jossa tieto siirretään aineistoon. 
Poimintasäännöt kirjoitetaan SQL-lausekkeina, käyttäen SQLiten muotoa. Poimintasääntöjen lähdeaineistona on käytettävissä eri tietokantatauluja. Kun aineistoa muodostetaan, käydään jokainen aineistomuodostuksessa valittu henkilö yksitellen läpi ja poimittavassa tietokantataulussa on tiedot vain kyseistä henkilöä koskien.
Poimintasäännöt kirjoitetaan SQL-muotoon:
[code]
    SELECT ... FROM <taulun nimi> WHERE ...
[/code]
SQL-kielestä voidaan käyttää myös muuta toiminnallisuutta kuten JOIN, aggrekaattifunktiot (SUM, COUNT, jne).
SQL-syntaksista ja toiminnallisuuksista voit tarkemmin lukea SQLiten [omasta dokumentaatiosta](<https://www.sqlite.org/docs.html>).
SQLiten toimintojen lisäksi palveluun on toteutettu [apufunktioita](<https://support.nepton.com/hc/fi/articles/360009018778>), joiden avulla voidaan helpommin käsitellä esimerkiksi merkkijonoja kuin käyttäen SQLiten toiminnallisuutta.
## Sääntöjoukon käyttäminen aineistosiirrossa
Sääntöjoukolla kuvataan poiminnan sisältö. Sääntöjoukon muodostamisen jälkeen aineisto voidaan ladata missä tahansa muodossa. Mikäli käytetty aineistomuoto käyttää sellaisia tietokenttiä, joita poimintasäännössä ei ole määritetty, siirtyvät ne aineistomuodosta riippuen oletusarvoisena tai tyhjänä.
Asetusryhmän ylätasolla määritetty sääntö on mahdollista korvata asettamalla aliryhmään toinen sääntö. Asetusryhmien selkeyden vuoksi emme suosittele tätä vaihtoehtoa. Ylätasolle muodostettava sääntö voi jo poissulkea tiedon poiminnan alaryhmässä. Tällöin käyttöympäristöön ei muodosteta alaryhmiin poikkeuksia, vaan kaikkia sääntöjoukon sääntöjä voidaan hallita yhtenä listana. Esimerkiksi jos tietyn palkkalajin muodostuminen halutaan estää alaryhmässä, niin yläryhmän sääntöön voidaan määritellä poissulkeva ehto alla olevan esimerkin mukaisesti. Tällöin sääntöjoukossa nähdään selkeästi aineiston muodostumisen säännöt kokonaisuudessaan ilman jakoa useiden asetusryhmien asetuksiin.
Esimerkki, jossa kysely kohdistetaan UserSalaryData-tauluun ja tuloksista jätetään pois henkilöt asetusryhmästä, jonka koodi on "tuntipalkkaiset urakkamiehet":
[code]
    SELECT ...,
    IFNULL(
      (SELECT
         uid.Value
       FROM
         UserInfoData uid
       WHERE
         uid.InfoTypeName = 'SettingGroupCode_SDSQL'
         AND DATETIME(usd.SalaryRenderingDate) BETWEEN ui.ValidFrom AND ui.ValidTo
       LIMIT 1), '') AS _SettingGroupCode
    FROM
      UserSalaryData
    WHERE
      SettingGroupCode != 'tuntipalkkaiset urakkamiehet'
[/code]
## Poiminnan ryhmittely - GROUP BY
GROUP BY -ehdolla voidaan ryhmitellä henkilölle muodostuva aineisto muilla ehdoilla. Ryhmittely laskee yhteen ne rivit, joissa poiminnan ryhmittelyyn määritetyt tiedot ovat samanlaisia. Liittymäajoissa aineisto muodostetaan aina henkilöittäin, minkä vuoksi useamman eri käyttäjän tietoja ei voi ryhmitellä yhteen ja aineisto tulee myös käyttäjien mukaan. Raporttiajoissa aineisto käsitellään aina kokonaisena jolloin voit ryhmitellä myös useamman käyttäjän tietoja yhteen ja määrittää niiden järjestyksen.
Pääsääntöisesti palkkajärjestelmiin viedään palkkaliittymässä aineisto siten, että se on ryhmitelty per säännöllä muodostettu palkkalaji (OverrideSalaryCode), per päivä (SalaryRenderingDate) ja mahdollisesti per projektit (ProjectCode1, ProjectCode2, ProjectCode3, ProjectCode4, ProjectCode5, ProjectCode6).  
  
Mikäli on tarpeen ryhmitellä aineisto esimerkiksi tapahtumatyypeittäin, voi ryhmittelyssä käyttää ActivityTypeCodea.
Mikäli taas palkkajärjestelmässä on tärkeää eritellä tapahtumalle tehty kuvaus, niin siinä tapauksessa ryhmitellään vielä per kuvaus (Comment).
## Poiminnan rajaaminen
### Rajaaminen WHERE-ehdossa
Jos on tarve rajata aineiston ulkopuolelle sellaisia tapahtumia tai esim. lisiä, joissa palkkalajikoodia ei ole asetettu, tällöin tulee sääntöön lisätä WHERE-ehtoon
[code]
    AND OverrideSalaryCode IS NOT NULL
[/code]
Sääntöjoukon WHERE-ehdossa voidaan rajata aineiston ulkopuolelle esimerkiksi hyväksymättömät tapahtumat tai palkkauksen mukaisesti esimerkiksi tuntipalkkaiset tai kuukausipalkkaiset tapahtumat:
[code]
    AND IsApproved = 'Y'
    AND employeesalarytype = 'hourly'
    AND employeesalarytype = 'monthly'
[/code]
Kun käytetään ehtoa IsApproved = 'Y', rajataan aineiston ulkopuolelle nimenomaan hyväksymättömät tapahtumat. Esimerkiksi automaattisesti kertymästä lainattua aikaa (ei tapahtumakirjausta) ei voi rajata aineistolta tällä ehdolla, sillä tällaista kertymästä lainattua aikaa ei ole mahdollista hyväksyä erikseen.
### Rajaaminen HAVING-lausekkeella
Palkkalaji on määritelty poimintasäännössä, tai se tulee esimerkiksi työlisän tai työkorotuksen asetuksista. Poiminnoissa voi määritellä, että palkkalajia 0 ei muodosteta aineistoon HAVING-säännöllä:
[code]
    HAVING
    OverrideSalaryCode != 0
[/code]
Asettamalla työkorotuksen-, työlisän- tai säännöstä muodostuvan palkkalajin nollaksi, se jätetään pois aineistosta.
## Poiminnassa käytettävä henkilön tunniste
Aineistossa muodostuu automaattisesti henkilön tunniste sen mukaisena kuin se on kuvattu liittymäkohtaisessa aineistokuvauksessa. Tämä tunniste voidaan korvata poimimalla säännössä toinen tunniste sarakkeeksi, esimerkiksi 'AS OverridePersonnelNumber'.
## Määrä poiminnassa
Määrä eli Amount muodostuu oletuksena sekunteina.  
Muutat sekunnit minuuteiksi esim. näin:
[code]
    SELECT *, Amount / 60 AS OverrideAmount
[/code]
Otettava huomioon, että vakioitu liittymä tekee muutoksia määrien tulkintaan (tulkitaanko vastaanottavassa päässä sekunteina/minuutteina/tunteina)
Voit tarvittaessa muuntaa sekuntit 'HH:MM' muotoiseksi merkkijonoksi seuraavalla tavalla
[code]
    SELECT
      *,
      CONCAT(PRINTF('%02d', Amount / 3600), ':', PRINTF('%02d', Amount % 3600 / 60)) AS OverrideAmount
[/code]
## Override-sarakenimen käyttö
Kun tietoa siirretään, tietokentät saavat automaattisesti sen sisällön, joka siirrettävässä aineistomuodossa on määritetty. Minkä tahansa kentän arvo voidaan korvata poimimalla SQL-säännöllä sarake, jonka nimi sisältää tekstin Override+sarakkeen nimi.
Esimerkiksi useassa liittymässä siirretään tunti- tai kappalemääriä. Tulkinta voi muodostaa useita rivejä samalle päivälle ja usein näitä tuloksia halutaan laskea yhteen päivätasolla. Tällöin siirtyvä sarake 'Amount' voidaan korvata uudella arvolla poimimalla sisältö sarakkeeksi 'OverrideAmount'.
[code]
    SELECT *, SUM(Amount) AS OverrideAmount
[/code]
Vastaavalla tavalla esimerkiksi kommenttikenttään voi liittää muutakin tietoa muodostamalla kyselyssä sarakkeen 'OverrideComment'. Siirtoaineiston sisältämä kenttä voidaan korvata käyttämällä tätä override-sarakenimeä. Tarkemmat tiedot sarakkeiden nimistä on esitetty liittymäkohtaisissa kuvauksissa [täällä](<https://support.nepton.com/hc/fi/articles/360002494538>).
## Käsiteltävän ajanjakson määrittely
Sääntöjoukon poimintasäännöt poimivat sisältöä aina joltakin ajanjaksolta. Käsiteltävä ajanjakso määritellään joko [sääntöjoukon siirron automatisointi - artikkelissa](<https://support.nepton.com/hc/fi/articles/360002492458>) tai käyttöliittymässä sääntöjoukon tuloksia noudettaessa. Poimintasäännöt kohdistuvat käsiteltävään ajanjaksoon ja palauttavat tulokset siltä ajanjaksolta.
Tapahtumia voidaan poimintasäännössä rajata :exportPeriodStart ja :exportPeriodEnd -muuttujilla. :exportPeriodStart korvataan kyselyä suoritettaessa käsiteltävän jakson alkupäivällä YYYY-MM-DD HH:MM:SS -muotoisena. Vastaavasti :exportPeriodEnd korvataan vietävän jakson loppupäivällä.
Alla esimerkki, jossa poimintaa rajataan kyseisillä muuttujilla.
[code]
    WHERE
      DATE(EventStartDateTime) BETWEEN :ExportPeriodStart AND :ExportPeriodEnd
[/code]
## Asetusryhmät ja niiden voimassaolon vaikutus poiminnassa
Jos asetusryhmä vaihtuu kesken poimintajakson, käytetään poiminnassa sitä asetusryhmää, joka on voimassa poimintajakson viimeisenä päivänä. Tämä voi tulla kyseeseen esimerkiksi palkkalajikoodin kohdalla, joka on ainoa määritys aliasetusryhmän poimintasäännössä.
Tämän voi kiertää asettamalla palkkalajikoodin siinä poimintasäännössä, joka on ylimmällä tasolla.
Alla olevassa esimerkissä poimitaan palkkalajille koodi perustuen asetusryhmän koodin arvoon. Lisäehtona WHERE-ehdossa on työ-tapahtumatyypit, säännöllisenä työaika sekä kukausipalkkaisuus.
[code]
    SELECT
      *, 
      SUM(Amount) As OverrideAmount,
      CASE
        WHEN uid.Value = '12h_kp' THEN 105
        WHEN uid.value IN ('12h', '3-vuoro','28') THEN 5
        WHEN uid.value IN ('2-vuoro', 'Keskeytymätön 2-vuoro') THEN 6
        ELSE 1
      END AS OverrideSalaryCode
    FROM 
      UserSalaryData usd
    LEFT JOIN UserInfoData uid ON
      usd.UserId = uid.UserId
      AND InfoTypeName = 'SettingGroupCode_SDSQL'
      AND usd.SalaryRenderingDate BETWEEN DATE(uid.ValidFrom) AND DATE(uid.ValidTo)
    WHERE 
      CompensationType = 'BasicTime' 
      AND BasePartTarget = 'salary'
      AND OvertimeTarget IS NULL
      AND ActivityTypeCategoryId = 1 
      AND EmployeeSalaryType = 'monthly' 
    GROUP BY
      SalaryRenderingDate,
      ProjectCode1
[/code]
## Poimintasäännön voimassaolo ja siihen liittyvät ongelmatilanteet
Poimintasäännöille voi asetusten tapaan määrittää voimassaolon, mikä mahdollistaa säännön toiminnan muuttamisen tietyn päivän kohdalla. Jos sääntö on määritetty asetusryhmätasolle, voi sääntö henkilön kohdalla muuttua myös sen takia, että henkilö on vaihdettu toiseen asetusryhmään. Järjestelmä käsittelee tilanteet, joissa sääntö on voimassa vain osan valitusta ajanjaksosta tai muuttuu sen aikana.
![](https://support.nepton.com/hc/article_attachments/21186042411293)
Jos käyttäjän kohdalla esiintyy kuvanmukainen tilanne, järjestelmä ajaa säännön ensimmäisen version päiville 1. - 9. ja säännön toisen version 10. päivälle ja siitä eteenpäin. Kummankin sääntöversion tuottamat rivit lisätään lopputulokseen. Jos yhdessä tai molemmissa säännöistä on käytetty jonkinlaista ryhmittelyä tai rivien yhdistämistä (esim. yhteenlaskettu tuntimäärä per henkilö), voi rivien lisääminen kummastakin tuottaa ei-halutun lopputuloksen. Järjestelmä lisää lokiin varoitusviestin tällaisesta tilanteesta.
**![](https://support.nepton.com/hc/article_attachments/21186009276701)**
Jos ylläolevan kuvanmukainen tilanne esiintyy ajetaan käyttäjän työaikatiedot säännön mukaisesti, mutta vain päiville 1. - 9. Lokiin jää viesti tällaisesta tilanteesta. Poimintasäännöstä ja käytettävästä liittymästä riippuen siirtotiedostosta ei välttämättä käy ilmi, että tiedot on poimittu vain osasta valittua ajanjaksoa.
Joskus voi olla tarpeen välttää tilanteita, joissa sääntö muuttuu kesken raportointijakson. Säännön muuttumista kesken raportointijakson voi välttää seuraavasti:
  * Määritä sääntö työyhteisön asetuksiin. Työyhteisötasolle määritetty sääntö ei muutu vaikka henkilöitä siirrellään asetusryhmien välillä. UserInfo-taulun avulla on mahdollista säännössä poimia vain ne tuntimerkinnät, joiden aikana henkilö kuului esim. tiettyyn palkkaryhmään. Myös asetusryhmää voi käyttää tässä, mutta sääntökyselyn ehtolausekkeessa voi määrittää vain aliryhmiä.
  * Jos sääntöä tarvitsee muuttaa, aseta muutos voimassaolotyökalua käyttäen niin, että se tapahtuu raportointijaksojen välissä. Esim. jos tiedot siirretään kuukausi kerrallaan tulisi säännön muutos asettaa voimaan kuun alussa.


## Ero UserEventData- ja UserSalaryData-taulujen ajan määrässä
Kun tapahtuma merkitään palveluun, merkitty aika on taulussa UserEventData ja ajasta muodostettu tieto taulussa UserSalaryData. Molemmissa tauluissa on kenttä MarkedTime, mutta niiden arvot voivat poiketa toisistaan riippuen siitä, onko tapahtuma tehty reaaliaikaisena eli ns. kellotettuna vai ei.
Reaaliaikasesti merkityn tapahtuman alku- ja loppuajassa on mukana myös sekuntiosuus, esim. alku 08:02:57 ja loppu 16:13:12. Vastaava merkintä ei-reaaliaikaisena olisi alku 08:02:00 ja loppu 16:13:00. UserEventData-taulussa olisi määrä (Amount) 08h10min15sek, UserSalaryData-taulussa määrä olisi 08h11min00sek eli 45 sekuntia enemmän. Tällä on harvoin merkitystä, mutta mikäli tietoja poimitaan molemmista tauluista, saattaa olla tarve saada sama määrä riippumatta tapahtuman merkintätavasta.
Alla olevalla esimerkillä saadaan UserEventData- ja UserSalaryData-taulusta poimittua sama määrä riippumatta tapahtuman merkintätavasta.
[code]
    CAST(strftime('%s', strftime('%Y-%m-%d %H:%M:00', EndDateTime)) AS INT)
    - CAST(strftime('%s', strftime('%Y-%m-%d %H:%M:00', StartDateTime)) AS INT)
[/code]
## Ajat ja aikavyöhykkeet
Tapahtumien ja palkkatietojen alku- ja päättymisajat tallennetaan ja noudetaan "kuten ne on kirjattu" eli käyttäjän tarkoituksen mukaisesti. On tärkeää huomata, että emme välttämättä tiedä aikavyöhykettä, jolla aika on tallennettu, ellei tätä tietoa ole määritelty palveluun.
Esimerkkejä löydät ohjeesta [Aikavyöhykkeet ja tapahtumien luonti.](<https://support.nepton.com/hc/fi/articles/360003994357>)
On myös tärkeää huomata, että sääntöjoukon kysely käyttää SQLitea, jonka päivämäärä- ja aika-avustajat käyttävät oletusarvoisesti UTC-aikastandardia.
Tästä seuraa, että jos käytät kyselyssä käsitettä 'nyt' tai CURRENT_TIMESTAMP hakeaksesi nykyisen ajan ja sen muodon, se näytetään 2-3 tuntia todellisesta ajasta jäljessä (olettaen, että olet Suomen aikavyöhykeellä ja riippuen siitä, vaikuttaako kesäaika).
Alla esimerkki mahdollisesti ongelmallisesta kyselystä, joka palauttaa tiedot vain kuun 1. päivänä:
[code]
    SELECT * FROM UserEventData WHERE strftime('%d', 'now') = '01'
[/code]
Koska strftimelle ei anneta aikavyöhyketietoja, se käyttää UTC-aikaa ja sen jälkeen kysely ei palauta tuloksia, jos se suoritetaan 00:00 ja 02:00 välillä 1. päivänä (Suomessa). Voimme tarjota palvelun paikallisen aikavyöhykkeen tämän odottamattoman toiminnan korjaamiseksi mm:
[code]
    SELECT * FROM UserEventData WHERE strftime('%d', 'now', 'localtime') = '01'
[/code]
Lisätietoja UTC:stä ja aikavyöhykkeistä SQLitessa löytyy [SQLiten omasta dokumentaatiosta](<https://www.sqlite.org/lang_datefunc.html>).
## Rajoituksia
### Kirjainkoolla on merkitystä muilla kuin ASCII-merkeillä
Jos esimerkiksi poimitaan tapahtumatyypin koodin perusteella, kun koodina on YÖ, koodin jälkimmäinen merkki tulee esittää samalla kirjainkoolla millä se on tapahtumatyypin koodiin asetettu.
Esimerkiksi seuraava lauseke toimii, koska tapahtumatyypin koodin  _Ö_ -merkki on kyselyssä isolla kirjankoolla. Pienellä kirjainkoolla kysely ei toimisi:
[code]
    SELECT * FROM UserSalaryData
    
    WHERE CompensationType = 'BasicTime' AND ActivityTypeCode = 'YÖ'
[/code]
Voit lukea enemmän ASCII-merkeistä / merkistöstä [Wikipedian artikkelista](<https://fi.wikipedia.org/wiki/ASCII>).
### Uusia tietotyyppejä saatetaan lisätä myöhemmin
Joihinkin tietokantatauluihin saatetaan lisätä rivejä ja uusia tietotyyppejä järjestelmän päivityksissä. Mikäli kyselyssä rajataan tietoja jonkin tyypin perusteella, kannattaa rajaus tehdä niin, ettei kysely ala päivityksen jälkeen poimimaan myös uusia tietotyyppejä. 
Esimerkiksi seuraavissa lausekkeissa on riskinä, että ne poimivat myös jonkin myöhemmin lisätyn työaikatulkinnan.
[code]
    SELECT * FROM UserSalaryData WHERE CompensationType != 'BasicTime';
    
    SELECT * FROM UserSalaryData WHERE CompensationType NOT IN ('PublicHoliday', 'MarkedTime');
[/code]
