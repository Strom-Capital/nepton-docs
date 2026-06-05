---
id: 360009018778
title: Sääntöjoukon apufunktiot
url: https://support.nepton.com/hc/fi/articles/360009018778-S%C3%A4%C3%A4nt%C3%B6joukon-apufunktiot
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels:
- pyöristys
- pyöristäminen
promoted: false
updated_at: '2026-03-09T08:30:12Z'
edited_at: '2026-03-09T08:30:12Z'
---

# Sääntöjoukon apufunktiot

Kirjoitettaessa sääntöjoukon poimintasääntöjä, käytettävissä on SQL Liten toimintojen lisäksi palveluun toteutettuja apufunktioita. Apufunktioiden avulla, SQL Litella on helpompi käsitellä esimerkiksi merkkijonoja.
### Luettelo käytettävissä olevista apufunktioista ja niiden toiminnasta
  * **substring_part**. Parametrit: (sourceString, separator, index). Funktio jakaa annetun merkkijonon sourceString annetulla erotinmerkkijonolla separator. Paluuarvona muodostuu niin mones tietosisältö kuin index arvo osoittaa. Mikäli merkkijono ei sisällä tätä elementtiä niin palautetaan NULL. Negatiivinen index palauttaa indeksin osoittaman elementin laskettuna viimeisistä tuloksista. -1 palauttaa viimeisen elementin, -2 palauttaa toiseksi viimeisen ja niin edelleen.  

  * **substring_index()** <https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_substring-index>  

  * **sql_left()** <https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_left>  

  * **sql_right()** <https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_right>  

  * **concat()** <https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_concat>  

  * **if()**<https://dev.mysql.com/doc/refman/8.0/en/flow-control-functions.html#function_if>  

  * **timestamp()** <https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_timestamp>  

  * **strftime(format, timestring)** Palauttaa merkkijonon, joka on muotoiltu annetun muodon mukaan. Esimerkiksi strftime('%Y %m %d', 'now', 'localtime') poimisi vuoden, kuukauden ja päivän nykyiselle päivämäärälle, paikallisen ajan mukaan. Jos esimerkiksi mukautetun viennin päivämääräformaattia halutaan muuttaa pisteelliseksi, niin se onnistuisi tällaisella komennolla: STRFTIME('%d.%m.%Y', SalaryRenderingDate) AS 'Tapahtumapäivä'  

  * **curdate()** Palauttaa nykyisen päivämäärän palvelimen paikallisen aikavyöhykkeen mukaan (Suomi). Muoto VVVV-KK-PP  

  * **curtime()** Palauttaa nykyisen ajan palvelimen paikallisen aikavyöhykkeen mukaan (Suomi). Muoto H:i:s  

  * **now()** Palauttaa nykyisen päivämäärän ja kellonajan palvelimen paikallisen aikavyöhykkeen (Suomi) mukaan. Muoto VVVV-KK-PP HH:MM:SS  

  * **weekday(date/datetime/timestamp)** Palauttaa viikonpäivän numerona annetun päivämäärän tai kellonajan perusteella. 0 (maanantai) - 6 (sunnuntai). Jos esimerkiksi haluat suodattaa pois lauantait ja sunnuntait, voit lisätä koodiin seuraavan rivin: AND weekday(salaryrenderingdate) NOT IN (5, 6)  

  * **ceil(decimal)** Pyöristä desimaali ylöspäin lähimpään kokonaislukuun  

  * **floor(decimal)** Pyöristä desimaali alaspäin lähimpään kokonaislukuun  

  * [**round (decimal)**](<https://support.nepton.com/hc/fi/articles/23677421993501>) Pyöristä desimaali haluttuun tarkkuuteen.  

  * **minutesToHHMM(decimal)** Muuntaa minuuttien määrän muotoon HH:MM. Arvoa ei pyöristetä. Esimerkiksi `minutesToHHMM(270.8)` palauttaa arvon 04:30. Jos pyöristystä tarvitaan, se on tehtävä erikseen, esimerkiksi `minutesToHHMM(round(270.8))`  

  * **minutesToHHMMSS(decimal)** Muuntaa minuuttien määrän muotoon HH:MM:SS. Esimerkiksi `minutesToHHMMSS(270.8)` palauttaa arvon 04:30:48.  

  * **secondsToHHMM(decimal)** Muuntaa sekuntien määrän muotoon HH:MM. Arvoa ei pyöristetä. Esimerkiksi `secondsToHHMM(16248)` palauttaa arvon 04:30. Jos pyöristystä tarvitaan, se on tehtävä erikseen, esimerkiksi `minutesToHHMM(round(16248 / 60.0))`  

  * **secondsToHHMMSS(decimal)** Muuntaa sekuntien määrän muotoon HH:MM:SS format. Esimerkiksi `secondsToHHMMSS(16248)` palauttaa arvon 04:30:48.  

  * **isAnniversary(**  
<currentDate>,  
<date to test e.g. birthday, contract start date, etc>,  
<years as string CSV that you want to match e.g. "5,10" for 5th and 10th anniversary>,  
<number of days to match beforehand e.g. 14 could be used to remind about anniversaries 2 weeks before the anniversary> **)**  
Palauttaa vastaavan vuoden. Esimerkiksi jos nykyinen päivämäärä on työsuhteen alkamispäivämäärän 5. vuosipäivä, se palauttaa arvon 5. Muussa tapauksessa palauttaa null-arvon.  
**Esimerkki:**  
**![](https://support.nepton.com/hc/article_attachments/33078362318237)**
