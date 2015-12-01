
import random as rd
import urllib
import ssl
import sys
import re
from BeautifulSoup import *

def loadContentURL(url):
	webPage = urllib.urlopen(url).read()
	return BeautifulSoup(webPage)

def newURL(url,stem):
	if stem in url: return url
	else: return stem + url

def main():

	cmdargs = sys.argv
	if(len(cmdargs) == 2): 
		itr = int(cmdargs[1])
	else: return "Wrong syntax"

	url = "https://en.wikipedia.org/wiki/Main_Page"
	stem = "https://en.wikipedia.org"

	while(itr>0): 
		soup = loadContentURL(url)
		links = soup.findAll('a',href=True)
		url = newURL(rd.choice(links)['href'],stem)
		print url
		itr -= 1
	return 0

main()