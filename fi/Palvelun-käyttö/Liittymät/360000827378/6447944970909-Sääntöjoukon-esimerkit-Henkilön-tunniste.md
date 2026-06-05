---
id: 6447944970909
title: Sääntöjoukon esimerkit - Henkilön tunniste
url: https://support.nepton.com/hc/fi/articles/6447944970909-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-Henkil%C3%B6n-tunniste
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
updated_at: '2025-05-06T11:14:25Z'
edited_at: '2025-05-06T11:14:25Z'
---

# Sääntöjoukon esimerkit - Henkilön tunniste

Osa liittymistä sallii sääntöjoukon ylikirjoittaa käyttäjän tunnisteen. Sääntöjoukon kyselyssä voidaan funktioiden avulla myös toteuttaa tunnisteen poimintaan erilainen logiikka, kuin mitä Nepton normaalisti käyttäisi.
Käyttäjän tunnisteen ylikirjoitus ei ole käytettävissa kaikkien liittymien kohdalla. Tarkista kyseessä olevan liittymän tukiartikkelista, tukeeko liittymä käyttäjän tunnisteen ylikirjoittamista.
Tarkista että ulkoinen järjestelmä, johon tietoa ollaan siirtämässä, pystyy kohdistamaan tapahtumat oikein tunnisteella, jonka olet määrittänyt.
Käyttäjän tunnisteen ylikirjoitus tapahtuu aina määrittämällä kyselyyn sarake 'OverrideUserIntegrationId'.
UserData taulu sisältää sarakkeen 'UserIntegrationId' joka sisältää liittymän peruslogiikan mukaisen tunnisteen henkilölle.
# Käyttäjän henkilönumero integraation tunnisteena
UserInfoData-taulun liittämällä voidaan poimia käyttäjän henkilönumero käyttäjän tunnisteeksi. Huom. mikäli ylikirjoitussarake saisi NULL-arvon riville käytettäisiin siinä kohtaa oletuslogiikkaa tunnisteen poimimiseen. ifnull-funktiolla voidaan korvata NULL-arvo jollain muulla arvolla tai toisen kentän sisällöllä. Esimerkissä on liitos tehty INNER JOIN lauseella joka palauttaa vain ne rivit jotka saatiin liitettyä henkilönumero tyyppiseen tietoriviin.
[code] 
    SELECT   
      usd.*,   
      uid.Value AS OverrideUserIntegrationId   
    FROM   
      UserSalaryData usd  
      INNER JOIN UserInfoData uid ON  
        (usd.UserId = uid.UserId   
         AND uid.InfoTypeName = 'PersonnelNumber'   
         AND DATETIME(usd.SalaryRenderingDate) BETWEEN uid.ValidFrom AND uid.ValidTo)
[/code]
