---
id: 360019840217
title: Tapahtumien API
url: https://support.nepton.com/hc/fi/articles/360019840217-Tapahtumien-API
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Työajan API
section_id: 360005706218
section_path:
- Liittymät
- Sovellusliittymät (API)
- Työajan API
labels:
- tapahtumien API
- getworktargetunit
promoted: false
updated_at: '2025-09-08T08:40:16Z'
edited_at: '2025-09-08T08:16:23Z'
---

# Tapahtumien API

Tässä artikkelissa kuvataan Työajan APIn metodeita tapahtumien käsittelyyn. [Tästä](<https://support.nepton.com/hc/fi/articles/360004861518>) artikkeliin, jossa kuvataan API liittymän käyttöönotto.
## Hae tapahtumia
API:sta voi hakea työtapahtumia, poissaoloja, lomapäiviä, matkalaskuja, suunniteltuja työvuoroja sekä muita tapahtumatietoja. Haettuja tietoja voidaan myös API-kutsussa suodattaa tietyin kriteerein (esim. käyttäjä tai ajanjakso)
API-metodit tapahtumien hakemiseen
  * [GetActivities (Vanhentunut)](<https://support.nepton.com/hc/fi/articles/6580727241501>)
  * [GetActivitiesV2 (Vanhentunut)](<https://support.nepton.com/hc/fi/articles/6580610511133>)
  * [GetActivitiesV3](<https://support.nepton.com/hc/fi/articles/360020751677>)


## Lisää tapahtumia
APIn kautta voit lisätä tapahtumia, poissaoloja, lomapäiviä, matkalaskuja tai muita tapahtumatietoja käyttäjälle.
API-metodit tapahtumien lisäämiseen:
  * [ InsertActivities (vanhentunut) ](<https://support.nepton.com/hc/fi/articles/6788254740893>)
  * [ InsertActivitiesV2 (Vanhentunut) ](<https://support.nepton.com/hc/fi/articles/6788513921565>)
  * [InsertActivitiesV3](<https://support.nepton.com/hc/fi/articles/6788985086621>)


## Päivitä tapahtumia
Voit päivittää määritettyjä tapahtumia API:n kautta. Päivitettävät tapahtumat on mahdollista osoittaa yksilöllisen Neptonin tunnisteen lisäksi myös ulkoisella tunnisteella, mikäli sellainen on tapahtumalle määritetty lisäysvaiheessa 
API-metodit tapahtumien päivitykseen:
  * [UpdateActivities (vanhentunut)](<https://support.nepton.com/hc/fi/articles/6865125183261>)
  * [UpdateActivitiesV2 (vanhentunut)](<https://support.nepton.com/hc/fi/articles/6865441448861>)
  * [UpdateActivitiesV3](<https://support.nepton.com/hc/fi/articles/6865760767645>)


## Hae tapahtumatyyppejä
Palvelun kautta voi hakea kaikki Neptoniin määritetyt tapahtumatyypit sekä tapahtumatyyppien nimet kaikilla Neptonin tukemilla kielillä.
API-metodit tapahtumatyyppien hakemiseen:
  * [GetActivityTypes](<https://support.nepton.com/hc/articles/6899092915101>)


Asetuksista riippuen jotkin tapahtumatyypit eivät välttämättä ole saatavilla kaikille käyttäjille. Tietylle käyttäjälle sopivien tapahtumatyyppien hakemista varten katso [TerminalLogin](<https://support.nepton.com/hc/articles/360019841037#TerminalLogin>) verkkopalvelu metodi.
