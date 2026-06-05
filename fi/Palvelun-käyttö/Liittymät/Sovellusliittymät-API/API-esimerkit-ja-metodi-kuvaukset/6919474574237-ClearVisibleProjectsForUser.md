---
id: 6919474574237
title: ClearVisibleProjectsForUser
url: https://support.nepton.com/hc/fi/articles/6919474574237-ClearVisibleProjectsForUser
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: API esimerkit ja metodi-kuvaukset
section_id: 4410135708433
section_path:
- Liittymät
- Sovellusliittymät (API)
- API esimerkit ja metodi-kuvaukset
labels: []
promoted: false
updated_at: '2026-06-01T14:44:17Z'
edited_at: '2026-06-01T11:13:47Z'
---

# ClearVisibleProjectsForUser

Tästä metodista on uudempi versio. Mikäli käytät jo tätä metodia, niin suosittelemme että tarkastelet seuraavan version ohjeesta, mitä muutoksia vaaditaan uuden version käyttöönottamiseksi. Seuraavan version ohjeen löydät [täältä](<https://support.nepton.com/hc/fi/articles/36506225707677>).
## Rajapinnan yleiskuvaus
Verkkopalvelun avulla voidaan poistaa määritetyltä henkilöltä kaikki käyttäjätason projektinäkyvyydet. Tämä ei vaikuta millään tavalla henkilöryhmän kautta määritettyihin projekteihin.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla[ täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Käyttäjäviittaukset
Kohdekäyttäjä voidaan tunnistaa yksilöllisen Nepton tunnisteen, käyttäjän henkilönumeron tai käyttäjätunnuksen perusteella. Jokin näistä on annettava. Palvelu palauttaa virheen mikäli yhtään käyttäjätunnistetta ei ole määritetty tai tunnistetta vastaavaa käyttäjää ei löytynyt.
## Lähetettävät tiedot
TASO | KENTÄN NIMI | MUOTO | ESIINTYMISKERRAT | SELITE  
---|---|---|---|---  
0 | ParametersForClearVisibleProjectsForUser | XML element | 1 | Juurielementti,  
SOAP body:n alla  
1 | CallerAuthentication | XML element | 1 | Tunnistautumistiedot. Katso tarkemmat tiedot [täältä](<https://support.nepton.com/hc/fi/articles/360019983978>)  
1 | ClearVisibleProjectsForUserList | XML element | 1 |   
2 | ClearVisibleProjectForUser | XML element | 1..n |   
3 | UserId | integer | 0..1 | Kohdekäyttäjän Nepton tunniste.  
3 | PersonnelNumber | string | 0..1 | Kohdekäyttäjän henkilönumero.   
3 | UserName | string | 0..1 | kohdekäyttäjän käyttäjätunnus  
### Kyselyn esimerkki
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForClearVisibleProjectsForUser>
          <CallerAuthentication /> <!-- Autentikointi vaaditaan, mutta on jätetty pois tästä esimerkistä -->
          <ClearVisibleProjectsForUserList>
            <ClearVisibleProjectForUser>
              <PersonnelNumber>54236</PersonnelNumber>
            </ClearVisibleProjectForUser>
          </ClearVisibleProjectsForUserList>
        </tyo:ParametersForClearVisibleProjectsForUser>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
