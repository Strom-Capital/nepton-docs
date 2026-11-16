---
id: 36673036993565
title: HRX ja Nepton liittymäopas
url: https://support.nepton.com/hc/fi/articles/36673036993565-HRX-ja-Nepton-liittym%C3%A4opas
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Järjestelmäkohtaiset henkilötietojen tuonnit
section_id: 7976634441629
section_path:
- Liittymät
- Henkilötiedot
- Järjestelmäkohtaiset henkilötietojen tuonnit
labels: []
promoted: false
updated_at: '2026-06-18T09:29:23Z'
edited_at: '2026-06-09T04:56:08Z'
---

# HRX ja Nepton liittymäopas

Tämä artikkeli kertoo HRX ja Nepton -liittymän määrittämisestä. Siinä kerrotaan HRX:ssä määritettävistä tiedoista ja niiden sijoittamisesta, jotta liittymä toimii saumattomasti Neptonin kanssa.
Kun HRX on käytössä, HRX on henkilötietojen master-järjestelmä. 
## HRX:stä tuotavat kentät
**Kenttä** | **Master-järjestelmä** | **Kuvaus**  
---|---|---  
Ulkoinen tunniste 1 |  **Pakollinen kenttä.** Luotu HRX:ään | Henkilön ensisijainen tunniste, jonka HRX toimittaa. Tämä on yhdistävä avain kahden järjestelmän välillä ja sen on oltava uniikki ja pysyvä.  
Etunimi |  **Pakollinen kenttä.** Luotu HRX:ään | Henkilön etunimi  
Sukunimi |  **Pakollinen kenttä.** Luotu HRX:ään | Henkilön sukunimi  
Sähköposti | Luotu HRX:ään | Henkilön sähköpostiosoite  
Yksikkö | Luotu ensin Neptoniin. Nepton toimittaa yksikköluettelon HRX:ään. |  HRX tukee useampaa tasoa organisaatiorakenteessaan, ja jokaisen asiakkaan tulee päättää, kuinka monta tasoa on käytössä. Kun organisaatiorakenne on sovittu, vastaavat yksiköt on luotava Neptoniin täsmälleen samoilla nimillä. HRX käyttää näitä nimiä henkilötuonnissa. Esimerkiksi jos organisaatiorakenne on  
  
Taso 1 > Taso 2 > Taso 3 > Taso 4  
Yksikköjen osalta: Jos asiakas valitsee Neptonin yksikkötasoksi Tason 2, vastaavat Tason 2 yksiköt on luotava Neptoniin etukäteen. Tämän jälkeen HRX lähettää synkronoinnin aikana jokaisesta henkilöstä Tason 2 arvon yksikkö-kentässä. Jos asiakas valitsee Nepton yksikkötasoksi Tason 3, vastaavat Tason 3 yksiköt on luotava Neptoniin etukäteen. Tämän jälkeen HRX lähettää synkronoinnin aikana jokaisesta personasta Tason 3 arvon yksikkö-kentässä.  
RFID  | Luotu HRX:ään | Päätelaitteen tunnistuksessa käytettävä RFID-tunnisteen arvo.  
Ensisijainen esimies | Luotu HRX:ään | Tällä hetkellä tuetaan vain ensisijaisen esimiehen päivittämistä **henkilönumerolla**. HRX toimittaa henkilönumeron tähän kenttään.  
Nepton HR-rooli | Roolit ovat Nepton sisäänrakennettuja. Nepton on toimittanut rooliluettelon HRX:ään. | Määritelty HRX:ään nimenomaan Neptonia varten. Tämä on määritelty HRX:n puolella eikä sitä normaalisti muuteta henkilötasolla.  
Nepton Työaika-rooli | Luotu Neptoniin. Nepton on toimittanut rooliluettelon HRX:ään. | Dynaaminen. HRX ylläpitää manuaalisesti muokattavaa listaa hyväksytyistä Työaika-rooleista, joka sitten asetetaan henkilöittäin.  
Sopimuksen alku | Luotu HRX:ään | Käytetään HRX:n kenttää "Konserniin tulopäivä" (ensimmäisen työsopimuksen alkupäivä)  
Sopimuksen loppu | Luotu HRX:ään | HRX lähettää uusimman työsopimuksen päättymispäivän (päivämäärien perusteella, ei sopimuksen luomisajan perusteella). Jos uusimmassa sopimuksessa ei ole päättymispäivää, HRX lähettää päivämäärän tyhjänä.  
Sopimuksen tyyppi | Luotu HRX:ään | Sopimuksen tyyppi  
Henkilöryhmän koodipolku hierarkiassa | Luotu HRX:ään | Henkilöryhmän koodipolku hierarkiassa - Hierarkia ylläpidetään HRX:ssä osana organisaation rakennetta ja tuodaan Neptoniin osana henkilötietoja.  
Henkilöryhmän nimipolku hierarkiassa | Luotu HRX:ään | Henkilöryhmän nimipolku hierarkiassa - Hierarkia ylläpidetään HRX:ssä osana organisaation rakennetta ja tuodaan Neptoniin osana henkilötietoja.  
Työaikaprosentti | Luotu HRX:ään | Henkilön sovittu työaika prosentteina. HRX lähettää tämän arvon Neptoniin.  
Työajan asetusryhmä | Luotu Neptoniin. Ryhmät luodaan myös HRX:ään manuaalisesti. | Neptonissa hallittu hierarkia. Ryhmät luodaan HRX:ään manuaalisesti. Nykyinen arvo määritetään HRX:ssä ja siirretään Neptoniin päivittäin. Huomioi, että tämä on päivittäinen synkronointi eikä reaaliaikainen tapahtuma, joten muutokset näkyvät Neptonissa vasta seuraavan päivittäisen synkronoinnin jälkeen.  
Aktiivinen  | Luotu HRX:ään | Onko henkilö tällä hetkellä aktiivinen HRX:ssä. Inaktiiviset henkilöt on deaktivoitava Neptonissa vastaavasti. Henkilöä ei poisteta, vaan hänelle merkitään vain inaktiivinen tila.  
> **Tärkeää:** Kaikkia yllä lueteltuja kenttiä ei synkronoida HRX:stä. Liittymään siirtyville asiakkaille nämä kentät tyhjennetään Neptonissa.
