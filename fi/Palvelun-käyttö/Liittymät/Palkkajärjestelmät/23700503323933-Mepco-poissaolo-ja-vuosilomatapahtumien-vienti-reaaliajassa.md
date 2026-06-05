---
id: 23700503323933
title: Mepco poissaolo- ja vuosilomatapahtumien vienti reaaliajassa
url: https://support.nepton.com/hc/fi/articles/23700503323933-Mepco-poissaolo-ja-vuosilomatapahtumien-vienti-reaaliajassa
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
updated_at: '2026-01-15T08:24:24Z'
edited_at: '2026-01-15T08:24:24Z'
---

# Mepco poissaolo- ja vuosilomatapahtumien vienti reaaliajassa

Accountor Mepco HRM poissaolojen vienti -liittymällä poissaolot lisätään vientipuskuriin reaaliajassa kun ne tallennetaan Neptonissa. Puskurissa olevat tiedot siirretään valitulla aikavälillä Mepcoon. Liittymä käyttää Mepcon poisto- ja lisäysmerkintöjä ("P" ja "U"). Poissaoloa muokattaessa lähetetään molemmat.
## Hyvä tietää
  * Työntekijät henkilönumerolla 0 eivät tule osaksi aineistoa.
  * Liittymä käsittelee ainoastaan poissaoloja. Huomaathan tämän, kun teet poimintasääntöä. Esim. työtapahtumia ei käsitellä mutta tapahtumatyyppi, jonka käyttäytymiseksi on valittu "poissaolo", otetaan mukaan (liittymä käsittelee siis tapahtumia, joiden activitytypecategoryid = '2').
  * Mikäli poissaolotapahtuma aloitetaan kalenterissa ilman lopetusaikaa, liittymä ei käsittele sitä. Liittymä käsittelee poissaolotapahtuman, kun se lopetetaan ja sille määrittyy lopetusaika.
  * Poissaolotapahtuman tallennuksen yhteydessä käsitellään vain kyseinen poissaolotapahtuma ja se viedään SFTP-palvelimelle. Muut saman päivän tapahtumat eivät tule osaksi aineistoa.
  * Poissaolotapahtuma siirretään ainoastaan, jos se on uusi, poistettu tai siihen on tehty sellainen muutos, joka koskee aineistossa siirrettävää tietoa. Tarkista aineiston tietueet -kohdasta alta, mitkä tiedot siirretään. Esimerkiksi kommentin lisääminen poissaolotapahtumaan ei muodosta uutta aineistoa eikä jo lähetetyn tapahtuman hyväksyminen.
  * **Mikäli halutaan siirtää tapahtumat vasta hyväksyttyinä, niin poimintasääntöön tulee lisätä isApproved = 'Y'**  

  * Poissaolotapahtuman voi tallentaa vaikka liittymän suorittamisessa ilmenisi ongelmia. Esim. virheellinen poimintasääntö tai ongelma SFTP-palvelimella ei estä poissaolotapahtuman tallentamista. Virheestä annetaan käyttäjälle varoitus.
  * Jokaista poissaolotapahtumaa ja sääntöjoukkoa kohden muodostetaan oma tiedosto, joka siirretään SFTP-palvelimelle. Mikäli sama poissaolotapahtuma muodostaa aineistoa kahdessa eri sääntöjoukossa, luodaan kaksi eri tiedostoa.
  * Poistettu poissaolotapahtuma tai muokatun poissaolotapahtuman edellinen versio muodostuu aineistolle poistomerkinnällä "P".
  * Uusi tapahtuma tai muokatun poissaolotapahtuman viimeisin versio muodostuu aineistolle lisäysmerkinnällä "U".
  * Poissaolotapahtuman muokkaus muodostaa kaksi riviä. Ensimmäisellä rivillä on poissaolon ennen muokkausta ollut versio tunnisteella ”P”. Jälkimmäisellä rivillä on poissaolon päivitetty versio tunnisteella “U".
  * Liittymää varten on mahdollista määritellä useampi sääntöjoukko. Mikäli liittymälle on määritelty useita sääntöjoukkoja, tapahtuman tallennus voi kestää hieman kauemmin.
  * Mikäli poissaolotapahtumia poistetaan henkilön kalenterista massatoimintojen kautta, muodostuvat poistettavat rivit yhteen tiedostoon, vaikka poissaolotapahtumia olisi useampi. Poissaolotapahtumia kopioidessa jokaista tapahtumaa kohden muodostuu oma tiedosto.


## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilötunnisteet voidaan määrittää kohdassa **Työsuhde > Henkilön tiedot > Tunnisteet**.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/23700503320093)
Mikäli henkilön Mepco-tunnusta ei ole asetettu, käytetään henkilönumeroa.
**2\. Kohdepalvelimen lisäys**
Jos liittymälle ei vielä ole kohdepalvelinta, lisää se työyhteisön asetuksista kohdasta **Liittymät > Liittymien kohdepalvelimet**. Katso [Työajan vientiliittymien kohdepalvelimet](<https://support.nepton.com/hc/fi/articles/26861716054045>) yleiset ohjeet kohdepalvelimen lisäykseen ja kohdepalvelimen SFTP-asetuksien asetukseen.
Kohdepalvelimen SFTP-asetuksissa tulee määrittää vähintään _SFTP-palvelimen osoite, SFTP-käyttäjätunnus_ sekä _SFTP-salasana_(tai public key -autentikointi).
**3\. Liittymän asetukset**
Liittymän käyttöönottoa varten tulee määrittää [sääntöjoukko](<https://support.nepton.com/hc/fi/articles/360002492278>), jolla muodostetaan poissaoloaineisto. Sääntöjoukon asetuksissa valitaan viennin tiedostomuodoksi _Accountor Mepco poissaolojen vienti (Poissaolo)_ tai _Accountor Mepco poissaolojen vienti (Vuosiloma)_. ![](https://support.nepton.com/hc/article_attachments/23701485589149)
Valitse liittymälle kohdepalvelin, jonka lisäsit kohdassa 2.
![](https://support.nepton.com/hc/article_attachments/27214544554781)
Vientitiedoston nimeen tulee lisätä tarkka aikaleima _[timestamp-ms]_ , kuten alla olevassa esimerkissä. Mikäli aikaleimaa ei käytetä, jokaisella tiedostolla on sama nimi ja ne ylikirjoittavat toisensa.
![](https://support.nepton.com/hc/article_attachments/27214568098077)
Osio **Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Accountor Mepco HRM poissaolojen vienti **sisältää tulosten sisältöön liittyvät asetukset, jotka on kuvattu [täällä](<https://support.nepton.com/hc/fi/articles/360003473498-Mepco-palkkatapahtumat#Tiedostomuoto>).
![](https://support.nepton.com/hc/article_attachments/24641083700765)
Päivämäärän muoto tulee tarkistaa Mepcon puolelta ja asettaa oikeaan muotoon asetukseen "Päivämäärän muoto". 
**4\. Viennin ajastus kohdepalvelimelle**
Viimeisenä kohdepalvelimen puskurille tarvitsee määrittää viennin ajastus. Tästä voit lukea lisää artikkelista [Työajan vientiliittymien kohdepalvelimet](<https://support.nepton.com/hc/fi/articles/26861716054045#h_01JSK5VK4NMRKM5R7TP1B6ATE1>).
## Tiedostomuoto
Siirtotiedosto on UTF-8 muotoista puolipisteellä (`;`) eroteltua tekstimuotoista dataa. Kenttien pituuksille ei ole määritelty ylärajaa. Mepcoon määritellään tiedoston luentaan tätä aineistoa vastaavat sarakkeet ja käsittelysäännöt.
Tiedonsiirto on mahdollista ottaa käyttöön myös vain yhdellä projektikohdenteella.
## Aineiston tietueet
Sarake | Kenttä | Sääntöjoukon kentän nimi | Muoto | Kuvaus  
---|---|---|---|---  
A | Henkilönumero | _Lisätään automaattisesti, ei korvattavissa_ | string | Henkilön Mepco-tunnus / henkilönumero.  
B | Poissaolon alkamispvm | StartDateTime | date | Poissaolon alkamispäivämäärä.  
C | Poissaolon päättymispvm | EndDateTime | date | Poissaolon päättymispäivämäärä.   
D | Henkilön nimi | _Lisätään automaattisesti, ei korvattavissa_ | string | Henkilön suku- ja etunimet  
E | Projektikoodi 1 | ProjectCode1 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode1`  
F | Projektikoodi 2 | ProjectCode2 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode2`  
G | Projektikoodi 3 | ProjectCode3 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode3`  
H | Projektikoodi 4 | ProjectCode4 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode4`  
I | Projektikoodi 5 | ProjectCode5 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode5`  
J | Palkkalajikoodi | SalaryCode | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideSalaryCode`  
K | Määrä | Amount | decimal | Poissaolon pituus, voidaan esittää tunteina tai päivinä. Desimaalierottimena on piste (`.`)  
L | Rivin tyyppi | _Lisätään automaattisesti, ei korvattavissa_ | string |  Määrittää, onko tieto Mepcosta poistettava vai Mepcoon lisättävä. Poisto: `P` Lisäys: `U`  
Alla oleva aineisto kuvastaa muokattua poissaoloa. 6 tunnin pituinen poissaolo on muokattu 8 tunnin pituiseksi. Edellisestä versiosta luodaan poistorivi ("P") ja uudesta version lisäysrivi ("U").
[code]
    1918;2024-12-12;2024-12-12;Meikäläinen Matti;1001;;;;;123;6.00;P
    1918;2024-12-12;2024-12-12;Meikäläinen Matti;1001;;;;;123;8.00;U
[/code]
## Liittymän suorittaminen tapahtuman tallentamisen tai hyväksynnän yhteydessä
Alla olevassa esimerkissä on kalenterinäkymässä kopioitu poissaolotapahtuma viidelle päivälle. 
![](https://support.nepton.com/hc/article_attachments/24641100378909)
Tallennuksen tai hyväksynnän yhteydessä siirtopuskuriin muodostuu jokaisesta tapahtumasta oma tiedosto, jossa on sääntöjoukon muodostama aineisto. Se muodostuuko tapahtumasta tiedosto siirtopuskuriin vasta hyväksynnän vai jo sen tallennuksen jälkeen, riippuu siitä miten poiminta on määritetty (sisältääkö IsApproved = 'Y' tiedon vai ei).   
  
Siirtopuskuriin muodostuneet tiedostot siirretään siirtopuskurista eteenpäin kohdepalvelimelle Neptoniin tehtävän liittymän ajastuksen myötä (ks. tämän ohjeen osio "Määrittäminen", kohta 4).
  
Huomaathan, että on tärkeää määrittää sääntöjoukon asetuksissa asetukseen **Vientitiedoston nim** i aineiston nimeen tarkka aikaleima, jotta tiedostot siirtyessään SFTP-palvelimelle eivät ylikirjoita toisiaan (esim. Lomat_[vvvvkkpphhmmss].csv tai Lomat_[timestamp-ms].csv.   
  

![](https://support.nepton.com/hc/article_attachments/24641100381469)
## Liittymän suorittaminen manuaalisesti
Liittymän voi suorittaa manuaalisesti kohdassa **Hallinta > Liittymät > Accountor Mepco HRM poissaolojen vienti**. Tämä voi olla tarpeellista esimerkiksi silloin, kun halutaan ajaa tietyn aikavälin aineisto kokonaan uudelleen tai poistaa se.
Rivin tyyppi on mahdollista valita Merkintä-pudotusvalikosta. Esimerkiksi valinta "Poistettu" luo rivejä poistomerkinnällä "P".
Alla olevassa esimerkissä käytetään aiemmin luotua poimintasääntöä "Mepco poissaolot". Poimintasääntö on pakollinen.  
  
![](https://support.nepton.com/hc/article_attachments/27214568099741)
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
    WHEN AbsenceTypeId = 11 THEN 'KERTAUS' -- Kertausharjoitukset
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
    AND isApproved = 'Y' -- Lähetä ainoastaan hyväksytyt tapahtumat
    GROUP BY ActivityId
[/code]
Kun kalenteriin lisätään uusi isyysvapaa, muodostetaan aineisto, joka sisältää isyysvapaan lisäysmerkinnällä "U". Mikäli isyysvapaata muokataan, muodostetaan uusi aineisto lisäysmerkinnällä "U", mutta edellistä versiota poissaolosta ei muodosteta poistomerkinnällä "P". Mikäli isyysvapaaa poistetaan kokonaan, ei aineistoa muodosteta.
Mikäli kalenteriin lisätään kertausharjoitukset (tai mikä tahansa muu poissaolo), se käsitellään liittymän normaalin toimintatavan mukaisesti.
## Kuluvan päivän poissaolokirjauksen poimintasäännön ehto
Tilanteessa, jossa kuluvalle päivälle kirjataan poissaolo, tietokantatauluun muodostuu tieto "istimeborrowedfrombalance = 'Y'. Tämä aiheuttaa tilanteen, jossa hyväksymätön poissaolo siirtyy aiheettomasti eteenpäin vientipuskuriin ja edelleen Mepcoon. Tämän tiedon muodostuminen on tarkoituksenmukaista.   
  
Tästä syystä poissaolojen poimintasääntöön tulee lisätä ehto istimeborrowedfrombalance = 'N', jotta kuluvan päivän poissaolokirjaukset eivät siirry ennenaikaisesti ja aiheettomasti liittymällä ennen niiden hyväksyntää. 
## Ongelmatilanteet
### Poissaolojen lisäys ja poistaminen Mepcosta
Mikäli Mepcosta halutaan kerralla poistaa suurempi määrä sinne vietyjä poissaoloja tietyllä ajanjaksolla, voi sen tehdä suorittamalla liittymän [manuaalisesti](<https://support.nepton.com/hc/fi/articles/23700503323933-Mepco-poissaolojen-vienti-tapahtuman-muokkauksen-yhteydess%C3%A4#h_01JEZV3MKT3MS9JX1BJPYZT8N2>). Manuaalista liittymän suoritusta voi käyttää samalla tavalla myös poissaolojen lisäämiseen.
### Asetusmuutokset
Palkka-aineistoon vaikuttavia asetusmuutoksia ei ole suositeltavaa tehdä jälkikäteen. Esimerkiksi työpäivän pituuden muuttaminen päiväkohtaisesti kalenterinäkymässä voi muuttaa myös palkallisia tunteja. Tällaisia muutoksia tehdessä liittymää  _ei_ suoriteta ja Mepcoon jää sinne mahdollisesti aiemmin viety tieto poissaolon palkallisesta kestosta. Tällaisessa tilanteessa tulee toimia seuraavasti:
  * Poista Mepcosta aiemmin luotu poissaolo.
  * Poista Neptonista nykyinen poissaolo. Tämä lähettää "P" -rivin, jolle ei ole vastinetta Mepcossa.
  * Lisää poissaolo uudelleen. Tämä luo "U" -rivin muodostaen aineiston käyttäen nykyisiä asetuksia.
