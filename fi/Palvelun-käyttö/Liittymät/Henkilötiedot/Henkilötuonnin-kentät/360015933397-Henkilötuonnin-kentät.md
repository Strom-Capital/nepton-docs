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
updated_at: '2026-10-27T09:12:09Z'
edited_at: '2026-10-27T09:11:38Z'
---

# Henkilötuonnin kentät

Henkilötuonneissa on käytössä olevat kentät riippuvat tuotavien henkilötietojen lähdejärjestelmästä, sekä käytettävästä aineistomuodosta. Alla taulukossa on esitetty [henkilötuonnin](<https://support.nepton.com/hc/fi/articles/360003762577>) tukemat kiinteät kentät. Yleisen henkilötuonnin lisäksi osa lähdejärjestelmäkohtaisista aineistomuodoista tukevat näitä kenttiä, mutta lähdejärjestelmäkohtaiset ohjeet mainitsevat tästä erikseen.
Alempaa löytyvässä kenttätaulukossa kenttä on kentän nimi/otsikko, jolla kenttä tunnistetaan tuonnissa. Kentistä voi käyttää myös englanninkielisiä nimiä, jotka saat näkyviin vaihtamalla tämän ohjesivuston kieleksi englannin. Yleinen henkilötuonti tukee myös asiakaskohtaisia lisätietokenttiä. Näiden kenttien niminä/otsikoina tuonnissa toimii kentän "Työsopimuksen tunniste". Ohjeet sen asettamiseen löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002430918>).
**NOLLA** -avainsanalla voidaan varmistaa henkilötiedon tyhjentäminen sitä tukevissa kentissä. Osassa kentistä (erityisesti tapauksissa, joissa samassa kentässä voidaan tuoda useampia arvoja kerrallaan) NOLLA-avainsanalla on tavallisesta poikkeava merkitys, joka on kuvattu tarkemmin kuvauksessa ja/tai [Henkilöiden tuonti](<https://support.nepton.com/hc/fi/articles/360003762577>) -sivulla.
"Oletus"-henkilötuonnissa työsuhteen alku- ja loppupäivä tuodaan täysin aineiston arvojen mukaisesti. Jos haluat tuoda henkilötietoja oletus-tuonnin säännöin ja mahdollisuuksin, mutta haluat että tuonti voi vain pidentää työsuhdetta alla kuvatun mukaisesti, käytä tuontityyppiä "Jatka työsopimusten päiväyksiä".
## Pakolliset kentät
### Lisäys
  * Etunimi
  * Sukunimi


### Päivitys
  * Nepton-tunniste, ulkoinen tunniste 1, käyttäjätunnus tai henkilönumero (henkilön tunnistamista varten, vastaavuus tarkistetaan tässä tarkassa järjestyksessä)
    * Kun Nepton-tunniste tai ulkoinen tunniste 1 on aineistossa, niitä käytetään henkilön tunnistamiseen, joka mahdollistaa käyttäjätunnuksen tai henkilönumeron vaihtamisen.


## Kenttien rajoitukset
### Tekstikentät
  * Tekstikentien arvoilla ei ole maksimipituusrajoituksia, ellei rajoituksista ole erikseen mainittu

Kenttä | XML kenttä | Tietotyyppi | Kuvaus | Tietojen validointi | Tukee voimassaoloja | Tukee NOLLA-avainsanaa  
---|---|---|---|---|---|---  
Nepton-tunniste | Nepton_Id | Teksti |  Neptonin yksilöllinen henkilötunniste, jonka luodaan automaattisesti jokaiselle henkilölle. Tämä arvo näkyy henkilölomakkeella. Olemassa oleva henkilö voidaan tunnistaa Neptonissa tällä kentän arvolla tuonnin aikana (vastaavuus tarkistetaan ensimmäisenä tunnistettaessa henkilöä). |  Globaalisti yksilöllinen tunniste (GUID). Arvoa ei voi muuttaa olemassa olevalle henkilölle. Uudelle käyttäjälle annettu GUID, joka ei täsmää olemassa olevaan henkilöön, hylkää koko rivin. | Ei | Ei  
Ulkoinen tunniste 1 | Ulkoinen_tunniste_1 | Teksti | Tunniste jota käytetään henkilön tunnistamiseksi tuontitiedostossa (vastaavuus tarkistetaan Nepton-tunnisteen jälkeen sekä ennen käyttäjätunnusta ja henkilönumeroa). Tunnisteena käytetään usein lähdejärjestelmän omaa tunnistetta henkilölle. Mikäli tunniste on Neptonissa, rivi päivittää tämän henkilön tietoja. | Täytyy olla yksilöllinen. | Kyllä | Kyllä  
Henkilönumero | Employee_number | Teksti |  Työntekijän henkilönumero. Tätä käytetään henkilön tunnistamiseen tuontitiedostossa, jos Nepton-tunnistetta, ulkoista tunnistetta 1 tai käyttäjätunnusta ei tuoda: jos henkilö löytyy tuodulla henkilönumerolla, rivi päivittää kyseisen henkilön tiedot. Henkilönumero luodaan automaattisesti vain, jos kenttä jätetään tyhjäksi. |  Enintään 24 merkkiä; vain kirjaimia, numeroita, yhdysmerkkejä `-` ja alaviivoja `_`; ei välilyöntejä. Täytyy olla yksilöllinen. Virheellinen muoto aiheuttaa varoituksen, hylkää arvon ja tallentaa käyttäjän ilman henkilönumeroa. | Kyllä | Kyllä  
Käyttäjätunnus | Username | Teksti | Kirjautumistunnus, jota käytetään kirjautumissivulla henkilön tunnistamiseen. Voidaan myös hyödyntää kertakirjautumisessa henkilön tunnistamiseksi. Jos kenttä tuodaan ilman Nepton-tunnistetta tai ulkoista tunnistetta 1, sillä tunnistetaan olemassa oleva henkilö, mikä mahdollistaa henkilönumeron päivittämisen. |  1–100 merkkiä. Sallii kirjaimia, numeroita, yksittäisiä välilyöntejä ja erikoismerkkejä `@ ' ! # $ % & * + - / = ? ^ _ ` { | } ~ .` Alun/lopun välilyöntejä ja tuplavälilyöntejä ei sallita ja ne hylkäävät koko rivin. Olemassa olevaa käyttäjätunnusta ei voi muuttaa, ellei tuonnissa ole määritetty "Henkilön tunniste" -asetukselle / "IdentifierFieldName"-parametrille muuta arvoa kuin käyttäjätunnus – muutosyritys ohittaa koko rivin. | Kyllä | Ei  
Voimassa alkaen | Valid_from_date | Päivämäärä | Päivämäärä, josta alkaen siirrettävä tieto on voimassa. Katso [kentän käytön ohje](<https://support.nepton.com/hc/fi/articles/360015754117>). |  `DD.MM.YYYY` tai `YYYY-MM-DD` muodot käyttäen piste `.`, vinoviiva `/` tai yhdysmerkki `-` erottimia. Vuoden on oltava 1899 jälkeen. Virheellinen päivämäärä ohittaa koko rivin. | Ei | Ei  
Etunimi | First_name | Teksti | Henkilön etunimi. |  Sallii kirjaimia, numeroita, yksittäisiä välilyöntejä sekä merkkejä `' - _ .` [Pakollinen](<https://support.nepton.com/hc/fi/articles/360003762577>) uutta käyttäjää luotaessa. Tuplavälilyönnit tai muut kielletyt merkit hylkäävät koko rivin uudelle käyttäjälle, tai hylkäävät uuden arvon ja antavat varoituksen olemassa olevalle käyttäjälle. | Kyllä | Ei  
Sukunimi | Last_name | Teksti | Henkilön sukunimi. |  Samat merkki- ja validointisäännöt kuin Etunimi-kentässä. [Pakollinen.](<https://support.nepton.com/hc/fi/articles/360003762577>) uutta käyttäjää luotaessa. | Kyllä | Ei  
Käyttäjätili käytössä | User_account_enabled | Totuusarvo | Onko henkilön käyttäjätili aktiivinen. Oletus Kyllä. '0', 'N', 'No', 'false', tai 'Ei' poistaa käyttäjätunnuksen. |  Tukee syötteitä kuten 1, 0, Y, N, Yes, No, true, false, Kyllä, Ei. Ei kirjainkokoriippuvainen. Tuntematon arvo aiheuttaa varoituksen, mutta rivi tallennetaan silti. | Ei | Ei  
Henkilötunnus | Personal_identity_code | Teksti | Henkilötunnus (esim. `121234+1235`). |  Suomalaisen henkilötunnuksen muoto (6-numeroinen DDMMYY, vuosisadan tunnus `+`, `-` tai `A`, 3-numeroinen yksilönumero ja tarkistusmerkki). Virheellinen muoto aiheuttaa varoituksen, ei estä tuontia ja tallentaa arvon sellaisenaan. | Kyllä | Kyllä  
Sähköposti | Email | Teksti | Sähköpostiosoite. |  Kansainväliset merkit on sallittu, paitsi Gmail-osoitteissa. Virheellinen sähköposti aiheuttaa varoituksen, mutta rivi tallennetaan silti. | Kyllä | Kyllä  
Verkkosivu | Web_page | Teksti | Henkilön kotisivu (jos alihankkija niin esimerkiksi toimittajan kotisivu tms.). |  | Kyllä | Kyllä  
Katuosoite | Street_address | Teksti | Katuosoite. |  | Kyllä | Kyllä  
Postinumero | Postcode | Teksti | Postinumero. |  | Kyllä | Kyllä  
Postitoimipaikka | City | Teksti | Kaupunki. |  | Kyllä | Kyllä  
Puhelinnumero | Phone_number | Teksti | Puhelinnumero. |  Vain numeroita (voi alkaa `+`, voi sisältää välilyöntejä tai yhdysmerkkejä, ja on päätyttävä numeroon). Tyhjä sallittu. Virheelliset arvot aiheuttavat varoituksen, mutta rivi tallennetaan silti. | Kyllä | Kyllä  
IBAN | IBAN | Teksti | IBAN tilinumero. |  Standardi IBAN-muoto. Täytyy läpäistä standardi IBAN-tarkistussumman validointi (tyhjä sallittu). Virheellinen IBAN aiheuttaa varoituksen, mutta rivi tallennetaan silti. | Kyllä | Kyllä  
BIC | BIC | Teksti | IBAN tilinumeron BIC/SWIFT -tunniste. |  8 tai 11 merkkiä standardissa BIC-muodossa. Tyhjä sallittu. Virheellinen koodi aiheuttaa varoituksen, mutta rivi tallennetaan silti. | Kyllä | Kyllä  
RFID-tunniste | RFID_tag_identifier | Teksti | Lista henkilön käytössä olevista RFID-tunnisteista. Käytetään kirjauspäätteelle tunnistautuessa. |  Piippumerkillä `|` eroteltu lista. Täytyy olla yksilöllinen. Jos arvo on jo toisen henkilön käytössä, annetaan varoitus eikä kaksoiskappaletta määritetä (rivi tallennetaan silti). | Kyllä | Kyllä  
PIN-koodi | Pin_code | Teksti | PIN-Koodi. Käytetään kirjauspäätteelle tunnistautuessa. |  Vain numeroita. Täytyy täyttää asiakkaan vähimmäispituusvaatimuksen ja olla yksilöllinen. Kaksoiskappale tai virheellinen arvo aiheuttaa varoituksen, ja rivi tallennetaan silti. | Kyllä | Kyllä  
Salasana | Password | Teksti | Henkilön salasana. Suosittelemme, että salasanaa ei tuoda palveluun, jolloin salasana muodostuu automaattisesti. Käyttäjät voivat asetettaa salasanansa palvelun sisäänkirjautumissivun 'unohdin salasanani' - toiminnolla. |  Enintään 100 merkkiä; ei voi alkaa tai päättyä välilyöntiin. Täytyy täyttää asiakkaan salasanan vähimmäispituusvaatimus. Vaatimusten vastainen arvo aiheuttaa varoituksen, vaikka rivi tallennetaan silti. | Kyllä | Ei  
Rooli | Role | Teksti |  Henkilön rooli.
  * Työntekijä
  * Ylläpitäjä
  * Palkkahallinto
  * Esimies
  * Yksikön johtaja
  * Henkilöstöhallinto

|  Täytyy vastata olemassa olevaa roolia/käyttöoikeustasoja. Tuntematon rooli tuottaa varoituksen ja rivi tallennetaan silti (uudelle käyttäjälle asetetaan "Työntekijä"-rooli; olemassa olevan käyttäjän roolia ei muuteta). | Kyllä | Ei  
Työajan roolit | Worktime_roles | Teksti |  Työajan rooli. Kirjoita roolin koko nimi, esim. 'Omien sekä alaisten tietojen muokkausoikeus'.  
Jos käytät useita rooleja, erota jokainen piippumerkillä (|). Annetut arvot korvaavat olemassaolevat työajan roolit.  
NOLLA-avainsanalla voidaan varmistaa kaikkien olemassaolevien työajan roolien poistaminen, vaikka IgnoreEmptyValues-asetus olisi päällä (esim. tuonti web service-rajapinnan kautta). Katso myös oletusarvo-osio sivun alaosasta. | Piippumerkillä `|` eroteltu lista työajan roolien nimistä. | Ei | Kyllä  
Ammattinimike | Job_title | Teksti | Työskentelynimike. |  | Kyllä | Kyllä  
Työskentelyalue | Work_area | Teksti | Työskentelyalue. |  | Kyllä | Kyllä  
Vuorokautinen työaika | Daily_work_obligation | Desimaali | Vuorokautinen työaika. | Tukee desimaaleja pisteellä `.` tai pilkulla `,` ja negatiivisia arvoja. | Kyllä | Kyllä  
Viikoittaiset tunnit MIN | Weekly_hours_MIN | Desimaali | Viikoittaisen työajan minimiarvo (esim. 15,5 tai 15.5). Kentän arvoa käytetään työvuorosuunnittelussa. | Tukee pilkkua `,` tai pistettä `.` ja miinusmerkkejä. | Kyllä | Kyllä  
Viikoittaiset tunnit MAX | Weekly_hours_MAX | Desimaali | Viikoittaisen työajan maksimiarvo (esim. 37,5 tai 37.5). Kentän arvoa käytetään työvuorosuunnittelussa. | Tukee pilkkua `,` tai pistettä `.` ja miinusmerkkejä. | Kyllä | Kyllä  
Työsuhteen alkupäivä | Employment_start_date | Päivämäärä |  [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9003095125149>). |  `DD.MM.YYYY` tai `YYYY-MM-DD` muodot piste `.`, vinoviiva `/` tai yhdysmerkki `-` erottimilla. Vuoden on oltava 1899 jälkeen. Täytyy olla ennen työsuhteen päättymispäivää tai samana päivänä; jos se on myöhemmin, annetaan varoitus ja rivi tallennetaan silti. | Ei | Kyllä  
Työsuhteen päättymispäivä | Employment_end_date | Päivämäärä | Jos työntekijän sopimus on toistaiseksi voimassaoleva, tulee kenttä tuoda tyhjänä. [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9003095125149>). |  `DD.MM.YYYY` tai `YYYY-MM-DD` muodot piste `.`, vinoviiva `/` tai yhdysmerkki `-` erottimilla. Vuoden on oltava 1899 jälkeen. Täytyy olla työsuhteen alkupäivänä tai sen jälkeen. | Ei | Kyllä  
Koeajan päättymispäivä | Trial_period_end_date | Päivämäärä | Koeajan päättymispäivämäärä. |  `DD.MM.YYYY` tai `YYYY-MM-DD` muodot piste `.`, vinoviiva `/` tai yhdysmerkki `-` erottimilla. Vuoden on oltava 1899 jälkeen. | Kyllä | Kyllä  
Yksikkö | Units | Teksti |  Yksikkö (tai yksiköt). Annetut arvot korvaavat olemassa olevat henkilön yksikköjäsenyydet.  
NOLLA-avainsanalla voidaan varmistaa kaikkien olemassa olevien yksikköjäsenyyksien poistaminen henkilöltä, vaikka IgnoreEmptyValues-asetus olisi käytössä (esim. web service -rajapinnan kautta). [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9001251146653>) **Huomioi:** Yksikkö pitää luoda ensin Neptoniin, jotta se voidaan tuoda oikein. |  Piippumerkillä `|` eroteltu lista yksiköiden nimistä tai koodeista. Tämä kenttä on kirjainkoosta riippumaton. Jokaisen arvon on vastattava **tarkalleen yhtä** olemassa olevaa yksikköä; jos arvo ei vastaa yhtään tai vastaa useita yksiköitä, tuotetaan varoitus eikä yksikköä määritetä (rivi tallennetaan silti). | Ei | Kyllä  
Työnantaja | Employer | Teksti | Henkilön työnantajan koodi. | Koodi validoidaan olemassa olevia työnantajia vasten (tuntematon koodi aiheuttaa varoituksen eikä määritä työnantajaa, vaikka rivi tallennetaan). | Kyllä | Kyllä  
Oletusprojekti | Default_project | Teksti | Henkilön oletusprojekti. | Tyhjä sallittu. Täytyy vastata olemassa olevan projektin koodia, joka **ei** ole ylä-/ryhmäprojekti. | Ei | Kyllä  
Vuororyhmä | Work_schedule_group | Teksti | Henkilön vuororyhmän koodi. | Tyhjä sallittu. Täytyy vastata olemassa olevaa vuororyhmän koodia (lomaryhmien koodeja ei hyväksytä). Tuntemattomat koodit aiheuttavat varoituksen ja ryhmää ei määritetä (rivi tallennetaan silti). | Kyllä | Kyllä  
Lomaryhmä | Holiday_schedule_group | Teksti | Henkilön lomaryhmän koodi. Huomaa, että mikäli henkilö kuuluu sekä vuoro- että lomaryhmään ja ryhmien aikataulut menevät päällekkäin, lomaryhmä yliajaa vuororyhmän, eli kalenterinäkymissä näytetään kyseisen henkilön osalta vain lomaryhmä. | Täytyy vastata olemassa olevaa lomaryhmän koodia; tyhjä sallittu. | Kyllä | Kyllä  
Oletuskustannuspaikka | Default_cost_group  | Teksti | Henkilön oletuskustannuspaikka. |  | Kyllä | Kyllä  
Ensisijainen esimies | Primary_supervisor | Teksti |  Ensisijaisen esimiehen henkilönumero. Tyhjä arvo tai NOLLA-avainsana tyhjentää ensisijaisen esimiehen (Alaiselle tulee olla määriteltynä vähintään yksi ensisijainen esimies, jotta ilmoitukset tapahtumapyynnöistä yms. lähetetään kenellekään). [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9002553468829>). **Huomioi:** Tällä hetkellä ensisijainen esihenkilö voidaan tuoda vain esihenkilön henkilönumerolla | Täytyy kuulua olemassa olevalle käyttäjälle. Tuntematon henkilönumero tai käyttäjän asettaminen omaksi esimiehekseen tuottaa varoituksen (esimiestä ei määritetä, mutta rivi tallennetaan silti). | Ei | Kyllä  
Toissijaiset esimiehet | Secondary_supervisors | Teksti |  Toissijaiset esimiehet. Jos arvojen joukossa on NOLLA-avainsana, luetellut esimiehet korvaavat kaikki henkilölle aiemmin luetellut toissijaiset esimiehet. [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9002553468829>). **Huomioi:** Tällä hetkellä toissijainen esihenkilö voidaan tuoda vain esihenkilön henkilönumerolla |  Piippumerkillä `|` eroteltu lista henkilönumeroita. Täytyy kuulua olemassa oleville käyttäjille. Tuntemattomat henkilönumerot tai käyttäjän asettaminen omaksi esimiehekseen tuottaa varoituksen (rivi tallennetaan silti). | Ei | Kyllä  
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
Fivaldi Heeros  
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
Visma | Teksti | Henkilön ulkoisen järjestelmän tunniste. Palvelussa on useita ulkoisen järjestelmän tunnisteita ja sarakkeen nimenä tulee käyttää otsikossa järjestelmän nimeä. Esimerkiksi 'Mepco'. |  | Kyllä | Kyllä  
Saldo | Balance | Kokonaisluku | Asettaa saldon arvon kuluvalle päivälle. | Täytyy ilmoittaa minuutteina kokonaislukuna. | Ei | Ei  
Hallinnon lisätieto | Additional_administrative_information | Teksti | Henkilön lisätiedot. |  | Kyllä | Kyllä  
Lähiomainen | Next_of_kin | Teksti | Lähiomaisen nimi. |  | Kyllä | Kyllä  
Lähiomaisen puhelinnumero | Next_of_kin_phone_number | Teksti | Lähiomaisen puhelinnumero. |  Vain numeroita (voi alkaa `+`, voi sisältää välilyöntejä tai yhdysmerkkejä, ja on päätyttävä numeroon). Tyhjä sallittu. Virheelliset arvot aiheuttavat varoituksen, mutta rivi tallennetaan silti. | Kyllä | Kyllä  
Raporteilla näkyvä lisätieto | Additional_information_for_reports | Teksti | Raportoinnin lisätieto. Kentän sisältö esitetään useilla palvelun raporteilla omana sarakkeenaan. |  | Kyllä | Kyllä  
Työsuhteen päättymissyy | Reason_for_ending_employment | Teksti | Työsopimuksen päättymisen syy. | Tarkka vastaavuus: "FixedTermContract" tai "EmploymentRelationshipEnded" | Kyllä | Kyllä  
Kuukausipalkka | Monthly_salary | Desimaali | Henkilön kuukausipalkka (esim. 2600, 3733.33 tai 4595,50). | Tukee desimaaleja pisteellä `.` tai pilkulla `,` ja miinusmerkkiä. | Kyllä | Kyllä  
Tuntipalkka | Hourly_wage | Desimaali | Henkilön tuntipalkka (esim. 20, 25.50 tai 23,50). | Tukee desimaaleja pisteellä `.` tai pilkulla `,` ja miinusmerkkiä. | Kyllä | Kyllä  
Veronumero | Tax_number | Teksti | Henkilön suomalainen veronumero. |  Täytyy olla 12 numeroa. Tyhjä sallittu. Vaatimusten vastainen arvo aiheuttaa varoituksen, ja rivi tallennetaan silti. | Kyllä | Kyllä  
Henkilöryhmä | Person_group | Teksti | Henkilön henkilöryhmän koodi. Vaihtoehtoisesti voidaan osana henkilötuontia muodostaa organisaatiorakenne kentillä 'Henkilöryhmän nimipolku hierarkiassa' ja 'Henkilöryhmän koodipolku hierarkiassa'. [Lisätietoa](<https://support.nepton.com/hc/fi/articles/9000335221661>). |  | Ei | Kyllä  
Henkilöryhmän nimipolku hierarkiassa | Person_group_name_path_in_hierarchy | Teksti |  Henkilöryhmien nimet, jotka muodostavat vanhempi-lapsi-hierarkian ja edustavat henkilöryhmärakennetta, johon henkilö kuuluu. Sekä "Henkilöryhmän koodipolku hierarkiassa" että "Henkilöryhmän nimipolku hierarkiassa" vaaditaan, jos toinen siirretään. Hierarkia luodaan ja päivitetään automaattisesti. Mikäli arvona tuodaan esimerkiksi 'Toimisto|Myyjät' niin palveluun muodostuu henkilöryhmä 'Toimisto', jonka alaryhmäksi perustetaan 'Myyjät'. Tuotava henkilö asetetaan ryhmään 'Myyjät'. |  Piippumerkillä `|` eroteltu lista ryhmien nimiä. Jos nimien määrä ei vastaa annettua koodipolkua, annetaan varoitus ja arvoa ei tallenneta (itse rivi tallennetaan silti). | Ei | Ei  
Henkilöryhmän koodipolku hierarkiassa | Person_group_code_path_in_hierarchy | Teksti |  Henkilöryhmien koodit, jotka edustavat henkilöryhmärakennetta, johon henkilö kuuluu. Sekä "Henkilöryhmän koodipolku hierarkiassa" että "Henkilöryhmän nimipolku hierarkiassa" vaaditaan, jos toinen siirretään. Hierarkia luodaan ja päivitetään automaattisesti. Mikäli arvona tuodaan esimerkiksi '10|20' niin palveluun muodostuu edellisen rivin esimerkkiä jatkaen 'Toimisto'-ryhmälle koodi '10' ja 'Myyjät'-ryhmälle koodi '20'. |  Piippumerkillä `|` eroteltu lista koodeja. Tyhjä syöte tai ero syötteiden määrässä nimipolkuun verrattuna aiheuttaa varoituksen ja arvoa ei tallenneta (itse rivi tallennetaan silti). | Ei | Kyllä  
Työajan asetusryhmä | Worktime_setting_group | Teksti |  Henkilön työajan asetusryhmän koodi. Kun syötät 'NOLLA' tai ei mitään (tyhjä arvo), henkilö poistetaan kaikista asetusryhmistä kuluvan päivän alusta ilman päättymispäivää. Alla oleva oletusarvo-osio tulee myös huomioida. |  Tarkka koodivastaavuus. Täytyy vastata olemassa olevaa työajan asetusryhmää. Tuntematon koodi tuottaa varoituksen, ja rivi tallennetaan silti. Tämä kenttä on kirjainkoosta riippumaton. | Kyllä | Kyllä  
Työaika prosentteina | Work_time_percentage | Desimaali | Henkilön työaikaprosentti, jota käytetään työpäivän ja työviikon pituuden laskemisessa. Jos prosenttiluku muuttuu, uutta prosenttilukua sovelletaan kuluvasta päivästä alkaen (esim. 80,00 tai 80.00). |  Tukee desimaaleja pilkulla `,` tai pisteellä `.` ja miinusmerkkiä. Tämä kenttä on kirjainkoosta riippumaton. | Kyllä | Ei  
Palvelun käyttökieli | Service_usage_language | Teksti |  Kieli, jolla henkilö käyttää palvelua. Tuetut arvot ovat:  "Finnish" (suomi), "English" (englanti), "Swedish" (ruotsi), "Danish" (tanska), "Norwegian" (norja), "Polish" (puola) ja "Estonian" (viro). Jos palvelun käyttökieltä ei ole annettu, käytetään palvelulle asetettua oletuskieltä, joka on oletuksena suomi. Jos asiakkuudelle halutaan vaihtaa toinen oletuskieli, tämän muuttamista voidaan pyytää Neptonin asiakaspalvelusta. | Tuntematon kieli tuottaa varoituksen ja rivi tallennetaan silti. | Kyllä | Ei  
Lyhytaikainen laina sallittu | Short_term_loan_permit | Totuusarvo | Palkkaennakko sallittu. | Tukee esim. yes/no, true/false, 1/0. | Kyllä | Ei  
Microsoft AX -tuntihinta | Microsoft_AX_hourly_cost | Desimaali | Tuntihinta. | Tukee desimaaleja pisteellä `.` tai pilkulla `,` ja miinusmerkkiä. | Kyllä | Kyllä  
Visma-kustannuspaikka | Visma_cost_centre | Teksti | Visma-kustannuspaikka. |  | Kyllä | Ei  
Maksuryhmä | Payment_group | Teksti | Henkilön jäsenyys maksuryhmässä. Maksuryhmän asettamisen perusteella henkilön palkanmaksu ohjataan maksuryhmän maksukausien perusteella. |  Voi olla koodi, nimi tai Nepton-tunniste. Täytyy vastata olemassa olevaa maksuryhmää (tyhjä sallittu). Tämä kenttä on kirjainkoosta riippumaton. | Kyllä | Ei  
Ammattiluokitus | Classification_of_occupations | Teksti | Tämä kenttä määrittelee [Tulorekisterin TK10-ammattiluokituksen](<https://www.stat.fi/fi/luokitukset/ammatti/ammatti_17_20210101/>) henkilön ammatille. | Täytyy vastata olemassa olevaa ammattiluokituskoodia (tyhjä sallittu). | Kyllä | Kyllä  
Sopimuksen tyyppi | Contract_type | Teksti | Tämä kenttä on pakollinen Nepton Palkat -palvelun ollessa käytössä. | Tarkka vastaavuus: monthlysalary tai hourlysalary | Ei | Ei  
## 
## Yksilölliset tunnistekentät
Käyttäjiä uudelleentuotaessa Nepton tunnistaa olemassa olevat käyttäjät tarkistamalla seuraavat kentät tässä tarkassa järjestyksessä: **1\. Nepton-tunniste** → **2\. Ulkoinen tunniste 1** → **3\. Käyttäjätunnus** → **4\. Henkilönumero**. Huomaa, että näiden ensisijaisten tunnisteiden lisäksi myös **RFID-tunnisteet** ja **PIN-koodit** tarkistetaan yksilöllisyyden osalta (kaksoiskappaleet aiheuttavat varoituksen eikä niitä määritetä, vaikka rivi tallennetaan silti).
### Nepton-tunniste
Neptonin yksilöllinen tunniste (GUID), jonka Nepton luo automaattisesti kaikille käyttäjille ja se näytetään käyttäjän tiedoissa. Tämän kentän arvoa ei voida käyttää uudelleen toiselle käyttäjälle (vaikka käyttäjä olisi poistettu) ja se on aina yksilöllinen. Uudelle käyttäjälle annettu GUID, joka ei täsmää olemassa olevaan henkilöön, hylkää koko rivin (muut kuin GUID-arvot tallennetaan sellaisenaan ilman päällekkäisyyksien poistoa).
### Ulkoinen tunniste 1
Ulkoinen tunniste 1 on yksilöllinen henkilötunniste. Jos käyttäjällä A on Ulkoinen tunniste 1 "ID-123" ja tuo tunniste täytyy määrittää käyttäjälle B, se tulee ensin poistaa käyttäjältä A.
### Henkilönumero
Henkilönumero on yksilöllinen henkilötunniste. Jos käyttäjällä A on henkilönumero 1234 ja se täytyy käyttää uudelleen käyttäjälle B, se tulee ensin poistaa käyttäjältä A. Jos rivi vastaa olemassa olevaa käyttäjää henkilönumeron perusteella, mutta sisältää eri käyttäjätunnuksen, koko rivi hylätään.
### Käyttäjätunnus
Käyttäjätunnus on yksilöllinen henkilötunniste. Jos käyttäjällä A on käyttäjätunnus Testi Käyttäjä ja se täytyy käyttää uudelleen käyttäjälle B, se tulee ensin poistaa käyttäjältä A. Huomaa, että olemassa olevan käyttäjän käyttäjätunnusta ei voi muuttaa, ellei tuonnissa ole määritetty "Henkilön tunniste" -asetukselle / "IdentifierFieldName"-parametrille muuta arvoa kuin käyttäjätunnus (koko rivi ohitetaan).
## Oletusarvot
Mikäli henkilötuonnissa ei ole määritelty jotakin arvoa, oletusarvoja käytetään uutta käyttäjää lisättäessä. Taulukossa kuvataan oletusarvot ja se, miten oletusarvot voidaan määritellä.
Kentän nimi | Säännöt | Miten asetetaan oletusarvo(t)  
---|---|---  
Työajan roolit | Jos oletusarvot on määritelty, niitä käytetään kun luodaan **uusi käyttäjä** eikä roolia ole määritelty. Tämä tehdään koska tämä on pakollinen kenttä. |  Työajan roolien oletusarvot voidaan määritellä asetuksessa "Työajan oletusrooli  
(Oletus kun uusi henkilö luodaan)" osiossa **Työsuhde** > **Hallinta >** **Asetukset > Yleiset**  
Työajan asetusryhmä |  Kun **uusi käyttäjä** luodaan **käyttöliittymän** kautta **Työsuhde > Henkilöt > Lisää henkilö** -näkymässä, tai luodaan tuomalla uusi käyttäjä tiedostolla **Työsuhde > Henkilöt > Tuo henkilöitä** -toiminnolla ja asetusryhmätietoa ei tuoda, käyttäjälle asetetaan oletusasetusryhmä, joka on määritelty **Työsuhde >** **Hallinta >** **Asetukset > Yleiset **-näkymässä. Poikkeus tähän on tilanne, jossa asetusryhmätietona tuodaan **RESET** -avainsana, tällöin kyseiselle käyttäjälle ei aseteta asetusryhmä-tietoa. Kun käyttäjä luodaan **ajastetun tehtävän** kautta ja asetusryhmätietoa ei ole määritelty tuotavassa tiedostossa, käyttäjälle ei aseteta asetusryhmä-tietoa.  
Eli asetus "Työajan oletusrooli  
(Oletus kun uusi henkilö luodaan)" ei päde tässä tilanteessa. **Joustava tila (Lenient mode):** Tässä tilassa tyhjät arvot ohitetaan eikä arvoa poisteta tietokannasta. **Tiukka tila (Strict mode):** Tässä tilassa, jos kentän arvo on tyhjä, arvo poistetaan tietokannasta. |  Työajan asetusryhmän oletusarvo voidaan määritellä asetuksessa "Työajan oletusrooli  
(Oletus kun uusi henkilö luodaan)" osiossa **Työsuhde** > **Hallinta >** **Asetukset > Yleiset**
