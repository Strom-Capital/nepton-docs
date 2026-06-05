---
id: 360015933397
title: Henkilötuonnin kentät
url: https://support.nepton.com/hc/fi/articles/360015933397-Henkil%C3%B6tuonnin-kent%C3%A4t
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötuonnin kentät
section_id: 9000763181981
section_path:
- Liittymät
- Henkilötiedot
- Henkilötuonnin kentät
labels:
- kustannusryhmä
promoted: false
updated_at: '2026-06-03T13:09:11Z'
edited_at: '2026-06-03T13:09:10Z'
---

# Henkilötuonnin kentät

Henkilötuonneissa on käytössä olevat kentät riippuvat tuotavien henkilötietojen lähdejärjestelmästä, sekä käytettävästä aineistomuodosta. Alla taulukossa on esitetty [henkilötuonnin](<https://support.nepton.com/hc/fi/articles/360003762577>) tukemat kiinteät kentät. Yleisen henkilötuonnin lisäksi osa lähdejärjestelmäkohtaisista aineistomuodoista tukevat näitä kenttiä, mutta lähdejärjestelmäkohtaiset ohjeet mainitsevat tästä erikseen.
Alempaa löytyvässä kenttätaulukossa kenttä on kentän nimi/otsikko, jolla kenttä tunnistetaan tuonnissa. Kentistä voi käyttää myös englanninkielisiä nimiä, jotka saat näkyviin vaihtamalla tämän ohjesivuston kieleksi englannin. Yleinen henkilötuonti tukee myös asiakaskohtaisia lisätietokenttiä. Näiden kenttien niminä/otsikoina tuonnissa toimii kentän "Työsopimuksen tunniste". Ohjeet sen asettamiseen löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002430918>).
**NOLLA** -avainsanalla voidaan varmistaa henkilötiedon tyhjentäminen sitä tukevissa kentissä. Osassa kentistä (erityisesti tapauksissa, joissa samassa kentässä voidaan tuoda useampia arvoja kerrallaan) NOLLA-avainsanalla on tavallisesta poikkeava merkitys, joka on kuvattu tarkemmin kuvauksessa ja/tai [Henkilöiden tuonti](<https://support.nepton.com/hc/fi/articles/360003762577>) -sivulla.
## Pakolliset kentät
### Lisäys
  * Etunimi
  * Sukunimi


### Päivitys
  * Nepton-tunniste, ulkoinen tunniste 1, käyttäjätunnus tai henkilönumero (henkilön tunnistamista varten)
    * Kun Nepton-tunniste tai ulkoinen tunniste 1 on aineistossa, niitä käytetään henkilön tunnistamiseen, joka mahdollistaa käyttäjätunnuksen tai henkilönumeron vaihtamisen.


Kenttä | XML kenttä | Kuvaus | Tukee voimassaoloja | Tukee NOLLA-avainsanaa  
---|---|---|---|---  
Nepton-tunniste | Nepton_Id |  Neptonin yksilöllinen henkilötunniste, jonka Nepton luo automaattisesti jokaiselle henkilölle. Tämä arvo näkyy henkilölomakkeella. Voit yhdistää tuotavat tiedot Neptonissa olemassa olevaan henkilöön tämän kentän avulla. Tällä kentällä ei voi muuttaa olemassa olevan henkilön Nepton-tunnistetta. | Ei | Ei  
Ulkoinen tunniste 1 | Ulkoinen_tunniste_1 | Tunniste jota käytetään henkilön tunnistamiseksi tuontitiedostossa. Tunnisteena käytetään usein lähdejärjestelmän omaa tunnistetta henkilölle. Mikäli tunniste on Neptonissa, rivi päivittää tämän henkilön tietoja. | Kyllä | Kyllä  
Henkilönumero | Employee_number | Työntekijän henkilönumero. Käytetään henkilön tunnistamiseksi tuontitiedostossa, jos Nepton-tunnistetta tai käyttäjätunnusta ei tuoda: Mikäli henkilönumero on Neptonissa niin rivi päivittää tämän henkilön tietoja. | Kyllä | Kyllä  
Käyttäjätunnus | Username | Kirjautumistunnus, jota käytetään kirjautumissivulla henkilön tunnistamiseen. Voidaan myös hyödyntää kertakirjautumisessa henkilön tunnistamiseksi. Jos käyttäjätunnuskenttä on annettu tuonnissa ilman Nepton-tunniste-kenttää, sillä tunnistetaan olemassaoleva henkilö Neptonissa. Kentän käyttö aineistossa mahdollistaa myös henkilönumeron muuttamisen.  
Käyttäjätunnusta ei voida muuttaa henkilötuonnissa, vaan muutos pitää tehdä Neptonissa henkilön henkilötietosivulla. | Kyllä | Ei  
Voimassa alkaen | Valid_from_date | Päivämäärä, josta alkaen siirrettävä tieto on voimassa. Katso [kentän käytön ohje](<https://support.nepton.com/hc/fi/articles/360015754117>). | Ei | Ei  
Etunimi | First_name | Henkilön etunimi. [Pakollinen](<https://support.nepton.com/hc/fi/articles/360003762577>). | Kyllä | Ei  
Sukunimi | Last_name | Henkilön sukunimi. [Pakollinen.](<https://support.nepton.com/hc/fi/articles/360003762577>) | Kyllä | Ei  
Käyttäjätili käytössä | User_account_enabled | Onko henkilöllä käyttöoikeus palveluun. Oletus kyllä. (tukee muotoja 1,0, Y, N, Kyllä, Ei, Yes, No). Voidaan käyttää isoja tai pieniä kirjaimia. '0', 'N', 'Ei' tai 'No' poistaa käyttäjätunnuksen. | Ei | Ei  
Henkilötunnus | Personal_identity_code | Henkilötunnus | Kyllä | Kyllä  
Sähköposti | Email | Sähköpostiosoite | Kyllä | Kyllä  
Verkkosivu | Web_page | Henkilön kotisivu (jos alihankkija niin esimerkiksi toimittajan kotisivu tms.) | Kyllä | Kyllä  
Katuosoite | Street_address | Katuosoite | Kyllä | Kyllä  
Postinumero | Postcode | Postinumero | Kyllä | Kyllä  
Postitoimipaikka | City | Kaupunki | Kyllä | Kyllä  
Puhelinnumero | Phone_number | Puhelinnumero | Kyllä | Kyllä  
IBAN | IBAN | IBAN tilinumero | Kyllä | Kyllä  
BIC | BIC | IBAN tilinumeron BIC - tunniste | Kyllä | Kyllä  
RFID-tunniste | RFID_tag_identifier | Piippumerkillä (|) eroteltu lista henkilön käytössä olevista RFID-tunnisteista. Käytetään kirjauspäätteelle tunnistautuessa. | Kyllä | Kyllä  
PIN-koodi | Pin_code | PIN-Koodi. Käytetään kirjauspäätteelle tunnistautuessa. | Kyllä | Kyllä  
Salasana | Password | Henkilön salasana tekstimuodossa. Suosittelemme, että salasanaa ei tuoda palveluun, jolloin salasana muodostuu automaattisesti. Jokainen käyttäjä saa asetettua salasanansa palvelun sisäänkirjautumissivun 'unohdin salasanani' - toiminnolla. | Kyllä | Ei  
Rooli | Role |  Henkilön rooli. Tukee seuraavia arvoja: · Työntekijä · Esimies · Yksikön johtaja · Palkkahallinto · Henkilöstöhallinto · Ylläpitäjä Jos tuotava arvo ei täsmää näihin, asetetaan rooliksi uudelle henkilölle "Työntekijä"; olemassa olevan henkilön roolia ei muuteta. | Kyllä | Ei  
Työajan roolit | Worktime_roles |  Työajan rooli. Kirjoita roolin koko nimi, esim. 'Omien sekä alaisten tietojen muokkausoikeus'.  
Jos käytät useita rooleja, erota jokainen piippumerkillä (|). Annetut arvot korvaavat olemassaolevat työajan roolit.  
NOLLA-avainsanalla voidaan varmistaa kaikkien olemassaolevien työajan roolien poistaminen, vaikka IgnoreEmptyValues-asetus olisi päällä (esim. tuonti web service-rajapinnan kautta). | Ei | Kyllä  
Ammattinimike | Job_title | Työskentelynimike | Kyllä | Kyllä  
Työskentelyalue | Work_area | Työskentelyalue | Kyllä | Kyllä  
Vuorokautinen työaika | Daily_work_obligation | Vuorokautinen työaika | Kyllä | Kyllä  
Viikoittaiset tunnit MIN | Weekly_hours_MIN | Henkilön viikoittaisen työajan minimiarvo kokonais- tai desimaalilukuna. Esitetään työvuorosuunnittelussa suunnittelijalle. | Kyllä | Kyllä  
Viikoittaiset tunnit MAX | Weekly_hours_MAX | Henkilön viikoittaisen työajan maksimiarvo kokonais- tai desimaalilukuna. Esitetään työvuorosuunnittelussa suunnittelijalle. | Kyllä | Kyllä  
Työsuhteen alkupäivä | Employment_start_date | Annetaan muodossa DD.MM.YYYY. [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9003095125149>). | Ei | Kyllä  
Työsuhteen päättymispäivä | Employment_end_date | Annetaan muodossa DD.MM.YYYY. Jos työntekijän sopimus on toistaiseksi voimassaoleva tulee arvo siirtää tyhjänä. [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9003095125149>). | Ei | Kyllä  
Koeajan päättymispäivä | Trial_period_end_date | Koeajan päättymispäivämäärä muodossa DD.MM.YYYY | Kyllä | Kyllä  
Yksikkö | Units |  Yksikkö. Arvona voi käyttää joko yksikön nimeä tai koodia. Jos henkilö kuuluu useaan yksikköön, erota jokainen piippumerkillä (|). Annetut arvot korvaavat olemassaolevat henkilön yksiköt.  
NOLLA-avainsanalla voidaan varmistaa henkilön poistaminen kaikista yksiköistä, vaikka IgnoreEmptyValues-asetus olisi päällä (esim. tuonti web service-rajapinnan kautta). Kenttä on kirjainkoosta riippumaton. [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9001251146653>). **Huomioi:** Yksikkö pitää luoda ensin Neptoniin, jotta se voidaan tuoda oikein. | Ei | Kyllä  
Työnantaja | Employer | Henkilön työnantaja | Kyllä | Kyllä  
Oletusprojekti | Default_project | Henkilön oletusprojekti | Ei | Kyllä  
Vuororyhmä | Work_schedule_group | Henkilön vuororyhmän koodi | Kyllä | Kyllä  
Lomaryhmä | Holiday_schedule_group | Henkilön lomaryhmän koodi. Huomaa, että mikäli henkilö kuuluu sekä vuoro- että lomaryhmään ja ryhmien aikataulut menevät päällekkäin, lomaryhmä yliajaa vuororyhmän, eli kalenterinäkymissä näytetään kyseisen henkilön osalta vain lomaryhmä. | Kyllä | Kyllä  
Oletuskustannuspaikka | Default_cost_group  | Henkilön oletuskustannuspaikka | Kyllä | Kyllä  
Ensisijainen esimies | Primary_supervisor |  Ensisijaisen esimiehen henkilönumero. Tyhjä arvo tai NOLLA-avainsana tyhjentää ensisijaisen esimiehen (Alaiselle tulee olla määriteltynä vähintään yksi ensisijainen esimies, jotta ilmoitukset tapahtumapyynnöistä yms. lähetetään kenellekään). [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9002553468829>). **Huomioi:** Tällä hetkellä ensisijainen esihenkilö voidaan tuoda vain esihenkilön henkilönumerolla | Ei | Kyllä  
Toissijaiset esimiehet | Secondary_supervisors |  Piippumerkillä (|) eroteltu lista toissijaisten esimiesten henkilönumeroista. Jos arvojen joukossa on NOLLA-avainsana, luetellut esimiehet korvaavat kaikki henkilölle aiemmin luetellut toissijaiset esimiehet. [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9002553468829>). **Huomioi:** Tällä hetkellä toissijainen esihenkilö voidaan tuoda vain esihenkilön henkilönumerolla | Ei | Kyllä  
Integration id-kentät Aastra  
DL Software  
Elisa Ring  
Emce  
Fivaldi  
Heeros  
Hogia  
IFS  
Kieku  
Lessor-5  
Liksa  
Mepco  
Oscar  
Personec F  
Personec W  
ProCountor  
Scala  
Sedab  
Sonet  
Tikon  
Visma |  Integration id-kentät: Aastra  
DL_Software  
Elisa_Ring  
Emce  
Fivaldi  
Hogia  
IFS  
Kieku  
Lessor-5  
Liksa  
Mepco  
Oscar  
Personec_F  
Personec_W  
ProCountor  
Scala  
Sedab  
Sonet  
Tikon  
Visma |  Henkilön ulkoisen järjestelmän tunniste. Palvelussa on useita ulkoisen järjestelmän tunnisteita ja sarakkeen nimenä tulee käyttää otsikossa järjestelmän nimeä. Esimerkiksi 'Mepco'. Arvona siirretään merkkijono. | Kyllä | Kyllä  
Saldo | Balance | Asettaa saldon arvon minuuteissa kuluvalle päivälle. Kenttään syötetään kokonaisluku. | Ei | Ei  
Hallinnon lisätieto | Additional_administrative_information | Henkilön lisätiedot. Vapaamuotoinen tekstikenttä. | Kyllä | Kyllä  
Lähiomainen | Next_of_kin | Lähiomaisen nimi. Vapaamuotoinen tekstikenttä. | Kyllä | Kyllä  
Lähiomaisen puhelinnumero | Next_of_kin_phone_number | Lähiomaisen puhelinnumero (puhelinnumeromuodossa tai tyhjä) | Kyllä | Kyllä  
Raporteilla näkyvä lisätieto | Additional_information_for_reports | Raportoinnin lisätieto. Kentän sisältö esitetään useilla palvelun raporteilla omana sarakkeenaan. | Kyllä | Kyllä  
Työsuhteen päättymissyy | Reason_for_ending_employment | Työsopimuksen päättymisen syy. Vapaamuotoinen tekstikenttä. | Kyllä | Kyllä  
Kuukausipalkka | Monthly_salary | Henkilön kuukausipalkka (numeerinen, voi olla myös desimaaleja, mutta ei voi alkaa nollalla. Käytä pilkkua ',' tai pistettä '.' desimaalierottimena, esim. 2600, 3733.33 tai 4595,50). | Kyllä | Kyllä  
Tuntipalkka | Hourly_wage | Henkilön tuntipalkka (numeerinen, voi olla myös desimaaleja, mutta ei voi alkaa nollalla. Käytä pilkkua ',' tai pistettä '.' desimaalierottimena, esim. 20, 25,67 tai 37.50) | Kyllä | Kyllä  
Veronumero | Tax_number | Henkilön suomalainen veronumero. Kentän tulee olla 12 merkkiä pitkä numero tai tyhjä. | Kyllä | Kyllä  
Henkilöryhmä | Person_group | Henkilön henkilöryhmän koodi. Vaihtoehtoisesti voidaan osana henkilötuontia muodostaa organisaatiorakenne kentillä 'Henkilöryhmän nimipolku hierarkiassa' ja 'Henkilöryhmän koodipolku hierarkiassa'. [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9000335221661>). | Ei | Kyllä  
Henkilöryhmän nimipolku hierarkiassa | Person_group_name_path_in_hierarchy |  Jos arvo tuodaan, niin tulee myös tuoda arvo kentälle 'Henkilöryhmän koodipolku hierarkiassa'. Näillä kentillä muodostetaan henkilöryhmät ja niiden hierarkia automaattisesti. Arvona tuodaan koko henkilöryhmän nimihierarkia '|' - merkillä erotettuna. Mikäli arvona tuodaan esimerkiksi 'Toimisto|Myyjät' niin palveluun muodostuu henkilöryhmä 'Toimisto', jonka alaryhmäksi perustetaan 'Myyjät'. Tuotava henkilö asetetaan ryhmään 'Myyjät' | Ei | Ei  
Henkilöryhmän koodipolku hierarkiassa | Person_group_code_path_in_hierarchy |  Jos arvo tuodaan niin tulee myös tuoda arvo kentälle 'Henkilöryhmän nimipolku hierarkiassa'. Näillä kentillä muodostetaan henkilöryhmät ja niiden hierarkia automaattisesti. Arvona tuodaan koko henkilöryhmän koodihierarkia piippumerkillä (|) erotettuna. Mikäli arvona tuodaan esimerkiksi '10|20' niin palveluun muodostuu edellisen rivin esimerkkiä jatkaen 'Toimisto' - ryhmälle koodi '10 ja 'Myyjät' - ryhmälle koodi '20'. | Ei | Kyllä  
Työajan asetusryhmä | Worktime_setting_group |  Henkilön työajan asetusryhmän koodi.  Kun syötät NOLLA-avainsanan tai ei mitään (ei tekstiä), henkilö poistetaan kaikista asetusryhmistä kuluvan päivän alusta ilman päättymispäivää Kenttä on kirjainkoosta riippumaton. | Kyllä | Kyllä  
Työaika prosentteina | Work_time_percentage |  Henkilön työaikaprosentti, jota käytetään työpäivän ja työviikon pituuden laskemisessa. Jos prosenttiluku muuttuu, uutta prosenttilukua sovelletaan kuluvasta päivästä alkaen. Arvona siirretään desimaalimuoto esimerkiksi 80,00. Kenttä on kirjainkoosta riippumaton. | Kyllä | Ei  
Palvelun käyttökieli | Service_usage_language |  Kieli, jolla henkilö käyttää palvelua. Tuotavana arvona käytetään englanninkielistä kielen nimeä. Tuetut arvot ovat: "Finnish" (suomi), "English" (englanti), "Swedish" (ruotsi), "Danish" (tanska), "Norwegian" (norja), "Polish" (puola) ja "Estonian" (viro). Jos palvelun käyttökieltä ei ole annettu, käytetään palvelulle asetettua oletuskieltä, joka on oletuksena suomi. Jos asiakkuudelle halutaan vaihtaa toinen oletuskieli, tämän muuttamista voidaan pyytää Neptonin asiakaspalvelusta. | Kyllä | Ei  
Lyhytaikainen laina sallittu | Short_term_loan_permit | Palkkaennakko sallittu | Kyllä | Ei  
Microsoft AX -tuntihinta | Microsoft_AX_hourly_cost | rahamäärä kahdella desimaalilla | Kyllä | Kyllä  
Visma-kustannuspaikka | Visma_cost_centre | Visma-kustannuspaikka | Kyllä | Ei  
Maksuryhmä | Payment_group |  Henkilön jäsenyys maksuryhmässä. Maksuryhmän asettamisen perusteella henkilön palkanmaksu ohjataan maksuryhmän maksukausien perusteella. Arvo voi olla joko maksuryhmän koodi, nimi tai tunniste. Kenttä on kirjainkoosta riippumaton. | Kyllä | Ei  
Ammattiluokitus | Classification_of_occupations | Tämä kenttä määrittelee [Tulorekisterin TK10-ammattiluokituksen](<https://www.stat.fi/fi/luokitukset/ammatti/ammatti_17_20210101/>) koodin henkilön ammatille. | Kyllä | Kyllä  
Sopimuksen tyyppi | Contract_type |  Tämä kenttä on pakollinen Nepton Palkat -palvelun ollessa käytössä. Sisäänluettavalla Excelillä tätä tietoa henkilöille päivitettäessä, arvo on  monthlysalary tai hourlysalary | Ei | Ei  
## 
## Yksilölliset tunnistekentät
### Nepton-tunniste
Neptonin yksilöllinen tunniste, jonka Nepton luo automaattisesti kaikille käyttäjille ja se näytetään käyttäjän tiedoissa. Tämän kentän arvoa ei voida käyttää uudelleen toiselle käyttäjälle (vaikka käyttäjä olisi poistettu) ja se on aina yksilöllinen.
### Ulkoinen tunniste 1
Ulkoinen tunniste 1 on yksilöllinen henkilötunniste. Jos käyttäjällä A on Ulkoinen tunniste 1 "ID-123" ja haluat tuon tunnisteen käyttäjälle B, se tulee ensin poistaa käyttäjältä A.
### Henkilönumero
Henkilönumero on yksilöllinen henkilötunniste. Jos käyttäjällä A on henkilönumero 1234 ja haluat tuon numeron käyttäjälle B, se tulee ensin poistaa käyttäjältä A.
### Käyttäjätunnus
Käyttäjätunnus on yksilöllinen henkilötunniste. Jos käyttäjällä A on käyttäjätunnus Testi Käyttäjä ja haluat tuon käyttäjätunnus käyttäjälle B, se tulee ensin poistaa käyttäjältä A.
## Oletusarvot
Mikäli henkilötuonnissa ei ole määritelty jotakin arvoa, käytetään oletusarvoa uutta käyttäjää lisättäessä. Taulukossa kuvataan oletusarvot ja se, miten oletusarvot voidaan määritellä.
Kentän nimi | Säännöt | Miten asetetaan oletusarvo(t)  
---|---|---  
Työajan roolit | Jos oletusarvot on määritelty, niitä käytetään kun luodaan **uusi käyttäjä** eikä roolia ole määritelty. Tämä tehdään koska tämä on pakollinen kenttä. |  Työajan roolien oletusarvot voidaan määritellä asetuksessa "Työajan oletusrooli  
(Oletus kun uusi henkilö luodaan)" osiossa **Työsuhde** > **Hallinta >** **Asetukset > Yleiset**  
Työajan asetusryhmä |  Kun **uusi käyttäjä** luodaan **käyttöliittymän** kautta **Työsuhde > Henkilöt > Lisää henkilö** -näkymässä, tai luodaan tuomalla uusi käyttäjä tiedostolla **Työsuhde > Henkilöt > Tuo henkilöitä** -toiminnolla ja asetusryhmätietoa ei tuoda, käyttäjälle asetetaan oletusasetusryhmä, joka on määritelty **Työsuhde >** **Hallinta >** **Asetukset > Yleiset **-näkymässä. Poikkeus tähän on tilanne, jossa asetusryhmätietona tuodaan **RESET** -avainsana, tällöin kyseiselle käyttäjälle ei aseteta asetusryhmä-tietoa. Kun käyttäjä luodaan **ajastetun tehtävän** kautta ja asetusryhmätietoa ei ole määritelty tuotavassa tiedostossa, käyttäjälle ei aseteta asetusryhmä-tietoa.  
Eli asetus "Työajan oletusrooli  
(Oletus kun uusi henkilö luodaan)" ei päde tässä tilanteessa. |  Työajan asetusryhmän oletusarvo voidaan määritellä asetuksessa "Työajan oletusrooli  
(Oletus kun uusi henkilö luodaan)" osiossa **Työsuhde** > **Hallinta >** **Asetukset > Yleiset**
