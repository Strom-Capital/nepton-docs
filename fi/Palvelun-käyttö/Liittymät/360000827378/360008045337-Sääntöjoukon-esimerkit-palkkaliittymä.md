---
id: 360008045337
title: Sääntöjoukon esimerkit - palkkaliittymä
url: https://support.nepton.com/hc/fi/articles/360008045337-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-palkkaliittym%C3%A4
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels:
- sääntöjoukko
- poimintasäännöt
- palkkaliittymä
- poiminta
promoted: false
updated_at: '2026-02-25T10:46:44Z'
edited_at: '2026-02-25T10:45:57Z'
---

# Sääntöjoukon esimerkit - palkkaliittymä

Huomoithan, että poimintasääntöjen luominen ja muokkaaminen edellyttää perustason ymmärrystä SQL:stä.
Tähän artikkeliin on koottu tyypillinen palkkaliittymän malli. Tässä mallissa on esitetty parhaat käytännöt palkkaliittymän määrittelyyn, jossa yhdellä säännöllä poimitaan kerralla kokonaisuus - esimerkiksi kaikki ylityöt. Säännöt voidaan hyödyntää sellaisenaan palkkaliittymissä, mutta niihin tulee huomioida kohdejärjestelmän vaatimukset esimerkiksi tiedon ryhmittelyn ja mahdollisten järjestelmäkohtaisten tietokenttien osalta.
  * [Tässä artikkelissa](<https://support.nepton.com/hc/fi/articles/21077132021149>) käydään läpi sääntöjoukon poiminnan perusperiaatteet.  
Lisäksi artikkelissa käydään läpi poimintasääntöihin useimmiten tarvittavat lisäsäännöt.  

  * Tietokantataulujen sarakekuvaukset löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>).  

  * Muita sääntöjoukon esimerkkejä löydät seuraavista artikkeleista:  
  
[Poissaololiittymän poiminnan malli](<https://support.nepton.com/hc/fi/articles/360013979998>)  
[Projektirakenteen ja projektien huomiointi poiminnassa](<https://support.nepton.com/hc/fi/articles/360013894637>)  
[Henkilötietojen poiminnan malli](<https://support.nepton.com/hc/fi/articles/360015612638>)


### Henkilötietojen (UserInfoData) poiminta
Jos henkilötieto liitetään JOIN-lausekkeella väärin, se helposti johtaa palkka-aineiston tuntimäärien moninkertaistumiseen.
Jos on tarve poimia useampia henkilötietoja, tarvitaan useampi JOIN-lauseke.
Seuraavaa tapaa voi käyttää, jolla on myös helpompi poimia useampi henkilötieto:
[code]
    SELECT
      usd.*,
      SUM(Amount) AS OverrideAmount,
    -- Henkilöryhmän koodi, valittu CustomData1 -tietoon
      IFNULL(
        (SELECT
           uid.Value
         FROM
           UserInfoData uid
         WHERE uid.InfoTypeName = 'UserGroupCode_SDSQL'
         AND datetime(usd.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo
         LIMIT 1), '') AS CustomData1,
    -- Maksuryhmän koodi, valittu CustomData2 -tietoon
      IFNULL(
        (SELECT
           uid.Value
         FROM
           UserInfoData uid
         WHERE
           uid.InfoTypeName = 'NeptonPaymentGroupCode_SDSQL'
           AND datetime(usd.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo
         LIMIT 1), '') AS CustomData2
    FROM
      UserSalaryData usd
    GROUP BY
      usd.SalaryRenderingDate,
      usd.CompensationType,
      usd.ProjectCode1
[/code]
## Sääntöjoukon malli
Sääntöjoukolle perustetaan mallin mukaisesti seuraavat poimintasäännöt. Poimintasäännöt ovat ryhmitelty siten, että kukin sääntö poimii aineistokokonaisuuden kerralla, kuten ylityöt tai sairauspoissaolot. Mallin mukaista sääntöä tulee muokata siten, että se sisältää oikeat järjestelmä- tai asiakaskohtaiset palkkalajit ja halutun ryhmittelyn.
### Toteutunut työ ilman ylitöitä (tuntipalkka)
Poimitaan kaikki tapahtumat, jotka huomioidaan säännölliseen työaikaan (CompensationType = 'BasicTime'), sekä saldosta lainattu aika.
[code]
    SELECT
      *, 
      SUM(Amount) As OverrideAmount
    FROM 
      UserSalaryData
    WHERE
      (ActivityTypeCategoryId = 1
      AND CompensationType = 'BasicTime'
      AND BasePartTarget = 'salary'
      AND (OvertimeTarget IS NULL OR OvertimeTarget = 'uncompensated')) -- Tehty työaika
      OR
      (BasePartTarget = 'salary' AND ActivityTypeCode IS NULL AND IsTimeBorrowedFromBAlance = 'Y') -- Saldosta lainattu
    --  AND EmployeeSalaryType = 'hourly'
    GROUP BY 
      SalaryRenderingDate
[/code]
Jos tuloksia on tarve ryhmitellä päivän (SalaryRenderingDate) lisäksi projektin mukaan, GROUP BY -osioon lisätään tarpeen mukaan ProjectCode1, ProjectCode2, ProjectCode3, ProjectCode4, ProjectCode5, ProjectCode6.
[code]
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6
[/code]
Mikäli palkkajärjestelmässä on tärkeää eritellä tapahtumalle tehty kuvaus, niin siinä tapauksessa ryhmitellään vielä per kuvaus (Comment).
[code]
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
[/code]
### Toteutunut ylityö
Poimitaan kaikki tapahtumat, joissa muodostuu ylityötä, jonka perusosa sekä korotusosa maksetaan palkkana.
Mikäli poimittu aineisto sisältää sellaisia rivejä, joiden palkkalajia ei ole otettu huomioon aineistossa niin ne tulevat palkkalajilla 'NOT_DEFINED'
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      CASE
        BasePartTarget = 'salary' AND OvertimeTarget = 'salary' 
        WHEN CompensationType = 'AdditionalWork' AND OvertimePercentage = 0 THEN 'LISÄTYÖ0%_PALKKALAJI' -- lisätyö0%
        WHEN CompensationType = 'AdditionalWork' AND OvertimePercentage = 50 THEN 'LISÄTYÖ50%_PALKKALAJI' -- lisätyö50%
        WHEN CompensationType = 'OvertimeDaily50' THEN  'VRK50_PALKKALAJI' -- vrk50
        WHEN CompensationType = 'OvertimeDaily100' THEN 'VRK100_PALKKALAJI' -- vrk100
        WHEN CompensationType = 'OvertimeWeekly50' THEN 'VK50_PALKKALAJI' -- vk50
        WHEN CompensationType = 'OvertimeWeekly100' THEN 'VK100_PALKKALAJI' -- vk100
        WHEN CompensationType = 'OvertimeSunday50' THEN 'SUNNUNTAI50_PALKKALAJI' -- Sunnuntai50
        WHEN CompensationType = 'OvertimeSunday100' THEN 'SUNNUNTAI100_PALKKALAJI' -- Sunnuntai100
        WHEN CompensationType = 'OvertimeBaseFixed' THEN 'BASEFIXED_PALKKALAJI' -- Base fixed
        WHEN CompensationType = 'OvertimeExtraFixed' THEN 'EXTRAFIXED_PALKKALAJI' -- Extra fixed
        WHEN CompensationType = 'LevellingPeriodAdditional' THEN 'TASOITTUMISJAKSOLISATYO_PALKKALAJI' -- Levelling period additional work
        WHEN CompensationType = 'LevellingPeriodOvertime50' THEN 'TASOITTUMISJAKSOYLITYO50_PALKKALAJI' -- Levelling period overtime 50
        WHEN CompensationType = 'LevellingPeriodOvertime100' THEN 'TASOITTUMISJAKSOYLITYO100_PALKKALAJI' -- Levelling period overtime 100
        ELSE 'NOT_DEFINED'
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('AdditionalWork', 'OvertimeDaily50', 'OvertimeDaily100', 'OvertimeWeekly50',
                           'OvertimeWeekly100', 'OvertimeSunday50', 'OvertimeSunday100',
                           'OvertimeBaseFixed', 'OvertimeExtraFixed', 'TESOvertime50', 'TESOvertime100',
                           'LevellingPeriodAdditional', 'LevellingPeriodOvertime50', 'LevellingPeriodOvertime100')
      AND BasePartTarget = 'salary'
      AND OvertimeTarget = 'salary'
      AND IsApproved = 'Y'
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Työkorotukset
Poimitaan kaikki työkorotukset ja asetetaan työkorotuksen palkkalajiksi korotukselle asetettu palkkalajikoodi. Työkorotuksen koodiksi on mahdollista asettaa palkkalaji / - viivalla jaoteltuna esimerkiksi siten, että
  * ensimmäinen osa kuvaa palkkalajia säännöllisellä työajalla
  * toinen osa kuvaa palkkalajia 50% ylityön ajalta
  * kolmas osa kuvaa palkkaljia 100% ylityön ajalta


Työkorotuksen koodia ei kuitenkaan tarvitse jakaa tällä tavalla, vaan sääntö poimii kaikissa tapauksissa koodin sellaisenaan, vaikka jaottelua ei ole tehty.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      CASE
        WHEN instr(WorkRiseSalaryCode,'/') = 0 OR WorkRiseEarnedAtCompensationType = 'BasicTime' THEN substring_part(WorkRiseSalaryCode, '/', 1)
        WHEN WorkRiseEarnedAtCompensationType IN ('OvertimeDaily50','OvertimeWeekly50','OvertimeSunday50') THEN substring_part(WorkRiseSalaryCode, '/', 2)
        ELSE substring_part(WorkRiseSalaryCode, '/', 3) 
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'WorkRise' 
      AND workrisepaytarget = 'Salary'
      AND IsApproved = 'Y'
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Työlisät
Poimitaan kaikki työlisät ja asetetaan työlisän palkkalajiksi työlisälle asetettu palkkalajikoodi.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      WorkIncrementCode as OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'WorkIncrement' 
      AND IsApproved = 'Y'
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Osapäivän sairauspoissaolot
Poimitaan kaikki osapäivän sairauspoissaolot
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
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
        WHEN SickLeaveTypeId IS NOT NULL THEN ('Sairauspoissaolo: ' || SickLeaveTypeId || ' - ' || CompensationType) --this row picks up all sick leaves´types that are not picked up by the rule already
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('BasicTime','UnpaidBasicTime')
      AND SickLeaveTypeId IS NOT NULL
      AND IsApproved = 'Y'
    -- Alla oleva ehto jättää tuloksista pois ne päivät, joissa työaikaa on korvattu työnä
      AND SalaryRenderingDate IN 
        (SELECT
           SalaryRenderingDate 
         FROM
           UserSalaryData 
         WHERE
           ActivityTypeCategoryId = 1
           AND CompensationType IN ('BasicTime', 'AdditionalWork', 'OvertimeDaily50', 'OvertimeDaily100',
                                    'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50', 'OvertimeSunday100'))
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Osapäivän poissaolot
Poimitaan kaikki osapäivän poissaolot
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      CASE
        WHEN AbsenceTypeId = 25 AND CompensationType = 'UnpaidBasicTime' THEN 'AMMATTIYHDISTYSTOIMINTA_PALKATON' -- Palkaton ammattiyhdistystoiminta 
        WHEN AbsenceTypeId = 10 AND CompensationType = 'UnpaidBasicTime' THEN 'ASEPALVELUS_PALKATON' -- Palkaton ase- tai siviilipalvelusaika 
        WHEN AbsenceTypeId = 1 AND CompensationType = 'UnpaidBasicTime' THEN 'ERITYISAITIYSVAPAA_PALKATON'-- Palkaton erityisäitiysvapaa 
        WHEN AbsenceTypeId = 5 AND CompensationType = 'UnpaidBasicTime' THEN 'HOITOVAPAA_PALKATON'-- Palkaton hoitovapaa 
        WHEN AbsenceTypeId = 3 AND CompensationType = 'UnpaidBasicTime' THEN 'ISYYSVAPAA_PALKATON'-- Palkaton isyysvapaa 
        WHEN AbsenceTypeId = 11 AND CompensationType = 'UnpaidBasicTime' THEN 'KERTAUS_PALKATON'-- Palkaton kertausharjoitus
        WHEN AbsenceTypeId = 27 AND CompensationType = 'UnpaidBasicTime' THEN 'KUNTOUTUS_PALKATON' -- Palkaton kuntoutus 
        WHEN AbsenceTypeId = 18 AND CompensationType = 'UnpaidBasicTime' THEN 'KUTSUNTA_PALKATON' -- Palkaton kutsuntatilaisuus 
        WHEN AbsenceTypeId = 13 AND CompensationType = 'UnpaidBasicTime' THEN 'MUU_POISSAOLO_PALKATON' -- Palkaton muu poissaolo 
        WHEN AbsenceTypeId = 26 AND CompensationType = 'UnpaidBasicTime' THEN 'MUUTTOVAPAA_PALKATON' -- Palkaton muuttovapaa 
        WHEN AbsenceTypeId = 452 AND CompensationType = 'UnpaidBasicTime' THEN 'OMAISHOITOVAPAA_PALKATON' -- Palkaton omaishoitovapaa
        WHEN AbsenceTypeId = 17 AND CompensationType = 'UnpaidBasicTime' THEN 'OMAT50_60_JUHLAT_PALKATON' -- Palkaton oma 50- tai 60-vuotisjuhla
        WHEN AbsenceTypeId = 16 AND CompensationType = 'UnpaidBasicTime' THEN 'PARISUHTEEN_REKISTEROINTI_PALKATON' -- Palkaton omat vihkiäiset / parisuhteen rekisteröinti 
        WHEN AbsenceTypeId = 8 AND CompensationType = 'UnpaidBasicTime' THEN 'OPINTOVAPAA_PALKATON' -- Palkaton opintovapaa 
        WHEN AbsenceTypeId = 22 AND CompensationType = 'UnpaidBasicTime' THEN 'OSA_AIKAELAKE_PALKATON' -- Palkaton osa-aikaeläke 
        WHEN AbsenceTypeId = 31 AND CompensationType = 'UnpaidBasicTime' THEN 'OSA-AIKAISUUS_PALKATON' -- Palkaton osa-aikaisuus 
        WHEN AbsenceTypeId = 14 AND CompensationType = 'UnpaidBasicTime' THEN 'PERHEENJASENEN_KUOLEMA_PALKATON' -- Palkaton perheenjäsenen kuolema 
        WHEN AbsenceTypeId = 15 AND CompensationType = 'UnpaidBasicTime' THEN 'HAUTAJAISET_PALKATON' -- Palkaton perheenjäsenen tai lähiomaisen hautajaiset 
        WHEN AbsenceTypeId = 20 AND CompensationType = 'UnpaidBasicTime' THEN 'PERHEENJASENEN_SAIRASTUMINEN_PALKATON' -- Palkaton perheenjäsenen äkillinen sairastuminen 
        WHEN AbsenceTypeId = 7 AND CompensationType = 'UnpaidBasicTime' THEN 'PAKOTTAVAT_PERHESYYT_PALKATON' -- Palkaton poissaolo pakottavien perhesyiden takia 
        WHEN AbsenceTypeId = 450 AND CompensationType = 'UnpaidBasicTime' THEN 'RASKAUSVAPAA_PALKATON' -- Palkaton raskausvapaa
        WHEN AbsenceTypeId = 6 AND CompensationType = 'UnpaidBasicTime' THEN 'TILAPAINEN_HOITOVAPAA_PALKATON' -- Palkaton tilapäinen hoitovapaa 
        WHEN AbsenceTypeId = 19 AND CompensationType = 'UnpaidBasicTime' THEN 'TOIMIVAPAA_PALKATON' -- Palkaton toimivapaa 
        WHEN AbsenceTypeId = 12 AND CompensationType = 'UnpaidBasicTime' THEN 'TYONTEKIJAN_PYYNTO_PALKATON' -- Palkaton työntekijän oma pyyntö 
        WHEN AbsenceTypeId = 451 AND CompensationType = 'UnpaidBasicTime' THEN 'VANHEMPAINVAPAA_PALKATON' -- Palkaton vanhempainvapaa
        WHEN AbsenceTypeId = 4 AND CompensationType = 'UnpaidBasicTime' THEN 'VANHEMPAINVAPAA_PALKATON'-- Palkaton vanhempainvapaa 
        WHEN AbsenceTypeId = 23 AND CompensationType = 'UnpaidBasicTime' THEN 'VIRKAPAVAA_PALKATON' -- Palkaton virkavapaa 
        WHEN AbsenceTypeId = 9 AND CompensationType = 'UnpaidBasicTime' THEN 'VUOROTTELUVAPAA_PALKATON' -- Palkaton vuorotteluvapaa 
        WHEN AbsenceTypeId = 2 AND CompensationType = 'UnpaidBasicTime' THEN 'AITIYSVAPAA_PALKATON' -- Palkaton äitiysvapaa
        WHEN AbsenceTypeId = 25 AND CompensationType = 'BasicTime' THEN 'AMMATTIYHDISTYSTOIMINTA_PALKALLINEN' -- Palkallinen ammattiyhdistystoiminta
        WHEN AbsenceTypeId = 10 AND CompensationType = 'BasicTime' THEN 'ASEPALVELUS_PALKALLINEN' -- Palkallinen ase- tai siviilipalvelusaika
        WHEN AbsenceTypeId = 1 AND CompensationType = 'BasicTime' THEN 'ERITYISAITIYSVAPAA_PALKALLINEN'-- Palkallinen erityisäitiysvapaa
        WHEN AbsenceTypeId = 5 AND CompensationType = 'BasicTime' THEN 'HOITOVAPAA_PALKALLINEN'-- Palkallinen hoitovapaa
        WHEN AbsenceTypeId = 3 AND CompensationType = 'BasicTime' THEN 'ISYYSVAPAA_PALKALLINEN'-- Palkallinen isyysvapaa 
        WHEN AbsenceTypeId = 11 AND CompensationType = 'BasicTime' THEN 'KERTAUS_PALKALLINEN'-- Palkallinen kertausharjoitus
        WHEN AbsenceTypeId = 27 AND CompensationType = 'BasicTime' THEN 'KUNTOUTUS_PALKALLINEN' -- Palkallinen kuntoutus
        WHEN AbsenceTypeId = 18 AND CompensationType = 'BasicTime' THEN 'KUTSUNTA_PALKALLINEN' -- Palkallinen kutsuntatilaisuus
        WHEN AbsenceTypeId = 13 AND CompensationType = 'BasicTime' THEN 'MUU_POISSAOLO_PALKALLINEN' -- Palkallinen muu poissaolo
        WHEN AbsenceTypeId = 26 AND CompensationType = 'BasicTime' THEN 'MUUTTOVAPAA_PALKALLINEN' -- Palkallinen muuttovapaa
        WHEN AbsenceTypeId = 452 AND CompensationType = 'BasicTime' THEN 'OMAISHOITOVAPAA_PALKALLINEN' -- Palkallinen omaishoitovapaa
        WHEN AbsenceTypeId = 17 AND CompensationType = 'BasicTime' THEN 'OMAT50_60_JUHLAT_PALKALLINEN' -- Palkallinen oma 50- tai 60-vuotisjuhla
        WHEN AbsenceTypeId = 16 AND CompensationType = 'BasicTime' THEN 'PARISUHTEEN_REKISTEROINTI_PALKALLINEN' -- Palkallinen omat vihkiäiset / parisuhteen rekisteröinti
        WHEN AbsenceTypeId = 8 AND CompensationType = 'BasicTime' THEN 'OPINTOVAPAA_PALKALLINEN' -- Palkallinen opintovapaa
        WHEN AbsenceTypeId = 22 AND CompensationType = 'BasicTime' THEN 'OSA_AIKAELAKE_PALKALLINEN' -- Palkallinen osa-aikaeläke
        WHEN AbsenceTypeId = 31 AND CompensationType = 'BasicTime' THEN 'OSA-AIKAISUUS_PALKALLINEN' -- Palkallinen osa-aikaisuus
        WHEN AbsenceTypeId = 14 AND CompensationType = 'BasicTime' THEN 'PERHEENJASENEN_KUOLEMA_PALKALLINEN' -- Palkallinen perheenjäsenen kuolema
        WHEN AbsenceTypeId = 15 AND CompensationType = 'BasicTime' THEN 'HAUTAJAISET_PALKALLINEN' -- Palkallinen perheenjäsenen tai lähiomaisen hautajaiset
        WHEN AbsenceTypeId = 20 AND CompensationType = 'BasicTime' THEN 'PERHEENJASENEN_SAIRASTUMINEN_PALKALLINEN' -- Palkallinen perheenjäsenen äkillinen sairastuminen
        WHEN AbsenceTypeId = 7 AND CompensationType = 'BasicTime' THEN 'PAKOTTAVAT_PERHESYYT_PALKALLINEN' --Palkallinen poissaolo pakottavien perhesyiden takia
        WHEN AbsenceTypeId = 450 AND CompensationType = 'BasicTime' THEN 'RASKAUSVAPAA_PALKALLINEN' --Palkallinen raskausvapaa
        WHEN AbsenceTypeId = 6 AND CompensationType = 'BasicTime' THEN 'TILAPAINEN_HOITOVAPAA_PALKALLINEN' -- Palkallinen tilapäinen hoitovapaa
        WHEN AbsenceTypeId = 19 AND CompensationType = 'BasicTime' THEN 'TOIMIVAPAA_PALKALLINEN' -- Palkallinen toimivapaa
        WHEN AbsenceTypeId = 12 AND CompensationType = 'BasicTime' THEN 'TYONTEKIJAN_PYYNTO_PALKALLINEN' -- Palkallinen työntekijän oma pyyntö
        WHEN AbsenceTypeId = 451 AND CompensationType = 'BasicTime' THEN 'VANHEMPAINVAPAA_PALKALLINEN' -- Palkallinen vanhempainvapaa
        WHEN AbsenceTypeId = 4 AND CompensationType = 'BasicTime' THEN 'VANHEMPAINVAPAA_PALKALLINEN'-- Palkallinen vanhempainvapaa
        WHEN AbsenceTypeId = 23 AND CompensationType = 'BasicTime' THEN 'VIRKAPAVAA_PALKALLINEN' -- Palkallinen virkavapaa
        WHEN AbsenceTypeId = 9 AND CompensationType = 'BasicTime' THEN 'VUOROTTELUVAPAA_PALKALLINEN' -- Palkallinen vuorotteluvapaa
        WHEN AbsenceTypeId = 2 AND CompensationType = 'BasicTime' THEN 'AITIYSVAPAA_PALKALLINEN' -- Palkallinen äitiysvapaa
        WHEN AbsenceTypeId IS NOT NULL THEN ('Poissaolo: ' || AbsenceTypeId || ' - ' || CompensationType) --this row picks up all absence types set up by the customer without a specific salary code set
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('BasicTime','UnpaidBasicTime')
      AND AbsenceTypeID IS NOT NULL
      AND IsApproved = 'Y'
      AND SalaryRenderingDate IN 
      (SELECT
         SalaryRenderingDate 
       FROM
         UserSalaryData 
       WHERE
         ActivityTypeCategoryId = 1
         AND CompensationType IN ('BasicTime', 'AdditionalWork', 'OvertimeDaily50', 'OvertimeDaily100',
                                  'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50', 'OvertimeSunday100'))
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Viikkolepo, arkipyhä
Poimitaan viikkolepo, arkipyhä
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount,
      CASE 
        WHEN CompensationType = 'WeeklyRestTime' THEN 'VIIKKOLEPO'
        WHEN CompensationType = 'PublicHoliday' THEN 'ARKIPYHÄ'
      END AS OverrideSalaryCode
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('WeeklyRestTime', 'PublicHoliday')
      AND IsApproved = 'Y'
    GROUP BY
      SalaryRenderingDate,
      OverrideSalaryCode,
      ProjectCode1,
      ProjectCode2,
      ProjectCode3,
      ProjectCode4,
      ProjectCode5,
      ProjectCode6,
      Comment
    HAVING
      Overridesalarycode != 0
[/code]
### Varallaolo vähennettynä varallaoloaikana tehdyllä työllä
Alla oleva kysely poimii varallaoloajan. Varallaoloajan päälle kirjatut tapahtumat vähennetään varallaoloajasta, mutta järjestelmän asetusten kautta on mahdollista määrittää että tietyt tapahtumatyypit eivät vähennä varallaoloaikaa. Varallaolon asetuksista voit lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/8040695057821>)
Tarvittaessa voit lisätä kyselyyn ryhmittelyn (GROUP BY) ja määrän yhteenlaskun mikäli et halua jokaista yksittäistä kestoa ja ajanjaksoa. 
Huom. Tämä esimerkki muuttui järjestelmän 2.12.0 päivityksen myötä. Vanhentunut malli toimii edelleen mutta sen käyttämista uusille liittymille ei suositella. Vanhan mallin mukaisen esimerkin löydät [täältä](<https://support.nepton.com/hc/fi/articles/8405862536349>)
[code]
    SELECT
      *
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'OnCall'
[/code]
### Aloitus- ja lopetustyö
[code]
    SELECT
      *
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'StartupWork'
[/code]
[code]
    SELECT
      *
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'TerminationWork'
[/code]
## Muita esimerkkipoimintoja
Esimerkkipoiminnoissa on yksittäisiä esimerkkejä erilaisiin erikoistilanteisiin. Näitä esimerkkejä voi soveltaa mallissa, mikäli asiakaskohtainen toteutus vaatii esimerkissä kuvatun kaltaisia poikkeuksia.
### Poimitaan työaika siten, että muodostetaan eri kustannuspaikan aineisto riippuen siitä päivästä milloin aineisto muodostetaan
Where - ehdossa on kuvattu että 6. päivä poimitaan kustannuspaikan 10 henkilöt ja 14. päivä poimitaan kustannuspaikan 20 henkilöt.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'BasicTime'
      AND
      CASE --in here define the list of day numbers and the corresponding UserCostGroup we wish to pick 
        WHEN strftime('%d', 'now') = '06' THEN UserCostGroup = '10' 
        WHEN strftime('%d','now') = '14' THEN UserCostGroup = '20'
      END
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
### Poimitaan saldokertymän arvo kuukauden viimeisenä päivänä
Where - ehdossa on kuvattu, että laskentapäivän tulee olla kuukauden viimeinen päivä. Vain silloin muodostuu tulos, johon poimitaan saldo-kertymän arvo.
[code]
    SELECT
      *,
      SUM(Amount) As OverrideAmount
    FROM
      UserSalaryData
    WHERE 
      CompensationType = 'Accrual'
      AND AccrualType = 'Balance'
      AND SalaryRenderingDate = date(salaryrenderingDate, 'start of month', '+1 month', '-1 day') -- this rule calculates the last day of the month
    GROUP BY
     SalaryRenderingDate
[/code]
### Poimitaan saldokertymän arvo ajojakson viimeiseltä päivältä
[code]
    SELECT
      Amount AS OverrideAmount
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'Accrual'
      AND AccrualType = 'Balance'
      AND SalaryRenderingDate = DATE(:ExportPeriodEnd) --poimitaan kertymän arvo ajojakson viimeiseltä päivältä
    GROUP BY
      UserId
[/code]
### Poimitaan henkilöryhmät mukaan aineistoon
Where - ehdossa on kuvattu että poimitaan henkilöryhmät A100, B100, C100, D100.
[code]
    SELECT ...,
    IFNULL(
      (SELECT
         uid.Value
       FROM
         UserInfoData uid
       WHERE
         uid.InfoTypeName = 'UserGroupCode_SDSQL' AND
         datetime(UserSalaryData.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo
        LIMIT 1), '') AS _UserGroupCode,
    FROM
      UserSalaryData
    WHERE
      _UserGroupCode IN ('A100', 'B100', 'C100', 'D100')
[/code]
### Poimitaan määräksi se tieto kuinka monena päivänä henkilö on tehnyt säännöllistä työaikaa tai ylitöitä
[code]
    SELECT
      *,
      COUNT(DISTINCT(SalaryRenderingDate)) As OverrideAmount,
      'J' AS OverrideUnitType -- siirretään määrä päivinä
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('BasicTime', 'AdditionalWork', 'OvertimeDaily50', 'OvertimeDaily100',
                           'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50', 'OvertimeSunday100')
      AND BasePartTarget IN ('salary','bank','balance','flexiblehours')
      AND ActivityTypeCategoryId = 1
    GROUP BY
      UserId
    HAVING
      OverrideAmount > 0 -- Mikäli tämän ehdon arvo on numeerinen (kuten Amount), ei nollan ympärillä saa käyttää heittomerkkejä ('0')
[/code]
### Poimitaan tietoa siten, että projektikoodiksi voidaan määritellä arvo perustuen työlisän numeroon
[code]
    SELECT
      *,
      SUM(amount) AS OverrideAmount,
      CASE 
        WHEN WorkIncrementNumber = 10 THEN '5000'
        WHEN WorkIncrementNumber = 30 THEN '6000'
        WHEN WorkIncrementNumber = 50 THEN '7000'
        ELSE 0
      END AS OverrideProjectCode1
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'workincrement'
[/code]
### Poimitaan tietoa siten, että projektikoodiksi määritellään projektin ulkoinen tunniste
[code]
    SELECT
      *,
      SUM(amount) AS OverrideAmount,
      ProjectExternalIdentifier1 AS OverrideProjectCode1
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'BasicTime'
[/code]
### Poimitaan 'saldon muutos' tapahtumat ja siirretään arvona muutoksen itseisarvo
[code]
    SELECT
      *,
      ABS(amount) AS OverrideAmount
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 13
[/code]
### Poimitaan matkalasku (myös muut työlisät poimitaan, ellei WorkIncrementType-kohtaa päivitetä, kts. alla)
[code]
    SELECT 
      *, 
      SUM(amount) AS OverrideAmount, 
      WorkIncrementCode AS OverrideSalaryCode -- Use the salary code from the Työlisät settings
    FROM 
      UserSalaryData 
    WHERE 
      CompensationType = 'WorkIncrement' 
      AND WorkIncrementCode IS NOT NULL -- Export all supplements unless they have been explicitly set not to be exported 
      AND WorkIncrementType = ??? -- If you ONLY want travel invoice supplements you can specify the types you wish here
    GROUP BY 
      SalaryRenderingDate, 
      Workincrementcode, 
      UnitType -- Ensures that if the supplement type changes, the old and new values aren't summed together
    
    
[/code]
### Poimitaan kertymät
[code]
    SELECT
      *,
      Amount AS OverrideAmount
    FROM
      UserSalaryData
    WHERE
      CompensationType = 'Accrual'
      AND AccrualType = 'balance' --Tässä poimitaan ainoastaan Saldo
[/code]
### Poimitaan Saldo-kertymän leikattu määrä
Tässä säännössä poimitaan Saldo-kertymän maksimäärän vuoksi henkilön Saldo-kertymästä leikattu määrä. 
[code]
    SELECT
      usd.*,
      usd.amount + COALESCE(usd2.sumAmount, 0) AS OverrideAmount
    FROM
    UserSalaryData usd
    LEFT JOIN
      (SELECT 
         salaryRenderingDate, 
         COALESCE(SUM(
           CASE
             WHEN compensationType = 'BasicTime' AND basePartTarget = 'balance' AND overtimeTarget = 'uncompensated' THEN - amount
             ELSE amount
           END), 0) AS SumAmount 
    FROM 
      UserSalaryData 
    WHERE 
      compensationType = 'BasicTime' 
      AND isTimeBorrowedFromBalance = 'Y' 
      AND (ActivityTypeId IS NULL 
         OR
          (compensationType = 'BasicTime' 
           AND basePartTarget = 'balance' 
           AND overtimeTarget = 'uncompensated')) 
    GROUP BY 
      salaryRenderingDate) usd2 ON usd.salaryRenderingDate = usd2.salaryRenderingDate 
    WHERE 
      usd.compensationType = 'AccrualChange' 
      AND usd.accrualType = 'Balance' 
    GROUP BY 
      usd.accrualType
[/code]
### Poimitaan lomarahavapaa myös lauantailta, jolla ei työvelvoitetta
Tässä säännössä poimitaan poikkeuksellisesti merkittyä työaikaa (''MarkedTime'') päivinä. Sääntöön on tehty myös poikkeus, että sunnuntaita ei oteta mukaan lukuun eli aineistolle nousee ainoastaan päivät maanantaista lauantaihin. 
[code]
    SELECT 
      *, 
      COUNT(DISTINCT(SalaryRenderingDate)) AS OverrideAmount, 
      'J' AS OverrideUnitType 
    FROM 
      UserSalaryData 
    WHERE 
      ActivityTypeCode = 164 --Lomarahavapaa-tapahtumatyypin koodi
      AND CompensationType = 'MarkedTime' 
      AND Weekday(StartDateTime) != 6  
    GROUP BY 
      UserId, 
      ProjectCode1,
      SalaryRenderingDate
[/code]
### Poimitaan työpäivät
Poimitaan määräksi summa niistä palkkapäivistä, joille on syntynyt korvattavaa aikaa. Palkkalajiksi muodostuu arvo '1' silloin kun käsiteltävä päivä on samalla kuukaudella kuin käsiteltävän jakson viimeinen päivä. Muulloin palkkalajiksi muodostuu arvo '2'.
[code]
    SELECT
      *,
      (CASE
         WHEN
           (SELECT
              strftime('%m', MAX(salaryrenderingdate))
            FROM
              UserSalaryData) = strftime('%m', salaryrenderingdate) THEN 1
         ELSE 2
       END) AS OverrideSalaryCode,
      COUNT(DISTINCT(SalaryRenderingDate)) As OverrideAmount,
      'J' AS OverrideUnitType
    FROM
      UserSalaryData
    WHERE
      CompensationType IN ('BasicTime', 'AdditionalWork', 'OvertimeDaily50','OvertimeDaily100',
                           'OvertimeWeekly50', 'OvertimeWeekly100')
      AND BasePartTarget IN ('salary','bank','balance','flexiblehours')
      AND EmployeeSalaryType = 'hourly'
    GROUP BY
      OverrideSalaryCode
[/code]
### Poimitaan matkalaskun matkojen tietoja
Poiminnassa oleva `char(10)` on rivinvaihtomerkki `LF`.
[code]
    SELECT
      ued.*, 
      utetd.StartDateTime AS OverrideStartDatetime, 
      utetd.EndDateTime AS OverrideEndDatetime, 
      utetd.StartLocation || ' - ' || utetd.EndLocation || char(10) || utetd.ReasonForTrip AS OverrideComment 
    FROM
      UserEventData ued 
    JOIN UserTravelExpenseTripData utetd ON ued.ActivityId = utetd.ActivityId
    ORDER BY
      ued.StartDateTime,
      utetd.TripNumber
[/code]
