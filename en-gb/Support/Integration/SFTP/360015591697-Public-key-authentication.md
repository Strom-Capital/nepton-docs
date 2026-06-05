---
id: 360015591697
title: Public key-authentication
url: https://support.nepton.com/hc/en-gb/articles/360015591697-Public-key-authentication
locale: en-gb
category: Support
category_id: 360000446658
section: SFTP
section_id: 360001029457
section_path:
- Integration
- SFTP
labels: []
promoted: false
updated_at: '2024-09-13T07:14:30Z'
edited_at: '2024-09-13T07:14:29Z'
---

# Public key-authentication

If Public key authentication is used, the username/password login method is not available.
**NOTE: Following are not possible via Public key -authentication**
  * **Import of personnel information to Nepton**
  * **Export of personnel information from Nepton**
  * **Export of payment groups from Nepton**


Other data transfers can utilize RSA public key authentication. In this case only Nepton service can connect to SFTP server.
Define suitable username and leave password undefined.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360013442138)
Both public and private keys have already been created by Nepton Service. You can download the public key from the bottom of this article. Please note that there are several versions of the public key in different formats. You must select the public key version based on the target system or application requirements.
Deliver the public key and your defined username to SFTP service administrator.
