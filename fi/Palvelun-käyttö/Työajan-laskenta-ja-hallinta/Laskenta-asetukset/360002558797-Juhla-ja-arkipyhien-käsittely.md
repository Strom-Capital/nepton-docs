---
id: 360002558797
title: Juhla- ja arkipyhien käsittely
url: https://support.nepton.com/hc/fi/articles/360002558797-Juhla-ja-arkipyhien-k%C3%A4sittely
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- NEPTONNEEDSREVIEW
- pyhäkalenteri
- arkipyhä
- juhlapyhä
- Arkipyhänä tehdyn työn ja arkipyhäviikkojen käsittely
- Arkipyhäviikko
- juhlapyhäasetukset
- lyhennetty työpäivä
- Aattolisä
- arkivapaa
- juhannus
- arkipyhävapaa
- pääsiäissunnuntai
- aattotyö
- pyhäpäiväkoodi
- pyhäpäiväkoodit
- juhlapyhäkorvaus
promoted: false
updated_at: '2026-05-21T09:29:48Z'
edited_at: '2026-05-21T09:29:48Z'
---

# Juhla- ja arkipyhien käsittely

Palvelussa voidaan määrittää asetukset juhlapyhäkohtaisesti. Asetuksissa voidaan määrittää, näytetäänkö juhlapyhä kalenterissa ja onko sillä laskennallisia vaikutuksia työaikaan tai korvauksiin.
## Asetusten määrittely
Asetukset voidaan määrittää Työaika-osiossa joko Asetusryhmät- tai Työyhteisö-tasolle polkua **Työaika > Työyhteisön/Asetusryhmän asetukset > Työtunnit > Juhlapyhät** pitkin. 
![](https://support.nepton.com/hc/article_attachments/26466582767645)
### Yleisasetukset
Ensimmäisissä asetuksissa määritellään, miten juhlapyhät vaikuttavat työaikaan.
![](https://support.nepton.com/hc/article_attachments/26466582772765)
Asetuksella "**Työn laskenta juhlapyhänä** " määritetään, mitä tapahtuu, jos juhlapyhäpäivälle kirjataan työtapahtumia.
Normaali työ = juhlapyhälle merkitty työ käsitellään normaalina työpäivänä. Työpäivän laskennassa käytetään päivälle asetettua työvelvoitetta. Työvelvoitteen alittava aika vähennetään saldosta, mikäli päivällä on työkirjauksia. Vuorotyössä työvuoro voi sijoittua juhlapyhälle, jolloin juhlapyhä halutaan käsitellä normaalina työpäivänä.  
Lisätyö = juhlapyhälle merkitty työ tulkitaan lisätyönä [lisätyön asetusten](<https://support.nepton.com/hc/fi/articles/360002559438>) mukaisesti  
Päivä- / viikkoylityö = juhlapyhälle merkitty työ on ensin viikkoylityötä, jonka jälkeen päiväylityötä vuorokautisen enimmäistyöajan ylityksen jälkeen   
Vrk-ylityötunnit = juhlapyhälle merkitty työ on vuorokautista ylityötä
Työn laskennassa juhlapyhänä on syytä huomioida, että mikäli säännöllisen työajan ylittävä ohjaus on esimerkiksi "Tunti tunnista - Saldo", merkittyä työtä ei silloin tulkita automaattisesti ylityön mukaisilla prosenttikorotuksilla.
Mikäli juhlapyhänä tehty työ on tarkoitus korvata tunti tunnista, työn laskenta juhlapyhänä-asetuksen tulee olla joko "Lisätyö", "Päivä- / viikkoylityö" tai "Vrk-ylityötunnit" riippuen siitä, miten juhlapyhänä tehty työ korvattaisiin, jos työ kohdistuisi ylityönä palkkaan ja siten työntekijälle maksuun.
Asetuksella "**Juhlapyhät lyhentävät viikkoa** " voit myös määritellä lyhentääkö juhlapyhä työviikon pituutta päivittäisen velvoitteen, viikottaisen velvoitteen tai viikottaisen enimmäistyöajan mukaan. Asetuksen toiminnallisuus on kuvattu tarkemmin [täällä](<https://support.nepton.com/hc/fi/articles/360005058217>).
![](https://support.nepton.com/hc/article_attachments/26466582777117)
HUOM! Juhlapyhä lyhentää työviikkoa enintään 8 tuntia yhdeltä päivältä.
Asetus "**Näytä juhlapyhäkorvaus** " määrittää, näytetäänkö kalenterinäkymässä omalla rivillään mahdollisesti ansaittava juhlapyhäkorvaus. Korvauksen muodostumiseen vaikuttaa kohdan "Juhlapyhät: Näytä/Korvaus ansaitaan/Lyhentää työviikkoa" asetukset. Korvaus perustuu siihen, kuinka paljon juhlapyhä lyhentää työviikkoa.
![](https://support.nepton.com/hc/article_attachments/26466598413085)
### Kiinteä korvaus
Osion asetuksilla voidaan määrittää juhlapyhäkorvaukselle kiinteä korvaus. Ensimmäisellä asetuksella määritellään, onko kiinteä korvaus käytössä, ja toisella, mikä on korvauksen määrä. Kumpaankin asetukseen voidaan määrittää myös poikkeusasetuksia, mikä kiinteä korvaus ei ole ollenkaan käytössä tiettynä päivänä, tai on erisuuruinen jonain tiettynä juhlapyhänä. Korvaus määräytyy juhlapyhätaulukon "korvaus ansaitaan" asetuksen perusteella. Esimerkiksi, jos halutaan, että ansaitaan 8h juhlapyhäkorvaus jokaisesta juhlapyhästä arkipäivinä, huolimatta työvelvoitteesta, laitettaisiin asetukset seuraavasti:  
![](https://support.nepton.com/hc/article_attachments/29922346912541)
Ja lisäksi jokaisen korvauksen muodostavan juhlapyhän kohdalle "Korvaus ansaitaan: Vain arkipäivänä". 
![](https://support.nepton.com/hc/article_attachments/29922315442589)
Tällöin 8h korvaus ilmestyy jokaisena juhlapyhänä, joka osuu arkipäivälle:  
![](https://support.nepton.com/hc/article_attachments/29922346916893)
Ylläolevassa kuvassa nähdään, että 8h kiinteä korvaus muodostuu niille juhlapyhille, jotka osuvat arkipäivälle, mutta lauantaille osuvalle Tapaninpäivälle ei muodostu korvausta.
### Juhlapyhät jotka lyhentävät työviikon pituutta, lyhentävät
Voit lisäksi määritellä, miten työviikkoa lyhentävät juhlapyhät käyttäytyvät ja mitä työviikon pituuden määritystä ne lyhentävät.
![](https://support.nepton.com/hc/article_attachments/26466582790557)
Määritykset suositellaan tehtävän [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta.
**Työviikon lyhentäminen ja ylityön raja**
Jos halutaan lyhentää työviikkoa, mutta ei ylityön rajaa, tällöin arvoina pitäisi olla
  * Työviikon pituus työehtosopimuksessa = Kyllä
  * TES enimmäistyöaika viikossa = Ei


Jos halutaan lyhentää myös ylityön rajaa, tällöin arvoina pitäisi olla:
  * Työviikon pituus työehtosopimuksessa = Kyllä
  * TES enimmäistyöaika viikossa = Kyllä


Jokaiselle näistä kolmesta asetuksesta voi antaa [poikkeusasetuksia](<https://support.nepton.com/hc/fi/articles/360002560677>), jotka ovat voimassa tiettyinä päivinä.
Kolmannella asetuksella ei ole merkitystä jos "Kynnysarvo viikkoylityölle jos ansaittu ennen TES:n päivän maksimipituutta" ei ole asetettu TES asetuksista (Työtunnit > TES).
### Juhlapyhäpäivät
Osiossa on listattu palvelussa olevat päivät, jotka voidaan määrittää juhlapyhiksi. Jokaiselle juhlapyhälle on kolme erillistä asetusta; "Näytä", "Korvaus ansaitaan" ja "Lyhentää viikkoa".
![](https://support.nepton.com/hc/article_attachments/26466582792221)
**Näytä** -asetuksella määritellään, miten kyseinen päivä näkyy kalenterinäkymässä. 
![](https://support.nepton.com/hc/article_attachments/26466582792989)
Ei -määrityksellä kyseinen päivä näytetään kalenterissa kuten mikä tahansa muu päivä (valkoinen tausta)  
Tärkeänä päivänä -määrityksellä kyseinen päivä näytetään kalenterissa punaisella otsikolla korostettuna (valkoinen tausta)  
Juhlapyhänä -määrityksellä kyseinen päivä näytetään kalenterissa punaisella otsikolla sekä punaisella taustavärillä.
Kuvassa näkyy ensin normaali päivä, sitten tärkeäksi päiväksi asetettu päivä, sitten juhlapyhäksi asetettu päivä:  
![](https://support.nepton.com/hc/article_attachments/26466598418717)
**Korvaus ansaitaan** -asetus määrittää, saako kyseisestä päivästä juhlapyhäkorvauksen. Tässä asetuksessa vaihtoehdot ovat:
Ei  
Vain arkipäivinä  
Vain päivinä joilla työvelvoite  
Vain päivinä joina juhlapyhä lyhentää viikkoa  
Aina
![](https://support.nepton.com/hc/article_attachments/26466582795933)
Jotta valittujen asetusten mukaan muodostuva korvaus näytetään kalenterissa, tulee myös asetukseen "näytä juhlapyhäkorvaus" olla määriteltynä "kyllä". Korvaus perustuu siihen, kuinka paljon juhlapyhä lyhentää työviikkoa (Juhlapyhäosion toinen asetus: Juhlapyhät lyhentävät viikkoa), ellei korvaukselle olla määrätty kiinteää arvoa.
**Lyhentää viikkoa** -asetus määrittää lyheneekö viikon työvelvoite viikolla, jolle kyseinen päivä osuu. Vaihtoehdot ovat:  
Ei  
Vain arkipäivinä  
Vain päivinä joilla työvelvoite  
Aina
![](https://support.nepton.com/hc/article_attachments/26466582797725)
Muut työviikon lyhentämiseen liittyvät määritykset löytyvät taulukon yläpuolelta.
## Työviikon pituuden lyhentäminen alkuviikosta
Juhlapyhät ja vuosilomat voivat lyhentää työviikon pituutta jo viikon alussa. Tällöin esimerkiksi juhlapyhä tai vuosiloma perjantaina lyhentää työviikon pituutta maanantaina. Tämä kannattaa ottaa huomioon varsinkin osa-aikaisilla työntekijöilä.
Asetus löytyy kohdasta **Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Työtunnit > TES.**  

![mceclip1.png](https://support.nepton.com/hc/article_attachments/360004731557)
## Vuorosuunnittelun juhlapyhäasetukset
Jos käytössä on vuorosuunnittelu, voidaan juhla- ja arkipyhiä koskevat asetukset määrittää **Työsuhde-** osiossa. Vuorosuunnitteluasetukset löytyvät kohdasta **Työsuhde > Hallinta > Asetukset > Vuorosuunnittelu**. Juhlapyhälle voidaan määrittää lyhennetty pituus sekä lisätäänkö päivittäinen työvelvoite suunnitellun työvuoron lisäksi. Tarkemman kuvauksen vuorosuunnittelun juhlapyhäasetuksista ja laskennasta suunnittelunäkymässä löydät [täältä](<https://support.nepton.com/hc/fi/articles/360017908457-Laskenta-suunnittelun%C3%A4kym%C3%A4ss%C3%A4#h_01HQ3CEEJYRZKY8E6GYGBWB8DW>).
![Screenshot 2024-05-24 130537.png](https://support.nepton.com/hc/article_attachments/19084546237341)
## Juhlapyhät Neptonissa 2025 ja 2026
**Juhlapäivä** | **Päivämäärä (2025)** | **2026** | **Maa** | **Huomioita**  
---|---|---|---|---  
Belgian kansallispäivä | 21\. heinäkuuta | 21.7.2026 | Belgia | Itsenäisyyspäivä  
Helatorstai | 29\. toukokuuta | 14.5.2026 | Suomi ym. | Kristillinen juhla  
Helluntai | 8\. kesäkuuta | 24.5.2026 | Suomi ym. | 50 päivää pääsiäisestä  
Isänpäivä | 9\. marraskuuta | 8.11.2026 | Suomi | Marraskuun toinen sunnuntai  
Isänpäivä (Liettua) | 1\. kesäkuuta | 7.6.2026 | Liettua | Kesäkuun ensimmäinen sunnuntai  
Itsenäisyyden palauttamisen päivä (Liettua) | 11\. maaliskuuta | 11.3.2026 | Liettua | Vuonna 1990  
Itsenäisyyden palauttamisen päivä (Viro) | 20\. elokuuta | 20.8.2026 | Viro | Vuonna 1991  
Itsenäisyyspäivä | 6\. joulukuuta | 6.12.2026 | Suomi | Vuonna 1917  
Itsenäisyyspäivä (Viro) | 24\. helmikuuta | 24.2.2026 | Viro | Vuonna 1918  
Itsenäisyyspäivän aatto | 5\. joulukuuta | 5.12.2026 | Suomi | Ei virallinen juhlapäivä  
Itsenäisyyspäivänaatto (Viro) | 23\. helmikuuta | 23.2.2026 | Viro | Ei virallinen juhlapäivä  
Itävallan kansallispäivä | 26.10.2025 | 26.10.2026 | Itävalta |   
Johannes Kastajan päivä | 24\. kesäkuuta | 24.6.2026 | Suomi | Juhannuspäivä  
Johannes Kastajan päivän aatto | 23\. kesäkuuta | 23.6.2026 | Suomi | Juhannusaatto  
Johannes Kastajan päivän aatto (Viro) | 23\. kesäkuuta | 23.6.2026 | Viro | Jaanilaupäev  
Jouluaatto | 24\. joulukuuta | 24.12.2026 | Suomi | Ei virallinen juhlapäivä  
Joulupäivä | 25\. joulukuuta | 25.12.2026 | Suomi ym. | Kristillinen juhla  
Juhannusaatto | 20\. kesäkuuta | 19.6.2026 | Suomi | Kesäkuun kolmas perjantai  
Juhannuspäivä | 21\. kesäkuuta | 20.6.2026 | Suomi | Kesäkuun kolmas lauantai  
Kiirastorstai | 17\. huhtikuuta | 2.4.2026 | Suomi ym. | Torstai ennen pitkäperjantaita  
Kuningas Mindaugasin kruunajaisten vuosipäivä | 6\. heinäkuuta | 6.7.2026 | Liettua | Valtionpäivä  
Latvian itsenäisyyden palauttamispäivä | 4\. toukokuuta | 4.5.2026 | Latvia | Vuonna 1990  
Latvian itsenäisyyden palauttamispäivä (seuraava maanantai) | 5\. toukokuuta | 4.5.2026 | Latvia | Siirretty juhlapäivä  
Latvian tasavallan julistamispäivä | 18\. marraskuuta | 18.11.2026 | Latvia | Vuonna 1918  
Latvian tasavallan julistamispäivä (maanantai) | 17\. marraskuuta | 16.11.2026 | Latvia | Siirretty juhlapäivä  
Loppiainen | 6\. tammikuuta | 6.1.2026 | Suomi ym. | Kristillinen juhla  
Maailmansodan päättymisen muistopäivä | 11\. marraskuuta | 8.5.2026 | Eurooppa | Ensimmäisen maailmansodan päättyminen  
Marian taivaaseenottaminen | 15\. elokuuta | 15.8.2026 | Katoliset maat | Kristillinen juhla  
Norjan valtiomuotopäivä | 17\. toukokuuta | 17.5.2026 | Norja | Perustuslain päivä  
Pitkäperjantai | 18\. huhtikuuta | 3.4.2026 | Suomi ym. | Kristillinen juhla  
Pyhäinpäivä | 1\. marraskuuta | 31.10.2026 | Suomi | Kristillinen juhla  
Pyhäinpäivä (Belgia/Ranska) | 1\. marraskuuta | 1.11.2026 | Belgia/Ranska | Kristillinen juhla  
Pyhäinpäivä (Liettua) | 1\. marraskuuta | 1.11.2026 | Liettua | Kristillinen juhla  
Pyhäinpäivä (Saksa) | 1\. marraskuuta | 1.11.2026 | Saksa | Kristillinen juhla  
Pyhän ruumiin juhlapäivä | 19\. kesäkuuta | 4.6.2026 | Katoliset maat | Kristillinen juhla  
Pääsiäislauantai | 19\. huhtikuuta | 4.4.2026 | Suomi ym. | Lauantai ennen pääsiäistä  
Pääsiäismaanantai | 21\. huhtikuuta | 6.4.2026 | Suomi ym. | Kristillinen juhla  
Pääsiäissunnuntai | 20\. huhtikuuta | 5.4.2026 | Suomi ym. | Kristillinen juhla  
Ranskan kansallispäivä | 14\. heinäkuuta | 14.7.2026 | Ranska | Bastille-päivä  
Ruotsin kansallispäivä | 6\. kesäkuuta | 6.6.2026 | Ruotsi | Kansallispäivä  
Tapaninpäivä | 26\. joulukuuta | 26.12.2026 | Suomi ym. | Kristillinen juhla  
Toinen helluntaipäivä | 9\. kesäkuuta | 25.5.2026 | Ruotsi | Helluntain jälkeinen maanantai  
Uudenvuodenaatto | 31\. joulukuuta | 31.12.2026 | Suomi | Ei virallinen juhlapäivä  
Uudenvuodenpäivä | 1\. tammikuuta | 1.1.2026 | Suomi ym. | Vuoden ensimmäinen päivä  
Valtion palauttamispäivä (Liettua) | 16\. helmikuuta | 16.2.2026 | Liettua | Vuonna 1918  
Vappupäivä | 1\. toukokuuta | 1.5.2026 | Suomi ym. | Työväen juhlapäivä  
Vapunaatto | 30\. huhtikuuta | 30.4.2026 | Suomi | Ei virallinen juhlapäivä  
Voitonpäivä | 9\. toukokuuta | 9.5.2026 | Eurooppa | Toisen maailmansodan päättyminen  
Voittopäivä (Viro) | 9\. toukokuuta | 9.5.2026 | Viro | Toisen maailmansodan päättyminen  
Äitienpäivä | 11\. toukokuuta | 10.5.2026 | Suomi | Toukokuun toinen sunnuntai  
Äitienpäivä (Liettua) | 4\. toukokuuta | 3.5.2026 | Liettua | Toukokuun ensimmäinen sunnuntai
