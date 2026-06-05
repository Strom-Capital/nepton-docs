---
id: 360006255458
title: Sääntöjoukon tuloksen jakaminen useaan tiedostoon
url: https://support.nepton.com/hc/fi/articles/360006255458-S%C3%A4%C3%A4nt%C3%B6joukon-tuloksen-jakaminen-useaan-tiedostoon
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels: []
promoted: false
updated_at: '2024-11-01T11:58:17Z'
edited_at: '2024-11-01T11:58:17Z'
---

# Sääntöjoukon tuloksen jakaminen useaan tiedostoon

Sääntöjoukon tulokset on mahdollista jakaa useaan tiedostoon. Tätä voidaan tarvita esimerkiksi seuraavissa tapauksissa:
  * _Jaa tulokset tiedostoihin kustannuspaikoittain_ \- jokaiselle kustannuspaikalle luodaan oma tiedostonsa, katso esimerkki 1
  * _Jaa tulokset tiedostoihin projekteittain_ \- jokaiselle projektille luodaan oma tiedostonsa
  * _Tiedostot jaetaan sisältämään tulokset siten että tiedostot sisältävät siihen määritellyt kustannuspaikat_ \- katso esimerkki 2
  * _Jaa tulokset tiedostoihin maksuryhmittäin_ \- jokaiselle maksuryhmälle luodaan oma tiedostonsa, katso esimerkki 3


Huomioi että tyhjiä tiedostoja ei luoda. Jos tulokset jaetaan oletuskustannuspaikan mukaan ja oletuskustannuspaikka-dataa ei ole, tiedostoa ei luoda.
## Vientitiedoston osiin jakamisen asetukset
Asetus "Jaa tulokset" koskee vain Visma LTR toteutuksia.
![20210112-support-export-file-splitting-1.PNG](https://support.nepton.com/hc/article_attachments/360015796517)
Asetukset vientitiedoston osiin jakamiselle löytyvät sääntöjoukkojen asetuksista sääntöjoukkojen kyselyiden asetusten jälkeen. Vähintään kohdat 'Jaa tiedostoihin arvoilla*' sekä ' Jaa "Palkka-aineiston taulu" tiedot seuraavasti' tulee täyttää. 
Huomio: sääntöjoukon kyselyssä käytetyn taulun jakamisen asetukset eivät saa olla tyhjiä. Jos esimerkiksi sääntöjoukon kyselyssä käytetään taulua UserEventData, tulee myös Jaa "Tapahtumataulu" tiedot seuraavasti -asetus olla käytössä. Muuten sääntöjoukon kysely ei palauta tähän tauluun liittyviä tietoja.
Alla kuvattuna osiin jakamisen asetukset:
  1. Jaa tiedostoihin arvoilla - Tällä asetuksella määritetään määrätyt arvot/käsitteet, joiden mukaan data jaetaan tiedostoihin. Tämän ei tarvitse olla olemassa oleva arvo viennin sääntöjoukoissa, mutta sen tulee olla yksittäinen sarake, jossa on uniikki arvo jota voidaan hyödyntää seuraavien kohtien asetuskyselyissä.  
  

  2. Jaa "Palkka-aineiston taulu" tiedot seuraavasti", Jaa "Tapahtumataulu" tiedot seuraavasti ja Jaa "Tapahtumahistoriataulu" tiedot seuraavasti" - Nämä asetukset määrittävät datan, joka on saatavilla jokaiselle tiedostolle, ja jonka perusteella tiedostot jaotellaan. Jaottelu tehdään arvojen perusteella, jotka saadaan kohdan 1 kyselyn (Jaa tiedostoihin arvoilla) tuloksesta. Kyselyn 1 palauttamat arvot ovat saatavilla muuttujassa `:splittingValue` ja kysely toistetaan jokaiselle palautetulle arvolle.  
  

  3. Jaetun tiedoston nimi - Vapaavalintainen: Jaetun tiedoston nimen kaavan asetus. Arvoa `[SplittingValue]` voi käyttää tiedoston nimen kaavassa korvaavana tietona. Tällöin jos tulokset jaetaan oletuskustannuspaikan mukaan, tämä kaava korvataan tiedostonimeen oletuskustannuspaikalla.  
  
Jos esimerkiksi halutaan tiedostoja, jotka alkavat korvattavalla kaavalla, asetetaan: `[SplittingValue]_exportToSomeSystem.csv`  
  
Tällöin jos esimerkiksi tiedot jaotellaan kahden kustannuspaikan kesken, joiden koodit ovat 1200 ja 9001, tiedostojen nimiksi muodostuu `1200_exportToSomeSystem.csv` and `9001_exportToSomeSystem.csv`  
Käytettävissä olevat korvauskuviot. Huomaathan, että kaikki formaatit ovat suomenkielisessä muodossa.  
\- **[vvvvkkpphhmmss]** Päivämäärä ja aika, esimerkiksi 20181201120000  
\- **[vvvvkkpphhmm]** Päivämäärä ja aika ilman sekunteja, esimerkiksi 201812011200  
\- **[vvvvkkpp]** Päivämäärä, esimerkiksi 20181201  
\- **[SplittingValue]** Arvo, joka muodostetaan kyselyllä kohdassa "Jaa tiedostoihin arvoilla"  
  

  4. "Vie tiedostot zip-muodossa" - Määrittää viedäänkö jaetut tiedostot SFTP-palvelimelle yhtenä zip-muotoiseksi pakattuna tiedostona vai pakkaamattomina erillisinä tiedostoina. Määritys koskee ainoastaan sftp-siirtoja, ei aineiston lataamista käyttöliittymässä.


## Esimerkki 1 - Tulosten jaottelu kustannuspaikoittain erillisiin tiedostoihin
Näillä asetuksilla tulokset jaetaan tiedostoihin siten että jokaiselle sääntöjoukon tulosten löytämälle kustannuspaikalle luodaan oma tiedostonsa. Esimerkiksi jos tulokset sisältävät henkilöitä, jotka kuuluvat kustannuspaikkoihin **A** , **B** ja **D** , näiden henkilöiden tulokset jaotellaan kolmeen tiedostoon:
  1. Tiedosto "**A** _xxxxx.csv", joka sisältää kustannuspaikkaan A kuuluvien henkilöiden tulokset
  2. Tiedosto "**B** _xxxxx.csv", joka sisältää kustannuspaikkaan B kuuluvien henkilöiden tulokset
  3. Tiedosto "**D** _xxxxx.csv", joka sisältää kustannuspaikkaan D kuuluvien henkilöiden tulokset


Jos on olemassa muita kustannuspaikkoja, joiden henkilöitä sääntöjoukon tulokset eivät palauttaneet, näille kustannuspaikoille ei luoda omaa tiedostoa. Myös esimerkiksi tiedostoa "**A** _xxxxx.csv" ei luoda, jos tulokset eivät sisällä yhtään dataa kustannuspaikan A henkilöille.
"Jaa tiedostoihin arvoilla*" -kysely:
[code] 
    SELECT DISTINCT IFNULL(Value, '') FROM UserInfoData WHERE InfoTypeName = 'DefaultCostGroupCode'
[/code]
"Jaa Palkka-aineiston taulu tiedot seuraavasti*" -kysely:
[code] 
    SELECT * FROM UserSalaryData WHERE IFNULL(UserCostGroup, '') = :splittingValue
[/code]
"Jaa Tapahtumataulu tiedot seuraavasti*" -kysely:
[code] 
    SELECT * FROM UserEventData WHERE IFNULL(UserCostGroup, '') = :splittingValue
[/code]
"Jaa Tapahtumahistoriataulu tiedot seuraavasti*" -kysely:
[code] 
    SELECT * FROM UserEventHistoryData WHERE IFNULL(UserCostGroup, '') = :splittingValue
[/code]
## Esimerkki 2 - Tulosten jakaminen määritettyjen kustannuspaikkojen mukaan
Näillä asetuksilla tulokset jaetaan kahteen tiedostoon, joista:
  1. "FileOne" sisältää tulokset kustannuspaikoista **A** , **B** ja **C** ,
  2. ja "FileTwo" sisältää tulokset kustannuspaikoista **D** ja **E**


"Jaa tiedostoihin arvoilla*" -kysely:
[code] 
    SELECT DISTINCT CASE  
    WHEN Value IN('A', 'B', 'C') THEN 'FileOne'  
    WHEN Value IN('D', 'E') THEN 'FileTwo'  
    END  
    FROM UserInfoData  
    WHERE InfoTypeName = 'DefaultCostGroupCode'
[/code]
"Jaa Palkka-aineiston taulu tiedot seuraavasti*" -kysely:
[code] 
    SELECT   
    *   
    FROM UserSalaryData   
    WHERE   
    CASE   
    WHEN UserCostGroup IN('A', 'B', 'C') THEN 'FileOne'   
    WHEN UserCostGroup IN('D', 'E') THEN 'FileTwo'  
    END = :splittingValue
[/code]
Huomio: Sekä "Jaa tiedostoihin arvoilla**" että "Jaa Palkka-aineiston taulu tiedot seuraavasti*" -kyselyt tulee määrittää asetuksiin.
Huomio: Määritettyjä kustannuspaikkoja ja muodostettavien tiedostojen määrää voidaan muuttaa, samoin 'FileOne' ja 'FileTwo' (jotka tulevat kyselyn palauttamien tiedostojen etuliitteiksi) voidaan muuttaa, mutta kyselyiden ehtojen ja tiedostonimien pitää täsmätä molemmissa kyselyissä.
## Esimerkki 3 - Tulosten jakaminen maksuryhmän perusteella
"Jaa tiedostoihin arvoilla*" -kysely:
[code] 
    SELECT DISTINCT IFNULL(uid.Value, '')   
    FROM UserData as u   
    LEFT JOIN userinfodata AS uid ON (  
        u.userId = uid.userId AND  
        uid.InfoTypeName = 'NeptonPaymentGroupName_SDSQL'  
    )
[/code]
"Jaa Palkka-aineiston taulu tiedot seuraavasti*" -kysely:
[code] 
    SELECT usd.*   
    FROM UserSalaryData AS usd   
    LEFT JOIN UserInfoData as uid ON (  
        usd.userId = uid.userId AND  
        uid.InfoTypeName = 'NeptonPaymentGroupName_SDSQL' AND  
        datetime(usd.salaryrenderingdate) BETWEEN uid.ValidFrom AND uid.ValidTo  
    )   
    WHERE IFNULL(uid.value, '') = :splittingValue
[/code]
"Jaa Tapahtumataulu tiedot seuraavasti*" -kysely:
[code] 
    SELECT ued.*  
    FROM UserEventData AS ued   
    LEFT JOIN UserInfoData as uid ON (  
        ued.userId = uid.userId AND  
        uid.InfoTypeName = 'NeptonPaymentGroupName_SDSQL' AND  
        datetime(ued.startdatetime) BETWEEN uid.ValidFrom AND uid.ValidTo  
    )   
    WHERE IFNULL(uid.value, '') = :splittingValue
[/code]
"Jaa Tapahtumahistoriataulu tiedot seuraavasti*" -kysely:
[code] 
    SELECT ued.*   
    FROM UserEventHistoryData AS ued   
    LEFT JOIN UserInfoData as uid ON (  
        ued.userId = uid.userId AND  
        uid.InfoTypeName = 'NeptonPaymentGroupName_SDSQL' AND  
        datetime(ued.startdatetime) BETWEEN uid.ValidFrom and uid.ValidTo  
    )   
    WHERE IFNULL(uid.value, '') = :splittingValue
[/code]
Tässä esimerkissä tiedostojen jakoarvona käytetään maksuryhmän nimeä mutta pienillä muokkauksilla (jokin muu InfoTypeName) saisi näillä ehdoilla jakamisarvona käytettyä esim. maksuryhmän koodia.
Jälkimmäinen parametri lauseessa: `IFNULL(uid.value, '')` asettaa ilman maksuryhmää oleville tyhjän merkkijonon mutta ilman ryhmää oleville voi käyttää jotain muutakin merkkijonoa.
Huomaa että kummatkin esitetyt muutosvaihtoehdot pitää asettaa samalla tavoin kaikkiin jakamiskyselyihin
## Esimerkki 4 - Tulosten jakaminen kiinteiden arvojen perusteella
Näillä asetuksilla tulokset jaetaan kahteen tiedostoon, joista:
  * "monthly" sisältää kuukausipalkkaisten henkilöiden tulokset
  * "hourly" sisältää tuntipalkkaisten henkilöiden tulokset


"Jaa tiedostoihin arvoilla*" -kysely:
[code] 
    SELECT * FROM (VALUES ('monthly'), ('hourly'));
[/code]
"Jaa Palkka-aineiston taulu tiedot seuraavasti" -kysely:
[code] 
    SELECT *   
    FROM UserSalaryData  
    WHERE EmployeeSalaryType = :splittingValue
[/code]
"Jaa Tapahtumataulu tiedot seuraavasti" -kysely:
[code] 
    SELECT *   
    FROM UserEventData  
    WHERE EmployeeSalaryType = :splittingValue
[/code]
"Jaa Tapahtumahistoriataulu tiedot seuraavasti" -kysely:
[code] 
    SELECT *   
    FROM UserEventHistoryData  
    WHERE EmployeeSalaryType = :splittingValue
[/code]
## Useamman tiedoston käsittely viennissä
  * Manuaalinen vienti käyttöliittymässä - tiedostot pakataan ZIP-arkistoon
  * Ajastettu vienti - tiedostot pakataan ZIP-arkistoon
  * Julkinen Web service - ZIP-arkisto sisällytetään _ResponseString_ -elementtiin base64-enkoodattuna 


### Miten jaottelu toimii
Kun tulokset jaotellaan useaan tiedostoon, käytännössä datan luonnissa ja jaottelussa on kolme vaihetta:
  1. Haetaan arvot, joiden mukaan jaottelu tehdään, esimerkiksi oletuskustannuspaikka (yksi tiedosto per kustannuspaikka)
  2. Luodaan väliaikaiset taulut UserSalaryData ja UserEventData joihin populoidaan jaotteluarvon mukainen data (esimerkiksi tietty oletuskustannuspaikka). Tämä tehdään jokaiselle vaiheessa 1 saadulle arvolle.
  3. Suoritetaan sääntöjoukon kyselyt tauluille jotka ovat luotu vaiheessa 2.
