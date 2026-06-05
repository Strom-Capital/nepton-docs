---
id: 360002590097
title: SAML SSO-kirjautumisen käyttöönotto
url: https://support.nepton.com/hc/fi/articles/360002590097-SAML-SSO-kirjautumisen-k%C3%A4ytt%C3%B6%C3%B6notto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: SAML-kirjautuminen
section_id: 360004542757
section_path:
- Kirjautuminen
- Kertakirjautuminen (SSO)
- SAML-kirjautuminen
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2025-03-28T08:16:19Z'
edited_at: '2025-03-28T08:16:19Z'
---

# SAML SSO-kirjautumisen käyttöönotto

Ylläpitäjä voi hallinnoida kertakirjautumisen asetuksia osiossa **Työsuhde - Hallinta - Kertakirjautuminen (SSO)**. Uusia SAML SSO-kirjautumisasetuksia lisätessä valitse SSO-kirjautuminen-otsikon alta **Lisää**. Käytössä voi olla yhtäaikaisesti useita eri SAML SSO-kirjautumisia käytössä. Kaikki kirjautumisvaihtoehdot näytetään palvelun kirjautumissivulla.
Identiteettitoimittaja (IdP) tyypillisesti tarjoaa tarvittavat konfiguraatiotiedot. Nämä tiedot tarvitaan **XML -muotoisena metadatana.** Näiden tietojen pohjalta, tarvittavat tiedot voidaan määrittää Neptonissa. 
Jos käytössäsi on Active Directory, katso myös [Asetukset ADFS palvelimella](<https://support.nepton.com/hc/fi/articles/360005242897>)
Jos käytössäsi on OKTA, katso myös [Asetukset OKTA palvelussa](<https://support.nepton.com/hc/fi/articles/5115492518301>)
## Kertakirjautumisasetusten määrittäminen - ennakkotoimenpide
Ennen kertakirjautumisasetusten määrittämistä tee seuraava toimenpide. Tämä toimenpide tulee tehdä, jotta sinulla on myöhemmin asetuksiin määritettävät tiedot. 
  1. Avaa asiakkaan toimittama xml-muotoinen metadata tekstieditorilla (esim. Notepad)
  2. Hae CTRL + F-toiminnolla metadatasta "Certificate", jolloin haun pitäisi löytää seuraavanlainen osuma  
![](https://support.nepton.com/hc/article_attachments/26140819271837)
  3. Kopioi pitkä "MII" alkava merkkijono > merkin jälkeen aina < merkkiin asti
  4. Liitä kopiomasi merkkijono uuteen tekstieditori-tiedostoon
  5. Lisää merkkijonon alkuun -----BEGIN CERTIFICATE----- ja loppuun -----END CERTIFICATE----- (huom. viisi kpl viivoja oleellinen)  
  
![](https://support.nepton.com/hc/article_attachments/26140780198173)  
  
![](https://support.nepton.com/hc/article_attachments/26140819277469)
  6. Tallenna tiedosto haluamasi nimellä ja kirjoita nimen perään .cer.


Tulet hyödyntämään tätä tiedostoa kertakirjautumisasetusten määrittämisessä seuraavissa vaiheissa.   
  

## Kertakirjautumisasetusten määrittäminen Neptonissa
![Capture_1.PNG](https://support.nepton.com/hc/article_attachments/360010905758)
**Ei käytössä** painikkeen avulla on mahdollista hetkellisesti ottaa SSO-kirjautuminen pois käytöstä, jos käyttäjien esim. jostain syystä halutaan kirjautuvan väliaikaisesti pelkillä Nepton kirjautumistunnuksilla. Myös asetuksia ensimmäistä kertaa määriteltäessä on suositeltavaa valita Ei käytössä -valinta voimaan, jotta SSO-painike ei aktivoidu käyttäjille näkyville ennenkuin kertakirjautumisen varmennetiedot on lisätty.
**Nimi** kohtaan määritellään se nimi/teksti, joka kirjautumissivulla halutaan käyttäjille näkyvän SSO-painikkeessa.
Käyttäjä voi myös kirjautua palveluun suorakirjautumislinkillä ilman erillistä kertakirjautumisen painiketta. Linkki muodostuu seuraavalla tavalla: [https://go.nepton.com/Portal/ExternalLogin/Saml2Login.aspx?deploymentID=XXXX&cc=YYYYY](<https://go.nepton.com/Portal/ExternalLogin/Saml2Login.aspx?deploymentID=XXXX&cc=YYYYY.>). Laita ar voihin XXXX ja YYYY työyhteisösi oikeat arvot. Löydät nämä työyhteisökohtaiset arvot menemällä <https://go.nepton.com> sivulle, kirjoittamalla oman työyhteisösi nimen ja löytämällä oman työyhteisösi. Arvot ovat nyt nähtävissä selaimen osoitepalkin osoitteessa.
  
**Aloita käyttö** mahdollistaa sen, että SSO-asetusten käyttöönotto voidaan ajastaa jo etukäteen tapahtumaan tiettynä päivänä.  
  
**Lopeta käyttö** päivämäärä on hyödyllinen erityisesti silloin, kun vaihdetaan palveluntarjoajaa, ja vanhojen asetusten päättäminen ja uusien käyttöönotto halutaan ajastaa tiettyyn päivään.  
  
**Hallinta** kohdassa valitaan, määritelläänkö kertakirjautumisasetukset manuaalisesti, vai poimitaanko ne automaattisesti metadatalähteestä. Automaattisen metadatalähteen tulee olla sellainen, jota Nepton voi lukea. Jos valitaan automaattinen hallinta, täyttyy suurin osa asetuksista automaattisesti metadatasta, ja vain muutamaan kohtaan tulee määritellä asetukset. **HUOM! Automaattista poimintaa metadatalähteestä käytetään ainoastaan Virtu-kertakirjautumisen yhteydessä, muissa tavoissa se ei ole Neptonissa tuettu.**  
  
**Verkkopalvelun tunnus (Entity Id)** tieto löytyy IdP:n (identiteettitoimittaja) toimittamasta metadatasta. Tämä on IdP:n yksilöivä tunniste.   
**Toimenpide** : Hae asiakkaan toimittamasta metadatasta "Entity ID" löytääksesi oikean tiedon.   
**Organisaation nimi** kohtaan määritellään taho, joka vastaa SSO:sta (esim. IdP).  
**Toimenpide** : Täytä kenttään asiakkaan organisaation nimi.   
**Yhteyshenkilö(t)** on SSO:sta vastaavan organisaation yhteyshenkilö, jonka puoleen SSO-asioissa voi kääntyä.  
**Toimenpide** : Täytä kenttään asiakkaan yhteyshenkilön nimi ja yhteystiedot. 
**Kirjautumispalvelun URL** tieto löytyy IdP:n toimittamasta metadatasta. Tämä määrittää IdP:n kirjautumissivuston osoitteen.  
**Toimenpide** : Hae asiakkaan toimittamasta metadatasta "SingleSignOnService" löytääksesi oikean tiedon.   
**Kirjautumispalvelun URL binding** tieto löytyy IdP:n toimittamasta metadatasta.  
**Toimenpide** : Hae asiakkaan metadatasta "SingleSignOnService". Löydät URL Binding tiedon hakutuloksen "SingleSignOnService"-rivin **ensimmäiseltä riviltä** , esim. HTTP-POST.   
**Varmenteen hajautusalgoritmi** tieto löytyy varmenteen (sertifikaatin) tiedoista.  
**Toimenpide** : Avaa aiemmin tallentamasi .cer-muotoinen varmennetiedosto. Mene välilehdelle "Details". Löydät tiedon kohdasta "Signature hash algorithm"
**Henkilöllisyyden tunnisteen muoto (name Id format)** tieto löytyy IdP:n toimittamasta metadatasta. Arvo on useimmiten Transient tai Unspecified.  
**Toimenpide** : Hae asiakkaan metadatasta "nameid-format" löytääksesi oikean tiedon.   
**Käytä Nameid tunnistetta henkilön tunnistamiseen** Mikäli tähän vastataan Kyllä, henkilöt tunnistetaan identiteettituottajan Nameid arvon perusteella, eikä sinun tarvitse määrittää alla olevaa henkilöntunnistusatribuutit määritystä.  
**Toimenpide** : Tähän asetukseen määritetään yleensä "Ei" sillä tunnistus tapahtuu henkilöntunnistinatribuutin perusteella (seuraava asetus). 
**Henkilöntunnistusatribuutit** tieto löytyy IdP:n toimittamasta metadatasta.  
**Toimenpide** : Hae asiakkaan metadatasta "urn:oid" löytääksesi oikean tiedon.   
  
Atribuutti voi olla esim. nimi tai sähköpostiosoite. Tätä tietoa käytetään henkilön tunnistamiseen.
Jokaista tunnistusatribuuttia vastaava koodi löytyy IdP:n metadatasta. Esim. sähköpostiosoitetta voi metadatassa vastata yksi koodi, joka yksinään riittää atribuutiksi mikäli sähköpostiosoitetta halutaan käyttää käyttäjän tunnisteena.  
  
Joskus haluttu tunnistetieto ei sellaisenaan löydy metadatasta, jolloin se rakennetaan yhdistämällä atribuutteihin erilaisia osia. Esimerkiksi jos halutaan käyttää SSO-tunnisteena sähköpostia, mutta IdP:n tiedoista löytyy vain kokonimi, voidaan haluttu tunnisteatribuutti rakentaa lisäämällä kokonimi-atribuuttiin tarvittavia lisätekstejä. Kokonimi-tietoa voi metadatassa vastata esim. koodi “urn:oid:0.1.1234.56789100.100.1.1”, josta voidaan rakentaa haluttu tunnisteatribuutti lisäämällä sähköpostia vastaavat tiedot atribuutin perään. Tässä esimerkkitapauksessa tunnistusatribuutti "urn:oid:0.1.1234.56789100.100.1.1\@yritys.fi" vastaisi sähköpostiosoitetta "kokonimi@yritys.fi". Tätä sähköpostiosoitetta peilattaisiin sitten Neptonissa oleviin tietoihin.
Kun kaikki vaadittavat tiedot on määritelty, tallenna tiedot Tallenna -painikkeesta.
**Henkilön tunnistetieto** on Neptoniin tallennettu HR tietue, jota puolestaan käytetään henkilön tunnistamiseen kertakirjautumisessa. Vaihtoehtoja ovat sähköposti, käyttäjätunnus, henkilönumero ja henkilötunnus.  
**Toimenpide :** Varmista tämä tieto asiakkaalta ja tallenna oikea arvo kenttään. 
## Varmenteen lisääminen Neptoniin
Asetuksiin määritettävät tiedot saadaan tunnistetietojen tarjoajalta (identity provider, IdP, tai muulta taholta, jolta varmenne on hankittu.). IdP toimittaa tiedot XML-muotoisena metadatana, jonka perusteella allaolevat tiedot voidaan lisätä.
Lisää varmenne -kenttään lisätään Base64 enkoodattu varmenneteksti. Löydät tämän varmennetekstin:
a) Katsomalla ja etsimällä asiakkaan toimittamasta XML-muotoisesta metadatasta tekstieditorilla (esim. Notepad) alla näkyvän kohdan
b) Varmenneteksti alkaa tyypillisesti **MII** kirjaimilla ja loppuu **=** kirjaimeen.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21078310146589)
Kopioituasi varmennetekstin siirry aiemmin tallentamiisi kertakirjautumisasetuksiin ja valitse "Lisää varmenne", jolloin päädyt seuraavanlaiseen näkymään:  
![](https://support.nepton.com/hc/article_attachments/26140819280029)  
  
  
Liitä kopioimasti varmenne kenttään ja tallenna. Tallentamisen jälkeen Nepton tarkistaa varmenteen, joka voi kestää muutaman minuutin. Varmenteen tarkistuksen jälkeen se esitetään varmenteet osiossa. Mikäli tarkistettu varmenne on voimassa, eikä muita varmenteita ole käytössä, otetaan uusi varmenne automaattisesti heti käyttöön.
Huomaa että asiakkaalla voi olla käytössä erilliset varmenteet tiedon kryptaukseen ja allekirjoituksiin. Tällöin metadatassa on kaksi eri varmennetta ja kummatkin tulee lisätä erikseen Neptoniin.
## Uuden varmenteen lisääminen ja ajastaminen
Yhteen kertakirjautumiseen on mahdollista lisätä useampi varmenne, joista vain yksi kerrallaan voi olla käytössä. Useamman varmenteen lisäys mahdollistaa sen, että varmenteen vaihtuminen voidaan ajastaa ja automatisoida tulevaisuuteen tapahtumaan haluttuna ajankohtana Aloita käyttö-toiminnon kautta. Mikäli palveluun lisättävä uusi varmenne on päällekkäinen käytössä olevan varmenteen kanssa, palvelu tarjoaa automaattisesti vaihtopäivää, jonka ylläpitäjä voi hyväksyä. Varmenteen vaihtopäivää on mahdollista myös muokata Aloita käyttö-toiminnon kautta. 
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360011702117)
## Liitännäisvarmenteet 
Osa varmenteista voi vaatia useamman varmenteen varmenneketjun (**liitännäisvarmenteet**) ollakseen luotettavia. Palveluun on mahdollista tarvittaessa määritellä yksittäisten varmenteiden lisäksi myös liitännäisvarmenteita.
Huomaa, että mahdolliset salausvarmenteet (encryption certificate) tulee aina lisätä **Liitännäisvarmenteet** -toiminnon kautta.
![](https://support.nepton.com/hc/article_attachments/21601599936029)
Varmenteet -osiossa varmenteen tiedoissa esitetään erilaisia herätteitä, jos esimerkiksi varmenne on vanhenemassa, kahden eri varmenteen aloitus- ja lopetusajan välissä on katkos, tai liitännäisvarmenteet ovat puutteellisia.
## Kirjautuminen 
Jos nyt aktivoit SSO kirjautumisen, pitäisi tämän tulla näkyviin kirjautumissivulle. Napsauta SSO Login-painiketta. Jos kaikki on määritetty oikein, siirrytään ensin oman työyhteisön IdP tunnistuspalvelimelle jossa mahdollisesti kysytään henkilön tunnistetietoja. Tämän jälkeen siirrytään takaisin Neptoniin ja kirjaudutaan automaattisesti palveluun sisälle.
