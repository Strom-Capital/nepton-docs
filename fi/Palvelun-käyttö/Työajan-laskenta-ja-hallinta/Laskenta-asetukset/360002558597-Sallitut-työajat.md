---
id: 360002558597
title: Sallitut työajat
url: https://support.nepton.com/hc/fi/articles/360002558597-Sallitut-ty%C3%B6ajat
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels: []
promoted: false
updated_at: '2026-10-09T07:36:13Z'
edited_at: '2026-10-09T07:32:54Z'
---

# Sallitut työajat

Sallitut työajat määrittävät kellonajat, joiden ulkopuolella tehtyä työtä ei tulkita työajaksi. Sallittu työaika voi muodostua joko määritettyjen asetusten mukaisesti tai suunnitellun työvuoron perusteella.
Tässä artikkelissa käydään läpi sallittujen työaikojen määrittäminen sekä asetuksilla että vuoron perusteella muodostuvaksi. 
## Sallitun työajan määrittäminen asetuksilla
Sallitut työajat voidaan määrittää joko Työyhteisö- tai asetusryhmätasolla kohdassa **Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Työtunnit > Sallitut työajat**. Ensimmäinen asetus määrittää, onko sallitut työajat lainkaan käytössä. "Käytössä" asetuksella voidaan estää ylemmältä asetusryhmätasolta määritysten periytyminen alatasolle, mikäli tällä tasolla ei haluta käyttää sallittuja työaikoja.
![](https://support.nepton.com/hc/article_attachments/29868778760221)
Sallittujen työaikojen määrittämiseen asetuksilla on käytettävissä kahta tapaa. Asetustavat ovat ”Päiviin, joille työvuoro osuu” sekä ”Päivään, jolle työvuoro kuuluu”. Mikäli arvoa ei ole asetettu, käytetään ”Päivään, jolle työvuoro kuuluu” -asetusta.
### Asetustapa: Päiviin, joille työvuoro kuuluu
Suosittelemme käyttämään asetusta "Päiviin, joille työvuoro kuuluu". Tämä on uudempi tapa (julkaistu 8.3.2025) määrittää sallitut työajat, ja tässä asetustavassa sallittujen työaikojen voimassaoloajat määritetään yhdellä voimassaoloasetuksella. Sallitut työajat ovat täten oletuksena voimassa viikon jokaisena päivänä. Voimassaoloaikojen poikkeusasetuksia, kuten päivämäärä- tai tapahtumatyyppiperusteisia poikkeuksia, voidaan edelleen määrittää tälläkin asetustavalla.
Oleellisin ero vanhempaan sallittujen työaikojen määrittelytapaan (Asetustapa: Päiviin, joille työvuoro osuu) on voimassaoloaikojen hyödyntäminen sen päivän mukaisesti, [jolle työajan tulkintakin kuuluu](<https://support.nepton.com/hc/fi/articles/360008777997>).
![](https://support.nepton.com/hc/article_attachments/29868821780253)
Sallittujen työaikojen kellonajat määritellään yhdelle tai kahdelle riville (jos päivällä on kaksi eri sallittua työajan pätkää), ja ne koskevat tällöin jokaista viikonpäivää. [Poikkeusasetuksilla](<https://support.nepton.com/hc/fi/articles/360002560677>) määritellään poikkeukset tähän kaavaan. Esimerkiksi "käytössä" asetukseen voidaan määrittää poikkeus, että sallitut työajat eivät ole käytössä lauantaisin ja sunnuntaisin. Tällöin sallitut työajat koskevat vain arkipäiviä.
![](https://support.nepton.com/hc/article_attachments/30054663721757)
Poikkeusasetuksia voidaan tehdä myös esimerkiksi päivämäärästä, käytetyistä tapahtumatyypeistä ja ylityönkohdenteista riippuen useita. Tarkemmat ohjeet eri poikkeusasetusten määrittelyyn löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360002560677>).
#### Esimerkki 1 - Poikkeavat sallitut työajat juhlapyhinä
Otetaan esimerkiksi tapaus, jossa sallitut työajat ovat normaalisti ma-pe klo 07-18. Lauantaisin ja sunnuntaisin niitä ei ole ollenkaan (asetukset kuten kuvattu edellisessä kappalessa). Juhlapyhinä halutaan kuitenkin rajoittaa, että sallitut työajat ovatkin vain klo 10-15 välisellä ajalla. Tällöin asetetaan asetuksen perusarvoksi 07-18, sallitut ajat pois käytöstä lauantaisin ja sunnuntaisin, ja tehdään vielä seuraava poikkeus 'Voimassa' -asetukseen:
![](https://support.nepton.com/hc/article_attachments/30054663727901)
Näillä määrityksillä sallitut työajat ovat ma-pe 07-18 ja juhlapyhinä 10-15.
#### Esimerkki 2 - Sallitut työajat vuorokauden vaihtuessa
Kun sallitut ajat koskevat kahta eri vuorokautta, on asetuksella "Työtapahtumien näyttö" suuri vaikutus tulkintaan. Esimerkiksi, jos halutaan, että tapahtumat näytetään päivänä jona vuoro loppuu:  
![](https://support.nepton.com/hc/article_attachments/30059970146461)
Ja sallitut ajat halutaan asettaa klo 23-07, eli koskemaan kahta vuorokautta. Tällöin sallittujen aikojen 'voimassa' asetuksiin määriteltäisiin, että ne ovat voimassa klo 23 **edellisenä** päivänä, ja loppuvat klo 07 **nykyisenä** päivänä:
![](https://support.nepton.com/hc/article_attachments/30059985176349)
Jolloin sallitut työajat tulkitaan oikein linjassa työtapahtumien näytön kanssa:
![](https://support.nepton.com/hc/article_attachments/30059970150813)
Mikäli sallittuihin aikoihin olisi laitettu klo 23:00 nykyisenä päivänä ja 07:00 seuraavana päivänä, ei 23-07 ajalle tehdystä työkirjauksesta tulkittaisi mitään, sillä se olisi sallittujen työaikojen ulkopuolella. Jos taas näytön asetuksissa olisi asetettu, että tapahtumat näytetään päivänä, jona vuoro alkaa, olisi oikea sallittujen aikojen määrittely juurikin nykyinen - seuraava päivä. 
### Asetustapa: Päiviin, joille työvuoro osuu
Vaikka uudempi tapa määrittää sallitut työajat on julkaistu, voidaan palvelussa edelleen käyttää vanhempaa tapaa "Asetustapa: Päiviin, joilla työvuoro osuu" sallittujen työaikojen määrittämiseen.
Sallitut työajat määritellään alkamaan ja päättymään per viikonpäivä. Määrittelyssä valitaan aloitusaika ja se, onko aika edellisen, nykyisen vai seuraavan päivän kellonaika.
![](https://support.nepton.com/hc/article_attachments/20572330203037)
Voimassaoloaikoihin on mahdollista asettaa kaksi eri arvoa. Tämä on tarpeellista esim. silloin, kun tehdään töitä vuorokauden vaihtuessa. Ensimmäinen voimassaoleva arvo tulee ylempiin kenttiin, ja seuraavat arvot alempiin kenttiin. Kahta arvoa käyttämällä voidaan katkottaa sallitut työajat päivälle, esim. niin, että sallitut työajat ovat klo 06-11 ja 16-21.   
![](https://support.nepton.com/hc/article_attachments/15026203098397)
Asetuksella "tai sallitun työajan kesto jos lopetusaika riippuu aloitusajasta:" voidaan määrittää, että sallitulla työajalla on tietty kesto, jonka jälkeen työ ei enää ole sallittua. Tällöin itse ajat vaihtelevat työn aloituksesta riippuen.
### Ylityön korvaustyypit, joita sallitut työajat voidaan määritellä koskevaksi
Sallittujen työaikojen määrityksissä kohdassa **Rajoita kun ylityön kohdenne** määritellään, missä ylityökohdenteissa sallitut työajat huomioidaan ja vastaavasti missä niitä ei huomioida. Mikäli rajoituksia ei ole määritelty, rajataan kaikki sallittujen työaikojen yli menevä työaika.
Mikäli ylityön kohdennetyyppiä ei ole rajoitettu, ylityön kohdenteen avulla määritellään miten säännöllisen työajan ylittävä aika halutaan korvata. Ylityön kohdenne tallennetaan osana tapahtumaa, ja se on nähtävissä Ylityö-otsikon alta tapahtuman lisäämisen tai muokkaamisen ikkunassa.  
  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360004650118)
### Tapahtumatyyppikohtaiset ohitukset
![](https://support.nepton.com/hc/article_attachments/19038023413277)
Palvelussa voidaan myös ohittaa määritetyt sallitut työajat tiettyä tapahtumatyyppiä ja ylityön kohdennetta käytettäessä. Jos esimerkiksi "Rajoita kun ylityön kohdenne" kohdenteelle "ylityö - palkkaan" on voimassa, mutta sallittujen työaikojen ei haluta olla voimassa siinä tapauksessa kun tapahtumatyyppinä on "Työ", voidaan tähän asetukseen määrittää nämä ehdot. Yllä olevassa kuvassa on annettu Työ-tapahtuman ylityökohdenteella ylityö-palkkaan ohittaa sallitut työajat, kun taas Työ muualla -tapahtuma Tunti-tunnista saldoon ohjauksella ei.
### Työn salliminen ennen suunniteltua vuoroa ja vuoron jälkeen
![](https://support.nepton.com/hc/article_attachments/19038023421341)
Mikäli käytössä on vuorosuunnittelu, määritellyille tapahtumatyypeille on mahdollista sallia tietty määrä sallittua aikaa, jota voidaan ansaita ennen suunniteltua vuoroa ja vuoron jälkeen. Sallittu aika ansaitaan, vaikka sallitut työajat muuten rajoittaisivat tätä. Yllä olevassa esimerkissä "Työ" tapahtumatyypillä voitaisiin ansaita palkallista aikaa 2 tuntia ennen vuoroa ja 3 tuntia vuoron jälkeen. "Työ"-tapahtumakirjauksen tulee kuitenkin osua edes osittain vuoron ajalle, jotta työajan tulkinta ennen vuoroa ja vuoron jälkeen sallitaan tämän asetuksen mukaan.
Huom! Asetus rajoittaa ansaittua aikaa ennen suunniteltua vuoroa ja vuoron jälkeen vaikka sallitut työajat eivät olisi voimassa.
Huom! Asetus ei muuta sallittuja aikoja kalenterinäkymässä.
## Sallitun työajan poikkeuksen asettaminen yksittäiselle päivälle
Sallittuja työaikoja voidaan muokata päiväkohtaisesti yhdelle henkilölle, mikäli erikoissyystä on tarve venyttää sallittua työaikaa yksittäiselle päivälle. Muokkaus tehdään suoraan kyseisen henkilön kalenterinäkymästä, painamalla halutun päivän päivämäärää ja aukeavasta valikosta valitaan **Sallitut työajat**.
![](https://support.nepton.com/hc/article_attachments/29871160819229)
Valitsemalla **Sallitut työajat** aukeaa uusi ikkuna, johon määritellään kyseiselle päivälle asetusryhmän asetuksista poikkeavat sallitut työajat. Yksittäisen päivän poikkeusasetusta käytettäessä sallitut työajat tulee aina asettaa käyttäen kellonaikoja 'Nykyisenä päivänä' (Jos työkirjaus menee vuorokauden vaihteen yli, tehdään poikkeus kummallekin työpäivälle asettaen haluttu kellonaika 'nykyisenä päivänä').
Jos esimerkiksi asetusryhmästä tulevat sallitut työajat ovat klo 07-18, mutta poikkeustilanteessa halutaan sallia työnteko jo klo 06 alkaen, asetetaan haluttu alkamisaika poikkeusikkunaan ja painetaan 'Tallenna'.
![](https://support.nepton.com/hc/article_attachments/32016856193437)
Poikkeusasetus tallentuu ja asetetun poikkeuksen näkee kalenterinäkymässä klikkaamalla päivämäärää.
![](https://support.nepton.com/hc/article_attachments/29871190464925)
Sallitun työajan päiväkohtaisen poikkeuksen saa poistettua painamalla päivämäärää ja valitsemalla aukeavasta valikosta Sallitut työajat uudestaan. Asetettu poikkeus poistetaan painamalla "Poista poikkeus"-painiketta.  
  
![](https://support.nepton.com/hc/article_attachments/32016856196253)
## Sallitun työajan asettaminen suunnitellulta vuorolta
Asetuksilla määritellyn sallitun työajan lisäksi voidaan asettaa sallittu työaika muodostuvaksi työvuoroilta. Asetus löytyy Työyhteisö- tai asetusryhmätasolla valikosta **Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Vuorot.**
Asetuksilla **Sallittu työn aloitusajan poikkeama suunnitellun vuoron alussa** ja **Sallittu työn lopetusajan poikkeama suunnitellun vuoron päättyessä** voidaan ohjata, kuinka pitkältä ajalta työaikaa voidaan ansaita ennen työvuoroa tai työvuoron jälkeen. 
![](https://support.nepton.com/hc/article_attachments/26620685405725)
Sallitun työn aloitus- ja lopetusajan lisäksi tulee Työtunnit-osion **Sallitut ajat** -asetuksissa määrittää salittut ajat käyttöön ja sallitut ylityön korvaustyypit. Tarkemman kuvauksen sallitun työn ylityön korvaustyyppien määrittelyistä löydät [tästä artikkelista](<https://support.nepton.com/hc/fi/articles/360002558597-Sallitut-ty%C3%B6ajat>).
## Sallitun työajan asettaminen vuorokohtaisesti
Sallitut työajat voidaan määritellä suoraan myös Vuorosuunnittelun suunnittelunäkymässä yksittäisille vuoroille. Toiminnallisuus on nähtävissä ja käytettävissä yksittäisen vuoron luomisessa ja sitä voidaan hyödyntää olemassa olevien vuorojen muokkauksessa.
Kenttä **Sallittu työn aloitusajan poikkeama** ja **Sallittu työn lopetusajan poikkeama** löytyvät vuoron tiedoista omina kenttinään. 
![](https://support.nepton.com/hc/article_attachments/39777376727453)
Kumpaankin kenttään voidaan asettaa poikkeama sallituille työajoille suhteessa työvuoron alkamis- ja loppumisaikaan. Poikkeama voidaan asettaa kahdella eri tavalla:
  * minuuttiperusteinen poikkeama suhteessa vuoron alkamiseen tai päättymiseen (esim. -10 ja +10)
  * tarkka aika hh:mm-muodossa – sallittu työaika alkaa tai päättyy asetettuun kellonaikaan (esim. 06:50 - 14:10)


Esimerkiksi aamuvuoron 07:00 - 14:00 osalta, sallittu työn aloitusajan poikkeama-kentän -10 saa sallitun työajan alkamaan 10 minuuttia ennen vuoron alkua klo 06:50. Sallittu työn lopetusajan poikkeama-kentän +10 tekee sallitun työajan päättyneeksi 10 minuuttia vuoron päättymisen jälkeen klo 14:10. Poikkeama arvolla 0 tarkoittaa, että sallittu työaika vastaa täsmälleen työvuoroaikaa.
![](https://support.nepton.com/hc/article_attachments/39777389282589)
Vastaava esimerkki samalla lopputuloksella kellonajoilla hh:mm-muotoisena:  
  
![](https://support.nepton.com/hc/article_attachments/39777376730269)
Sallittu työn aloitusajan poikkeama- ja Sallittu työn lopetusajan poikkeama -asetuksia voidaan hyöyntää myös vuorokalenterien vuorotyypeissä. Tällöin sallitun työajan poikkeama pätee aina tähän vuorotyyppiin. Vuorokalenterien vuorotyyppien osalta poikkeaman määrittämisen periaate on sama, aloitus- ja lopetusajalle on käytettävissä omat kentät vuorotyyppien luonnissa sekä niiden muokkauksessa.  
  
![](https://support.nepton.com/hc/article_attachments/39779022419613)  
  
Vuorosuuunnittelun suunnittelunäkymässä yksittäiselle vuorolle tai vuorokalenterin vuorotyypille tällä tavoin asetetut sallitut työajat ohittavat Työajan asetuksessa "Sallittu työn aloitusaika tulee suunnitteltu vuorolta" ja "Sallittu työn lopetusaika tulee suunnitellulta vuorolta" määritetyn poikkeaman. Jos yksittäisen työvuoron sallittujen työaikojen poikkeamien kentät jätetään tyhjiksi, em. asetuksia käytetään kuten ennenkin.
