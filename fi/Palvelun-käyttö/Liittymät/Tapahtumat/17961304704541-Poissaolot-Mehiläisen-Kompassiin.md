---
id: 17961304704541
title: Poissaolot Mehiläisen Kompassiin
url: https://support.nepton.com/hc/fi/articles/17961304704541-Poissaolot-Mehil%C3%A4isen-Kompassiin
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumat
section_id: 360001061298
section_path:
- Liittymät
- Tapahtumat
labels: []
promoted: false
updated_at: '2025-01-28T07:53:12Z'
edited_at: '2024-11-12T13:47:49Z'
---

# Poissaolot Mehiläisen Kompassiin

Poissaolotapahtumien vienti Neptonista Mehiläisen Kompassi-järjestelmään onnistuu [mukautetun viennin](<https://support.nepton.com/hc/fi/articles/10758741671581-Mukautetut-Ty%C3%B6ajan-viennit>) avulla.
## Poimintasääntö
Esimerkin poimintasäännössä poimitaan sairauspoissaoloja ja määritellään, että riville muodostuvat tyhjät kentät rivin alkuun ja loppuun. Kompassi vaatii rivien juoksevan numeroinnin ensimmäiseen kenttään mutta sitä ei tarvitse Neptonista lähtiessä olla. Viimeinen kenttä on Kompassissa poissaolon syy, jota ei myöskään Neptonista tarvita ja se saa olla tyhjä kenttä. 
[code] 
    SELECT   
    '""' as emptyColumn1,   
    CASE WHEN UserEventData.SickLeaveTypeId = 1   
    AND SickLeaveMedicalCertificateId = 3 THEN '"O"' -- Omailmoitteinen sairauspoissaolo  
    WHEN UserEventData.SickLeaveTypeId = 1   
    AND SickLeaveCompensationTypeId = 2 THEN '"S1"' -- Sairauspoissaolo palkaton   
    WHEN UserEventData.SickLeaveTypeId = 2 THEN '"LS"' -- Lapsen sairaus   
    WHEN UserEventData.SickLeaveTypeId = 3 THEN '"T"' -- Työtapaturma   
    WHEN UserEventData.SickLeaveTypeId = 5 THEN '"S2"' -- Vapaa - ajan tapaturma   
    WHEN UserEventData.SickLeaveTypeId = 1 THEN '"S"' -- Sairauspoissaolo  
    ELSE '""' END AS SickLeaveType,   
    CONCAT('"', UserInfoData.Value, '"') AS socialSecurityNumber,   
    CONCAT('"', DATE(UserEventData.startDateTime), '"') as startDate,   
    CONCAT('"', DATE(UserEventData.endDateTime), '"') as endDate,   
    '""' as customReasonCode   
    FROM   
    UserEventData   
    INNER JOIN UserInfoData ON ( -- INNER JOIN -lausekkeella haetaan henkilötunnus ja varmistetaan, että se on voimassa haetulla jaksolla  
    UserInfoData.UserId = UserEventData.UserId   
    AND UserInfoData.InfoTypeName = 'SocialSecurityNumber'   
    AND datetime(UserEventData.startDateTime) BETWEEN UserInfoData.ValidFrom   
    AND UserInfoData.ValidTo  
    )   
    WHERE   
    ActivityTypeCode = 2
[/code]
### Esimerkki poiminnan tuloksista (csv-tiedosto):
[code] 
    "";"S";"456789-456A";"2024-02-22";"2024-02-23";""  
    "";"S2";"987654-987B";"2024-02-13";"2024-02-28";""
[/code]
Sisältö:
"[tyhjä]";"poissaolon tyyppi";"henkilötunnus";"poissaolon alkamispäivämäärä";"poissaolon loppumispäivämäärä";"[tyhjä]"
Tuloksiin tulevat vain sellaisten käyttäjien tapahtumat, joilla on henkilötunnus määriteltynä profiileissaan. Poimintaesimerkissä henkilötunnus haetaan INNER JOIN -lausekkeella.
## Mukautetun viennin asetukset
Alla näkyvät kyseisen mukautetun viennin asetukset, lisäksi asetetaan mahdolliset SFTP-asetukset ja viennin ajastus.
![](https://support.nepton.com/hc/article_attachments/17961304700829)
