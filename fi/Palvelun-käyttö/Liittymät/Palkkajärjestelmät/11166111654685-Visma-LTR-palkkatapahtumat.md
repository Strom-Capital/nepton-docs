---
id: 11166111654685
title: Visma LTR palkkatapahtumat
url: https://support.nepton.com/hc/fi/articles/11166111654685-Visma-LTR-palkkatapahtumat
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
updated_at: '2025-06-18T08:12:32Z'
edited_at: '2025-06-18T08:11:53Z'
---

# Visma LTR palkkatapahtumat

Palvelusta voidaan viedä palkkatapahtumia Visma LTR -järjestelmään. Viennissä käytetään Visman tarjoamaa REST-rajapintaa.
## Vaatimukset
  * [Projektikohdistuksen tulee olla käytössä Neptonissa](<https://support.nepton.com/hc/fi/articles/4409389747601>).
  * Jotta palkkatapahtumia voidaan viedä Visma LTR -järjestelmään REST-rajapinnan kautta, on Neptonin projektirakenteen oltava identtinen Visma L7:n projektirakenteen kanssa ja siksi on suositeltavaa tuoda projektit Visma L7:stä Neptoniin. Lue lisää [Visma L7 / LTR kokonaisratkaisusta](<https://support.nepton.com/hc/fi/articles/4405111784081>) ja [Visma L7 projektien tuonnista](<https://support.nepton.com/hc/fi/articles/360003751058>).
  * Kaikissa LTR:ään vietävissä tapahtumissa tulee olla projektimerkintä.
  * Siirrettävien kenttien tulee olla määritetty Visma LTR:n kirjauslomakkeen asetuksissa rivitasolle.


## Käyttötarkoitus ja rajoitukset
  * Vienti tukee vain uusien tapahtumien vientiä. Jo kerran vietyjä tapahtumia ei päivitetä LTR:ään, vaan tapahtumat luodaan uudelleen. Jos siirto täytyy tehdä uudestaan jo siirretylle ajanjaksolle, täytyy tämän ajanjakson tapahtumat poistaa ensin LTR:stä.
  * Kun palkkajakson kirjaukset ovat tehty ja hyväksytty, siirretään Neptonista tulkinta LTR:n REST-rajapintaan. Siirto käynnistetään Neptonissa, ja valitun ajanjakson mukainen tulkinta siirtyy LTR:n käsiteltäväksi. Siirto muodostaa aineiston sen sääntöjoukon mukaisena, mikä on valittu siirrettäväksi.


## Määrittäminen
Viennin määrittäminen tapahtuu [sääntöjoukkojen](<https://support.nepton.com/hc/fi/articles/360002492278>) avulla. Uusi sääntöjoukko voidaan lisätä osiosta Työaika > Hallinta > Liittymät > Poimintasäännöt > Lisää integraation sääntöjoukko. Kun sääntöjoukko on lisätty, voidaan sen määritykset avata klikkaamalla sääntöjoukon nimeä.
### Poimintasäännöt
Sääntöjoukolle tulee määrittää poimintasäännöt, joiden avulla lähetettävät tiedot poimitaan ja määritetään viennille.
![](https://support.nepton.com/hc/article_attachments/11164987015709)
Poimintasääntö tulee muodostaa siten, että palkkalajikoodit vastaavat LTR:ssä olevia koodeja. Alla on esimerkki mahdollisesta poimintasäännöstä, mutta kaikkien OverrideSalaryCode -kentälle määritettävien palkkalajikoodien tulee vastata LTR-ratkaisussa olevia palkkalajikoodeja ko. palkkalajille.
[code] 
    SELECT   
    *,   
    CASE  
    WHEN CompensationType = 'OvertimeDaily100' THEN '0410' -- If 0410 would be salary code for 100% daily overtime in LTR   
    WHEN CompensationType = 'YearLeave' THEN '3600' -- If 3600 would be salary code for year leave in LTR  
    WHEN CompensationType = 'UnpaidBasicTime' THEN '6199' -- If 6199 would be salary code for unpaid basic time  
    WHEN CompensationType = 'BasicTime' THEN '0001' -- If 0001 would be salary code for basic work in LTR  
    WHEN CompensationType = 'WorkRise' THEN WorkRiseSalaryCode -- Salary code is set for Work rises in settings  
    WHEN CompensationType = 'WorkIncrement' THEN WorkIncrementCode -- Salary code is set for Supplements in settings  
    ELSE 'NOT_DEFINED'  
    END as OverrideSalaryCode,  
    CASE   
    WHEN isApproved = 'Y' THEN '2'  
    ELSE '1'  
    END AS VismaLTRStatus, -- If correct license to send approval status updates to LTR  
    CASE  
    WHEN CompensationType = 'BasicTime' THEN '00012' -- If 00012 would be the correct billing code for this compensationtype in LTR  
    ELSE ''  
    END as VismaLTRBillingCode -- If compensationtype would require a specific billing code  
    FROM   
    UserSalaryData  
    WHERE   
    (  
    CompensationType IN (  
    "BasicTime","ReducedRateTime","UnpaidBasicTime",  
    "AdditionalWork","OvertimeDaily50","OvertimeDaily100",  
    "OvertimeWeekly50","OvertimeWeekly100","OvertimeSunday50",  
    "OvertimeSunday100","OvertimeBaseFixed","OvertimeExtraFixed",  
    "LevellingPeriodAdditional","LevellingPeriodOvertime50",  
    "LevellingPeriodOvertime100","LevellingPeriodUnderTarget",  
    "WorkRise","WorkIncrement","PublicHoliday","WeeklyRestTime",  
    "YearLeave","PayLevellingPeriodToSalary",  
    "TESOvertime50","TESOvertime100"  
    )   
    OR (  
    CompensationType = "MarkedTime"   
    AND ActivityTypeCode = 33  
    )  
    )  
    AND OverrideSalaryCode != 0  
    AND SickLeaveTypeId IS NULL  
    AND AbsenceTypeId IS NULL  
    AND IsTimeBorrowedFromBalance = 'N'
[/code]
### Viennin asetukset
Sääntöjoukon poimintasääntöjen alta löytyvät viennin asetukset. Viennin tiedostomuodoksi asetetaan Visma LTR. Projektitieto sisältyy Visma LTR -vientiin automaattisesti. Jos rajapinta-tunnuksia on useampia per työnantaja, voidaan määrittää "Jaa tulokset" kohtaan Työnantaja. Lisätietoja Työnantajalla jakamiseesta seuraavassa kappaleessa. 
![](https://support.nepton.com/hc/article_attachments/11165017992861)
Tämän jälkeen yhteysasetukset määritetään kohdassa "Vie web serviceen". Viennin web service -osoite kohtaan määritetään Visman REST-rajapinnan osoite. Asiakkaan tulee pyytää tämä osoite Vismalta. Rajapinnan osoitteen tulee käyttää suojattua yhteyttä (eli https://). Osoite käyttää rajapinnan tasks-päätepistettä, eli osoitteen lopussa tulee olla _/tasks/_.  
  
Esimerkiksi jos rajapinnan osoite on https://rajapinnan.verkkotunnus.com/ltrws/REST/ , tulee osoitteeksi määrittää https://rajapinnan.verkkotunnus.com/ltrws/REST/tasks/  
  
API-käyttäjäksi määritetään rajapinnan API-käyttäjä ([LTR-dokumentaatiossa](<https://demoltr1.visma.fi/ltrws/LTRRESTapi/#/tasks/post_tasks_>) _hash_) ja API avain -kohtaan rajapinnan tunnisteavain ([LTR-dokumentaatiossa](<https://demoltr1.visma.fi/ltrws/LTRRESTapi/#/tasks/post_tasks_>) _authkey_). Jos API-tunnukset vaihtuvat riippuen siitä mikä henkilön työnantaja on, voidaan tunnukset määrittää niin, että asetetaan viennin asetuksiin "Jaa tulokset" -kohtaan "Työnantaja", ja asetetaan esimerkiksi API-käyttäjän tai avaimen kohtaan työnantajan lisätietoihin viittaava kentän nimi {} -merkkien ympäröimänä. Esimerkki:
  * Työnantajalle "Yritys Oy" on asetettu työntaja-osiossa lisätietokenttiin LTRApiUser, jonka arvoksi on asetettu "exampleuserhash"
  * Työnantajalle "Yritys 2 Oy" on asetettu työntaja-osiossa lisätietokenttiin LTRApiUser, jonka arvoksi on asetettu "esimerkkikayttaja"
  * Kenttään API käyttäjä asetetaan {LTRApiUser}, jolloin liittymä käyttää työnantajakohtaista arvoa liittymässä.
  * Kenttään API avain asetetaan {LTRApiKey}, jolloin liittymä käyttää työnantajakohtaista arvoa liittymässä.
  * Tämä mahdollistaa sen että jos LTR:ssä on useampi rajapinnan käyttäjätunnus per työnantaja, saadaan tiedot välitettyä oikein sen mukaan, miten henkilölle on Neptonissa asetettu työnantaja  
![](https://support.nepton.com/hc/article_attachments/11165112300061)


Alla esimerkki työnantajasta jolle on asetettu LTRApiUser- ja LTRApiKey-lisätiedot työnantajan tietoihin. Kenttien nimen voi määrittää itse, mutta sen on hyvä olla kuvaava ja kentän nimen täytyy täsmätä annetun määrityksen kanssa. [Lue lisää työnantajista täältä](<https://support.nepton.com/hc/fi/articles/10847746064797>).![](https://support.nepton.com/hc/article_attachments/11165930933661)
## Viennin käynnistäminen
Vienti käynnistetaan Työaika > Hallinta > Liittymät > Visma LTR-näkymässä
  * Valitse tarvittava poimintasääntö
  * "Lukitse tapahtumat siirtotiedoston loppupäivämäärään saakka" -asetus voidaan valita tarvittaessa
  * Määrittele haluamasi aikaväli
  * Valitse "Lähetä siirtotiedosto web servicelle"
  * Valitse henkilöt
  * Klikkaa Käynnistä


![](https://support.nepton.com/hc/article_attachments/14387562549789)
### Rajapintasanoma
Liittymä kutsuu Visma LTR REST-rajapinnan post_tasks-metodia. Löydät lisätietoja [Visma LTR teknisestä kuvauksesta](<https://demoltr1.visma.fi/ltrws/LTRRESTapi/#/tasks/post_tasks_>). Huomioi että rajapintaan lähetetään yksittäinen kutsu jokaisesta tapahtumasta per käyttäjä, jolloin lokiin tallennetaan zip-tiedosto joka sisältää kaikki integraation lähettämät yksittäiset kutsut JSON-tiedostoina.
Taso | Kentän nimi | Muoto | Selite  
---|---|---|---  
juuri | id | numero | Aina 0, liittymä tukee vain uusien tapahtumien luomista, ei päivittämistä  
juuri | personnumber | merkkijono | Henkilön henkilönumero. Tulee vastata henkilön henkilönumeroa Visma LTR:ssä. Ensisijaisesti lähetetään henkilön Visma-tunniste, tai jos sitä ei ole asetettu käytetään henkilönumeroa.  
juuri | ts_start | merkkijono | Tapahtuman alkuajankohta muodossa YYYY-MM-DD HH:ii:ss  
juuri | ts_end | merkkijono | Tapahtuman loppuajankohta muodossa YYYY-MM-DD HH:ii:ss  
juuri | workid | numero | Aina 0, liittymä tukee vain uusien tapahtumien luomista, ei päivittämistä  
juuri | title | merkkijono | Tapahtuman tyyppi  
juuri | description | merkkijono | Tapahtuman kuvaus  
juuri | rows | Joukko tapahtuman rivejä | Rivit sisältävät tapahtumaan liittyvät tiedot kuten tehty työaika, mahdolliset työlisät yms.  
rows - rivijoukko | row | Tapahtumaan liittyvä rivi | Rivi sisältää tapahtumaan liittyvän yksittäisen palkkalajin, työlisän tmv. merkinnän tiedon  
row - rivin tieto | id | numero | Aina 0, liittymä tukee vain uusien tapahtumien luomista, ei päivittämistä  
row - rivin tieto | type | merkkijono |  Tapahtuman rivin tyyppi
  * HO = tuntiperusteinen tapahtuma
  * TR = matkalasku
  * SR = materiaali-perusteinen tapahtuma
  * IV = kulu

Tieto voidaan yliajaa sääntöjoukossa arvolle `VismaLTRRowType`  
row - rivin tieto | costcenter | merkkijono |  Henkilön kustannuspaikka. Jos Visma L7 projektien tuonnissa on määritetty "Lisää kustannuspaikka tuodun projektin koodiin"-valinnaksi "Kyllä", kustannuspaikka haetaan projektin koodista. Voidaan yliajaa sääntöjoukossa arvolle `VismaCostCentre`  
row - rivin tieto | letter | merkkijono |  Littera. Ei lähetetä oletuksena mutta voidaan määrittää sääntöjoukossa arvolle `VismaLTRLetter` Litteran tulee löytyä LTR:stä jotta tiedon siirto onnistuu.  
row - rivin tieto | wagetype | merkkijono |  Palkkalajikoodi  
row - rivin tieto | ts_start | merkkijono |  Merkinnnän alkuaika  
row - rivin tieto | ts_end | merkkijono |  Merkinnän loppuaika  
row - rivin tieto | ts_directed | merkkijono |  Päivämäärä jolle merkintä lisätään LTR:ssä. Voidaan yliajaa sääntöjoukossa arvolle `VismaLTRDirectedTimestamp` muodossa YYYY-MM-DD 00:00:00  
row - rivin tieto | costamount | numero |  Merkinnän määrä, jos tuntiperusteinen niin tuntien määrä. Jos valuuttamääräinen IV (kulu) tai TR (matkalasku), aina 1 ja varsinainen kulu määritetään costprice - tietueessa  
row - rivin tieto | description | merkkijono |  Merkinnän kuvaus  
row - rivin tieto | unit | merkkijono |  Yksikkö tekstimuotoisena. Voidaan yliajaa sääntöjoukossa arvolle `VismaLTRUnit`  
row - rivin tieto | costprice | numero |  Kulun valuuttamäärä. Käytetään rivityypeissä TR (matkalasku) ja IV (kulu) kun määrä on valuuttana, esimerkiksi euroina.  
row - rivin tieto | project | merkkijono |  Ylänumeron projektin tunniste. Tulee vastata Visma L7:ssä olevaa ylänumeron projektin tunnistetta. Voidaan yliajaa sääntöjoukossa arvolle `VismaLTRProject`  
row - rivin tieto | work | merkkijono |  Alanumeron projektin tunniste. Tulee vastata Visma L7:ssä olevaa alanumeron projektin tunnistetta. Voidaan yliajaa sääntöjoukossa arvolle `VismaLTRWork`  
row - rivin tieto | billingcode | merkkijono |  Merkinnän laskutuskoodi, jos Visma LTR:ssä on määritetty että palkkalaji vaatii laskutuskoodin. Voidaan määrittää sääntöjoukossa arvolle `VismaLTRBillingCode`  
row - rivin tieto | status | numero |  Merkinnän hyväksynnän tila,  
1 = Avoin  
2 = Hyväksytty  
5 = Ei siirtoa  
Vaatii Visma LTR:ään lisenssin jolla mahdollista määrittää merkinnän hyväksyntä. Jos halutaan liittää vientiin, tulee määrittää sääntöjoukossa arvolle `VismaLTRStatus`. Jos hyväksyntä viedään, täytyy viennissä välittää myös acceptor ja ts_accepted  
row - rivin tieto | acceptor | merkkijono |  Jos hyväksytty, hyväksyjän nimi. Viedään automaattisesti jos status - tieto viedään hyväksyttynä  
row - rivin tieto | ts_accepted | merkkijono |  Jos hyväksytty, hyväksynnän ajankohta. Viedään automaattisesti jos status - tieto viedään hyväksyttynä  
row - rivin tieto | tripreason | merkkijono |  Liitetään vientiin jos kyseessä matkalasku, matkalaskun kuvaus. Voidaan yliajaa sääntöjoukossa arvolle `VismaLTRTripReason`  
row - rivin tieto | triproute | merkkijono |  Liitetään vientiin jos kyseessä matkalasku, matkalaskun reitit. Voidaan yliajaa sääntöjoukossa arvolle `VismaLTRTripRoute`  
row - rivin tieto | trippassenger | merkkijono |  Liitetään vientiin jos kyseessä matkalasku, matkalaskun matkustajat. Määritetään sääntöjoukossa arvolle `VismaLTRTripPassengerAmount`  
Esimerkkisanoma JSON-muodossa:
[code] 
    {  
      "id": 0,  
      "personnumber": "123456",  
      "ts_start": "2023-03-02 08:00:00",  
      "ts_end": "2023-03-02 16:00:00",  
      "workid": 0,  
      "title": "Työ",  
      "description": "",  
      "rows": [  
        {  
          "row": {  
            "id": 0,  
            "type": "HO",  
            "costcenter": "CostCenterName",  
            "wagetype": "40",  
            "ts_start": "2023-03-02 08:00:00",  
            "ts_end": "2023-03-02 16:00:00",  
            "ts_directed": "2023-03-02 00:00:00",  
            "costamount": 8,  
            "description": "",  
            "unit": "H",  
            "project": "SomeProjectCode",  
            "work": "SubProjectCode",  
            "billingcode": "987654321",  
            "status": 2,  
            "acceptor": "Acceptor Name",  
            "ts_accepted": "2023-03-04 16:00:00"  
          }  
        },  
        {  
          "row": {  
            "id": 0,  
            "type": "IV",  
            "costcenter": "CostCenterName",  
            "wagetype": "567890",  
            "ts_start": "2023-03-02 08:00:00",  
            "ts_end": "2023-03-02 16:00:00",  
            "ts_directed": "2023-03-02 00:00:00",  
            "costamount": 1,  
            "description": "",  
            "unit": "C",  
            "costprice": 51,  
            "project": "SomeProjectCode",  
            "work": "SubProjectCode",  
            "billingcode": "12345678",  
            "status": 2,  
            "acceptor": "Acceptor Name",  
            "ts_accepted": "2023-03-04 16:00:00"  
          }  
        }  
      ]  
    }
[/code]
