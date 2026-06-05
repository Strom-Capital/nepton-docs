---
id: 10758741671581
title: Mukautetut Työajan viennit
url: https://support.nepton.com/hc/fi/articles/10758741671581-Mukautetut-Ty%C3%B6ajan-viennit
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä liittymistä
section_id: 360002325398
section_path:
- Liittymät
- Yleistä liittymistä
labels:
- raportti
- kustomoitu raportti
- customized report
promoted: false
updated_at: '2026-02-23T11:05:14Z'
edited_at: '2026-02-23T11:05:14Z'
---

# Mukautetut Työajan viennit

Haluatko luoda omiin tarpeisiisi räätälöityjä raportteja? [Lue täältä Muokattavista raporteista](<https://support.nepton.com/hc/fi/articles/19801354657309>), joiden avulla voit luoda organisaatiollesi omia raportteja haluamiesi tietojen pohjalta ja jakaa ne helposti esimerkiksi esihenkilöille ja työntekijöille. Käyttäjät näkevät vain omiin oikeuksiinsa kuuluvat tiedot, mikä varmistaa tietoturvallisen raportoinnin.
## Esittely
Mukautetun viennin avulla voit viedä työajan tietoja valitsemasi rakenteen mukaisena taulukkotiedostona muihin ohjelmistoihin. Voit mukauttaa tiedoston sisältöä ja formaatia tarpeidesi mukaan, jolloin tietojen siirtäminen eri järjestelmiin on helppoa ja joustavaa. Näet viennin tukemat tiedostotyypit [täältä](<https://support.nepton.com/hc/fi/articles/10510800700573>).
Viennin asetukset mahdollistavat useita tapoja siirtää tietoa:
  * **Manuaalinen vienti** : Taulukko voidaan ladata määritetyillä käyttäjillä ja päivämäärillä välittömästi kohdasta _Työaika > Hallinta > Liittymät > Mukautettu vienti._
  * **Ajastettu vienti** : Vienti voidaan asettaa suorittamaan säännöllisesti ja toimittamaan tiedosto automaattisesti joko SFTP-palvelimelle tai haluttuihin sähköpostiosoitteisiin. Määritykset tehdään kohdassa _Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Liittymien ajastus _(ohje ajastamiseen [täällä](<https://support.nepton.com/hc/fi/articles/10510800700573>)).
  * **API-rajapinta** : Työajan tietojen siirtäminen voidaan toteuttaa myös API-rajapintaa hyödyntämällä ajamalla sääntöjoukko [tämän](<https://support.nepton.com/hc/fi/articles/360014449458>) ohjeen mukaisesti.


## Tuetut tiedostomuodot
  * .**CSV** \- Yksinkertainen taulukkotiedostomuoto, joka on yhteensopiva useiden järjestelmien kanssa, mukaan lukien yleiset taulukkolaskentaohjelmat kuten Microsoft Excel, Libre Calc tai Open Office Calc. Tämä on hyvä vaihtoehto tietojen viemiseksi muihin järjestelmiin, sillä se on laajasti tuettu ja helppo käsitellä eri sovelluksissa.
  * .**XLSX** \- Paras tiedostomuoto viedyn tiedon katseluun suoraan Microsoft Excelissä. Tukee maksimissaan 1 048 576 rivin viemistä tiedostoon.


## Määritykset
**Viennin asetukset** (löytyvät poimintasääntökohtaisesti sivun alalaidasta) tulee tehdä työyhteisötasolle.
  1. Mukautettu vienti vaatii että integraation sääntöjoukko on asetettu, joka määrittää haettavat tiedot integraatiokyselyillä. Vähintään yksi palkkalajikoodi ja kysely pitää sisältyä sääntöjoukkoon, mutta niitä voidaan lisätä useita. Katso [integraation sääntöjoukot](<https://support.nepton.com/hc/fi/sections/360000827378>) \- osiosta lisätietoja.  
  
**![fi-me.png](https://support.nepton.com/hc/article_attachments/10791123562141)**  
  

  2. Sarakemääritykset tulee määrittää samassa sääntöjoukossa siten että jokainen sarakkeen nimi vastaa joko mukautettua saraketta joka on määritetty kyselyssä, tai kenttää joka tulee automaattisesti sääntöjoukon tuloksissa, esimerkiksi:  
![fi-tr.png](https://support.nepton.com/hc/article_attachments/10791199664797)  
Arvojen muotoilu ja muuntaminen (esimerkiksi sekunteina olevan arvon muuttaminen tunneiksi desimaaleina) tulee määrittää sääntöjoukon kyselyissä eikä sarakemäärityksissä. Oletuksena sekunnit kuitenkin muunnetaan desimaalimuotoisiksi tunneiksi.  
  
Voit myös asettaa haluatko sisällyttää sarakkeiden otsikot taulukkotiedoston ensimmäisellä rivillä asettamalla "Sisällytä otsikkorivi viennissä" kohtaan "Kyllä".  

  3. Jos haluat käyttää CSV-muotoista tiedostoa, tulee tiedoston muodon määäritykset asettaa. Jos olet epävarma että mitkä määritykset ovat oikeat, niin yleensä alla olevat määritykset toimivat hyvin:  
![custom-export-csv-settings-fi.png](https://support.nepton.com/hc/article_attachments/25737171741213)Asetuksella "Sisällytä rivinvaihtomerkki vientitiedoston viimeiselle riville" voidaan määrittääkö, muodostuuko tiedoston loppuun yksi tyhjä rivi. Joihinkin järjestelmiin tietoa siirrettäessä voi olla välttämätöntä käyttää tätä asetusta. 
  4. Voit testata vientitiedostoa ajamalla sen manuaalisesti Työaika > Hallinta > Liittymät - sivulta, tai luomalla [ajastuksen](<https://support.nepton.com/hc/fi/articles/10510800700573>) ja painamalla "Suorita nyt".  
_Huom: Vain henkilöt joilla on voimasssa oleva henkilönumero sisällytetään vietyihin tietoihin_  
 _![](https://support.nepton.com/hc/article_attachments/21080324377757)_  



## Esimerkki mukautetusta työajan viennistä
Alla olevassa esimerkissä haetaan taulukolle tietoja **UserInfoData** -tietokantataulusta (henkilönumero ja henkilöryhmä) sekä **UserSalaryData** -tietokantataulusta (päivämäärä ja summa tietyntyyppisestä tulkitusta työajasta kyseisenä päivänä). Voit lukea lisää eri tietokantatauluista saatavilla olevasta datasta [tästä artikkelista](<https://support.nepton.com/hc/fi/articles/360002489257>).
Kyseisellä työajan viennillä on tarkoitus raportoida sellaiset työpäivät, jolloin säännöllisenä työnä tulkittua työaikaa on kirjattu yli kuusi tuntia eikä samana päivänä ole lounastaukoa.
[code]
    SELECT
      uid.Value AS 'Henkilönumero', 
      uid2.Value AS 'Henkilöryhmä', 
      Salaryrenderingdate AS 'Pvm', 
      SUM(Amount) / 3600 AS 'Säännöllisen työajan tunnit' 
    FROM 
      Usersalarydata usd 
      LEFT JOIN UserInfoData uid ON usd.UserId = uid.UserId 
      AND uid.InfoTypeName = 'PersonnelNumber'
      AND datetime(usd.SalaryRenderingDate) BETWEEN Uid.ValidFrom AND uid.ValidTo
      LEFT JOIN UserInfoData uid2 ON usd.UserId = uid2.UserId 
      AND uid2.InfoTypeName = 'UserGroupName_SDSQL' 
      AND datetime(usd.SalaryRenderingDate) BETWEEN Uid2.ValidFrom AND uid2.ValidTo 
    WHERE 
      CompensationType IN ('Basictime') 
      AND ActivitytypecategoryID = 1 
      AND SalaryRenderingDate NOT IN (
        SELECT 
          SalaryrenderingDate 
        FROM 
          UserSalaryData 
        WHERE 
          CompensationType = 'Lunch')
          AND istimeborrowedfrombalance = 'N' 
    GROUP BY 
      uid.value, 
      Salaryrenderingdate 
    HAVING 
      SUM(Amount) > 21600
[/code]
