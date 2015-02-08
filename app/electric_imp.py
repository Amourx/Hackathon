import urllib2

IMP_URL = 'https://agent.electricimp.com/ldq9C8yJxKUP'

def romance():
    urllib2.urlopen(IMP_URL + '?level=2')

def lukewarm():
    urllib2.urlopen(IMP_URL + '?level=1')
