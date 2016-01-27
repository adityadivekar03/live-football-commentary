
#!/usr/bin/python
import time
import urllib2

from bs4 import BeautifulSoup
from urllib import urlopen

import json

f = open('BernleyvsDerbyCounty.txt','w')
user_url = raw_input('Enter the url of the site for live football commentary')

#catching any error in opening the url
try:
	urlopen(user_url)

except IOError:
	print "Incorrect URL supplied. Please enter a correct URL"

except urllib2.HTTPError, err:
   if err.code == 404:
       print "Page not found!"
   elif err.code == 403:
       print "Access denied!"
   else:
       print "Something happened! Error code", err.code

except urllib2.URLError, err:
    print "Some other error happened:", err.reason

soccerpage = urlopen(user_url).read()
soup = BeautifulSoup(soccerpage.decode('utf-8', 'ignore'))

for commentary in soup.find_all(attrs={"class": "post"}):
	comm = commentary.get_text()
	comm = comm.encode('ascii', 'ignore').decode('ascii')
	f.write(comm)
	f.write('\n\n\n\n\n\n')
	time.sleep(60)
	#sleep time introduced so as to wait between page refreshes

f.close()
