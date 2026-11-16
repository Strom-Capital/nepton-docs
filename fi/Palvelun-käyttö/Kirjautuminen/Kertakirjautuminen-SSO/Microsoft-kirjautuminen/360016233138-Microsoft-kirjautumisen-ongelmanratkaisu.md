---
id: 360016233138
title: Microsoft-kirjautumisen ongelmanratkaisu
url: https://support.nepton.com/hc/fi/articles/360016233138-Microsoft-kirjautumisen-ongelmanratkaisu
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Microsoft-kirjautuminen
section_id: 360002832097
section_path:
- Kirjautuminen
- Kertakirjautuminen (SSO)
- Microsoft-kirjautuminen
labels:
- ms login
promoted: false
updated_at: '2026-10-29T14:05:12Z'
edited_at: '2025-01-21T10:43:27Z'
---

# Microsoft-kirjautumisen ongelmanratkaisu

Microsoft Azure Active Directory on nyt Microsoft Entra ID
Tietyissä tilanteissa Microsoft-kirjautuminen ei toimi odotetusti. Ongelmatilanteita voi syntyä esimerkiksi seuraavissa tilanteissa:
  * Henkilön laitteeseen Microsoft Endpoint Managerin kautta jaetut apps asennukset aiheuttavat sekannuksen mikäli henkilö käyttää jotain muuta kuin laitteen vakioselainta.
  * Määritysvirhe henkilön tai organisaation Neptoniin tallennetuissa tiedoissa.
  * Määritysvirhe tai normaalia tiukemmat turvasäännöt organisaation Entra ID -palvelussa.
  * Käytettävän laitteen määritykset estävän Microsoft-kirjautumisen toiminnan.


Alla olevien toimenpiteiden avulla voidaan selvittää ja ratkaista ongelmat Microsoft-kirjautumisessa. Suorita toimenpiteet alla olevassa järjestyksessä.
## Tarkista Microsoft Endpoint Manageriin tallennetut määritykset
**Tämä koskee vain Microsoft Endpoint Manageria käyttäviä organisaatioita**
Mikäli henkilön laitteeseen on organisaatiossanne tehty Nepton app -tyyppinen asennus ja henkilö käyttää muuta kuin laitteen vakioselainta kirjautuakseen Neptoniin, voivat tietyt laitteet ja käyttöjärjestelmäversiot aina ohjata kirjautumisen laitteen vakioselaimeen. Tämä saattaa aiheuttaa tilanteen, jossa henkilön tulee kirjautua palveluun kaksi kertaa. Kyseessä ei ole Nepton-palvelun ominaisuus tai puute, vaan laitteen käyttöjärjestelmän ominaisuus. Ratkaisuna on ohjeistaa henkilö käyttämään Nepton-palvelua selaimen sijaan laitteeseen asennetun pikalinkin kautta.
## Tarkista Neptonin palvelukoki
[Palvelulokissa](<https://support.nepton.com/hc/fi/articles/360002575478>) esitetään epäonnistuneet kertakirjautumisyritykset. On mahdollista että epäonnistuneen kirjautumisen syy selviää palvelulokia tarkastelemalla. Epäonnistuneen kirjautumisen syy voi olla esimerkiksi että Neptonista ei löydy henkilöä sillä sähköpostiosoitteella jolla yritetään kirjautua tai useammalla henkilöllä on Neptonissa sama sähköpostiosoite. Kirjautuminen voi alkaa toimimaan korjaamalla palvelulokissa esitetty ongelma.
Palveluloki on nähtävissä palvelussa navigoimalla **Työsuhde - > Hallinta -> Palveluloki **ja tarkastele **SSO** osion palvelulokin huomioita.
## Tarkista Entra ID -loki
Entra ID kerää lokia kirjautumisyritysten tuloksista. Tarkista Entra ID -loki ja mikäli siellä on esitetty virheviesti niin se voi antaa selityksen ongelmaan. Kirjautuminen voi alkaa toimimaan korjaamalla Entra ID -palvelulokissa esitetty ongelma.
Entra ID -palvelulokin viestit voidaan nähdä seuraavalla tavalla
  * Kirjaudu ylläpitäjänä Azure-palveluun.
  * Siirry **Microsoft Entra ID, Monitoring, Signs-Ins** osioon.
  * Lisää **Status = Failure** suodatin.
  * Lisää **Application, SSO for Nepton v2** suodatin.
  * Tarkista virheviestien sisältö.


Mikäli virheviesti on tyyppiä AADSTS50011, niin lisää puuttuva "redirect URI" määritys [tämän artikkelin](<https://support.nepton.com/hc/fi/articles/360009872457>) kohdan 6 mukaisesti.
Entra ID kirjautumisen virhetulkinnasta voit lukea tarkemmin <https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-troubleshoot-sign-in-errors> artikkelista.
## Tarkista Entra ID Conditional Access -määritykset
Mikäli vain osassa päätelaitteita esiintyy kirjautumisongelmia tai sertifikaattihuomautuksia, tai jos Entra ID lokeissa näkyy INTERRUPTED merkintöjä, liittyy ongelma todennäköisesti Conditional Access määrityksiin. Huomaa että ongelma voi esiintyä vaikka ajaisit Conditional Accessia pelkästään "report only" tilassa. Aiheesta tarkemmin [https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only ](<https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only>)artikkelissa. Katso erityisesti keltaisen "WARNING" laatikon sisältö tässä artikkelissa.
Device State asetuksen voi tarkastaa seuraavalla tavalla.
  * Kirjaudu ylläpitäjänä Azure palveluun
  * Siirry **Microsoft Entra ID, Manage, Enterprise Applications, SSO for Nepton v2, Security, Conditional Access** osioon
  * Tarkista conditional access määritykset
  * Katso **Device State** asetus.


Jos **Device State** asetus on **ON** tai **REPORT ONLY** , niin vaihda asetus **OFF** tilaan testataksesi korjaako tämä kirjautumisongelman.
**Device state** asetuksen sijaan vastaavan suojauksen voi mahdollisesti toteuttaa myös yhdistelmänä **Assignments, Conditions, Client Apps** ja **Access Controls, Grants** -määrityksiä.
## Usean yhtäaikaisen Microsoft kirjautumisnapin ongelmatilanteet
Palveluun voidaan määrittää useita yhtäaikaisia Microsoft kirjautumisnappeja. Kukin nappi yhdistää asiakkaan erilliseen Entra ID tenanttiin. Mikäli tällaisessa monikirjautumisympäristössä esiintyy ongelmia, tarkista että kussakin Entra ID tenantissa on vain yksi Nepton appregistration. Mikäli useammassa Entra ID tenantissa on jostain syystä appregistrationeja samalla application ID tunnuksella, on tämä todennäköinen selitys ongelmiin. Tee tällöin kaikkiin tenantteihin uudet Nepton appregistrationit [Microsoft-kirjautumisen määritys Entra ID palvelussa](<https://support.nepton.com/hc/fi/articles/360009872457>) ohjeen mukaisesti, päivitä uudet arvot Neptoniin [Microsoft-kirjautumisen määritys Neptonissa](<https://support.nepton.com/hc/fi/articles/360010602957>) ohjeen mukaisesti, ja poista vanhat appregistrationit kaikista tenantista kokonaan.
## AADSTS7000215: Invalid client secret provided
**Tämä koskee tyypillisesti vain Powershellillä luotuja client secret arvoja**
Powershellillä luotu pidempiaikainen client secret ei aina toimi oikein. Ongelma ei koske kaikkia asiakkaita.
Tarvittaessa voit hylätä Powershellin kautta luodun client secret arvon ja luoda uuden lyhyempiaikaisen client secret arvon käsin Azure Portalin kautta. Tämä onnistuu tekemällä [Neptonin määritys Entra ID palvelussa](<https://support.nepton.com/hc/fi/articles/360009872457>) vaiheet 12B - 16. Muista päivittää uusi client secret arvo myös Neptoniin.
## Entra ID sovelluksen uudelleenluonti
Nepton palvelulokin ja Microsoftin Entra ID -lokin tarkastelusta on kuvaukset hiukan ylempänä. On mahdollista että Entra ID -loki näyttää onnistuneita kirjautumisia, mutta käyttäjät vain palautuvat Entra ID kirjautumisen jälkeen Neptonin etusivulle, ja Neptonin omissa lokeissa ei näy mitään merkintöjä. Tällöin asetuksissa on todennäköisesti virhe, joten on suositeltavaa poistaa aikaisemmin tehty app registration Entra ID:stä, poistaa aikaisemmin tehty Microsoft Login määritys Neptonista ja tehdä koko määritysprosessi alusta uudestaan.
## Microsoft tunnuksien pakotettu uloskirjautuminen
Mikäli henkilöllä on useampia Microsoft tunnuksia, voi laite tai selain jäädä "jumiin" vääriin tunnuksiin. Henkilö voi pakottaa itsensä ulos vääristä tunnuksista seuraavilla toimenpiteillä.
  1. Avaa puhelimella verkkoselain auki
  2. Mene osoitteeseen [https://mysignins.microsoft.com](<https://mysignins.microsoft.com/>)
  3. Valitse oikean yläreunan valikosta My Account -> Sign Out


![My_SignIns.PNG](https://support.nepton.com/hc/article_attachments/21077191790621)
## Tarkempi ongelmanselvitys
Mikäli ongelma ei ole selvinnyt yllä olevilla toimenpiteillä, tai organisaationne käytössä on InTune ottakaa yhteyttä toimittajaanne teknisen selvityksen aloittamiseksi.
