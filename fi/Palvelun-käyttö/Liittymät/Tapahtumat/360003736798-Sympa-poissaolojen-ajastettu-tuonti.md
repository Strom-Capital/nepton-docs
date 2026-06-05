---
id: 360003736798
title: Sympa poissaolojen ajastettu tuonti
url: https://support.nepton.com/hc/fi/articles/360003736798-Sympa-poissaolojen-ajastettu-tuonti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumat
section_id: 360001061298
section_path:
- Liittymät
- Tapahtumat
labels: []
promoted: false
updated_at: '2025-08-25T11:20:38Z'
edited_at: '2025-08-25T11:20:38Z'
---

# Sympa poissaolojen ajastettu tuonti

Palveluun voidaan tuoda tapahtumia Sympasta. SFTP-palvelimelle tulee muodostaa csv-muotoinen aineisto. Muodostettavan aineiston tulee tiedostonimessä sisältää luontihetken aikaleima osana tiedostonimeä. Aikaleima lisätään tiedostonimen perään. Tällä varmistetaan, että aiempaa tiedostoa tietoa ei ylikirjoiteta esimerkiksi sellaisessa tilanteessa, jossa aineiston lukua ei ole suoritettu ajastuksen mukaisena.
Tiedosto tallennetaan UTF-8 koodauksella. Tietueet ovat erotettu puolipisteellä (`;`). Rivinvaihdon merkkinä on UNIX-merkki `LF`. Tämä rivinvaihto muodostuu oletuksena lähes kaikista tietojärjestelmistä.
Aineisto ei sisällä otsikkoriviä. Aineistossa yksi tapahtuma ja sen voimassaoloajat esitetään yhdellä rivillä. Aineiston rivit tulee muodostaa Sympasta siten, että vain edellisen siirron jälkeen luodut (rivintyyppi uusi) tai/ja poistetut poissaolot (rivin tyyppi poisto) sisältyvät aineistoon. Asetuksella "Menneiden päivien määrä siirtotiedostossa" ei siis ole vaikutusta Sympa tapahtumien ajastetulla tuonnilla, sillä kaikki aineistolla olevat tapahtumat käsitellään joko poistona tai lisäyksenä niiden päivämäärästä huolimatta. 
Tiedoston rivit käsitellään peräkkäisessä järjestyksessä. Esimerkiksi, jos ensimmäinen rivi lisää uuden tapahtuman 1. tammikuuta ja sitten toinen rivi poistaa tapahtuman 1. tammikuuta, se poistaa juuri luomansa tapahtuman. Tästä syystä, jos tuontitiedot jakautuvat useille tiedostoille, on varmistettava, että käyttäjiä ei ole useassa tiedostossa samanaikaisesti. Jos käyttäjiä on useassa tiedostossa samanaikaisesti, niin tiedostot tulee olla oikeassa järjestyksessä (tiedostoja käsitellään SFTP-palvelimella aikajärjestyksessä, jolloin ne luotiin).
Huom: Sympa ei lähetä niistä tapahtumista liittymällä tietoa, joita pääkäyttäjä on muokannut hyväksynnän jälkeen. Nämä tapahtumat tulee Sympan ohjeiden mukaan poistaa ja luoda uusi.
## Määrittäminen
### Henkilöiden tunnisteiden määrittäminen
Henkilöiden tunnisteet voidaan määrittää muokkaamalla henkilönumeroa henkilötiedoista **Työsuhde** > **Henkilön tiedot** > **Työsuhde** > **Henkilön tiedot** > **Tunnisteet**
![mceclip2.png](https://support.nepton.com/hc/article_attachments/22448143964317)
### Tapahtumien alku- ja loppukellonajan määrittäminen
Sympan tuonnin luomat tapahtumat luodaan tiedostojen tuonnissa määritettyjen päivämäärien ja työaika-asetusten mukaisesti. Navigoi **Työaika** > **Hallinta** > **Työyhteisön asetukset** / **Asetusryhmät** > **Työtunnit** > **Näytön asetukset** > **Työtapahtuman oletusalkuajankohta** ja **oletusloppuajankohta**. Arvoja 08:00 - 16:00 käytetään vakiona, jos aikoja ei ole määritetty.
HUOM: Mikäli oletetut työajat on käytössä, tapahtumat luodaan oletettujen työaikojen kellonaikojen perusteella.
### Poissaolojen ja lomien koodien, sekä SFTP-asetuksien määrittäminen
Poissaolojen ja lomien koodit sekä SFTP-asetukset voidaan määrittää kohdassa **Työaika** > **Hallinta** > **Työyhteisön asetukset** / **Asetusryhmät** > **Liittymät** > **Sympa**. Jos tapahtumatyypille on useita koodeja, nämä voidaan määrittää pilkulla eroteltuina.
SFTP-asetukset löytyvät vain työyhteisön asetuksista.
### Tuonnin ajastus
Automaattisen tuonnin ajastus voidaan asettaa kohdassa **Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Ajastus**. Ajastuksen määrittämisestä ja ajastusosiosta voit lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/10510800700573>)
### Osapäivän poissaolojen tuonti
Osapäivän poissaolot on mahdollista tuoda niin, että sarakkeessa 7 on poissaolon alkuaika ja sarakkeessa 8 poissaolon loppuaika. Jotta sarakeita käytetään, tulee seuraava asetus määrittää kohdassa **Työaika** > **Hallinta** > **Työyhteisön asetukset** > **Liittymät** > **Sympa** :
![](https://support.nepton.com/hc/article_attachments/11186904833309)
#### Osapäivän poissaolon kellonaikojen tulkinta
Jos tapahtuman alku- ja loppuajat on ilmoitettu valinnaisilla sarakkeilla, sijoitetaan tapahtuma käyttäjän työpäivälle annettujen aikojen mukaan.
## Tiedoston muoto
Jos tuotavassa aineistossa on enemmän kuin kuusi saraketta, tuonti jättää ylimääräiset sarakkeet huomioimatta.
Alla on luettelo aineiston tietueista ja niiden lisätiedoista.
Sarake | Tieto | Kuvaus  
---|---|---  
1 | Henkilönumero | Henkilönumero  
2 | Poissaolo / lomakoodi | Koodit on määritetty käyttöliittymässä Sympa-asetuksissa. Jos koodia ei ole, kalenteriin ei kirjaudu mitään tapahtumaa.  
3 | Tyyppi |  Uusi rivi vai vanhan rivin poisto. Seuraavat arvot hyväksytään:
  * `uusi` tai `false`
  * `poisto` tai `true`

Tyyppi 'uusi' luo uuden poissaolon. Tyyppi 'poisto' poistaa olemassa olevan poissaolon. **HUOM! Tapahtumaa poistettaessa on poisto-rivin oltava identtinen tapahtuman luonti-rivin ('uusi') kanssa. Mikäli uusi- ja poisto-rivit ovat erilaisia keskenään, ei tapahtumaa poisteta.**  
4 | Lomajakso | Käytössä ainoastaan loma-tapahtumilla, poissaoloilla se on tyhjä. Tallennetaan selitteenä.  
5 | Alkupäivä | Tapahtuman alkupäivä, formaatti `PP.KK.VVVV`  
6 | Loppupäivä | Tapahtuman loppupäivä, formaatti `PP.KK.VVVV`  
7 | Alkuaika |  Valinnainen tieto. Poissaolon alkuaika, formaatti `HH:MM`  
8 | Loppuaika |  Valinnainen tieto. Poissaolon loppuaika, formaatti `HH:MM`  
Alla esimerkki muodostetun tiedoston sisällöstä:
[code] 
    445;101;uusi;;02.05.2016;04.05.2016;  
    445;103;uusi;;03.05.2016;06.05.2016;08:00;16:00  
    445;101;poisto;;02.05.2016;03.05.2016;  
    445;200;uusi;"lomajakso, jotain jotain";01.06.2016;28.06.2016  
    445;200;uusi;"lomajakso, jotain jotain. Väärät päivät edellisessä";06.06.2016;02.07.2016  
    445;200;poisto;"lomajakso, jotain jotain";01.06.2016;28.06.2016 
[/code]
