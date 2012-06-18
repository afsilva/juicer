# -*- coding: utf-8 -*-
import Juicer.utils
import JuicerAdmin
import json
import requests


class JuicerAdmin(object):
    def __init__(self, args):
        self.args = args
        self.envs = self.args.envs

        connect_params = Juicer.utils.get_login_info(self.args)

        self.base_url = connect_params['base_url']
        self.auth = (connect_params['username'], connect_params['password'])
        self.headers = {'content-type': 'application/json'}

    def put(self, url="", data={}):
        # Returns (response, content)
        return requests.put(url, json.dumps(data), auth=self.auth,
                            headers=self.headers, verify=False)

    def get(self, url=""):
        # Returns (response, content)
        return requests.get(url, self.auth, self.headers)

    def create_repo(self, query='/repositories/'):
        data = {'name': self.args.name,
                'arch': 'noarch'}
        for env in self.envs:
            data['relative_path'] = '/%s/%s/' % (env, self.args.name)
            data['id'] = '-'.join([self.args.name, env])
            url = self.base_url + query
            r = self.put(url, data)
