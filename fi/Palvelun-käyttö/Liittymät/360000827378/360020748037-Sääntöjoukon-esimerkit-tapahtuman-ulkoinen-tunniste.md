---
id: 360020748037
title: Sääntöjoukon esimerkit - tapahtuman ulkoinen tunniste
url: https://support.nepton.com/hc/fi/articles/360020748037-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-tapahtuman-ulkoinen-tunniste
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
updated_at: '2025-03-28T12:27:14Z'
edited_at: '2025-03-28T12:26:44Z'
---

# Sääntöjoukon esimerkit - tapahtuman ulkoinen tunniste

Artikkeliin on koottu tyypillisiä tapahtuman ulkoiseen tunnisteeseen liittyviä poiminnan esimerkkejä
Löydät tietokantataulujen sarakekuvaukset [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>)
Tyypilliset poissaolojen poiminnan esimerkit ovat [tässä](<https://support.nepton.com/hc/fi/articles/360013979998>) artikkelissa, työajan poiminta [tässä](<https://support.nepton.com/hc/fi/articles/360008045337>) artikkelissa ja henkilötietojen poiminnan esimerkit [tässä](<https://support.nepton.com/hc/fi/articles/360015612638>) artikkelissa.
Esimerkeissä oleva kenttä CustomData1 on käytettävissä CGI-, Mepco- ja Pegasos-palkkaliittymissä sekä SD Worx - ja Sympa-poissaololiittymissä.  
Lisäksi kenttä on käytettävissä Visma L7/LTR -kokonaisratkaisussa.
### Poimitaan säännöllinen työaika ja tapahtuman ulkoinen tunniste.
Ulkoinen tunniste valitaan CustomData1 -tietona.
[code] 
    SELECT  
      usd.*,  
      SUM(usd.Amount) AS OverrideAmount,  
      uexid.ExternalIdentifier AS CustomData1  
    FROM UserSalaryData usd  
    LEFT JOIN UserEventExternalIdentifierData uexid ON  
      uexid.ActivityId = usd.ActivityId  
      AND uexid.IdentifierType = 'External'  
    WHERE  
      usd.CompensationType = 'BasicTime'  
      AND usd.BasePartTarget IN ('salary','bank','balance','flexiblehours')  
      AND (usd.OvertimeTarget IS NULL OR usd.OvertimeTarget = 'uncompensated')  
      AND usd.ActivityTypeCode = 1   
    GROUP BY  
      usd.SalaryRenderingDate,  
      usd.ActivityId
[/code]
### Poimitaan säännöllinen työaika vain tapahtumista, joilla on ulkoinen tunniste.
Ulkoinen tunniste valitaan CustomData1 -tietona.
[code] 
    SELECT  
      usd.*, SUM(usd.Amount) AS OverrideAmount,  
      uexid.ExternalIdentifier AS CustomData1  
      
    FROM UserSalaryData usd  
    JOIN UserEventExternalIdentifierData uexid ON  
      uexid.ActivityId = usd.ActivityId  
    WHERE  
      usd.CompensationType = 'BasicTime'  
      AND usd.BasePartTarget IN ('salary','bank','balance','flexiblehours')  
      AND (usd.OvertimeTarget IS NULL OR usd.OvertimeTarget = 'uncompensated')  
      AND usd.ActivityTypeCode = 1  
      AND e.IdentifierType = 'External'  
    GROUP BY  
      usd.SalaryRenderingDate,  
      usd.ActivityId
[/code]
### Poimitaan säännöllinen työaika vain tapahtumista, joilla ei ole ulkoista tunnistetta.
[code] 
    SELECT  
      usd.*,  
      SUM(usd.Amount) AS OverrideAmount  
    FROM  
      UserSalaryData usd  
    LEFT JOIN UserEventExternalIdentifierData uexid ON  
      uexid.ActivityId = usd.ActivityId  
      AND uexid.IdentifierType = 'External'  
    WHERE  
      usd.CompensationType = 'BasicTime'  
      AND usd.BasePartTarget IN ('salary','bank','balance','flexiblehours')  
      AND (usd.OvertimeTarget IS NULL OR usd.OvertimeTarget = 'uncompensated')  
      AND usd.ActivityTypeCode = '1'  
      AND uexid.ActivityId IS NULL  
    GROUP BY  
      usd.SalaryRenderingDate
[/code]
