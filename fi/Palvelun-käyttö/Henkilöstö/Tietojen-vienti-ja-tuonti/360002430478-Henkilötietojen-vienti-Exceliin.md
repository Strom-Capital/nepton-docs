---
id: 360002430478
title: Henkilötietojen vienti Exceliin
url: https://support.nepton.com/hc/fi/articles/360002430478-Henkil%C3%B6tietojen-vienti-Exceliin
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tietojen vienti ja tuonti
section_id: 360004488578
section_path:
- Henkilöstö
- Tietojen vienti ja tuonti
labels: []
promoted: false
updated_at: '2026-05-28T07:44:01Z'
edited_at: '2026-04-21T08:23:01Z'
---

# Henkilötietojen vienti Exceliin

Henkilötietoja voidaan viedä Exceliin, mikäli on oikeus tarkastella muiden henkilöiden tietoja henkilöhaun kautta. Esimerkiksi esimiehet voivat viedä omia ja alaistensa tietoja raportointitarkoituksiin. Voidaan käyttää myös vientitoiminnallisuutta ja muokata useampia arvoja kerralla Excelissä, jonka jälkeen tuoda muokatut tiedot Neptoniin tai ulkoiseen järjestelmään.
Teknisistä rajoituksista johtuen henkilön viennin ja tuonnin tukemien tietokenttien välillä on eroja. Tarkista ohjeista aina huolellisesti uusimmat tiedot.
## Vie Exceliin
  1. Siirry valikkoon **Työsuhde > Henkilöt > Henkilöt.**
  2. Suodata henkilölistaa eri hakukriteereillä kunnes löydät haluamasi henkilöt, joiden tiedot haluat viedä.
  3. Valitse **Vie Exceliin** ja **tallenna** tiedosto tietokoneellesi.
  4. Voit avata tallennetun tiedoston Excelissä tai muissa taulukkolaskentaohjelmissa.


## Vie sisäänluettavaan Exceliin
  1. Siirry valikkoon **Työsuhde > Henkilöt > Henkilöt.**
  2. Suodata henkilölistaa eri hakukriteereillä kunnes löydät haluamasi henkilöt, joiden tiedot haluat viedä.
  3. Valitse **Vie sisäänluettavaan Exceliin** ja **tallenna** tiedosto tietokoneellesi.


Sisäänluettavaa Exceliä voi hyödyntää henkilötietojen tuonnissa. [Tästä artikkelista](<https://support.nepton.com/hc/fi/articles/360003762577>) löydät tarkemmat tiedot henkilötietojen tuontiin liittyen.
## Sisäänluettavan Excel-tiedoston sarakkeet
Vientitiedoston nimessä on alussa päiväys ja kellonaika, sitten "HENKILOT" ja lopuksi työyhteisön nimi - muodossa: VVVVKKPP_TTMM_HENKILOT_TYÖYHTEISÖ.xlsx. Kaikki henkilöt ovat ensimmäisellä lomakkeella. Lomakkeen nimi on "Henkilölista".
Sarakkeet näytetään seuraavassa järjestyksessä. Sarakkeiden järjestystä ei voi muokata.
Sarakkeen nimi näytetään ensimmäisellä rivillä, muilla riveillä on kullakin yhden henkilön tiedot.
**Sarake oletusarvoisessa Excel-tiedostossa** | **Sarake sisäänluettavassa Excel-tiedostossa** | **Sarakkeen nimi** | **Kuvaus**  
---|---|---|---  
A | A | Etunimi | Henkilön etunimi  
B | B | Sukunimi | Henkilön sukunimi  
C | C | Sähköposti | Henkilön sähköpostiosoite  
D | D | Puhelinnumero | Henkilön puhelinnumero (tekstinä)  
E | E | Katuosoite | Henkilön osoitteen katuosoite  
F | F | Postinumero | Henkilön osoitteen postinumero (tekstinä)  
G | G | Postitoimipaikka | Henkilön osoitteen postitoimipaikka (tekstinä)  
H | H | IBAN | Henkilön pankkitilin IBAN-tunnus ilman välilyöntejä  
I | I | BIC | Henkilön pankkiyhteyden BIC-tunnus  
J | J | Henkilötunnus | Henkilön henkilötunnus  
K | K | Veronumero | Henkilön veronumero (tekstinä)  
L | L | Lähiomainen | Henkilön lähiomainen  
M | M | Lähiomaisen puhelinnumero | Henkilön lähiomaisen puhelinnumero (tekstinä)  
N | N | Verkkosivu | Henkilön verkkosivun osoite  
O | O | Ammattinimike | Henkilön ammattinimike  
P | P | Ammattiluokitus | Viisinumeroinen koodi (Käytössä Nepton Palkat -toiminnossa)  
Q | Q | Sopimuksen tyyppi | Kuukausipalkkainen tai tuntipalkkainen työntekijä  
R | R | Työsuhteen alkupäivä | Henkilön nykyisen tai viimeisimmän työsuhteen alkamispäivä (muodossa PP.KK.VVVV)  
S | S | Työsuhteen päättymispäivä | Henkilön viimeisimmän työsuhteen päättymispäivä (muodossa PP.KK.VVVV)  
T | T | Työsuhteen päättymissyy | Henkilön viimeisimmän työsuhteen päättymissyy  
U | U | Syy työsopimuksen päättymiseen | Tekstimuotoinen selitys työsuhteen päättymiselle  
V | V | Koeajan päättymispäivä | Henkilön koeajan päättymispäivä (muodossa PP.KK.VVVV)  
W | W | Työajan asetusryhmä | Sen työajan asetusryhmän koodi, johon henkilö kuuluu  
X | X | Työaika prosentteina | Henkilön työaika prosentteina (pilkulla (,) eroteltu desimaaliluku tekstinä)  
Y | Y | Kuukausipalkka | Henkilön kuukausipalkka (numeerinen, voi olla myös desimaaleja, mutta ei voi alkaa nollalla)  
Z | Z | Tuntipalkka | Henkilön tuntipalkka (tekstinä)  
AA | AA | Työskentelyalue | Henkilön työskentelyalue  
AB | AB | Työnantaja | Työnantaja  
AC | AC | Rooli | Henkilön rooli Neptonissa ("Työntekijä", "Esimies", "Yksikön johtaja", "Palkkahallinto", "Henkilöstöhallinto" tai "Ylläpitäjä")  
AD | AD | Työajan roolit | Niiden työajan roolien nimet, joita henkilöllä on, eroteltuina piippumerkillä (|)  
AE | AE | Pääsy henkilöryhmiin | Lista henkilöryhmistä joihin henkilöllä on lisäoikeuksia  
AF | AF | Lyhytaikainen laina sallittu | "Kyllä", jos lyhytaikainen laina on sallittu, muutoin "Ei"  
AG | AG | Henkilöryhmä | Sen henkilöryhmän koodi, jonka jäsen henkilö on  
AH | AH | Yksiköt | Niiden yksiköiden nimet, joihin henkilö kuuluu (ei erityisessä järjestyksessä), eroteltuina piippumerkillä (|)  
AI | AI | Oletusprojekti | Henkilön oletusprojektin koodi (tekstinä)  
AJ | AJ | Oletuskustannuspaikka | Henkilön oletuskustannuspaikka  
AK | AK | Maksuryhmä | Niiden maksuryhmien nimet, joihin henkilö kuuluu (ei erityisessä järjestyksessä), eroteltuina piippumerkillä (|)  
AL | AL | Viikoittaiset tunnit MIN | Henkilön viikoittaisen työajan minimi tunteina (pilkulla (,) eroteltu desimaaliluku tekstinä)  
AM | AM | Viikoittaiset tunnit MAX | Henkilön viikoittaisen työajan maksimi tunteina (pilkulla (,) eroteltu desimaaliluku tekstinä)  
AO | AO | Vuororyhmä | Vuororyhmä vuorokalentereissa  
AP | AP | Lomaryhmä | Lomaryhmä vuorokaletereissa  
AQ | AQ | Hallinnon lisätieto | Henkilölle syötetty hallinnon lisätieto  
AR | AR | Raporteilla näkyvä lisätieto | Henkilölle syötetty raporteilla näkyvä lisätieto  
AS | AS | Palvelun käyttökieli | Sen kielen englanninkielinen nimi, jolla henkilö käyttää Neptonia:  
"English" = englanti  
"Finnish" = suomi  
"Swedish" = ruotsi  
"Danish" = tanska  
"Polish" = puola  
"Estonian" = viro  
"Norwegian" = norja  
AT | AT | Microsoft AX -tuntihinta | Microsoft AX -tuntihinta (pilkulla (,) eroteltu desimaaliluku tekstinä)  
AU | AU | Visma-kustannuspaikka | Visma-kustannupaikka (tekstinä)  
AV | AV | Nepton-tunniste | Neptonin automaattisesti luoma muuttumaton tunniste, jolla henkilö on aina tunnistettavissa.   
AW | AW | Henkilönumero | Henkilön henkilönumero Neptonissa (tekstinä)  
AX | AX | Käyttäjätunnus | Henkilön käyttäjätunnus Neptonissa  
AY | AY | Ulkoinen tunniste (tulee toukokuussa 2026) | Yksilöllinen ulkoinen tunniste  
AZ | AZ | RFID-tunniste | Henkilön RFID-tunniste  
BA | BA | Aastra | Henkilön Aastra-tunniste (tekstinä)  
BB | BB | DL Software | Henkilön DL Software -tunniste (tekstinä)  
BC | BC | Elisa Ring | Henkilön Elisa Ring -tunniste (tekstinä)  
BD | BD | Emce | Henkilön Emce-tunniste (tekstinä)  
BE | BE | Fivaldi | Henkilön Fivaldi-tunniste (tekstinä)  
BF | BF | Heeros | Henkilön Heeros-tunniste (tekstinä)  
BG | BG | Hogia | Henkilön Hogia-tunniste (tekstinä)  
BH | BH | IFS | Henkilön IFS-tunniste (tekstinä)  
BI | BI | Kieku | Henkilön Kieku-tunniste (tekstinä)  
BJ | BJ | Lessor-5 | Henkilön Lessor-5-tunniste (tekstinä)  
BK | BK | Liksa | Henkilön Liksa-tunniste (tekstinä)  
BL | BL | Mepco | Henkilön Mepco-tunniste (tekstinä)  
BM | BM | Oscar | Henkilön Oscar-tunniste (tekstinä)  
BN | BN | Personec F | Henkilön Personec F -tunniste (tekstinä)  
BO | BO | SD Worx | Henkilön SD Worx (aiemmin Personec W) -tunniste (tekstinä)  
BP | BP | ProCountor | Henkilön ProCountor-tunniste (tekstinä)  
BQ | BQ | Scala | Henkilön Scala-tunniste (tekstinä)  
BR | BR | Sedab | Henkilön Sedab-tunniste (tekstinä)  
BS | BS | Sonet | Henkilön Sonet-tunniste (tekstinä)  
BT | BT | Tikon | Henkilön Tikon-tunniste (tekstinä)  
BU | BU | Visma | Henkilön Visma-tunniste (tekstinä)  
Sarakkeesta BO lähtien - yksi sarake kutakin kohden | Sarakkeesta BO lähtien - yksi sarake kutakin kohden | (Henkilön lisätietokenttien nimikentät) | Yksi sarake kutakin henkilön lisätietokenttää kohden samassa järjestyksessä kuin listattu toiminnossa Työsuhde > Hallinta > Henkilön lisätietokentät. Sisältö näytetään tekstinä ja sarakkeen sisältö on sama kuin kentän alasvetovalikosta valittu arvo. Muoto riippuu kentän tyypistä:  
Kokonaislukukentissä numero näytetään ilman välimerkkejä, jos arvo on 0:n ja 2147483647:n välillä. Negatiiviset luvut -2147483648:n ja -1:n välillä näytetään miinusmerkkietuliitteellä (-). Näiden rajojen ulkopuolisia numeroita ei näytetä.  
Desimaaliluvuilla erotinmerkkinä on pilkku (,)  
Kyllä/Ei-kentillä arvona on "Kyllä" tai "Ei"  
Päivämäärä ja aika -kentillä muoto on PP.KK.VVVV TT:MM  
Päivämääräkentillä muoto on PP.KK.VVVV  
Muilla kentillä arvo on muotoiltu kuten näytetään henkilölomakkeella  
Lisätietokenttien jälkeen | Ei käytössä sisäänluettavassa Excel-tiedostossa | Sijainen | Henkilön aktiiviset sijaiset suku- ja etunimi pilkulla (,) ja välilyönnillä eroteltuina. Sijaiset näkyvät vain "Vie Exceliin" raportilla, eivät "Vie sisäänluettavaan exceliin".  
|  | Koko nimi | Henkilön suku- ja etunimi pilkulla (,) ja välilyönnillä eroteltuina  
|  | Ensisijainen esimies | Henkilön ensisijaisten esimiesten henkilönumerot piippumerkillä (|) eroteltuina  
|  | Toissijaiset esimiehet | Henkilön toissijaisten esimiesten henkilönumerot piippumerkillä (|) eroteltuina  
|  | Esimiesten henkilönumerolista | (Tyhjä sarake, ks. edelliset sarakkeet)  
|  | Käyttäjätili käytössä | "Kyllä", jos käyttäjätili on käytössä, muutoin "Ei"  
| Ei käytössä sisäänluettavassa Excel-tiedostossa | Mobiililinkki | Linkki henkilön vanhalle mobiilisivulle. Sarake on käytössä vain oletus-Excel-tiedostossa ja vain jos vanha mobiililinkkiominaisuus on käytössä  
|  | Voimassa alkaen | [(Tyhjä sarake - täytettäväksi manuaalisesti tuontia varten, ks. Tietojen voimassaolot henkilötuonneissa)](<https://support.nepton.com/hc/articles/360015807338>)  
| Ei käytössä sisäänluettavassa Excel-tiedostossa | PrimarySupervisorFullNames | Henkilön ensisijaisen esimiehen suku- ja etunimi pilkulla (,) ja välilyönnillä eroteltuina. Jos henkilölle on merkitty useita ensisijaisia esimiehiä, heidät kaikki luetellaan piippumerkillä (|) eroteltuina.  
| Ei käytössä sisäänluettavassa Excel-tiedostossa | SecondarySupervisorFullNames | Henkilön toissijaisen esimiehen suku- ja etunimi pilkulla (,) ja välilyönnillä eroteltuina. Jos henkilöllä on useita esimiehiä, joita ei ole merkitty ensisijaisiksi, heidät kaikki luetellaan piippumerkillä (|) eroteltuina.
