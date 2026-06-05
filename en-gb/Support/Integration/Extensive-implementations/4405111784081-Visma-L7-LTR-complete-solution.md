---
id: 4405111784081
title: Visma L7 / LTR complete solution
url: https://support.nepton.com/hc/en-gb/articles/4405111784081-Visma-L7-LTR-complete-solution
locale: en-gb
category: Support
category_id: 360000446658
section: Extensive implementations
section_id: 4405119312657
section_path:
- Integration
- Extensive implementations
labels: []
promoted: false
updated_at: '2024-01-18T11:48:41Z'
edited_at: '2023-05-29T10:18:28Z'
---

# Visma L7 / LTR complete solution

**Sorry!**
This article has not been translated yet.
## Kokonaisratkaisu
Nepton ja Visma ovat yhdessä toteuttaneet kokonaisratkaisun Visma L7 asiakkaille. Kokonaisratkaisussa liittymät ovat suunniteltu ja toteutettu siten, että ne tuovat asiakkaille suurimman mahdollisen arvon kummankin palvelun käyttöön.
Nepton ja Visma L7 kokonaisratkaisulla on mahdollista toteuttaa seuraava toiminnallisuus. Tästä kokonaisratkaisusta voidaan ottaa yksi tai useampia liittymiä käyttöön.
Liittymien tekninen toteutus on käynnissä ja niiden käyttöönotto voidaan tehdä liittymien valmistuttua.
Liittymiä suunniteltaessa on tärkeää huomioida asiakaskohtaiset käyttötavat palveluiden määrittelyssä. Seurantakohteiden rakenne voi vaihdella asiakkaittain riippuen siitä onko käytössä kustannuspaikat, työn kohdistaminen tai litterat. Palkan perusteiden muodostumisessa voi olla paikallisia sopimuksia tai käytäntöjä, jotka määritellään Neptonissa.
## Käyttötavat
Liittymien käyttöön on kaksi tapaa, jotka ovat kuvattu alla. Asiakkaalle valitaan käyttöön yksi käyttötapa. Käyttötapoja ei voi sekoittaa. Sopiva käyttötapa valitaan yhdessä asiakkaan kanssa siten, että se mahdollistaa asiakkaalle mahdollisimman sujuvan käytön. Esimerkiksi, jos LTR:ssä tehdään materiaalihallintaa, niin sujuvin käyttötapa on kirjata kaikki tiedot LTR-ratkaisuun. Muussa tapauksessa voi olla sujuvinta kirjata kaikki tapahtumat Neptonissa, josta ne siirretään LTR:n kautta L7 maksettavaksi.
### 1) Kaikki työ- ja palkkatapahtumat kirjataan LTR:aan ja tulkitaan Neptonissa
Kaikki työtapahtumat kirjataan LTR-palveluun ja siirretään Neptoniin tulkittaviksi. LTR siirtää hyväksytyt tapahtumat, ja tällöin tapahtumia ei muokata tai lisätä Neptonissa. LTR hakee tulkinnan tuloksen takaisin LTR-palveluun, josta tapahtumat viedään L7:aan palkanmaksua, raportointia ja laskutusta varten.
Tässä käyttötavassa aktivoidaan seuraavat liittymät:
  1. Nepton hakee ajastuksella kerran yössä L7:n REST - rajapinnasta työkohteeet. Liittymä määritellään Neptonissa. Littymän määrittämisestä voit lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/360003751058>).
  2. Kun palkkajakson kirjaukset ovat tehty ja hyväksytty, niin liittymä määritellään Neptonissa. 
     * **Suositeltu tapa** : Nepton lähettää aineiston LTR:ään LTR REST - rajapinnan kautta. Liittymä määritellään Neptonissa. Liittymän määrittämisestä voit lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/11166111654685>).
     * **Vanhentunut tapa** : LTR:ssä aktivoidaan tapahtumien siirto Neptoniin ja Nepton lähettää aineiston LTR:ään LTR REST - rajapinnan kautta. Liittymä määritellään Neptonissa. Liittymän määrittämisestä voit lukea lisää täältä. (linkki)LTR hakee Neptonissa tulkitut työtapahtumat L7 laskutusta ja palkanmaksua varten. Aineisto haetaan Neptonin APIsta. Aineistonoutoa varten muodostetaan poiminnan sääntöjoukko, jonka mukainen aineisto siirretään. Aineisto haetaan RunIntegrationRulesetV2 - metodilla. Aineiston teknisenä muotona käytetään Mepco - palkkatapahtuma muotoa. Sarakkeeseen 18 tulee poimia alkupäivämäärä, sarakkeeseen 19 loppupäivämäärä, sarakkeeseen 20 tapatuman tunniste. Poimintasäännössä nämä sarakkeet määritellään poimintasäännön SELECT osassa näin: "SELECT  
*, SUM(Amount) As OverrideAmount,  
MIN (StartDateTime) AS CustomData1,  
MAX(EndDateTime) AS CustomData2,  
MIN(ActivityId) AS CustomData3"


### 2) Kaikki työ- ja palkkatapahtumat kirjataan Neptoniin ja tulkinta siirretään maksettavaksi LTR:aan
Kaikki työ- ja palkkatapahtumat kirjataan Neptoniin. Nepton siirtää tulkitut tapahtumat LTR:n REST rajapintaan palkanmaksua, raportointia ja laskutusta varten. Tämä siirto aktivoidaan asiakkaan toimesta silloin, kun palkkajakson tiedot ovat syötetty, hyväksytty ja valmiina palkanmaksuun. Tässä käyttötavassa tapahtumia ei tuoda LTR - palvelusta Neptoniin.
Tässä käyttötavassa aktivoidaan seuraavat liittymät:
  1. Nepton hakee ajastuksella kerran yössä L7:n REST - rajapinnasta työkohteeet. Liittymä määritellään Neptonissa. Littymän määrittämisestä voit lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/360003751058>).
  2. Kun palkkajakson kirjaukset ovat tehty ja hyväksytty, niin Neptonista siirretään tulkinta LTR:n REST - rajapintaan. Siirto käynnistetään Neptonissa, ja valitun ajanjakson mukainen tulkinta siirtyy LTR:n käsiteltäväksi. 
     * Siirto muodostaa aineiston sen sääntöjoukon mukaisena, joka on valittu siirrettäväksi.


## Tekniset vaatimukset
Asiakkaalla tulee olla käytössään LTR-työtapahtumat ja siihen liittyvät REST - rajapinnan lisenssit. Tiedostopohjaisia palkka- tai työajantulkinnan siirtoja ei tueta uusissa toteutuksissa Visma L7 järjestelmään. Visma L7/LTR REST - rajapinnasta voi lukea lisää [täältä](<https://community.visma.com/t5/Visma-L7-kayttovinkit/Visma-L7-REST-API-rajapinnat-ja-integraatiot/ta-p/357158>).
