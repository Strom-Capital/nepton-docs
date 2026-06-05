---
id: 5080867698717
title: Henkilötuonnin kentän tyhjentäminen NOLLA -avainsanalla
url: https://support.nepton.com/hc/fi/articles/5080867698717-Henkil%C3%B6tuonnin-kent%C3%A4n-tyhjent%C3%A4minen-NOLLA-avainsanalla
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötiedot
section_id: 360001070377
section_path:
- Liittymät
- Henkilötiedot
labels:
- Reset
- Nolla keyword
- Nolla
- Reset keyword
- tyhjä kenttä
- tyhjä arvo
promoted: false
updated_at: '2023-02-13T06:50:16Z'
edited_at: '2023-02-11T14:04:54Z'
---

# Henkilötuonnin kentän tyhjentäminen NOLLA -avainsanalla

Henkilötietokentän tyhjentäminen voidaan tehdä RESET- tai NOLLA-avainsanalla kentissä, joissa sitä tuetaan. Henkilötuonnissa on kaksi vaihtoehtoa käsitellä tyhjiä arvoja henkilötuonnissa: 1) **Turvallisin** (jos kentän arvo on tyhjä, älä muuta olemassa olevia arvoja) 2) **Tarkka** (jos kentän arvo on tyhjä, poista kentän olemassa oleva arvo). Kaikki henkilöiden tuontityypit ja tyhjät arvot -tila ja RESET/NOLLA -avainsanojen toiminta on kuvattu alla.
## Henkilötuontityypit ja tyhjän arvon tuonti
**Henkilötuontityypit** | **Tyhjän arvon tuonti  
**  
---|---  
Manuaalinen tuonti ([/wrm/admin/personimport.aspx](<https://go.nepton.com/wrm/admin/personimport.aspx>)) |  Jompikumpi seuraavista vaihtoehdoista voidaan valita avattavasta Tyhjät arvot tuontitiedostossa -valikosta.
  * Älä muuta olemassa olevia kenttäarvoja (**turvallisin**)
  * Poista nykyiset kenttäarvot (**tarkka**)

  
Henkilön tuonti (SFTP) - Ajastettu tehtävä | Tyhjän arvon tila on aina "Olemassaolevat kenttien arvot poistetaan (**tarkka**)"  
Henkilön tuonti (REST API) - Ajastettu tehtävä |  Tyhjän arvon tila on aina "Olemassaolevat kenttien arvot poistetaan (**tarkka**)"  
Henkilön tuonti - Soap Web Service menetelmällä**ImportUsersFromCSV** [/api/soapwebservice.asmx?wsdl](<https://go.nepton.com/api/soapwebservice.asmx?wsdl>) |  Tässä menetelmässä on parametri nimeltä ignoreEmptyValues, joka asettaa tyhjän arvon kentälle henkilötuonnissa. ignoreEmptyValues = **True** tarkoittaa "Olemassaolevia kenttien arvoja ei muuteta (**turvallisin**)" ignoreEmptyValues = **False** tarkoittaa "Olemassaolevat kenttien arvot poistetaan (**tarkka**)"  
Henkilön tuonti - Soap Web Service menetelmällä **ImportUsersFrom XML** [/api/soapwebservice.asmx?wsdl](<https://go.nepton.com/api/soapwebservice.asmx?wsdl>) |  Tässä menetelmässä on parametri nimeltä **ignoreEmptyValues** , joka asettaa tyhjän arvon kentälle henkilötuonnissa. ignoreEmptyValues = **True** tarkoittaa "Olemassaolevia kenttien arvoja ei muuteta (**turvallisin**)" ignoreEmptyValues = **False** tarkoittaa "Olemassaolevat kenttien arvot poistetaan (**tarkka**)"  
## Tietokentän tyhjentämisen kuvaus
**Tyhjä arvo  
** | **Kuvaus**  
---|---  
Olemassaolevia kenttien arvoja ei muuteta (**turvallisin**) **Huomio** : "Olemassaolevia kenttien arvoja ei muuteta (turvallisin)" tunnetaan järjestelmässämme myös nimellä ignoreEmptyValues | 
  * Jos kentän arvo on tyhjä merkkijono "", se ohitetaan, eli jätetään tuomatta  

  * Jos kentän arvoksi on asetettu NOLLA tai RESET, se tuodaan ja nykyisen kentän arvo tyhjennetään
  * Jos moniarvoinen kenttä sisältää avainsanan NOLLA tai RESET, kaikki sen arvot poistetaan, esim. yksiköt (henkilöllä voi olla useita yksiköitä)
  * Jos henkilön Salasana-kentässä on NOLLA tai RESET, luodaan satunnainen salasana, kun uusi henkilö lisätään

  
Olemassaolevat kenttien arvot poistetaan (**tarkka**) | 
  * Jos kentän arvo on tyhjä merkkijono "", se tuodaan jolloin nykyinen kentän arvo tyhjennetään
  * Jos kentän arvoksi on asetettu NOLLA tai RESET, se tuodaan ja nykyinen kentän arvo tyhjennetään
  * Jos moniarvoinen kenttä sisältää avainsanan NOLLA tai RESET, kaikki sen arvot poistetaan, esim. yksiköt (henkilöllä voi olla useita yksiköitä)
  * Jos henkilön Salasana-kentässä on NOLLA tai RESET, luodaan satunnainen salasana, kun uusi henkilö lisätään
