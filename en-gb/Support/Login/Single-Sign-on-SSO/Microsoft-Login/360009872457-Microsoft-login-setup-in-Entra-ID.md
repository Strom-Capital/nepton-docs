---
id: 360009872457
title: Microsoft login setup in Entra ID
url: https://support.nepton.com/hc/en-gb/articles/360009872457-Microsoft-login-setup-in-Entra-ID
locale: en-gb
category: Support
category_id: 360000446658
section: Microsoft Login
section_id: 360002832097
section_path:
- Login
- Single Sign-on (SSO)
- Microsoft Login
labels: []
promoted: false
updated_at: '2026-02-05T13:58:38Z'
edited_at: '2024-09-27T12:05:11Z'
---

# Microsoft login setup in Entra ID

Microsoft Azure Active Directory is now called Microsoft Entra ID
Microsoft login (Entra ID Single Sign-On) enables your employees to access Nepton with the standard credentials and security practices of your organization. This guidance describes the necessary configuration steps to enable Microsoft SSO for Nepton in Entra ID. Intended audience is Microsoft Entra ID or Microsoft 365 administrator of your organisation.
## Requirements
Your organization needs to have active Microsoft 365 or Entra ID subscription. Your organization needs to have at least one free Entra ID application registration slot available. All Microsoft 365 customers received at least 10 application registration slots on initial subscription start. 
## User Identity
Entra ID field EMAIL is used to identify the user. This must match the Nepton field EMAIL of the user.
Nepton needs to know the value of Entra ID field EMAIL of your employees. These are typically transferred to Nepton via scheduled daily user import mechanism. Please discuss this in more detail with your Nepton project manager as needed.
Entra ID email of your employee can be manually checked via following method
  * Azure Portal
  * Microsoft Entra ID
  * Users, select employee
  * Email can be found in one of these (use the below order): 
    * Profile, contact info, email
    * Authentication methods, email
    * Profile, user principal name


## Entra ID Configuration Steps
1\. Sign-in to your Azure portal <https://portal.azure.com/#home>
2\. Microsoft Entra ID
3\. Manage, app registrations (NOT enterprise applications)
4\. Press the tab button + New Registration
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360009165118)
5\. Register an application
6\. Fill in details exactly like below:
  * **Name:** SSO for Nepton V2
  * **Supported account types:** Accounts in this organizational directory only
  * **Redirect URI Type:** Web
  * **Redirect URIs:**
    * <https://go.nepton.com/msal.aspx>
    * <https://entra.microsoft.com/TokenAuthorize>


We recommend the use of "Accounts in this organizational directory" option. This ensures that authorization attempts through other organizations (companies, schools, etc) are already blocked directly by Microsoft.
Please note that only the "Accounts in any organizational directory" option is supported.
Please note that the Redirect URIs -addresses must be uppercase/lowercase typed exactly as above.
Press the Register -button
7\. You should now be redirected to the overview of the SSO for Nepton V2 application you just created.
8\. On the left, Authentication, advanced settings, Front-channel logout URL
<https://go.nepton.com/logout.aspx>
The URL above is case-sensitive, write URL fully in lowercase
9\. On the left, Authentication, advanced settings, implicit grant, enable Access tokens and ID tokens. These are needed as Nepton authentication flow invokes Web API
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360011895738)
10\. Save
11\. On the left, Overview, copy the values of **Application (client) ID** and **Object ID** to notepad. You will need at least one of these values on later steps.
12\. Let's create a client secret value. 
ATTENTION: Each client secret value has an expiration date. Please see details below. Before this expiration date arrives, you must renew the client secret and update the new client secret value to Nepton. This is required for uninterrupted use of the Microsoft logins in Nepton service.
You have two options for this step.
**A) Create client secret via Powershell**
ATTENTION: This is the best option, if you can get it to work.
Do not define expiration date to be more than 5 years in the future. Any client secret value thus defined would be created, but it might ultimately fail to work when taken into use in Nepton, due to bug in Entra ID.  

If you can't get Nepton logins to work with option A, you should pick option B instead.
This option allows client secrets with 5 years. Steps 12, 13 and 16 need to be re-done every ten years.
For this option, you would need to know Powershell. Please note that Powershell 7 does not support Entra ID connectivity, so please use Powershell 5.1 x86 version instead.
In case you have not yet installed the necessary Powershell module, please do it now: 
Install-Module AzureAD
Execute the following commands (end date can't be over 5 years from now):
Connect-AzureAD
$startDate = Get-Date
$endDate = $startDate.AddYears(5)
$value= New-AzureADApplicationPasswordCredential -ObjectId "REPLACE_WITH_OBJECTID_OF_APP_REGISTRATION" -StartDate $startDate -EndDate $endDate 
$value
**B) Create client secret via Azure Portal**
This option can be done solely via browser. Downside is that client secret expires every two years and thus steps 12, 13 and 16 have to be re-done every two years.
On the left, Certificates & Secrets, create new client secret. Mark this client secret to be in effect as long as possible, or (if possible) never to expire. Add. Wait until you see this notification on the top right corner:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360011736677)
13\. Copy the client secret **value** to notepad. Make sure (option 12B) that you did not copy the client secret **ID** value by accident. You will need the client secret **value** on later steps.
14\. Go to **Microsoft Entra ID, Manage, Enterprise Applications, SSO for Nepton v2, Security, Permissions**
15\. Click **Grant admin consent for YOUR TENANT** and approve the consent terms shown in the popup
16\. [Setup Microsoft login in Nepton](<https://support.nepton.com/hc/en-gb/articles/360010602957>)
