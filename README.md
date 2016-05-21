#BruteXSS
**WARNING: Copying or modification of this tool is not allowed!**

BruteXSS - Cross-Site Scripting BruteForcer

Author: [Shawar Khan](https://shawarkhan.com)

###Compatibility: 
* Windows , Linux or any device running python 2.7

###Requirements: 

* Python 2.7

* Wordlist included(wordlist.txt)

* Modules included(Colorama,Mechanize)

###Description:
**BruteXSS** is a Cross-Site Sripting Bruteforcer which is used for bruteforcing parameters with XSS payloads. This tool is specially designed for Pentesters, Security Researchers and Hackers who are willing to check the URLs by using XSS bruteforce. BruteXSS basically loads payloads from a specified wordlist and injects them in the target url, If the parameter is vulnerable it will be printed out. BruteXSS now supports GET and POST requests which makes it much powerful when it comes to bruteforcing and scanning the modern web.

###Features:

* XSS Bruteforcing

* XSS Scanning

* Supports GET/POST requests

* Custom wordlist can be included

* User-friendly UI

###Usage(GET Method):

```
COMMAND:  python brutexss.py
METHOD:   g
URL:      http://www.site.com/?parameter=value
WORDLIST: wordlist.txt
```

###Usage(POST method):

```
COMMAND:   python brutexss.py
METHOD:    p
URL:       http://www.site.com/file.php
POST DATA: parameter=value&parameter1=value1
WORDLIST:  wordlist.txt
```

###Output:

```
  ____             _        __  ______ ____  
 | __ ) _ __ _   _| |_ ___  \ \/ / ___/ ___| 
 |  _ \| '__| | | | __/ _ \  \  /\___ \___ \ 
 | |_) | |  | |_| | ||  __/  /  \ ___) |__) |
 |____/|_|   \__,_|\__\___| /_/\_\____/____/ 
                                            
 BruteXSS - Cross-Site Scripting BruteForcer
 
 Author: Shawar Khan - https://shawarkhan.com                      


Select method: [G]ET or [P]OST (G/P): p
[?] Enter URL:
[?] > http://site.com/file.php
[+] Checking if site.com is available...
[+] site.com is available! Good!
[?] Enter post data: > parameter=value&parameter1=value1
[?] Enter location of Wordlist (Press Enter to use default wordlist.txt)
[?] > wordlist.txt
[+] Using Default wordlist...
[+] Loading Payloads from specified wordlist...
[+] 25 Payloads loaded...
[+] Injecting Payloads...

[+] Testing 'parameter' parameter...
[+] 2 / 25 payloads injected...
[!] XSS Vulnerability Found! 
[!] Parameter:	parameter
[!] Payload:	"><script>prompt(1)</script>

[+] Testing 'parameter1' parameter...
[+] 25 / 25 payloads injected...
[+] 'parameter1' parameter not vulnerable.
[+] 1 Parameter is vulnerable to XSS.
+----+--------------+----------------+
| Id | Parameters   |     Status     |
+----+--------------+----------------+
| 0  |  parameter   |  Vulnerable    |
+----+--------------+----------------+
| 1  |   parameter1 | Not Vulnerable |
+----+--------------+----------------+

```
