---
id: 360003461977
title: Kirjauspäätteen käyttöönotto (ennen syyskuuta 2022)
url: https://support.nepton.com/hc/fi/articles/360003461977-Kirjausp%C3%A4%C3%A4tteen-k%C3%A4ytt%C3%B6%C3%B6notto-ennen-syyskuuta-2022
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Uuden kirjauspäätteen asennus
section_id: 360002103958
section_path:
- Kirjauspäätteet
- Uuden kirjauspäätteen asennus
labels:
- Deploy
- Quick start
- seinäpääte
promoted: false
updated_at: '2022-10-07T08:44:06Z'
edited_at: '2022-10-07T08:43:58Z'
---

# Kirjauspäätteen käyttöönotto (ennen syyskuuta 2022)

The following instructions are intended for hardware models delivered before September 2022.
For the latest instructions please see the dedicated article [here](<https://support.nepton.com/hc/en-gb/articles/6231723616925>)
Tällä sivulla on esitelty kirjauspäätteen käyttöönotto. Jos et ole vielä tilannut kirjauspäätettä, niin ota yhteys palveluntarjoajaasi.
Kun sinulla on kirjauspääte niin voit seurata seuraavia askeleita kirjauspäätteen käyttöönottoon. Mikäli et saa kirjauspäätettä käyttöön näillä ohjeilla tai tarvitset apua otathan yhteyttä palvelun toimittajaasi.
## Asennus ja aloittaminen
Ennen aloittamista varmista, että voit kirjautua siihen käyttöympäristöön, johon haluat lisätä laitteen, ja johon sinulla on pääkäyttäjätunnukset.
**1)** Poista laite pakkauksesta
  * Jos kirjauspääte on Idesco-mallinen, tulee laitteen takakansi poistaa ja reitittää kaapelit takakannessa olevan läpiviennin kautta. Katso Idesco-mallin seinäasennuksen lisätiedot [täältä](<https://support.nepton.com/hc/fi/articles/360003778457>).


**2)** Jos sinulle on RFID-lukija, yhdistä RFID-lukija laitteen USB-porttiin
**3)** Kytke Ethernet-kaapeli, josta on yhteys internetiin
**4)** Jos käytössäsi ei ole Power over Ethernetiä (PoE), kytke virtalähde laitteeseen. Jos et tiedä, tukeeko päätelaitemallisi PoE-tekniikkaa, voit tarkistaa sen päätelaitemallisi teknisistä tiedoista. Tällä hetkellä ainoastaan Idesco Touch -päätelaitteet tukevat PoE-virransyöttöä.
Power over Ethernet vaatii myös Ethernet-kaapelin toisen pään kytkemisen PoE-kytkimeen tai injektoriin. Muutoin päätelaite ei saa virtaa Ethernet-kaapelista, vaikka tukisi PoE-tekniikkaa.
**5)** Laite käynnistyy automaattisesti ja muodostaa yhteyden palvelimeen, kun virtalähte on kytketty laitteeseen. Laite tekee päivityksen uusimpaan sovellusversioon, kun yhteys palvelimeen on saatu. Päivityksen jälkeen sovellus käynnistyy automattisesti. 
  * On tavallista, että laite käynnistyy offline - tilassa ja muodostaa yhteyden palvelimeen tämän jälkeen. Kun laite päivittää sovellusta niin ruudulla näkyy päivityssovelluksen ikkunoita. Ne eivät vaadi käyttäjältä toimenpiteitä.
  * Jos laite on offline-tilassa yli 15 minuuttia tai siinä ilmenee muita ongelmia, tutustu usein kysyttyihin kysymyksiin tai ota yhteys verkon ylläpitäjään.


**6)** Kun sovellus on päivitetty ja käynnistetty, laite odottaa sen yhdistämisestä palvelun käyttöympäristöön. Kirjauspäätteen ruudulla näkyy kirjauspäätteen tunnus. Laita tunnus talteen.
**7)** Voit nyt liittää kirjauspäätteen käyttöympäristöön. Tehdäksesi tämän, kirjaudu palveluun ylläpitäjänä ja siirry kohtaan **Työsuhde - > Hallinta -> Kirjauspäätteet. **
  * Aseta kirjauspäätteen tunnus otsikon **Lisää - > Päätteen tunnus** alta ja paina Tallenna - painiketta.
  * Katso kirjauspäätteen lisäämisen ohje [täältä](<https://support.nepton.com/hc/fi/articles/360004790097>)
  * Jos kirjauspäätteen tunnuksen lisääminen ei onnistu, ota yhteyttä palvelun toimittajaasi


**8)** Jos käytössä on ulkoinen RFID-lukija, ole yhteydessä palvelun toimittajaasi RFID-koodin pituuden määrittämiseksi.
**9)** Kirjauspääte lataa nyt käyttöympäristönkohtaiset asetukset, jonka jälkeen se on valmiina kirjauksiin. Päätelaitteen sovellus voi käynnistyä uudelleen tämän vaiheen aikana.
**10)** Laite on nyt käyttövalmis ja sillä voidaan tehdä kirjauksia.
  * Kirjauspäätteen esittää ne kirjautumistavat, jotka on määritetty palvelun asetuksissa
  * Jotta kirjauksia voidaan tehdä, tulee henkilön tiedoissa olla asetettu jokin tunnistautumistapa, esimerkiksi PIN-koodi tai RFID-tunniste
