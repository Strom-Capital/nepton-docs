---
id: 360002558097
title: Tuntityön asetusryhmä
url: https://support.nepton.com/hc/fi/articles/360002558097-Tuntity%C3%B6n-asetusryhm%C3%A4
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Esimerkkejä asetusryhmien perustamiseksi
section_id: 360001483898
section_path:
- Työajan laskenta ja hallinta
- Asetusryhmät
- Esimerkkejä asetusryhmien perustamiseksi
labels:
- tuntityöntekijä
- nollatunti
- tuntipalkka
- nolla
- työaikamuutokset
- töihin kutsuttava
- tuntityö
- tuntityöläinen
promoted: false
updated_at: '2024-09-11T09:47:39Z'
edited_at: '2024-08-12T10:06:30Z'
---

# Tuntityön asetusryhmä

Kuten muillekin työaikamuodoille, myös tuntityötä tekeville työntekijöille on suositeltavaa perustaa oma työajan [asetusryhmänsä](<https://support.nepton.com/hc/fi/articles/360002558498>).
Tässä ohjeessa on käyty läpi tuntityö-työaikamuotoa noudattavan asetusryhmän kannalta oleelliset asetukset. Ohjeessa on käytetty esimerkkinä tilannetta, jossa tavoitteena on ainoastaan seurata tuntipalkkaisten työntekijöiden toteutunutta työaikaa. Työntekijälle korvataan siis kaikki tehty työ tunti tunnista palkkaan.
Ylityö- ja saldolaskenta on kuitenkin tarvittaessa mahdollista toteuttaa myös tuntipalkkaisten kohdalla.
## Työpäivän pituuden määrittäminen
Vaikka tuntityötä tekevillä työntekijöillä seurattaisiinkin vain toteutunutta työaikaa, tulee työpäivän pituus (keskimääräinen vuorokautinen työvelvoite) määrittää asetusryhmän asetuksissa jokaiselle arkipäivälle maanantai-perjantai. Määritys löytyy kohdasta **Työaika > Hallinta > Asetusryhmät > Valitse haluttu asetusryhmä > Toiminto: Asetusryhmän asetukset >Työtunnit ****> Työpäivän pituus.**
Työpäivän pituus on tässä esimerkissä 7h 30min.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4409532357009)
## Työviikon pituuden määrittäminen
Samaan tapaan kuin työpäivän pituus, tulee myös työviikon pituus määrittää asetusryhmän asetuksissa **TES** -osion kohdassa **Työviikon pituus työehtosopimuksessa ja TES enimmäistyöaika viikossa**. Työviikon pituus tässä esimerkissä 37h 30min (7h 30min * 5pv).
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360004707538)  
![mceclip2.png](https://support.nepton.com/hc/article_attachments/360004642777)
## Työajan laskennan määritykset
Koska esimerkissä lasketaan vain toteutuneita työtunteja, eikä saldo- tai ylityölaskentaa ole käytössä, tulee määritykset tehdä myös kohtaan **Asetusryhmän asetukset > Työtunnit > Kertymät ja ylityötunnit** alla olevan kuvan mukaisesti.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4789547554333)
Kertymät ja ylityötunnit -osion "laskennan asetukset" alaotsikon alta valitaan Ylityö. Täältä määritellään, että kaikki tunnit tehdään oletuksena tunti tunnista palkkaan:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4406427664145)
Kaikki muut ylityön kohdenteet otetaan pois käytöstä kohdassa "Näkyvissä olevat ylityöasetukset tapahtuman luonnissa", jotta muuta ylityön ohjausta ei ole kyseisessä ryhmässä mahdollista tehdä.
Jos saldoa tai muita kertymiä halutaan seurata, voidaan ne määrittää samassa valikossa halutulla tavalla. Tässä esimerkissä käytössä on saldo- ja vuosivapaalaskenta.
![Kertym_t_ja_ylity_laskenta_01.png](https://support.nepton.com/hc/article_attachments/4796100540957)
Henkilön (työpäivän pituus) jälkeen tehdyt tunnit kohdistuvat automaattisesti saldoon ja ne voidaan kohdistaa manuaalisesti ylityönä palkkaan. Huom: Jos saldolaskenta on käytössä tuntityöläisen asetusryhmässä, saa henkilö myös miinussaldoja mikäli hän tekee työvelvoitettaan lyhyemmän päivän.
