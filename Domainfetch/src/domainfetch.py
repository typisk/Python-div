# -*- coding: utf-8 -*-

# Fetches expired domains from domeneshop #
import urllib, re, sys

f = urllib.urlopen("http://www.domeneshop.no/expired.cgi")
s = f.readlines()

dato = False

for line in s:
    
    finndato = re.search('(\d{2}\.\d{2}\.\d{4})', line)
         
    if finndato:
        dato = finndato.group(1)
        print dato
        
    if dato:
        finnurl = re.search('([a-zA-z0-9øæåØÆÅ\-\.]*)\.no', line)
        if finnurl:
            print finnurl.group(0)
            
    finnslutt = re.match('<\/table>', line)
    if finnslutt:
        sys.exit()

f.close()
