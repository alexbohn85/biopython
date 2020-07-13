#!/usr/bin/env python
import requests
import sched, time

url = 'https://www.cic.gc.ca/english/information/where-to-give-biometrics.asp'
s = sched.scheduler(time.time, time.sleep)

loc_response = requests.get(url)

def check_changes(url):
    response = requests.get(url)
    if loc_response == response:
        print('They are the same')
    else
        print('They are different')

s.enter(4, 1, check_changes, url)
s.run()