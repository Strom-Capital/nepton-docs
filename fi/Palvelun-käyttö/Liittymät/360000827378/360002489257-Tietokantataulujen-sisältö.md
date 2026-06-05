---
id: 360002489257
title: Tietokantataulujen sisältö
url: https://support.nepton.com/hc/fi/articles/360002489257-Tietokantataulujen-sis%C3%A4lt%C3%B6
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels:
- NEPTONNEEDSREVIEW
- palkkalajimääritys
- poimintasäännöt
- sääntöjoukot
- palkkasääntö
- tietotaulu
- tietokantataulu
- database table
- content of database
promoted: false
updated_at: '2026-06-01T14:48:24Z'
edited_at: '2026-06-01T13:43:44Z'
---

# Tietokantataulujen sisältö

Sääntöjoukolla määritetään siirrettävään aineistoon poimittava sisältö. Tässä artikkelissa kuvataan tietokantataulut, joiden sisältöä voi poimia sääntöjoukolla.
Sääntöjoukoista yleisesti voit lukea [täältä](<https://support.nepton.com/hc/fi/articles/360002492278>).
Sääntöjoukon poiminnan periaatteista voit lukea [täältä](<https://support.nepton.com/hc/fi/articles/21077132021149>).
Kattavan listan sääntöjoukon poimintasääntöjen malleista löydät [täältä](<https://support.nepton.com/hc/fi/sections/360000827378>).
### Eri tietokantataulujen sisältö
Alla on kuvattu tietokantataulut, joiden sisältöä voi poimia siirtoihin.
Tietokantataulun nimi | Kuvaus | Tuettu asetusarvojen poikkeuksissa  
---|---|---  
**UserSalaryData** |  Taulu sisältää henkilön tulkitun työaikatiedon voimassa olevien sääntöjen mukaisesti. Poimittaessa tulkittuja tapahtumia, kannattaa poimintajakso pitää mahdollisimman lyhyenä, jotta tietojen hakuaika ei kasvaisi pitkäksi. Suosittelemme poimintajaksoksi enintään kaksi kuukautta eteen- ja taaksepäin. | Ei  
**UserEventData** |  Taulu sisältää henkilölle kirjatut tapahtumat sellaisena kuin ne on kirjattu. Poimittaessa kirjattuja tapahtumia, voi poimintajakso olla pidempi kuin tulkittuja tapahtumia poimittaessa. Suosittelemme poimintajaksoksi enintään yksi vuosi eteen- ja taaksepäin. |  Kyllä, pois lukien asetukset, joilla määritetään työvuorokauden ajoittuminen. UserCostGroup-tieto ei ole käytettävissä. Tieto löytyy UserInfoData-taulusta.  
**UserEventHistoryData** | Taulu sisältää henkilölle kirjatut tapahtumat sellaisina kuin ne on kirjattu mukaan lukien muokattujen tapahtumien aiemmat versiot, poistetut tapahtumat ja asetetulla aikavälillä muokatut tapahtumat. Tapahtumien eri versiot saattavat ajoittua myös asetetun aikavälin ulkopuolelle, jos tapahtuman jonkin version muokkaus- tai tapahtuma-aika sijoittuu kuitenkin annetulle välille. |  Kyllä, pois lukien ne asetukset, joilla määritetään työvuorokauden ajoittuminen. UserCostGroup-tieto ei ole käytettävissä. Tieto löytyy UserInfoData-taulusta.  
**UserEventProjectData** | Jokaiselle tapahtumaan liitetylle projektille on tässä taulukossa rivi, joka sisältää projektin tunnuksen ja muistiinpanot. | Kyllä  
**UserTravelExpenseTripData** | Taulu sisältää henkilön matkalaskuille kirjattujen matkojen tiedot. | Ei  
**UserEventExternalIdentifierData** | Taulu sisältää tapahtumien ulkoisten tunnisteiden tiedot. | Kyllä, pois lukien ne asetukset joilla määritetään työvuorokauden ajoittuminen.  
**UserData** | Taulu sisältää voimassa olevat henkilö- sekä työsuhdetiedot. Voidaan yhdistää kyselyihin _UserSalaryData_ \- sekä _UserEventData_ -tauluista. | Kyllä  
**UserInfoData** |  Taulu sisältää henkilö- ja työsuhdetietoja historia-arvoineen. Voidaan yhdistää kyselyihin _UserSalaryData_ \- sekä _UserEventData_ -tauluista. Myös yrityksen omat lisätietokentät ovat oletuksena saatavilla tiedoissa.Tarkka listaus taulun sisällöstä kohdassa 8 - UserInfoData. |  Kyllä, lukuunottamatta arkaluontoisia tietoja:
  * RFIDTagNumber
  * SocialSecurityNumber

  
**UserGroupData**  
| Taulu sisältää henkilöryhmätiedot henkilöille, jotka ovat aineistossa. Valittujen henkilöryhmien kaikki ylähenkilöryhmät löytyvät taulusta. | Kyllä  
**ProjectData** | Sisältää täydelliset projektitiedot projekteista, joita käyttäjä käyttää raportointikaudella. | Kyllä  
**PaymentGroupPeriodData** | Sisältää maksuryhmien maksukausien tiedot henkilöille, jotka ovat aineistossa. | Kyllä  
**PlanningYearTargetData** | Sisältää vuorosuunnittelun vuosityöajan seuraamisen tiedot. | Ei  
**PlanningYearTargetBreakdownData** | Sisältää vuorosuunnittelun vuosityöajan tavoitteen muodostumisen erittelyn. | Ei  
**UserExternalIdentifier** | Taulu sisältää henkilön ulkoiset tunnisteet. UserId-kentän perusteella tämä voidaan liittää useimpiin muihin tietokantatauluihin esim. UserEventData tai UserSalary data. Tämä taulu on hyödyllinen liittymille, jotka sekä tuovat käyttäjiä järjestelmään että vastaanottavat käyttäjiin liittyviä työaikatietoja. | Kyllä  
### UserSalaryData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**CompensationType** | enum |  Käytettävissä ainoastaan SalaryData-taulun dataan.
  * "BasicTime" - Tehty säännöllinen työaika sekä tunti-tunnista korvatta aika
  * "ReducedRateTime" - Vähennetyn korvauksen aika. Joistakin poissaolotyypeistä ja sairauslomista voidaan ansaita alennettua palkkaa.
  * "UnpaidBasicTime" - Perustyöaika, josta ei makseta korvausta. Esimerkiksi palkattomasta poissaolosta muodostuu enintään työvelvoitteen verran.
  * "AdditionalWork" - Lisätyö, jota ansaitaan säännöllisen työajan (työpäivän ja työviikon pituus) jälkeen, mutta ennen työpäivän- ja työviikon enimmäispituutta.
  * "OvertimeDaily50" - Vuorokautinen ylityö 50%.
  * "OvertimeDaily100" - Vuorokautinen ylityö 100%.
  * "OvertimeWeekly50" - Viikottainen ylityö 50%.
  * "OvertimeWeekly100" - Viikottainen ylityö 100%.
  * "OvertimeSunday50" - Sunnuntaiylityö 50%. Ylityö, jota ansaitaan sunnuntaiylityöasetusten mukaisesti.
  * "OvertimeSunday100" - Sunnuntaiylityö 100%. Ylityö, jota ansaitaan sunnuntaiylityöasetusten mukaisesti.
  * "OvertimeBaseFixed" - Ylityö 1, käytetään osassa pohjoismaissa käytössä olevia TES:ejä.
  * "OvertimeExtraFixed" - Ylityö 2, käytetään osassa pohjoismaissa käytössä olevia TES:ejä.
  * "TESOvertime50" - Osassa TES:ejä käytettävä TES:n mukainen ylityö, joka ansaitaan erillisenä viikottaisesta ylityöstä. Muodostuu vain, kun asetus 'Viikottaisesta ylityöstä erillisenä ansaittu TES:n mukainen ylityö' on käytössä; muuten TES:n mukainen ylityö on normaalia ylityötä, jolle on merkitty IsTesOvertime-arvoksi "Y".
  * "TESOvertime100" - Osassa TES:ejä käytettävä TES:n mukainen ylityö, joka ansaitaan erillisenä viikottaisesta ylityöstä. Muodostuu vain, kun asetus 'Viikottaisesta ylityöstä erillisenä ansaittu TES:n mukainen ylityö' on käytössä; muuten TES:n mukainen ylityö on normaalia ylityötä, jolle on merkitty IsTesOvertime-arvoksi "Y".
  * "LevellingPeriodAdditional" - Lisätyö, joka ansaitaan tasoittumisjakson lopussa.
  * "LevellingPeriodOvertime50" - 50% ylityö, joka ansaitaan tasoittumisjakson lopussa.
  * "LevellingPeriodOvertime100" - 100% ylityö, joka ansaitaan tasoittumisjakson lopussa.
  * "LevellingPeriodUnderTarget" - Jos tasoittumisjakson lopussa on tehty vähemmän työtä kuin tasoittumisjakson enimmäistyöaika, sisältää enimmäistyöajan alittavan määrän
  * "UnpaidOvertime" - Ylityö, jonka korvaus on asetettu "Ei korvata" ja ei siksi makseta.
  * "WorkRise" - Työkorotus eli korvaus, joka ansaitaan tiettynä aikana tehdystä työstä, esim. ilta- ja sunnuntailisä.
  * "WorkRisePercentagePart" - Laskettu prosentti- tai minuuttikorotus per tunti työkorotukseen
  * "WorkIncrement" - Työlisä, manuaalisesti merkitty korvaus esim. esimieslisä.
  * "WorkIncrementPercentagePart" - Laskettu prosenttiosa työlisästä, joka kerryttää kertymää jollain prosentilla.
  * "PublicHoliday" - Juhlapyhä. Korvauksen määrä riippuu siitä, paljonko juhlapyhä lyhentää työviikkoa.
  * "YearLeave" - Vuosiloma.
  * "WeeklyRestTime" - Viikkolepoaika. _Huom: kun viedään viikkolepokorvausta toiseen järjestelmään käyttäen poimintasääntöjä, tämä asetus voidaan määritellä käyttämällä "basePartTarget" -kenttää._
  * "ProjectOverAllocation" - Projektille kirjattu aika, joka ylittää tapahtuman keston.
  * "StartupWork" - Aloitustyö, joka korvataan säännöllisenä työaikana
  * "StartupWorkAdditionalWork" - Aloitustyö, joka korvataan lisätyönä
  * "StartupWorkOvertime50" - Aloitustyö, joka korvataan 50% ylityönä
  * "StartupWorkOvertime100" - Aloitustyö, joka korvataan 100% ylityönä
  * "UnpaidStartupWork" - Aloitustyönä merkitty aika, jota ei korvata.
  * "TerminationWork" - Lopetustyö, joka korvataan säännöllisenä työaikana
  * "TerminationWorkAdditionalWork" - Lopetustyö, joka korvataan lisätyönä
  * "TerminationWorkOvertime50" - Lopetustyö, joka korvataan 50% ylityönä
  * "TerminationWorkOvertime100" - Lopetustyö, joka korvataan 100% ylityönä
  * "UnpaidTerminationWork" - Lopetustyönä merkitty aika, jota ei korvata.
  * "Accrual" - Kertymä. Juokseva/kumulatiivinen arvo tietylle kertymälle esim. saldo ja pankki.
  * "AccrualChange" - Kertymän muutos edellisestä päivästä.
  * "MarkedTime" - Tapahtumalle kirjattu aika. EventStartTime- ja EventEndtime-kentät kuvaavat kirjauksen kellonajat. Seuraavista tapahtumista ei muodosteta tätä tietoa:
    * Juhlapyhätapahtumat.
    * Kertymien, kuten työaikasaldo tai vuosiloma, muutos- ja asetustapahtumat.
  * "Lunch" - Ruokatauko. Kertoo, miten ruokatauko on laskennallisesti sijoitettu työpäivään.
  * "OnCall" - Sisältää toteutuneen varallaoloajan. Oletuksena kaikki tapahtumat, jotka on kirjattu varallaolojakson päälle poisluetaan varallaoloajasta, mutta asetusten kautta on mahdollista määrittää poikkeuksia tietyille tapahtumatyypeille.
  * "PayOverAccrualLimit" - sisältää kertymästä automaattisesti leikatut tunnit, kun positiivisen kertymärajan käyttäytyminen on "Siirrä rajatut palkkaan".
  * "UnpaidOverMinAccrualLimit" - sisältää kertymästä automaattisesti leikatut tunnit, kun negatiivisen kertymätajan käyttäytyminen on "Siirrä rajatut palkkaan".

  
**AccrualType** | enum|null | Käytettävissä kertymien ja kertymien muutosten kanssa  
**Amount** | decimal | Määrä. Arvo sekunneissa kaikissa muissa kuin kokonaisluvuissa. Kokonaisluvuissa arvo esitetään kokonaislukuna (katso UnitType).  
**UnitType** | enum|null | 
  * "U" - kokonaisluku
  * "D" - desimaaliluku
  * "S" - sekunteja
  * "H" - tunteja
  * "J" - päiviä
  * "C" - valuutta

  
**SalaryRenderingDate** | date | Päivä, johon maksu/vuoro kuuluu. Formaatti: _YYYY-MM-DD._  
**PaymentDate** | date | Maksupäivä. Formaatti: _YYYY-MM-DD._  
**StartDateTime** | datetime | Alkupäivä ja -aika, milloin _salary data_ on ansaittu (jos käytettävissä). Huom. Pitkät merkinnät, kuten sairauslomat jaetaan laskentapäiville. Formaatti: _YYYY-MM-DD HH:MM:SS_  
Aikavyöhyke: Käyttäjän paikallinen aikavyöhyke.  
  
**EndDateTime** | datetime | Loppupäivä ja -aika, milloin _salary data_ on ansaittu (jos käytettävissä). Huom. Pitkät merkinnät, kuten sairauslomat jaetaan laskentapäiville. Formaatti: YYYY-MM-DD HH:MM:SS Aikavyöhyke: Käyttäjän paikallinen aikavyöhyke.  
**EventStartDateTime** | datetime | Alkupäivä ja -aika, milloin tulkittuun työaikaan liittyvä tapahtuma on merkitty kalenteriin (jos käytettävissä).  
Formaatti: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Käyttäjän paikallinen aikavyöhyke.  
**EventEndDateTime** | datetime | Loppupäivä ja -aika, milloin tulkittuun työaikaan liittyvä tapahtuma on merkitty kalenteriin (jos käytettävissä). Formaatti: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Käyttäjän paikallinen aikavyöhyke.  
**CreatedDatetime** | datetime|null | Päivä ja aika, milloin tähän riviin liittyvä tapahtuma on luotu. Formaatti: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Suomen aikavyöhyke  
**ModifiedDatetime** | datetime|null |  Päivä ja aika, milloin riviin liittyvää tapahtumaa on viimeksi muokattu.   
Formaatti: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Suomen aikavyöhyke Tasoittumisjakson ja viikkolepojan korvauksissa käytetään jakson viimeisen viikon viimeisintä tapahtuman muokkausaikaa.  
**ActivityId** | int|null |  Tapahtuman yksilöllinen tunniste Tapahtumat-taulusta. Hyödyllinen, jos haluaa ryhmitellä aikoja, jotka tulevat samasta tapahtumasta, esim. vuosilomapalkka. ActivityId ei muutu, jos tapahtumaa muokataan. Jos ActivityId on negatiivinen, tarkoittaa se sitä että tapahtuma generoidaan asetusten perusteella (esimerkiksi oletettu tapahtuma tai vuorokalenterin vuoro). Tässä tapauksessa ActivityId voi muuttua.  
**ActivityTypeCode** | string|null | Tapahtumatyypin koodi.  
**WorkRiseNumber** | int|null | Työkorotuksen numero asetuksissa.  
**WorkRiseSalaryCode** | string|null | Työkorotuksen palkkakoodi asetuksissa.  
**WorkRisePercentageIncrease** | decimal(4,1)|null | Työkorotuksen korotusprosentti, jota käytetään työkorotuksen keston laskentaan "WorkRisePercentagePart"-rivillä.  
**WorkRiseMinutesPerHourIncrease** | smallint|null | Työkorotuksen minuuttia/tunti-lisä, jota käytetään työkorotuksen keston laskentaan "WorkRisePercentagePart"-rivillä.  
**WorkRisePayTarget** | string|null |  Työkorotuksen korvauksen kohdenne. Tuetut valinnat ovat:
  * "salary" - Kohdistettu palkkaan
  * "annualbalance" - Kohdistettu vuosivapaakertymään
  * "balance" - Kohdistettu saldoon
  * "bank" - Kohdistettu pankkiin
  * "flexiblehours" - Kohdistettu joustokertymään
  * "flexibleworkhours" - Kohdistettu joustotyötuntikertymään
  * "holidaypayleave" - Kohdistettu lomarahavapaakertymään
  * "levellingperiodhours" - Kohdistettu tasoittumisjaksotuntikertymään
  * "overtimebalance" - Kohdistettu ylityökertymään
  * "savingsleave" - Kohdistettu säästövapaakertymään
  * "weeklyrest" - Kohdistettu viikkolepokertymään
  * "worktimeshorteningleave" - Kohdistettu työajanlyhennysvapaakertymään

Kohde voidaan valita myös tapahtuman ylityökohdenteen perusosalta tai korotusosalta.  
**WorkIncrementName**  
| string|null | Työlisän nimi.  
**WorkIncrementNumber** | int|null | Työlisän numero/indeksi asetuksissa.  
**WorkIncrementTripNumber** | int | Matkalaskun matkan juokseva numero tapahtumalla, johon työlisä liittyy. Jos työlisä ei liity matkaan, arvona on `null`.  
**WorkIncrementPercentageIncrease** | decimal(4,1)|null | Työlisän korotusprosentti, jota käytetään Työlisän keston laskentaan "WorkIncrementPercentagePart"-rivillä.  
**WorkIncrementPercentageAccrualTarget** | string|null | Sisäinen nimi kertymälle, johon "work increment percentage part" kohdennetaan.  
**WorkIncrementCode** | string|null | Työlisän palkkalajinumero, joka voidaan asettaa Työlisän asetuksissa (Työyhteisö- tai Asetusryhmätasolla).  
**WorkIncrementDate** | date|null | If the supplement has the date field enabled, the date will appear here (YYYY-MM-DD)  
Aikavyöhyke: Käyttäjän paikallinen aikavyöhyke  
**WorkIncrementComment** | string|null | If the supplement has the comment field enabled, the comments will appear here  
**WorkIncrementType** | enum|null | 
  * "normal" - Normal supplement type for normal event types
  * "correction" - Supplements that only appear on Correction events
  * "cafe" - Supplements that only appear in terminal cafeteria mode
  * "expense" - Supplements that only as a travel invoice expense
  * "allowance" - supplements that only appear as a travel invoice daily allowance
  * "tripReimbursement" - supplements that only appear as a travel invoice trip/transportation reimbursement
  * null - not a supplement

  
**WorkRiseEarnedAtCompensationType** | enum|null | Suodattaa työkorotukset perustuen korvaustyyppiin (compensationtype), jolla se ansaittiin. Katso CompensationType-lista tuetuista arvoista  
**ProjectId1** | int|null |  Tapahtumalla ensimmäisenä olevan projektin sisäinen tunniste. Sarake toistuu liitetylle projektille siten että ensimmäinen projekti on numerolla 1, toinen projekti numerolla 2 ja niin edelleen. Sarake esiintyy numeroille liitetyille projekteille 1-6.  
**EventProjectRowId1** | int|null |  Järjestelmän sisäinen tunniste tapahtuman ja projektin välisestä suhteesta. Voidaan liittää kyselyyn parametrillä UserSalaryData.EventProjectRowId1 = UserEventProjectData.Id Sarake toistuu liitetylle projektille siten että ensimmäinen projekti on numerolla 1, toinen projekti numerolla 2 ja niin edelleen. Sarake esiintyy numeroille liitetyille projekteille 1-6.  
**ProjectExternalIdentifier1** | string|null |  Tapahtumalla ensimmäisenä olevan projektin ulkoinen tunniste. Sarake toistuu liitetylle projektille siten että ensimmäinen projekti on numerolla 1, toinen projekti numerolla 2 ja niin edelleen. Sarake esiintyy numeroille liitetyille projekteille 1-6.  
**ProjectCode1** | string|null |  Tapahtumalla ensimmäisenä olevan projektin koodi. Sarake toistuu liitetylle projektille siten että ensimmäinen projekti on numerolla 1, toinen projekti numerolla 2 ja niin edelleen. Sarake esiintyy numeroille liitetyille projekteille 1-6.  
**ProjectName1** | string|null |  Tapahtumalla ensimmäisenä olevan projektin nimi. Sarake toistuu liitetylle projektille siten että ensimmäinen projekti on numerolla 1, toinen projekti numerolla 2 ja niin edelleen. Sarake esiintyy numeroille liitetyille projekteille 1-6.  
**ProjectType1** | string|null |  Tapahtumalla ensimmäisenä olevan projektin sisäinen nimi projektin tyypille. Esimerkiksi: "toimipiste" (location), "projektityö" (project_work), and "yksikkö" (unit). Sarake toistuu liitetylle projektille siten että ensimmäinen projekti on numerolla 1, toinen projekti numerolla 2 ja niin edelleen. Sarake esiintyy numeroille liitetyille projekteille 1-6.  
**BasePartTarget** | string|null |  Päivän pituuden ylittävä työ jaetaan ylityön perusosan kohdistukseen "BasePartTarget" sekä ylityöosan kohdistukseen "OvertimeTarget". BasePartTarget kertoo kuinka kirjauksen perusosa on kohdistettu. Esimerkiksi kun korvataan tunti-tunnista saldoon, niin korotusosaa ei korvata, jolloin korvattu aika sisältää kohdistukset BasePartTarget = 'balance' ja OvertimeTarget = 'uncompensated'. Tuetut valinnat ovat:
  * "salary" - Kun perusosa on kohdistettu palkkaan
  * "balance" - Kun perusosa on kohdistettu saldoon.
  * "bank" - Kun perusosa on kohdistettu pankkiin.
  * "overtimebalance" - Kun perusosa on kohdistettu ylityökertymään.
  * "uncompensated" - Kun perusosaa ei korvata.
  * "flexiblehours" - Kun perusosa on kohdistettu joustokertymään.

  
**OvertimeTarget** | string|null |  Päivän pituuden ylittävä työ jaetaan ylityön perusosan kohdistukseen "BasePartTarget" sekä ylityöosan kohdistukseen "OvertimeTarget". OvertimeTarget kertoo kuinka kirjauksen ylityöosa on kohdistettu. Esimerkiksi kun työ korvataan ylityönä niin OvertimeTarget saa muun arvon kuin NULL tai 'uncompensated'. Ylityönä pankkiin kohdistettu työ sisältäisi BasePartTarget = 'bank' ja OvertimeTarget = 'bank'. Tuetut valinnat ovat:
  * "salary" - Kun ylityöosa on kohdistettu palkkaan.
  * "balance" - Kun ylityöosa on kohdistettu saldoon.
  * "bank" - Kun ylityöosa on kohdistettu pankkiin.
  * "overtimebalance" - Kun ylityöosa on kohdistettu ylityökertymään.
  * "uncompensated" - Kun korotusosaa ei korvata
  * "flexiblehours" - Kun korotusosa on kohdistettu joustokertymään.
  * NULL - Ylityöosaa ei ole. Arvoa käytetään, kun työ on tehty säännöllisenä työaikana.

  
**OvertimePercentage** | int|null | Tapahtuman ylityöprosentti. Jos asetus "Ylityöstä maksetaan kiinteä korvaus" on päällä eli kalenterissa näkyy Ylityö 1 tai Ylityö 2, on arvo null.  
**WorkRiseEarnedAtOvertimePercentage** |  | Tapahtuman ylityöprosentti, josta työkorotus on muodostunut. Jos asetus "Ylityöstä maksetaan kiinteä korvaus" on päällä eli kalenterissa näkyy Ylityö 1 tai Ylityö 2, on arvo null.  
**UserId** | int | Henkilön palvelun sisäinen tunniste. Ei ole esillä käyttöliittymässä, ja aina kun mahdollista tulisi käyttää henkilön muita tunnisteita.  
**ApprovedByUserId** | int|null |  Tapahtuman hyväksyneen käyttäjän UserId. Tasoittumisjakson ja viikkolepojan korvauksissa käytetään jakson viimeisen viikon viimeistä hyväksyjää.  
**UserCostGroup** | string | Henkilön oletuskustannuspaikka  
**EmployeeSalaryType** | enum | 
  * "hourly" - tuntipalkka
  * "monthly" - kuukausipalkka

  
**EmployeeWorkContractActive** | enum |  Onko henkilö työsuhteessa kyseisenä päivänä
  * "Y" - kyllä
  * "N" - ei

  
**EmployeeWorkContractStartDate** | date | Työsuhteen alkupäivä, null, jos tyhjä. Muoto: YYYY-MM-DD  
**EmployeeWorkContractEndDate** | date | Työsuhteen loppupäivä, null, jos tyhjä. Muoto: YYYY-MM-DD  
**Comment** | string | Kommentti, rajattu 2000 merkkiin  
**IsTimeBorrowedFromBalance** | enum |  Jos työntekijä, jolla on käytössä saldopankki, ei ole töissä päivänä, jolloin hänellä on työvelvoite, työtunnit lainataan saldopankista
  * "Y" - kyllä
  * "N" - ei

  
**IsTesOvertime** | enum |  Onko TES-ylityötä?
  * "Y" - kyllä
  * "N" - ei

  
**IsEmergencyWork** | enum |  Onko hälytystyötä?
  * "Y" - kyllä
  * "N" - ei

  
**IsApproved** | enum |  Onko tapahtuma hyväksytty?
  * "Y" - kyllä
  * "N" - ei

  
**SickLeaveCompensationTypeId** | int |  Sairausloman palkallisuus
  * 1 = palkallinen
  * 2 = palkaton
  * 3 = vähennetty palkka

  
**SickLeaveTypeId** | int |  Sairausloman syy
  * 1 = sairas
  * 2 = lapsi sairas
  * 3 = työtapaturma
  * 4 = tapaturma työmatkalla
  * 5 = vapaa-ajan tapaturma

  
**SickLeaveMedicalCertificateId** | int |  Lääkärintodistus
  * 0 = ei tiedossa
  * 1 = ei vastaanotettu
  * 2 = vastaanotettu
  * 3 = esimiehen hyväksyntä

  
**AbsenceCompensationTypeId** | int |  Poissaolon palkallisuus
  * 1 = palkallinen
  * 2 = palkaton
  * 3 = vähennetty palkka

  
**AbsenceTypeId** | int | Poissaolotyypin tunniste. NULL jos arvoa ei ole. Näkyy asetuksissa osiossa Työtunnit > Poissaolotyypit  
**EarnsVacationDays** | enum |  Ansaitaanko tapahtumasta vuosilomapäiviä. Tulee joko vuosiloman asetuksista tai tapahtumalle kirjatusta tiedosta.
  * "Y" - kyllä
  * "N" - ei

Arvona voi myös olla `null` jos tieto ei ole relevantti työaikatiedolle (esim. hallinnolliset tapahtumatyypit, joista ei muodostu tulkittua työaikaa)  
**FromRounding** | enum | 
  * "Y" = Time has been created due to rounding
  * "N" = Time has not been created due to rounding

  
**OverlapsUnderlyingActivityTypeIds** | string |  Pilkuilla erotettu lista tapahtumatyyppien koodeista, jotka ovat päällekkäin leimauksen kanssa. Nämä ovat tarkoituksella asetettu jäämän toisen leimauksen alle, esim. varallaolo. Nämä tulee käsitellä WHERE-lauseissa alla olevalla tavalla.
[code] 
    WHERE overlapsunderlyingactivitytypeids LIKE '%,33,%'
[/code]  
**ActivityTypeCategoryId** | int | Tapahtumatyypin kategoria, 1 = työ, 2 = poissaolo  
**AdjacencyGroupingId** | int |  Yksilöllinen tunniste keskeytymättömille jaksoille, jotka tulkitaan yhdeksi työjaksoksi. Useampikin tapahtuma ryhmitellään samalle jaksolle, jos tulkittu palkanmaksu ei keskeydy. Ryhmittelemällä tulokset tämän kentän mukaan saat maksetut jaksot pitkille leimauksille, katkottuna välissä olevilla päivillä, joita ei makseta. Esimerkiksi poissaolomerkintä 2. - 22.5.2016:
  * 2\. - 4.5.2016 - Poissaolo maanantaista keskiviikkoon
  * 6.5.2016 - Poissaolo perjantaina (helatorstai 5.5.2016)
  * 9\. - 13.5.2016 - Poissaolo maanantaista perjantaihin
  * 16\. - 20.5.2016 - Poissaolo maanantaista perjantaihin

  
### UserEventData, UserEventHistoryData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**ActivityId** | int |  Tapahtuman yksilöllinen tunniste Tapahtumat-taulusta. Hyödyllinen, jos haluaa ryhmitellä aikoja, jotka tulevat samasta tapahtumasta, esim. vuosilomapalkka. ActivityId ei muutu, jos tapahtumaa muokataan. Jos ActivityId on negatiivinen, tarkoittaa se sitä että tapahtuma generoidaan asetusten perusteella (esimerkiksi oletettu tapahtuma tai vuorokalenterin vuoro). Tässä tapauksessa ActivityId voi muuttua.  
**ActivityTypeCode** | string | Tapahtumatyypin koodi.  
**BasePartTarget** | string |  Päivän pituuden ylittävä työ jaetaan ylityön perusosan kohdistukseen "BasePartTarget" sekä ylityöosan kohdistukseen "OvertimeTarget". BasePartTarget kertoo kuinka kirjauksen perusosa on kohdistettu. Esimerkiksi kun korvataan tunti-tunnista saldoon, niin korotusosaa ei korvata, jolloin korvattu aika sisältää kohdistukset BasePartTarget = 'balance' ja OvertimeTarget = 'uncompensated'. Tuetut valinnat ovat:
  * "salary" - Kun perusosa on kohdistettu palkkaan
  * "balance" - Kun perusosa on kohdistettu saldoon.
  * "bank" - Kun perusosa on kohdistettu pankkiin.
  * "overtimebalance" - Kun perusosa on kohdistettu ylityökertymään.
  * "uncompensated" - Kun perusosaa ei korvata.
  * "flexiblehours" - Kun peruosa on kohdistettu joustokertymään.

  
**OvertimeTarget** | string |  Päivän pituuden ylittävä työ jaetaan ylityön perusosan kohdistukseen "BasePartTarget" sekä ylityöosan kohdistukseen "OvertimeTarget". OvertimeTarget kertoo kuinka kirjauksen ylityöosa on kohdistettu. Esimerkiksi kun työ korvataan ylityönä niin OvertimeTarget saa muun arvon kuin NULL tai 'uncompensated'. Ylityönä pankkiin kohdistettu työ sisältäisi BasePartTarget = 'bank' ja OvertimeTarget = 'bank'. Tuetut valinnat ovat:
  * "salary" - Kun ylityöosa on kohdistettu palkkaan.
  * "balance" - Kun ylityöosa on kohdistettu saldoon.
  * "bank" - Kun ylityöosa on kohdistettu pankkiin.
  * "overtimebalance" - Kun ylityöosa on kohdistettu ylityökertymään.
  * "uncompensated" - Kun korotusosaa ei korvata
  * "flexiblehours" - Kun korotusosa on kohdistettu joustokertymään.
  * NULL - Ylityöosaa ei ole. Arvoa käytetään, kun työ on tehty säännöllisenä työaikana.

  
**AccrualType** | enum | Käytössä kertymien Muutos- ja Asetustapahtumilla.  
**Amount** | decimal | Määrä sekunteina  
**UnitType** | enum | 
  * "U" - yksiköitä
  * "D" - desimaaliluku
  * "S" - sekunteja
  * "H" - tunteja
  * "J" - päiviä
  * "C" - valuutta

  
**StartDatetime** | datetime |  Päivä ja aika, jolloin tapahtuma alkaa. Formaatti: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Käyttäjän paikallinen aikavyöhyke  
**EndDatetime** | datetime |  Päivä ja aika, jolloin tapahtuma loppuu. Formaatti: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Käyttäjän paikallinen aikavyöhyke  
**CreatedDatetime** | datetime |  Päivä ja aika, jolloin tapahtuma on luotu. Muoto: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Suomen aikavyöhyke  
**ModifiedDatetime** | datetime |  Päivä ja aika, jolloin tapahtumaa on viimeksi muokattu. Huom! UserEventHistoryData-taulussa, jos kyseessä on muokatun tapahtuman aiempi versio, ModifiedDatetime osoittaa muokkausajan, jolloin kyseinen versio on luotu.  Muoto: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Suomen aikavyöhyke  
**ProjectId1** | int | Tapahtumalla ensimmäisenä olevan projektin sisäinen tunniste  
**ProjectCode1** | string | Tapahtumalla ensimmäisenä olevan projektin koodi  
**ProjectExternalIdentifier1** | string | Tapahtumalla ensimmäisenä olevan projektin ulkoinen tunniste  
**ProjectName1** | string | Tapahtumalla ensimmäisenä olevan projektin nimi  
**ProjectType1** | string | Tapahtumalla ensimmäisenä olevan projektin sisäinen nimi projektin tyypille. Esimerkiksi "toimipiste" (location), "projektityö" (project_work), tai "yksikkö" (unit).  
**UserId** | int | Henkilön palvelun sisäinen tunniste. Ei ole esillä käyttöliittymässä, ja aina kun mahdollista tulisi käyttää henkilön muita tunnisteita.  
**ApprovedByUserId** | int | Tapahtuman hyväksyneen henkilön sisäinen tunniste.  
**ApprovedByFirstname** | string | Tapahtuman hyväksyneen henkilön etunimi.  
**ApprovedByLastname** | string | Tapahtuman hyväksyneen henkilön sukunimi.  
**ApprovedByPersonnelNumber** | string | Tapahtuman hyväksyneen henkilön henkilönumero.  
**ApprovedByNeptonGUID** | string | Tapahtuman hyväksyneen henkilön sisäinen Nepton-tunniste.  
**UserCostGroup** | string | Henkilön kalleusluokka  
**EmployeeSalaryType** | enum |  Henkilön palkkaustyyppi
  * "hourly" - tuntipalkka
  * "monthly" - kuukausipalkka

  
**EmployeeWorkContractActive** | enum |  Onko henkilöllä voimassa oleva työsopimus käsiteltävänä päivänä.
  * "Y" - kyllä
  * "N" - ei

  
**EmployeeWorkContractStartDate** | date | Työsuhteen alkupäivä, null, jos tyhjä. Muoto: YYYY-MM-DD  
**EmployeeWorkContractEndDate** | date | Työsuhteen loppupäivä, null, jos tyhjä. Muoto: YYYY-MM-DD  
**Comment** | string | Kommentti, rajattu 2000 merkkiin  
**IsApproved** | enum |  Onko tapahtuma hyväksytty?
  * "Y" - kyllä
  * "N" - ei

  
**IsRequestType** | enum |  Onko tapahtuma tyyppiä, joka vaatii esimiehen hyväksynnän etukäteen?
  * "Y" - kyllä
  * "N" - ei

  
**IsEmergencyWork** | enum |  Onko hälytystyötä?
  * "Y" kyllä
  * "N" ei

  
**SickLeaveCompensationTypeId** | int |  Sairausloman palkallisuus
  * 1 = palkallinen
  * 2 = palkaton
  * 3 = vähennetty palkka

  
**SickLeaveTypeId** | int |  Sairausloman syy
  * 1 = sairas
  * 2 = lapsi sairas
  * 3 = työtapaturma
  * 4 = tapaturma työmatkalla
  * 5 = vapaa-ajan tapaturma

  
**SickLeaveMedicalCertificateId** | int |  Lääkärintodistus
  * 0 = ei tiedossa
  * 1 = ei vastaanotettu
  * 2 = vastaanotettu
  * 3 = esimiehen hyväksyntä

  
**AbsenceCompensationTypeId** | int |  Poissaolon palkallisuus
  * 1 = palkallinen
  * 2 = palkaton
  * 3 = vähennetty palkka

  
**AbsenceTypeId** | int | Poissaolotyypin tunniste, voi olla myös asiakaskohtaisesti määritetty. Näkyy asetuksissa taulukossa Työtunnit->Käytössä olevat poissaolotyypit  
**EarnsVacationDays** | enum |  Ansaitaanko tapahtumasta vuosilomapäiviä. Tulee joko vuosiloman asetuksista tai tapahtumalle kirjatusta tiedosta.
  * "Y" - kyllä
  * "N" - ei

  
**TravelBeginDateTime** | datetime | Matkan alkamispäivä  
Formatti: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Käyttäjän vakituinen aikavyöhyke  
**TravelEndDateTime** | datetime | Matkan päättymispäivä  
Formatti: YYYY-MM-DD HH:MM:SS  
Aikavyöhyke: Käyttäjän vakituinen aikavyöhyke  
**IsActive** | string |  Käytössä vain UserEventHistoryData-taulussa.
  * Y = Tapahtuma on aktiivinen
  * N = Tapahtuma on poistettu tai muokatun tapahtuman aiempi versio. Jos tapahtuma on muokatun tapahtuman aiempi versio, sille on asetettu OriginalActivityId.

  
**OriginalActivityId** | int|null |  Käytössä vain UserEventHistoryData-taulussa. Sisäinen tunniste muokatulle tapahtumalle, josta tämä tapahtuma on aiempi versio. Tapahtuman OriginalActivityId on sama kuin sen viimeisimmän version ActivityId. Jos OriginalActivityId on `null`, on kyseessä tapahtuman viimeisin versio.  
**TerminalId** | int|null |  Sen kirjauspäätteen ID, jolla tapahtuma on aloitettu. Mikäli tapahtuma aloitetaan kirjauspäätteellä, mutta lopetetaan jotain muuta tapaa käyttäen, esimerkiksi mobiililaitteella, niin tapahtuman terminalID häviää lopetuskirjauksen yhteydessä.  
**PlannedActivityTypeCode** | string|null | Suunnitellun vuoron suunnitellun tapahtumatyypin koodi.  
**PlannedActivityAlias** | string|null | Suunnitellun vuoron lyhenne. Saatavilla vain vuorokalenterissa luoduille vuoroille.  
**ShiftTypeDescription** | string|null | Suunnitellun vuoron vuorotyypin lisätieto. Saatavilla vain vuorokalenterissa luoduille vuoroille.  
### UserEventProjectData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**Id** | int | Järjestelmän sisäinen tunniste tapahtuman ja projektin välisestä suhteesta. Voidaan liittää kyselyyn parametrillä UserSalaryData.eventprojectrowid _X_  
**ActivityId** | int | Järjestelmän sisäinen tunniste tapahtumalle johon projektimerkintä on liitetty.  
**ProjectId** | int | Järjstelmän sisäinen tunniste projektitiedolle. Voidaan liittää kyselyparametrillä ProjectData.id  
**ProjectDurationMarked** | string | Projektille tallennettu kesto joko prosentteina tai aika-arvona kuten henkilö on projektin keston merkinnyt tapahtumalle. Eri asia kuin laskettu projektin kesto (katso UserSalaryData)   
**ApprovedByUserId** | int | Projektimerkinnän hyväksyneen henkilön järjestelmän sisäinen tunniste. Tätä ei tule sekoittaa tapahtuman hyväksymiseen, projektitason hyväksynnät tehdään usein projektijohtajien toimesta Projektituntien hyväksyntä -työkalulla.  
**InternalNotes** | string | Projektimerkinnän sisäinen huomautus  
**PublicNotes** | string | Projektimerkinnän ulkoinen huomautus  
### UserTravelExpenseTripData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**ActivityId** | int | Tapahtuman yksilöllinen tunniste Tapahtumataulusta.  
**TripNumber** | int | Matkan juokseva numero tapahtumalla.  
**TransportationMethodId** | int |  Käytetyn matkustusmuodon tunnus. Voi sisältää seuraavat arvot:
  * 1 - auto
  * 2 - lentokone
  * 3 - laiva
  * 4 - julkinen liikenne
  * 5 - muu

  
**StartDateTime** | datetime | Matkan lähtöpäivä ja -aika. Muoto `YYYY-MM-DD HH:MM:SS`  
**StartTimeZone** | string | Matkan lähtöajan aikavyöhyke. Esimerkiksi `Europe/Helsinki`  
**EndDateTime** | datetime | Matkan päättymispäivä ja -aika. Muoto `YYYY-MM-DD HH:MM:SS`  
**EndTimeZone** | string | Matkan päättymisajan aikavyöhyke. Esimerkiksi `Europe/Helsinki`  
**StartLocation** | string | Lähtöpaikan osoite  
**StartRegion** | string | Lähtöpaikan maa  
**EndLocation** | string | Kohdepaikan osoite  
**EndRegion** | string | Kohdepaikan maa  
**ReasonForTrip** | string | Matkan tarkoitus  
### UserEventExternalIdentifierData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**ActivityId** | int | Tapahtuman yksilöllinen tunniste Tapahtumataulusta.  
**ExternalIdentifier** | string | Tapahtuman ulkoinen tunniste  
**IdentifierType** | string | Ulkoisen tunnisteen tyyppi. Tällä hetkellä ainoa tuettu tyyppi on `External`  
### UserData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**UserId** | int | Henkilön palvelun sisäinen tunniste. Ei ole esillä käyttöliittymässä, ja aina kun mahdollista tulisi käyttää henkilön muita tunnisteita.  
**UserIntegrationId** | string |  Henkilön liittymässä yksilöivä tunniste. Muodostuu valitun liittymän mukaisesti. Voi olla jokin seuraavista:
  * Tiettyä integraatiota varten asetettu tunniste
  * Henkilönumero
  * Henkilötunnus

  
**FirstName** | string | Henkilön etunimi  
**LastName** | string | Henkilön sukunimi  
**DefaultProjectId1** | int | Henkilön oletusprojektin sisäinen tunniste  
**DefaultProjectCode1** | string | Henkilön oletusprojektin koodi  
**DefaultProjectType1** | string | Henkilön oletusprojektin sisäinen nimi projektin tyypille. Esimerkiksi "toimipiste" (location), "projektityö" (project_work), tai "yksikkö" (unit).  
**DefaultCostGroup** | string | Henkilön kalleusluokka  
**UserGroupCode** | string | Henkilön henkilöryhmän koodi  
**RootGroupCode** | string | Juuritason henkilöryhmän koodi, mihin henkilön henkilöryhmä kuuluu.  
**ContractType**  
| string | Sopimuksen tyyppi, "monthly" (Kuukausipalkka) tai "hourly" (Tuntipalkka)  
**Contractstartdate** | date | Työsuhteen alkupäivä, null, jos tyhjä. Muoto: YYYY-MM-DD  
**Contractenddate** | date | Työsuhteen loppupäivä, null, jos tyhjä. Muoto: YYYY-MM-DD  
### UserInfoData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**UserId** | int | Henkilön palvelun sisäinen tunniste. Ei ole esillä käyttöliittymässä, ja aina kun mahdollista tulisi käyttää henkilön muita tunnisteita.  
**InfoTypeName** | string |  Henkilötiedon tunniste. Taulu sisältää henkilölle luodut lisätietokentät. Arvo voi esimerkiksi olla:
  * AdministrativeAdditionalInfo
  * AdditionalReportingInfo
  * BIC
  * City
  * DefaultCostGroupCode
  * DefaultProjectId
  * DefaultProjectCode_SDSQL
  * DefaultProjectName_SDSQL
  * Email
  * EventsLockedDate
  * FinnishTaxNumber
  * Firstname
  * HolidayScheduleGroupCode_SDSQL
  * HolidayScheduleName_SDSQL
  * IBAN
  * IntegrationIdAastra
  * IntegrationIdDLSoftware
  * IntegrationIdEmce
  * IntegrationIdFivaldi
  * IntegrationIdHeeros
  * IntegrationIdHogia
  * IntegrationIdIFS
  * IntegrationIdKieku
  * IntegrationIdLessor5
  * IntegrationIdLiksa
  * IntegrationIdMepco
  * IntegrationIdOscar
  * IntegrationIdPersonecF
  * IntegrationIdPersonecW
  * IntegrationIdProCountor
  * IntegrationIdScala
  * IntegrationIdSedab
  * IntegrationIdSonet
  * IntegrationIdTikon
  * IntegrationIdVisma
  * IntegrationIdElisaRing
  * IsSalaryAdvanceAllowed
  * JobTitle
  * Language
  * LastWorkingContractBeginDate
  * LastWorkingContractEndDate
  * LastWorkingContractEndReason
  * LastWorkingContractHourlyWage
  * LastWorkingContractWeeklyHours
  * MicrosoftAxHourlyCost
  * NextOfKinName
  * NextOfKinTel
  * PersonnelNumber
  * PrimarySupervisor_SDSQL
  * PrimaryUnit_SDSQL
  * NeptonPaymentGroupIdentifier
  * NeptonPaymentGroupCode_SDSQL
  * NeptonPaymentGroupId_SDSQL
  * NeptonPaymentGroupName_SDSQL
  * Postcode
  * PhoneNumber
  * RFIDTagNumber
  * Role
  * RootUserGroupCode_SDSQL
  * RootUserGroupId_SDSQL
  * RootUserGroupName_SDSQL
  * SecondarySupervisor_SDSQL (voi olla useita rivejä)
  * SecondaryUnit_SDSQL (voi olla useita rivejä)
  * SettingGroupCode_SDSQL
  * SettingGroupId_SDSQL
  * SettingGroupName_SDSQL
  * SocialSecurityNumber
  * StreetAddress
  * Surname
  * TrialPeriodEndDate
  * UserGroupCode_SDSQL
  * UserGroupId_SDSQL
  * UserGroupName_SDSQL
  * Username
  * WebPageURL
  * WorkArea
  * WorkDayLength_SDSQL, arvo sekunneissa, voi olla useita rivejä
  * WorkWeekLength_SDSQL,arvo sekunneissa, voi olla useita rivejä
  * WorkTimePercentage_SDSQL, oletuksena 100, voi olla useita rivejä
  * WorkScheduleGroupCode_SDSQL
  * WorkScheduleName_SDSQL
  * WorkTimeRoleId_SDSQL
  * WorkTimeRoleName_SDSQL

Huom: Työpäivän ja työviikon pituuteen vaikuttaa työaikaprosentti.  
Työpäivän pituuden, työviikon pituuden ja työajan prosentin voimassaoloajat eivät ole täysin oikein. Asetus voi olla voimassa ajanjakson ulkopuolella, mutta sillä on silti sekä ValidFrom ja ValidTo arvot, jotka osuvat valitun ajanjakson sisälle.  
**InfoTypeId** | int |  Henkilötiedon tyypin sisäinen tunnus. Tätä tietoa ei tule käyttää tunnisteena tiedon hyödyntämisessä, sillä se voi muuttua.  
**ValidFrom** | datetime |  Päivä ja aika, mistä lähtien henkilötieto on voimassa. Jos henkilötiedolle ei ole asetettu voimassaolon alkupäivää, arvona on 1970-01-01 00:00:00 Formaatti: `YYYY-MM-DD HH:MM:SS`  
**ValidTo** | datetime |  Päivä ja aika, mihin asti henkilötieto on voimassa. Jos henkilötiedolle ei ole asetettu voimassaolon päättymispäivää, arvona on 2999-12-31 23:59:59 Formaatti: `YYYY-MM-DD HH:MM:SS`  
**Value** | string |  Kentän arvo merkkijonona. Tieto esitetään tietokentän tyypin perusteella seuraavassa muodossa:
  * Boolean (valintaruutu) - True / False
  * Date - `YYYY-MM-DD`
  * Datetime - `YYYY-MM-DD HH:MM:SS`

  
### UserGroupData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**Id** | int | Neptonin sisäinen henkilöryhmän tunniste  
**Name** | string | Henkilöryhmän nimi  
**Code** | string | Henkilöryhmän koodi  
**Description** | string | Henkilöryhmän kuvaus  
**ParentId** | int|null | Yläryhmän Neptonin sisäinen tunnista. Jos henkilöryhmällä ei ole yläryhmää, arvona on `null`  
**IsRoot** | enum |  Onko henkilöryhmä juuritason ryhmä, eli ryhmä jolla ei ole yläryhmää.
  * `Y` \- kyllä
  * `N` \- ei

  
**Depth** | int |  Numeerinen arvo siitä, kuinka syvällä henkilöryhmä on puurakenteessa. Esimerkiksi:
  * `0` \- juuritason ryhmä
  * `1` \- juuritason ryhmän alaryhmä
  * `2` \- edellisen tason alaryhmä
  * jne.

  
### ProjectData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**Id** | int | Neptonin sisäinen projektin tunniste  
**ExternalId** | int | Projektille annettu ulkoinen tunniste. Lue lisää ulkoisesta tunnisteesta [täällä](<https://support.nepton.com/hc/fi/articles/360006768998>).  
**Name** | string | Projektin nimi projektin tiedot -sivulla  
**Code** | string | Projektin koodi projektin tiedot -sivulla  
**Description** | string | Projektin kuvaus projektin tiedot -sivulla  
**ParentId** | int|null | Yläprojektin Neptonin sisäinen tunnista. Jos projektilla ei ole yläprojektia, arvona on `null`  
**StartDate** | date | Projektin alkamispäivä projektin tiedot -sivulla. Muotona `YYYY-MM-DD`  
**EndDate** | date | Projektin päättymispäivä projektin tiedot -sivulla. Muotona `YYYY-MM-DD`  
**TypeInternalName** | string | Projektityypin sisäinen nimi. Lue lisää projektityypeistä [täällä](<https://support.nepton.com/hc/fi/articles/360002562338>).  
**IsLeaf** | enum |  Onko projekti ns. lehtisolmu (leaf node), eli projekti, jolla ei ole alaprojekteja.
  * `Y` \- kyllä
  * `N` \- ei

  
**IsRoot** | enum |  Onko projekti juuritason projekti, eli projekti, jolla ei ole yläprojektia.
  * `Y` \- kyllä
  * `N` \- ei

  
**IsAssignedProject** | enum |  Onko projekti tapahtumalle kirjattu projekti.
  * `Y` \- kyllä
  * `N` \- ei

Arvona on kyllä, jos projekti on suoraan tapahtumalle kirjattu projekti. Arvona on ei jos projekti on tapahtumalle kirjatun projektin yläprojekti.  
**Depth** | int |  Numeerinen arvo siitä, kuinka syvällä projekti on puurakenteessa. Esimerkiksi:
  * `0` \- juuritason projekti
  * `1` \- juuritason projektin alaprojekti
  * `2` \- edellisen tason alaprojekti
  * jne.

  
### PaymentGroupPeriodData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**Id** | int | Neptonin sisäinen maksuryhmän maksukauden tunniste  
**NeptonPaymentGroupPeriodIdentifier** | string | Neptonin maksuryhmän maksukauden tunniste  
**PaymentGroupId** | int | Neptonin sisäinen maksuryhmän tunniste johon maksuryhmän maksukausi liittyy  
**NeptonPaymentGroupIdentifier** | string | Neptonin maksuryhmän tunniste johon maksuryhmän maksukausi liittyy  
**PaymentPeriodStartDate** | date | Maksuryhmän maksukauden alkupäivä  
**PaymentPeriodEndDate** | date | Maksuryhmän maksukauden loppupäivä  
**PaymentDate** | date | Maksuryhmän maksukauden maksupäivä  
**ValueDate** | date | Maksuryhmän maksukauden arvopäivä  
### PlanningYearTargetData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**UserId** | int | Sisäinen käyttäjän tunnus  
**TargetMinutes** | integer | Jakson tavoite minuuteissa  
**PublishedPlannedMinutes** | integer | Jakson julkaistut suunnitellut työvelvoitteet minuuteissa  
**DraftedPlannedMinutes** | integer | Jakson suunnitellut työvelvoitteet minuuteissa  
**PeriodBeginDate** | date | Vuositavoitteen jakson alkupäivä  
**PeriodEndDate** | date | Vuositavoitteen jakson loppupäivä  
### PlanningYearTargetBreakdownData
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**UserId** | int | Sisäinen käyttäjän tunnus.  
**CalculatedTargetInMinutes** | int | Laskettu vuosityöajan tavoite minuuteissa vuositavoitteen jaksolle. Arvo on 0 tai enemmän.  
**ConfiguredTargetInMinutes** | int | Asetettu vuosityöajan tavoite minuuteissa muodostumiskaudelle. Tämä arvo ei ole laskettu, vaan asetuksissa asetettu arvo.  
**WorktimePercentage** | decimal | Työaikaprosentti muodostumiskaudella.  
**TargetReductionFromEventsInMinutes** | decimal | Minuuttien määrä, millä tavoite lyhenee muodostumiskaudella tapahtumien vuoksi.  
**ContributedMinutesToTarget** | decimal | Minuuttien määrä, jolla muodostumiskausi vaikuttaa tavoitteeseen.  
**ContributionBeginDate** | date | Muodostumiskauden alkupäivä.  
**ContributionEndDate** | date | Muodostumiskauden loppupäivä.  
**YearTargetPeriodBeginDate** | date | Vuositavoitteen jakson alkupäivä.  
**YearTargetPeriodEndDate** | date | Vuositavoitteen jakson loppupäivä.  
### UserExternalIdentifier
Kentän nimi | Tyyppi | Kuvaus  
---|---|---  
**UserId** | int | Henkilön sisäinen tunniste, jonka avulla tämän taulun voi liittää muihin tauluihin.  
**ExternalIdentifier** | string | Ulkoinen tunniste. Työyhteisössä useammalla henkilöllä ei voi olla samaa ulkoista tunnistetta.  
**FieldName** | string | Tekninen nimi ulkoisen tunnisteen kentälle. Määrittää henkilön ulkoisen tunnisteen tyypin. Tällä hetkellä ainoa tuettu arvo on 'ExternalIdentifier1'. Taulujen liitosehdoissa tulisi käyttää myös tätä sillä uusia tunnistekenttiä voidaan lisätä tulevaisuudessa
