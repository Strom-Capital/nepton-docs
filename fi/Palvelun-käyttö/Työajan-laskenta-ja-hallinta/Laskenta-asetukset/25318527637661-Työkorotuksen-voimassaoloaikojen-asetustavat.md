---
id: 25318527637661
title: Työkorotuksen voimassaoloaikojen asetustavat
url: https://support.nepton.com/hc/fi/articles/25318527637661-Ty%C3%B6korotuksen-voimassaoloaikojen-asetustavat
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
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2025-06-06T10:04:03Z'
---

# Työkorotuksen voimassaoloaikojen asetustavat

Työkorotusten voimassaoloaikojen määrittämiseen on käytettävissä kahta eri asetustapaa. Asetustavat ovat ”Päiviin, joille työvuoro osuu” sekä ”Päivään, jolle työvuoro kuuluu”. Mikäli asetustavaksi ei ole asetettu mitään, käytetään oletuksena ”Päivään, jolle työvuoro kuuluu” -asetusta.
Tässä artikkelissa kuvataan molemmat asetustavat esimerkkien avulla. Esimerkit, joilla asetustapojen toimintaa kuvataan ovat Työkorotus: Iltalisä sekä Työkorotus: Yölisä. Ohjeistus muihin työkorotusten asetuksiin löytyvät [tästä ohjeesta.](<https://support.nepton.com/hc/fi/articles/360002560978>)
## Asetustapa: Päiviin, joille työvuoro osuu
Tämä asetustapa on ollut vakiomenettely ennen 8.3.2025 2.16.0 versiojulkaisua ja tapa on edelleen käytettävissä. Tässä asetustavassa työkorotuksen voimassaoloajat asetetaan jokaiselle viikonpäivälle (työkorotuksesta riippuen) käyttäen vähintään kahta voimassaolokenttää. Samojen aikojen asettaminen usealle päivällä vaatii toistoa ja voi olla mahdollisten poikkeusasetusten käyttöönoton kannalta haastavaa.
Tässä työkorotuksen voimassaolojen asetustavassa työvuoron osuessa kahdelle päivälle, esimerkiksi yövuorojen tilanteessa, käytetään sekä keskiviikolle että torstaille määritettyjä voimassaoloaikoja. Tämä voi aiheuttaa epäselvyyksiä työkorotuksen ansainnassa ja päiväkohtaisissa ansainnan poikkeusasetuksissa.
### Esimerkki Työkorotus: Yölisä
Työkorotuksen voimassaoloaikojen tulkitseminen useamman päivän voimassaolomäärityksistä konkretisoituu Yölisän ansainnassa. Tässä esimerkissä käydään läpi yölisän voimassaoloaikojen määritys asetustavalla Päiviin, joille työvuoro osuu.
Työkorotuksen Yölisän laskentatapa on “Päiviin, joille työvuoro osuu” ja voimassaoloajat klo 22:00 – 06:00 
![](https://support.nepton.com/hc/article_attachments/25676421847197)
Jolloin työkorotuksen Yölisä ansainta työtapahtumasta on:
![](https://support.nepton.com/hc/article_attachments/25676421848733)
Tässä esimerkkikirjauksessa maanantaina alkavasta yövuorosta ansaitaan työkorotusta Yölisä kahden eri voimassaoloaikakentän ja päivän perusteella:
  * Maanantain voimassaoloaikojen 22:00 – 24:00 perusteella
  * Tiistain voimassaoloaikojen 00:00 – 06:00 perusteella


Voimassaoloaikojen “ketjuttamisen” myötä voimassaoloaikoja voi olla haastavaa soveltaa päiväkohtaisiin poikkeusasetuksiin, sillä yksittäisiä voimassaoloaikamäärityksiä on hyvin monta viikon jokaiselle päivälle, jolloin myös poikkeusasetuksia joudutaan määrittämään usealle eri päivälle. Työkorotuksen voimassaoloaikoihin tehtäviä poikkeusasetuksia voivat olla esimerkiksi tapahtumatyyppikohtaiset poikkeukset.
### Esimerkki Työkorotus: Iltalisä
Yhdelle päivälle osuvan työkorotuksen ansainnan määritys asetustavalla "Päiviin, joille työvuoro osuu" ei aiheuta vastaavanlaista useamman päivän voimassaolotulkintaa kuin edellisessä yölisän esimerkissä.
Työkorotuksen Iltalisä laskentatapa “Päiviin, joille työvuoro osuu” ja voimassaoloajat klo 14:00 – 22:00.
![](https://support.nepton.com/hc/article_attachments/25676369485085)
Jolloin työkorotuksen Iltalisä ansainta työtapahtumasta on:
![](https://support.nepton.com/hc/article_attachments/25676369485725)
Tässä esimerkissä koko työtapahtuma osuu maanantaille, jonka myötä myös työkorotusta Iltalisä ansaitaan maanantaille määritettyjen voimassaoloaikojen perusteella.
## Asetustapa: Päiviin, joille työvuoro kuuluu
Tässä asetustavassa työkorotuksen voimassaoloajat määritetään yhdellä voimassaoloasetuksella. Työkorotuksen ansainta on täten oletuksena voimassa viikon jokaisena päivänä. Voimassaoloaikojen poikkeusasetuksia, esimerkiksi tapahtumatyyppien perusteella, voidaan edelleen määrittää tälläkin asetustavalla.
Oleellisin ero toiseen voimassaoloaikojen laskentatapaan on työkorotuksen voimassaoloaikojen hyödyntäminen sen päivän mukaisesti, [jolle työajan tulkintakin kuuluu.](<https://support.nepton.com/hc/fi/articles/360008777997>) Seuraavissa esimerkeissä käydään läpi työkorotusten Yölisä sekä Iltalisä voimassaoloaikojen määrittäminen tällä asetustavalla tilanteissa, joissa
  * Työtapahtumien näyttö on määritykseltään “Tapahtumat ja laskenta näytetään päivänä milloin vuoro loppuu”.
  * Työtapahtumien näyttö on määritykseltään “Tapahtumat ja laskenta näytetään päivänä milloin vuoro alkaa”


![](https://support.nepton.com/hc/article_attachments/25676369486493)
### Esimerkki Työkorotus: Yölisä
Työtapahtumien näyttö: “Tapahtumat ja laskenta näytetään päivänä milloin vuoro loppuu”
Työkorotuksen Yölisä laskentatapa “Päiviin, joille työvuoro kuuluu” ja voimassaoloajat klo 22:00 – 06:00 
![](https://support.nepton.com/hc/article_attachments/25676421851677)
Tällä asetustavalla työkorotuksen voimassaoloajat määritetään kiinteällä asetuksella Ansaintakausi. Tapahtumien ja laskennan näytön ollessa päivällä, milloin vuoro loppuu, voimassaoloajat tulee määrittää logiikalla **“Edellisenä päivänä” – “Nykyisenä päivänä”.**
Jolloin työkorotuksen Yölisä ansainta työtapahtumasta on:
![](https://support.nepton.com/hc/article_attachments/25676369490461)
Tässä esimerkkikirjauksessa tapahtuma ja siitä muodostuva tulkinta näytetään päivällä jolla työvuoro päättyy (maanantai). Työkorotuksen voimassaoloaikojen (ansaintakauden) ollessa 22:00 Edellisenä päivänä – 06.00 Nykyisenä päivänä, työkorotusta Yölisä muodostuu sunnuntain klo 22.00 ja maanantain 06.00 välisellä ajalla tehdystä työstä (ruokatauko huomioiden). Työtapahtumien ja työajan tulkinta ja näyttäminen kalenterissa on tällöin suoraan yhteydessä työkorotuksen Yölisä ansainnan voimassaoloaikaan. 
Työtapahtumien näyttö: “Tapahtumat ja laskenta näytetään päivänä milloin vuoro alkaa”
Työkorotuksen Yölisä laskentatapa “Päiviin, joille työvuoro kuuluu” ja voimassaoloajat klo 22:00 – 06:00 
![](https://support.nepton.com/hc/article_attachments/25676421855901)
Tällä asetustavalla työkorotuksen voimassaoloajat määritetään kiinteällä asetuksella Ansaintakausi. Tapahtumien ja laskennan näytön ollessa päivällä, milloin vuoro loppuu, voimassaoloajat tulee määrittää logiikalla “Edellisenä päivänä” – “Nykyisenä päivänä”.
Jolloin työkorotuksen Yölisä ansainta työtapahtumasta on:
![](https://support.nepton.com/hc/article_attachments/25676369493405)
Tässä esimerkkikirjauksessa tapahtuma ja siitä muodostuva tulkinta näytetään päivällä jolla työvuoro päättyy (maanantai).
Työkorotuksen voimassaoloaikojen (ansaintakauden) ollessa 22:00 Edellisenä päivänä – 06.00 Nykyisenä päivänä, työkorotusta Yölisä muodostuu sunnuntain klo 22.00 ja maanantain 06.00 välisellä ajalla tehdystä työstä (ruokatauko huomioiden). Työtapahtumien ja työajan tulkinta on tällöin suoraan yhteydessä työkorotuksen Yölisä ansainnan voimassaoloaikaan.
Työtapahtumien näyttö: “Tapahtumat ja laskenta näytetään päivänä milloin vuoro alkaa”
Työkorotuksen Yölisä laskentatapa “Päiviin, joille työvuoro kuuluu” ja voimassaoloajat klo 22:00 – 06:00.
![](https://support.nepton.com/hc/article_attachments/25676369495197)
Tällä asetustavalla työkorotuksen voimassaoloajat määritetään kiinteällä asetuksella Ansaintakausi. Tapahtumien ja laskennan näytön ollessa päivällä, milloin vuoro alkaa, voimassaoloajat tulee määrittää logiikalla **“Nykyisenä päivänä” – “Seuraavana päivänä”.**
Jolloin työkorotuksen Yölisä ansainta työtapahtumasta on:
![](https://support.nepton.com/hc/article_attachments/25676526707741)
Tässä esimerkkikirjauksessa tapahtuma ja siitä muodostuva tulkinta näytetään päivällä jolla työvuoro alkaa (sunnuntai). Työkorotuksen voimassaoloaikojen (ansaintakauden) ollessa 22:00 Nykyisenä päivänä – 06.00 seuraavana päivänä, työkorotusta Yölisä muodostuu sunnuntain klo 22.00 ja maanantain 06.00 välisellä ajalla tehdystä työstä (ruokatauko huomioiden). Työtapahtumien ja työajan tulkinta on tällöin suoraan yhteydessä työkorotuksen Yölisä ansainnan voimassaoloaikaan.
### Esimerkki Työkorotus: Iltalisä
Käytettäessä työkorotuksen voimassaoloaikojen asetustapaa “Päiviin, joille työvuoro kuuluu” palvelu pohjaa työkorotuksen ansainnan työtapahtumien näytön asetukseen (ohjelinkki), samaan tapaan kuin edellisen esimerkin Yölisä-työkorotuksen tapauksessa.
![](https://support.nepton.com/hc/article_attachments/25676526708893)
Iltalisän tapauksessa työkorotuksen ansainta on kuitenkin usein päiväkohtainen, ts. sen ansainta ei ulotu vuorokaudelta toiselle. Tällöin sekä henkilön kirjaamat työtapahtumat ja niiden tulkinta sekä työkorotuksen voimassaoloajat toteutuvat saman vuorokauden aikana.
Tässä esimerkissä käytetään Iltalisää esimerkkinä saman päivän aikana ansaittavasta työkorotuksesta ja tätä ohjetta voidaan soveltaa muihin vastaaviin työkorotuksiin.
Työkorotuksen Iltalisä laskentatapa “Päiviin, joille työvuoro kuuluu” ja voimassaoloajat klo 14:00 – 22:00.
![](https://support.nepton.com/hc/article_attachments/25676541648157)
Tällä asetustavalla työkorotuksen voimassaoloajat määritetään kiinteällä asetuksella Ansaintakausi. Riippumatta siitä, mikä työtapahtumien näytön asetus on, voimassaoloajat ovat voimassa nykyisenä päivänä (linkki näytön asetuksiin).
Jolloin työkorotuksen Iltalisä ansainta työtapahtumasta on:
![](https://support.nepton.com/hc/article_attachments/25676541649565)
Tässä esimerkkikirjauksessa työtapahtuma alkaa ja päättyy saman vuorokauden aikana ja työkorotus Iltalisää muodostuu sille määritettyjen voimassaoloaikojen mukaisesti klo 14.00 – 22.00 väliseltä ajalta (30min ruokatauko huomioiden).
## Toisen vuorokauden puolelle jatkuvan vuoron tulkinta
Asetusvaihtoehtoon "Päivään, jolle työvuoro kuuluu" liittyy myös valinnainen asetus "Ansaitse seuraavaan/edelliseen päivään kuuluvista vuoroista". Asetuksen avulla voidaan määrittää työkorotusta ansaittavaksi toiselle päivälle kuuluvan vuoron tunneilta, mikäli vuoro jatkuu vuorokauden puolelle, jossa työkorotuksen ehdot täyttyvät. Tällainen voi olla korotus juhlapyhinä, josta esimerkki alla.
Määritellään työkorotus ansaittavaksi koko vuorokaudelta ja otetaan se käyttöön juhlapyhinä. Korotukselle on annettu nimeksi "Juhlapyhäkorotus".
![](https://support.nepton.com/hc/article_attachments/27940371888797)
![](https://support.nepton.com/hc/article_attachments/25393917552797)
Kun torstaille sijoittuva vuoro jatkuu perjantain itsenäisyyspäivän puolelle, ansaitaan juhlapyhäkorotusta 2 tuntia aikaväliltä 00:00 - 02:00.
![](https://support.nepton.com/hc/article_attachments/25393975738397)
Mikäli asetus "Ansaitse seuraavaan/edelliseen päivään kuuluvista vuoroista" ei ole käytössä, ei juhlapyhäkorotusta muodostu, sillä asetukset tulkitaan täysin torstain mukaan. 
![](https://support.nepton.com/hc/article_attachments/25393976997021)
Molemmissa tapauksissa vuoro tulkitaan kuuluvaksi torstaille, koska se on alkanut torstaina. Tämä on tapahtumien näyttämisen oletusasetus.
![](https://support.nepton.com/hc/article_attachments/25393982927261)
## Työkorotuksen voimassaolon määrittäminen vain tietyille päiville
Laskentatavalla “Päiviin, joille työvuoro kuuluu” työkorotuksen voimassaolo (ansaintakausi) määrittää työkorotuksen voimaan viikon jokaiselle päivälle. Mikäli työkorotusta ansaitaan esimerkiksi ainoastaan välillä maanantai – perjantai, määritetään voimassaolotoiminnon kautta työkorotuksen ”Käytössä” -asetukseen [poikkeusasetus](<https://support.nepton.com/hc/fi/articles/360002560677>), jolla määritellään, ettei työkorotus ole käytössä lauantaina ja sunnuntaina.
![](https://support.nepton.com/hc/article_attachments/25676677384605)
Vastaavanlainen mutta käänteinen tilanne esiintyy myös esimerkiksi työkorotuksessa Sunnuntailisä, jonka tulee olla voimassa ainoastaan sunnuntaisin ja esimerkiksi arkipyhinä. Myös tällöin työkorotuksen “Käytössä”- asetukseen määritetään poikkeusasetus, että se on voimassa vain sunnuntaisin ja arkipyhinä.
![](https://support.nepton.com/hc/article_attachments/25676892731933)
