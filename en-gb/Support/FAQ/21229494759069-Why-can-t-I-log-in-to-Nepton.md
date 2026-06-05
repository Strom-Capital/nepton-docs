---
id: 21229494759069
title: Why can't I log in to Nepton?
url: https://support.nepton.com/hc/en-gb/articles/21229494759069-Why-can-t-I-log-in-to-Nepton
locale: en-gb
category: Support
category_id: 360000446658
section: FAQ
section_id: 360000934177
section_path:
- FAQ
labels:
- login problem
- kirjautumisongelma
- ongelma kirjautumisessa
- problem with login
promoted: false
updated_at: '2026-03-13T06:34:54Z'
edited_at: '2026-03-13T06:34:54Z'
---

# Why can't I log in to Nepton?

This article reviews the most common login problems and solutions.
Instructions for logging in can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002602998>).
### 1\. First, check the following
  * You are logging into the service at **go.nepton.com** (same address on mobile device and computer)
  * You are logging into the right **Company** (your organization’s environment). If necessary, confirm the name of your organization's Nepton environment with your HR department.
  * Is there an outage in the service: We will update in the [Platform status article](<https://support.nepton.com/hc/en-gb/articles/360006554777>) if a malfunction affecting login has been detected in the service. The maintenance window is normally active every Tuesday from 19:15 to 19:45. During this time, there may be a short service outage.
  * If a username/email and password are used instead of SSO login, make sure the information is correct and order a new password if necessary.


**Password reset link not received in the user's email?**  
First, check that the user has indeed tried to log in using the same email address that is specified in the person's Employees section information in the service. An extra space at the end of the email can also prevent login. After this, it is advisable to check the spam folder in the email. If these actions do not help, the organization’s Nepton administrator can set a temporary password for the user and ask the user to change the password to a new one after logging into the service (password change instructions [here](<https://support.nepton.com/hc/en-gb/articles/360002596657>)).
### 2\. Check if the problem is browser or device-specific
  * Does logging in work with another browser (Safari/Chrome/Firefox/Edge)?
  * Does logging in work with another device (mobile device, tablet, computer)?


To ensure the login issue is not caused by the browser, please clear the browser’s cache and cookies.
Instructions for clearing the browser’s cache and cookies can be found on the service providers’ own pages (the following links direct to an external site):
[Google Chrome cache clearing](<https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop>)  
[Firefox cache clearing](<https://support.mozilla.org/en-US/kb/how-clear-firefox-cache>)  
[Microsoft Edge cache clearing](<https://support.microsoft.com/en-us/microsoft-edge/view-and-delete-browser-history-in-microsoft-edge-00cf7943-a9e1-975a-a33d-ac10ce454ca4>)
Also, update your browser to the latest software version if necessary.
### 3\. If the above measures do not help, contact your supervisor, your organization’s HR department, or the Nepton administrator, who can check the following:
  * First, ensure that the login credentials used by the person match the information stored in the service (email address and username). The login identifier is the person's email address or username. An extra space at the end of the email can also prevent login.
  * After this, the Nepton administrator can investigate [the service log](<https://support.nepton.com/hc/en-gb/articles/360002575478>) to determine any other reasons for the login issue. Only the organization's administrators can access the service log via **Employees > Administration > Service Log**.
If you encounter issues with single sign-on (Microsoft Login, Google Login, SAML), select SSO in the Area field in the service log filters. The service log will describe the cause of the login issue. The most common problems are due to changes in the login details of the person logging in that have not been updated in Nepton (for example, the email address has changed), or the secret value provided by a third party for logging in has expired (for example, Entra ID). We have a separate article in our support service for troubleshooting Microsoft Login issues [here](<https://support.nepton.com/hc/en-gb/articles/360016233138>).
  * If necessary, the trained administrator user can also contact our [customer service](<https://support.nepton.com/hc/en-gb/articles/7077076926237>). Please include the following information in the support request:
    1. The person affected by the problem, and if the problem affects multiple people
    2. The devices and browsers used to attempt the login
    3. Whether the cache and cookies have been cleared
    4. A video of the login attempt or a clear description of when the problem occurs: For example, does the login page open at all or can the organization's environment be selected?
With this information, we can immediately start investigating the cause of the problem.
