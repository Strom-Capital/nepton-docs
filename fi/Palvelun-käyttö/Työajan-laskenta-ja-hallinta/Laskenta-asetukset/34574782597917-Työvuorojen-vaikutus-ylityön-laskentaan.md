---
id: 34574782597917
title: Työvuorojen vaikutus ylityön laskentaan
url: https://support.nepton.com/hc/fi/articles/34574782597917-Ty%C3%B6vuorojen-vaikutus-ylity%C3%B6n-laskentaan
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- ylityö
- työajan laskenta
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2026-03-12T08:54:03Z'
---

# Työvuorojen vaikutus ylityön laskentaan

Tässä ohjeessa kuvataan, miten suunniteltu työvuoro vaikuttaa ylityön kertymiseen ja miten vuoron ulkopuolella tehty työ tulkitaan työajanlaskennassa. Ylityön tulkintaan voidaan vaikuttaa Vuorot-osiossa olevissa asetuksilla, joilla määritetään, lasketaanko vuoron ulkopuolella tehty työ heti ylityöksi vai täyttääkö se ensin säännöllisen työajan. Jos päivälle halutaan muodostuvan ylityön lisäksi tarkempaa laskentaa, kuten kertymämiinusta, tulee ottaa [oletetut työajat](<https://support.nepton.com/hc/fi/articles/360002558617-Oletetut-ty%C3%B6ajat>) käyttöön.
### Työajan ja poissaoloajan korvausasetukset
Vuorot-osiossa on käytettävissä kaksi asetusta:
  * Työaika korvataan työvuorojen ajalta ennen kuin se korvataan vuorojen ulkopuolelta
  * Poissaoloaika korvataan työvuorojen ajalta ennen kuin se korvataan vuorojen ulkopuolelta


![Screenshot 2026-03-12 090442.png](https://support.nepton.com/hc/article_attachments/34574782594973)
Näillä asetuksilla määritetään, miten vuoron ulkopuolella tehty työ tulkitaan ja miten ylityö kertyy suhteessa suunniteltuun työvuoroon. Asetukset määritetään kohdassa:
**Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Vuorot**
Kun asetuksen arvona on "Kyllä", ylityö (työvelvoitteen yli menevä työaika) ansaitaan ensisijaisesti työvuoron ulkopuolella tehdystä työstä. Käytännössä tämä tarkoittaa, että ylityötä voidaan ansaita ennen suunnitellun työvuoron alkua. Asetusken oletusarvo on "Kyllä", jos arvoa ei ole erikseen muutettu.
Kun aetuksen arvona "Ei" tai "Ei asetettu", ylityö (työvelvoitteen yli menevä työaika) ansaitaan vasta tehdyn työvuoron päätteeksi. Vuoron ulkopuolella tehty työ täyttää ensin säännöllisen työajan, ja ylityötä alkaa kertyä vasta sen jälkeen.
### Ylityön kertyminen suunnitellun vuoron kanssa
Seuraavissa esimerkeissä havainnollistetaan, miten ylityötä kertyy erilaisissa tilanteissa, kun päivälle on suunniteltu työvuoro. Ylityön muodostumiseen vaikuttavat myös määritetyt ylityöasetukset.
#### Esimerkki 1 – Työajan korvausasetus arvolla "Ei"
Päivälle on suunniteltu työvuoro ajalle 8–16. Henkilö on kirjannut ylityönä palkkaan aikaväliltä 6–8 ja tunti-tunnista saldoon aikaväliltä 8–16. Tällöin ajalta 6–8 tehty työ täyttää säännöllistä työaikaa eikä kerrytä ylityötä. Ylityötä alkaa kertyä vasta kun säännöllinen työaika on tullut täyteen, jolloin päivältä ansaitaan saldoplussaa ylityön sijaan.
![Screenshot 2026-03-12 093907.png](https://support.nepton.com/hc/article_attachments/34574910302621)
#### Esimerkki 2 – Työajan korvausasetus arvolla "Kyllä"
Päivälle on suunniteltu työvuoro ajalle 8–16. Henkilö on kirjannut ylityönä palkkaan aikaväliltä 6–8 ja tunti-tunnista saldoon aikaväliltä 8–16. Tällöin ajalta 6–8 kertyy ylityötä.
![Screenshot 2026-03-12 092701.png](https://support.nepton.com/hc/article_attachments/34574735164701)
#### Esimerkki 3 – Työtä tehdään vuoron jälkeen
Päivälle on suunniteltu työvuoro ajalle 9–17. Työtä tehdään ajalla 9–19, jolloin ylityötä muodostuu ajalta 17–19. Työajan korvausasetuksessa arvona on "Kyllä".
![](https://support.nepton.com/hc/article_attachments/34576558937245)
#### Esimerkki 5 – Lyhyempi työpäivä kuin suunniteltu vuoro
Päivälle on suunniteltu työvuoro ajalle 9–17. Työtä tehdään ajalla 8–13, jolloin ylityötä ei muodostu. Päivältä muodostuu saldomiinusta ajoilta 8–9 ja 13–17, koska päivälle on asetettu sallitut työajat, jotka rajaavat työtuntien ansaintaa. Työajan korvausasetuksessa arvona on "Kyllä".
![Screenshot 2026-03-12 095900.png](https://support.nepton.com/hc/article_attachments/34576558937885)
#### Esimerkki 6 – Työtä tehdään sekä ennen vuoroa että vuoron jälkeen
Päivälle on suunniteltu työvuoro ajalle 9–17. Työtä tehdään ajalla 8–19, jolloin ylityötä muodostuu seuraavasti:
  * 8–9: ylityötä 50 %
  * 17–18: ylityötä 50 %
  * 18–19: ylityötä 100 %


![Screenshot 2026-03-12 101228.png](https://support.nepton.com/hc/article_attachments/34576558939165)
### Oletetut työajat suunnitellun vuoron kanssa
[Oletettujen työaikojen](<https://support.nepton.com/hc/fi/articles/360002558617-Oletetut-ty%C3%B6ajat>) avulla voidaan määrittää kellonajat, joiden perusteella lasketaan esimerkiksi saldomiinus ja ylityö saman päivän aikana. Seuraavissa esimerkeissä kuvataan, miten oletetut työajat vaikuttavat laskentaan päivällä, jolla on suunniteltu vuoro.
#### Esimerkki 1 – Työ alkaa ennen oletettuja työaikoja
Oletetut työajat on asetettu ajalle 6–20 ja suunniteltu vuoro sekä tehty työ sijoittuvat ajalle 5–11. Päivältä muodostuu ylityötä ajalta 5–6, koska oletetut työajat alkavat vasta kello 6.
![Screenshot 2026-03-12 102315.png](https://support.nepton.com/hc/article_attachments/34576558939549)
#### Esimerkki 2 – Työ jatkuu oletettujen työaikojen jälkeen
Oletetut työajat on asetettu ajalle 6–20 ja suunniteltu vuoro sekä tehty työ sijoittuvat ajalle 16–22. Ylityötä muodostuu kaksi tuntia ajalta 20–22, koska oletetut työajat päättyvät kello 20.
![Screenshot 2026-03-12 102513.png](https://support.nepton.com/hc/article_attachments/34576527900701)
#### Esimerkki 3 – Hienosuunnittelu vuorotietojen avulla
Oletetut työajat voidaan asettaa suunnitellun vuoron mukaisesti käyttämällä vuorolla olevaa **Vuorotiedot** -kenttää ja [poikkeusasetuksia](<https://support.nepton.com/hc/fi/articles/360002560677-Poikkeusasetusten-m%C3%A4%C3%A4rittely#h_01HA4D033YCH9QDQKEKFWRSA0C>). Tällöin oletettu työaika muodostuu suunnitellun vuoron kellonaikojen mukaisesti, jos vuorolle on kirjattu poikkeusasetuksessa määritetty Comment-tieto. Poikkeusasetus tulee asettaa SQL-lausekkeella.
![Screenshot 2026-03-11 131239.png](https://support.nepton.com/hc/article_attachments/34576527901213)
Päivälle on suunniteltu työvuoro ajalle 7–15. Suunnitellulle vuorolle on lisätty vuorotieto "A07". Työtä tehdään ajalla 8–17, ja päivältä halutaan muodostuvan sekä saldomiinusta että ylityötä. Oletetut työajat muodostuvat suunnitellun vuoron mukaisesti eli ajalle 7–15. Laskenta muodostuu seuraavasti:
  * 7–8: saldomiinusta, koska työvuoro on alkanut vasta kello 8
  * 8–15: säännöllistä työaikaa
  * 15–17: ylityötä


![Screenshot 2026-03-12 103031.png](https://support.nepton.com/hc/article_attachments/34576527904797)
#### Esimerkki 4 – Vuorokalenteri
Oletetut työajat voidaan asettaa suunnitellun vuoron mukaisesti myös vuorokalentereita käyttämällä. Toimintaperiaate on sama kuin esimerkissä 3, mutta oletettujen työaikojen poikkeussäännössä käytetään sääntökomentoa **[WORK-DAY-HAS-ANY-OF-PLANNED-EVENT-ALIASES]** , jonka avulla oletettu työaika määräytyy vuorokalenteriin suunnitellun vuoron mukaisesti.
