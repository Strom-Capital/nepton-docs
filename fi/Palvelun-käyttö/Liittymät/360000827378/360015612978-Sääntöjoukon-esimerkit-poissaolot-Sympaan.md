---
id: 360015612978
title: Sääntöjoukon esimerkit - poissaolot Sympaan
url: https://support.nepton.com/hc/fi/articles/360015612978-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-poissaolot-Sympaan
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels: []
promoted: false
updated_at: '2025-08-12T07:27:14Z'
edited_at: '2025-08-12T07:27:14Z'
---

# Sääntöjoukon esimerkit - poissaolot Sympaan

Tässä artikkelissa kuvataan parhaat käytännöt poissaolojen viemiseksi Sympaan. 
Löydät tietokantataulujen sarakekuvaukset [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>)
Tyypilliset työajan poiminnan esimerkit ovat [tässä ](<https://support.nepton.com/hc/fi/articles/360008045337>)artikkelissa ja projektirakenteen, projektien huomioiden poiminta [tässä](<https://support.nepton.com/hc/fi/articles/360013894637>) artikkelissa ja poissaolojen poiminnan yleisohje [tässä](<https://support.nepton.com/hc/fi/articles/360013979998>) artikkelissa.
Esimerkissä siirretään
  * Poissaolotapahtuman kokopäivän poissaolotunnit sekä osapäivän poissaolotunnit.
  * Sairauslomatapahtuman kokopäivän poissaolotunnit sekä osapäivän poissaolotunnit.
  * Poissaoloina käsiteltävien tapahtumatyyppien kokopäivän poissaolotunnit sekä osapäivän poissaolotunnit


Aineistoon muodostuu yksi rivi per tapahtuma. Rivi sisältää yksilöllisen tunnisteen (activityId), jonka perusteella Sympa päivittää riviin tulevat muutokset automaattisesti. Myös hyväksymättömät poissaolot ja tieto poistetuista tapahtumista siirretään. Muutokset poissaolon päivämääriin, poissaololajiin, hyväksyntätietoon sekä tieto tapahtuman poistamisesta siirtyy Sympaan sääntöjoukon ajastuksen mukaisesti. Sääntöjoukko suositellaan ajastettavan ajettavaksi kerran yössä, jolloin aineisto muodostuu SFTP palvelimelle. Aineisto poimitaan 3kk taaksepäin ja 3kk eteenpäin. Poimintasääntö rajaa siirrettäviksi tapahtumiksi ne, jotka alkavat enintään 2kk sitten.
Esimerkit ovat tehty siirrettäväksi SD Works (aiemmin nimeltään Personec W) poissaolot -muodossa. Aineistoon tulee muodostaa poissaolon syy (salary code) vastaamaan Sympaan määriteltyjä koodeja. Siirtoaineiston kuvauksen löydät [täältä](<https://support.nepton.com/hc/fi/articles/360003473418>).
Sympan määrittely tehdään tämän kuvauksen mukaisesti.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360013063197)
Poimintasäännöt tehdään tämän kuvauksen mukaisesti
### 
### Poimitaan poissaolo - tapahtumatyypin poissaolot
Poimitaan poissaolo-tapahtumatyypin poissaolot. Tulokseen muodostuu kokopäiväiset poissaolotunnit sekä osapäiväiset poissaolotunnit. Rivillä on ID, joka päivittää tiedon Sympaan mikäli se on jo siirretty aiemmilla ajoilla.
[code] 
    SELECT 
      *, 
      SUM(
        CASE  
          WHEN SalaryRenderingDate NOT IN  
            (SELECT 
               SalaryRenderingDate 
             FROM 
               UserSalaryData 
             WHERE 
               ActivityTypeCategoryId = 1 --Work event types
               AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork', 'OvertimeDaily50',  
                                        'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50',  
                                        'OvertimeSunday100', 'PublicHoliday', 'YearLeave')) THEN Amount  
          ELSE 0  
        END) / 3600 AS OverrideAmount, --this gives the amount of absence hours when considering full day absences
      REPLACE(ROUND(SUM(
        CASE  
          WHEN SalaryRenderingDate IN  
            (SELECT 
               SalaryRenderingDate 
             FROM 
               UserSalaryData 
             WHERE 
               ActivityTypeCategoryId = 1 --Work event types
               AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork', 'OvertimeDaily50',  
                                        'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50',  
                                        'OvertimeSunday100', 'PublicHoliday', 'YearLeave')) THEN Amount  
          ELSE 0  
        END) / 3600, 2), '.',',') AS CustomData3, --CustomData3 gives the amount of absence hours when considering part day absences
      MIN(ActivityId) As CustomData1,   -- this is added to create a key that is used to match updates on Sympa side
      IsApproved As CustomData2, 
      'Uusi' AS OverrideUserCostGroup, 
      MIN(SalaryRenderingDate) As OverrideStartDatetime, 
      MAX(SalaryRenderingDate) AS OverrideEndDatetime, 
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
        ELSE 'NOT DEFINED'
      END AS OverrideSalaryCode
    FROM  
      UserSalaryData 
    WHERE  
      AbsenceTypeId IS NOT NULL  
      AND CompensationType IN ('BasicTime', 'UnpaidBasicTime', 'ReducedRateTime')  
    GROUP BY  
      ActivityId
    
[/code]
### 
### Poimitaan sairauspoissaolot
Poimitaan sairauspoissaolot. Tulokseen muodostuu kokopäiväiset poissaolotunnit sekä osapäiväiset poissaolotunnit. Rivillä on ID, joka päivittää tiedon Sympaan mikäli se on jo siirretty aiemmilla ajoilla.
[code] 
    SELECT 
      *,
      SUM(  
        CASE  
          WHEN SalaryRenderingDate NOT IN  
            (SELECT
               SalaryRenderingDate 
             FROM 
               UserSalaryData 
             WHERE 
               ActivityTypeCategoryId = 1 --Work event types
               AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork', 'OvertimeDaily50',  
                                        'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50',  
                                        'OvertimeSunday100', 'PublicHoliday', 'YearLeave')) THEN Amount  
        ELSE 0  
      END) / 3600 AS OverrideAmount, --this gives the amount of absence hours when considering full day absences
      REPLACE(ROUND(SUM(
        CASE  
          WHEN SalaryRenderingDate IN
            (SELECT 
               SalaryRenderingDate 
             FROM 
               UserSalaryData 
             WHERE 
               ActivityTypeCategoryId 1 --Work event types
               AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork', 'OvertimeDaily50',  
                                        'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50',
                                        'OvertimeSunday100', 'PublicHoliday', 'YearLeave')) THEN Amount  
          ELSE 0  
        END) / 3600, 2), '.',',') AS CustomData3, --CustomData3 gives the amount of absence hours when considering part day absences  
      MIN(ActivityId) As CustomData1, -- this is added to create a key that is used to match updates on Sympa side
      IsApproved As CustomData2, 
      'Uusi' AS OverrideUserCostGroup, 
      MIN(SalaryRenderingDate) As OverrideStartDatetime, 
      MAX(SalaryRenderingDate) AS OverrideEndDatetime, 
      CASE  
        WHEN SickLeaveTypeId = 1 AND CompensationType = 'BasicTime' AND SickLeaveMedicalCertificateId = 2 THEN 'PALKALLINEN_ITSESAIRAS_TODISTUKSELLA' -- itse sairas todistuksella
        WHEN SickLeaveTypeId = 1 AND CompensationType = 'BasicTime' AND SickLeaveMedicalCertificateId <> 2 THEN 'PALKALLINEN_ITSESAIRAS' -- itse sairas
        WHEN SickLeaveTypeId = 2 AND CompensationType = 'BasicTime' AND SickLeaveMedicalCertificateId = 2 THEN 'PALKALLINEN_LAPSISAIRAS_TODISTUKSELLA' -- lapsi sairas todistuksella
        WHEN SickLeaveTypeId = 2 AND CompensationType = 'BasicTime' AND SickLeaveMedicalCertificateId <> 2 THEN 'PALKALLINEN_LAPSISAIRAS_ILMANTODISTUSTA' -- lapsi sairas
        WHEN SickLeaveTypeId = 3 AND CompensationType = 'BasicTime' THEN 'PALKALLINEN_TYOTAPATURMA_TOISSA' -- työtapaturma työpaikalla
        WHEN SickLeaveTypeId = 4 AND CompensationType = 'BasicTime' THEN 'PALKALLINEN_TYOTAPATURMA_TYOMATKALLA' -- työtapaturma työmatkalla
        WHEN SickLeaveTypeId = 5 AND CompensationType = 'BasicTime' THEN 'PALKALLINEN_TYOTAPATURMA_VAPAALLA' --työtapaturma vapaa-ajalla
        WHEN SickLeaveTypeId = 1 AND CompensationType = 'UnpaidBasicTime' AND SickLeaveMedicalCertificateId = 2 THEN 'PALKATON_ITSESAIRAS_TODISTUKSELLA' -- palkaton itse sairas todistuksella
        WHEN SickLeaveTypeId = 1 AND CompensationType = 'UnpaidBasicTime' AND SickLeaveMedicalCertificateId <> 2 THEN 'PALKATON_ITSESAIRAS' -- palkaton itse sairas
        WHEN SickLeaveTypeId = 2 AND CompensationType = 'UnpaidBasicTime' AND SickLeaveMedicalCertificateId = 2 THEN 'PALKATON_LAPSISAIRAS_TODISTUKSELLA' -- palkaton lapsi sairas todistuksella
        WHEN SickLeaveTypeId = 2 AND CompensationType = 'UnpaidBasicTime' AND SickLeaveMedicalCertificateId <> 2 THEN 'PALKATON_LAPSISAIRAS_ILMANTODISTUSTA' -- palkaton lapsi sairas 
        WHEN SickLeaveTypeId = 3 AND CompensationType = 'UnpaidBasicTime' THEN 'PALKATON_TYOTAPATURMA_TOISSA' -- palkaton työtapaturma työpaikalla
        WHEN SickLeaveTypeId = 4 AND CompensationType = 'UnpaidBasicTime' THEN 'PALKATON_TYOTAPATURMA_TYOMATKALLA' -- palkaton työtapaturma työmatkalla
        WHEN SickLeaveTypeId = 5 AND CompensationType = 'UnpaidBasicTime' THEN 'PALKATON_TYOTAPATURMA_VAPAALLA' --palkaton työtapaturma vapaa-ajalla
        ELSE 'NOT DEFINED'  
      END AS OverrideSalaryCode 
    FROM 
      UserSalaryData 
    WHERE 
      ActivityTypeCode = 2 --Sairausloma
      AND CompensationType IN ('BasicTime', 'UnpaidBasicTime', 'RedudedRateTime') -- this row exists to prevent lunch or other events from getting included
    GROUP BY 
      ActivityId
[/code]
### Poimitaan muut poissaolona käsiteltävät tapahtumatyypit
Poimitaan poissaoloina käsiteltävät tapahtumatyypit. Tulokseen muodostuu kokopäiväiset poissaolotunnit sekä osapäiväiset poissaolotunnit. Rivillä on ID, joka päivittää tiedon Sympaan mikäli se on jo siirretty aiemmilla ajoilla.
[code] 
    SELECT 
      *, 
      SUM(
        CASE  
          WHEN SalaryRenderingDate NOT IN  
            (SELECT 
               SalaryRenderingDate 
             FROM 
               UserSalaryData 
             WHERE 
               ActivityTypeCategoryId = 1 --Work event types
              AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork', 'OvertimeDaily50',  
                                       'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50',
                                       'OvertimeSunday100', 'PublicHoliday', 'YearLeave')) THEN Amount  
          ELSE 0  
        END) / 3600 AS OverrideAmount, --this gives the amount of absence hours when considering full day absences
      REPLACE(ROUND(SUM(
        CASE  
          WHEN SalaryRenderingDate IN  
            (SELECT   
               SalaryRenderingDate 
             FROM 
               UserSalaryData 
             WHERE 
               ActivityTypeCategoryId = 1 --Work event type
               AND CompensationType IN ('BasicTime', 'ReducedRateTime', 'UnpaidBasicTime', 'AdditionalWork', 'OvertimeDaily50',  
                                        'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50',
                                        'OvertimeSunday100', 'PublicHoliday', 'YearLeave')) THEN Amount  
          ELSE 0  
        END) / 3600, 2), '.',',') AS CustomData3, --CustomData3 gives the amount of absence hours when considering part day absences
      MIN(ActivityId) As CustomData1,   -- this is added to create a key that is used to match updates on Sympa side
      IsApproved As CustomData2, 
      'Uusi' AS OverrideUserCostGroup, 
      MIN(SalaryRenderingDate) As OverrideStartDatetime, 
      MAX(SalaryRenderingDate) AS OverrideEndDatetime, 
      CASE 
        WHEN ActivityTypeCode = '16'  THEN 'SALDOVAPAA' -- Saldovapaa
        WHEN ActivityTypeCode = '278' THEN 'YLITYOVAPAA' -- Ylityövapaa
        WHEN ActivityTypeCode = '25' THEN 'PALKALLINEN_KOULUTUS' -- Koulutus
        WHEN ActivityTypeCode = '23' THEN 'LOMAUTUS' -- Lomautus
        WHEN ActivityTypeCode = '102' THEN 'PANKKIVAPAA' -- Pankkivapaa
        ELSE 'NOT DEFINED'
      END AS OverrideSalaryCode
    FROM  
      UserSalaryData 
    WHERE  
      ActivityTypeCode IN ('16','278','25','23','102')
      AND CompensationType NOT IN ('MarkedTime')
    GROUP BY  
      ActivityId
    
[/code]
### Poimitaan poistetut poissaolot
Poimitaan poistetut poissaolot. Rivillä on ID, joka päivittää tiedon Sympaan mikäli se on jo siirretty aiemmilla ajoilla.
[code] 
    SELECT  
      *,
      0 AS OverrideAmount,
      MIN(ActivityId) As CustomData1,   -- this is to match previously added event on Sympa side
      0 AS CustomData3,
      IsApproved As CustomData2, 
      'Poisto' AS OverrideUserCostGroup,
      CASE 
        WHEN ActivityTypeCode = '16'  THEN 'SALDOVAPAA' -- Saldovapaa
        WHEN ActivityTypeCode = '278' THEN 'YLITYOVAPAA' -- Ylityövapaa
        WHEN ActivityTypeCode = '25' THEN 'PALKALLINEN_KOULUTUS' -- Koulutus
        WHEN ActivityTypeCode = '23' THEN 'LOMAUTUS' -- Lomautus
        WHEN ActivityTypeCode = '102' THEN 'PANKKIVAPAA' -- Pankkivapaa
        WHEN AbsenceTypeId = 25 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_AMMATTIYHDISTYSTOIMINTA' -- Palkallinen ammattiyhdistystoiminta  
        WHEN AbsenceTypeId = 10 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_ASEVELVOLLISUUS' -- Palkallinen ase- tai siviilipalvelusaika  
        WHEN AbsenceTypeId = 1 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_ERITYISÄITIYSVAPAA' -- Palkallinen erityisäitiysvapaa  
        WHEN AbsenceTypeId = 5 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_HOITOVAPAA' -- Palkallinen hoitovapaa  
        WHEN AbsenceTypeId = 3 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_ISYYSVAPAA' -- Palkallinen isyysvapaa  
        WHEN AbsenceTypeId = 11 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_KERTAUSHARJOITUKSET' -- Palkallinen kertausharjoitukset  
        WHEN AbsenceTypeId = 27 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_KUNTOUTUS' -- Palkallinen kuntoutus  
        WHEN AbsenceTypeId = 18 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_KUTSUNTATILAISUUS' -- Palkallinen kutsuntatilaisuus  
        WHEN AbsenceTypeId = 13 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_MUUPOISSAOLO' -- Muu poissaolo palkallinen  
        WHEN AbsenceTypeId = 26 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_MUUTTOVAPAA' -- Palkallinen muuttovapaa  
        WHEN AbsenceTypeId = 452 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_OMAISHOITOVAPAA' -- Palkallinen omaishoitovapaa  
        WHEN AbsenceTypeId = 17 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_50TAI60MERKKIPAIVA' -- Omat 50- tai 60-vuotisjuhlat palkallinen  
        WHEN AbsenceTypeId = 16 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_PARISUHTEENREKISTEROINTI' -- Palkallinen Omat vihkiäiset / Parisuhteen rekisteröinti  
        WHEN AbsenceTypeId = 8 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_OPINTOVAPAA' -- Palkallinen Opintovapaa  
        WHEN AbsenceTypeId = 22 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_OSAAIKAELAKE' -- Palkallinen osa-aikaeläke  
        WHEN AbsenceTypeId = 31 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_OSAAIKAISUUS' -- Palkallinen osa-aikaisuus  
        WHEN AbsenceTypeId = 14 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_PERHEENJASENENKUOLEMA' -- Palkallinen perheenjäsenen kuolema  
        WHEN AbsenceTypeId = 15 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_LAHIOMAISENHAUTAJAISET' -- Palkallinen perheenjäsenen tai lähiomaisen hautajaiset  
        WHEN AbsenceTypeId = 20 AND AbsenceCompensationTypeId = 1 THEN 'PERHEENJASENEN_SAIRASTUMINEN_PALKALLINEN' -- Palkallinen perheenjäsenen äkillinen sairastuminen  
        WHEN AbsenceTypeId = 7 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_PAKOTTAVAPERHESYY' -- Poissaolo pakottavien perhesyiden takia  
        WHEN AbsenceTypeId = 450 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_RASKAUSVAPAA' -- Palkallinen raskausvapaa  
        WHEN AbsenceTypeId = 6 AND AbsenceCompensationTypeId = 1 THEN 'TILAPAINEN_HOITOVAPAA_PALKALLINEN' -- Palkallinen tilapäinen hoitovapaa  
        WHEN AbsenceTypeId = 19 AND AbsenceCompensationTypeId = 1 THEN 'TOIMIVAPAA_PALKALLINEN' -- Palkallinen toimivapaa  
        WHEN AbsenceTypeId = 12 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_TYONTEKIJANOMAPYYNTO' -- Palkaton työntekijän oma pyyntö  
        WHEN AbsenceTypeId = 451 AND AbsenceCompensationTypeId = 1 THEN 'VANHEMPAINVAPAA_PALKALLINEN' -- Palkallinen vanhempainvapaa  
        WHEN AbsenceTypeId = 4 AND AbsenceCompensationTypeId = 1 THEN 'VANHEMPAINVAPAA_PALKALLINEN (ENNEN UUDISTUSTA)' -- Palkallinen vanhempainvapaa (ennen uudistusta)  
        WHEN AbsenceTypeId = 23 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_VIRKAVAPAA' -- Palkallinen virkavapaa  
        WHEN AbsenceTypeId = 9 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_VUOROTTELUVAPAA' -- Palkallinen vuorotteluvapaa  
        WHEN AbsenceTypeId = 2 AND AbsenceCompensationTypeId = 1 THEN 'PALKALLINEN_AITIYSVAPAA' -- Palkallinen äitiysvapaa  
        WHEN AbsenceTypeId = 25 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_AMMATTIYHDISTYSTOIMINTA' -- Palkaton ammattiyhdistystoiminta  
        WHEN AbsenceTypeId = 10 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_ASEVELVOLLISUUS' -- Palkaton ase- tai siviilipalvelusaika  
        WHEN AbsenceTypeId = 1 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_ERITYISÄITIYSVAPAA' -- Palkaton erityisäitiysvapaa  
        WHEN AbsenceTypeId = 5 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_HOITOVAPAA' -- Palkaton hoitovapaa  
        WHEN AbsenceTypeId = 3 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_ISYYSVAPAA' -- Palkaton isyysvapaa  
        WHEN AbsenceTypeId = 11 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_KERTAUSHARJOITUKSET' -- Palkaton kertausharjoitukset  
        WHEN AbsenceTypeId = 27 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_KUNTOUTUS' -- Palkaton kuntoutus  
        WHEN AbsenceTypeId = 18 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_KUTSUNTATILAISUUS' -- Palkaton kutsuntatilaisuus  
        WHEN AbsenceTypeId = 13 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_MUUPOISSAOLO' -- Palkaton muu poissaolo  
        WHEN AbsenceTypeId = 26 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_MUUTTOVAPAA' -- Palkaton muuttovapaa  
        WHEN AbsenceTypeId = 452 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_OMAISHOITOVAPAA' -- Palkaton omaishoitovapaa  
        WHEN AbsenceTypeId = 17 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_50TAI60MERKKIPAIVA' -- Palkaton omat 50- tai 60-vuotisjuhlat  
        WHEN AbsenceTypeId = 16 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_PARISUHTEENREKISTEROINTI' -- Palkaton omat vihkiäiset / parisuhteen rekisteröinti  
        WHEN AbsenceTypeId = 8 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_OPINTOVAPAA' -- Palkaton opintovapaa  
        WHEN AbsenceTypeId = 22 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_OSAAIKAELAKE' -- Palkaton osa-aikaeläke  
        WHEN AbsenceTypeId = 31 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_OSAAIKAISUUS' -- Palkaton osa-aikaisuus  
        WHEN AbsenceTypeId = 14 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_PERHEENJASENENKUOLEMA' -- Palkaton perheenjäsenen kuolema  
        WHEN AbsenceTypeId = 15 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_LAHIOMAISENHAUTAJAISET' -- Palkaton perheenjäsenen tai lähiomaisen hautajaiset  
        WHEN AbsenceTypeId = 20 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_PERHEENJASENEN_SAIRASTUMINEN' -- Palkaton perheenjäsenen äkillinen sairastuminen  
        WHEN AbsenceTypeId = 7 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_PAKOTTAVAPERHESYY' -- Palkaton poissaolo pakottavien perhesyiden takia  
        WHEN AbsenceTypeId = 450 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_RASKAUSVAPAA' -- Palkaton raskausvapaa  
        WHEN AbsenceTypeId = 6 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_HOITOVAPAA_PALKALLINEN' -- Palkaton tilapäinen hoitovapaa  
        WHEN AbsenceTypeId = 19 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_PALKALLINEN' -- Palkaton toimivapaa  
        WHEN AbsenceTypeId = 12 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_TYONTEKIJANOMAPYYNTO' -- Palkaton työntekijän oma pyyntö  
        WHEN AbsenceTypeId = 451 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_VANHEMPAINVAPAA' -- Palkaton vanhempainvapaa  
        WHEN AbsenceTypeId = 4 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_VANHEMPAINVAPAA(ENNEN UUDISTUSTA)' -- Palkaton vanhempainvapaa (ennen uudistusta)  
        WHEN AbsenceTypeId = 23 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_VIRKAVAPAA' -- Palkaton virkavapaa  
        WHEN AbsenceTypeId = 9 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_VUOROTTELUVAPAA' -- Palkaton vuorotteluvapaa  
        WHEN AbsenceTypeId = 2 AND AbsenceCompensationTypeId = 2 THEN 'PALKATON_AITIYSVAPAA' -- Palkaton äitiysvapaa
        WHEN SickLeaveTypeId = 1   AND SickLeaveCompensationTypeId = 1   AND SickLeaveMedicalCertificateId = 2 THEN 'PALKALLINEN_ITSESAIRAS_TODISTUKSELLA' -- itse sairas todistuksella
        WHEN SickLeaveTypeId = 1   AND SickLeaveCompensationTypeId = 1  AND SickLeaveMedicalCertificateId <> 2 THEN 'PALKALLINEN_ITSESAIRAS' -- itse sairas
        WHEN SickLeaveTypeId = 2   AND SickLeaveCompensationTypeId = 1   AND SickLeaveMedicalCertificateId = 2 THEN 'PALKALLINEN_LAPSISAIRAS_TODISTUKSELLA' -- lapsi sairas todistuksella
        WHEN SickLeaveTypeId = 2   AND SickLeaveCompensationTypeId = 1   AND SickLeaveMedicalCertificateId <> 2 THEN 'PALKALLINEN_LAPSISAIRAS_ILMANTODISTUSTA' -- lapsi sairas
        WHEN SickLeaveTypeId = 3   AND SickLeaveCompensationTypeId = 1 THEN 'PALKALLINEN_TYOTAPATURMA_TOISSA' -- työtapaturma työpaikalla
        WHEN SickLeaveTypeId = 4   AND SickLeaveCompensationTypeId = 1  THEN 'PALKALLINEN_TYOTAPATURMA_TYOMATKALLA' -- työtapaturma työmatkalla
        WHEN SickLeaveTypeId = 5   AND SickLeaveCompensationTypeId = 1  THEN 'PALKALLINEN_TYOTAPATURMA_VAPAALLA' --työtapaturma vapaa-ajalla
        WHEN SickLeaveTypeId = 1   AND SickLeaveCompensationTypeId = 2   AND SickLeaveMedicalCertificateId = 2 THEN 'PALKATON_ITSESAIRAS_TODISTUKSELLA' -- palkaton itse sairas todistuksella
        WHEN SickLeaveTypeId = 1   AND SickLeaveCompensationTypeId = 2  AND SickLeaveMedicalCertificateId <> 2 THEN 'PALKATON_ITSESAIRAS' -- palkaton itse sairas
        WHEN SickLeaveTypeId = 2   AND SickLeaveCompensationTypeId = 2   AND SickLeaveMedicalCertificateId = 2 THEN 'PALKATON_LAPSISAIRAS_TODISTUKSELLA' -- palkaton lapsi sairas todistuksella
        WHEN SickLeaveTypeId = 2   AND SickLeaveCompensationTypeId = 2  AND SickLeaveMedicalCertificateId <> 2 THEN 'PALKATON_LAPSISAIRAS_ILMANTODISTUSTA' -- palkaton lapsi sairas 
        WHEN SickLeaveTypeId = 3   AND SickLeaveCompensationTypeId = 2 THEN 'PALKATON_TYOTAPATURMA_TOISSA' -- palkaton työtapaturma työpaikalla
        WHEN SickLeaveTypeId = 4   AND SickLeaveCompensationTypeId = 2 THEN 'PALKATON_TYOTAPATURMA_TYOMATKALLA' -- palkaton työtapaturma työmatkalla
        WHEN SickLeaveTypeId = 5   AND SickLeaveCompensationTypeId = 2 THEN 'PALKATON_TYOTAPATURMA_VAPAALLA' --palkaton työtapaturma vapaa-ajalla
        ELSE 'NOT DEFINED'
      END AS OverrideSalaryCode
    FROM  
      UserEventHistoryData 
    WHERE 
       ModifiedDateTime BETWEEN :exportPeriodStart AND :exportPeriodEnd
       AND IsActive = 'N'
       AND OriginalActivityId IS NULL
       AND -- pick only those deleted events that are treated as absence type 
         (AbsenceTypeId IS NOT NULL 
          OR ActivityTypeCode IN ('4','2','16', '278', '25', '23', '102'))
    
[/code]
