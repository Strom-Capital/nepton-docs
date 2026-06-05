---
id: 4408264552977
title: Palkanlaskennassa käytettävät HR-tiedot
url: https://support.nepton.com/hc/fi/articles/4408264552977-Palkanlaskennassa-k%C3%A4ytett%C3%A4v%C3%A4t-HR-tiedot
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Nepton Palkat
section_id: 4406259955345
section_path:
- Nepton Palkat
labels: []
promoted: false
updated_at: '2025-02-20T08:00:36Z'
edited_at: '2025-02-20T08:00:36Z'
---

# Palkanlaskennassa käytettävät HR-tiedot

Nepton Palkat -palvelu käyttää henkilötietoja, jotka asetetaan "Työsuhde"-osiossa. Syöttämällä ja ylläpitämällä näitä tietoja, Nepton Palkat-toimii ja palkat saadaan maksettua. Muokkaukset työsuhdetietoihin ovat heti käytettävissä palkanlaskennassa, mukaan lukien voimassaolopäivään liittyvät muutokset (esim. tulevaisuudessa tapahtuvat muutokset).
Profiilitietoja täydennettäessä tulee huomioida Voimassa alkaen -tieto. Jos esim. tuodaan sisäänluettavalla Excelillä tietoja eikä Voimassa alkaen -tietoa määritellä, tiedot ovat tuontipäivästä alkaen voimassa ja täten takautuvasti ei voida palkkatietoja tarkastella Palkkojen puolella. Testaamisen aikana on tarpeellista ajaa menneitä tapahtumia Palkkoihin.
## Maksuryhmät
[Maksuryhmät](<https://support.nepton.com/hc/fi/articles/4406602996625>) ovat vaadittu tieto, jotta Nepton Palkat toimii oikein. Niitä käytetään palkkalistojen automaattiseen luomiseen palkanlaskennassa.
Määrittele Neptonin Työsuhde-osiossa:
  * Maksuryhmät - Erilliset ryhmät vähintään kuukausi- ja tuntipalkkaisille työntekijöille. Tarvittaessa voit ryhmitellä työntekijöitä vielä tarkemmin.  

    * Nimi - Helppoa tunnistamista varten
    * Koodi - Palkanlaskennan asiantuntijan antama. Se yhdistää maksuryhmän palkanlaskentaan ("Toistuvan palkkalaskelman ID" palkanlaskentajärjestelmässä)
    * Ryhmää kuvaava lisätieto (vapaaehtoinen)
  * Maksuryhmän jaksot - Kukin jakso edustaa maksua työntekijöille 
    * Ajanjakso, jolta maksu koskee
    * Päivä, jolloin tämän maksuryhmän työntekijät saavat palkan
    * Päivä, jolloin tämä maksu huomioidaan kirjanpidossa (vapaaehtoinen)
    * Aineistopäivä: Palkanlaskentaprosessin helpottamiseksi olemme lisänneet päivämääräkentän, joka kuvaa, milloin tapahtumat ja hyväksynnät tulisi olla valmiina, jotta palkanlaskennan asiantuntijat voivat viimeistellä palkanlaskennan. Päivämäärä on suuntaa-antava eikä vaikuta teknisesti palkanmaksuun.
    * Huomio: Ylimääräiset kertaluonteiset maksut hoidetaan palkanlaskennan asiantuntijoiden toimesta palkanlaskentajärjestelmässä, eikä niitä tule lisätä maksuryhmän jaksoihin.
  * Työntekijöiden maksuryhmäjäsenyydet 
    * Nämä voidaan lisätä manuaalisesti henkilötietoihin kaikille työntekijöille tai henkilötietojen tuonnin ominaisuuksia käyttäen. Tiedot voidaan tuoda manuaalisesti Excelillä tai ajastetun integraation kautta.


## Henkilötiedot
Seuraavia tietoja käytetään palkanlaskennassa. Nämä tiedot on täytettävä Neptonissa, jotta palkkalaskenta toimii oikein. On suositeltavaa käyttää kaikkia seuraavia kenttiä, vaikka niitä ei olisi merkattu pakollisiksi.
Neptonin palkanlaskennassa Neptonia pidetään pääjärjestelmänä (master data). Nämä kentät tulee aina pitää ajan tasalla Neptonin Työsuhde-osiossa manuaalisesti tai integraatiolla toisesta HR-järjestelmästä tuomalla.
Vaikka on tärkeää pitää kaikki henkilötiedot aina ajan tasalla, Nepton Palkat -palvelun käyttöönotossa on erityisen tärkeää varmistaa, että työsuhteen päivämäärät, työntekijän numerot ja maksuryhmät on asetettu oikein kaikille työntekijöille, **mukaan lukien entiset ja poistetut työntekijät**. Näitä tietoja käytetään määrittämään, ketkä työntekijät sisällytetään palkanlaskentaan.
Työntekijät, joiden työntekijänumero on 0 (nolla), eivät synkronoidu palkanlaskentaan. Tämä työntekijänumero on varattu erikoistapauksille, kuten automaatiota tai hallintoa varten käytetyille tileille, joita ei tarvitse ottaa huomioon palkanlaskennassa. Se ei ole tarkoitettu poistetuille tai entisille työntekijöille. Lue lisää henkilöiden poistamisesta [täältä](<https://support.nepton.com/hc/fi/articles/360002424617>).
**Tietoryhmä** | **Kentän nimi** | **Pakollinen** | **Lisätietoa**  
---|---|---|---  
Perustiedot | Etunimi | x |   
Sukunimi | x |   
Sähköposti | x |   
Puhelinnumero |  |   
Katuosoite |  |   
Postinumero |  |   
Postitoimipaikka |  |   
IBAN | x | Käytetään palkanmaksuun.  
Henkilotunnus | x |   
Työsuhde | Ammattinimike |  | Näytetään palkkalaskelmalla.  
Ammattiluokitus | x | Käytetään vakuutuksen määrittelyyn palkanlaskennassa.  
Sopimuksen tyyppi | x |  Kuukausipalkkainen työntekijä TAI Tuntipalkkainen työntekijä Käytetään automaattiseen palkanlaskentaan.  
Työsuhteen alkupäivä | x |   
Työsuhteen päättymispäivä |  | Jos asetettu, työsuhde päättyy palkanmaksussa.  
Työaika prosentteina |  |  Käytetään automaattiseen palkanlaskentaan.**Huom!** Jos henkilölle on toteutettu osa-aikaisuus Oletettujen työaikojen avulla, työaika prosentteina -kenttää ei täytetä.  
Kuukausipalkka | x | Sekä kuukausi- että tuntipalkka tarvitaan kuukausipalkkaisilla henkilöillä. Tuntipalkkaa käytetään kuukausipalkkaisilla, kun tuntivähennyksiä ja korjauksia tehdään.  
Tuntipalkka | x | Pakollinen tuntipalkkaisissa sopimuksissa.  
Organisaatio | Maksuryhmä | x | Määrittää, mihin maksuryhmään henkilö kuuluu. Käytetään palkkalistojen ja maksukausien luomiseen.  
| Oletusprojekti |  | Jos projektikohdennus on käytössä.  
## Ongelmien ratkaiseminen
Jos henkilön HR-tiedoista puuttuu palkanlaskennan vaatima tieto, siitä ilmoitetaan varoituksena [palvelulokissa](<https://support.nepton.com/hc/fi/articles/360002575478>). Täydellinen lista vaadituista kentistä löytyy yllä olevasta taulukosta.
Jos joillekin kentille raportoidaan puuttuvia, virheellisiä tai hylättyjä arvoja, kaikki henkilön pätevät tiedot ovat silti käytettävissä palkanlaskennassa.
Jos palveluloki raportoi virheen koskien oikeuksia, kuten "Ei oikeutta" tai "Kirjoitusoikeus evätty", se tarkoittaa, että palvelua ei ole määritetty oikein. Ota yhteyttä asiakaspalveluun ja anna heille päivämäärä ja kellonaika, jona ongelma näkyy lokissa.
