---
id: 360019840237
title: Projektien API
url: https://support.nepton.com/hc/fi/articles/360019840237-Projektien-API
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
- projektit
promoted: false
updated_at: '2025-09-08T10:11:18Z'
edited_at: '2023-11-23T15:15:26Z'
---

# Projektien API

Tämä artikkeli kuvaa [Työajan APIn](<https://support.nepton.com/hc/articles/360004861558>) metodeja projektien käsittelyyn. [Tästä](<https://support.nepton.com/hc/fi/articles/360004861518>) artikkeliin joka kuvaa API liittymän käyttöönottoa.
## Projektien haku
Palvelun kautta on mahdollista hakea projekteja ja toimipisteitä ja suodattaa haettuja tuloksia.
API-metodit projektien hakemiseen:
  * [GetProjects (vanhentunut)](<https://support.nepton.com/hc/fi/articles/6913429557405>)
  * [GetProjectsV2](<https://support.nepton.com/hc/fi/articles/6904062030621>)


## Projektien lisääminen ja päivittäminen
Palvelun kautta on mahdollista lisätä ja päivittää projekteja. Palvelusta löytyy metodit projektin lisäämiseen, projektin päivittämiseen sekä kolmas vaihtoehto, jolla pystyt yhden kutsun avulla joko luomaan tai päivittämään projekteja Neptonissa perustuen johonkin tunnistetietoon. Jälkimmäinen vaihtoehto on suunniteltu erityisesti eräajoihin sekä tietojen synkronointiin Neptonin ja erillisen järjestelmän välillä.
API-metodi, jolla voidaan lisätä projekteja:
  * [InsertProjects](<https://support.nepton.com/hc/fi/articles/6903131386013>)


API-metodi, jolla voidaan päivittää projekteja:
  * [UpdateProjects](<https://support.nepton.com/hc/fi/articles/6913613074845>)


API-metodit, jolla voidaan luoda tai päivittää olemassa olevia projekteja:
  * [EnsureProjectsExist (vanhentunut)](<https://support.nepton.com/hc/articles/6880677487005>)
  * [EnsureProjectsExistV2 (vanhentunut)](<https://support.nepton.com/hc/articles/360005783318>)
  * [EnsureProjectsExistV3](<https://support.nepton.com/hc/fi/articles/13106403486109>)


## Projektien näkyvyyden muuttaminen käyttäjätasolla
Palvelun kautta voidaan muuttaa projektien näkyvyyttä käyttäjätasolla.
API-metodit, jolla voidaan asettaa projektit näkymään käyttäjälle
  * [SetVisibleProjectsForUser (vanhentunut)](<https://support.nepton.com/hc/fi/articles/6885147716893>)
  * [SetVisibleProjectsForUserV2](<https://support.nepton.com/hc/fi/articles/360005968797>)


API-metodi, jolla voidaan tyhjentää käyttäjäkohtaiset projektien näkyvyys säännöt tietyltä käyttäjältä:
  * ClearVisibleProjectsFromUser
