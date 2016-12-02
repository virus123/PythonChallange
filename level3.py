import urllib.request
import re
website= urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
string = re.findall("<!--(.*?)-->", website, re.DOTALL)[-1]
re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", string)
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", string)))
