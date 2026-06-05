---
id: 360003994357
title: Aika, kieli ja alue
url: https://support.nepton.com/hc/fi/articles/360003994357-Aika-kieli-ja-alue
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- aikaero
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2024-11-13T06:53:27Z'
---

# Aika, kieli ja alue

Palvelussa voidaan määrittää henkilölle, asetusryhmälle tai työyhteisölle oletuskäyttökieli ja aikavyöhyke. Asettamalla aikavyöhykkeen palvelun **reaaliaikaisia** työn aloitus- ja lopetustoimintoja voidaan käyttää myös niissä organisaatioissa, joissa työtä tehdään eri aikavyöhykkeillä. Nepton ei muuta kalenterissa näkyvää aikaa katsojan aikavyöhykkeen mukaan, eli eri aikavyöhykkeeltä katsottuna kalenterissa näkyvä aika on sama kuin kirjaajan aikavyöhykkeen aika. Aikavyöhykkeen voi määrittää vain organisaation ylläpitäjä.
Jos henkilö kirjaa työaikaa paikallista aikaa ilman reaaliaikatoimintoja (Mobiilin pika-aloitus, Työaikapääte tai Nykyaika toiminnallisuus) eri aikavyöhykkeeltä, tällöin ei ole väliä vaikka hänen aikavyöhykkeensä on Suomen ajassa. Mutta jos henkilö kirjaa työaikaa reaaliaikatoiminnoilla (Mobiilin pika-aloitus, Työaikapääte tai Nykyaika toiminnallisuus) ilman, että aikavyöhykettä ei ole muutettu henkilön asetuksissa, tällöin kalenteriin muodostuu työaika Suomen ajassa. Neptonin kellon on siis Suomen ajassa, jos aikavyöhykettä ei ole muutettu. Jos henkilön asetuksissa määritetään aikavyöhyke työskentelymaan mukaan, tällöin reaaliaikainen työajan kirjaaminen näkyy työaikakalenterissa paikallisessa ajassa.
## Asetukset
Käytettävän kielen ja aikavyöhykkeen voi määritellä henkilön asetuksissa **Työaika > Hallinta > Henkilöt**, asetusryhmän asetuksissa **Työaika > Hallinta > Asetusryhmät > Asetusryhmän asetukset > Aika, kieli ja alue** tai työyhteisö-tason asetuksissa **Työaika > Hallinta > Työyhteisön asetukset.**
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360004875277)
## Oletukset
Oletuksena palvelussa kielenä on suomi ja aikavyöhykkeenä Suomen aikavyöhyke.
## Aikavyöhykkeet ja tapahtumien luonti päätteellä
  * Jos kirjataan tapahtuma käyttäen kirjauspäätettä, kirjautuu tapahtuman alku- ja loppuajat Neptoniin kirjauspäätteeseen asetetun aikavyöhykkeen ja kellonajan perusteella. Jos työntekijä matkustaa hetkellisesti eri aikavyöhykkeelle, hän voi kirjata työtapahtumansa paikallisen ajan mukaan.
  * Jos kirjataan tapahtuma Nykytilan tai Mobiilin kautta, kirjautuu tapahtuman alku- ja loppuajat Neptonin työyhteisö/asetusryhmätasolle määriteltyjen asetusten mukaan. Tämä varmistaa työaikakirjausten oikeellisuuden. Tästä syystä henkilön aikavyöhyke suositellaan asettamaan Neptonissa oikeaksi aina senhetkisen sijainnin mukaan.


Huom: Jos aikavyöhyke muutetaan takautuvasti, muutoksella ei ole vaikutusta jo kirjattuihin tapahtumiin.
## Rajoitukset 
Yhden päivän aikana voimassa voi olla vain yksi aikavyöhyke päivässä.
API: Jos lähetät aikoja UTC-muodossa nollapoikkeamalla ne muutetaan paikallisiksi ajoiksi aikavyöhyke-asetuksen perusteella (2019-12-25T10:11:12Z).
Kun [henkilöitä tuodaan](<https://support.nepton.com/hc/fi/articles/360003762577>) ilman käyttökieltä, työyhteisön asetuksissa asetettu kieli ei vaikuta henkilön palvelun käyttökieleen. Jos henkilöitä tuodaan ilman käyttökieltä, käytetään asiakkuuden oletuskieltä, joka on oletuksena suomi. Oletuskielen muuttamista voidaan pyytää Neptonin asiakaspalvelusta.
