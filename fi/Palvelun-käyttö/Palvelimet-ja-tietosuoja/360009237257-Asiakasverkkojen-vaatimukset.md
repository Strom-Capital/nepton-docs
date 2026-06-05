---
id: 360009237257
title: Asiakasverkkojen vaatimukset
url: https://support.nepton.com/hc/fi/articles/360009237257-Asiakasverkkojen-vaatimukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palvelimet ja tietosuoja
section_id: 360005870038
section_path:
- Palvelimet ja tietosuoja
labels:
- palomuuri
- palomuuriportit
- verkkomääritykset
promoted: false
updated_at: '2026-05-15T06:53:39Z'
edited_at: '2026-05-15T06:53:39Z'
---

# Asiakasverkkojen vaatimukset

Nepton palvelun käyttö edellyttää, että asiakasverkot voivat muodostaa yhteyden siihen julkisen internetin kautta. Alla on kuvattu kaikki verkkovaatimukset, joita verkkoasiantuntija voi käyttää taatakseen yhteyksien hyvän tason.
Verkkoon liitetyillä laitteilla tulee olla pääsy nimipalvelimille (Name Server).
Asiakkaat voivat määrittää palomuureihinsa ja muihin vastaaviin järjestelmiinsä joko alla mainittuja DNS osoitteita tai alla mainittuja IP osoitteita.
Tavoitteemme on säilyttää tässä dokumentissa määritetyt IP osoitteet voimassa pitkään tai jopa ikuisesti. On kuitenkin mahdollista, että osoitteet voivat muuttua tulevaisuudessa. Mikäli osoitteet joskus tulevaisuudessa muuttuvat, tulemme viestimään muutokset hyvissä ajoin ennen muutospäivää. 
## Nepton palvelut
Alla on kuvattu Nepton palvelun ja sen kaikkien osien verkkoyhteysvaatimukset.
Jotta vältetään epäyhteensopivuudet mahdollisten tulevien päivitysten ja muutosten suhteen, on kussakin käyttötapauksessa suositeltavaa sallia pääsy kaikista domaineista ja porteista, joita asiakkuutenne käyttää (tuotanto- tai testipalvelu).
### Tuotantopalvelu
Nepton palvelun viimeisin versio sisältäen kaikki ominaisuudet ja alapalvelut. Alla on kuvattu tarvitsemanne yhteysvaatimukset.
#### Työsuhde (HR), ylläpitopalvelut ja kirjauspäätteet
Kommentti | Pakollinen selaimille, kännyköille, kirjauspäätteille, API käytölle ja automaattisille rajapinnoille  
---|---  
Domain | go.nepton.com  
IP osoite | 83.150.75.175  
TCP portit | 80 ja 443  
#### Työaika ja kirjauspäätteet
Kommentti | Pakollinen selaimille, kännyköille, kirjauspäätteille, API käytölle ja automaattisille rajapinnoille  
---|---  
Domain | time.nepton.com  
IP osoite | 83.150.75.169  
TCP portit | 80 ja 443  
#### Oppimisen hallinta
Kommentti | Pakollinen selaimille, kännyköille, API käytölle ja automaattisille rajapinnoille  
---|---  
Domain | priima.nepton.com  
IP osoite | 94.237.105.7  
TCP portit | 80 ja 443  
#### Henkilöstökyselyt ja analytiikka
Kommentti | Pakollinen selaimille, kännyköille, API käytölle ja automaattisille rajapinnoille  
---|---  
Domain | kivawork.nepton.com  
IP osoite | 94.237.15.216  
TCP portit | 80 ja 443  
#### Kirjauspäätteet
Päätteet eivät tue AD tai proxy teknologioita.
Suosittelemme kirjauspäätteet kytkettävän omaan erilliseen (fyysiseen tai VLAN virtualisoinnin avulla tehtyyn) asiakasverkkoon. Tämä on paras käytänne, joka maksimaalisesti eristää kirjauspäätteet asiakkaan muista verkoista.
Mikäli erillistä verkkomääritystä ei ole tehty, kirjauspäätteet hakevat IP osoitteensa ja asiakkaan käyttämien DNS palvelimien tiedot asiakkaan DHCP palvelimelta.
Asiakkaan palomuurin on sallittava kirjauspäätteille pääsy asiakkaan käyttämiin DNS palvelimiin. Lisäksi kirjauspäätteille on sallittava pääsy ulospäin alla mainittuun Windows päivityspalveluun, NTP aikapalveluun ja TeamViewerin-palveluun.
Nepton Touch kirjauspäätteet päivittävät itsensä automaattisesti. Voit lukea tästä lisää [Kirjauspäätteen automaattiset päivitykset](<https://support.nepton.com/hc/fi/articles/7611101419037>) artikkelista.
Nepton Touch kirjauspääte käyttää tietoturvapäivityksiin Microsoftin päivityspalvelimia. Windows Update käyttää TCP portteja 80, 443 ja seuraavia palvelimia:
http://download.windowsupdate.com  
http://*.download.windowsupdate.com  
http://download.microsoft.com  
https://*.update.microsoft.com  
http://*.update.microsoft.com  
https://update.microsoft.com  
http://update.microsoft.com  
http://*.windowsupdate.com  
http://*.windowsupdate.microsoft.com  
http://windowsupdate.microsoft.com  
https://*.windowsupdate.microsoft.com  
<http://ntservicepack.microsoft.com>
<http://wustat.windows.com>
https://activation.sls.microsoft.com  
https://validation.sls.microsoft.com  
  
Nepton Touch -päätteet hakevat NTP aikakyselyt time1.mikes.fi osoitteesta, joten tämä tulee sallia palomuurista.
Nepton Flexim -päätteet hakevat NTP aikakyselyt time.mikes.fi, time1.mikes.fi sekä time2.mikes.fi osoitteista, joten nämä tulee sallia palomuurista.
Etäyhteyttä varten Nepton Touch päätteissä on TeamViewer asennettuna ongelmatilanteiden varalle. Teamviewer käyttää oletuksena TCP 5938 porttia ja varatilanteessa 443 porttia. Teamviewerin ip-osoitteiden PTR-tietueet ohjautuvat *.teamviewer.com osoitteeseen.
### Testipalvelu
Saatavissa erillisellä sopimuksella. Asiakas voi käyttää testipalvelua julkisen Internetin kautta. Testipalvelu voidaan päivittää mihin tahansa palvelun versioon, mukaan lukien lähitulevaisuudessa julkaistaviin uusiin versioihin.
#### Työsuhde (HR) ja ylläpitopalvelut
Kommentti | Pakollinen selaimille, kännyköille, kirjauspäätteille, API käytölle ja automaattisille rajapinnoille  
---|---  
Domain | publictesting-go.nepton.com  
IP osoite | 83.150.75.168  
TCP portit | 80 ja443  
#### Työaika ja kirjauspäätteet
Kommentti | Pakollinen selaimille, kännyköille, kirjauspäätteille, API käytölle ja automaattisille rajapinnoille  
---|---  
Domain | publictesting-time.nepton.com  
IP address | 83.150.75.165  
TCP ports | 80 and 443  
## SFTP tiedonsiirrot
### Nepton SFTP palvelu
Saatavissa erillisellä sopimuksella. Nepton tarjoaa asiakkaalle rajapintakäyttöön SFTP palvelun. Käyttötunnukset toimitetaan asiakkaalle käyttöönottoprosessin yhteydessä.
Kuvaus | Asiakas avaa verkkoonsa ulospäin suuntautuvan yhteyden Nepton SFTP palveluun. Tätä yhteyttä voidaan käyttää siirtämään tietoa sisään Nepton palveluun tai ulos Nepton palvelusta.  
---|---  
Asiakkaan IP osoite |  Asiakkaan tulee kertoa Neptonille käyttämänsä kiinteät IP osoitteet, joista käsin automaattinen palvelu ottaa yhteyttä Nepton SFTP palveluun. HUOM: Dynaamiset pilvi IP osoitteet eivät riitä tähän. Käytä aina kiinteitä pilvi IP osoitteita.
  * AZURE <https://docs.microsoft.com/en-us/azure/virtual-network/public-ip-addresses>

  
Nepton Domain | transfers.nepton.com  
Nepton IP osoite | 83.150.75.188  
Nepton TCP portti | 22  
### Asiakkaan SFTP palvelin
Mikäli asiakas haluaa käyttää integraatioihin omaa SFTP palvelintansa, tulee asiakkaan kertoa Neptonille SFTP palvelimensa domain, IP osoite, TCP portti ja käyttäjätunnukset. Nämä tiedot voidaan määrittää Neptonin käyttöliittymässä [tämän](<https://support.nepton.com/hc/fi/articles/360003722778-SFTP-tiedonsiirron-m%C3%A4%C3%A4ritt%C3%A4minen>) artikkelin ohjeiden mukaisesti, jolloin Nepton tulee sallimaan yhteydet asiakkaan SFTP palvelimelle.
Valtuuttaakseen Nepton pääsyn asiakkaan SFTP palvelimelle, asiakkaan tulee sallia yhteydet palomuurissaan alla mainituista Neptonin IP osoitteista omalle SFTP palvelimelleen.
#### Tarvitaan HR- ja ylläpitopalveluiden sallimiseksi
Kuvaus | Asiakas avaa verkkoonsa sisäänpäin suuntautuvan yhteyden omaan SFTP palvelimeensa. Tätä yhteyttä voidaan käyttää siirtämään tietoa sisään Nepton palveluun tai ulos Nepton palvelusta.  
---|---  
Nepton domain | go.nepton.com  
Nepton IP osoite | 83.150.75.175  
Asiakkaan TCP portti | 22  
####  Tarvitaan työaika- ja ylläpitopalveluiden sallimiseksi
Kuvaus | Asiakas avaa verkkoonsa sisäänpäin suuntautuvan yhteyden omaan SFTP palvelimeensa. Tätä yhteyttä voidaan käyttää siirtämään tietoa sisään Nepton palveluun tai ulos Nepton palvelusta.  
---|---  
Nepton domain | time.nepton.com  
Nepton IP osoite | 83.150.75.169  
Asiakkaan TCP portti | 22  
#### Tarvitaan tehostamaan integraatioiden luonteja, testauksia ja käyttöönottoja
Kuvaus | Asiakas avaa verkkoonsa sisäänpäin suuntautuvan yhteyden omaan SFTP palvelimeensa. Tätä yhteyttä voidaan käyttää mm. luomaan, testaamaan ja ottamaan käyttöön erilaisia integraatioita.  
---|---  
Nepton IP osoite | 79.134.102.194  
Asiakkaan TCP portti | 22
