#!/usr/bin/env python
#!BruteXSS
#!Cross-Site Scripting Bruteforcer
#!Author: Shawar Khan
#!Site: http://shawarkhan.com

import httplib
import urllib
import socket
import urlparse
import os
from colorama import init , Style, Back,Fore
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
init()
banner = """                                                                                       
  ____             _        __  ______ ____  
 | __ ) _ __ _   _| |_ ___  \ \/ / ___/ ___| 
 |  _ \| '__| | | | __/ _ \  \  /\___ \___ \ 
 | |_) | |  | |_| | ||  __/  /  \ ___) |__) |
 |____/|_|   \__,_|\__\___| /_/\_\____/____/ 
                                            
 BruteXSS - Cross-Site Scripting BruteForcer
 
 Author: Shawar Khan                      

"""
print banner
try:
	def bg(p,status):
	    b = ""
	    l = ""
	    lostatus = ""
	    num = []
	    s = len(max(p, key=len)) #list
	    for i in range(len(p)): num.append(i)
	    maxval = str(len(num)) #number
	    for i in range(s) : b = b + "-"
	    for i in range(len(maxval)):l = l + "-"
	    statuslen = len(max(status, key=len))
	    for i in range(statuslen) : lostatus = lostatus + "-"
	    if len(b) < 10 : b = "----------"
	    if len(lostatus) < 14:lostatus="--------------"
	    if len(l) < 2 : l = "--"
	    los = statuslen
	    if los < 14: los = 14
	    lenb=len(str(len(b)))
	    if lenb < 14 : lenb = 10
	    upb = ("+-%s-+-%s-+-%s-+")%(l,b,lostatus)
	    print(upb)
	    st0 = "Parameters"
	    st1 = "Status"
	    print("| Id | "+st0.center(s," ")+" | "+st1.center(los," ")+" |")
	    print(upb)
	    for n,i,d in zip(num,p,status):
	        string = (" %s | %s ")%(str(n),str(i));
	        lofnum = str(n).center(int(len(l))," ")
	        lofstr = i.center(lenb," ")
	        lofst = d.center(los," ")
	        if "Not Vulnerable" in lofst:
	        	lofst = Fore.GREEN+d.center(los," ")+Style.RESET_ALL
	        else:
	        	lofst = Fore.RED+d.center(los," ")+Style.RESET_ALL
	        print("| "+lofnum+" | "+lofstr+" | "+lofst+" |")
	        print(upb)
	    return("")
	site = raw_input("[?] Enter URL(Make sure parameters have any value):\n[?] > ") #Taking URL
	if 'https://' in site:
		pass
	elif 'http://' in site:
		pass
	else:
		site = "http://"+site
	paraname = []
	paravalue = []
	finalurl = urlparse.urlparse(site)
	urldata = urlparse.parse_qsl(finalurl.query)
	domain0 = '{uri.scheme}://{uri.netloc}/'.format(uri=finalurl)
	domain = domain0.replace("https://","").replace("http://","").replace("www.","").replace("/","")

	print (Style.DIM+Fore.WHITE+"[+] Checking if "+domain+" is available..."+Style.RESET_ALL)
	connection = httplib.HTTPConnection(domain)
	connection.connect()
	print("[+] "+Fore.GREEN+domain+" is available! Good!"+Style.RESET_ALL)
	url = site
	wordlist = raw_input("[?] Enter location of Wordlist > ")
	payloads = []
	try:
		with open(wordlist,'r') as f: #Importing Payloads from specified wordlist.
			print(Style.DIM+Fore.WHITE+"[+] Loading Payloads from specified wordlist..."+Style.RESET_ALL)
			for line in f:
				final = str(line.replace("\n",""))
				payloads.append(final)
		lop = str(len(payloads))
		grey = Style.DIM+Fore.WHITE
		print(Style.DIM+Fore.WHITE+"[+] "+lop+" Payloads loaded..."+Style.RESET_ALL)
		print(Style.DIM+Fore.WHITE+"[+] Injecting Payloads..."+Style.RESET_ALL) 
		o = urlparse.urlparse(site)
		parameters = urlparse.parse_qs(o.query,keep_blank_values=True)
		path = urlparse.urlparse(site).scheme+"://"+urlparse.urlparse(site).netloc+urlparse.urlparse(site).path
		for para in parameters: #Arranging parameters and values.
			for i in parameters[para]:
				paraname.append(para)
				paravalue.append(i)
		total = 0
		c = 0
		fpar = []
		fresult = []
		for pn, pv in zip(paraname,paravalue): #Scanning the parameter.
			print(grey+"[+] Testing '"+pn+"' parameter..."+Style.RESET_ALL)
			fpar.append(str(pn))
			for x in payloads: #Bruteforcing
				enc = urllib.quote_plus(x)
				data = path+"?"+pn+"="+pv+enc
				page = urllib.urlopen(data)
				sourcecode = page.read()
				if x in sourcecode:
					print(Style.BRIGHT+Fore.RED+"[!]"+" XSS Vulnerability Found! \n"+Fore.RED+Style.BRIGHT+"[!]"+" Parameter:\t%s\n"+Fore.RED+Style.BRIGHT+"[!]"+" Payload:\t%s"+Style.RESET_ALL)%(pn,x)
					fresult.append("Vulnerable")
					c = 1
					total = total+1
					break
				else:
					c = 0
			if c == 0:
				print("[+]"+Style.BRIGHT+Fore.GREEN+Style.RESET_ALL+Style.DIM+Fore.WHITE+" '%s' parameter not vulnerable."+Style.RESET_ALL)%pn
				fresult.append("Not Vulnerable")
				pass
		print("[+] Bruteforce Completed.")
		if total == 0:
			print("[+] Given parameters are "+Style.BRIGHT+Fore.GREEN+"not vulnerable"+Style.RESET_ALL+" to XSS.")
		elif total ==1:
			print("[+] '%s' Parameter is "+Style.BRIGHT+Fore.RED+"vulnerable"+Style.RESET_ALL+" to XSS.")%total
		else:
			print("[+] '%s' Parameters are "+Style.BRIGHT+Fore.RED+"vulnerable"+Style.RESET_ALL+" to XSS.")%total
		print("[+] Scan Result for %s:")%domain
		print bg(fpar,fresult)
		exit()
	except(IOError) as Exit:
		print(Style.BRIGHT+Fore.RED+"[!] Wordlist not found!"+Style.RESET_ALL)
except(httplib.HTTPResponse, socket.error) as Exit:
	print(Style.BRIGHT+Fore.RED+"[!] Site "+domain+" is offline!"+Style.RESET_ALL)
	exit()
