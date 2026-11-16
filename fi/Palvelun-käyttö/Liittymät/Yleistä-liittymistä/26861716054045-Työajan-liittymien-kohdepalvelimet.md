---
id: 26861716054045
title: Työajan liittymien kohdepalvelimet
url: https://support.nepton.com/hc/fi/articles/26861716054045-Ty%C3%B6ajan-liittymien-kohdepalvelimet
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä liittymistä
section_id: 360002325398
section_path:
- Liittymät
- Yleistä liittymistä
labels: []
promoted: false
updated_at: '2026-08-14T11:43:40Z'
edited_at: '2026-08-14T11:43:40Z'
---

# Työajan liittymien kohdepalvelimet

Työajan liittymille asetetaan kohdepalvelin, jonne liittymässä luotu tiedosto siirretään ajastuksen mukaan tai josta haetaan tiedostoja esim. tapahtumien tuontia varten. Kun kohdepalvelimet on määritelty, useammassa liittymässä voi käyttää samaa kohdepalvelinta, jolloin palvelimen tiedot tarvitsee määrittää vain kertaalleen.
Kohdepalvelimia hallinnoidaan osiossa **Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Liittymien kohdepalvelimet**.
![](https://support.nepton.com/hc/article_attachments/30712421267101)
## Kohdepalvelimen asetukset
Uusi kohdepalvelin lisätään painamalla "Lisää liittymien kohdepalvelin", jolloin pääsee täyttämään kohdepalvelimen perustiedot:  
![](https://support.nepton.com/hc/article_attachments/30712452643997)
Kohdepalvelimelle annetaan nimi, halutessaan kuvaus, ja sen tyyppi valitaan alasvetolaatikosta. Tyyppinä voi olla joko SFTP (Vienti), SFTP (Tuonti) tai webservice. Tyyppi valitaan sen mukaan, minkätyyppiseen liittymään kohdepalvelinta käytetään. Kun nämä tiedot on lisätty ja painettu "Tallenna", ilmestyy tämä kohdepalvelin kohdepalvelimien valikkoon:  
![](https://support.nepton.com/hc/article_attachments/30712421268253)
Yllä olevassa kuvassa on lisätty uusi kohdepalvelin nimeltä "Poissaolot Mepcoon". Kohdepalvelimen tarkemmat tiedot päästään täyttämään, kun sen nimestä klikataan. Huom: Jokaiselle kansiorakenteelle pitää olla määriteltynä oma kohdepalvelin. Eli vaikka kaksi eri aineistoa viedään samalle SFTP-palvelimelle, jos kohdekansio on eri, tulee näille luoda omat kohdepalvelimet. Esimerkiksi jos käytössä olisi palkkaliiittymä ja poissaololiittymä, jotka viedään palvelimelle kansioihin FromNepton/Salaries ja FromNepton/Absences, tulisi Neptoniin määrittää kaksi kohdepalvelinta. 
![](https://support.nepton.com/hc/article_attachments/30712452645149)
Katso [SFTP tiedonsiirron määrityksistä](<https://support.nepton.com/hc/fi/articles/360003722778>) yleiset ohjeet liittyen palvelimen osoitteeseen, käyttäjätunnukseen, autentikointiin (public key tai salasana) sekä minkälainen polkurakenne palvelimella tulisi olla.
Mikäli kohdepalvelinta käytetään reaaliaikaiseen liittymään, tulee asetukseen "Ota reaaliaikainen synkronointi käyttöön (jos tuettu)" määrittää Kyllä.
Kun kohdepalvelimen tiedot on määritetty, voidaan se valita ajastetun viennin kohdepalvelimeksi kohdassa "Ajastus". Samaa kohdepalvelinta voidaan käyttää useassa liittymässä.
![](https://support.nepton.com/hc/article_attachments/30712663855133)
## Reaaliaikaisten liittymien viennin puskurointi
Puskuroinnilla vientitietojen siirto voidaan siirtää ajastettuun ajoon sen sijaan, että vienti tapahtuisi tapahtumien tallennuksen tai hyväksynnän yhteydessä.
Suurin hyöty puskuroinnissa on se, että kohdepalvelimen käyttökatkokset eivät johda tietojen siirtymättä jäämiseen. Epäonnistuneita siirtoja yritetään uudelleen niin pitkään kun ne ovat puskurissa.
Puskurin määrittäminen tapahtuu siten, että liittymien kohdepalvelimelle määritetään ajastus. Ajastuksen asetuksissa tulee valita:
  1. Liittymäksi "SFTP tiedostojen vienti"
  2. Liittymän kohdepalvelimeksi haluttu kohdepalvelin


![](https://support.nepton.com/hc/article_attachments/26862033866653)
Liittymien ajastuksesta voit lukea lisää artikkelista [Työajan vienti/tuonti liittymien ajastus](<https://support.nepton.com/hc/fi/articles/10510800700573>).
