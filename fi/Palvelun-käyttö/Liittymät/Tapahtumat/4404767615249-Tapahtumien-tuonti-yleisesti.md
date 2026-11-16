---
id: 4404767615249
title: Tapahtumien tuonti yleisesti
url: https://support.nepton.com/hc/fi/articles/4404767615249-Tapahtumien-tuonti-yleisesti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumat
section_id: 360001061298
section_path:
- Liittymät
- Tapahtumat
labels:
- alkusaldo
promoted: false
updated_at: '2026-10-16T11:42:20Z'
edited_at: '2026-10-16T11:42:20Z'
---

# Tapahtumien tuonti yleisesti

Nepton-palveluun voidaan tuoda tapahtumia (esim. poissaoloja, lomia, jne) muista järjestelmistä
**\- API-kutsulla**
**\- aineistolatauksella**
Valitse oikea tapa tuoda tapahtumia alleviivattujen huomioiden perusteella.
## Tapahtumien tuonti ohjelmallisella liittymällä, eli API:lla
Palveluun voidaan tuoda tapahtumia käyttäen API-rajapintaa. API-rajapinta mahdollistaa tiedonsiirron reaaliaikaisesti tai sillä aikataululla kuin tiedon lähettävä pää haluaa tiedon siirtää. Lisätietoja rajapinnan käytöstä voi lukea [täältä](<https://support.nepton.com/hc/fi/articles/360019840217>).
## Tapahtumien tuonti aineistolatauksella
Tapahtuma-aineisto voidaan tuoda Neptoniin
**\- ajastetusti SFTP-palvelimelta**
**\- manuaalisesti käyttöliittymän kautta**
### Tuonti aineistolatauksella: Tapahtumien tuonti ajastetusti
Nepton-palveluun voidaan tuoda tapahtumia käyttäen ajastettua siirtoaineiston tuontia. Siirtoaineiston ajastettua lataamista suositellaan silloin kun tapahtumia tuodaan palveluun säännöllisesti ja lähettävä järjestelmä voi muodostaa aineiston automaattisesti. Lisätietoja ajastetusta aineistolatauksesta voi lukea [täältä](<https://support.nepton.com/hc/fi/articles/4403974690321>).
### Tuonti aineistolatauksella: Tapahtumien tuonti manuaalisesti käyttöliittymän kautta
Palveluun voidaan tuoda tapahtumia käyttäen käyttöliittymästä ladattavaa siirtoaineistoa. Joko niin, että
\- **määritellään tuotavan tiedon rakenne etukäteen**  
  
Tätä tapaa suositellaan silloin kun halutaan testata ajastettua tuontia ilman SFTP-määrityksiä tai kun tuodaan samanlaista tapahtumatietoa usein käyttölliittymän kautta.  
  
Lisätietoja käyttöliittymän aineistolatauksesta ennalta määritetyllä rakenteella voi lukea [täältä](<https://support.nepton.com/hc/fi/articles/4419484517521>).
tai
\- **valitaan tiedon rakenne tuonnin aikana**  
Tätä tapaa suositellaan kun tapahtumien tuonti ei ole säännöllistä ja esimerkiksi käyttöönoton aikana toteuttavat kertymien pohja-arvojen asettamiset tai lomaoikeuksien tuonnit suositellaan tehtävän tällä tavalla. Tämä tapa toimii, jos on määritelty vain yhdet, tätä tuontia varten määritellyt tuontiasetukset Neptonissa (Katso kuva artikkelin lopusta).
Lisätietoja käyttöliittymän aineistolatauksesta tuonnissa valittavalla rakenteella voi lukea [täältä](<https://support.nepton.com/hc/fi/articles/360002868137>).
## Tapahtumien tuonti -asetukset
**Aina kun tapahtumia tuodaan aineistolatauksella** , joko SFTP:ltä tai käyttöliittymästä manuaalisesti,**tulee ensin määritellä Tapahtumien tuonti -asetukset**
Työaika > Hallinta > Työyhteisön asetukset > Liittymät -näkymässä:
![](https://support.nepton.com/hc/article_attachments/18259962339229)
Tapahtumien tuonnin asetuksissa on määriteltävä seuraavat asiat:
  * Aineistolla tuotavien tapahtumien koodit Neptonia vastaaviin tapahtuma- ja poissaolotyyppeihin, esimerkiksi:
    * Aineistolla tuodaan vuosilomaa koodilla "VL". Jotta Nepton osaa lukea tämän sisään oikein, on tapahtuman tuonnin asetuksiin määritettävä Vuosiloma-tapahtumatyypin kohdalle kyseinen koodi 
    * Kaikkien aineistolla tuotavien tapahtuma- ja poissaolotyyppien koodit on löydyttävä Neptonista. Mikäli aineistolla tuodaan tapahtumaa, jolle ei ole vastinparia Neptonissa, **kyseinen tapahtuma jää tuomatta**. 


![](https://support.nepton.com/hc/article_attachments/23619381499549)
  * Tapahtumien tuonnin asetukset SFTP-palvelimen tietojen osalta
    * Täytä vaaditut kentät, jotta Nepton pääsee palvelimelle hakemaan sisäänluettavaa aineistoa
  * Lisähuomioita asetuksista:
    * **Menneiden päivien määrä siirtotiedostossa** -asetus on tärkeä. Aineistosta puuttuvat tapahtumat poistetaan henkilön kalenterista, mikäli kalenterissa oleva tapahtuma on perustettu samalla käyttäjällä kuin siirtoa suoritetaan. Palveluun asetetaan se päivien määrä, jota siirrettävää aineistoa tulkitaan historiaan. Tätä päivien määrää verrataan tapahtuman päättymispäivään. Tapahtumat poistetaan siltä ajalta, milloin ne ovat voimassa henkilön kalenterissa päivitettävällä ajanjaksolla, ja eivät ole siirtoaineistossa. Tapahtuman on täten löydyttävä siirtotiedostosta koko sen voimassaoloajan lisättynä menneisyyteen päivitettävien päivien lukumäärällä. Mikäli aikarajaa ei ole asetettu käytetään arvona 0 päivää.
