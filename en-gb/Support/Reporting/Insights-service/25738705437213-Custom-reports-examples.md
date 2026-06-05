---
id: 25738705437213
title: Custom reports examples
url: https://support.nepton.com/hc/en-gb/articles/25738705437213-Custom-reports-examples
locale: en-gb
category: Support
category_id: 360000446658
section: Insights service
section_id: 25746849648925
section_path:
- Reporting
- Insights service
labels: []
promoted: false
updated_at: '2025-04-30T08:06:37Z'
edited_at: '2025-04-11T11:39:28Z'
---

# Custom reports examples

**Sorry!**
This article has not been translated yet.
[Muokattavat raportit](<https://support.nepton.com/hc/fi/articles/19801354657309>) tarjoavat tehokkaan ja joustavan tavan luoda uusia raportteja organisaation tietojen pohjalta. Raportit perustuvat sääntöjoukkoihin, joiden avulla voidaan määrittää tarkasti, mitä tietoja raporteille poimitaan. Näin voit räätälöidä raportoinnin organisaatiosi tarpeiden mukaisesti ja varmistaa, että saatte käyttöönne kaikki relevantit tiedot. Tämä artikkeli sisältää esimerkkejä muokattavista raporteista.
## Lauantailomapäivät
Laskee käytettyjen vuosilomapäivien summan ja lauantailomapäivien summan.
\- Vuosilomapäivät yhteensä
\- Lauantaipäivät yhteensä
[code] 
    SELECT  
      usd.UserId AS 'Käyttäjän ID',  
      ud.FirstName AS 'Etunimi',  
      ud.LastName AS 'Sukunimi',  
      SUM(  
        CASE  
          WHEN usd.ActivityTypeCode = 3 THEN  
            CASE  
              WHEN DATE(usd.StartDateTime) = DATE(usd.EndDateTime) THEN 1  
              ELSE ROUND( julianday(usd.EndDateTime) - julianday(usd.StartDateTime))  
            END  
          ELSE 0  
        END ) AS 'Vuosilomapäivät yhteensä',  
      SUM(  
        CASE  
          WHEN strftime('%w', usd.StartDateTime) = '6' THEN ROUND(julianday(usd.EndDateTime) - julianday(usd.StartDateTime))  
          ELSE 0  
        END) AS 'Lauantaipäivät yhteensä'  
    FROM  
      UserSalaryData usd  
    JOIN UserData ud ON usd.UserId = ud.UserId  
    WHERE  
      strftime('%w', usd.StartDateTime) != '0' -- Jättää sunnuntait huomioimatta  
    GROUP BY  
      usd.UserId,  
      ud.FirstName,  
      ud.LastName
[/code]
![Näyttökuva 2025-03-10 kello 16.25.10.png](https://support.nepton.com/hc/article_attachments/25793758778653)
## Työajan jakautuminen henkilöryhmittäin
Raportti näyttää työajan jakautumisen henkilöryhmittäin.
\- Perustyötunnit  
\- Ylityötunnit  
\- Poissaolotunnit
[code] 
    SELECT  
      ud.UserGroupCode AS 'Henkilöryhmä',  
      CONCAT(  
        FLOOR(SUM(  
          CASE  
            WHEN usd.CompensationType = 'BasicTime' THEN usd.Amount  
            ELSE 0  
          END) / 3600),  
        'h ',  
        FLOOR((SUM(  
          CASE  
            WHEN usd.CompensationType = 'BasicTime' THEN usd.Amount  
            ELSE 0  
          END) % 3600) / 60),  
        'm') AS 'Perustyötunnit',  
      CONCAT(  
        FLOOR(SUM(  
          CASE  
            WHEN usd.CompensationType IN ('OvertimeDaily50', 'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100') THEN usd.Amount  
            ELSE 0  
          END) / 3600),  
        'h ',  
        FLOOR((SUM(  
          CASE  
            WHEN usd.CompensationType IN ('OvertimeDaily50', 'OvertimeDaily100', 'OvertimeWeekly50', 'OvertimeWeekly100') THEN usd.Amount  
            ELSE 0  
          END) % 3600) / 60),  
        'm') AS 'Ylityötunnit',  
      CONCAT(  
        FLOOR(SUM(  
          CASE  
            WHEN usd.CompensationType IN ('UnpaidBasicTime', 'ReducedRateTime') THEN usd.Amount  
            ELSE 0  
          END) / 3600),  
        'h ',  
        FLOOR((SUM(  
          CASE  
            WHEN usd.CompensationType IN ('UnpaidBasicTime', 'ReducedRateTime') THEN usd.Amount  
            ELSE 0  
          END) % 3600) / 60),  
        'm') AS 'Poissaolotunnit'  
    FROM  
      UserSalaryData usd  
    JOIN UserData ud ON usd.UserId = ud.UserId  
    GROUP BY  
      ud.UserGroupCode
[/code]
![Näyttökuva 2025-03-10 kello 14.57.37.png](https://support.nepton.com/hc/article_attachments/25793772978077)
## Etätöiden osuus
Raportti näyttää etätöiden osuuden muihin töihin verrattuna.
\- Kokonaistyöaika; (Työaika + poissaolot)  
\- Tehty työ; (Tehdyt työt, muut kuin etätyö)  
\- Etätyö; (Tapahtumatyypit 84 & ETA)  
\- Etätyön osuus % (Etätyön osuus kaikesta tehdystä työstä)
[code] 
    WITH RECURSIVE  
    UserGroupRecursive (Id, Depth, Code, Name, ParentId, AssignedGroupId) AS  
      (SELECT  
         Id,  
         Depth,  
         Code,  
         Name,  
         ParentId,  
         Id AS AssignedGroupId  
       FROM  
         UserGroupData  
       UNION ALL  
       SELECT  
         g.Id,  
         g.Depth,  
         g.Code,  
         g.Name,  
         g.ParentId,  
         r.AssignedGroupId  
       FROM  
         UserGroupData g  
       JOIN UserGroupRecursive r ON r.ParentId = g.Id  
       WHERE  
       r.Depth > g.Depth)  
    SELECT  
      ud.UserId AS 'Käyttäjän ID',  
      ud.FirstName AS 'Etunimi',  
      ud.LastName AS 'Sukunimi',  
      CONCAT(  
        FLOOR(SUM(  
          CASE  
            WHEN usd.ActivityTypeCategoryId IN ('1', '2') AND usd.CompensationType NOT IN ( 'MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart' ) THEN usd.Amount  
            ELSE 0  
          END) / 3600),  
        'h ',  
        FLOOR((SUM(  
          CASE  
            WHEN usd.ActivityTypeCategoryId IN ('1', '2') AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') THEN usd.Amount  
            ELSE 0  
          END) % 3600) / 60),  
        'm') AS 'Kokonaistyöaika',  
      CONCAT(  
        FLOOR(SUM(  
          CASE  
            WHEN usd.ActivityTypeCategoryId = 1 AND usd.ActivityTypeCode NOT IN (84, 'ETA') AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') THEN usd.Amount  
            ELSE 0  
          END) / 3600),  
        'h ',  
        FLOOR((SUM(  
          CASE  
            WHEN usd.ActivityTypeCategoryId = 1 AND usd.ActivityTypeCode NOT IN (84, 'ETA') AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') THEN usd.Amount  
            ELSE 0  
          END) % 3600) / 60),  
        'm') AS 'Tehty työ',  
      CONCAT(  
        FLOOR(SUM(  
          CASE  
            WHEN usd.ActivityTypeCode IN (84, 'ETA') AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') AND usd.FromRounding = 'N' THEN usd.Amount  
            ELSE 0  
          END) / 3600),  
        'h ',  
        FLOOR((SUM(  
          CASE  
            WHEN usd.ActivityTypeCode IN (84, 'ETA') AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') AND usd.FromRounding = 'N' THEN usd.Amount  
            ELSE 0  
          END) % 3600) / 60),  
        'm') AS 'Etätyö',  
      CONCAT(  
        ROUND(IFNULL(SUM(  
          CASE  
            WHEN usd.ActivityTypeCode IN (84, 'ETA') AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') AND usd.FromRounding = 'N' THEN usd.Amount  
            ELSE 0  
          END) / 3600, 0) /  
        (IFNULL(SUM(  
           CASE  
             WHEN usd.ActivityTypeCode IN (84, 'ETA') AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') AND usd.FromRounding = 'N' THEN usd.Amount  
             ELSE 0  
           END) / 3600, 0) +  
         IFNULL(SUM(  
           CASE  
             WHEN usd.ActivityTypeCategoryId = 1 AND usd.ActivityTypeCode NOT IN (84, 'ETA') AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') THEN usd.Amount  
             ELSE 0  
           END) / 3600, 0)) * 100, 2),  
         '%') AS 'Etätyön osuus %'  
    FROM  
      UserSalaryData usd  
    JOIN UserData ud ON usd.UserId = ud.UserId  
    GROUP BY  
      ud.UserId,  
      ud.FirstName,  
      ud.LastName
[/code]
![Näyttökuva 2025-03-10 kello 14.55.52.png](https://support.nepton.com/hc/article_attachments/25793758783645)
## Sairauspoissaolojen osuus työajasta
Raportti näyttää sairauspoissaoloprosentin
\- Kokonaistyöaika; (Työaika + poissaolot)  
\- Tehty työ; (Tehdyt työt, muut kuin sairauspoissaolo)  
\- Sairauspoissaolo; (Tapahtumatyypit 2)  
\- Sairauspoissaolon osuus % (Sairauspoissaolon osuus kaikesta tehdystä työstä)
[code] 
    SELECT   
      ud.UserId AS 'Käyttäjän ID',  
      ud.FirstName AS 'Etunimi',   
      ud.LastName AS 'Sukunimi',   
      CONCAT(  
        FLOOR(SUM(  
          CASE  
            WHEN usd.ActivityTypeCategoryId IN ('1', '2') AND usd.CompensationType NOT IN ( 'MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart' ) THEN usd.Amount  
            ELSE 0   
          END) / 3600),  
          'h ',  
          FLOOR((SUM(  
            CASE  
              WHEN usd.ActivityTypeCategoryId IN ('1', '2') AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') THEN usd.Amount  
              ELSE 0  
            END) % 3600) / 60),   
            'm') AS 'Kokonaistyöaika',   
      CONCAT(  
        FLOOR(SUM(  
          CASE  
            WHEN usd.ActivityTypeCategoryId = 1 AND usd.ActivityTypeCode NOT IN (2) AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') THEN usd.Amount  
            ELSE 0  
          END) / 3600),   
          'h ',   
          FLOOR((SUM(  
            CASE  
              WHEN usd.ActivityTypeCategoryId = 1 AND usd.ActivityTypeCode NOT IN (2) AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') THEN usd.Amount  
              ELSE 0  
            END) % 3600) / 60),   
            'm') AS 'Tehty työ',   
      CONCAT(  
        FLOOR(SUM(  
          CASE  
            WHEN usd.ActivityTypeCode = 2 AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') AND usd.FromRounding = 'N' THEN usd.Amount  
            ELSE 0  
          END) / 3600),   
          'h ',   
        FLOOR((SUM(  
          CASE  
            WHEN usd.ActivityTypeCode = 2 AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') AND usd.FromRounding = 'N' THEN usd.Amount  
            ELSE 0  
          END) % 3600) / 60),   
          'm') AS 'Sairauspoissaolo',   
      CONCAT(  
        ROUND(IFNULL(SUM(  
          CASE  
            WHEN usd.ActivityTypeCode = 2 AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') AND usd.FromRounding = 'N' THEN usd.Amount  
            ELSE 0  
          END) / 3600, 0) /  
          (IFNULL(SUM(  
             CASE  
               WHEN usd.ActivityTypeCode = 2 AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') AND usd.FromRounding = 'N' THEN usd.Amount  
               ELSE 0  
             END) / 3600, 0)  
             + IFNULL(SUM(  
               CASE  
                 WHEN usd.ActivityTypeCategoryId = 1 AND usd.ActivityTypeCode NOT IN (2) AND usd.CompensationType NOT IN ('MarkedTime', 'Lunch', 'WorkRise', 'WorkIncrement', 'WorkRisePercentagePart') THEN usd.Amount  
                 ELSE 0  
               END) / 3600, 0)) * 100, 2),   
               '%') AS 'Sairauspoissaoloprosentti'   
    FROM   
      UserSalaryData usd   
    JOIN UserData ud ON usd.UserId = ud.UserId   
    GROUP BY   
      ud.UserId,   
      ud.FirstName,   
      ud.LastName
[/code]
![Näyttökuva 2025-03-10 kello 14.56.08.png](https://support.nepton.com/hc/article_attachments/25793758785693)
