---
id: 4404282746641
title: Poissaolot henkilöittäin -raportti
url: https://support.nepton.com/hc/fi/articles/4404282746641-Poissaolot-henkil%C3%B6itt%C3%A4in-raportti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Työaikaraportit
section_id: 360005870318
section_path:
- Raportit
- Työaikaraportit
labels: []
promoted: false
updated_at: '2025-05-12T10:08:23Z'
edited_at: '2025-05-12T09:40:17Z'
---

# Poissaolot henkilöittäin -raportti

Poissaolot henkilöittäin -raportti näyttää poissaolot henkilöittäin ja poissaoloittain. Raportilla näkyy kaikki tapahtumatyypit, jotka käyttäytyvät kuten poissaolo (poissaolot, vuosilomat, kertymävapaat). Arkipyhiä ei näytetä.
Useampaan tapahtumaan jaetut poissaolot näytetään oletuksena yhdellä rivillä, jos ne on merkitty peräkkäin ja sisältävät samat perustiedot (poissaolotyyppi, sairauslomatyyppi, korvaustyyppi). Esimerkiksi perjantaille merkitty poissaolo 'Ase- tai siviilipalvelusaika' näytetään yhtenä rivinä maanantaille merkityn saman poissaolotyypin kanssa, koska kummatkin ovat 'Ase- tai siviilipalvelusaika' ja kummassakin on sama korvaustyyppi palkaton/palkallinen eikä näiden poissaolojen välissä ole työtapahtumia. Mikäli näiden poissaolojen väliin olisi merkattu toinen tapahtuma, näytettäisiin ne raportilla omina riveinään. Tämä on raportin oletusnäkymä. Raportti voidaan ladata myös tapahtumittain ilman ryhmittelyä.
## Raportin valinnat
Raportti voidaan ajaa joko tiedot ryhmiteltynä (oletus) tai ilman ryhmittelyä. Esimerkiksi kalenteriin on kahden viikon jaksolla merkattu sairauspoissaoloa kahtena eri tapahtumana, sekä yksi palkallinen poissaolo:  
![](https://support.nepton.com/hc/article_attachments/27304051279389)
**_Raportti ryhmiteltynä_ _:_** Sairauspoissaolo-merkinnät joista toinen on merkitty 2.6.- 6.6. ja toinen on merkitty 9.6.2022, ryhmitellään samalle riville yhtäjaksoiseksi poissaoloksi, koska ne ovat saman tyypin poissaoloja, eikä niiden välillä ole merkitty muita tapahtumia. Jos välissä olisi muita tapahtumia, molemmat merkinnät olisivat omilla riveillään, koska poissaolo ei ole tällöin yhtäjaksoinen.
Raportin kestossa näkyvät työtunnit ja työpäivät tulevat sen mukaan, kuinka paljon henkilöllä on ollut työvelvoitetta yhtäjaksoisen poissaolon aikana.
![](https://support.nepton.com/hc/article_attachments/27304064341149)
**_Raportti ilman ryhmittelyä_ _:_** Samalta aikajaksolta otettu raportti valinnalla "ei ryhmittelyä" näyttäisi tältä:
![](https://support.nepton.com/hc/article_attachments/27304064342813)
Erikseen merkatut sairauspoissaolot näytetään omilla riveillään, kuten ne on kirjattu henkilön kalenteriin. Raportilla näkyy sarake "Kesto (kalenteripäivät)" vain, kun se ajetaan ilman ryhmittelyä.
Raportin voi tulostaa tai ladata Exceliin.
## Saraketiedot
  * Henkilönumero – Henkilön henkilönumero (jos asetettu)
  * Työntekijä – Henkilön nimi
  * Henkilöryhmä – Henkilön henkilöryhmä (jos asetettu)
  * Raportin lisätieto – Henkilön tietoihin tallennettu Raporteilla näkyvä lisätieto -kentän sisältö (jos asetettu)
  * Poissaolon tyyppi – Poissaolon tyypin perustiedot. Arkaluontoiset tiedot, kuten poissaolon tyyppi, näkyvät vain henkilöille, joilla on riittävät oikeudet.
  * Korvaus – Palkallinen, palkaton, tai vähennetty palkka sen mukaan, mitä tapahtumaan on määritelty. Näkyy vain henkilöille, joilla on riittävät oikeudet.
  * Aikaväli - Ajanjakso peräkkäisistä poissaoloista, jotka täyttävät henkilön työvelvoitteen ja joilla on samat peruskriteerit.
  * Kesto (työtunnit) - Kuinka monta tuntia henkilön työvelvoitteesta poissaolo täyttää. Esimerkiksi jos henkilö kirjaa palkattoman poissaolon klo 00.00 -> 24.00, kesto tunteina on päivittäisen työvelvoitteen mukaan esim. 7h30min.
  * Kesto (työpäivät) – Kuinka monta työpäivää poissaolo kattaa henkilön työvelvoitteesta.
  * Kesto (kalenteripäivät) - Kuinka monta kalenteripäivää poissaolomerkintä kestää. Sisällytetään raportille vain jos "Ei ryhmittelyä" on valittu.
