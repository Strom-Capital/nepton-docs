---
id: 7132764025373
title: IP-osoitteen määrittäminen kirjauspäätteeseen (toimitukset syyskuu 2022 alkaen)
url: https://support.nepton.com/hc/fi/articles/7132764025373-IP-osoitteen-m%C3%A4%C3%A4ritt%C3%A4minen-kirjausp%C3%A4%C3%A4tteeseen-toimitukset-syyskuu-2022-alkaen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Uuden kirjauspäätteen asennus
section_id: 360002103958
section_path:
- Kirjauspäätteet
- Uuden kirjauspäätteen asennus
labels: []
promoted: false
updated_at: '2024-08-23T09:11:59Z'
edited_at: '2023-09-12T13:28:00Z'
---

# IP-osoitteen määrittäminen kirjauspäätteeseen (toimitukset syyskuu 2022 alkaen)

Kiinteän IP osoitteen lisääminen kirjauspäätteelle pitää tehdä asiakkaan omissa tiloissa, jotta kirjauspäätteen toimivuuden testaaminen on mahdollista tämän jälkeen.
1\. Poistu kirjauspäätesovelluksesta painamalla kaikista kulmista järjestyksessä vasen yläkulma, oikea yläkulma, oikea alakulma, vasen alakulma.
2\. Tuplaklikkaa Windowsin työpöydällä olevaa kuvaketta Static IP. Jos käytettävissä ei ole ulkoista näppäimistöä, klikkaa Keyboard-kuvakkeesta avataksesi virtuaalinäppäimistö.
![1_Pikakuvakkeet.jpg](https://support.nepton.com/hc/article_attachments/21077798473245)
3\. Jos haluat tarkastaa laitteen MAC-osoitteen, valitse avautuvasta ikkunasta Details. MAC-osoite on Physical Address.
![MAC_address.png](https://support.nepton.com/hc/article_attachments/21077752251933)
4\. Jos haluat muokata IP-osoitetta, valitse avautuvasta ikkunasta Properties
![2_Static_IP_.jpg](https://support.nepton.com/hc/article_attachments/21077798478365)
4\. Klikkaa Yes-painikkeesta
![3_Static_ip_propertises_press_ok.jpg](https://support.nepton.com/hc/article_attachments/21077798475677)
5.Avaa Internet Protocol Version 4 (TCP/IPv4) tuplaklikkaamalla sitä.
![4._Properties.jpg](https://support.nepton.com/hc/article_attachments/21077798474013)
6\. Tee tarvittavat määritykset IP-osoitteeseen, aliverkon peitteeseen (subnet mask) ja oletusyhdyskäytävään (default gateway) sekä tarvittaessa myös DNS-servereihin ja klikkaa OK
![5_Static_IP_setup.jpg](https://support.nepton.com/hc/article_attachments/21077798476957)
7\. Sulje kaikki ikkunat ja palaa Windowsin työpöydälle. Käynnistä terminaalisovellus Nepton-kuvakkeesta.
