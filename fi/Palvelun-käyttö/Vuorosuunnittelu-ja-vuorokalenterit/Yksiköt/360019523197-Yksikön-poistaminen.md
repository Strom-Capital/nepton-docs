---
id: 360019523197
title: Yksikön poistaminen
url: https://support.nepton.com/hc/fi/articles/360019523197-Yksik%C3%B6n-poistaminen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yksiköt
section_id: 360000708958
section_path:
- Vuorosuunnittelu ja vuorokalenterit
- Yksiköt
labels:
- unit
- yksikkö
- remove unit
- yksikön poistaminen
promoted: false
updated_at: '2025-06-18T07:34:25Z'
edited_at: '2025-06-18T07:32:51Z'
---

# Yksikön poistaminen

## Yleistä
Yksikköjä käytetään useassa yhteydessä Nepton-palvelussa ja yksikön poistamisella voi olla ei-toivottuja seurauksia. Tarkista kaikki tässä ohjeessa mainitut asiat ennen yksikön poistamista.
## Tarkista toimipisteet
Yksikköä ei pidä poistaa, jos sen alla on toimipisteitä, joita ei ole poistettu. Voit tarkistaa, onko yksiköllä toimipisteitä Toimipisteet-osiosta. Valitse "Vaihda Yksikköä" -välilehti, valitse yksikkö yksikön valinnassa ja valitse Jatka. Yksikön toimipisteiden pitäisi nyt näkyä näytöllä. Jos yksiköllä on toimipisteitä, jokaisen osalta pitäisi tarkistaa, onko toimipistettä vielä tarpeen käyttää. Toimipisteet näytetään hierarkiapuuna:
![mceclip2.png](https://support.nepton.com/hc/article_attachments/360019362777)
Jos aiot poistaa toimipisteen, sinun pitäisi varmistaa, ettei yhtäkään sen alaista toimipistettä tarvita. Toimipisteen alaiset toimipisteet voidaan siirtää toisen toimipisteen alaisiksi muuttamalla kategoriaa. Toimipisteitä voida kuitenkaan siirtää toiseen yksikköön, joten jos yhtäkään sen alaista toimipistettä tarvitaan, yksikköä ei voida poistaa.
### Yksiköt vuorosuunnittelussa
Jos työyhteisössäsi on käytössä [vuorosuunnittelu](<https://support.nepton.com/hc/fi/sections/360000934137>), toimipistettä voidaan tarvita suunnittelutasona henkilöiden ryhmittelyyn [toimipistekohtaisessa vuorosuunnittelussa](<https://support.nepton.com/hc/fi/articles/360015675918>). Voit tarkistaa, onko toimipisteen suunnittelutasolle liitetty henkilöitä kohdasta "Vuorosuunnittelu" > valitse "Vaihda yksikköä" > valitse yksikkö yksikön valinnassa > Jatka > valitse toimipiste toimipisteen valinnassa > Jatka > Toimipisteet > Suunnittelutason henkilöt. Jos "Suunnittelutason henkilöt" -otsikon alla on henkilöitä, tarkista, pitäisikö heidät siirtää toiseen (yksikköön ja) toimipisteeseen.
## Tarkista Työajan projektit
Jos yksikön alle on luotu toimipisteitä, Työaikaan on luotu automaattisesti projektit, joiden nimet ja koodit vastaavat yksikön ja toimipisteiden nimiä ja koodeja (toimipisteillä projektikoodi vastaa laskentayksiköitä). Näitä projekteja voidaan käyttää kuten muitakin projekteja työtapahtumien kohdistamiseen ja niille on voitu määritellä projektipäälliköitä - [katso lisätietoja projektihallinnasta](<https://support.nepton.com/hc/fi/sections/360000707398>). Kun toimipiste poistetaan, myös sitä vastaava projekti poistetaan eikä sitä voida enää käyttää työtapahtumien kohdistamiseen. Poistetulle projektille kohdistettua työtä ei myöskään voida hakea Työajasta projektiraporteille. Voit tarkistaa, onko projektille kohdistettu työtä käyttämällä eri raportteja Työaika > Projektit > Raportit -toiminnon alta.
## Tarkista yksikön henkilöt
Voit tarkistaa, onko yksikkö määritelty henkilöiden yksiköksi, kohdasta **Työsuhde > Yksiköt > valitse yksikkö > Yksikön henkilöt**. Ennen kuin poistat henkilöitä tästä näkymästä, tarkista, pitäisikö sinun lisätä henkilöt toiseen yksikköön. Ks. [Henkilöiden liittäminen yksikköön](<https://support.nepton.com/hc/fi/articles/360002595478>).
## Vapauta yksikön koodi tulevaa käyttöä varten
Suosittelemme vahvasti, että yksikön koodi muutetaan ennen yksikön poistamista. Voit käyttää muotoa, jota ei koskaan käytettäisi tavallisille yksikkökoodeille. Voit esimerkiksi käyttää POISTETTU_-etuliitettä, esim. POISTETTU_1000.
## Yksikön poistaminen
Kun olet ratkaissut kaikki mainitut esteet, jotka estäisivät yksikön poistamisen (ks. edelliset kohdat) ja nimettyäsi yksikön koodin uudelleen (ks. viimeisin kohta ennen tätä), voit poistaa yksikön kohdasta **Työsuhde > Yksiköt > valitse yksikkö > (tarkista, että olet valinnut oikean yksikön) > Lisätoiminteet > Poista**.
Yksikön poiston jälkeen näytetään viesti: "Yksikkö poistettu". Jos tässä vaiheessa huomaat painaneesi Poista-painiketta vahingossa tai olet jättänyt jonkin tarkistuksen tekemättä, voit painaa **Palauta** , jolloin yksikkö palautetaan käyttöön.
