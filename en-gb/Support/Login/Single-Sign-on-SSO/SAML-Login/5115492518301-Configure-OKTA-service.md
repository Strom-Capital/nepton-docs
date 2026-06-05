---
id: 5115492518301
title: Configure OKTA service
url: https://support.nepton.com/hc/en-gb/articles/5115492518301-Configure-OKTA-service
locale: en-gb
category: Support
category_id: 360000446658
section: SAML Login
section_id: 360004542757
section_path:
- Login
- Single Sign-on (SSO)
- SAML Login
labels: []
promoted: false
updated_at: '2026-01-21T12:35:16Z'
edited_at: '2026-01-21T12:34:30Z'
---

# Configure OKTA service

Below are detailed technical instructions for configuration of a customers' OKTA service for SAML based SSO (Single Sign On) with the Nepton platform. These instructions are intended for individuals with experience in the area of OKTA service.
Please see other articles under the [Configuring SSO](<https://support.nepton.com/hc/en-gb/articles/360002590097>) section for more information on the topic of SSO configuration.
Nepton SP (Service Provider) metadata can be found here:
https://go.nepton.com/ExternalLogin/Metadata/EntityDescriptor_SP_go.nepton.com_V7_27_Apr_2025_26_Apr_2026.xml
## OKTA configuration
Create new application and name it Nepton
Define SAML settings
Single sign-on URL: https://go.nepton.com/ExternalLogin/Saml2Consumer.aspx
Audience URI (SP Entity ID): https://go.nepton.com/ExternalLogin/Saml
Name ID format: Transient
Application username: Email
Response: Signed
Assertion Signature: Signed
Signature Algorithm: RSA-SHA256
Assertion Encryption: Unecrypted
Load the Identity Provider (IdP) certificate from OKTA
Find and copy the sign-in service URL from OKTA
Find and copy the EntityID value from the OKTA:n metadata
## Nepton configuration
Add the SSO settings and certificate to Nepton. Guidance can be seen [here](<https://support.nepton.com/hc/en-gb/articles/360002590097>).
