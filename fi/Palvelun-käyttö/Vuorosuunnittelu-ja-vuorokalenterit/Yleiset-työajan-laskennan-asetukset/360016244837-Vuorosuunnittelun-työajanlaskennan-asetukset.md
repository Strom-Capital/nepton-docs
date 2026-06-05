---
id: 360016244837
title: Vuorosuunnittelun työajanlaskennan asetukset
url: https://support.nepton.com/hc/fi/articles/360016244837-Vuorosuunnittelun-ty%C3%B6ajanlaskennan-asetukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleiset työajan laskennan asetukset
section_id: 19210968853277
section_path:
- Vuorosuunnittelu ja vuorokalenterit
- Yleiset työajan laskennan asetukset
labels:
- työaikasuunnittelu
promoted: false
updated_at: '2024-09-02T11:19:02Z'
edited_at: '2024-09-02T11:18:48Z'
---

# Vuorosuunnittelun työajanlaskennan asetukset

Seuraavat asetukset vaikuttavat tulkitun työajan laskentaan sekä vuorojen keston laskentaan vuorosuunnittelussa. Asetukset vaikuttavat myös vuorokalenterissa luotuihin vuoroihin. Asetukset löytyvät kohdasta **Työsuhde - > Hallinta -> Asetukset -> Vuorosuunnittelu.**
## Oletetun ruokatauon vähennys
Tässä määritetyt ruokatauon vähennysmääritykset ohittavat työyhteisötasolla, asetusryhmässä, henkilöasetuksissa tehdyt [ruokatauon määritykset. ](<https://support.nepton.com/hc/fi/articles/360002558757>)
### Ruokatauon kesto
Tällä asetuksella asetetaan se ruokatauon kesto, joka vähennetään tulkitusta työajasta silloin kun tulkittu työaika ylittää asetetun vähimmäiskeston.
### Vuoron vähimmäiskesto ennen ruokatauon vähennystä
Asetettu vuoron vähimmäiskesto, jonka jälkeen vuoron oletetaan sisältävän ruokatauon. Tällöin ruokatauon pituutta ei lasketa vuorosuunnittelun yhteensä summissa. Jos tulkittu työaika ylittää vähimmäiskeston niin ruokatauko vähennetään tulkitusta työajasta asetetun ruokatauon keston mukaisena.
![WSP_settings_2.png](https://support.nepton.com/hc/article_attachments/360014814558)
## Juhlapyhäasetukset
### Juhlapyhän lyhennetty pituus
Määritetään, minkä kestoisena arkipäivälle osuva juhlapyhä lyhentää viikottaista työaikaa vuorosuunnittelussa, jos lyhennyksen on tarkoitus olla pienempi kuin henkilön keskimääräinen työaika. Jos asetus on aktivoitu, henkilölle suunniteltavaa työn määrää vähennetään tässä määritellyn pituuden verran jokaiselta jakson juhlapyhältä. Jos asetusta ei ole määritelty tai henkilön tavanomainen päivittäinen työaika laskettuna viikottaisesta maksimityöajasta on lyhyempi kuin juhlapyhän lyhennetty pituus, käytetään henkilön viikkotyöajasta laskettua arvoa. Päivät, jotka ovat juhlapyhiä, määritellään [juhla- ja arkipyhien käsittelyssä](<https://support.nepton.com/hc/fi/articles/360002558797>).
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4411632353169)
#### Esimerkkejä juhlapyhän lyhennetyn pituuden käytöstä
_Esimerkki 1_ : Juhlapyhän lyhennetty pituus 06:00:
  * Henkilön viikoittaiset tunnit MAX: 37,5 tuntia → laskennallinen päivittäinen työaika on 7,5 tuntia → juhlapyhän osalta vähennetään 6 tuntia asetuksen mukaisesti.
  * Henkilön viikottaiset tunnit MAX: 20 tuntia → laskennallinen päivittäinen työaika on 4 tuntia → juhlapyhän osalta vähennetään 4 tuntia, koska päivittäinen työaika on lyhyempi kuin juhlapyhän lyhennetty pituus.


_Esimerkki 2_ : Juhlapyhän lyhennettyä pituutta ei ole määritelty:
  * Henkilön viikoittaiset tunnit MAX: 37,5 tuntia → laskennallinen päivittäinen työaika on 7,5 tuntia → juhlapyhän osalta vähennetään 7,5 tuntia.
  * Henkilön viikottaiset tunnit MAX: 20 tuntia → laskennallinen päivittäinen työaika on 4 tuntia → juhlapyhän osalta vähennetään 4 tuntia.


## TES-säännöt
Osiossa määritellään lepoajat ja ne on käsitelty tarkemmin [täällä](<https://support.nepton.com/hc/fi/articles/360006832837>).
![WSP_settings_4.png](https://support.nepton.com/hc/article_attachments/360014814598)
