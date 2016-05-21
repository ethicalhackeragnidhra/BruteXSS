##BruteXSS
BruteXSS - Cross-Site Scripting BruteForcer

Author: Shawar Khan  

###Compatibility: 
*Windows , Linux or any device running python 2.7

###Requirements: 
*Python 2.7
*Wordlist included(wordlist.txt)
*Modules included(Colorama,Mechanize)

**WARNING: Copying or modification of this tool is not allowed!**

###Description:
BruteXSS is a Cross-Site Sripting Bruteforcer which is used for bruteforcing parameters with XSS payloads. This tool is specially designed for Pentesters, Security Researchers and Hackers who are willing to check the URLs by using XSS bruteforce. BruteXSS basically loads payloads from a specified wordlist and injects them in the target url, If the parameter is vulnerable it will be printed out.

###Features:

*XSS Bruteforcing
*XSS Scanning
*Supports GET/POST requests
*Custom wordlist can be included
*User-friendly UI

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
