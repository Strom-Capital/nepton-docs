---
id: 360006615478
title: Julkaisutiedotteet
url: https://support.nepton.com/hc/fi/articles/360006615478-Julkaisutiedotteet
locale: fi
category: Palvelun tila ja versiot
category_id: 22476701377821
section: Palvelun tila ja versiot
section_id: 360000934197
section_path:
- Palvelun tila ja versiot
labels:
- REFERENCED_FROM_SERVICE
promoted: false
updated_at: '2026-11-16T11:25:48Z'
edited_at: '2026-11-16T11:24:22Z'
---

# Julkaisutiedotteet

Neptoniin julkaistaan säännöllisesti parannuksia ja korjauksia eri huoltoikkunoiden aikana. Tällä sivulla ilmoitetaan tulevista päivityksistä aina ennen julkaisua. Tarkemmat tiedot huoltoikkunoista sekä palvelun tilasta löytyvät [**Palvelun tila**](<https://support.nepton.com/hc/fi/articles/360006554777>) -sivulta. Suosittelemme myös ottamaan käyttöön [**artikkelin seurannan**](<https://support.nepton.com/hc/fi/articles/4406604045585-Artikkelien-seuraaminen>), jotta saat ilmoitukset uusista julkaisuista.
##  **17.11.2026** julkaisu (2.18.6)
###  __ Uutta 
  * #### Nepton tyytyväisyyskysely H2 2026
Kysely esitetään esimiehille ja hallinnallisille rooleille 23.11. ja työntekijöille 25.11. alkaen.
[Lisätietoa](<https://support.nepton.com/hc/fi/articles/16439727874717-Palautteesi-on-meille-t%C3%A4rke%C3%A4%C3%A4>)
[ref 5423]


###  __ Parannus 
  * #### Työsuhde-osion suorituskykyä parannettu.
[ref 4866, 5361]


###  __ Korjaukset 
  * #### Päättynyt oletusprojekti ei enää ole oletuskohdenteena Nepton Flexim -päätteellä aloitettavassa tapahtumassa.
[ref 3723]
  * #### Nepton Flexim -päätteellä aloitettuja tapahtumia ei enää tallenneta päättyneelle projektille, mikäli päätteellä valittuna oleva projekti merkitään päättyneeksi ennen tapahtuman aloitusta.
[ref 4943]
  * #### Viikkolepojakso lasketaan oikein tilanteissa, joissa ansaintakauden peruste-asetus on "Työ ennen seuraavan viikon ensimmäistä vuoro" ja päivälle on tehty vuoropoikkeama.
[ref 5249]
  * #### Henkilötietosivu aukeaa nopeasti myös asiakkaille, joilla henkilöryhmähierarkia on suuri.
[ref 5361]
  * #### Osapäivän poissaolo jolle oli määritetty että kiinteää lopetustyötä ansaitaan, kun poissaolo alkaa työn päättyessä, ei ansainnut kiinteää lopetustyötä oikein, kun osapäivän poissaolon alku ennen vuoron loppua oli sama kuin kiinteän lopetustyön korvattu aika.
[ref 5417]


##  **10.11.2026** julkaisu (2.18.5)
###  __ Korjaukset 
  * ####  Valikossa 'Työkalut > Aseta tapahtumien lukituspäivä' esihenkilön rajaukseen oli mahdollista valita ainostaan alaisuuden tai sijaisuuteen perustuvia henkilöitä, vaikka henkilöllä oli oikeus tarkastella kaikkia ympäristön henkilöitä. 
[ref ND-5309]
  * ####  Henkilön tiedoissa esihenkilövalikossa henkilö esitetään vain kertaalleen. 
[ref ND-5315]
  * #### Mukautetun raportin esikatselu ei toiminut.
[ref ND-5318]
  * ####  Tapahtuman muokkauslomakkeen avaaminen saattoi aiheuttaa virheen, mikäli henkilöllä oli ainoastaan ruokailu-tapahtumien muokkausoikeus. 
[ref ND-5323]
  * ####  Kirjauspäätteellä on nyt mahdollista lisätä tapahtumia kahden vuoden päähän. 
[ref ND-3694]


##  **03.11.2026** julkaisu (2.18.4)
###  __ Parannukset 
  * ####  Kiinteää lopetustyötä voidaan nyt ansaita, kun työntekijä pitää työn jälkeen osapäivän poissaolon. - Poissaolotapahtumatyypit, joiden alkaessa kiinteää lopetustyötä voidaan ansaita, voidaan määrittää asetuksella 'Kiinteää lopetustyötä ansaitaan, kun poissaolo alkaa työn päättyessä'. 
[ref ND-2717]
  * ####  Henkilö-viennit tukevat nyt RFC 4180 -standardin mukaista arvojen käsittelyä CSV-tiedostojen viennin rikkoutumisen estämiseksi, kun arvot sisältävät kenttäerottimen (;) tai lainausmerkkejä ("). 
[ref ND-3053]
  * ####  Lopetustyön kiinteän korvauksen ansaitseminen voidaan nyt rajata niihin päiviin, joiden palkallinen työaika on asetettua rajaa pienempi tai suurempi. - Rajat voidaan määrittää asetuksilla 'Kiinteä korvaus, jos palkallinen työaika on alle' ja 'Kiinteä korvaus, jos palkallinen työaika on yli'. 
[ref ND-3859]


###  __ Korjaus 
  * ####  Joissakin tapauksissa käyttäjä ei voinut avata Työaikaa, jos hänellä ei ollut oikeutta tarkastella omia tapahtumiaan. 
[ref ND-5319]


##  **28.10.2026** julkaisu (2.18.3)
###  __ Parannus 
  * ####  Kirjauspäätteiden hakua voidaan suodattaa tilan mukaan valikossa Työsuhde > Hallinta. 
[ref 5196]


###  __ Korjaukset 
  * ####  Toteutuneen työajan määrä -raportti ei näytä enää ylöspäin pyöristettyä työaikaa, vaan pelkän aidosti tehdyn työajan. 
[Ohje](<https://support.nepton.com/hc/fi/articles/360016836978>)  
[ref 2834]
  * ####  Ilmoitusten sähköpostiviestin linkit avaavat nyt kohdesivun myös SSO-käyttäjille. 
[ref 4336]
  * ####  Maksuryhmän muokkaus saattoi aiheuttaa virheen, mikäli palkkakauden aineistopäivä tyhjennettiin. 
[ref 5288]
  * #### Palveluloki näyttää lokimerkinnät uusimmasta vanhimpaan.
[ref 5299]
  * ####  Projektitunnit tapahtumatyypeittäin -raportti näytti kaikki tapahtumatyypit, jotka käyttäytyvät kuin vuosiloma päivinä, joilla projektitunteja oli kirjattu vuosilomalle. 
[ref 5302]
  * ####  Tuo henkilöitä -toiminto näyttää ladatun tiedoston nimen oikein. 
[ref 5313]


##  **22.10.2026** julkaisu (2.18.2)
###  __ Korjaukset 
  * ####  EndActivity-metodi palautettu työajan WebService API-rajapintaan 
[ref ND-5312]
  * ####  Palautettu vuosilomien ja ruokailutapahtumien raporttien näkyvyys kaikille käyttäjille 
[ref ND-5310]
  * ####  Vuosilomien käyttö kausittain raportti ei ollut käytettävissä, jos käyttäjällä ei ollut oikeutta tarkastella kenenkään työtapahtumia, mutta hänellä oli oikeus tarkastella kaikkien vuosilomaraportteja 
[ref ND-5310]


##  **20.10.2026** julkaisu (2.18.1)
###  __ Korjaukset 
  * ####  Tapahtumapyyntöjen hyväksynnässä kertymäarvot esitettiin tietyissä tilanteissa väärillä sarakkeilla. 
[ref ND-3597]
  * ####  Ilman aloitus- ja lopetusaikaa tuoduille tapahtumille saatettiin muodostaa aika "12:00 - 12:00", mikäli tapahtuma ajoittui vuorokalenterin vuorojen väliselle tyhjälle päivälle. 
[ref ND-3843]
  * ####  Tapahtumien tuontien määritysten järjestysnumerot säilytetään liittymien asetusnäkymässä. Aiemmin määritykset esitettiin aakkosjärjestyksessä. 
[ref ND-4859]
  * ####  Ajastettu liittymä saattoi lähettää sähköpostiin tiedoston väärällä .zip -päätteellä, mikäli sääntöjoukon tulosten jakaminen useaan tiedostoon oli käytössä ja liittymän tuloksista muodostettiin ainoastaan yksi tiedosto. 
[ref ND-5061]
  * ####  Mobiilissa päivämääräkentät eivät aina auenneet tapahtuman muokkausikkunassa. 
[ref ND-5268]


##  **17.10.2026** julkaisu (2.18.00)
###  __ Parannukset 
  * ####  Tietoturva- ja suorituskykyparannuksia sekä taustajärjestelmien päivityksiä. 
[ref ND-2208, ND-2166, ND-2163, ND-2240, ND-2221, ND-3747, ND-2211]
  * #### Parannettu ryhmittelyä henkilövalikoissa.
    * Ryhmittely maksuryhmillä huomioi nyt henkilön maksuryhmien voimassaoloajat. 
    * Henkilö näytetään henkilövalikoissa vain yhden kerran saman asetusryhmän alla. 
[ref ND-3712]
  * ####  Parannuksia reaaliaikaisten liittymien virheiden käsittelyyn. 
[ref ND-5073]
  * ####  Microsoft-kirjautuminen: lisätty UPN-tuki (User Principal Name) tunnuksille, joilla ei ole sähköpostiosoitetta. 
[ref ND-5246]
  * ####  BeginActivity ja EndActivity API-rajapintametodeissa (kaikki versiot) parannettu TerminalId-kentän toimintaa: 
Kentällä voidaan tuoda vain Nepton-ympäristöön liitetyn työaikapäätteen tunniste. Palvelu ei suorittanut kaikkia tarkistuksia tuotavan työaikapäätteen tunnisteen osalta eikä antanut asianmukaista virheilmoitusta tietyissä tilanteissa. 
[BeginActivityV2](<https://support.nepton.com/hc/fi/articles/6869562936221>)  
[EndActivityV2](<https://support.nepton.com/hc/fi/articles/6870443544477>)  
[ref ND-5176]
  * ####  Nepton Palkat: Tuntipalkan koko historiatieto voimassaolojaksoineen lähetetään nyt Palkkaukselle. 
[ref ND-3505]


###  __ Muutos 
  * ####  Työsopimusten käsittelyä on parannettu. Sopimustiedot tallennetaan nyt vasta työnantajan hyväksynnän jälkeen. 
[ref ND-2862]


###  __ Korjaukset 
  * ####  Työajan navigointikohteiden näkyvyyksiin on tehty korjauksia. 
[ref ND-2745]
  * ####  Joissakin tapauksissa työajan raporteissa listattiin raportteja, joihin käyttäjällä ei ollut käyttöoikeutta. 
[ref ND-2745]
  * ####  Henkilöryhmiä voidaan nyt hallinnoida oikeilla käyttöoikeuksilla. 
    * Aiemmin käyttäjällä tuli olla "Kaikki ylemmän tason ja ylempää tasoa alemmat oikeudet" oikeus. Nyt "Voi hallinnoida työajan henkilöryhmiä" oikeus antaa pääsyn henkilöryhmien hallintaan. 
[ref ND-2745]
  * ####  Palvelupyynnön lisääminen ilman päivämäärää aiheutti virheen. 
[ref ND-5044]
  * ####  Hyväksy tapahtumapyyntöjä -näkymässä tapahtumapyynnön hyväksymisen yhteydessä annettu viesti ei tallentunut. 
[ref ND-3599]
  * ####  Mobiilinäkymä ei auennut, mikäli päivällä oli suunniteltu vuoro ja ainoastaan ruokailu-tapahtuma. 
[ref ND-5188]
  * ####  Rajaa Nepton API käyttäjiä -asetuksen IP-osoitteessa ei ollut mahdollista käyttää asteriskia (esim. 83.150.*). 
[ref ND-5168]
  * ####  Vuosilomille kohdennettu työ näytetään projektiraporteilla johdonmukaisesti ja vuosiloman määrä näytetään tunteina päivien sijaan. 
[ref ND-3697]
  * ####  Palkattomia poissaoloja ei enää näytetä Projektitunnit henkilöittäin -raportilla. 
[ref ND-5245]
  * ####  Kalenterin synkronointi ei synkronoinut vuorokalenterin vuoroja. 
[ref ND-4361]
  * ####  Viikoittaisesta ylityöstä erillisenä ansaittu TES-ylityö ei näkynyt päivän ylitöiden erittelyssä Tapahtumat kalenterissa -näkymässä. 
[ref ND-2842]
  * #### PIN-koodi-henkilötietokentän enimmäismerkkimäärän poisto: 
Nyt myös yli 6 numeroa pitkät PIN-koodit voidaan syöttää suoraan henkilön tietoihin PIN-koodi -henkilötietokenttään tai tuoda henkilöille henkilötuonnin kautta. 
[ref ND-4831]
  * ####  Henkilötuonnin yhteydessä luotu käyttäjätunnus voi nyt olla enintään 100 merkkiä. 
[ref ND-4959]


## Vanhat julkaisutiedotteet
Jos etsit vanhempia julkaisutiedotteita, löydät ne [täältä](<https://support.nepton.com/hc/fi/articles/40011965488029>).
