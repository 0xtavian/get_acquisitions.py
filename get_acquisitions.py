#!/bin/python

import requests,sys
import base64
import re  
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Enter domain name (-d) to pull acquisition from SecurityTrails.com. Required arguments: email address (-e) and password (-p)')
parser.add_argument("-d")
parser.add_argument("-e")
parser.add_argument("-p")

args = parser.parse_args()
d = args.d
e = args.e
p = args.p

def get_acquisitions():
 
 s=requests.Session()
 r = s.get('https://securitytrails.com/app/account')
 soup = BeautifulSoup(r.content, 'html.parser')

 all_scripts = soup.find_all('script')
 precsrf = all_scripts[9]

 for line in precsrf:
  csrf = line.split('"')[3] 
 
 r2 = s.post('https://securitytrails.com/app/api/console/account/login', json={"_csrf_token": csrf , "login":{"email": "{0}".format(e), "password":"{0}".format(p)}})
 r3 = s.get('https://securitytrails.com/app/api/v1/surface_browser/acquisitions/{0}'.format(d))
 content = r3.content
 print(content.decode('utf-8')) 
get_acquisitions()
