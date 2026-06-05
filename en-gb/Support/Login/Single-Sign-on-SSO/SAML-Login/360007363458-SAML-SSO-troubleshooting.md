---
id: 360007363458
title: SAML SSO troubleshooting
url: https://support.nepton.com/hc/en-gb/articles/360007363458-SAML-SSO-troubleshooting
locale: en-gb
category: Support
category_id: 360000446658
section: SAML Login
section_id: 360004542757
section_path:
- Login
- Single Sign-on (SSO)
- SAML Login
labels:
- Troubleshoot
- FAQ
promoted: false
updated_at: '2024-11-17T20:22:58Z'
edited_at: '2024-04-03T06:10:54Z'
---

# SAML SSO troubleshooting

SSO problems can be mainly caused by two different things. Either there is a problem in the SSO settings and the SSO is not working for anyone, of there is an issue identifying a specific person logging into the service. These scenarios on possible solutions are described below.
## SSO is not working for some people
The SSO is configured to match people based on a specific person identification attribute, like their username. The most commonly used attribute is a person's email address. If SSO is not working for some of the employees then the most probable cause is that the identifier used in the service does not match what is set up on SSO. This can be solved by setting a matching identification attribute in the persons data and in the SSO.
Some of the SSO login issues will be shown in the service log. Below are some most common issues explained.
  * **Person identification attribute(s) not found:** This message implies that the attribute used for identifying people does not exist in the request Nepton received from the identity provider. To fix it, go to Employees > Administration > Single Sign-on (SSO), and check the correct attribute is set to the 'Identify person by' field.
  * **More than one users are found for the value:** This message means that there was more than one person found in Nepton with the configured identifier (usually email in this case). To fix it, visit Employees > Person list, and search for the problem people, then amend their data. Identifiers used for SSO should be unique for each person.
  * **Could not find user:** This means that the requested person does not exist. To fix it, make sure that the person is existing in Nepton. If the person  _is_ already present, make sure that the information used to identify persons has the correct value. You can check which person field is being used to identify people for SSO from Employees > Administration > Single Sign-on (SSO)) > 'Identify person by' field.


## SSO is not working for anyone
Setting up Single Sign-On (SSO) can be a complicated process. Wherever possible, it should be handled by a technical specialist. This page contains the most common troubleshooting tips for problems with SSO configurations.
SSO error messages are recorded to the service log which can be found from Employees > Administration > Service log. If SSO is not working, this should be the first place you check for more information on the problem.
### Check the settings under Employees > Administration > Single Sign-on (SSO)
Please make sure that all configuration values are provided and that a valid certificate is installed. For further information on how to set up an identity provider see [Configure ADFS server in Nepton](<https://support.nepton.com/hc/en-gb/articles/360005242897-Configure-ADFS-server>)
### No service provider available **or** An error occurred while loading SSO configuration for identity provider
This kind of error message indicates that something went wrong in the platform. If you see this error, please contact Nepton Platform Support.
### Could not set partner identity provider, Error in sending request to identity provider **or** Error in receiving request from identity provider
  1. Check if all the correct configuration values are saved (Employees > Administration > Single Sign-on (SSO))
  2. Make sure that a valid certificate is installed and it is not expired
  3. If you have just installed a new certificate and that certificate also needs an encryption certificate to be installed, then send the encryption certificate to Nepton and it will be taken care for you.
  4. Ask the person, who is responsible for setting identity provider at your end, to look for any errors in the ADFS server and send the error messages to Nepton. These error messages are very essential for Nepton to resolve SSO issues.


### SSO login failed due to clocks out of sync
If you are getting this message then make sure that your identity provider server's date & time is not out of sync.
### The SAML assertion signature failed to verify
If you are getting this message then make sure that the certificate is valid and it is not expired. To see certificate information go to **Employees** \- **Administration** \- **Single Sign-on (SSO)**
### You have a stand-alone instance of Nepton platform running on your own server
The most common SSO problems encountered on third-party servers are caused by out of sync date and time settings. Check that the date & time on your server is synchronised with Finnish standard time.
To avoid this problem, it is recommended that servers are configured to automatically synchronise with a trustworthy NTP time server on a regular basis. Please contact your server administrator for your particular server environment and configuration.
## Common certificate problems
SAML SSO requires certificates for providers to prove they are trustworthy during authentication and communication. In some cases multiple certificates are required to establish a so-called chain of trust.
Certificates related to your SSO configuration are managed from **Employees > Administration > SSO configuration**
### I don't have any certificates
When first configuring SSO using SAML, you will need to provide certificates neccessary for communication with your identifity provider. Please see the **[Configuring SSO](<https://support.nepton.com/hc/en-gb/articles/360002590097>)** article.
### My certificate(s) have warnings
If a certificate you are using has problems, information about the issue(s) will be displayed on the right-hand side of the management page. The most common types of warning are that your certificate is soon expiring or has expired, the chain of trust is incomplete, or that you do not have any certificate actively in use.
#### Certificate is soon expiring or has expired
If your certificate(s) expire soon or have already expired, there will be a warning about it in the SSO configuration pages. Warnings about expiries appear several months in advance of the expiry date and mention exactly when your certificate(s) expire. You must replace your certificate(s) before this date.
Ordering new certificates from an authority can take some time, so it advisable to act swiftly and get the new certificate(s) early. You should speak with your service provider about how to order your replacements and where from.
Once the replacement certificates have arrived, you can add them to the SSO configuration, and configure the date and time they will be taken into use. This date and time should be coordinated with your provider to ensure a seamless change-over which doesn't interrupt end-users.
#### Missing certificate from chain of trust
Some authorities require that more than one certificate is used to establish trust and prove authenticity. In these situations, all of the related certificates must be added to your SSO configuration. The root certificate should be added to the Certificates section, and all supporting certificates should be added to the Supporting certificates section. If certificate chain is not correct service log might can show errors with text "SAML - allekirjoitusta ei voitu varmentaa". This issue is solved by ensuring the trust chain of uploaded certificates is correct. More information on certificate trust can be seen for example in here <https://en.wikipedia.org/wiki/Chain_of_trust>
#### No active certificate
To avoid interruptions to end-users you must have an active certificate added and configured to be used at all times.
If you are configuring a new SSO instance, and do not yet have any certificates added, please see the **[Configuring SSO](<https://support.nepton.com/hc/en-gb/articles/360002590097>)** article.
In the event you have multiple certificates, it is possible to set the date from which each one is taken into use. This facilitates seamless change over from old certificates to new ones without any interruption to the SSO login features for end-users.
To set a certificate as active, simply select one of your certificates that is valid on the target date, and set the **Start using on date**.
