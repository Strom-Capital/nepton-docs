---
id: 360003737078
title: 'Projektien tuonti  '
url: https://support.nepton.com/hc/fi/articles/360003737078-Projektien-tuonti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Projektit
section_id: 360001075297
section_path:
- Liittymät
- Projektit
labels: []
promoted: false
updated_at: '2024-08-23T10:04:37Z'
edited_at: '2024-02-01T10:13:52Z'
---

# Projektien tuonti  

Palveluun on helppo tuoda projektitiedot muista palveluista ajastetusti tai manuaalisella tiedostolatauksella. Tarpeena voi olla esimerkiksi uusien projektien tuonti, projektien tietojen muokkaaminen tai projektien päättäminen. 
Artikkelin lopussa on esimerkkitiedosto projektituontia varten. 
## Ajastettu tiedostolataus
Projektien tiedot sisältävä aineisto voidaan ajastaa noudettavaksi Neptoniin SFTP-palvelimelta tai API-rajapinnalla. Lisätietoja löydät [tästä artikkelista.](<https://support.nepton.com/hc/fi/articles/360002492518>)
## Manuaalinen tiedostolataus
Projektien tuontia varten käyttäjällä tulee olla Ylläpitäjä-rooli ja Työajan Kaikki oikeudet -rooli.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360006502438)
Ohjeet henkilön lisäämiseen löydät täältä: [Henkilön lisääminen](<https://support.nepton.com/hc/fi/articles/360002427618>)
Ohjeet roolin liittämisestä löydät täältä: [Henkilön liittäminen Työajan rooliin](<https://support.nepton.com/hc/fi/articles/360002553397>)
## Tietojen valmisteleminen
  * Ota pohjaksi tämän artikkelin esimerkkitiedosto.
  * Pakolliset tiedot ovat projektin nimi, projektikoodi ja näkyvyys kirjauspäätteellä (A ja B, H sarakkeet)
  * Tyhjiä sarakkeita ei saa poistaa. Jätä sarakkeet tyhjiksi, jos niihin ei ole tietoja. 
  * Kun olet täyttänyt tiedot, poista tiedostosta kolme ensimmäistä riviä (rivit 1-3, sisältää A-sarakkeessa oranssilla kirjoitetun tekstin, ’Yksillöllinen arvo’ ja ’Project Code’).
  * Tallenna tiedosto CSV-muotoisena - CSV UTF-8 (Comma delimited) (*.csv).


## Tietojen tuonnin vaiheet
1\. Valitse **Työaika** -> **Hallinta** -> **Liittymät** -> **Projektien tuonti**
2\. Lataa tiedosto (Choose file). Hae tietokoneelta tallentamasi CSV-tiedosto. Valitse **Käynnistä.**
![](https://support.nepton.com/hc/article_attachments/15493290563613)
Mikäli siirto onnistui, näytetään se sinisellä pohjalla tuontihistoriassa. Suurennuslasi-kuvakkeesta aukeaa tuonnin lokitiedot.
![](https://support.nepton.com/hc/article_attachments/15493290564509)
Mikäli tuontitiedostossa on projekteja, joiden tiedot eivät ole muuttuneet, niiden tallennus ohitetaan ja ne merkitään tuontilokiin ohitetuiksi projekteiksi.
Mikäli tuonti epäonnistui, näytetään se punaisella pohjalla tuontihistoriassa. Huutomerkki-kuvakkeesta aukeaa tuonnin lokitiedot, joista ilmenee tuonnin aikaiset virheet. Kun virheet on korjattu, voidaan tiedosto tuoda uudelleen.
![](https://support.nepton.com/hc/article_attachments/15493290568093)
3\. Projektien tuonti on nyt tehty ja määrittelemäsi tiedot on päivitetty tai lisätty.
4\. Löydät tiedot siirrosta myös Työsuhde-osion palvelulokista. Valitse **Työsuhde** > **Hallinta >** **Palveluloki**. Tarkat tiedot siirrosta näet klikkaamalla rivin vasemman reunan kuvaketta. Kuvake on vihreä, jos siirto on onnistunut ja punainen, jos siirto on epäonnistunut.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360006509618)
Siirretyt projektit muodostuvat palveluun automaattisesti. Mikäli projekti on jo palvelussa, päivitetään sen tietoja.
Projektin sijaintia hierarkiassa ei voi muuttaa projektihierarkian ylätasolle.
## Tuonnissa käytettävät kentät 
Tuotava tieto | Kuvaus  
---|---  
Project Code |  Projektin koodi. Jos koodilla ei vielä ole projektia, se luodaan. Jos koodilla on jo projekti, se päivitetään.  
Project Name |  Projektin nimi. Pakollinen kenttä.  
Project Description |  Projektin kuvaus. Voi olla tyhjä.  
Project Start date |  Projektin alkupäivä, voi olla tyhjä. Muoto VVVV-KK-PP. **HUOM. 1.1.1970 ja aiemmat päivämäärät eivät näy käyttöliittymässä**  
Project End date |  Projektin loppupäivä, voi olla tyhjä. Muoto VVVV-KK-PP.  
Parent project code |  Yliprojektin koodi, voi olla tyhjä. Tuotu projekti on asetetun yliprojektin aliprojekti.  
ProjectTypeName |  Projektin tyyppi. Jos tyhjä, käytetään oletusta *Projektit'.  
Show on terminals |  Näytetään kirjauspäätteissä. '1' näytetään, '0' ei näytetä.  
External Identifier |  Ulkoinen tunniste. Mikäli ulkoisella tunnisteella on projekti, projekti päivitetään. Ulkoista tunnistetta käytetään projektin tunnistamiseen ennen projektin koodia. Voi olla tyhjä.  
Project Managers |  Projektipäälliköiden henkilönumerot. Mikäli projektille halutaan liittää useampi projektipäällikkö, erotellaan henkilönumerot "|" merkillä. Esim. "001 | 002 | 003". Voi olla tyhjä.  
User groups |  Projektin näkyvyys henkilöryhmille. Arvona käytetään henkilöryhmien koodeja. Mikäli projektille halutaan liittää useampi henkilöryhmä, erotellaan koodit "|" merkillä. Esim. "001 | 002 | 003". Voi olla tyhjä. **HUOM!** Näkyvyyden rajaus vaatii erillisen määrityksen, ks. tarkemmin [täältä](<https://support.nepton.com/hc/fi/articles/360006776758>).  
Users |  Projektin näkyvyys henkilöille. Arvona käytetään henkilönumeroita. Mikäli projektille halutaan liittää useampi henkilö, erotellaan henkilönumerot "|" merkillä. Esim. "001 | 002 | 003". Voi olla tyhjä. **HUOM!** Näkyvyyden rajaus vaatii erillisen määrityksen, ks. tarkemmin [täältä](<https://support.nepton.com/hc/fi/articles/360006776758>).  
## Projektin koodi ja ulkoinen tunniste tuonnissa
Projektin koodi on materiaalissa pakollinen, mutta ulkoinen tunniste ei. Projekti voidaan tunnistaa koodilla tai ulkoisella tunnisteella. Jos ulkoinen tunniste löytyy palvelusta ja tuontimateriaalista, päivitetään sitä vastaava projekti. Tuontiloki kertoo, kumpaa tunnistetta on päivityksen yhteydessä käytetty. Muussa tapauksessa projektin koodia käytetään olemassaolevien projektien tunnistamiseen. Huomioitavaa tunnisteiden käytössä:
  * Jos palvelussa on useampi kuin yksi projekti samalla koodilla ilman ulkoista tunnistetta, tuontimateriaalissa ohitetaan sitä vastaava projekti, koska ei ole mahdollista tietää, mikä projekti on tarkoitettu päivitettäväksi. Tämän takia on suositeltavaa käyttää yksilöllisiä projektikoodeja.
  * Jos palvelussa on useampi kuin yksi projekti samalla koodilla ja tätä projektia yritetään tuontimateriaalissa asettaa projektin yläprojektiksi, tuotava projekti ohitetaan, koska ei ole mahdollista tietää, mikä projekti on tarkoitettu yläprojektiksi. Tämän takia on suositeltavaa käyttää yksilöllisiä projektikoodeja.
  * Projektin koodia on mahdollista muuttaa tuonnissa, jos projekti tunnistetaan ulkoisen tunnisteen avulla. On suositeltavaa varmistaa, ettei palveluun jää tämän seurauksena useampaa projektia samalla projektikoodilla.


## Projektipäälliköiden, käyttäjäryhmien ja käyttäjien käsittely tuonnissa
Projektipäälliköt, käyttäjäryhmät ja käyttäjät ovat vapaaehtoinen tieto tuontimateriaalissa.
  * Jos vapaavalintaiset tiedot projektipäälliköistä, käyttäjäryhmistä tai käyttäjistä jätetään tyhjäksi, oletusarvoisesti ne jätetään huomiotta tuonnin yhteydessä. 
  * Jos kentissä on arvot, lisätään uudet arvot projektille. Kaikki arvot, jotka eivät ole tuontimateriaalissa, poistetaan projektilta. Esim. projektilla on tällä hetkellä päällikkö henkilönumerolla 123. Tuodaan projektille päälliköt henkilönumeroilla 321 ja 322. Tällöin päällikkö 123 poistetaan projektilta, koska se ei ole tuontimateriaalissa.
  * Jos halutaan, että tyhjä kenttä poistaa vastaavat tiedot palvelusta, tulee se erikseen määritellä asetuksissa **Hallinta > Työyhteisön asetukset > Liittymät > Projektien tuonti > Tyhjä solu poistaa...** Esim. projektilla on 10 projektipäälliköä. On valittu "Kyllä" asetuksen "Tyhjä solu poistaa projektipäälliköt projektilta" arvoksi ja tuontimateriaalissa vastaava solu on tyhjä. Kaikki projektipäälliköt poistetaan projektilta.


![](https://support.nepton.com/hc/article_attachments/15736620142237)
