---
id: 360010602957
title: Setup Microsoft login in Nepton
url: https://support.nepton.com/hc/en-gb/articles/360010602957-Setup-Microsoft-login-in-Nepton
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
- m365
promoted: false
updated_at: '2024-09-27T12:07:17Z'
edited_at: '2024-09-27T12:07:16Z'
---

# Setup Microsoft login in Nepton

Microsoft Azure Active Directory is now called Microsoft Entra ID
Microsoft login (Entra ID Single Sign-On) enables your employees to access Nepton with the standard credentials and security practices of your organization. This guidance describes the necessary configuration steps to enable Microsoft SSO for Nepton in Entra ID. Intended audience is Microsoft Entra ID or Microsoft 365 administrator of your organisation.
## Requirements
Your organization needs to have active Microsoft 365 or Entra ID subscription. Your organization needs to have at least one free Entra ID application registration slot available. All Microsoft 365 customers received at least 10 application registration slots on initial subscription start. 
## Get two values from Entra ID and save them to Nepton
Get two values **Application (client) ID** and **Secret value** from Entra ID. Instructions [here](<https://support.nepton.com/hc/en-gb/articles/360009872457>)
Go to Employees > Administration
Go to the section Single sign-on (SSO) > Microsoft Login
Fill in the values and save the changes
  * **Name** : The text that appears on the login button (for example: Microsoft login)
  * **Application (client) Id** : Text from Entra ID
  * **Secret value:** Text from Entra ID
  * Guidance about fetching these text values can be seen [here](<https://support.nepton.com/hc/en-gb/articles/360009872457>)
  * Please take care to use the **secret value** and not the **secret ID**


ATTENTION: If secret value has an expiration date, you must before occurrence of such expiration date always create in Entra ID a new secret value and update this secret value to Nepton. This is required for uninterrupted use of the Microsoft logins in Nepton service.
![](https://support.nepton.com/hc/article_attachments/14916351002013)
## Changing the secret value
If Microsoft login has already been used and you want to change the secret value (for example, when the secret value expires), change the new secret value in the Microsoft Entra ID line by pressing "Edit" button, enter the new secret value instead of the old one and press "Save".
![](https://support.nepton.com/hc/article_attachments/17684164749597)
## Grant permissions and test
On first Microsoft login, you might need to authorize the SSO app on behalf of the whole organization. If this occurs, a separate popup will be presented to user who first logs in from your organization. 
If user is Entra ID administrator, the popup will look like below, and user should accept. Do not press cancel.
![mceclip4.png](https://support.nepton.com/hc/article_attachments/13409925440925)
If user is normal user, she will be presented with a different popup allowing her to request permission from Entra ID administrator. In this case it’s advisable to **_separately & directly_** contact Entra ID administrator of your organization.
Microsoft login will not work before above consent and permissions are granted.
