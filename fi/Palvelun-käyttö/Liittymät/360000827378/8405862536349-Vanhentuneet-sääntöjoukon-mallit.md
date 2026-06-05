---
id: 8405862536349
title: Vanhentuneet sääntöjoukon mallit
url: https://support.nepton.com/hc/fi/articles/8405862536349-Vanhentuneet-s%C3%A4%C3%A4nt%C3%B6joukon-mallit
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
updated_at: '2025-12-03T06:48:10Z'
edited_at: '2025-12-03T06:48:10Z'
---

# Vanhentuneet sääntöjoukon mallit

# Varallaolo vähennettynä varallaoloaikana tehdyllä työllä
[code]
    SELECT OnCall.*, OnCall.SumAmount - IFNULL(OnCallWork.SumAmount, 0) AS OverrideAmount,
    substring_part(Oncall.ActivityTypeCode, '/', 2) AS OverrideSalaryCode
    
    FROM (SELECT *, SUM(Amount) SumAmount 
    FROM UserSalaryData
    WHERE CompensationType = 'MarkedTime'AND BasePartTarget IS NULL AND ActivityTypeCode = '33'GROUP BY SalaryRenderingDate) 
    OnCall
    
    LEFT JOIN (SELECT *, SUM(Amount) SumAmount
    
    FROM UserSalaryData
    WHERE ActivityTypeCode IN ('1') -- jatka tähän listaan ne kaikki tapahtumat joiden päällekkäisyys vähennetään varallaolona poimittavasta arvosta
    AND 
    (OverlapsUnderlyingActivityTypeIds LIKE '%,33,%' OR OverlapsUnderlyingActivityTypeIds LIKE '%,VARA%,%')
    AND CompensationType IN ('BasicTime', 'AdditionalWork', 'OvertimeDaily50', 
    'OvertimeDaily100','OvertimeWeekly50', 'OvertimeWeekly100', 'OvertimeSunday50', 
    'OvertimeSunday100')
    GROUPBY SalaryRenderingDate) 
    OnCallWork 
    
    ON (OnCallWork.SalaryRenderingDate = OnCall.SalaryRenderingDate)
    
    GROUPBY OverrideSalaryCode, Oncall.SalaryRenderingDate, Oncall.ProjectCode1, Oncall.ProjectCode2, Oncall.ProjectCode3,
    Oncall.ProjectCode4, Oncall.ProjectCode5, Oncall.ProjectCode6, Oncall.Comment
[/code]
Yllä olevaa mallia suositeltiin aiemmin käytettäväksi varallaoloaikojen laskemiseen palkkaliittymissä. Mallissa vähennetään varallaoloaika-tapahtuman kestosta tietyt tapahtumat, jotka on kirjattu sen päälle.
Tällainen laskenta lisättiin myöhemmin osaksi järjestelmää (tarkemmat tiedot [täällä](<https://support.nepton.com/hc/fi/articles/8040695057821>)).
Mallin mukainen kysely toimii edelleen mutta mikäli haluat käyttää järjestelmän sisäistä laskentaa ja asettaa sen arvot esille kalenterinäkymään on vahvasti suositeltavaa, että palkkaliittymiin välitetään sama arvo sen sijaan että se lasketaan erikseen sääntöjoukossa. UserSalaryData taulu sisältää nyt erilliset rivit varallaoloajalle kts. päivitetty esimerkki [täältä](<https://support.nepton.com/hc/fi/articles/360008045337-S%C3%A4%C3%A4nt%C3%B6joukon-mallit-palkkaliittym%C3%A4#360008045337-toc-13>)
