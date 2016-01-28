# live-football-commentary
A python script that notifies the user of a chosen football match updates. Provides notifications containing real time football match commentary from the website - www.sportsmole.co.uk 
Notifications appear on the top right corner of the screen.
Also logs of the entire commentary are stored in a local file on the user's machine. 

For users-

1. Edit the football_comm_stream.py file and change the name of the output file to desired name
    f = open('Team1vsTeam2.txt','w')
 Change the 'Team1vsTeam2.txt' to any other desired output file name

2. Place the football_comm_stream.py file and the notifier.py file in the same directory.
3. Install the following for using the application -
  
  Beautiful Soup -
      $ apt-get install python-bs4
      (instructions - http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
  
  Json
      $ pip install simplejson
  
  libnotify (library for displaying notifications)
      $ sudo apt-get install python-gobject
      $ sudo apt-get install libnotify-bin
      $ sudo apt-get install libnotify-dev
