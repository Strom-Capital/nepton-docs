---
id: 360017110497
title: Tapahtumien lisääminen - yleinen
url: https://support.nepton.com/hc/fi/articles/360017110497-Tapahtumien-lis%C3%A4%C3%A4minen-yleinen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtuman kirjaaminen
section_id: 360000934997
section_path:
- Tapahtumat
- Tapahtuman kirjaaminen
labels:
- tuntikirjaus
- työaikaleimaus
- leimausohje
- työaikakirjaus
promoted: false
updated_at: '2026-02-02T13:29:36Z'
edited_at: '2025-09-01T05:51:51Z'
---

# Tapahtumien lisääminen - yleinen

Tässä artikkelissa kerrotaan yleiset periaatteet tapahtumien kirjaamiseksi palveluun siten, että työajan tulkinta voidaan suorittaa yksiselitteisesti.
Kirjauksen kulku voidaan kuvata seuraavasti:  
1\. Aloitetaan työpäivä: Aloitetaan tapahtuma Työ.  
2\. Käydään lounaalla: Aloitetaan tapahtuma Ruokatauko.  
3\. Palataan töihin: Jatketaan ([mobiilin pika-aloitus](<https://support.nepton.com/hc/fi/articles/360002602638>)) tai aloitetaan (muut kirjaustavat) tapahtuma Työ.  
4\. Päätetään työpäivä: Valitaan Lopeta (mobiilin pika-aloitus tai kirjauspääte) tai päätetään käynnissä oleva tapahtuma syöttämällä tapahtumalle päättymisaika (kalenterinäkymä)
Eli päivän alussa leimataan Aloita ja päivän lopussa leimataan Lopeta. Kaikki muut leimaukset päivän aikana voidaan tehdä Aloita/Jatka-leimauksina ja palvelu päättää automaattisesti edellisen leimauksen kun uusi tapahtuma aloitetaan.
Tällä saadaan yhtäjaksoinen kirjausketju ja työajan tulkinta voidaan tehdä yksiselitteisesti. Jos kirjauksista ei muodostu yhtäjaksoinen ketju, esim. [automaattinen ruokatauko](<https://support.nepton.com/hc/fi/articles/360002558757>) ei mahdollisesti muodostu oikein.
Helpoin tapa tehdä leimaukset edellä kuvatulla tavalla on käyttää reaaliaikaisia leimauksia. Siihen palvelussa on useampi vaihtoehto: [mobiilileimaus](<https://support.nepton.com/hc/fi/articles/360002602638>), [työaikapääte](<https://support.nepton.com/hc/fi/articles/360002596797>) sekä [nykytila-näkymä](<https://support.nepton.com/hc/fi/articles/360002603258>). Myös [kalenteri-/taulukkonäkymässä](<https://support.nepton.com/hc/fi/articles/360002596797>) voidaan leimata reaaliaikaisesti.
Huom: Tapahtumia ei tule tallentaa pidemmälle kuin neljä vuotta tulevaisuuteen, tai reaaliaikaisten tapahtumien tai tapahtumapyyntöjen kirjaamisessa saattaa tulla virhetilanteita.
## Uuden tapahtuman aloitusajan logiikka
Tapahtumalle voidaan määrittää oletus Aloitus- ja Lopetusaika [Näytön asetuksista.](<https://support.nepton.com/hc/fi/articles/360008777997>) Lisätessä mille tahansa päivälle ensimmäistä tapahtumaa, joko mobiili-, kalenteri- tai taulukkonäkymässä, Nepton ehdottaa tapahtumalle näytön asetusten perusteella määritetyn oletus aloitus- ja lopetusajan. Jos oletus aloitus- ja loputusaikoja ei ole määritetty näytön asetuksissa, Nepton ehdottaa tapahtumalle oletuksena 0800-1600.
Jos nykyisellä päivällä on jo tapahtuma ja nykyiselle päivälle lisätään toinen tapahtuma, Nepton ehdottaa tapahtumalle oletuksena aloitusajaksi nykyajan.
Jos menneisyydessä tai tulevaisuudessa päivällä on jo tapahtuma ja päivälle lisätään toinen tapahtuma, Nepton ehdottaa tapahtumalle oletuksena aloitusajaksi edellisen tapahtuman lopetusajan.
![](https://support.nepton.com/hc/article_attachments/29995664744349)
