---
id: 360002558417
title: Työpäivän pituuden määrittäminen
url: https://support.nepton.com/hc/fi/articles/360002558417-Ty%C3%B6p%C3%A4iv%C3%A4n-pituuden-m%C3%A4%C3%A4ritt%C3%A4minen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- NEPTONNEEDSREVIEW
- työtuntimäärä
- työajanraja
- oletustyöaika
- työaikamuutokset
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2026-03-11T11:12:50Z'
---

# Työpäivän pituuden määrittäminen

Työpäivän pituus voidaan määrittää **Työaika** -osiossa joko **Työyhteisö** \- tai **Asetusryhmät** -tason asetuksissa. Asetukset löytyvät **Työaika > Hallinta > Työyhteisön / Asetusryhmän asetukset > Työtunnit > Työpäivän pituus.**
![](https://support.nepton.com/hc/article_attachments/34549989208093)
## Työpäivän kiinteä pituus
Työpäivän pituus määritellään viikonpäivä kerrallaan. Jos päivälle ei haluta määritellä työpäivän pituutta (esimerkiksi tilanteissa, joissa henkilö ei koskaan tee lauantaisin töitä) ei ko. päivälle tehdä lainkaan määrittelyä. 
Työpäivän pituuden määrittäminen on suositeltavaa tehdä [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta (pieni kalenteripainike asetuksen perässä). Näin työpäivän pituudelle voidaan määrittää Voimassa alkaen ja voimassa saakka-asetukset. 
![](https://support.nepton.com/hc/article_attachments/34553156353181)  
Jos työpäivän pituutta ei ole vielä määritetty, se voidaan asettaa voimaan ilman alku- ja loppupäivämäärää tai halutusta päivämäärästä alkaen.  
  
![](https://support.nepton.com/hc/article_attachments/34553156355357)  
Jos halutaan muuttaa olemassa olevaa arvoa, vanha arvo tulee päättää asettamalla arvolle **Voimassa saakka** -päivämäärä. Uusi arvo lisätään valitsemalla **Lisää uusi asetusarvo**. Uusi arvo tulee automaattisesti voimaan edellisen arvon päättymistä seuraavasta päivästä alkaen. Näin muutokset eivät vaikuta menneeseen työajan laskentaan, vaan astuvat voimaan valittuna päivänä.
Mikäli työpäivän pituuteen halutaan asettaa poikkeus, esim. tavallista lyhyempi päivä aina uudenvuoden aattona, lisätään se asetusarvon poikkeuksena kyseisen päivän kohdalle. 
![](https://support.nepton.com/hc/article_attachments/34553133333917)
Tarkemmat ohjeet ja esimerkit [täällä](<https://support.nepton.com/hc/fi/articles/360002560677>).
Työpäivän pituudelle voidaan asettaa poikkeusasetus myös [massakirjauksella](<https://support.nepton.com/hc/fi/articles/360002560837>).
## Suunniteltu vuoro määrittämässä työpäivän pituutta 
Asetuksella **Suunnitellut tapahtumatyypit, jotka ohittavat työpäivän pituuden** voidaan määrittää , että suunniteltu vuoro määrittää työpäivän pituuden niinä päivinä, jolloin päivälle on suunniteltu vuoro. Tämä asetus on mahdollista määrittää Työyhteisö-tasolla valikosta **Työaika > Hallinta > Työyhteisön asetukset > Vuorot **tai Asetusryhmät-tasolla valikosta**Työaika > Hallinta > Asetusryhmät > Asetusryhmä: Haluttu asetusryhmä > Toiminto: Asetusryhmän asetukset > Vuorot.** Jos työpäivän pituuden halutaan tulevan suunnitellusta vuorosta, ei asetusryhmään ole tarvetta määrittää päivän pituutta.
## Päivän poikkeusasetus asettaa myös enimmäistyöajan pituuden
Asetuksella "Päivän poikkeusasetus asettaa myös enimmäistyöajan pituuden" voidaan määrittää, muuttuuko päivän TES enimmäistyöaika tilanteessa, jossa henkilön työpäivän pituuteen on tehty poikkeusasetus kalenterinäkymässä yhtä päivää koskien. Mikäli asetuksessa on "kyllä", muuttuu TES-enimmäistyöaika tehdyn poikkeuksen verran.
