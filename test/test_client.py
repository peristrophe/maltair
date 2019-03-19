import helper
import maltair
import unittest

import os

from urllib.parse import unquote
from datetime import datetime, timedelta, timezone
from pprint import pprint

jst = timezone(timedelta(hours=9), 'JST')

class ClientTest(unittest.TestCase):

    def setUp(self):
        auth_data = {
            'base_url': os.getenv('MARKETO_BASE_URL'),
            'client_id': os.getenv('MARKETO_CLIENT_ID'),
            'client_secret': os.getenv('MARKETO_CLIENT_SECRET'),
        }

        self.client = maltair.Client(**auth_data)


    def tearDown(self):
        if hasattr(self, 'res'):
            pprint(self.res)


    def test_siffux_convert(self):
        start_date = datetime.strptime('2019/03/11 22:33:44.555', '%Y/%m/%d %H:%M:%S.%f').replace(tzinfo=jst)
        payloads = {'attr': 123}
        params = {
            'type': 'test',
            'start_date': start_date,
            'payloads': payloads,
            'ignore_value': None,
            'page': 12,
        }

        self.res = self.client._to_suffix_params(params)

        # it expected return like below, but don't ensured params order due to dict
        # 'type=test&start_date=2019-03-11T22%3A33%3A44Z&payloads=%7B%22attr%22%3A123%7D&page=12'
        for prm in self.res.split('&'):
            self.assertTrue(unquote(prm) in ('type=test', 'start_date=2019-03-11T22:33:44Z', 'payloads={"attr":123}', 'page=12'))

        self.assertEqual(len(self.res.split('&')), 4)


    def test_generate_token(self):
        self.res = self.client._generate_token()
        self.assertTrue(isinstance(self.res, str))


if __name__ == '__main__':
    unittest.main()
