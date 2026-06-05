---
id: 23677421993501
title: Sääntöjoukon esimerkit - yleisluonteiset
url: https://support.nepton.com/hc/fi/articles/23677421993501-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-yleisluonteiset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels: []
promoted: false
updated_at: '2024-12-13T08:37:10Z'
edited_at: '2024-12-13T07:21:01Z'
---

# Sääntöjoukon esimerkit - yleisluonteiset

Tähän artikkeliin on koottu yleisluontoisia esimerkkejä poimintasääntöjen muokkaamiseen. Sääntöjä voidaan hyödyntää osana poimintasääntöjä eri liittymissä, mutta tulee huomioida kohdejärjestelmän vaatimukset esimerkiksi tiedon ryhmittelyn ja mahdollisten järjestelmäkohtaisten tietokenttien osalta.
### Poimitaan kentän arvo pilkulla erotettuna pisteen sijaan:
[code] 
    REPLACE(  
     ROUND(Amount / 3600, 2),   
     '.',   
     ','  
    ) AS Amount-- poimittavan arvon kentän nimi
[/code]
### Muutetaan desimaaliluku minuuteiksi ja tunneiksi:
[code] 
    CASE WHEN amount >= 0  
    THEN CONCAT( PRINTF( '%02d', FLOOR(amount / 3600) ), ':', PRINTF( '%02d', ROUND( ABS( ROUND( ROUND(Amount / 3600, 2) - FLOOR(Amount / 3600), 2 ) )* 60, 0 ) ) )  
    WHEN amount < 0  
    THEN CONCAT( '-', PRINTF( '%02d', FLOOR( ABS(Amount)/ 3600 ) ), ':', PRINTF( '%02d', ROUND( ABS( ROUND( ROUND(Amount / 3600, 2) - CEILING(Amount / 3600), 2 ) )* 60, 0 ) ) )   
    END AS Määrä,
[/code]
### Muutetaan desimaali kahden desimaalin tarkkuuteen:
[code] 
    ROUND (SUM (amount),2)
[/code]
