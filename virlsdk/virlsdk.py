#!/usr/bin/env python3
'''
Bunch of functions to abstract the VIRL STD APIs
'''
import requests


class Virl(object):

    def __init__(self, virl, username, password):
        self.virl = virl
        self.username = username
        self.password = password

    def _get(self, path):
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.auth = self.session.post(self.virl)
        response = self.session.get(self.virl + path)
        return(response)

    def _post(self, path, payload):
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.auth = self.session.post(self.virl)
        headers = {'X-Requested-With': 'Python requests', 'Content-type': \
                   'text/xml'}
        response = self.session.post(url = self.virl + path, data = payload, \
                                     headers = headers)
        return(response)

    def getsims(self):
        path = "/simengine/rest/list"
        return(self._get(path))

    def stopsim(self, simname):
        path = "/simengine/rest/stop/" + simname
        return(self._get(path))

    def startsim(self, payload):
        path = "/simengine/rest/launch"
        return(self._post(path, payload))
