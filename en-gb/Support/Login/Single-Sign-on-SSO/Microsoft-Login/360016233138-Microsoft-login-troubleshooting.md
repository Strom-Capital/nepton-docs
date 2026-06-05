---
id: 360016233138
title: Microsoft login troubleshooting
url: https://support.nepton.com/hc/en-gb/articles/360016233138-Microsoft-login-troubleshooting
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
- ms login
promoted: false
updated_at: '2025-01-21T10:43:27Z'
edited_at: '2025-01-21T10:39:42Z'
---

# Microsoft login troubleshooting

Microsoft Azure Active Directory is now called Microsoft Entra ID
Under some conditions Microsoft login might not work as expected. Issues can be categorized to be one of the three following types:
  * Nepton app installed through Microsoft Endpoint Manager to device can lead to confusion in case the person is using non-default browser
  * There is a configuration mistake in personnel or organization information.
  * The organization-wide security rules in Entra ID might be misconfigured.


Guidance below allows administrator to investigate and solve issues regarding Microsoft login. You should perform the troubleshooting actions in the following order.
## Review Microsoft Endpoint Manager settings
**This only applies to organizations using Microsoft Endpoint Manager**
In case your organization has made Nepton app -style installation to device and person is using non-default browser, certain devices and operating systems can lead to situation in which person must login to Nepton service twice. This is not a feature or issue with the Nepton service, but a property of the device operating system instead. Solution is to instruct person to use Nepton service through the device installed app link, instead of the browser.
## Review Nepton Service log
Service log shows failed Microsoft login attempts. It is possible that the reason for the failed login can be seen from the log. Reason for failed login can be for example missing email address on persons information or multiple persons sharing one email address. Fixing the indicated issue can solve the login problem.
Service log can be seen in Nepton in following way.
Navigate to **Employees, Admistration, Service Log** and review the notes in the **SSO** area of the service log.
## Review Entra ID Log
Entra ID collects log of failed login attempts. Review Entra ID log to see if it explains the reason for the problem. Login problem can be solved by fixing the problem indicated in this log.
Entra ID log can be seen by performing following actions:
  * Login as administrator to Azure service
  * Navigate to **Microsoft Entra ID, Monitoring, Signs-Ins** section
  * Add **Status = Failure** filter
  * Add **Application, SSO for Nepton v2** filter
  * Review the contents of failure messages


In case the logged error message is AADSTS50011, please add the missing "redirect URI" definition according to configuration step 6 of [this article](<https://support.nepton.com/hc/en-gb/articles/360009872457>).
You can read more about Entra ID sign-in troubleshooting in the <https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-troubleshoot-sign-in-errors> article..
## Review Entra ID Conditional Access configuration
If only some of the devices experience login problems or certificate warnings, or if INTERRUPTED entries appear in the Entra ID logs, the problem is likely related to Conditional Access settings. Note that the problem can occur even if you run Conditional Access in “report only” mode. More on the topic can be found in the <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only> article. Please see the yellow "WARNING" section in this article.
You can check the Device State setting in the following way:
  * Login as administrator to Azure service
  * Navigate to **Microsoft Entra ID, Manage, Enterprise Applications, SSO for Nepton v2, Security, Conditional Access** section
  * Check the conditional access settings
  * Check the **Device State** setting


If the Device State setting is ON or REPORT ONLY, please change the setting to OFF, so you can test if this fixes the login problem.
Instead of the Device state setting, a similar protection can possibly also be implemented as a combination of Assignments, Conditions, Client Apps, and Access Controls, Grants settings.
## Problems when having multiple Microsoft login buttons
Several Microsoft Login buttons can be shown in the service. Each button connects to separate Entra ID tenant of the customer. If there appears problems in this kind of setup, please check that there is only one app registration in each Entra ID tenant. In case several Entra ID tenants have an app registration with the same application ID, this is probable cause for problems. Please follow [Microsoft login setup in Entra ID](<https://support.nepton.com/hc/en-gb/articles/360009872457>) instructions to create new app registrations to both tenants, follow [Setup Microsoft login in Nepton](<https://support.nepton.com/hc/en-gb/articles/360010602957>) instructions to overwrite existing values in Nepton service, and remove old app registrations from all Entra ID tenants.
## AADSTS7000215: Invalid client secret provided
**This typically only applies to client secrets created with Powershell**
Long-term client secret created with Powershell might not work properly. This issue does not affect all customer environments.
If necessary, you can abandon the Powershell generated client secret and create new shorter-validity client secret manually through the Azure Portal. Please see [Setup Nepton in Entra ID](<https://support.nepton.com/hc/en-gb/articles/360009872457>) steps 12B - 16. Remember to update the new client secret to Nepton settings.
## Recreating Entra ID application
Explanations for reviewing the Nepton service log and Microsoft's Entra ID log are provided above. It is possible that the Entra ID log shows successful logins, but users are simply returned to the Nepton front page after logging into Entra ID whilst there are no entries in Nepton's own logs. In this case, there is likely an error in the settings, so it is recommended to delete the previously created app registration from Entra ID, remove the previously created Microsoft Login configuration from Nepton, and redo the entire configuration process from the beginning.
## Enforce Microsoft Logout for selected person
If person has multiple Microsoft login credentials, browser or device might get "stuck" with wrong credentials. Person can logout from such wrong credentials with following actions:
  1. Open the (correct) web browser on your computer or phone
  2. Go to address [https://mysignins.microsoft.com](<https://mysignins.microsoft.com/>)
  3. On top right, select My Account -> Sign Out


![My_SignIns.PNG](https://support.nepton.com/hc/article_attachments/11617176563485)
## Detailed troubleshooting
If failed login is not solved by performing the actions above or your organization uses InTune, please contact your solution provider to initiate technical troubleshooting.
