---
id: 21229494759069
title: Miksi kirjautuminen Neptoniin ei onnistu?
url: https://support.nepton.com/hc/fi/articles/21229494759069-Miksi-kirjautuminen-Neptoniin-ei-onnistu
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: FAQ
section_id: 360000934177
section_path:
- FAQ
labels:
- login problem
- kirjautumisongelma
- ongelma kirjautumisessa
- problem with login
promoted: false
updated_at: '2026-03-13T06:34:54Z'
edited_at: '2026-03-13T06:34:13Z'
---

# Miksi kirjautuminen Neptoniin ei onnistu?

Tässä artikkelissa käydään läpi yleisimmät kirjautumisen ongelmatilanteet ja ratkaisut.
Ohjeet kirjautumiseen löydät [**täältä**](<https://support.nepton.com/hc/fi/articles/360002602998>).
#### 1\. Varmista ensin seuraavat asiat:
  * Olet kirjautumassa palveluun osoitteessa **go.nepton.com**(sama osoite mobiililaitteella ja tietokoneella)
  * Olet kirjautumassa oikeaan **Työyhteisöön**(oman organisaatiosi ympäristöön). Varmista organisaatiosi Nepton-ympäristön nimi tarvittaessa henkilöstöhallinnoltasi.
  * Onko palvelussa käyttökatko: Päivitämme [Palvelun tila -artikkeliin](<https://support.nepton.com/hc/fi/articles/360006554777>) tiedon, mikäli palvelussa on havaittu kirjautumiseen vaikuttava toimintahäiriö. Huoltoikkuna on normaalisti aktiivinen tiistaisin klo 19:15 - 19:45. Tällöin palvelussa saattaa olla lyhyt käyttökatko. 
  * Mikäli kirjautumisessa käytetään SSO-kirjautumisen sijaan käyttäjätunnusta/sähköpostia ja salasanaa, varmista tietojen oikeellisuus ja tilaa tarvittaessa uusi salasana.


**Salasanan vaihtolinkki ei tule käyttäjän omaan sähköpostiosoitteeseen?**  
Ensimmäisenä tulee tarkistaa, että käyttäjä on varmasti yrittänyt kirjautua käyttämällä samaa sähköpostiosoitetta, joka on määritetty henkilön Työsuhde-tietoihin palvelussa. Myös ylimääräinen välilyönti sähköpostin lopussa estää kirjautumisen. Tämän jälkeen kannattaa tarkastaa sähköpostin roskapostikansio. Mikäli nämä toimet eivät auta, voi organisaation Nepton-pääkäyttäjä asettaa käyttäjälle väliaikaisen salasanan ja pyytää käyttäjää vaihtamaan salasana uudeksi kirjauduttuaan palveluun (ohje salasanan vaihtoon [täällä](<https://support.nepton.com/hc/fi/articles/360002596657>)).
#### 2\. Tarkista, onko ongelma selain- tai laitekohtainen:
  * Toimiiko kirjautuminen jollain toisella selaimella (Safari/Chrome/Firefox/Edge)
  * Toimiiko kirjautuminen jollain toisella laitteella (mobiililaite, tabletti, tietokone)


Jotta voidaan varmistaa, johtuuko kirjautumisongelma selaimesta, on käytetyn selaimen välimuisti ja evästeet hyvä tyhjentää.
Ohjeet selaimen välimuistin ja evästeiden tyhjentämiseen löytyvät palveluntarjoajien omilta sivuilta (linkki ohjaa erilliselle sivustolle):
[Google Chromen välimuistin tyhjennys](<https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop>)  
[Firefoxin välimuistin tyhjennys](<https://support.mozilla.org/en-US/kb/how-clear-firefox-cache>)  
[Microsoft Edgen välimuistin tyhjennys](<https://support.microsoft.com/en-us/microsoft-edge/view-and-delete-browser-history-in-microsoft-edge-00cf7943-a9e1-975a-a33d-ac10ce454ca4>)
Päivitä myös tarvittaessa käyttämäsi selain uusimpaan ohjelmistoversioonsa.
#### 3\. Mikäli edellä mainitut toimenpiteet eivät auta, ota yhteys esihenkilöösi, organisaatiosi henkilöstöhallintoon tai Nepton-pääkäyttäjään, joka pääsee tarkistamaan seuraavat asiat:
  * Ensimmäiseksi on hyvä varmistaa, että henkilön käyttämät kirjautumistiedot vastaavat palveluun tallennettuja tietoja (sähköpostiosoite ja käyttäjätunnus). Kirjautumisen tunnisteena käytetään henkilön sähköpostiosoitetta tai käyttäjätunnusta. Myös ylimääräinen välilyönti sähköpostin lopussa estää kirjautumisen.  

  * Tämän jälkeen Nepton-pääkäyttäjä voi selvittää [palvelulokista](<https://support.nepton.com/hc/fi/articles/360002575478>), mistä muusta syystä ongelma kirjautumisessa voi johtua. Palvelulokiin pääsee käsiksi ainoastaan organisaatioiden ylläpitäjät reittiä **Työsuhde > Hallinta > Palveluloki**.  
  
Jos kohtaat ongelmia kertakirjautumisessa (Microsoft Login, Google Login, SAML) valitse palvelulokin rajauksissa Osio-kenttään SSO. Palvelulokissa kuvataan, mistä kirjautumisongelma johtuu. Yleisimmät ongelmat johtuvat siitä, että kirjautuvan henkilön kirjautumistiedoissa on tapahtunut muutoksia, joita ei ole päivitetty Neptoniin (esimerkiksi sähköpostiosoite on muuttunut), tai kolmannen osapuolen tarjoama salainen arvo kirjautumista varten on vanhentunut (esimerkiksi Entra ID). Tukipalvelussamme on erillinen artikkeli Microsoft Loginin ongelmanratkaisua varten [täällä](<https://support.nepton.com/hc/fi/articles/360016233138>).  

  * Pääkäyttäjä voi tarvittaessa ottaa yhteyttä [asiakaspalveluumme](<https://support.nepton.com/hc/fi/articles/7077076926237>). Pyydämme kertomaan tukipyynnössä:  
1\. Henkilön, jota ongelma koskee, tai koskeeko ongelma useampaa henkilöä  
2\. Millä laitteilla ja selaimilla kirjautumista on yritetty  
3\. Onko välimuisti ja evästeet tyhjennetty  
4\. Video kirjautumisyrityksestä tai selkeä kuvaus siitä, missä kohtaa ongelma tulee vastaan: Aukeaako esimerkiksi kirjautumissivu lainkaan tai onnistuuko Työyhteisön valitseminen?   
  
Näillä tiedoilla pääsemme heti selvittämään syytä ongelmaan.
