---
id: 360004861558
title: Työajan API yleisesti
url: https://support.nepton.com/hc/fi/articles/360004861558-Ty%C3%B6ajan-API-yleisesti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Työajan API
section_id: 360005706218
section_path:
- Liittymät
- Sovellusliittymät (API)
- Työajan API
labels: []
promoted: false
updated_at: '2025-02-27T06:58:51Z'
edited_at: '2025-02-27T06:56:21Z'
---

# Työajan API yleisesti

## Tuotanto-API:n kuvaus
<https://time.nepton.com/WebService.php?WSDL>
Varmistathan myös tarpeellisten IP-osoitteiden avaukset. Ohje [täältä](<https://support.nepton.com/hc/fi/articles/360009237257>).
API:in tehtävän POST-pyynnön datan suurin sallittu koko on 128 Mt. 
Työajan API tarjoaa ulkoisista järjestelmistä pääsyn tiettyihin työajan toimintoihin. Ohjeita yksittäisistä aiheista on saatavilla seuraavissa artikkeleissa:
  * [Autentikointi työajan API:ssa](<https://support.nepton.com/hc/articles/360019983978>)
  * [Tapahtumien API](<https://support.nepton.com/hc/articles/360019840217>)
  * [Projektien API](<https://support.nepton.com/hc/articles/360019840237>)
  * [Kertymien API](<https://support.nepton.com/hc/articles/360019984338>)
  * [Työajan liittymien API](<https://support.nepton.com/hc/articles/360019840857>)
  * [Päätepalveluiden API](<https://support.nepton.com/hc/articles/360019841037>)
  * [Työajan API:n palautekoodit](<https://support.nepton.com/hc/articles/360019841477>)


Huomioithan, että:
  * Lähetettävän XML:n pitää olla kelvollista (valid XML)
  * Merkistökoodauksen tulee olla UTF-8
  * Parametrien kirjainkoolla on merkitystä. Varmista siis, että kutsussa kaikki isot ja pienet kirjaimet ovat täsmälleen samalla tavalla kuin ohjeessamme.


Paras tapa varmistaa XML:n oikeellisuus on käyttää SOAP-kirjastoja pyyntöjen ja vastauksien käsittelyyn. Esimerkiksi PHP:n [SoapClient](<https://www.php.net/manual/en/class.soapclient>) tai .NET:in [WCF Web Service Reference](<https://learn.microsoft.com/en-us/dotnet/core/additional-tools/wcf-web-service-reference-guide>) toimivat.
Jos XML generoidaan käyttämättä siihen mitään XML-kirjastoa, tulee pitää mielessä että seuraavat merkit tulee esittää niiden entityinä.
Merkki | Entity  
---|---  
`&` | `&amp;`  
`<` | `&lt;`  
`>` | `&gt;`  
Jos XML:ssä halutaan esimerkiksi esittää projektin nimi "Projekti & muu työ", se pitäisi tehdä seuraavasti:
[code] 
    <Name>Projekti &amp; muu työ</Name>
[/code]
