import json
import requests
import simplejson

class SimpleJson(object):

    def __init__(self):
        self.myjson = {}
        self.url = "https://github.com/timeline.json"
        #self.url1 = "https://www.google.com"
        self.post_data = {'username' : 'dkumar', 'password' : 'Pa55w0rd' }

    def tryTouchStone(self):

        resp = requests.get(self.url)
        #post_resp = requests.post(self.url,json=self.post_data)
        #print post_resp.text
        getJson =  resp.json()
        for k,v in getJson.iteritems():
            print k,v



        #print r.headers
        #c =  r.content
        #print json.loads(r.text)
        #print r.json()
        #print r.url
        #print r.text



s = SimpleJson()
s.tryTouchStone()

