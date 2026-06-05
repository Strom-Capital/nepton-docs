---
id: 360009872457
title: Microsoft-kirjautumisen määritys Entra ID palvelussa
url: https://support.nepton.com/hc/fi/articles/360009872457-Microsoft-kirjautumisen-m%C3%A4%C3%A4ritys-Entra-ID-palvelussa
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
updated_at: '2026-02-05T13:58:38Z'
edited_at: '2026-02-05T13:58:38Z'
---

# Microsoft-kirjautumisen määritys Entra ID palvelussa

Microsoft Azure Active Directory on nyt Microsoft Entra ID
Microsoft-kirjautuminen (Entra ID Single Sign-On) antaa työntekijöille pääsyn Nepton-palveluun organisaation vakiovaltuuksilla ja turvallisuuskäytännöillä. Tämä ohje kuvaa tarpeelliset määritysvaiheet Microsoft SSO:n käyttöönottamiseksi Azuressa. Tämä artikkeli on tarkoitettu organisaatiosi Microsoft Entra ID tai Microsoft 365 -järjestelmänvalvojille.
## Edellytykset
Organisaatiollasi on oltava aktiivinen Microsoft 365- tai Entra ID -tilaus. Organisaatiollasi on oltava vähintään yksi vapaa Entra ID-sovelluksen rekisteröintipaikka käytettävissä. Kaikki Microsoft 365 asiakkaat saivat vähintään 10 sovelluksen rekisteröintipaikkaa tilauksen alkaessa.
## Käyttäjän henkilöllisyys
Entra ID kenttää EMAIL käytetään käyttäjän tunnistamiseen. Tämän on vastattava käyttäjän palveluun tallennettua sähköpostiosoitetta.  
  
Palvelun on tiedettävä työntekijöidesi Entra ID EMAIL-kentän arvo. Ne siirretään tyypillisesti palveluun käyttäjien ajoitetun päivittäisen tuontimekanismin kautta. Keskustele tästä tarkemmin Nepton-projektipäällikkösi kanssa tarpeen mukaan.  
  
Työntekijän Entra ID-sähköposti voidaan tarkistaa manuaalisesti seuraavalla menetelmällä:
  * Azure-portaali
  * Microsoft Entra ID
  * Users, select employee
  * Sähköposti löytyy yhdestä näistä (käytä alla olevaa järjestystä):
    * Profile, contact info, email
    * Authentication methods, email
    * Profile, user principal name 


## Entra ID määritysvaiheet
1\. Kirjaudu Azure-portaaliin <https://portal.azure.com/#home>
2\. Microsoft Entra ID
3\. Manage, app registrations (NOT enterprise applications)
4\. Valitse välilehti + New Registration
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21082402420637)
5\. Register an application
6\. Täytä tarvittavat tiedot kuten alla:
  * **Name:** SSO for Nepton V2
  * **Supported account types:** Accounts in this organizational directory only
  * **Redirect URI Type:** Web
  * **Redirect URIs:**
    * <https://go.nepton.com/msal.aspx>
    * <https://entra.microsoft.com/TokenAuthorize>


Suosittelemme "Accounts in this organizational directory" vaihtoehdon käyttöä. Tällöin tunnistautumisyritykset muiden organisaatioiden (yritykset, oppilaitokset, yms) tunnistautumispalveluiden kautta estetään suoraan jo Microsoftin toimesta.
Huomaa että Redirect URIs -osoitteiden isojen ja pienten kirjainten pitää olla kirjoitettu tarkalleen kuten yllä.
Paina Register -nappia.
7\. Sinun pitäisi ohjautua juuri luomaasi yleisnäkymään SSO for Nepton V2.  
  
![https://p29.zdusercontent.com/attachment/2068555/8KYrNajz5709VgOcMY9ncX2zV?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..y39v61GMqukAMoubDQnnZw.s9pIzqxNg6pM7FlUzYtyKc0-LTPIlkc2IBKhfFE582rW9ndiHczGqLS448tmPWcq2mnDjPjKNiygPAph2mkh0JITwL74JDe0qXzCVmx8hCqo6NcP9-MJMqdqw4Gv_wjG4CWbwrVx6c6LMt5LVGN44hfeD_Hj7jfH9-RCJ_3a4S8j5T7GCWOjUSj9BIgI6sfrF1gTdHX8Ljb_uynp3sEP2kT6GKLNXXoqRnKiXqQ2oeY3fO92cuYTzf2ntscuKyQ6a3StFsYj8VN7E9LjofG0Nn4gBIDo80zge42aWLZRdIA.IrUI_QWCgUje1-r4W7NfBg](https://p29.zdusercontent.com/attachment/2068555/8KYrNajz5709VgOcMY9ncX2zV?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..y39v61GMqukAMoubDQnnZw.s9pIzqxNg6pM7FlUzYtyKc0-LTPIlkc2IBKhfFE582rW9ndiHczGqLS448tmPWcq2mnDjPjKNiygPAph2mkh0JITwL74JDe0qXzCVmx8hCqo6NcP9-MJMqdqw4Gv_wjG4CWbwrVx6c6LMt5LVGN44hfeD_Hj7jfH9-RCJ_3a4S8j5T7GCWOjUSj9BIgI6sfrF1gTdHX8Ljb_uynp3sEP2kT6GKLNXXoqRnKiXqQ2oeY3fO92cuYTzf2ntscuKyQ6a3StFsYj8VN7E9LjofG0Nn4gBIDo80zge42aWLZRdIA.IrUI_QWCgUje1-r4W7NfBg)
8\. Vasemmalla, Authentication, Front-channel logout URL
<https://go.nepton.com/logout.aspx>
Merkkikoko yllä olevassa URL:ssa on merkitsevä, kirjoita URL kokonaisuudessaan pienaakkosin.
9\. Vasemmalla, Authentication, advanced settings, implicit grant, enable Access tokens ja ID tokens. Näitä tarvitaan, kun palvelun tunnistautuminen kutsuu API-rajapintaa.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360011895678)
10\. Save
![](https://support.nepton.com/hc/article_attachments/33751728236829)
11\. Vasemmalla, Overview, kopioi **Application (client) ID** ja **Object ID** arvot notepadiin. Tarvitset ainakin toista näistä arvoista myöhemmässä vaiheessa.
12\. Luodaan client secret -arvo.
HUOMIO: Jokaisella client secret -arvolla on vanhenemispäivä. Katso yksityiskohdat alempaa. Sinun tulee ennen vanhenemispäivää aina luoda uusi client secret -arvo ja päivittää tämä Neptoniin. Tämä on edellytys Microsoft-kirjautumisen keskeytymättömälle käytölle Neptonissa.
Tähän vaiheeseen on kaksi eri vaihtoehtoa
**A) Luo client secret Powershellin avulla**
HUOMIO: Tämä vaihtoehto on toimiessaan kaikkein paras.
Älkää määrittäkö vanhenemispäivää yli 5 vuotta tulevaisuuteen. Tällä tavalla määritelty client secret -arvo voidaan luoda, mutta se ei todennäkäisesti kuitenkaan käyttöönotettaessa toimi, johtuen Entra ID bugista.
Mikäli ette saa kirjautumista toimimaan vaihtoehdolla A, tulee teidän tehdä määritykset vaihtoehdolla B. 
Tämä vaihtoehto mahdollistaa 5 vuotta voimassa olevien client secret -arvojen luomisen. Sinun pitää tehdä vaiheet 12, 13 ja 16 uudestaan aina kymmenen vuoden välein.
Sinun tulee tässä vaihtoehdossa tuntea Powershellin toiminta. Huomioithan että Powershellin 7 versio ei tue Entra ID yhteyksiä, joten käytä Powershellin 5.1 x86 versiota.
Mikäli et ole vielä asentanut tarvittavaa Powershell moduulia, niin tee tämä:
Install-Module AzureAD
Aja seuraavanlaiset komennot (lopetuspäivä ei voi olla yli 5 vuoden päässä)
Connect-AzureAD
$startDate = Get-Date
$endDate = $startDate.AddYears(5)
$value = New-AzureADApplicationPasswordCredential -ObjectId "REPLACE_WITH_OBJECTID_OF_APP_REGISTRATION" -StartDate $startDate -EndDate $endDate
$value
**B) Luo client secret Entra ID portaalissa**
Tämä vaihtoehto voidaan tehdä pelkällä selaimella. Haittapuolena on se, että client secret vanhenee kahden vuoden välein ja täten vaiheet 12, 13 ja 16 pitää tehdä uudestaan aina kahden vuoden välein.
Vasemmalla, Certificates & Secrets, create new client secret. Merkitse uusi client secret olemaan voimassa mahdollisimman pitkään, tai jos mahdollista olemaan ikinä vanhenematta. Lisää. Odota että näet oikealla ylhäällä tämän ilmoituksen:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21082402422045)
13\. Kopioi client secret **value -** arvo notepadiin. Varmista (vaihtoehto 12B) et vahingossa kopioinut client secret **ID** -arvoa. Tarvitset client secret **value** -arvoa myöhemmässä vaiheessa.
14\. Siirry **Microsoft Entra ID, Manage, Enterprise Applications, SSO for Nepton v2, Security, Permissions**
15\. Paina **Grant admin consent for YOUR TENANT** ja hyväksy popupin mukaiset ehdot
16\. [Microsoft-kirjautumisen määritys Neptonissa](<https://support.nepton.com/hc/fi/articles/360010602957>)
