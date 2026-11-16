---
id: 40185048819485
title: Microsoft-kirjautuminen V2
url: https://support.nepton.com/hc/fi/articles/40185048819485-Microsoft-kirjautuminen-V2
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Microsoft-kirjautuminen
section_id: 360002832097
section_path:
- Kirjautuminen
- Kertakirjautuminen (SSO)
- Microsoft-kirjautuminen
labels: []
promoted: false
updated_at: '2026-11-09T09:20:21Z'
edited_at: '2026-11-09T09:05:10Z'
---

# Microsoft-kirjautuminen V2

Neptonin Microsoft-kirjautuminen (kertakirjautuminen) siirtyy käyttämään ensisijaisena tunnistautumismenetelmänä OpenID Connect (OIDC) v2.0 -päätepistettä, joka korvaa aiemmin käytetyn Microsoft Graph API -integraation.
  
Muutos otetaan käyttöön vaiheittain ja asiakkaita siirretään OpenID Connect -toteutukseen hallitusti. Muutos ei vaikuta loppukäyttäjän kirjautumiskokemukseen, vaan kirjautuminen toimii käyttäjän näkökulmasta samalla tavalla kuin aiemminkin.
#### Tunnistautumisen kulku
  * Ensisijainen: OIDC v2.0 -päätepiste — käytetään kaikissa kirjautumisissa
  * Varamentelmä: Microsoft Graph API — käytetään automaattisesti vain silloin, kun Microsoftin palauttama `id_token` ei sisällä käyttäjän sähköpostiosoitetta.


### Muutoksen syy
Muutoksella vastataan Microsoftin tekemiin Conditional Access -käytäntöjen muutoksiin:
  * **Ennen kesäkuuta 2026:** Pyynnöt osoitteeseen `https://graph.microsoft.com/v1.0/me` käyttäen `User.Read` -käyttöoikeusaluetta pystyivät ohittamaan Conditional Access -käytännöt, kun tenant-tason poissulkemiset oli määritetty.
  * **Kesäkuun 2026 jälkeen:** Microsoftin odotetaan arvioivan kaikki pyynnöt Conditional Access -käytäntöjen perusteella, mukaan lukien käyttäjän perustietojen hakemiseen liittyvät pyynnöt. Tenant-tason poissulut eivät enää samalla tavalla mahdollista poikkeusta. 
  * Tämän muutoksen yhteydessä myös Microsoft-kirjautuminen päivitetään käyttämään Microsoftin v2.0-päätepistettä.


### Edellytykset sähköpostiosoitteen `email`-claimin sisällyttämiselle ID-tokeniin
Jotta käyttäjän sähköpostiosoite sisältyy ID-tokeniin, kahden ehdon tulee täyttyä:
  1. Käyttäjän **mail-attribuutin** tulee olla määritelty.
  2. Sähköpostiosoitteen verkkotunnuksen tulee olla **vahvistettu (Verified)** kyseisessä tenantissa.


#### 1\. Käyttäjän `mail`-attribuutin määrittäminen
  * **Älä käytä** Entra-portaalin "Contact info → Email" -kenttää; se tallentaa arvon `otherMails`-attribuutiin, jota ei huomioida tokenin claimeissa.
  * **Suositus:** Määritä **Exchange Online / Microsoft 365 -lisenssi**. Tämä täyttää `mail`-attribuutin automaattisesti.
  * **Manuaalinen vaihtoehto:** Käytä Microsoft Graph PowerShelliä:
  * 
[code]Update-MgUser -UserId  -Mail "jane.doe@contoso.com"
[/code]
  * > **Huomio:** Jos Exchange-lisenssi määritetään myöhemmin, se saattaa korvata tämän manuaalisesti asetetun arvon.


#### 2\. Sähköpostiosoitteen verkkotunnuksen vahvistaminen
  * Siirry kohtaan **Entra-hallintakeskus (Entra admin center) → Identiteetti (Identity) → Mukautetut verkkotunnukset (Custom domain names)**.
  * Varmista, että käyttäjän `mail`-attribuutissa käytetty verkkotunnus (esim. `contoso.com`) on vahvistettu (**verified)**.
  * **Miksi:** Microsoft voi jättää `email`-claimin pois ID-tokenista monitilaajaympäristöissä (multi-tenant), jos sähköpostiosoitteen verkkotunnusta ei ole vahvistettu. Tällä ehkäistään tietoturvariskejä.


### Tilityypin asettaminen
Nepton-sovelluksen tilityypin (account type) Microsoft Entrassa on vastattava Neptonin Hallinta-osiossa olevaa asetusta:
  * Avaa Microsoft Entrassa Nepton-sovellusrekisteröinti (App registration) ja tarkista tuetut tilityypit (Supported account types) ("Choose the account types that can use this application or access this API").
  * Siirry Neptonissa kohtaan **Työsuhde → Hallinta → Kertakirjautuminen (SSO)**. **Azure AD -tilityyppi** -valinta näkyy vain, kun V2-hybridikirjautuminen on aktivoitu käyttöön.
  * Valitse Neptonissa sama tilityyppi (account type), joka on määritelty Microsoft Entra ID:ssä.

Entran sovellusrekisteröinti | Neptonin hallinta-asetus  
---|---  
Accounts in this organizational directory only | Vain yksi tenantti  
Accounts in any organizational directory | Useammat Entra ID-tenantit  
Accounts in any organizational directory + personal Microsoft accounts | Kaikki Entra ID-tenantit + henkilökohtaiset Microsoft-tilit  
Personal Microsoft accounts only | Vain henkilökohtaiset tilit  
![](https://support.nepton.com/hc/article_attachments/40378848764317) | ![](https://support.nepton.com/hc/article_attachments/40378848765341)  
---|---  
> **Huomio:** V1-kirjautumisessa tilityyppi on kiinteä eikä valintaa näytetä. Asetus koskee vain V2-kirjautumista.
