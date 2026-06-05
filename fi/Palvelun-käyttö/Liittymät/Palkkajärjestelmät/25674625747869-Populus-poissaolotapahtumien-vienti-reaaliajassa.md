---
id: 25674625747869
title: Populus poissaolotapahtumien vienti reaaliajassa
url: https://support.nepton.com/hc/fi/articles/25674625747869-Populus-poissaolotapahtumien-vienti-reaaliajassa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels: []
promoted: false
updated_at: '2026-01-15T08:25:53Z'
edited_at: '2026-01-15T08:25:53Z'
---

# Populus poissaolotapahtumien vienti reaaliajassa

Populus poissaolojen vienti -liittymällä poissaolot lisätään vientipuskuriin reaaliajassa kun ne tallennetaan Neptonissa. Puskurissa olevat tiedot siirretään valitulla aikavälillä kohdepalvelimelle, josta Populus noutaa tiedot. Liittymä käyttää Populuksen poisto- ja lisäysmerkintöjä ("P" ja "U"). Poissaoloa muokattaessa lähetetään molemmat.
Poisto- ja lisäysmerkinnät jaetaan omiin tiedostoihin. Samassa tiedostossa ei koskaan ole sekä poisto- että lisäysmerkintöjä.
## Hyvä tietää
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa.
  * Liittymä käsittelee ainoastaan poissaoloja. Huomaathan tämän, kun teet poimintasääntöä. Esim. työtapahtumia ei käsitellä mutta tapahtumatyyppi, jonka käyttäytymiseksi on valittu "poissaolo", otetaan mukaan (liittymä käsittelee siis tapahtumia, joiden activitytypecategoryid = '2').
  * Mikäli poissaolotapahtuma aloitetaan kalenterissa ilman lopetusaikaa, liittymä ei käsittele sitä. Liittymä käsittelee poissaolotapahtuman, kun se lopetetaan ja sille määrittyy lopetusaika.
  * Poissaolotapahtuman tallennuksen yhteydessä käsitellään vain kyseinen poissaolotapahtuma ja se viedään puskuriin. Muut saman päivän tapahtumat eivät tule osaksi aineistoa.
  * Poissaolotapahtuma siirretään ainoastaan, jos se on uusi, poistettu tai siihen on tehty sellainen muutos, joka koskee aineistossa siirrettävää tietoa. Tarkista [aineiston tietueet](<https://support.nepton.com/hc/fi/articles/23700503323933#h_01JEZPPGFVHBYN65G1EJJRSETM>) -kohdasta alta, mitkä tiedot siirretään. Esimerkiksi kommentin lisääminen poissaolotapahtumaan ei muodosta uutta aineistoa.
  * **Mikäli halutaan siirtää tapahtumat vasta hyväksyttyinä, niin poimintasääntöön tulee lisätä isApproved = 'Y'**
  * Poissaolotapahtuman voi tallentaa vaikka liittymän suorittamisessa ilmenisi ongelmia. Esim. virheellinen poimintasääntö tai ongelma SFTP-palvelimella ei estä poissaolotapahtuman tallentamista. Virheestä annetaan käyttäjälle varoitus.
  * Jokaista poissaolotapahtumaa ja sääntöjoukkoa kohden muodostetaan oma tiedosto, joka siirretään SFTP-palvelimelle. Mikäli sama poissaolotapahtuma muodostaa aineistoa kahdessa eri sääntöjoukossa, luodaan kaksi eri tiedostoa.
  * Poistettu poissaolotapahtuma tai muokatun poissaolotapahtuman edellinen versio muodostuu aineistolle poistomerkinnällä "P".
  * Uusi tapahtuma tai muokatun poissaolotapahtuman viimeisin versio muodostuu aineistolle lisäysmerkinnällä "U".
  * Poissaolotapahtuman muokkaus muodostaa kaksi riviä. Ensimmäisellä rivillä on poissaolon ennen muokkausta ollut versio tunnisteella ”P”. Jälkimmäisellä rivillä on poissaolon päivitetty versio tunnisteella “U". Ensimmäinen ja jälkimmäinen rivi luodaan omiin tiedostoihin.
  * Liittymää varten on mahdollista määritellä useampi sääntöjoukko. Mikäli liittymälle on määritelty useita sääntöjoukkoja, tapahtuman tallennus voi kestää hieman kauemmin.
  * Mikäli poissaolotapahtumia poistetaan henkilön kalenterista massatoimintojen kautta, muodostuvat poistettavat rivit yhteen tiedostoon, vaikka poissaolotapahtumia olisi useampi. Poissaolotapahtumia kopioidessa jokaista tapahtumaa kohden muodostuu oma tiedosto.


## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilötunnisteet voidaan määrittää kohdassa **Työsuhde > Henkilön tiedot > Tunnisteet**.
![](https://support.nepton.com/hc/article_attachments/25820999682845)
**2\. Kohdepalvelimen lisäys**
Jos liittymälle ei vielä ole kohdepalvelinta, lisää se työyhteisön asetuksista kohdasta Liittymät > Liittymien kohdepalvelimet. Katso [Työajan vientiliittymien kohdepalvelimet](<https://support.nepton.com/hc/fi/articles/26861716054045>) yleiset ohjeet kohdepalvelimen lisäykseen ja kohdepalvelimen SFTP-asetuksien asetukseen.
Kohdepalvelimen SFTP-asetuksissa tulee määrittää vähintään _SFTP-palvelimen osoite, SFTP-käyttäjätunnus_ sekä _SFTP-salasana_(tai public key -autentikointi)
**3\. Liittymän asetukset**
Liittymän käyttöönottoa varten tulee määrittää [sääntöjoukko](<https://support.nepton.com/hc/fi/articles/360002492278>), jolla muodostetaan poissaoloaineisto. Sääntöjoukon asetuksissa valitaan viennin tiedostomuodoksi _Populus poissaolojen vienti_.
![](https://support.nepton.com/hc/article_attachments/25820999688349)
Valitse liittymälle kohdepalvelin, jonka lisäsit kohdassa 2.
![](https://support.nepton.com/hc/article_attachments/27155310719389)
Vientitiedoston nimeen tulee lisätä tarkka aikaleima _[timestamp-ms]_ , kuten alla olevassa esimerkissä. Mikäli aikaleimaa ei käytetä, jokaisella tiedostolla on sama nimi ja ne ylikirjoittavat toisensa.
![](https://support.nepton.com/hc/article_attachments/27155310721565)
Vientitiedoston nimeen on myös mahdollista lisätä konteksti, eli onko tiedosto poisto- vai lisäysmerkinnät sisältävä tiedosto. Mikäli tämä lisätään, on tärkeää, että se on aikaleiman jälkeen. Esimerkiksi:
[code]
    nep-poissaolot-[timestamp-ms]-[context].csv
[/code]
Tiedostonimet yllä olevalla esimerkillä olisivat seuraavan muotoiset:
  * Poistomerkinnöille: nep-poissaolot-1741348913396-P.csv
  * Lisäysmerkinnöille: nep-poissaolot-1741348913396-U.csv


**4\. Viennin ajastus kohdepalvelimelle**
Viimeisenä kohdepalvelimen puskurille tarvitsee määrittää viennin ajastus. Tästä voit lukea lisää artikkelista [Työajan vientiliittymien kohdepalvelimet](<https://support.nepton.com/hc/fi/articles/26861716054045#h_01JSK5VK4NMRKM5R7TP1B6ATE1>).
## Tiedostomuoto
Siirtotiedosto on UTF-8 muotoista puolipisteellä (`;`) eroteltua tekstimuotoista dataa. Rivinvaihto on `LF`. Siirtotiedoston lopussa on yksi tyhjä rivi.
## Aineiston tietueet
Sarake | Kenttä | Sääntöjoukon kentän nimi | Muoto (maksimipituus) | Kuvaus  
---|---|---|---|---  
A | Tapahtuman tunnus | PopulusAbsenceEventIdentifier | string(3) | Tapahtuman tunnus, oletuksena tyhjä.  
B | Tapahtuman tyyppi | _Lisätään automaattisesti_ | string(1) |  Määrittää, onko tieto Populuksesta poistettava vai Populukseen lisättävä.
  * Poisto: `P`
  * Lisäys: `U`

Voidaan ohittaa sääntöjoukon säännössä kentällä `RowContext`, esimerkiksi:
[code] 
    SELECT *,
    CASE WHEN :integrationContext = 'P'
      THEN 'D'
      ELSE 'N'
    END AS RowContext
    FROM UserSalaryData
[/code]
Esimerkissä poiston tyyppi korvataan olemaan `D` ja lisäyksen tyyppi olemaan `N`.  
C | Yhteisö/yritys | PopulusAbsenceCompany | number(4) | Yhteisö/yritys, oletuksena tyhjä.  
D | Palkanlaskentaryhmä | _Henkilön maksuryhmän koodi_ | string(3) | Palkanlaskentaryhmä. Voidaan ohittaa sääntöjoukon säännössä kentällä `PopulusAbsencePaymentGroup`.  
E | Henkilönumero | _Lisätään automaattisesti_ | string(11) | Henkilön henkilönumero. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideUserIntegrationId`.  
F | Henkilön nimi | _Lisätään automaattisesti_ | string(50) | Henkilön suku- ja etunimet. Voidaan ohittaa sääntöjoukon säännössä kentällä `PopulusAbsencePersonName`.  
G | Palvelussuhteen tunnus | PopulusAbsenceWorkRelationshipId | number(8) | Palvelussuhteen tunnus, oletuksena tyhjä.  
H | Työsuhteen alkupäivä | _Lisätään automaattisesti_ | string(8) | Työsuhteen alkupäivä, muodossa `VVVVKKPP`. Voidaan ohittaa sääntöjoukon säännössä kentällä `PopulusAbsenceWorkRelationshipStartDate`. Säännössä valitut päivämäärät muodossa `VVVV-KK-PP` muutetaan automaattisesti oikeaan muotoon.  
I | Palkkalajikoodi | SalaryCode | number(9) | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideSalaryCode`  
J | Poissaolon alkamispvm | StartDateTime | string(8) | Poissaolon alkamispäivämäärä, muodossa `VVVVKKPP`. Säännössä valitut päivämäärät muodossa `VVVV-KK-PP` muutetaan automaattisesti oikeaan muotoon.  
K | Poissaolon päättymispvm | EndDateTime | string(8) | Poissaolon päättymispäivämäärä, muodossa `VVVVKKPP`. Säännössä valitut päivämäärät muodossa `VVVV-KK-PP` muutetaan automaattisesti oikeaan muotoon.  
L | Työtapaturman sattumispäivä | PopulusAbsenceWorkAccidentDate | string(8) | Työtapaturhman sattumispäivä, muodossa `VVVVKKPP`. Oletuksena tyhjä. Säännössä valitut päivämäärät muodossa `VVVV-KK-PP` muutetaan automaattisesti oikeaan muotoon.  
M | Osapäivän tunnit | CustomData1 | tyhjä | Osapäivän tunnit, oletuksena tyhjä.  
N | 3 päivän koulutusraportille tulevat tunnit | CustomData2 | tyhjä | 3 päivän koulutusraportille tulevat tunnit, oletuksena tyhjä.  
O | Opettajan kokopäivän tunnit | CustomData3 | tyhjä | Kokopäivän tunnit opettajat, Laskennallinen tuntimäärä/pv. Oletuksena tyhjä.  
P | Opettajan todelliset tunnit | CustomData4 | tyhjä | Opettajan todelliset tunnit, oletuksena tyhjä.  
Q | Lapsen syntymäaika | PopulusAbsenceChildBirthDate | string(8) | Lapsen syntymäaika, muodossa `VVVVKKPP`. Oletuksena tyhjä. Säännössä valitut päivämäärät muodossa `VVVV-KK-PP` muutetaan automaattisesti oikeaan muotoon.  
Alla olevat aineistot kuvastavat muokattua poissaoloa. Yhden päivän pituinen poissaolo on muokattu kahden päivän pituiseksi. Edellisestä versiosta luodaan poistorivi ("P") ja uudesta version lisäysrivi ("U").
[code]
    418;P;1234;707;1918;Meikäläinen Matti;;20200102;9090;20250113;20250113;;;;;;
[/code]
[code]
    418;U;1234;707;1918;Meikäläinen Matti;;20200102;9090;20250113;20250114;;;;;;
[/code]
## Liittymän suorittaminen tapahtuman tallentamisen yhteydessä
Alla olevassa esimerkissä on kalenterinäkymässä kopioitu poissaolotapahtuma viidelle päivälle.
![](https://support.nepton.com/hc/article_attachments/25820967933853)
Tallennuksen yhteydessä SFTP-palvelimelle muodostuu jokaisesta tapahtumasta oma tiedosto, jossa on sääntöjoukon muodostama aineisto. Huomaathan, että on tärkeää määrittää tapahtuman nimeen tarkka aikaleima _[timestamp-ms]_ , jotta tiedostot eivät ylikirjoita toisiaan.
![](https://support.nepton.com/hc/article_attachments/25821190558109)
## Liittymän suorittaminen manuaalisesti
Liittymän voi suorittaa manuaalisesti kohdassa **Hallinta > Liittymät > Populus poissaolojen vienti**. Tämä voi olla tarpeellista esimerkiksi silloin, kun halutaan ajaa tietyn aikavälin aineisto kokonaan uudelleen tai poistaa se. 
Rivin ja tiedoston tyyppi on mahdollista valita Merkintä-pudotusvalikosta. Esimerkiksi valinta "Poistettu" luo poistoon tarkoitetun tiedoston, jonka riveillä on poistomerkintä "P".
Alla olevassa esimerkissä käytetään aiemmin luotua poimintasääntöä "Populus poissaolot". Poimintasääntö on pakollinen.
![](https://support.nepton.com/hc/article_attachments/27155299221405)
## Rivityypin ohittaminen poimintasäännössä
Joskus saattaa olla tarpeellista ohittaa "P" tai "U" -rivien muodostuminen, kun käsitellään tiettyjä poissaolotyyppejä. Tätä varten poimintasäännössä voidaan käyttää kolmea eri muuttujaa:
  1. :integrationContext - konteksti, jossa liittymää suoritetaan ("P" tai "U")
  2. :integrationContextForDeletedOrEditedActivities - Rivin "P" muodostus
  3. :integrationContextForNewActivities - Rivin "U" muodostus


Alla oleva esimerkki kuvaa yksinkertaistetusti, kuinka isyysvapaalle muodostetaan ainoastaan lisäysmerkinnät "U", mutta poiston tai muokkauksen yhteydessä ei muodosteta poistomerkintää "P".
[code]
    SELECT *, SUM(Amount) AS OverrideAmount, 
    MIN(SalaryRenderingDate) As OverrideStartDatetime, 
    MAX(SalaryRenderingDate) AS OverrideEndDatetime,
    CASE 
    WHEN AbsenceTypeId = 11 THEN 'KERTAUS' --Kertausharjoitukset
    WHEN AbsenceTypeId = 3 THEN 'ISYYSVAPAA' -- Isyysvapaa
    ELSE
    'MUU VAPAA'
    END AS OverrideSalaryCode
    FROM UserSalaryData 
    WHERE CompensationType = 'BasicTime'
    AND 
    AbsenceTypeId IS NOT NULL 
    AND 
    (AbsenceTypeId != 3 OR :integrationContext != :integrationContextForDeletedOrEditedActivities) -- Lähetä ainostaan U-rivit isyysvapaalle
    GROUP BY ActivityId
[/code]
Kun kalenteriin lisätään uusi isyysvapaa, muodostetaan aineisto, joka sisältää isyysvapaan lisäysmerkinnällä "U". Mikäli isyysvapaata muokataan, muodostetaan uusi aineisto lisäysmerkinnällä "U", mutta edellistä versiota poissaolosta ei muodosteta poistomerkinnällä "P". Mikäli isyysvapaaa poistetaan kokonaan, ei aineistoa muodosteta.
Mikäli kalenteriin lisätään kertausharjoitukset (tai mikä tahansa muu poissaolo), se käsitellään liittymän normaalin toimintatavan mukaisesti.
## Kuluvan päivän poissaolokirjauksen poimintasäännön ehto
Tilanteessa, jossa kuluvalle päivälle kirjataan poissaolo, tietokantatauluun muodostuu tieto "istimeborrowedfrombalance = 'Y'. Tämä aiheuttaa tilanteen, jossa hyväksymätön poissaolo siirtyy aiheettomasti eteenpäin vientipuskuriin ja edelleen Populukseen. Tämän tiedon muodostuminen on tarkoituksenmukaista.   
  
Tästä syystä poissaolojen poimintasääntöön tulee lisätä ehto istimeborrowedfrombalance = 'N', jotta kuluvan päivän poissaolokirjaukset eivät siirry ennenaikaisesti ja aiheettomasti liittymällä ennen niiden hyväksyntää. 
## Ongelmatilanteet
### Poissaolojen lisäys ja poistaminen Populuksesta
Mikäli Populuksesta halutaan kerralla poistaa suurempi määrä sinne vietyjä poissaoloja tietyllä ajanjaksolla, voi sen tehdä suorittamalla liittymän manuaalisesti. Manuaalista liittymän suoritusta voi käyttää samalla tavalla myös poissaolojen lisäämiseen.
### Asetusmuutokset
Palkka-aineistoon vaikuttavia asetusmuutoksia ei ole suositeltavaa tehdä jälkikäteen. Esimerkiksi työpäivän pituuden muuttaminen päiväkohtaisesti kalenterinäkymässä voi muuttaa myös palkallisia poissolopäiviä. Tällaisia muutoksia tehdessä liittymää _ei_ suoriteta ja Populukseen jää sinne mahdollisesti aiemmin viety tieto poissaolojen päivistä. Tällaisessa tilanteessa tulee toimia seuraavasti:
  * Poista Populukseen aiemmin luotu poissaolo.
  * Poista Neptonista nykyinen poissaolo. Tämä lähettää "P" -rivin, jolle ei ole vastinetta Populuksessa.
  * Lisää poissaolo uudelleen. Tämä luo "U" -rivin muodostaen aineiston käyttäen nykyisiä asetuksia.
