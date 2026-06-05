---
id: 8042662966429
title: Henkilötietojen vienti REST API -palveluun
url: https://support.nepton.com/hc/fi/articles/8042662966429-Henkil%C3%B6tietojen-vienti-REST-API-palveluun
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötiedot
section_id: 360001070377
section_path:
- Liittymät
- Henkilötiedot
labels: []
promoted: false
updated_at: '2024-08-23T09:59:00Z'
edited_at: '2022-12-13T11:22:24Z'
---

# Henkilötietojen vienti REST API -palveluun

Tämä artikkeli kuvaa teknisiä tietoja, joita tarvitaan asennettaessa ulkoinen REST API -palvelu vastaanottamaan henkilötietoja Neptonista ajastetun henkilöviennin kautta. Tietoja ajastetun viennin asentamiseksi henkilövientiä varten, myös REST API -asetuksista, löydät [Henkilötietojen ajastettu vienti](<https://support.nepton.com/hc/fi/articles/360002489357>) -sivulta sekä tietomuotokohtaisilta [CSV](<https://support.nepton.com/hc/fi/articles/4405423095953>)\- ja [JSON](<https://support.nepton.com/hc/fi/articles/7982660700189>)-sivuilta.
# Pyyntöviesti
Tämä osio kuvaa ne HTTP-pyynnöt, joita Nepton-palvelu lähettää ottaessaan yhteyttä ulkoiseen REST API -palveluun viedäkseen henkilötietoja. Lähetettävän sisällön tietomuoto – valitun tietomuodon mukaan – on kuvattu sivuilla [Vie henkilöt - Oletusarvoinen CSV-tietomuoto](<https://support.nepton.com/hc/fi/articles/4405423095953>) ja [Vie henkilöt - JSON-tietomuoto](<https://support.nepton.com/hc/fi/articles/7982660700189>).
## Vastaanottavan palvelun osoite
Ajastettu henkilövienti käyttää [HTTP PUT -metodia](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT>) ottaessaan yhteyttä REST API -palveluun. Palvelun on tuettava [TLS](<https://developer.mozilla.org/en-US/docs/Glossary/TLS>)-protokollaa (osoite on määriteltävä https://-etuliitteellä).  
  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/8209850843293)
## Autentikaatiotyyppi
### Ei autentikointia
Jos "Ei autentikointia" on valittuna autentikaatiotyypiksi, tiedot lähetetään palveluun odottamatta mitään tunnistautumisvalintoja.
![mceclip7.png](https://support.nepton.com/hc/article_attachments/8211414543133)
### Perus-HTTP-autentikointi
Perus-HTTP-autentikointi lisää [Authorization-otsikon](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization>) arvolla "Basic", jonka jälkeen seuraavat välilyönti ja "username"- ja "password"-parametrien arvot kaksoispisteellä eroteltuina – muodossa username:password - [UTF-8-koodauksella](<https://fi.wikipedia.org/wiki/Unicode#UTF-8>) konvertoituna [Base64-merkkijonoksi](<https://en.wikipedia.org/wiki/Base64>).
![mceclip1.png](https://support.nepton.com/hc/article_attachments/8210284528029)  
Esimerkki:
[code] 
    Authorization: Basic c2FtcGxldXNlcm5hbWU6YW0jbWFhNmZtMjh2bWYmR2xo
[/code]
jossa c2FtcGxldXNlcm5hbWU6YW0jbWFhNmZtMjh2bWYmR2xo on _sampleusername:am#maa6fm28vm &Glh_ (username- ja password-parametrien arvot ajastetun tehtävän asetuksista yhdistettyinä kaksoispisteellä) muunnettuna Base64-merkkijonoksi.
### OAuth 2.0 (perus-HTTP-autentikointi)
OAuth 2.0 -tunnistautuminen ottaa ensin yhteyttä annettuun valtuutuspalveluun [HTTP POST -metodilla](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST>) käyttäen [Authorization-otsikkoa](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization>), joka on samankaltainen kuin Perus-HTTP-autentikoinnissa. Valtuutuspalvelimen on tuettava TLS-protokollaa (osoite on määriteltävä https://-etuliitteellä).
![mceclip4.png](https://support.nepton.com/hc/article_attachments/8210385299741)  
Onnistuneessa vastauksessa valtuutuspalvelimelta tulee olla sisältönä [JSON-objekti](<https://fi.wikipedia.org/wiki/JSON#Tuetut_tietomuodot>), jossa on ainakin _access_token_ -kenttä määriteltynä. Vastausviestin muoto (viestissä voi olla enemmän HTTP-otsikkorivejä):
[code] 
    HTTP/1.1 200 OK
    Content-Type: application/json;charset=utf-8
    Content-Length: 119
    
    {
    	"access_token": "secret_access_token_value",
    	"token_type": "token_type",
    	"expires_in": 999999,
    	"scope": "scope"
    }
[/code]
Kentän access_token arvo välitetään sitten annetulle REST API -palvelulle Authorization-otsikossa:
[code] 
    Authorization: Bearer _secret_access_token_value_
[/code]
jossa _secret_access_token_value_ on valtuutuspalvelimelta saadun vastauksen _access_token_ -kentän arvo.
### Tunnussanavaltuutus
Tunnussanavaltuutus lisää _apikey_ -parametrin arvon [Authorization-otsikkoon](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization>) TOKEN-etuliitteellä.
![mceclip5.png](https://support.nepton.com/hc/article_attachments/8210990240285)
Esimerkki Authorization-otsikosta:
[code] 
    Authorization: TOKEN _salainen_api-avain_
[/code]
jossa _salainen_api-avain_ on _apikey_ -parametrin arvo ajastetun tehtävän asetuksista.
## Turvallisuusprotokollat
Palvelun ja mahdollisen OAuth 2.0 -valtuutuspalvelun on tuettava [TLS-protokollaa](<https://developer.mozilla.org/en-US/docs/Glossary/TLS>) ja niiden osoitteet on määriteltävä https://-etuliitteellä. Tällä hetkellä tuemme TLS 1.2 ja TLS 1.1 -turvallisuusprotokollia.
## 100-Continue -toiminto
Ennen tietojen lähettämistä tehdään [HTTP PUT-metodilla](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT>) pyyntö [Expect-otsikolla](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expect>), jonka arvona on "100-continue" (jatka). Viestissä ovat mukana kaikki muut pyynnön otsikot, mutta viestissä ei ole mukana tietosisältöä:
[code] 
    Content-Length: 25959
    Expect: 100-continue
[/code]
Vastauksen odotetaan olevan [HTTP-vastaus 100](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100>) (continue – jatka) merkiksi onnistuneesta tunnistautumisesta ja muiden otsikkotietojen hyväksynnästä ennen kuin lähetetään varsinainen data:
[code] 
    HTTP/1.1 100 Continue
[/code]
Jos palvelin ei voi hyväksyä viestiä, se voi vastata [HTTP-vastauksella 417](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/417>) (expectation failed – odotuksiin ei voida vastata):
[code] 
    HTTP/1.1 417 Expectation Failed
[/code]
tai muulla sopivalla vastauksella, esim. [HTTP-vastauksella 401](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401>) (unauthorized – ei valtuutusta):
[code] 
    HTTP/1.1 401 Unauthorized
[/code]
## Sisällön tyyppi
Pyynnön sisällön tyyppi lähetetään [Content-Type-otsikon](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type>) arvona: lähetettävän sisällön [mediatyyppi](<https://developer.mozilla.org/en-US/docs/Glossary/MIME_type>) ("application/json" [JSON](<https://support.nepton.com/hc/fi/articles/7982660700189>)-muodolle, "text/csv" [CSV](<https://support.nepton.com/hc/fi/articles/4405423095953>)-muodolle), jota seuraa ";charset=" ja sisällön merkistökoodaus ("utf-8" [UTF-8](<https://fi.wikipedia.org/wiki/Unicode#UTF-8>)-merkistökoodaukselle (Unicode-merkistö) tai "iso-8859-1" [ISO-8859-1](<https://fi.wikipedia.org/wiki/ISO_8859-1>)-merkistökoodaukselle ("Latin 1" -merkistö)).
Esimerkkejä:
[code] 
    Content-Type: application/json;charset=utf-8
[/code]
[code] 
    Content-Type: text/csv;charset=iso-8859-1
[/code]
## Sisällön pituus
Viennissä siirrettävän henkilötietosisällön pituus tavuina lähetetään [Content-Length-otsikon](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Length>) arvona.
Esimerkki:
[code] 
    Content-Length: 3909
[/code]
# Vastausviesti
Tämä osio kuvaa ne HTTP-vastausviestien sisällöt, joita Nepton-palvelu odottaa vastauksena ulkoiselta REST API -palvelulta vietyään henkilötietoja.
## Vastausviestit JSON-tiedoston lähetykseen
### Siirto onnistui – raportit yksittäisistä henkilötiedoista
Nepton-palvelu odottaa [HTTP-vastausta onnistuneella tilakoodilla](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses>) (tilakoodi välillä 200–299, esim. tilakoodi 200: OK), jos ulkoinen palvelu otti siirretyn viestin onnistuneesti vastaan.
Vastauksen on oltava [JSON-objekti](<https://fi.wikipedia.org/wiki/JSON#Tuetut_tietomuodot>), ja objektin on sisällettävä vientiviestissä olleiden yksittäisten henkilöiden tietojen tilat. JSON-objektivastauksessa tulee olla seuraavat avainnimet:
  * "Status"-avain (tila). Sen arvona tulisi olla teksti: "Success" (onnistui). Tämä tarkoittaa, että vientiviesti saatiin käsiteltyä – yksittäisten henkilötietojen käsittelyssä on silti voinut olla ongelmia. Jos Status-kentän arvo on: "Error" (virhe) – tai mikä tahansa muu arvo kuin "Success" – palveluun raportoidaan, ettei mitään tietoa saatu käsiteltyä.
  * "StatusByEmployee"-avain (työntekijätiedon tila) JSON-objektien taulukkona. JSON-objekteja tulee olla kutakin yksittäistä henkilövientitiedostossa olevaa henkilöä kohden. Jokaisessa JSON-henkilöobjektissa tulee olla seuraavat avaimet:  

    * "EmployeeNeptonId" (työntekijän Nepton-tunniste) – pakollinen avain, jota vastaa [Nepton-tunnisteen](<https://support.nepton.com/hc/fi/articles/8017902121885>) sisältävä merkkijonoarvo, NeptonPersonGUID-kentän arvo henkilövientitiedostosta.
    * Jos yksittäisen henkilön tietojen käsittely onnistui, StatusByEmployee-objektissa pitäisi olla **yksi tai useampia seuraavista avaimista** , jotta yksittäisen henkilön tietojen viennin katsottaisiin onnistuneen. Näitä avaimia vastaavien arvojen tulisi olla JSON-objekteja, joilla on ainakin yksi avain. Arvojen tietomuotoa ei tällä hetkellä ole rajoitettu: 
      * Added (lisätty)
      * Modified (muokattu)
      * NoChanges (ei muutoksia)
      * RemovedInfo (poistetut tiedot)
    * Jos yksittäisen henkilön tietojen käsittelyssä tapahtui virhe tai siihen liittyi mitä tahansa varoituksia, yksi tai molemmat seuraavista avaimista pitää lisätä. Niiden arvot tallennetaan [palvelulokiin](<https://support.nepton.com/hc/fi/articles/360002575478>) varoitusviestinä, ja yksittäisen henkilön tietojen viennin katsotaan epäonnistuneen: 
      * FatalError (virheet, jotka estivät koko käsittelyn)
      * Warnings (varoitukset)
  * Sekä pääobjektissa että yksittäisissä StatusByEmployee-objekteissa voi olla muitakin avaimia. Niiden tietoja ei tällä hetkellä käsitellä, mutta _kaikki_ tiedot vastauksessa saattavat päätyä vastaavaan [palvelulokimerkintään](<https://support.nepton.com/hc/fi/articles/360002575478>).


Esimerkki (viestissä voi olla enemmän HTTP-otsikkorivejä):
[code] 
    HTTP/1.1 200 OK
    Content-Type: text/plain; charset=utf-8
    Content-Length: 905
    
    {
    	"Status": "Success",
    	"StatusByEmployee": [
    		{
    			"EmployeeNeptonId": "206894AF-E2E6-5F11-B988-DD9E52BD067A",
    			"Added": {
    				"Field1": "Success",
    				"Field2": "Success",
    				"Field3": "Success"
    			},
    			"Modified": {
    				"Field4": "Success"
    			},
    			"NoChanges": {
    				"Field5": "Success"
    			},
    			"RemovedInfo": {
    				"Field6": "Success"
    			},
    			"Mikä tahansa tieto": "Ylimääräisiä avaimia voi olla mukana – ne eivät vaikuta tuloksen tulkintaan"
    		},
    		{
    			"EmployeeNeptonId": "D9D6AA30-58A9-43E4-A66A-12193A71C25E",
    			"Modified": {
    				"Field1": "Success"
    			},
    		},
    		{
    			"EmployeeNeptonId": "2CA5D9DF-5B57-446A-879B-FC8F704FA0F7",
    			"FatalError": "Pakollinen kenttä puuttuu: XX-järjestelmä vaatii \"Henkilötunnus\"-kentän",
    		},
    		{
    			"EmployeeNeptonId": "FEE31CF4-B4BF-4DDF-ADAD-5ACB1B8CD130",
    			"Warnings": "Virheellinen arvo: \"Hallinnon lisätieto\" (\"1CC\")"
    		}
    	]
    }
[/code]
### Siirto epäonnistui
On suositeltavaa lähettää vastauksessa [onnistumisen HTTP-tilakoodi](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses>) (tilakoodi välillä 200–299), jos mitään siirtoon liittyvää virhettä ei tapahtunut. Tarkemmat yksityiskohdat voidaan ilmoittaa alla kuvatulla muodolla. Jos palvelimen on vain ilmoitettava, että vastaanotto epäonnistui tai palvelu ei voinut käsitellä tietoja lainkaan, se voi vaihtoehtoisesti lähettää virhevastauksen – [HTTP-asiakkaan virhevastauksen](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses>) (tilakoodi välillä 400–499), [HTTP-palvelimen virhevastauksen](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses>) (välillä 500–599) tai minkä tahansa muun virheeksi luokiteltavan vastauksen – ja se lisätään [palvelulokin](<https://support.nepton.com/hc/fi/articles/360002575478>) virheraporttiin.
Jos vastauksen sisältönä on JSON-objekti, jonka "Status"-avainta (tila) vastaavana arvona on "Error" (virhe) – tai mikä tahansa muu arvo kuin "Success" (onnistui) – tai jos "ErrorMessage"-avainta (virheilmoitus) vastaavana arvona on jokin viesti, koko viennin katsotaan epäonnistuneen. Mikä hyvänsä virheviesti "ErrorMessage"-avaimen arvona kirjataan [palvelulokin](<https://support.nepton.com/hc/fi/articles/360002575478>) virheilmoitukseen.
Esimerkki (viestissä voi olla enemmän HTTP-otsikkorivejä):
[code] 
    HTTP/1.1 200 OK
    Content-Type: application/json; charset=utf-8
    Content-Length: 74
    
    {
    	"Status": "Error",
    	"ErrorMessage": "Lokiin kirjattava virheilmoitus"
    }
[/code]
Virheitä ja varoituksia yksittäisten henkilöiden tiedoista henkilövientitiedostossa ei pidä raportoida yleisinä virheinä, vaan käyttäen "FatalError"- ja "Warnings"-avaimia "StatusByEmployee"-taulukon objekteissa, katso Siirto onnistui – raportit yksittäisistä henkilötiedoista.
## Vastausviestit CSV-tiedoston lähetykseen
### Siirto ja käsittely onnistui
Jos ulkoinen REST API -palvelu vastaanotti ja pystyi käsittelemään sisällön odotetulla tavalla, sen odotetaan vastaavan [onnistuneella HTTP-tilakoodilla](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses>) (tilakoodi välillä 200–299), esim. tilakoodilla 200: OK. Mitään muuta tietoa kuin onnistunut HTTP-tilakoodi ei vaadita onnistuneeksi vastaukseksi, kun sisältö lähetettiin CSV-muodossa. Jos viestin sisältönä on tietoa, se kirjataan tietona [palvelulokiin](<https://support.nepton.com/hc/fi/articles/360002575478>) onnistuneen suorituksen merkintään.
Esimerkki (viestissä voi olla enemmän HTTP-otsikkorivejä):
[code] 
    HTTP/1.1 200 OK
    Content-Type: text/plain; charset=utf-8
    Content-Length: 2
    
    OK
[/code]
### Siirto tai käsittely epäonnistui
Jos ulkoiseen REST API -palveluun siirrossa tai tietojen käsittelyssä palvelussa oli ongelmia, palvelun odotetaan vastaavan epäonnistumista osoittavalla HTTP-tilakoodilla. Koodi voi [HTTP-asiakkaan virhevastaus](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses>) (tilakoodi välillä 400– 499), [HTTP-palvelimen virhevastaus](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses>) (välillä 500–599) tai mikä tahansa muu virheeksi luokiteltava vastaus. Vastauskoodi ja kaikki tiedot vastausviestin sisällössä tallennetaan [palvelulokiin](<https://support.nepton.com/hc/fi/articles/360002575478>) virheilmoituksena.
Esimerkki (viestissä voi olla enemmän HTTP-otsikkorivejä):
[code] 
    HTTP/1.1 500 Internal Server Error
    Content-Type: text/plain; charset=utf-8
    Content-Length: 41
    
    Odottamaton virhe tietojen käsittelyssä
[/code]
