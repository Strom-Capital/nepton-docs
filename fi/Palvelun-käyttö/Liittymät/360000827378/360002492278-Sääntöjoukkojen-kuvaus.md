---
id: 360002492278
title: Sääntöjoukkojen kuvaus
url: https://support.nepton.com/hc/fi/articles/360002492278-S%C3%A4%C3%A4nt%C3%B6joukkojen-kuvaus
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels:
- NEPTONNEEDSREVIEW
- integrationruleset
- palkkalajimääritys
- liittymäkuvaus
- Integraatiosäännöt
- sääntöjoukkomallit
- sääntöeditori
- siirtojoukko
promoted: false
updated_at: '2026-04-29T04:36:36Z'
edited_at: '2026-04-29T04:35:16Z'
---

# Sääntöjoukkojen kuvaus

Palvelusta voidaan ladata tietoa eri muodoissa. Palvelu muodostaa joko ajastettuna tai käyttöliittymästä haettaessa tiedoston, jolle poimitaan sääntöjoukon poimintasäännöillä määritelty sisältö. Tiedon latauksia käytetään tyypillisesti siirtämään tietoa ulkoisiin järjestelmiin, kuten palkkajärjestelmiin (esim. Mepco, Sonet, CGI), raportointijärjestelmiin (esim. Qlikview / Qliksense, Cognos, Power BI) sekä laskutusjärjestelmiin. Tietoa voidaan siirtää mihin tahansa ulkoiseen palveluun, joka pystyy vastaanottamaan jotakin käytettävissä olevaa siirtomuotoa. Tiedostopohjaiset siirtomuodot on kuvattu [täällä](<https://support.nepton.com/hc/fi/articles/360002494538>). Siirtomuoto voi olla ajastettu siirto, tiedostolataus tai sisällön haku palvelun [API:sta](<https://support.nepton.com/hc/fi/articles/360004861558>) toiminnolla RunIntegrationRuleset.
Raportointijärjestelmiin tieto siirretään tyypillisesti siten, että aineisto muodostuu kerran yössä SFTP-kansioon, josta raportointijärjestelmä käy sen hakemassa.
### Uuden sääntöjoukon luominen
Siirrettävä sisältö määritetään käyttäen sääntöjoukkoja. Sääntöjoukot lisätään osiossa **Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Lisää integraation sääntöjoukko. **Sääntöjoukko kuvaa poimintasäännöt, joilla siirrettävään aineistoon valitaan tietoa. Poimintasäännöillä voidaan poimia tietoa henkilöistä, projekteista, tapahtumista tai työajan tulkinnasta. Minkä tahansa sääntöjoukon voi ladata erilaisissa tiedostomuodoissa. Poimintasääntöjen muodostamisen ohjeen löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>). Sääntöjoukolle asetetaan poimintasääntö jokaiselle sisällölle, joka palvelusta poimitaan. Säännöllä voidaan poimia esimerkiksi palkkalaji ja palkkalajin määrä, joka siirretään palkkajärjestelmään.
**Kuvaus** -sarakkeeseen annetaan poimintasäännön nimi, mielellään mahdollisimman informatiivinen, joka kertoo, mitä poimintasääntö poimii.
**Palkkalajikoodi** -sarakkeeseen voi laittaa palkkalajikoodin poimintasäännön tulokselle, joka viedään raportille tai Neptonista ulkoiseen järjestelmään. Palkkalajikoodi voidaan useissa liittymissä yliajaa määrittämällä arvolle OverrideSalaryCode, jolloin poiminnalle muodostuu palkkalajikoodi suoraan poimintasäännöstä. Tällöin palkkalajikoodia ei tarvitse määritellä tässä erillisessä sarakkeessa.
**Poimintasääntö** sisältää varsinaisen poimintasäännön jolla tietoja poimitaan.
**Palkkalajikoodi viedään** \- sarakkeella määritetään että missä yksikössä (esim. sekuntia, tuntia, päiviä) sääntöjoukon poimintasääntörivin tulos palautetaan. Kun yksikkö on määritetty, kyselyn antama määrä palautetaan siinä yksikössä, eikä määrälle tarvitse yksikön takia tehdä erillistä laskentaa kyselyssä.  
  
Useissa liittymissä määrän yksikkö voidaan myös ylikirjoittaa kyselyssä arvolle OverrideUnitType  
  
Mahdolliset arvot yksikölle on 
  * "U" - kokonaisluku
  * "D" - desimaaliluku
  * "S" - sekunteja
  * "H" - tunteja
  * "J" - päiviä
  * "C" - valuutta

![](https://support.nepton.com/hc/article_attachments/34332524073885)
Palvelu näyttää virheilmoituksen, mikäli poimintasäännön rakenne on virheellinen. Jokaisen säännön alapuolella on toiminto, jolla voidaan tarkistaa säännön oikeellisuus. Mikäli rakenne on oikein, muuttuu kentän taustaväri vihreäksi.
### Poimintasäännön tarkastus
Poimintasäännön sisältö voidaan tarkistaa 'katso säännön tulokset' -toiminnolla, joka näyttää poimintasäännön muodostamat tulokset. Valintoina voidaan määritellä aikaväli, henkilöt sekä tulosten muoto. Tulosten muoto 'Taulukko' esittää tulokset tietokantamuotoisena. Muissa muodoissa tulos esitetään sellaisena kuin se siirtyy kyseisen tiedostomuodon tiedostolatauksena. Näkymässä voidaan tarkistaa, että tiedostomuotoon siirtyy oikea aineisto oikeissa sarakkeissa.
![](https://support.nepton.com/hc/article_attachments/34332524076701)
Sääntöjoukon tulosten siirto voidaan automatisoida. Tällöin aineisto muodostuu aikataulun mukaisesti esimerkiksi SFTP-palvelimelle. Lisätietoja sääntöjoukon siirron automatisoinnista [täällä](<https://support.nepton.com/hc/fi/articles/360002492458>).
Kun sääntöjoukko on valmis, voi sääntöjoukon aineiston ladata missä tahansa tiedostomuodossa valikosta **Työaika > Hallinta > Liittymät.**
### Sääntöjoukon kopioiminen
Ympäristössä jo olevaa sääntöjoukkoa voidaan käyttää pohjana uutta sääntöjoukkoa luodessa. Tämä voidaan tehdä joko työyhteisö- tai asetusryhmätasolla valikossa **Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Liittymät > Lisää liittymien sääntöjoukko**.
Kohtaan "Luo pohjasta" valitaan se sääntöjoukko, jota halutaan käyttää uuden sääntöjoukon pohjana. Kun tämä on valittu, palvelu kopioi valitusta sääntöjoukosta kaikki muut asetukset, paitsi Vientitiedoston nimi sekä Liittymän kohdepalvelin.
![](https://support.nepton.com/hc/article_attachments/35715788070685)
