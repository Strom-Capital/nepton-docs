---
id: 38337017039645
title: Reaaliaikainen mukautettu Työajan vienti
url: https://support.nepton.com/hc/fi/articles/38337017039645-Reaaliaikainen-mukautettu-Ty%C3%B6ajan-vienti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä liittymistä
section_id: 360002325398
section_path:
- Liittymät
- Yleistä liittymistä
labels: []
promoted: false
updated_at: '2026-11-11T09:58:59Z'
edited_at: '2026-11-11T09:58:59Z'
---

# Reaaliaikainen mukautettu Työajan vienti

Samaan tapaan kuin Mepcon poissaolo- ja vuosilomaliittymä sekä Populuksen poissaololiittymä, myös mukautettu Työajan vienti voidaan toteuttaa reaaliaikaisena. Merkittävin ero näiden reaaliaikaisten Populus- ja Mepco-liittymien ja reaaliaikaisen mukautetun Työajan viennin välillä on se, että mukautetun Työajan vienti tukee myös muun tapahtumatiedon kuin poissaolojen ja/tai vuosilomien vientiä. Tällainen muu tapahtumatieto voi olla esimerkiksi tapahtumien projektitieto tai työtapahtumien aikaleimat. Lisäksi mukautetussa Työajan viennissä vientiaineiston tietueet (aineiston sarakkeet) määritetään aina erikseen tarpeen mukaisiksi, verrattuna Mepco- ja Populus-toteutuksiin, jossa tietueet ovat aina ko. järjestelmien mukaiset.
Reaaliaikaista mukautettua Työajan vientiä ei ole suunniteltu eikä se sovellu palkka-aineistoliittymän toteutukseen, sillä palkkatiedon muodostava tulkinta ei välttämättä ole Neptonissa reaaliaikaista.
Reaaliaikainen mukautettu Työajan vienti vaatii aina integraation sääntöjoukon. Sääntöjoukon poimintasääntöjen poimimat tapahtumat lisätään vientipuskuriin reaaliajassa, kun ne tallennetaan Neptonissa tai vaihtoehtoisesti vasta niiden hyväksynnän yhteydessä. Vientipuskurissa olevat tiedot siirretään valitulla aikavälillä vastajärjestelmään Neptonissa määritettävän ajastuksen avulla. Liittymä käyttää poisto- ja lisäysmerkintöjä ("P" ja "U"). Neptonissa jo olevaa tapahtumaa muokattaessa lähetetään molemmat.
## Hyvä tietää
  * Työntekijät henkilönumerolla 0 eivät tule osaksi aineistoa.
  * Mikäli tapahtuma aloitetaan kalenterissa ilman lopetusaikaa, liittymä käsittelee sen ja siirtää tapahtuman vientipuskuriin (vrt. reaaliaikainen Mepco- ja Populus-liittymä, jossa liittymä käynnistyy vasta, kun tapahtumalle määrittyy lopetusaika ja poimintasäännön ehdot täyttyvät).
  * Tapahtuman tallennuksen yhteydessä käsitellään vain kyseinen tapahtuma ja se viedään puskurille odottamaan ajastusta, joka siirtää tapahtuma-aineiston SFTP-palvelimelle. Muut saman päivän tapahtumat eivät tule osaksi aineistoa.
  * Tapahtuma siirretään ainoastaan, jos se on uusi, poistettu tai siihen on tehty sellainen muutos, joka koskee aineistossa siirrettävää tietoa. Siirrettävä tieto määräytyy sen mukaan, mitä mukautetun työajan viennin asetuksissa on määritetty siirrettäväksi.
  * **Mikäli halutaan siirtää tapahtumat vasta hyväksyttyinä, niin poimintasääntöön tulee lisätä isApproved = 'Y'**
  * Tapahtuman voi tallentaa vaikka liittymän suorittamisessa ilmenisi ongelmia. Esim. virheellinen poimintasääntö tai ongelma SFTP-palvelimella ei estä tapahtuman tallentamista. Virheestä annetaan käyttäjälle varoitus.
  * Jos poimintasääntöä muutetaan, niin muutos tulee asettaa voimaan myös takautuvasti sille ajanjaksolle, jolle mahdollisesti tehdään vielä muutoksia tapahtumakirjauksiin.
  * Mikäli sama tapahtuma muodostaa aineistoa kahden tai useamman eri sääntöjoukon poimintasäännön perusteella, kustakin sääntöjoukosta luodaan oma tiedostonsa.
  * Poistettu tapahtuma tai muokatun tapahtuman edellinen versio muodostuu aineistolle poistomerkinnällä "P".
  * Uusi tapahtuma tai muokatun tapahtuman viimeisin versio muodostuu aineistolle lisäysmerkinnällä "U".
  * Tapahtuman muokkaus muodostaa kaksi riviä. Ensimmäisellä rivillä on tapahtuman ennen muokkausta ollut versio tunnisteella ”P”. Jälkimmäisellä rivillä on tapahtuman päivitetty versio tunnisteella “U".
  * Liittymää varten on mahdollista määritellä useampi sääntöjoukko. Mikäli liittymälle on määritelty useita sääntöjoukkoja, tapahtuman tallennus voi kestää hieman kauemmin.
  * Mikäli tapahtumia poistetaan henkilön kalenterista massatoimintojen kautta, muodostuvat poistettavat rivit yhteen tiedostoon, vaikka tapahtumia olisi useampi. Tapahtumia kopioidessa jokaista tapahtumaa kohden muodostuu oma tiedosto.


## Määrittäminen
### **Henkilöiden tunnisteiden määrittäminen**
Henkilötunnisteet voidaan määrittää kohdassa **Työsuhde > Henkilön tiedot > Tunnisteet**. Henkilöllä tulee olla henkilönumero, jotta tämän tapahtumat tulevat osaksi aineistoa.
![](https://support.nepton.com/hc/article_attachments/38337849465757)
### **Kohdepalvelimen lisäys**
Jos liittymälle ei vielä ole kohdepalvelinta, lisää se työyhteisön asetuksista kohdasta **Liittymät > Liittymien kohdepalvelimet**. Katso [Työajan vientiliittymien kohdepalvelimet](<https://support.nepton.com/hc/fi/articles/26861716054045>) yleiset ohjeet kohdepalvelimen lisäykseen ja kohdepalvelimen SFTP-asetuksien asetukseen.
Kohdepalvelimen SFTP-asetuksissa tulee määrittää vähintään _SFTP-palvelimen osoite, SFTP-käyttäjätunnus_ sekä _SFTP-salasana_(tai public key -autentikointi).
### **Liittymän asetukset**
Liittymän käyttöönottoa varten tulee määrittää [sääntöjoukko](<https://support.nepton.com/hc/fi/articles/360002492278>), jolla muodostetaan liittymäaineisto. Sääntöjoukon asetuksissa Viennin asetukset-osion alta valitaan viennin tiedostomuodoksi _Mukautettu vienti käyttämällä vientipuskuria (csv) tai Mukautettu vienti käyttämällä vientipuskuria (xml).![](https://support.nepton.com/hc/article_attachments/38337849466525)_
Määritä mukautetun viennin aineiston tietueet "Mukautettu vienti" -taulukon rakenne-osiossa sekä "Mukautettu vienti" - CSV muotoilu-osiossa. Tarkemmat ohjeet mukautetun viennin toteutukseen ohjeartikkelissa [Mukautetut Työajan viennit.](<https://support.nepton.com/hc/fi/articles/10758741671581-Mukautetut-Ty%C3%B6ajan-viennit>)
Valitse liittymälle kohdepalvelin, jonka lisäsit kohdassa 2.
![](https://support.nepton.com/hc/article_attachments/38337017032861)
Määritä vientitiedoston nimi. Vientiedoston nimeen tulee lisätä aikaleima, kuten alla olevassa esimerkissä. Vientiedoston nimestä ja aikaleiman käytöstä kerrrotaan tarkemmin seuraavassa osiossa.
![](https://support.nepton.com/hc/article_attachments/38337017033885)
### Vientitiedoston nimi ja aikaleima
**Vientitiedoston nimi-asetukseen,** eli**** aineiston nimeen on tärkeää määrittää aikaleima, jotta tiedosto siirtyessään ajastetusti vientipuskurilta kohdepalvelimelle (SFTP-palvelimelle) ei ylikirjoita palvelimella mahdollisesti jo olevaa aiempaa tiedostoa. Alla muutamia esimerkkejä vientiedoston nimestä, aikaleimasta ja sen suhteesta Neptonissa olevaan ajastukseen:
  * **poissaolot_[vvvvkkpp].csv**
    * Henkilöiden kirjaamat tapahtumat tallentuvat vientipuskuriin**yhdeksi tiedostoksi päivätasolla** ja ne siirretään **yhdessä tiedostossa** Neptonin ajastuksen myötä vientipuskurilta eteenpäin kohdepalvelimelle.
    * Neptonissa olevan ajastuksen esimerkki: Vienti kerran päivässä tai harvemmin
  * **poissaolot_[vvvvkkpphh].csv**
    * Henkilöiden kirjaamat tapahtumat tallentuvat vientipuskuriin **useammaksi tiedostoksi** **tuntitasolla** ja tiedostot siirretään vientipuskurilta Nepton ajastuksen avulla edelleen kohdepalvelimelle.
    * Neptonissa olevan ajastuksen esimerkki: Vienti kerran tunnissa tai harvemmin/useammin
  * **poissaolot_[vvvvkkpphhmm].csv**
    * Henkilöiden kirjaamat tapahtumat tallentuvat vientipuskuriin **useammaksi tiedostoksi** **minuuttitasolla** ja tiedostot siirretään vientipuskurilta Nepton ajastuksen avulla edelleen kohdepalvelimelle.
    * Neptonissa olevan ajastuksen esimerkki: Vienti joka 15 minuutti (pienin tuettu aikaväli) tai harvemmin
  * **poissaolot_[vvvvkkpphhmmss].csv**
    * Henkilöiden kirjaamat tapahtumat tallentuvat vientipuskuriin **useammaksi tiedostoksi** **sekuntitasolla** ja tiedostot siirretään vientipuskurilta Nepton ajastuksen avulla edelleen kohdepalvelimelle.
    * Neptonissa olevan ajastuksen esimerkki: Vienti joka 15 minuutti (pienin tuettu aikaväli) tai harvemmin
  * **poissaolot_[timestamp-ms].csv.**
    * Henkilöiden kirjaamat tapahtumat tallentuvat vientipuskuriin omiksi**tiedostoikseen** **millisekuntitasolla** ja tiedostot siirretään vientipuskurilta Nepton ajastuksen avulla edelleen kohdepalvelimelle.
    * Neptonissa olevan ajastuksen esimerkki: Vienti joka 15 minuutti (pienin tuettu aikaväli) tai harvemmin


Se, mikä aikaleima palvelee parhaiten mitäkin toteutusta ei ole yksiselitteistä vaan riippuu liittymällä siirrettävän tiedon luonteesta sekä siitä, kuinka usein vastajärjestelmän puolella tätä tieto tulee rikastaa.
### Vientitiedoston osiin jakaminen
Liittymien sääntöjoukon asetuksissa Vientitiedoston osiin jakaminen -osiossa olevia asetuksia ei yleensä käytetä reaaliaikaisessa viennissä, sillä tiedoston osiin jakamiseen vaikuttaa se, miten tieto ryhmitellään, kun se siirretään puskurista palvelimelle. Neptoniin kirjatut tapahtumat siirtyvät puskuriin sääntöjoukoon poimintasääntöjen ehdoilla reaaliajassa.   
  
Jos aikaleimaperusteisen tiedostojaon lisäksi halutaan käyttää myös asetuksia “vientitiedoston osiin jakaminen” -osiossa, on kuitenkin mahdollista määrittää tiedoston jakaminen lisäksi jollain muulla perusteella, esimerkiksi maksuryhmätiedolla.  
  
Tässä on huomioitava, että jokainen yksittäinen reaaliaikainen siirto poimii hyvin pienen määrän dataa. Useimmilla ryhmittelyperusteilla tämä pieni datamäärä ei enää jakaudu pienempiin osiin, vaan siirrosta muodostuu edelleenkin vain yksi tiedosto. Tiedoston nimeen liitettäisiin kuitenkin määritetty ryhmittelyperuste (esim. maksuryhmä). Tätä määritystä noudettaisiin myös manuaalisesti käynnistetyissä siirroissa, joissa todennäköisesti muodostuisi useampi tiedosto suuremman datamäärän vuoksi.
![](https://support.nepton.com/hc/article_attachments/38337002882461)
### **Viennin ajastus kohdepalvelimelle**
Viimeisenä kohdepalvelimen vientipuskurille tarvitsee määrittää viennin ajastus. Tästä voit lukea lisää artikkelista [Työajan vientiliittymien kohdepalvelimet.](<https://support.nepton.com/hc/fi/articles/26861716054045-Ty%C3%B6ajan-liittymien-kohdepalvelimet#h_01JSK5VK4NMRKM5R7TP1B6ATE1>)
## Liittymän suorittaminen manuaalisesti
Liittymän voi suorittaa manuaalisesti kohdassa **Hallinta > Liittymät > Mukautettu vienti käyttämällä vientipuskuria**. Tämä voi olla tarpeellista esimerkiksi silloin, kun halutaan ajaa tietyn aikavälin aineisto kokonaan uudelleen tai poistaa se.
Rivin tyyppi on mahdollista valita Merkintä-pudotusvalikosta. Esimerkiksi valinta "Poistettu" luo rivejä poistomerkinnällä "P".
Alla olevassa esimerkissä käytetään aiemmin luotua poimintasääntöä "Poissaolot järjestelmään X (reaaliaikainen)". Poimintasääntö on pakollinen.
Huom! Aineiston voi ajaa maksimissaan vain kolmen kuukauden ajalta.  
  
![](https://support.nepton.com/hc/article_attachments/38337861455517)
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
## Sairauspoissaolokirjauksen poimintasäännön ehto
Kun kirjataan kuluvan päivän tai osapäivän sairauspoissaolo, tietokantatauluun muodostuu kaksi erillistä basictime riviä, joista toisella on tieto "istimeborrowedfrombalance = 'Y'" ja "isapproved = 'Y'". Tämä aiheuttaa tilanteen, jossa hyväksymätön sairauspoissaolo siirtyy aiheettomasti eteenpäin vientipuskuriin ja edelleen vastajärjestelmään. Tilanne voi syntyä osapäivän sairauspoissaoloille sekä sairauspoissaoloille, jotka kirjataan kuluvalle päivälle ilman loppumisaikaa.
Tästä syystä osapäivän sairauspoissaolojen poimintasääntöön tulee lisätä ehto istimeborrowedfrombalance = 'N', jotta kuluvan päivän tai osapäivän sairauspoissaolokirjaukset eivät siirry ennenaikaisesti ja aiheettomasti liittymällä ennen niiden hyväksyntää. 
## Ongelmatilanteet
### Tapahtumien lisäys ja poistaminen vastajärjestelmästä
Mikäli vastajärjestelmästä halutaan kerralla poistaa suurempi määrä sinne vietyjä tapahtumia tietyllä ajanjaksolla, voi sen tehdä suorittamalla liittymän manuaalisesti. Manuaalista liittymän suoritusta voi käyttää samalla tavalla myös tapahtumien lisäämiseen.
### Asetusmuutokset
Palkka-aineistoon vaikuttavia asetusmuutoksia ei ole suositeltavaa tehdä jälkikäteen. Esimerkiksi työpäivän pituuden muuttaminen päiväkohtaisesti kalenterinäkymässä voi muuttaa myös palkallisia tunteja. Tällaisia muutoksia tehdessä liittymää  _ei_ suoriteta ja vastajärjestelmään jää sinne mahdollisesti aiemmin viety tieto poissaolon palkallisesta kestosta. Tällaisessa tilanteessa tulee toimia seuraavasti:
  * Poista vastajärjestelmästä aiemmin luotu tapahtuma.
  * Poista Neptonista nykyinen tapahtuma. Tämä lähettää "P" -rivin, jolle ei ole vastinetta vastajärjestelmässä.
  * Lisää tapahtuma uudelleen. Tämä luo "U" -rivin muodostaen aineiston käyttäen nykyisiä asetuksia.
