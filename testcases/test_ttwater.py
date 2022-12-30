import jsonpath
import pytest
import requests
from commom.requests_util import RequestUtil
from commom.yaml_util import write_yaml, read_yaml


class TestInf:
    def __init__(self):
        self.token = ''
        self.sess = requests.session()

    def test_get_token(self):
        url = "https://hitpaw-test-api.afirstsoft.cn/api/v2/sessions"
        data = {
            'email': 'zhoumengjia@tenorshare.cn',
            'password': 'zhou123456'
        }
        res = self.sess.request("post",url=url, data=data)
        self.token = res.json()['data']['authorization']

    def test_get_ttwater(self):
        urls = "https://hitpaw-test-api.afirstsoft.cn/api/v2/ttWatermarkRemove"
        data = {
            'video_url':'https://www.tiktok.com/@cedricgrolet/video/7175939915048373510?is_from_webapp=1&sender_device=pc'
        }
        header = {
            'Authorization': self.token
        }
        res = self.sess.request("post", url=urls, data=data, headers=header)
        print(res.json())


if __name__ == '__main__':
    testinf = TestInf()
    testinf.test_get_token()
    testinf.test_get_ttwater()

