---
id: 360002492458
title: Scheduled task - Ruleset export
url: https://support.nepton.com/hc/en-gb/articles/360002492458-Scheduled-task-Ruleset-export
locale: en-gb
category: Support
category_id: 360000446658
section: Rulesets
section_id: 360000827378
section_path:
- Integration
- Rulesets
labels:
- NEPTONNEEDSREVIEW
- Viennin aikavälin sääntö
- Viennin asetukset
- viennin ajastus
promoted: false
updated_at: '2025-05-23T10:29:31Z'
edited_at: '2025-05-23T10:29:31Z'
---

# Scheduled task - Ruleset export

**Sorry!**
This article has not been translated yet.
Sääntöjoukolle voidaan määritellä asetukset, joiden perusteella niistä muodostetaan automaattisesti siirtotiedosto vietäväksi määritettyyn palveluun. Sääntöjoukon tulokset on mahdollista viedä tiedostosiirtona SFTP-palvelimelle tai joidenkin liittymien kohdalla myös Web Service rajapintakutsulla. Jos erillinen palveluntarjoaja tukee jotain näistä siirtotavoista voidaan liittymän tiedot välittää suoraan palveluntarjoajalle sen sijaan, että käyttäjä lataa erikseen siirtotiedoston ja vie sen kohdejärjestelmään. 
Viennin asetukset tulee määritellä työyhteisötasolle.
## Asetukset
![mceclip2.png](https://support.nepton.com/hc/article_attachments/9452455162525)
### Tietojen lähettäminen Web service rajapintakutsulla
![mceclip3.png](https://support.nepton.com/hc/article_attachments/9452570650013)
Tämä vaihtoehto on käytettävissä vain osalla liittymistä. Tarkista liittymäkohtaisesta ohjeesta tarkemmat tiedot tämän käyttöön.
### Tietojen lähettäminen SFTP-tiedostosiirrolla
![mceclip0.png](https://support.nepton.com/hc/article_attachments/9452156548381)
Palvelu siirtää sääntöjoukon poimintasääntöjen mukaisen tuloksen määritettyyn SFTP kansioon.
Katso [SFTP tiedonsiirron määrityksistä](<https://support.nepton.com/hc/fi/articles/360003722778>) yleiset ohjeet liittyen palvelimen osoitteeseen, käyttäjätunnukseen, autentikointiin (public key tai salasana) sekä minkälainen polkurakenne palvelimella tulisi olla.
**Vientitiedoston nimi** : Vaihtoehtoinen. Mikäli tätä ei ole määritetty käytetään valitun tiedostomuodon/palvelun oletuskäytäntöä tiedostonimen muodostukseen. Mikäli tiedostonimi määritetään kannattaa seuraavat asiat huomioida:
  * Nimen tulee sisältää myös tiedostopääte. On suositeltavaa että käytät samaa kuin mitä viennin tiedostomuoto oikeastikin käyttäisi (esim. '.csv' tai '.xml')
  * On vahvasti suositeltavaa että tiedoston nimi sisältää aikaleiman. Asetuskenttään voidaan lisätä seuraavat paikkamerkinnät, jotka järjestelmä korvaa ajohetken aikaleimalla 
    * [vvvvkkpphhmmss] korvautuu esim. 20230101043059
    * [vvvvkkpphhmm] korvautuu esim. 2023010430 
    * [vvvvkkpp] korvautuu esim. 20230101
  * Nimeen on hyvä lisätä jotain lähdetietoja esim. sääntöjoukon nimi jolloin tiedostopalvelimella näkee nimen perusteella mitä kautta siirtotiedosto on muodostunut.


### Vientitiedoston jakaminen osiin
![mceclip4.png](https://support.nepton.com/hc/article_attachments/9452659503901)
Tämän osion avulla voit määrittää, että suoritus luo enemmän kuin yhden tiedoston ja säännöt, joiden mukaan tiedot jaetaan eri tiedostoihin. Tietojen jakamisen voi toteuttaa esim. henkilön kustannuspaikan tai henkilön maksuryhmän perusteella. Lue lisää [täältä](<https://support.nepton.com/hc/fi/articles/360006255458>).
### Viennin aikavälin säännöt
Kaikki työaika-osion liittymien ajastukset, mukaanlukien sääntöjoukkojen vienti löytyvät kohdasta  
**Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Ajastus**
Liittymien ajastuksesta voit lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/10510800700573>)
## Ajastettujen vientien tarkastelu
Sääntöjoukon muodostamisen tulos löytyy työajan ajastusosiosta (Lue lisää [täältä](<https://support.nepton.com/hc/fi/articles/10510800700573>)). Ajastusosiossa tulokset nähdään koskien jokaista yksittäistä ajastusta.
Tulokset näytetään myös palvelulokissa. Palveluloki näyttää kaikki onnistuneet sekä epäonnistuneet sääntöjoukon tulosten muodostamiset ja sisältää tulokset kaikkien ajastusten osalta. Onnistuneessa sääntöjoukon tulosten muodostamisessa näytetään muodostunut sisältö ja epäonnistuneesta muodostamisesta näytetään syy ajon epäonnistumiseen. Esimerkiksi virheellinen määrittely viennin aikavälin säännössä näkyy palvelulokissa epäonnistumisen syynä.
