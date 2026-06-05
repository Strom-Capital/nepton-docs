---
id: 360019841037
title: Päätepalveluiden API
url: https://support.nepton.com/hc/fi/articles/360019841037-P%C3%A4%C3%A4tepalveluiden-API
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
- API
- pääte
promoted: false
updated_at: '2025-09-08T12:00:20Z'
edited_at: '2025-09-08T11:31:10Z'
---

# Päätepalveluiden API

Tässä artikkelissa kuvataan Työajan APIn menetelmiä päätepalvelujen käsittelemiseksi. Kuvattuja menetelmiä on teknisesti mahdollista käyttää myös muissa yhteyksissä mutta ne on ensisijaisesti suunniteltu työaikapäätekirjauksiin.
## Tapahtuman aloittaminen
Palvelun kautta on mahdollista aloittaa uusi tapahtuma. Esim. käyttäjä kirjaa työpäivan aloitetuksi
API-metodit tapahtuman aloittamiseen:
  * [ BeginActivity (vanhentunut) ](<https://support.nepton.com/hc/fi/articles/6869807559453>)
  * [BeginActivityV2](<https://support.nepton.com/hc/fi/articles/6869562936221>)


## Tapahtuman päättäminen
Palvelun kautta on mahdollista päättää avoinna oleva tapahtuma. Esim. käyttäjä lopettaa työpäivän ja kirjaa itsensä pois työajalta.
API-metodit tapahtuman päättämiseen:
  * [ EndActivity (vanhentunut) ](<https://support.nepton.com/hc/fi/articles/6870299031581>)
  * [EndActivityV2](<https://support.nepton.com/hc/fi/articles/6870443544477>)


## Päätekirjautuminen
Palvelun kautta on mahdollista saada tiettyä käyttäjää koskevia tietoja nykyhetkellä esim. avoinna olevan tapahtuman tiedot tai tapahtumatyypit, joita käyttäjä pystyy valitsemaan.
API-metodit:
  * [TerminalLogin (vanhentunut)](<https://support.nepton.com/hc/fi/articles/6887099778333>)
  * [TerminalLoginV2](<https://support.nepton.com/hc/fi/articles/360021180898>)
