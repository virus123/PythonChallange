import urllib.request
import re
sitesource = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
rare = re.findall("<!--(.*?)-->", sitesource, re.DOTALL)[-1]
print("".join(re.findall("[A-Za-z]", rare)))

