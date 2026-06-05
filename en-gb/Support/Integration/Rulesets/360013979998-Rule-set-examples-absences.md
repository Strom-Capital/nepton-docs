---
id: 360013979998
title: Rule set examples - absences
url: https://support.nepton.com/hc/en-gb/articles/360013979998-Rule-set-examples-absences
locale: en-gb
category: Support
category_id: 360000446658
section: Rulesets
section_id: 360000827378
section_path:
- Integration
- Rulesets
labels: []
promoted: false
updated_at: '2025-10-03T07:43:06Z'
edited_at: '2025-10-03T07:43:05Z'
---

# Rule set examples - absences

**Sorry!**
This article has not been translated yet.
Artikkeliin on koottu tyypillisiä poissaolojen poimintaan liittyviä esimerkkejä.
Poissaoloja käsitellään usein palkkajärjestelmissä eri tavoin. Poissaoloja poimiessa tulee tietää, halutaanko poissaolotieto siirtää sen mukaisena kuin se on kirjattu tapahtumaan vai halutaanko poissaolosta siirtää poissaolona tulkitut tunnit tai päivät.
Tyypillisesti erilaiset vapaat siirretään siten, että yksi kirjattu poissaolotapahtuma siirretään yhdellä rivillä.
Alkupäiväksi siirretään kirjatun poissaolotapahtuman alkupäivä ja loppupäiväksi kirjatun poissaolotapahtuman loppupäivä.
Rivin kestona siirretään kirjatun tapahtuman tulkittujen työtuntien määrä.
Erilaiset vapaat kuten pankkivapaa ja työajan lyhennysvapaa yleensä poimitaan sen mukaisesti, kuinka monta päivää tai tuntia tulkinnan tuloksena on syntynyt. Vapaiden siirrossa päivämääränä poimitaan se päivämäärä, mille päivälle tulkinta on muodostunut. Usein tällaiset vapaat siirretään rivinä per päivä.
Sairauspoissaolot poimitaan yleensä sen mukaisesti, kuinka monta päivää tai tuntia tulkinnan tuloksena on syntynyt. Sairauspoissaolo siirretään yhtenä jaksona, jossa rivin päivämääriksi muodostuu tulkitun jakson ensimmäinen korvattava päivä sekä tulkitun jakson viimeinen korvattava päivä.
Yllä olevat ovat tyypillisiä esimerkkejä kyseisten tietojen siirroista. Palkkajärjestelmäkohtaisesti tietojen poiminta voidaan haluta toteuttaa eri tavalla. Ennen poissaolojen poiminnan määrittämistä tulee olla selvää kuinka tieto halutaan muodostaa.
Löydät tietokantataulujen sarakekuvaukset [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>)
Tyypilliset työajan poiminnan esimerkit ovat [tässä ](<https://support.nepton.com/hc/fi/articles/360008045337>)artikkelissa ja projektirakenteen tai projektien huomioiden poiminta [tässä](<https://support.nepton.com/hc/fi/articles/360013894637>) artikkelissa.
## Poimitaan kokopäivän sairausloma, ja muodostetaan palkkalaji sairausloman lajin perusteella
Esimerkissä poimitaan kokopäivän sairauspoissaolot ulkoiseen järjestelmään.
Päivämääriksi poimitaan tapahtuman alku- ja loppupäivämäärät.
Tapahtumat ryhmitellään per tapahtuma.
Yhtenä poiminnan ehtona on, että päivällä ei ole sellaisia kirjauksia, joista on muodostunut töitä _(AND SalaryRenderingDate NOT IN )_. Tällöin kyseessä on kokopäivän poissaolo.
Mikäli poimitaan osapäivän poissaolo niin ehto kirjoitetaan muotoon _AND SalaryRenderingDate IN_. Korvaathan ' '-merkkien välissä olevan tekstin, esim. 'PALKATON_ITSESAIRAS', oikealla palkkalajikoodilla.
[code] 
    SELECT  
      *,  
      SUM(Amount) AS OverrideAmount,   
      MIN(SalaryRenderingDate) As OverrideStartDatetime,   
      MAX(SalaryRenderingDate) AS OverrideEndDatetime,
      CASE
        WHEN SickLeaveTypeId = 1 AND CompensationType = 'UnpaidBasicTime' THEN 'PALKATON_ITSESAIRAS' -- palkaton itse sairas   
        WHEN SickLeaveTypeId = 2 AND CompensationType = 'UnpaidBasicTime' THEN 'PALKATON_LAPSISAIRAS' -- palkaton lapsi sairas   
        WHEN SickLeaveTypeId = 3 AND CompensationType = 'UnpaidBasicTime' THEN 'PALKATON_TYOTAPATURMA_TOISSA' -- palkaton työtapaturma työpaikalla   
        WHEN SickLeaveTypeId = 4 AND CompensationType = 'UnpaidBasicTime' THEN 'PALKATON_TYOTAPATURMA_TYOMATKALLA' -- palkaton työtapaturma työmatkalla   
        WHEN SickLeaveTypeId = 5 AND CompensationType = 'UnpaidBasicTime' THEN 'PALKATON_TAPATURMA_VAPAALLA' --palkaton vapaa-ajan tapaturma  
        WHEN SickLeaveTypeId = 1 AND CompensationType = 'BasicTime' THEN 'PALKALLINEN_ITSESAIRAS' -- palkallinen itse sairas
        WHEN SickLeaveTypeId = 2 AND CompensationType = 'BasicTime' THEN 'PALKALLINEN_LAPSISAIRAS' -- palkallinen lapsi sairas
        WHEN SickLeaveTypeId = 3 AND CompensationType = 'BasicTime' THEN 'PALKALLINEN_TYOTAPATURMA_TOISSA' -- palkallinen työtapaturma työpaikalla
        WHEN SickLeaveTypeId = 4 AND CompensationType = 'BasicTime' THEN 'PALKALLINEN_TYOTAPATURMA_TYOMATKALLA' -- palkallinen työtapaturma työmatkalla
        WHEN SickLeaveTypeId = 5 AND CompensationType = 'BasicTime' THEN 'PALKALLINEN_TAPATURMA_VAPAALLA' --palkallinen vapaa-ajan tapaturma
        ELSE 'NOT DEFINED'
      END AS OverrideSalaryCode  
    FROM  
      UserSalaryData   
    WHERE  
      ActivityTypeCode = 2 --sick leave  
      AND CompensationType IN ('BasicTime', 'UnpaidBasicTime', 'ReducedRateTime') -- this row exists to prevent lunch or other events from getting included
      AND IsApproved = 'Y'
      AND SalaryRenderingDate NOT IN
        (SELECT  
           SalaryRenderingDate
         FROM  
           UserSalaryData
         WHERE  
           ActivityTypeCategoryId = 1 --Work event types
           AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork',  
                                    'OvertimeDaily50', 'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100',  
                                    'OvertimeSunday50', 'OvertimeSunday100', 'PublicHoliday', 'YearLeave'))
    GROUP BY  
      ActivityId
    
[/code]
## Poimitaan tulkitut kokopäivän poissaoloina käsiteltävät tapahtumatyypit
Tällä esimerkkisäännöllä poimitaan kokopäivän poissaolot siten, että poissaolopäivällä ei ole työtyyppistä palkallista tai palkatonta aikaa.
[code] 
    SELECT  
      *,  
      SUM(Amount) AS OverrideAmount,   
      MIN(SalaryRenderingDate) As OverrideStartDatetime,   
      MAX(SalaryRenderingDate) AS OverrideEndDatetime,  
      CASE
        WHEN ActivityTypeCode = 16  THEN 'SALDOVAPAA' -- Saldovapaa
        WHEN ActivityTypeCode = 23 THEN 'LOMAUTUS' -- Lomautus    
        WHEN ActivityTypeCode = 29 THEN 'TYOAJANLYHENNYSVAPAA' -- Tyoajan lyhennysvapaa   
        WHEN ActivityTypeCode = 102 THEN 'PANKKIVAPAA' -- Pankkivapaa  
        WHEN ActivityTypeCode = 278 THEN 'YLITYOVAPAA' -- Ylityövapaa
        ELSE 'NOT DEFINED'
      END AS OverrideSalaryCode
    FROM  
      UserSalaryData 
    WHERE  
      ActivityTypeCode IN (16, 23, 29, 102, 278)  
      AND CompensationType NOT IN ('MarkedTime')
      AND SalaryRenderingDate NOT IN 
        (SELECT  
           SalaryRenderingDate 
         FROM  
           UserSalaryData 
         WHERE  
           ActivityTypeCategoryId = 1 --Work event types
           AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork',  
                                    'OvertimeDaily50', 'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100',  
                                    'OvertimeSunday50', 'OvertimeSunday100', 'PublicHoliday', 'YearLeave')) 
    GROUP BY  
      ActivityId
[/code]
## Poimitaan tulkitut kokopäivän poissaolotapahtumatyypin kirjaukset yhdellä säännöllä siten, että eri poissaololajeilla on oma palkkalajin koodinsa
Kokopäivän poissaolo tunnistetaan siten, että poissaolopäivällä ei ole muuta palkallista tai palkatonta työaikaa, eikä päivä ole loma- tai pyhäpäivä. Tulokset ryhmitellään per kirjattu poissaolo ja aineistossa siirtyy tulkittuna poissaolon alku ja loppupäivät. Korvaathan ' '-merkkien välissä olevan tekstin, esim. 'AMMATTIYHDISTYSTOIMINTA', oikealla palkkalajikoodilla.
[code] 
    SELECT  
      *,  
      SUM(Amount) AS OverrideAmount,   
      MIN(SalaryRenderingDate) As OverrideStartDatetime,   
      MAX(SalaryRenderingDate) AS OverrideEndDatetime,  
      CASE   
        WHEN AbsenceTypeId = 25 THEN 'AMMATTIYHDISTYSTOIMINTA' -- Ammattiyhdistystoiminta  
        WHEN AbsenceTypeId = 10 THEN 'ASEPALVELUS' -- Ase- tai siviilipalvelusaika  
        WHEN AbsenceTypeId = 1 THEN 'ERITYISAITIYSVAPAA' -- Erityisäitiysvapaa  
        WHEN AbsenceTypeId = 5 THEN 'HOITOVAPAA' -- Hoitovapaa  
        WHEN AbsenceTypeId = 3 THEN 'ISYYSVAPAA' -- Isyysvapaa  
        WHEN AbsenceTypeId = 11 THEN 'KERTAUS' -- Kertausharjoitukset  
        WHEN AbsenceTypeId = 27 THEN 'KUNTOUTUS' -- Kuntoutus  
        WHEN AbsenceTypeId = 18 THEN 'KUTSUNTA' -- Kutsuntatilaisuus  
        WHEN AbsenceTypeId = 13 THEN 'MUU_POISSAOLO' -- Muu poissaolo  
        WHEN AbsenceTypeId = 26 THEN 'MUUTTOVAPAA' -- Muuttovapaa  
        WHEN AbsenceTypeId = 452 THEN 'OMAISHOITOVAPAA' -- Omaishoitovapaa  
        WHEN AbsenceTypeId = 17 THEN 'OMAT50_60_JUHLAT' -- Omat 50- tai 60-vuotisjuhlat  
        WHEN AbsenceTypeId = 16 THEN 'PARISUHTEEN_REKISTEROINTI' -- Omat vihkiäiset / Parisuhteen rekisteröinti  
        WHEN AbsenceTypeId = 8 THEN 'OPINTOVAPAA' -- Opintovapaa  
        WHEN AbsenceTypeId = 22 THEN 'OSA_AIKAELAKE' -- Osa-aikaeläke  
        WHEN AbsenceTypeId = 31 THEN 'OSA-AIKAISUUS' -- Osa-aikaisuus  
        WHEN AbsenceTypeId = 14 THEN 'PERHEENJASENEN_KUOLEMA' -- Perheenjäsenen kuolema  
        WHEN AbsenceTypeId = 15 THEN 'HAUTAJAISET' -- Perheenjäsenen tai lähiomaisen hautajaiset  
        WHEN AbsenceTypeId = 20 THEN 'PERHEENJASENEN_SAIRASTUMINEN' -- Perheenjäsenen äkillinen sairastuminen  
        WHEN AbsenceTypeId = 7 THEN 'PAKOTTAVAT_PERHESYYT' -- Poissaolo pakottavien perhesyiden takia  
        WHEN AbsenceTypeId = 450 THEN 'RASKAUSVAPAA' -- Raskausvapaa  
        WHEN AbsenceTypeId = 6 THEN 'TILAPAINEN_HOITOVAPAA' -- Tilapäinen hoitovapaa  
        WHEN AbsenceTypeId = 19 THEN 'TOIMIVAPAA' -- Toimivapaa  
        WHEN AbsenceTypeId = 12 THEN 'TYONTEKIJAN_PYYNTO' -- Työntekijän oma pyyntö  
        WHEN AbsenceTypeId = 451 THEN 'VANHEMPAINVAPAA' -- Vanhempainvapaa  
        WHEN AbsenceTypeId = 4 THEN 'VANHEMPAINVAPAA (ENNEN UUDISTUSTA)' -- Vanhempainvapaa (ennen uudistusta)  
        WHEN AbsenceTypeId = 23 THEN 'VIRKAPAVAA' -- Virkavapaa  
        WHEN AbsenceTypeId = 9 THEN 'VUOROTTELUVAPAA' -- Vuorotteluvapaa  
        WHEN AbsenceTypeId = 2 THEN 'AITIYSVAPAA' -- Äitiysvapaa  
        ELSE 'NOT DEFINED'  
      END AS OverrideSalaryCode  
    FROM  
      UserSalaryData   
    WHERE  
      AbsenceTypeId IS NOT NULL  
      AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime')  
      AND SalaryRenderingDate NOT IN   
        (SELECT  
           SalaryRenderingDate   
         FROM  
           UserSalaryData   
         WHERE  
           ActivityTypeCategoryId = 1  
           AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork',  
                                    'OvertimeDaily50', 'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100',  
                                    'OvertimeSunday50', 'OvertimeSunday100', 'PublicHoliday', 'YearLeave'))   
    GROUP BY  
      ActivityId
[/code]
## Poimitaan tulkitut osapäivän poissaolo-tapahtumat yhdellä säännöllä siten, että eri poissaololajeilla on oma palkkalajin koodinsa
Poissaolo tunnistetaan siten, että poissaolopäivällä on myös muuta palkallista tai palkatonta aikaa, tai päivä on loma- tai pyhäpäivä. Tulokset ryhmitellään per kirjattu poissaolo ja aineistossa siirtyy tulkitun poissaolon alku ja loppupäivät. Korvaathan ' '-merkkien välissä olevan tekstin, esim. 'AMMATTIYHDISTYSTOIMINTA', oikealla palkkalajikoodilla.
[code] 
    SELECT  
      *,  
      SUM(Amount) AS OverrideAmount,   
      MIN(SalaryRenderingDate) As OverrideStartDatetime,   
      MAX(SalaryRenderingDate) AS OverrideEndDatetime,  
      CASE   
        WHEN AbsenceTypeId = 25 THEN 'AMMATTIYHDISTYSTOIMINTA' -- Ammattiyhdistystoiminta  
        WHEN AbsenceTypeId = 10 THEN 'ASEPALVELUS' -- Ase- tai siviilipalvelusaika  
        WHEN AbsenceTypeId = 1 THEN 'ERITYISAITIYSVAPAA' -- Erityisäitiysvapaa  
        WHEN AbsenceTypeId = 15 THEN 'HAUTAJAISET' -- Perheenjäsenen tai lähiomaisen hautajaiset  
        WHEN AbsenceTypeId = 5 THEN 'HOITOVAPAA' -- Hoitovapaa  
        WHEN AbsenceTypeId = 3 THEN 'ISYYSVAPAA' -- Isyysvapaa  
        WHEN AbsenceTypeId = 11 THEN 'KERTAUS' -- Kertausharjoitukset  
        WHEN AbsenceTypeId = 27 THEN 'KUNTOUTUS' -- Kuntoutus  
        WHEN AbsenceTypeId = 18 THEN 'KUTSUNTA' -- Kutsuntatilaisuus  
        WHEN AbsenceTypeId = 13 THEN 'MUU_POISSAOLO' -- Muu poissaolo  
        WHEN AbsenceTypeId = 26 THEN 'MUUTTOVAPAA' -- Muuttovapaa  
        WHEN AbsenceTypeId = 452 THEN 'OMAISHOITOVAPAA' -- Omaishoitovapaa  
        WHEN AbsenceTypeId = 17 THEN 'OMAT50_60_JUHLAT' -- Omat 50- tai 60-vuotisjuhlat  
        WHEN AbsenceTypeId = 8 THEN 'OPINTOVAPAA' -- Opintovapaa  
        WHEN AbsenceTypeId = 22 THEN 'OSA_AIKAELAKE' -- Osa-aikaeläke  
        WHEN AbsenceTypeId = 31 THEN 'OSA-AIKAISUUS' -- Osa-aikaisuus  
        WHEN AbsenceTypeId = 7 THEN 'PAKOTTAVAT_PERHESYYT' -- Poissaolo pakottavien perhesyiden takia  
        WHEN AbsenceTypeId = 16 THEN 'PARISUHTEEN_REKISTEROINTI' -- Omat vihkiäiset / Parisuhteen rekisteröinti  
        WHEN AbsenceTypeId = 14 THEN 'PERHEENJASENEN_KUOLEMA' -- Perheenjäsenen kuolema  
        WHEN AbsenceTypeId = 20 THEN 'PERHEENJASENEN_SAIRASTUMINEN' -- Perheenjäsenen äkillinen sairastuminen  
        WHEN AbsenceTypeId = 450 THEN 'RASKAUSVAPAA' -- Raskausvapaa  
        WHEN AbsenceTypeId = 6 THEN 'TILAPAINEN_HOITOVAPAA' -- Tilapäinen hoitovapaa  
        WHEN AbsenceTypeId = 19 THEN 'TOIMIVAPAA' -- Toimivapaa  
        WHEN AbsenceTypeId = 12 THEN 'TYONTEKIJAN_PYYNTO' -- Työntekijän oma pyyntö  
        WHEN AbsenceTypeId = 451 THEN 'VANHEMPAINVAPAA' -- Vanhempainvapaa  
        WHEN AbsenceTypeId = 4 THEN 'VANHEMPAINVAPAA (ENNEN UUDISTUSTA)' -- Vanhempainvapaa (ennen uudistusta)  
        WHEN AbsenceTypeId = 23 THEN 'VIRKAPAVAA' -- Virkavapaa  
        WHEN AbsenceTypeId = 9 THEN 'VUOROTTELUVAPAA' -- Vuorotteluvapaa  
        WHEN AbsenceTypeId = 2 THEN 'AITIYSVAPAA' -- Äitiysvapaa  
        ELSE 'NOT DEFINED'  
      END AS OverrideSalaryCode  
    FROM  
      UserSalaryData   
    WHERE  
      AbsenceTypeId IS NOT NULL  
      AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime')  
      AND SalaryRenderingDate IN   
        (SELECT  
           SalaryRenderingDate   
         FROM  
           UserSalaryData   
         WHERE  
           AbsenceTypeId IS NULL   
           AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork',  
                                    'OvertimeDaily50', 'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100',  
                                    'OvertimeSunday50', 'OvertimeSunday100', 'PublicHoliday', 'YearLeave'))   
    GROUP BY  
      ActivityId
[/code]
## Poimitaan kirjatut, eilen hyväksytyt, poissaolotapahtumat yhdellä säännöllä siten, että eri poissaololajeilla on oma palkkalajin koodinsa
Tulokset ryhmitellään per kirjattu poissaolo ja aineistossa siirtyy kirjatun poissaolon alku ja loppupäivät. Määränä siirretään kirjatun poissaolon kesto päivinä. Korvaathan ' '-merkkien välissä olevan tekstin, esim. 'AMMATTIYHDISTYSTOIMINTA', oikealla palkkalajikoodilla.
[code] 
    SELECT  
      *,   
      julianday(date(Enddatetime)) -   
      julianday(date(StartDatetime)) + 1 AS OverrideAmount, -- tämä laskee poissaolon keston päivinä  
      MIN(StartDateTime) As OverrideStartDatetime, -- poissaolon alkupäivä  
      MAX(EndDateTime) AS OverrideEndDatetime, -- poissaolon loppupäivä  
      CASE   
        WHEN AbsenceTypeId = 25 THEN 'AMMATTIYHDISTYSTOIMINTA' -- Ammattiyhdistystoiminta  
        WHEN AbsenceTypeId = 10 THEN 'ASEPALVELUS' -- Ase- tai siviilipalvelusaika  
        WHEN AbsenceTypeId = 1 THEN 'ERITYISAITIYSVAPAA' -- Erityisäitiysvapaa  
        WHEN AbsenceTypeId = 15 THEN 'HAUTAJAISET' -- Perheenjäsenen tai lähiomaisen hautajaiset  
        WHEN AbsenceTypeId = 5 THEN 'HOITOVAPAA' -- Hoitovapaa  
        WHEN AbsenceTypeId = 3 THEN 'ISYYSVAPAA' -- Isyysvapaa  
        WHEN AbsenceTypeId = 11 THEN 'KERTAUS' -- Kertausharjoitukset  
        WHEN AbsenceTypeId = 27 THEN 'KUNTOUTUS' -- Kuntoutus  
        WHEN AbsenceTypeId = 18 THEN 'KUTSUNTA' -- Kutsuntatilaisuus  
        WHEN AbsenceTypeId = 13 THEN 'MUU_POISSAOLO' -- Muu poissaolo  
        WHEN AbsenceTypeId = 26 THEN 'MUUTTOVAPAA' -- Muuttovapaa  
        WHEN AbsenceTypeId = 452 THEN 'OMAISHOITOVAPAA' -- Omaishoitovapaa  
        WHEN AbsenceTypeId = 17 THEN 'OMAT50_60_JUHLAT' -- Omat 50- tai 60-vuotisjuhlat  
        WHEN AbsenceTypeId = 8 THEN 'OPINTOVAPAA' -- Opintovapaa  
        WHEN AbsenceTypeId = 22 THEN 'OSA_AIKAELAKE' -- Osa-aikaeläke  
        WHEN AbsenceTypeId = 31 THEN 'OSA-AIKAISUUS' -- Osa-aikaisuus  
        WHEN AbsenceTypeId = 7 THEN 'PAKOTTAVAT_PERHESYYT' -- Poissaolo pakottavien perhesyiden takia  
        WHEN AbsenceTypeId = 16 THEN 'PARISUHTEEN_REKISTEROINTI' -- Omat vihkiäiset / Parisuhteen rekisteröinti  
        WHEN AbsenceTypeId = 14 THEN 'PERHEENJASENEN_KUOLEMA' -- Perheenjäsenen kuolema  
        WHEN AbsenceTypeId = 20 THEN 'PERHEENJASENEN_SAIRASTUMINEN' -- Perheenjäsenen äkillinen sairastuminen  
        WHEN AbsenceTypeId = 450 THEN 'RASKAUSVAPAA' -- Raskausvapaa  
        WHEN AbsenceTypeId = 6 THEN 'TILAPAINEN_HOITOVAPAA' -- Tilapäinen hoitovapaa  
        WHEN AbsenceTypeId = 19 THEN 'TOIMIVAPAA' -- Toimivapaa  
        WHEN AbsenceTypeId = 12 THEN 'TYONTEKIJAN_PYYNTO' -- Työntekijän oma pyyntö  
        WHEN AbsenceTypeId = 451 THEN 'VANHEMPAINVAPAA' -- Vanhempainvapaa  
        WHEN AbsenceTypeId = 4 THEN 'VANHEMPAINVAPAA (ENNEN UUDISTUSTA)' -- Vanhempainvapaa (ennen uudistusta)  
        WHEN AbsenceTypeId = 23 THEN 'VIRKAPAVAA' -- Virkavapaa  
        WHEN AbsenceTypeId = 9 THEN 'VUOROTTELUVAPAA' -- Vuorotteluvapaa  
        WHEN AbsenceTypeId = 2 THEN 'AITIYSVAPAA' -- Äitiysvapaa  
        ELSE 'NOT DEFINED'  
      END AS OverrideSalaryCode  
    FROM  
      UserEventData  
    WHERE  
      AbsenceTypeId IS NOT NULL  
      AND IsApproved = 'Y' -- On hyväksytty  
      AND DATE(ModifiedDatetime) = DATE(DATETIME(CURDATE(),'-1 DAY')) -- Hyväksymispäivä eilen  
    GROUP BY  
      ActivityId
[/code]
## Poimitaan juhlapyhän kesto
Poimitaan Juhlapyhän kesto silloin kun henkilö on työsuhteessa kyseisenä päivänä ja hän on tuntipalkkainen. Esimerkin vuoksi itsenäisyyspäivää (6. joulukuuta) ei poimita.
[code] 
    SELECT  
      *,  
      SUM(Amount) AS OverrideAmount  
    FROM  
      UserSalaryData  
    WHERE  
      CompensationType = 'PublicHoliday'  
      AND employeeworkcontractactive = 'Y'   
      AND employeesalarytype = 'hourly'  
      AND strftime('%m-%d', salaryrenderingdate ) != '12-06'   
    GROUP BY  
      SalaryRenderingDate,  
      ProjectCode1,  
      Comment
[/code]
## Poimitaan juhlapyhän kesto vähennettynä tehdyllä työllä
Poimitaan Juhlapyhän kesto silloin kun henkilö on työsuhteessa kyseisenä päivänä ja hän on tuntipalkkainen. Juhlapyhän kestosta vähennetään kyseiselle päivälle kirjattu työaika korvauslajista riippumatta.
[code] 
    SELECT   
      *,   
      SUM(Amount) - IFNULL(WorkDoneOnDayAmount, 0) AS OverrideAmount -- Amount of public holiday is reduced by amount of work done on that day  
    FROM   
      UserSalaryData   
    LEFT JOIN  --In this left join section we fetch the amount of compensation on any of the mentioned types and sum it per day. This information is joined into salaryData table  
      (SELECT   
         SUM(Amount) As WorkDoneOnDayAmount,  
         SalaryRenderingDate AS WorkDoneOnDaySalaryRenderingDate  
       FROM   
         UserSalaryData   
       WHERE   
         CompensationType IN ('BasicTime', 'ReducedRateTime', 'AdditionalWork', 'OvertimeDaily50', 'OvertimeDaily100',  
                              'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50', 'OvertimeSunday100')   
       GROUP By   
         SalaryRenderingDate) AS WorkDonePerDay ON UserSalaryData.SalaryRenderingDate = WorkDonePerDay.WorkDoneOnDaySalaryRenderingDate   
    WHERE   
      CompensationType = 'PublicHoliday'   
      AND employeeworkcontractactive = 'Y'   
    GROUP BY   
      SalaryRenderingDate,   
      ProjectCode1,   
      Comment
[/code]
## Poimitaan juhlapyhän kesto niiltä päiviltä, jolloin henkilö on työsuhteessa ja työsuhde on kestänyt yli 1kk ajan
[code] 
    SELECT  
      *,  
      SUM(Amount) AS OverrideAmount FROM UserSalaryData
    WHERE  
      CompensationType = 'PublicHoliday'  
      AND EmployeeWorkContractActive = 'Y'
      AND SalaryRenderingDate >= DATE(EmployeeWorkContractStartDate, '+1 month')
    GROUP BY  
      SalaryRenderingDate,  
      ProjectCode1,  
      ProjectCode2,  
      ProjectCode3,  
      ProjectCode4,
      ProjectCode5,  
      ProjectCode6,  
      Comment
    
[/code]
