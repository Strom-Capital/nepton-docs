---
id: 360004855857
title: Henkilötietojen API yleisesti
url: https://support.nepton.com/hc/fi/articles/360004855857-Henkil%C3%B6tietojen-API-yleisesti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötietojen API
section_id: 4406143245713
section_path:
- Liittymät
- Sovellusliittymät (API)
- Henkilötietojen API
labels:
- henkilötietoliittymä
promoted: false
updated_at: '2025-02-27T07:05:34Z'
edited_at: '2025-02-27T06:55:21Z'
---

# Henkilötietojen API yleisesti

## Tuotantoliittymäkuvaus
<https://go.nepton.com/API/SOAPWebService.asmx>
Varmistathan myös tarpeellisten IP-osoitteiden avaukset. Ohje [täältä](<https://support.nepton.com/hc/fi/articles/360009237257>).
Henkilötietojen sovellusliittymät tarjoavat ulkoisille järjestelmille pääsyn tiettyihin Neptonin ominaisuuksiin ja tietoihin. Liittymän WSDL-kuvaus löytyy osoitteesta <https://go.nepton.com/API/SOAPWebService.asmx?wsdl>.
Pyyntö on välitettävä SOAP-pyyntönä POST-metodia käyttäen. HTTP-otsikko "Content-Type" tulee olla arvolla "text/xml; charset=utf-8".
Seuraavissa artikkeleissa on aihekohtaiset ohjeet:
  * [Tunnistautuminen henkilötietojen sovellusliittymiin](<https://support.nepton.com/hc/articles/4406441875089>)
  * [Henkilötietojen sovellusliittymien vastausviestit ja -koodit](<https://support.nepton.com/hc/articles/4406446686609>)
  * [Henkilötietojen sovellusliittymä](<https://support.nepton.com/hc/articles/4406271660945>)
  * [Yksiköiden sovellusliittymä](<https://support.nepton.com/hc/articles/4406271664273>)


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
Jos XML:ssä halutaan esimerkiksi esittää salasana "_HpR9cHN &f8C<_", se pitäisi tehdä seuraavasti:
[code] 
    <UserPassword>HpR9cHN&amp;f8C&lt;</UserPassword>
[/code]
