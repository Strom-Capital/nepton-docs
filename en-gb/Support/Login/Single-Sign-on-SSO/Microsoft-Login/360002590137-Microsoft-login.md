---
id: 360002590137
title: Microsoft login
url: https://support.nepton.com/hc/en-gb/articles/360002590137-Microsoft-login
locale: en-gb
category: Support
category_id: 360000446658
section: Microsoft Login
section_id: 360002832097
section_path:
- Login
- Single Sign-on (SSO)
- Microsoft Login
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-10-29T14:05:12Z'
edited_at: '2025-08-11T08:54:42Z'
---

# Microsoft login

Microsoft Azure Active Directory is now called Microsoft Entra ID
By setting up Microsoft login, access to Nepton will be granted by your Microsoft account login. Organization can also apply their defined Entra ID security policies for each login.
![](https://support.nepton.com/hc/article_attachments/29507457163421)
## Best practice
Best practice recommendation for implementing Single-Sign-On (SSO) is explained in this article and linked articles.
The best practice is to implement SSO with direct MSAL integration to Microsoft Identity Platform. This approach significantly reduces the initial SSO configuration and long-term maintenance effort required when compared to more traditional SAML based approaches. Over 90% of Nepton enterprise customers have selected this simple and modern MSAL approach instead of more legacy approaches.
## Best practice setup
When taking Microsoft login into use, you need to define certain configurations into your Entra ID environment. Instructions to do this can be read [here](<https://support.nepton.com/hc/en-gb/articles/360009872457>).
Please note that if you require project work from vendor during your Microsoft login activation, such work can be invoiced on standard hour rates.
Users can also login to the Nepton service with direct login link, without pressing the login button. User will be automatically logged in, as long as the user has logged into their Microsoft account, if not, user will be shown the login page. Direct login link can be found by a Administrator-role by navigating Employees > Administration > Single sign-on (SSO) > Microsoft-login.
