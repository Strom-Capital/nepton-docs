---
id: 360002590137
title: Microsoft-kirjautumisen yleiskuvaus
url: https://support.nepton.com/hc/fi/articles/360002590137-Microsoft-kirjautumisen-yleiskuvaus
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Microsoft-kirjautuminen
section_id: 360002832097
section_path:
- Kirjautuminen
- Kertakirjautuminen (SSO)
- Microsoft-kirjautuminen
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2025-08-11T08:54:42Z'
edited_at: '2025-08-11T08:53:22Z'
---

# Microsoft-kirjautumisen yleiskuvaus

Microsoft Azure Active Directory on nyt Microsoft Entra ID
Ottamalla käyttöön Microsoft-kirjautumisen, pääsy Neptoniin tapahtuu Microsoft-tilille kirjautumisen kautta. Kirjautumiseen voidaan tällöin lisäksi soveltaa organisaation vakioituja Entra ID turvallisuussääntöjä.
![](https://support.nepton.com/hc/article_attachments/29507448748701)
## Paras käytäntö
Suositeltu paras käytäntö kertakirjautumisen toteuttamiseen on kuvattu tässä ja linkitetyissä artikkeleissa.
Paras käytäntö on toteuttaa kertakirjautuminen suoralla MSAL Microsoft Identity Platform integraatiolla., Tämä lähestymistapa vähentää merkittävästi kertakirjautumisen alkuperäiseen määritykseen ja pitkäaikaiseen ylläpitoon liittyvää työkuormaa verrattuna perinteisempiin SAML pohjaisiin toteutuksiin. Yli 90% Neptonin enterprise-asiakkaista on valinnut suositellun MSAL pohjaisen toteutuksen.
## Parhaan käytännön toteutus
Microsoft-kirjautumisen käyttöönotto vaatii Entra ID määrityksiä, johon löytyy ohje [täältä](<https://support.nepton.com/hc/fi/articles/360009872457>). 
Huomioithan, että jos tarvitset toimittajan projektityötä Microsoft-kirjautumisen käyttöönotossa, on se tuntihinnaston mukaan veloitettavaa työtä.
Käyttäjä voi myös kirjautua palveluun suorakirjautumislinkillä ilman erillistä kertakirjautumisen painiketta. Käyttäjä kirjataan suoraan palveluun sisään, mikäli hän on kirjautuneena Microsoft-tililleen, muutoin hänet ohjataan sisäänkirjautumissivulle. Suorakirjautumislinkin näet Ylläpitäjä-roolissa Microsoft-kirjautumisten listasta menemällä Työsuhde > Hallinta > Kertakirjautuminen (SSO) > Microsoft-kirjautuminen.
