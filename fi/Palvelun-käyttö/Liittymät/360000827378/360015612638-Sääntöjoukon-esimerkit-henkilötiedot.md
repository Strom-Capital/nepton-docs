---
id: 360015612638
title: Sääntöjoukon esimerkit - henkilötiedot
url: https://support.nepton.com/hc/fi/articles/360015612638-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-henkil%C3%B6tiedot
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
updated_at: '2025-11-28T07:43:33Z'
edited_at: '2025-11-28T07:43:33Z'
---

# Sääntöjoukon esimerkit - henkilötiedot

Artikkeliin on koottu tyypillisiä henkilötietojen poimintaan liittyviä esimerkkejä. 
Löydät tietokantataulujen sarakekuvaukset [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>)
  * [1 Liitetään hakuun henkilötiedot ja poimitaan henkilön nimi osaksi kommenttia](<https://support.nepton.com/hc/fi/articles/360015612638-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-henkil%C3%B6tiedot#h_01J4P7NTDKXFX8JCQPMEZQ2B4T>)
  * [2 Käytetään haussa henkilötietoja](<https://support.nepton.com/hc/fi/articles/360015612638-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-henkil%C3%B6tiedot#h_01J4P7NTDKXSYWF9X1NXT33R75>)
  * [3 Henkilön työsuhteen alkupäivän hakeminen päivämäärämuodossa UserInfoData -taulusta](<https://support.nepton.com/hc/fi/articles/360015612638-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-henkil%C3%B6tiedot#h_01J4P7NTDKEP5ZH2CWX9GD87H8>)
  * [4 Poimitaan henkilöryhmän puurakenne](<https://support.nepton.com/hc/fi/articles/360015612638-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-henkil%C3%B6tiedot#h_01J4P7NTDK1YS27VQ2X7Z3H0H0>)
  * [5 Poimitaan henkilöryhmien ja projektien puurakenne](<https://support.nepton.com/hc/fi/articles/360015612638-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-henkil%C3%B6tiedot#h_01J4P7NTDKFGSYE7QFF1YEFGFS>)
  * [6 Poimitaan henkilöiden ulkoisten palveluiden tunnisteet vientiä varten](<https://support.nepton.com/hc/fi/articles/360015612638-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-henkil%C3%B6tiedot#h_01J4P7NTDKAK38719X4P28CPJ4>)
  * [7 Poimitaan henkilöiden maksuryhmien maksuryhmän tunnisteet ja maksukaudet vientiä varten](<https://support.nepton.com/hc/fi/articles/360015612638-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-henkil%C3%B6tiedot#h_01J4P7NTDKFYGG260PFK6HYV5A>)


Tyypilliset työajan poiminnan esimerkit ovat [tässä ](<https://support.nepton.com/hc/fi/articles/360008045337>)artikkelissa, poissaolojen poiminnan esimerkit ovat [tässä](<https://support.nepton.com/hc/fi/articles/360013979998>) artikkelissa ja projektirakenteen tai projektien huomioiden poiminta [tässä](<https://support.nepton.com/hc/fi/articles/360013894637>) artikkelissa. 
##  1 Liitetään hakuun henkilötiedot ja poimitaan henkilön nimi osaksi kommenttia 
[code] 
    SELECT
      usd.*,
      ud.Firstname || ' ' || ud.Lastname AS OverrideComment
    FROM
      UserSalaryData usd
    LEFT JOIN UserData ud ON usd.UserId = ud.UserId
[/code]
## 2 Käytetään haussa henkilötietoja
Mitä tahansa tietokantatauluissa olevaa henkilön tietoa voidaan käyttää osana poimintasääntöä. Poimintasääntö voi käyttäytyä esimerkiksi niin, että palkka-aineistoon muodostuva palkkalaji muuttuu henkilötiedoissa olevan kentän mukaisesti. 
UserInfo-taulu sisältää kaikki henkilön henkilötiedot voimassaoloaikoineen. Kun hakuehdossa tätä tietokantataulua niin on tärkeää poimia se arvo, joka on voimassa aineiston käsittelypäivänä. Jos voimassaolon tarkistusta ei tehdä, voi poiminnan tuloksena muodostua moninkertainen tulosten määrä. UserInfo-taulun kuvaus löytyy [täältä.](<https://support.nepton.com/hc/fi/articles/360002489257>)
Esimerkissä on kuvattu poiminta siten, että henkilön henkilöryhmän koodi ohjaa säännöllisestä työajasta muodostuvan palkkalajin koodia ja henkilöryhmän koodi muodostuu osaksi aineistoa. 
[code] 
    SELECT
      usd.*,
      SUM(usd.amount) AS OverrideAmount,
      uid.Value AS OverrideCustomData1, -- this adds the person group to a column in the exported material
      CASE -- the case statement defines the salarycode to be used based on persons group code.
        WHEN uid.InfoTypeName = 'RootUserGroupCode_SDSQL' AND uid.Value = 'Toimisto' THEN '100'
        WHEN uid.InfoTypeName = 'RootUserGroupCode_SDSQL' AND uid.Value = 'Tuotanto' THEN '200'
        ELSE 'NOT DEFINED'
      END AS OverrideSalaryCode
    FROM UserSalaryData usd
    LEFT JOIN UserInfoData uid ON
      usd.UserId = uid.UserId
      AND uid.InfoTypeName = 'RootUserGroupCode_SDSQL'
      AND datetime(usd.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo
    WHERE
      usd.CompensationType = 'BasicTime'
    GROUP BY
      usd.CompensationType,
      usd.salaryRenderingDate
[/code]
##  3 Henkilön työsuhteen alkupäivän hakeminen päivämäärämuodossa UserInfoData -taulusta 
Koneellista päivämäärämuotoa tarvitaan, jos halutaan käyttää automaattista palkka-aineistomallin mukaista päivämäärän muotoilua. UserInfo-taulun kuvaus löytyy [täältä.](<https://support.nepton.com/hc/fi/articles/360002489257>)
[code] 
    SELECT 
      CASE
        WHEN Value IS NULL OR Value = ''   THEN NULL
        ELSE
          date(substring_index(Value, '.', -1) || '-' || substr('0' || substring_index(substring_index(Value, '.', 2), '.', -1), -2, 2)
          || '-' || substr('0' || substring_index(Value, '.', 1), -2, 2))
      END AS CustomData1
    FROM
      UserInfoData
    WHERE
      InfoTypeName = 'LastWorkingContractBeginDate'
[/code]
## 4 Poimitaan henkilöryhmän puurakenne
Poimitaan henkilöryhmän puurakenne ja esitetään puurakenteen koodi henkilön kalleusluokka -tiedossa. Koodin osat erotellaan / -merkillä. 
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
           ugd.Id,
           ugd.Depth,
           ugd.Code,
           ugd.Name,
           ugd.ParentId,
           r.AssignedGroupId
         FROM
           UserGroupData ugd
         JOIN UserGroupRecursive r ON ugd.Id = r.ParentId
         WHERE
           r.Depth > ugd.Depth)
    SELECT
      usd.*,
      CASE
        WHEN g1.Code IS NULL THEN ''
        ELSE g1.Code
      END ||
      CASE
        WHEN g2.Code IS NULL THEN ''
        ELSE '/' || g2.Code
      END ||
      CASE
        WHEN g3.Code IS NULL THEN ''
        ELSE '/' || g3.Code
      END ||
      CASE
        WHEN g4.Code IS NULL THEN ''
        ELSE '/' || g4.Code
      END AS OverrideUserCostGroup
    FROM
      UserSalaryData usd
    LEFT JOIN UserInfoData uid ON
      usd.UserId = uid.UserId
      AND uid.InfoTypeName = 'UserGroupId_SDSQL'
      AND datetime(usd.SalaryRenderingDate) BETWEEN uid.UserId.ValidFrom AND uid.UserId.ValidTo
    LEFT JOIN UserGroupRecursive g1 ON CAST(uid.Value AS INTEGER) = g1.AssignedGroupId AND g1.Depth = 0
    LEFT JOIN UserGroupRecursive g2 ON CAST(uid.Value AS INTEGER) = g2.AssignedGroupId AND g2.Depth = 1
    LEFT JOIN UserGroupRecursive g3 ON CAST(uid.Value AS INTEGER) = g3.AssignedGroupId AND g3.Depth = 2
    LEFT JOIN UserGroupRecursive g4 ON CAST(uid.Value AS INTEGER) = g4.AssignedGroupId AND g4.Depth = 3
    WHERE
      usd.CompensationType = 'BasicTime'
[/code]
## 5 Poimitaan henkilöryhmien ja projektien puurakenne
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
         JOIN UserGroupRecursive r ON g.Id = r.ParentId
         WHERE r.Depth > g.Depth),
      ProjectRecursive (Id, Depth, Code, Name, ExternalId, TypeInternalName, ParentId, AssignedProjectId) AS
        (SELECT
           Id,
           Depth,
           Code,
           Name,
           ExternalId,
           TypeInternalName,
           ParentId,
           Id AS AssignedProjectId
         FROM
           ProjectData
         WHERE
           IsAssignedProject = 'Y'
         UNION ALL
         SELECT
           p.Id,
           p.Depth,
           p.Code,
           p.Name,
           p.ExternalId,
           p.TypeInternalName,
           p.ParentId,
           r.AssignedProjectId
         FROM ProjectData p
         JOIN ProjectRecursive r ON p.Id = r.ParentId
         WHERE
           r.Depth > p.Depth)
    SELECT
      usd.*,
      CASE
        WHEN g1.Code IS NULL THEN ''
        ELSE g1.Code
      END ||
      CASE
        WHEN g2.Code IS NULL THEN ''
        ELSE '/' || g2.Code
      END ||
      CASE
        WHEN g3.Code IS NULL THEN ''
        ELSE '/' || g3.Code
      END ||
      CASE
        WHEN g4.Code IS NULL THEN ''
        ELSE '/' || g4.Code
      END AS OverrideUserCostGroup,
      p1.Id AS OverrideProjectId1,
      p2.Id AS OverrideProjectId2,
      p3.Id AS OverrideProjectId3,
      p4.Id AS OverrideProjectId4,
      p1.ExternalId AS OverrideProjectExternalIdentifier1,
      p2.ExternalId AS OverrideProjectExternalIdentifier2,
      p3.ExternalId AS OverrideProjectExternalIdentifier3,
      p4.ExternalId AS OverrideProjectExternalIdentifier4,
      p1.TypeInternalName AS OverrideProjectType1,
      p2.TypeInternalName AS OverrideProjectType2,
      p3.TypeInternalName AS OverrideProjectType3,
      p4.TypeInternalName AS OverrideProjectType4, 
      p1.Code AS OverrideProjectCode1,
      p2.Code AS OverrideProjectCode2,
      p3.Code AS OverrideProjectCode3,
      p4.Code AS OverrideProjectCode4,
      p1.Name AS OverrideProjectName1,
      p2.Name AS OverrideProjectName2,
      p3.Name AS OverrideProjectName3,
      p4.Name AS OverrideProjectName4
    FROM
      UserSalaryData usd
    LEFT JOIN UserInfoData uid ON
      usd.UserId = uid.UserId
      AND uid.InfoTypeName = 'UserGroupId_SDSQL'
      AND datetime(usd.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo
    LEFT JOIN UserGroupRecursive g1 ON CAST(i.Value AS INTEGER) = g1.AssignedGroupId AND g1.Depth = 0
    LEFT JOIN UserGroupRecursive g2 ON CAST(i.Value AS INTEGER) = g2.AssignedGroupId AND g2.Depth = 1
    LEFT JOIN UserGroupRecursive g3 ON CAST(i.Value AS INTEGER) = g3.AssignedGroupId AND g3.Depth = 2
    LEFT JOIN UserGroupRecursive g4 ON CAST(i.Value AS INTEGER) = g4.AssignedGroupId AND g4.Depth = 3
    LEFT JOIN ProjectRecursive p1 ON usd.ProjectId1 = p1.AssignedProjectId AND p1.Depth = 0
    LEFT JOIN ProjectRecursive p2 ON usd.ProjectId1 = p2.AssignedProjectId AND p2.Depth = 1
    LEFT JOIN ProjectRecursive p3 ON usd.ProjectId1 = p3.AssignedProjectId AND p3.Depth = 2
    LEFT JOIN ProjectRecursive p4 ON usd.ProjectId1 = p4.AssignedProjectId AND p4.Depth = 3
    WHERE
     usd.CompensationType = 'BasicTime'
[/code]
##  6 Poimitaan henkilöiden ulkoisten palveluiden tunnisteet vientiä varten 
[code] 
    SELECT
      usd.*,
      uid.value as OverrideIntegrationId
    FROM
      UserSalaryData usd
    LEFT JOIN UserInfoData uid ON
      usd.userId = uid.userId 
      AND datetime(usd.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo
    WHERE
      uid.infotypename = 'IntegrationIdAastra' -- or IntegrationIdKieku or DefaultCostGroupCode etc..
    -- AND usd.compensationtype = 'BasicTime'
    -- AND jne
[/code]
##  7 Poimitaan henkilöiden maksuryhmien maksuryhmän tunnisteet ja maksukaudet vientiä varten 
[code] 
    SELECT 
      pgpd.* 
    FROM 
      UserSalaryData usd 
    LEFT JOIN UserInfoData uid ON
      usd.UserId = uid.UserId 
      AND datetime(usd.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo 
    LEFT JOIN PaymentGroupPeriodData pgpd ON
      uid.Value = pgpd.NeptonPaymentGroupIdentifier
    WHERE 
      uid.InfoTypeName = 'NeptonPaymentGroupIdentifier'
    GROUP BY 
      pgpd.NeptonPaymentGroupPeriodIdentifier
[/code]
