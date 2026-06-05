---
id: 10375124469021
title: Rounding of hours to a decimal number in work time
url: https://support.nepton.com/hc/en-gb/articles/10375124469021-Rounding-of-hours-to-a-decimal-number-in-work-time
locale: en-gb
category: Support
category_id: 360000446658
section: Reporting in general
section_id: 360005870478
section_path:
- Reporting
- Reporting in general
labels: []
promoted: false
updated_at: '2025-05-13T06:32:49Z'
edited_at: '2025-05-13T06:32:49Z'
---

# Rounding of hours to a decimal number in work time

Showing minutes as decimal hours is not possible without rounding the decimal value. To make work time reports easier to read, the hours as a decimal number are rounded to two decimal places.
In addition to this, it is good to be aware that the values shown in the reports always come from the total number of hours and minutes, which are presented as a rounded decimal number. Reports do not sum rounded decimals.
For example the following work hours:
  * Ma - 7h 33 min
  * Ti - 7h 47 min
  * Ke - 7h 54min
  * To - 7h 39 min
  * Pe - 7h 30 min


Would be shown on _Work hours_ > _Reports_ > _Realised work hours_ report as follows:
![](https://support.nepton.com/hc/article_attachments/27327604035485)
The total hours worked is calculated from the exact number of hours and minutes instead of adding up the decimal numbers shown on the report. The total hours worked in hours and minutes is 38 hours 23 minutes. The value as a rounded decimal number is 38,38 hours.
## Rounding table
Rounding of minutes to hours as a decimal value is done according to the following table:
Minutes | Decimal hours  
---|---  
1 | 0.02  
2 | 0.03  
3 | 0.05  
4 | 0.07  
5 | 0.08  
6 | 0.10  
7 | 0.12  
8 | 0.13  
9 | 0.15  
10 | 0.17  
11 | 0.18  
12 | 0.20  
13 | 0.22  
14 | 0.23  
15 | 0.25  
16 | 0.27  
17 | 0.28  
18 | 0.30  
19 | 0.32  
20 | 0.33  
21 | 0.35  
22 | 0.37  
23 | 0.38  
24 | 0.40  
25 | 0.42  
26 | 0.43  
27 | 0.45  
28 | 0.47  
29 | 0.48  
30 | 0.50  
31 | 0.52  
32 | 0.53  
33 | 0.55  
34 | 0.57  
35 | 0.58  
36 | 0.60  
37 | 0.62  
38 | 0.63  
39 | 0.65  
40 | 0.67  
41 | 0.68  
42 | 0.70  
43 | 0.72  
44 | 0.73  
45 | 0.75  
46 | 0.77  
47 | 0.78  
48 | 0.80  
49 | 0.82  
50 | 0.83  
51 | 0.85  
52 | 0.87  
53 | 0.88  
54 | 0.90  
55 | 0.92  
56 | 0.93  
57 | 0.95  
58 | 0.97  
59 | 0.98
