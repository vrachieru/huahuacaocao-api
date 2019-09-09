import base64
import json
import requests

class HuaHuaCaoCao:

    _HOST = 'https://api.huahuacaocao.net'

    def __init__(self, region='CN', country='CN', lang='en', phone='samsung_s7_27', self.app_version='AS_3042_5.4.4'):
        '''
        Create a new client instance

        :param str region: region code
        :param str country: country code
        :param str lang: language
        :param str phone: phone model
        :param str app_version: emulated FlowerCare application version
        '''
        self.region = region
        self.country = country
        self.lang = lang
        self.phone = phone
        self.app_version = app_version

    def find_plant_by_alias(self, alias, offset=0, limit=20):
        '''
        Find plant by name

        :param str alias: partial of full name
        :param int offset: start offset for results
        :param int limit: max number of results returned
        :return: list of results
        '''
        response = self._call(
            path = '/plant/alias',
            data = {
                'lang': self.lang,
                'alias': alias,
                'count': offset,
                'limit': limit
            }
        )

        return response.json()

    def get_plant_details(self, plant_id):
        '''
        Get plant details

        :param str plant_id: plant id
        :return: plant details
        '''
        response = self._call(
            path = '/plant/detail',
            data = {
                'lang': self.lang,
                'pid': plant_id
            }
        )

        return response.json()['data']

    def _call(self, path, data):
        '''
        Make API call

        :param str path: resource apth
        :param dict data: request payload
        :return: response payload
        '''
        return requests.post(
            url = '%s/api/v2' % self._HOST,
            headers = {
                'Content-Type': 'application/json',
                'x-hhcc-region': self.region
            },
            data = json.dumps({
                'service': 'pkb',
                'method': 'GET',
                'path': path,
                'extra': {
                    'version': self.app_version,
                    'position': [0, 0],
                    'app_channel': 'google',
                    'zone': 2,
                    'country': self.country,
                    'lang': self.lang,
                    'phone': self.phone,
                    'model': ''
                },
                'data': data
            })
        )
