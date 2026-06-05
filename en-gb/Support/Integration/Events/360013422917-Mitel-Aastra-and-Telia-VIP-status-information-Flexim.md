---
id: 360013422917
title: Mitel Aastra and Telia VIP status information (Flexim)
url: https://support.nepton.com/hc/en-gb/articles/360013422917-Mitel-Aastra-and-Telia-VIP-status-information-Flexim
locale: en-gb
category: Support
category_id: 360000446658
section: Events
section_id: 360001061298
section_path:
- Integration
- Events
labels: []
promoted: false
updated_at: '2026-05-12T06:32:17Z'
edited_at: '2026-05-12T06:32:17Z'
---

# Mitel Aastra and Telia VIP status information (Flexim)

Nepton can send person's status information to Mitel Aastra and Telia VIP (former Telia Merex) phone systems. Both integrations send data to Flexim which then provides the data for the phone systems.
## Definitions
### Defining persons identifier
Persons identifier can be set by editing persons information in **Employees - Person's information - Identifiers - Aastra**. Both Aastra and VIP integrations use the Aastra-identifier field set in the identifier settings.
![aastra-identifier-EN.png](https://support.nepton.com/hc/article_attachments/360012857478)
### Defining event types
Event type codes can be set in working community settings, **Worktime** \- **Administration** \- **Working Community Settings** \- **Integrations** \- **Mitel Aastra** for Mitel Aastra integration and **Worktime** \- **Administration** \- **Working Community Settings** \- **Integrations** \- **Telia Merex** for Telia VIP integration.
![aastra-wt-settings-EN.PNG](https://support.nepton.com/hc/article_attachments/360012857538)
### Event type codes
Event type codes can be set according to the table below.
Code | Information  
---|---  
1 | Meeting  
2 | In (equal to starting work)  
3 | Out (equal to ending work)  
5 | Travel work  
6 | Holiday / Work time shortening leave / Balance leave  
7 | Sick leave  
8 | Training  
9 | Work elsewhere  
0 | Out other reason (equal to ending work)  
a | Lunch  
### Sending data
The Mitel Aastra host address and other settings can set in working community settings, **Worktime** \- **Administration** \- **Working Community Settings** \- **Integrations** \- **Mitel Aastra - Configuration**
![aastra-configuration.PNG](https://support.nepton.com/hc/article_attachments/360012783097)
The Telia VIP host address and other settings can set in working community settings, **Worktime** \- **Administration** \- **Working Community Settings** \- **Integrations** \- **Telia Merex - Configuration**
The host address should be in form ”123.456.78.9:1234”, the IP address and the TCP port separated by a colon.
![merex-configuration.PNG](https://support.nepton.com/hc/article_attachments/360012783117)
For both integrations, the maximum amount of statuses sent per minute is 100 submissions by default. Delay between sent status rows in milliseconds is 500 milliseconds by default. These can be changed in their respective setting fields.
### Limitations
  * Employees with personnel number 0 are not included in the integration file


## Technical operation of the integration
Statuses are sent to the specified server address as raw data, one status at a time. Information is sent via an opened TCP socket and the connection does not wait for a return message for the sent data.
### Sent data
The integration is standardized and there is no need to make changes to the content. One status change is textual data separated by a tab character. Used character set is `ASCII`. The sent information is described below.
Information | Description  
---|---  
Start character | Start character is always an `STX` character (Start of Text), ASCII HEX `02`.  
Event type code |   
_Tab character_ |   
Person's Aastra identifier / employee number | Up to 11 characters long.  
_Tab character_ |   
Other reason code | Up to 3 characters long. Not used.  
_Tab character_ |   
Event end date | If the event has a known end date, it will be included. Format `DDMM`, for example `3105`.  
_Tab character_ |   
Event end time | If the event has a known end time, it will be included. Format `HHMM`, for example `1230`.  
Checksum character | Checksum is only calculated for Telia VIP integration and won't be included with Mitel Aastra integration.  
End character | End character is always an `CR` character (carriage return), ASCII HEX `0D`.  
### Expected response
Integration does not expect any response for sent person statuses. As long as writing to the open TCP socket does not fail, person status is considered as successfully sent.
### Checksum calculation formula
  1. The position of each character in the ASCII table is calculated and the integer value of all positions is added together. Only characters before checksum are checked.
  2. The integer value of lowest 7 bits of the sum from previous step is retrieved.
  3. If the integer value is less than 32, 32 is added to the value.
  4. The resulting integer value is the order number of the checsum character in ASCII table.


PHP example:
[code]
    <?php
    
    function getChecksum(string $string): string
    {
        $sum = array_sum(
            array_map(
                static function (string $chr): int {
                    return ord($chr);
                },
                str_split($string)
            )
        );
        $sum &= hexdec('0x7f');
        if ($sum < hexdec('0x20')) {
            $sum += hexdec('0x20');
        }
        return chr($sum);
    }
[/code]
### Example
`STX`, `TAB`, `CHECKSUM` and `CR` characters are visualized in the example.
[code]
    STX
[/code]
[code]
    TAB
[/code]
[code]
    TAB
[/code]
[code]
    TAB
[/code]
[code]
    TAB
[/code]
[code]
    CHECKSUM
[/code]
[code]
    CR
[/code]
