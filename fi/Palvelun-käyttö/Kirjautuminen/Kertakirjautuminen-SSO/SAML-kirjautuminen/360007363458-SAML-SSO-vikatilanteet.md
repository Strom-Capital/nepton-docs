---
id: 360007363458
title: SAML SSO vikatilanteet
url: https://support.nepton.com/hc/fi/articles/360007363458-SAML-SSO-vikatilanteet
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
- Troubleshoot
- FAQ
promoted: false
updated_at: '2024-11-17T20:22:58Z'
edited_at: '2021-12-07T06:48:56Z'
---

# SAML SSO vikatilanteet

SSO-ongelmat voivat johtua pääasiassa kahdesta eri syystä. Joko SSO-asetuksissa on ongelma, ja SSO ei toimi kenellekään, tai palveluun kirjautuvan henkilön tunnistamiseen liittyy ongelma. Näiden syiden mahdollisia ratkaisuja kuvataan alla.
# SSO ei toimi joillakin käyttäjillä
SSO on asetettu vastaamaan käyttäjää jonkun tunnistamismääritteen perusteella. Tämä tarkoittaa, että kirjautumistunnuksen tekevä käyttäjä vastaa tiettyä kenttää käyttäjätiedoissa. Käytetyin tapa tunnistaa käyttäjä on sähköpostiosoite. Jos SSO ei toimi joillekin käyttäjille, todennäköisin syy on, että palvelussa käytetty tunniste ei vastaa SSO:lla määritettyä. Tämä voidaan ratkaista asettamalla vastaava tunnisteattribuutti käyttäjien tiedoissa ja SSO:ssa.
Jotkut SSO-kirjautumisongelmista näytetään palvelulokissa (Työsuhde > Hallinta > Palveluloki). Alla on joitain yleisimpiä ongelmia selitettynä.
  * **Käyttäjien tunnistamisominaisuuksia ei löydy:** Tämä viesti viittaa siihen, että käyttäjien tunnistamiseen käytettyä ominaisuutta ei ole identiteettitoimittajalta (IDP) palvelun vastaanottamassa pyynnössä. Korjataksesi tämän, siirry kohtaan Työsuhde>Hallinta> Kertakirjautuminen (SSO) ja tarkista, että oikean määritteen arvoksi on määritetty Henkilön tunnistustieto-kenttä.
  * **Arvolle löytyy useampia kuin yksi käyttäjä:** Tämä viesti tarkoittaa, että palvelusta löytyi useampi kuin yksi käyttäjä, jolla on määritetty sama tunniste (tässä tapauksessa yleensä sähköposti). Korjaa se käymällä Työsuhde>Henkilöt>Henkilöt, etsi käyttäjät ja muokka heidän tietojaan. SSO-tunnisteiden on oltava yksilöllisiä.
  * **Käyttäjää ei löytynyt:** Tämä tarkoittaa, että pyydettyä käyttäjää ei ole. Korjataksesi tämän, varmista, että henkilö on olemassa palvelussa. Jos käyttäjä on jo palvelussa, varmista, että käyttäjien tunnistamiseen käytetyillä tiedoilla on oikea arvo. Voit tarkistaa, mitä tietokenttää käytetään käyttäjien tunnistamiseen SSO:ssa kohdassa Työsuhde>Hallinta>Kertakirjautuminen (SSO)>Henkilön tunnistustieto-kenttä.


# SSO ei toimi kenelläkään
Kertakirjautumisen (SSO) asettaminen voi olla monimutkainen prosessi. Teknisen asiantuntijan tulee käsitellä sitä mahdollisuuksien mukaan. Tämä sivu sisältää yleisimmät vianetsintävinkit SSO-määrityksiin liittyviin ongelmiin.
SSO-virheilmoitukset tallennetaan palvelulokiin, joka löytyy palvelusta Työsuhde > Hallinta > Palveluloki. Jos SSO ei toimi, tämän tulisi olla ensimmäinen paikka, josta tarkistat lisätietoja kirjautumisongelmasta.
## Tarkasta asetukset kohdasta Työsuhde >Hallinta >Kertakirjautuminen (SSO)
Varmista, että kaikki määritykset on tehty ja että voimassa oleva varmenne on asennettu. Lisätietoja identiteettitarjoajan määrittämisestä on ohjeessa [ADFS-palvelimen määrittäminen Neptonissa](<https://support.nepton.com/hc/fi/articles/360005242897>).
## Palveluntarjoajaa ei ole saatavana tai Virhe ladattaessa identiteettipalvelujen tarjoajan SSO-määrityksiä  

Tämänkaltainen virheviesti viittaa siihen, että jokin meni pieleen palvelussa. Jos näet tämän virheviestin, ole yhteydessä Neptonin asiakaspalveluun.
## Kumppanin identiteetin tarjoajaa ei voitu asettaa, Virhe lähetettäessä pyyntöä identiteetin tarjoajalle tai Virhe vastaanotettaessa pyyntöä identiteetin tarjoajalta
  1. Tarkista, että kaikki oikeat määritysarvot on tallennettu (Työsuhde > Hallinta > Kertakirjautuminen (SSO)).
  2. Varmista, että voimassa oleva varmenne on asennettu ja että se ei ole vanhentunut.
  3. Jos olet juuri asentanut uuden varmenteen ja se tarvitsee myös salaussertifikaatin asennettavaksi, lähetä salaussertifikaatti Neptonin asiakaspalveluun asian hoitamiseksi.
  4. Pyydä identiteettitarjoajan asettamisesta vastuussa olevaa henkilöä etsimään mahdolliset virheet ADFS-palvelimelta ja lähettämään virheilmoitukset Neptonille. Nämä virheilmoitukset ovat erittäin tärkeitä Neptonille SSO-ongelmien ratkaisemisessa.


## SSO-kirjautuminen epäonnistui, koska kellot eivät ole synkronoituja
Jos saat tämän viestin, varmista, että identiteetintarjoajan palvelimen päivämäärä ja aika ovat synkronoituja.
## SAML-vahvistusallekirjoituksen vahvistaminen epäonnistui
Jos saat tämän viestin, varmista, että varmenne on voimassa eikä se ole vanhentunut. Näet varmennetiedot kohdasta Työsuhde > Hallinta > Kertakirjautuminen (SSO).
## Omalla palvelimellasi on käynnissä erillinen Nepton esiintymä
Yleisimmät kolmannen osapuolen palvelimilla kohdatut SSO-ongelmat johtuvat synkronoimattomista päivämäärä- ja aika-asetuksista. Tarkista, että palvelimesi päivämäärä ja aika on synkronoitu Suomen normaaliajan kanssa.
Tämän ongelman välttämiseksi on suositeltavaa, että palvelimet määritetään automaattisesti synkronoitumaan luotettavan NTP-aikapalvelimen kanssa säännöllisesti. Ota yhteyttä palvelimen järjestelmänvalvojaan saadaksesi lisätietoja palvelinympäristöstäsi ja määrityksistä.
# Yleisiä varmenneongelmia
SAML SSO vaatii palveluntarjoajilta varmenteita, jotka osoittavat luotettavuuden todennuksen ja viestinnän aikana. Joissakin tapauksissa tarvitaan useita varmenteita niin kutsutun luottamusketjun muodostamiseksi.
SSO-määrityksiisi liittyviä varmenteita hallitaan kohdasta Työsuhde > Hallinta > SSO-määritykset.
## Minulla ei ole varmennetta
Kun määrität SSO:n ensimmäisen kerran SAML:n avulla, sinun on toimitettava tarvittavat varmenteet identiteettitarjoajasi kanssa viestimiseen. Katso [SSO:n määrittäminen](<https://support.nepton.com/hc/fi/articles/360002590097>) -artikkeli.
## Varmenteessani on varoituksia
Jos käyttämässäsi varmenteessa on ongelmia, tiedot ongelmasta/ongelmista näkyvät hallintasivun oikealla puolella. Yleisimmät varoitustyypit ovat, että varmenne on pian vanhentumassa tai vanhentunut, luottamusketju on epätäydellinen tai sinulla ei ole aktiivisesti käytössä varmennetta.
### Varmenne on vanhentumassa tai jo vanhentunut
Jos sertifikaattisi on vanhenemassa pian tai on jo vanhentunut, siitä näkyy varoitus SSO-määrityssivuilla. Varoitukset voimassaolon päättymisestä ilmestyvät useita kuukausia ennen viimeistä voimassaolopäivää, ja niissä mainitaan tarkalleen, milloin sertifikaattisi vanhenee. Sinun on vaihdettava todistuksesi/todistukset ennen tätä päivämäärää.
Uusien varmenteiden tilaaminen viranomaiselta voi viedä jonkin aikaa, joten kannattaa toimia ripeästi ja hankkia uudet varmenteet ajoissa. Sinun tulee keskustella palveluntarjoajasi kanssa siitä, kuinka tilata uusi varmenne ja mistä.
Kun korvaavat varmenteet ovat saapuneet, voit lisätä ne SSO-määrityksiin ja määrittää päivämäärän ja kellonajan, jolloin ne otetaan käyttöön. Tämä päivämäärä ja kellonaika tulee sovittaa yhteen palveluntarjoajan kanssa, jotta varmistetaan saumaton vaihto, joka ei häiritse loppukäyttäjiä.
### Puuttuva varmenne luottamusketjusta
Jotkut viranomaiset vaativat useampaa kuin yhtä varmennetta luottamuksen vahvistamiseen ja aitouden todistamiseen. Näissä tilanteissa kaikki asiaan liittyvät varmenteet on lisättävä SSO-määrityksiin. Ns. juurivarmenne tulee lisätä Varmenteet-osioon ja kaikki sitä tukevat varmenteet Tukivarmenteet-osioon.
### Ei aktiivista varmennetta
Jotta loppukäyttäjille ei aiheudu häiriöitä, sinulla on oltava aktiivinen varmenne, joka on lisätty ja määritetty käytettäväksi aina.
Jos olet määrittämässä uutta SSO:ta, etkä ole vielä lisännyt varmenteita, lue ohjeet [SSO:n määrittämisestä](<https://support.nepton.com/hc/fi/articles/360002590097>).
Jos sinulla on useita varmenteita, voit asettaa päivämäärän, josta jokainen sertifikaatti otetaan käyttöön. Tämä helpottaa saumatonta vaihtoa vanhoista varmenteista uusiin ilman keskeytyksiä loppukäyttäjien SSO-kirjautumisominaisuuksissa.
Jos haluat määrittää varmenteen aktiiviseksi, valitse yksi sertifikaateistasi, joka on voimassa oikeana päivänä, ja paina Aloita varmenteen käyttö.
