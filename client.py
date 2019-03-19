
import json
import urllib.request
from urllib.parse import quote
from datetime import datetime

from .assets import AssetsAPI

class Communicator(AssetsAPI):

    _wait_before_expire = 5 ### seconds

    def __init__(self, base_url, client_id, client_secret):
        self._base_url = base_url
        self._client_id = client_id
        self._client_secret = client_secret


    @staticmethod
    def _to_suffix_params(prm):
        def serialize(value, separator=','):
            if   isinstance(value, dict):      return json.dumps(value).replace(' ', '')
            elif isinstance(value, list):      return separator.join(map(serialize, value))
            elif isinstance(value, str):       return value
            elif isinstance(value, datetime):  return value.strftime('%Y-%m-%dT%H:%M:%SZ')
            else:                              return str(value)

        return '&'.join([ '{}={}'.format(k, quote(serialize(prm[k]))) for k in prm.keys() if prm[k] is not None ])


    def _send_req(self, apipath, **kwargs):
        params = kwargs.get('params', {})
        if 'access_token' not in params.keys():
            params['access_token'] = self._generate_token()

        url = self._base_url + apipath.format(**kwargs) + '?' + self._to_suffix_params(params)
        subkeys = ('data', 'headers', 'origin_req_host', 'unverifiable', 'method')
        subargs = dict(filter(lambda x: x[0] in subkeys, kwargs.items()))
        if isinstance(subargs.get('data'), dict):
            subargs['data'] = json.dumps(subargs.get('data')).replace(' ', '')

        request = urllib.request.Request(url, **subargs)
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")

        return response_body


    def _generate_token(self):
        params = {
            'grant_type': 'client_credentials',
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'access_token': None,
        }
        res = json.loads(self._send_req('/identity/oauth/token', method='GET', params=params))

        if res['expires_in'] <= self._wait_before_expire:
           sleep(self._wait_before_expire+1)
           res = json.loads(self._send_req('/identity/oauth/token', method='GET', params=params))

        return res.get('access_token')

