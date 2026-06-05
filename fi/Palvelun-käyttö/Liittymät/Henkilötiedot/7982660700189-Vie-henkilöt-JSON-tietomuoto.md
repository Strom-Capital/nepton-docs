---
id: 7982660700189
title: Vie henkilöt - JSON-tietomuoto
url: https://support.nepton.com/hc/fi/articles/7982660700189-Vie-henkil%C3%B6t-JSON-tietomuoto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötiedot
section_id: 360001070377
section_path:
- Liittymät
- Henkilötiedot
labels: []
promoted: false
updated_at: '2026-05-28T07:47:59Z'
edited_at: '2026-05-26T07:51:04Z'
---

# Vie henkilöt - JSON-tietomuoto

Henkilötietoja voidaan viedä Neptonista ulkoiseen järjestelmään. Tämä artikkeli kuvaa henkilötietojen viennin kentät, joita voidaan sisällyttää vietäessä tiedot JSON-tietomuodossa. Yksityiskohtainen kuvaus henkilötietojen viennistä löytyy [täältä](<https://support.nepton.com/hc/articles/360002489357>).
## Kentät JSON-muotoisessa henkilöviennin tiedostossa
**Kentän otsikko** | **Kenttä henkilötietolomakkeella** | **Sisällön muoto** | **Voidaan käyttää henkilön yksilöintiin**  
---|---|---|---  
Email | Sähköposti | Sähköpostiosoite | Ei  
Last name | Sukunimi | Tekstisisältö | Ei  
First name | Etunimi | Tekstisisältö | Ei  
IBAN | IBAN | [IBAN-muotoinen pankkitilinumero](<https://fi.wikipedia.org/wiki/IBAN>) | Ei  
Username | Käyttäjätunnus | Tekstisisältö (yksilöllinen) | Kyllä  
External identifier 1 | Ulkoinen tunniste 1 | Tekstisisältö (yksilöllinen) | Kyllä  
Street address | Katuosoite | Tekstisisältö | Ei  
Postcode | Postinumero | Tekstisisältö | Ei  
Phone number | Puhelinnumero | Puhelinnumero | Ei  
Web page | Verkkosivu | Tekstisisältö | Ei  
City | Postitoimipaikka | Tekstisisältö | Ei  
Employee number | Henkilönumero | Tekstisisältö (yksilöllinen) | Kyllä  
Personal identity code | Henkilötunnus | [Suomalainen henkilötunnus](<https://dvv.fi/henkilotunnus>) | Ei  
Default project | Oletusprojekti | Oletusprojektin koodi | Ei  
Employment start date | Työsuhteen alkupäivä | Päiväys muodossa "VVVV-KK-PP" | Ei  
Employment end date | Työsuhteen päättymispäivä | Päiväys muodossa "VVVV-KK-PP" | Ei  
Hourly wage | Tuntipalkka | Desimaaliluku | Ei  
Reason for ending employment | Työsuhteen päättymissyy | Tekstisisältö | Ei  
Additional administrative information | Hallinnon lisätieto | Tekstisisältö | Ei  
Default cost group | Oletuskustannuspaikka | Tekstisisältö | Ei  
RFID tag identifier | RFID-tunniste | Tekstisisältö | Ei  
BIC | BIC | [ISO 9362 BIC-koodi](<https://fi.wikipedia.org/wiki/ISO_9362>) | Ei  
Trial period end date | Koeajan päättymispäivä | Päiväys muodossa "VVVV-KK-PP" | Ei  
Short term loan permit | Lyhytaikainen laina sallittu | true = kyllä  
false = ei | Ei  
Full name | Koko nimi | Henkilön koko nimi muodossa Sukunimi, Etunimi | Ei  
Role | Rooli |  | [**Rooli**](<https://support.nepton.com/hc/fi/articles/360002425637>) | **Arvo**  
---|---  
Työntekijä | Employee  
Esimies | Supervisor  
Yksikön johtaja | Unit Manager  
Palkkahallinto | Salary Management  
Henkilöstöhallinto | HR Management  
Ylläpitäjä | Administrator  
Ei  
List of employee numbers of supervisors | Esimiehet |  [Esimiesten](<https://support.nepton.com/hc/fi/articles/360002430618>) henkilönumerot ensisijaisesta esimiehestä alkaen | Ei  
Job title | Ammattinimike | Tekstisisältö | Ei  
Work area | Työskentelyalue | Tekstisisältö | Ei  
Aastra | Aastra | Tekstisisältö | Ei  
Heeros | Heeros | Tekstisisältö | Ei  
DL Software | DL Software | Tekstisisältö | Ei  
Fivaldi | Fivaldi | Tekstisisältö | Ei  
Mepco | Mepco | Tekstisisältö | Ei  
Oscar | Oscar | Tekstisisältö | Ei  
Personec W | Personec W | Tekstisisältö | Ei  
Sedab | Sedab | Tekstisisältö | Ei  
Sonet | Sonet | Tekstisisältö | Ei  
Tikon | Tikon | Tekstisisältö | Ei  
Visma | Visma | Tekstisisältö | Ei  
Worktime setting group | Työajan asetusryhmä |  [Asetusryhmän](<https://support.nepton.com/hc/fi/articles/360002558498>) koodi | Ei  
User account enabled | Käyttäjätili käytössä | true = kyllä  
false = ei | Ei  
Scala | Scala | Tekstisisältö | Ei  
Additional information for reports | Raporteilla näkyvä lisätieto | Tekstisisältö | Ei  
Kieku | Kieku | Tekstisisältö | Ei  
Tax number | Veronumero | 12-numeroinen [Suomalainen veronumero](<https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48791/veronumero-ja-julkinen-veronumerorekisteri/#2.1-veronumero>) | Ei  
Next of kin | Lähiomainen | Tekstisisältö | Ei  
Next of kin phone number | Lähiomaisen puhelinnumero | Puhelinnumero | Ei  
Person group | Henkilöryhmä |  [Henkilöryhmän](<https://support.nepton.com/hc/fi/articles/360002553457>) koodi | Ei  
Hogia | Hogia | Tekstisisältö | Ei  
Elisa Ring | Elisa Ring | Tekstisisältö | Ei  
Personec F | Personec F | Tekstisisältö | Ei  
Primary task | Ensisijainen tehtävä | Ensisijaisen [tehtävän](<https://support.nepton.com/hc/fi/articles/360010504757>) koodi | Ei  
Primary supervisor | Ensisijainen esimies | Ensisijaisen [esimiehen](<https://support.nepton.com/hc/fi/articles/360002430618>) [Nepton-tunniste](<https://support.nepton.com/hc/fi/articles/8017902121885>) (UUID) | Ei  
Secondary supervisors | Toissijaiset esimiehet | Toissijaisten [esimiesten](<https://support.nepton.com/hc/fi/articles/360002430618>) [Nepton-tunnisteet](<https://support.nepton.com/hc/fi/articles/8017902121885>) (UUID) | Ei  
IFS | IFS | Tekstisisältö | Ei  
Lessor-5 | Lessor-5 | Tekstisisältö | Ei  
Service usage language | Palvelun käyttökieli |  | **Henkilön valittu kieli** | **Kentän arvo**  
---|---  
englanti | en-GB  
puola | pl-PL  
ruotsi | sv-SE  
suomi | fi-FI  
tanska | da-DK  
viro | et-EE  
norja | nb-NO  
Ei  
Emce | Emce | Tekstisisältö | Ei  
Microsoft AX hourly cost | Microsoft AX -tuntihinta | Desimaaliluku | Ei  
Weekly hours MIN | Viikoittaiset tunnit MIN | Desimaaliluku | Ei  
Weekly hours MAX | Viikoittaiset tunnit MAX | Desimaaliluku | Ei  
Visma cost centre | Visma-kustannuspaikka | Tekstisisältö | Ei  
Work time percentage | Työaika prosentteina | Desimaaliluku | Ei  
Worktime roles | Työajan roolit |  [Työajan roolien](<https://support.nepton.com/hc/fi/articles/360002554338>) nimet | Ei  
Units | Yksiköt |  [Yksiköiden](<https://support.nepton.com/hc/fi/articles/360002590317>) koodit | Ei  
Deputy | Sijainen |  [Sijaisten](<https://support.nepton.com/hc/fi/articles/360002430678>) [Nepton-tunnisteet](<https://support.nepton.com/hc/fi/articles/8017902121885>) | Ei  
Mobile link | Mobiililinkki | Url | Ei  
NeptonPersonGUID | Nepton-tunniste |  [Nepton-tunniste](<https://support.nepton.com/hc/fi/articles/8017902121885>) (UUID) | Kyllä (suositeltu)  
Monthly wage | Kuukausipalkka | Desimaaliluku | Ei  
Classification of occupations | Ammattiluokitus | 5-numeroinen [Tulorekisterin TK10-ammattiluokitus](<https://www.stat.fi/fi/luokitukset/ammatti/ammatti_17_20210101/>) | Ei  
Payment group | Maksuryhmä |  [Maksuryhmän](<https://support.nepton.com/hc/fi/articles/4406602996625>) tunniste (UUID) | Ei  
Kaikki [henkilön lisätietokentät](<https://support.nepton.com/hc/fi/articles/360002430918>) | (Kentän nimi) | Muotoiltu kunkin kentän tyypin mukaisesti | Ei  
## Tietomuodon yksityiskohdat
  * Character encoding of the exported file is always [UTF-8](<https://en.wikipedia.org/wiki/UTF-8>) (a Unicode encoding).
  * Vientitiedoston merkistökoodaus on aina [UTF-8](<https://fi.wikipedia.org/wiki/Unicode#UTF-8>) (yleinen Unicode-merkistökoodaus).
  * Rivinvaihto on Windowsin vakiorivinvaihto (CR+LF 0x0D 0x0A).
  * [JSON](<https://fi.wikipedia.org/wiki/JSON>)-tietomuodossa henkilötiedot viedään henkilöolioiden taulukkona.
  * Jokainen henkilöoolio vastaa yhtä henkilöä.
  * Henkilöolio koostuu nimi–arvo-pareista, joissa kukin nimi vastaa kentän nimeä ja arvo on yhden tai useamman arvo-olion taulukko.
  * Kukin arvo-olio koostuu kolmesta nimi–arvo-parista:
**Nimi** | **Arvo**  
---|---  
Valid from | null (= määrittelemätön) tai ensimmäinen päiväys, jolloin arvo on tai oli voimassa, muodossa "VVVV-KK-PP"  
Valid to | null (= määrittelemätön) tai viimeinen päiväys, jolloin arvo on tai oli voimassa, muodossa "VVVV-KK-PP"  
Value | Desimaaliluku tai totuusarvo (true/false) ilman lainausmerkkejä tai mikä tahansa muu arvo lainausmerkeissä (")  
  * Jos kenttä ei ole käytössä tai sille ei ole määritelty arvoa, kenttä ei ole mukana tiedostossa lainkaan.
  * [Nepton-tunniste](<https://support.nepton.com/hc/fi/articles/8017902121885>) (kentän nimi NeptonPersonGUID), Ulkoinen tunniste 1 (External identifier 1), käyttäjätunnus (Username) ja henkilönumero (Employee number) ovat kaikki henkilön yksilöiviä kenttiä ja niitä voidaan käyttää henkilön tunnistamiseen. Suosittelemme Nepton-tunnisteen käyttämistä, koska se ei varmuudella muutu. Muilla näistä tunnisteista lukuunottamatta kenttää "Ulkoinen tunniste 1", on aina arvo vientiaineistossa.
  * Päivämääräkentät käyttävät muotoa "VVVV-KK-PP" (vuosi, kuukausi ja päivä väliviivoin (-) eroteltuina, lainausmerkein ympäröityinä).
  * Mahdolliset päivämäärä ja aika -tyyppiset [lisätietokentät](<https://support.nepton.com/hc/fi/articles/360002430918>) käyttävät muotoa "VVVV-KK-PP TT:MM:SS" (vuosi, kuukausi ja päivä eroteltuina väliviivoin (-), välilyönti, tunnit, minuutit ja sekunnit eroteltuina kaksoispistein (:), lainausmerkein ympäröityinä).
  * Desimaaliluvut käyttävät pistettä (.) desimaalierottimena, kun desimaaliosa ei ole nolla. Muutoin arvo on vain kokonaisluku. Negatiivisissa luvuissa on viiva alussa (-).
  * UUID-kentät esitetään merkkijonoina, jotka koostuvat 32 heksadesimaalimerkistä eroteltuina neljällä väliviivalla: 8 merkkiä - 4 merkkiä - 4 merkkiä - 4 merkkiä - 12 merkkiä. Kirjainmerkit ovat isokirjaimisia. Koodi ympäröidään lainausmerkein (").
  * Mitkä tahansa muut arvot kuin true (tosi), false (epätosi), null (määrittelemätön) tai desimaaliluvut ympäröidään aina lainausmerkein ("). Tietyt merkit korvataan takakenoviivalla (\\) alkavilla merkkiyhdistelmillä:
**Korvaava merkkijono** | **Alkuperäinen merkki**  
---|---  
\" | "  
\\\ | \  
\/ | /  
\b | askelpalautin (backspace)  
\f | sivunvaihto (form feed)  
\r | paluu rivin alkuun (carriage return)  
\n | rivinvaihto (line feed)  
\u heksadesimaalikoodi | mikä tahansa Unicode-merkki, joka ei ole sallitulla arvovälillä 0x0020 - 0x10FFFF esitetään \u-alukkeella ja vähintään 4-merkkisenä heksadesimaalikoodina  


## Esimerkkitiedosto
[code]
    [
    	{
    		"Email": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "email@compa.ny"
    			}
    		],
    		"Last name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Last"
    			}
    		],
    		"First name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "First"
    			}
    		],
    		"Username": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "First Last"
    			}
    		],
    		"Street address": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Street address 1"
    			}
    		],
    		"Postcode": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "01234"
    			}
    		],
    		"Phone number": [
    			{
    				"Valid from": null,
    				"Valid to": "2022-10-28",
    				"Value": "019581928"
    			},
    			{
    				"Valid from": "2022-10-29",
    				"Valid to": null,
    				"Value": "08855150015"
    			}
    		],
    		"City": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "City"
    			}
    		],
    		"Employee number": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "1"
    			}
    		],
    		"Personal identity code": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "111111-111C"
    			}
    		],
    		"Employment start date": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "2022-11-01"
    			}
    		],
    		"Full name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Last, First"
    			}
    		],
    		"Role": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Employee"
    			}
    		],
    		"User account enabled": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": true
    			}
    		],
    		"Service usage language": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "en-GB"
    			}
    		],
    		"Weekly hours MIN": [
    			{
    				"Valid from": null,
    				"Valid to": "2022-11-15",
    				"Value": 40
    			},
    			{
    				"Valid from": "2022-11-16",
    				"Valid to": null,
    				"Value": 37.55
    			}
    		],
    		"Weekly hours MAX": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": 40
    			}
    		],
    		"Work time percentage": [
    			{
    				"Valid from": "2022-12-01",
    				"Valid to": null,
    				"Value": 50
    			}
    		],
    		"Worktime roles": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Omien sekä alaisten tietojen muokkausoikeus"
    			}
    		],
    		"NeptonPersonGUID": "37F7EAFE-046F-ED11-81FD-A0510B65B142",
    		"AdditionalDecimal": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": 4.5
    			}
    		],
    		"External identifier 1": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "12345"
    			}
    		],
    		"AdditionalDateTime": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "2022-11-20 12:20:00"
    			}
    		]
    	},
    	{
    		"Last name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Account"
    			}
    		],
    		"First name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Disabled"
    			}
    		],
    		"Username": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Disabled Account"
    			}
    		],
    		"Full name": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Account, Disabled"
    			}
    		],
    		"Role": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Employee"
    			}
    		],
    		"User account enabled": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": false
    			}
    		],
    		"Service usage language": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "fi-FI"
    			}
    		],
    		"Worktime roles": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "Omien sekä alaisten tietojen muokkausoikeus"
    			}
    		],
    		"NeptonPersonGUID": "FA1A79A9-126F-ED11-81FD-A0511B65B142"
    		"External identifier 1": [
    			{
    				"Valid from": null,
    				"Valid to": null,
    				"Value": "123456"
    			}
    		],
    	}
    ]
[/code]
