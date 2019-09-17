# -*- coding: utf-8 -*-
'''
------------------------------------------------------------------------------------------------
Author: @arnby
Last Updated: 17 Sept 2019
Contact: Message @arnby at https://forum.c1games.com/
Copyright: CC0 - completely open to edit, share, etc
Short Description: 
This is a python script to download a replay file from its id
------------------------------------------------------------------------------------------------
README:
This script takes an input of one or several match ids, then download and save them
The command to run it is:
>py replay_downloader.py [LIST OF MATCH IDS]

Don't forget to change the needed variables!


'''
import sys
import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


"""
###########
Change the variables in this section
###########
"""

USERNAME = "my_git_username@gmail.com"
PASSWORD = "myGitPassword"
SAVE_DIRECTORY = "test/"


"""
###########
###########
"""


"""
fetch the replay file as a string from terminal API and save it
"""
def getMatchContent(match_id):
    try:
        url = 'https://terminal.c1games.com/api/game/replayexpanded/' + str(match_id)
        auth=(USERNAME, PASSWORD)
        r = requests.get(url,auth=auth,verify=False)
        f = open(SAVE_DIRECTORY + str(match_id) + '.replay','wb')
        f.write(r.content)
        f.close()
        print('match {} has been downloaded'.format(match_id))
    except Exception as e:
        print("\nerror trying to download match",match_id,":",e)
            


if __name__ == "__main__":
    args = sys.argv
    for match_id in args[1:]:
        getMatchContent(match_id)