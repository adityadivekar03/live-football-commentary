
#!/usr/bin/python
import time
import urllib2

from bs4 import BeautifulSoup
from urllib import urlopen

import json

from notifier import notifiersystem

f = open('Team1vsTeam2.txt','w')
user_url = raw_input('Enter the url of the site for live football commentary')
lag = int(raw_input("Enter in seconds the time between url refreshes"))

last_comm = "hello"
comm = "hello"

#ctr will record the number of times we get the same data on scraping a page. we scrape a page max 10 times with same data before exiting the program
ctr = 0

while True:

	#catching any error in opening the url
	try:
		urlopen(user_url)

	except IOError:
		print "Incorrect URL supplied. Please enter a correct URL by running the program again"
		exit()

	except urllib2.HTTPError, err:
	   if err.code == 404:
	       print "Page not found!"
	       exit()

	   elif err.code == 403:
	       print "Access denied!"
	       exit()
	   else:
	       print "Something happened! Error code", err.code
	       exit()

	except urllib2.URLError, err:
	    print "Some other error happened:", err.reason
	    exit()


	
	soccerpage = urlopen(user_url).read()
	soup = BeautifulSoup(soccerpage.decode('utf-8', 'ignore'))

	for commentary in soup.find_all(attrs={"class": "post"}):
		comm = commentary.get_text()
		comm = comm.encode('ascii', 'ignore').decode('ascii')
		
		#write the commentary to a file	
		f.write(comm)
		f.write('\n\n\n\n\n\n')
						

	if last_comm == "hello" or last_comm!=comm:
		#means that the program has scraped a new live commentary
		ctr = 0
		#make last_comm=comm
		last_comm = comm
		#call the notifier function from here with parameter 'last_comm'
		notifiersystem(last_comm)
	
	elif last_comm ==comm:
		ctr+=1
		if ctr>10:
			exit()
		continue
	time.sleep(lag)

f.close()
