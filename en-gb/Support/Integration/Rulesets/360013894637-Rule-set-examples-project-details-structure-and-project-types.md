---
id: 360013894637
title: Rule set examples - project details, structure and project types
url: https://support.nepton.com/hc/en-gb/articles/360013894637-Rule-set-examples-project-details-structure-and-project-types
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
updated_at: '2026-09-14T10:19:17Z'
edited_at: '2025-06-13T07:18:08Z'
---

# Rule set examples - project details, structure and project types

**Sorry!**  
This article has not been translated yet.
Artikkeliin on koottu tyypillisiä projektien rakenteeseen ja projektien huomioihin liittyviä poiminnan esimerkkejä
Löydät tietokantataulujen sarakekuvaukset [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>)
Tyypilliset poissaolojen poiminnan esimerkit ovat [tässä](<https://support.nepton.com/hc/fi/articles/360013979998>) artikkelissa, työajan poiminta [tässä](<https://support.nepton.com/hc/fi/articles/360008045337>) artikkelissa ja henkilötietojen poiminnan esimerkit [tässä](<https://support.nepton.com/hc/fi/articles/360015612638>) artikkelissa.
### Poimitaan projektikoodit halutussa järjestyksessä riippumatta niiden syöttöjärjestyksessä 
Esimerkissä poimitaan OverrideProjectCode1 arvoksi sen projektin koodi, jonka tyyppi on '4'. Lisäksi poimitaan OverrideProjectCode2 arvoksi sen projektin koodi, jonka tyyppi on 'Ulkoiset'
[code] 
    SELECT 
      *, 
      CASE 
        WHEN ProjectType1 = '4' THEN ProjectCode1 
        WHEN ProjectType2 = '4' THEN ProjectCode2 
        WHEN ProjectType3 = '4' THEN ProjectCode3 
        WHEN ProjectType3 = '4' THEN ProjectCode4 
        ELSE 'NOTFOUND'
      END AS OverrideProjectCode1, 
      CASE 
        WHEN ProjectType1 = 'Ulkoiset' THEN ProjectCode1
        WHEN ProjectType2 = 'Ulkoiset' THEN ProjectCode2
        WHEN ProjectType3 = 'Ulkoiset' THEN ProjectCode3
        WHEN ProjectType4 = 'Ulkoiset' THEN ProjectCode4
        ELSE 'NOTFOUND'
      END AS OverrideProjectCode2
    FROM 
      UserSalaryData 
    WHERE 
      CompensationType = 'BasicTime' 
    
    
[/code]
### Poimitaan aika projektien julkisten huomautuksien ja nimien kanssa
Tämä kysely lisää projektikirjausten julkiset huomautukset ja projektin nimen palkka-aineistolle enintään kahdessa päällekkäisessä projektissa ja koska ryhmittelemme julkisten huomautusten ja projektin mukaan, ryhmittelyssä ja summauksessa ei häviä huomautustietoja. Useimmissa liittymissä ei ole sarakkeita tällaisille tiedoille, joten voit harkita esimerkiksi kommentti- tai CustomData-kenttien käyttämistä.
[code] 
    SELECT 
      usd.*, 
      SUM(amount) as OverrideAmount, 
      ProjectOverlap1.PublicNotes as PublicProjectNotes1, 
      ProjectData1.Name as ProjectName1, 
      ProjectOverlap2.PublicNotes as PublicProjectNotes2, 
      ProjectData2.Name as ProjectName2 
    FROM 
      UserSalaryData 
    LEFT JOIN UserEventProjectData ProjectOverlap1 ON usd.EventProjectRowId1 = ProjectOverlap1.Id 
    LEFT JOIN ProjectData ProjectData1 ON ProjectOverlap1.ProjectId = ProjectData1.Id 
    LEFT JOIN UserEventProjectData ProjectOverlap2 ON usd.EventProjectRowId2 = ProjectOverlap2.Id 
    LEFT JOIN ProjectData as ProjectData2 ON ProjectOverlap2.ProjectId = ProjectData2.Id 
    WHERE 
      CompensationType = 'BasicTime' 
    GROUP BY 
      SalaryRenderingDate, 
      ProjectId1, 
      ProjectId2, 
      ProjectOverlap1.PublicNotes, 
      ProjectOverlap2.PublicNotes
[/code]
### Poimitaan projektin kaikki yläprojektit
Kysely poimii tapahtumalle kirjatun projektin puurakenteen seuraavasti:
  * Projekti 1 - juuritason projekti
  * Projekti 2 - juuritason projektin alaprojekti
  * Projekti 3 - edellisen projektin alaprojekti
  * Projekti 4 - edellisen projektin alaprojekti


Jos projektitasoja on esimerkiksi kolme:
  * Projekti 3 -tiedossa on tapahtumalle kirjattu projekti
  * Projekti 2 -tiedossa on projekti 3:n yläprojekti
  * Projekti 1 -tiedossa on projekti 2:n yläprojekti ja projekti on juuritason projekti


[code] 
    WITH RECURSIVE
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
    FROM UserSalaryData usd
    LEFT JOIN ProjectRecursive p1 ON usd.ProjectId1 = p1.AssignedProjectId AND p1.Depth = 0
    LEFT JOIN ProjectRecursive p2 ON usd.ProjectId1 = p2.AssignedProjectId AND p2.Depth = 1
    LEFT JOIN ProjectRecursive p3 ON usd.ProjectId1 = p3.AssignedProjectId AND p3.Depth = 2
    LEFT JOIN ProjectRecursive p4 ON usd.ProjectId1 = p4.AssignedProjectId AND p4.Depth = 3
    WHERE
      usd.CompensationType = 'BasicTime'
[/code]
