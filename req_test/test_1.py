import jsonpath
import pytest
import requests
from commom.requests_util import RequestUtil
from commom.yaml_util import write_yaml, read_yaml


class TestInf:
    # token = ''
    # 原因是pytest中不能出现__init__方法
    # def __init__(self):
    #     self.token = ''
        # self.sess = requests.session()

    # def setup_class(self):
    #     print("\n在每个类执行前的初始化工作：比如：创建日志对象、创建数据库连接、创建接口请求对象")
    #
    # def setup(self):
    #     print("\n执行测试用例之前初始化：打开浏览器，加载网页")
    #
    # def teardown(self):
    #     print("\n执行测试用例后的扫尾工作：关闭浏览器")
    #
    # def teardown_class(self):
    #     print("\n在每个类执行后的扫尾工作：比如：销毁日志对象、断开数据库连接、销毁接口请求对象")

    @pytest.mark.smoke
    def test_get_login(self,base_url):
        url = base_url + "/api/v2/sessions"
        data = {
            'email': 'zhoumengjia@tenorshare.cn',
            'password': 'zhou123456'
        }
        res = RequestUtil().send_all_request(method="post",url=url, data=data)
        # res = self.sess.request("post",url=url, data=data)
        # res = requests.post(url=url, data=data)
        # lis = jsonpath.jsonpath(res.json(),"$.data.authorization")
        # TestInf.token = res.json()['data']['authorization']
        write_yaml({"access_token": res.json()['data']['authorization']})
        # print(lis[0])
        # print(TestInf.token)

    def test_get_token(self,my_fixture):
        urls = "https://hitpaw-test-api.afirstsoft.cn/api/v2/ttWatermarkRemove"
        data = {
            'video_url':'https://www.tiktok.com/@cedricgrolet/video/7175939915048373510?is_from_webapp=1&sender_device=pc'
        }
        header = {
            'Authorization': read_yaml("access_token")
        }

        res = RequestUtil().send_all_request(method="post", url=urls, data=data, headers=header)
        # res = self.sess.request("post", url=urls, data=data, headers=header)
        # res = requests.post(url=urls,data=data,headers=header)
        # print(res.json())

    def test_open_file(self):
        url = "https://hitpaw-test-api.afirstsoft.cn/app/uploadImage"
        header = {
            # 'Content-Type': 'application/json',
            'authorization': read_yaml("access_token")
        }
        data = {
            'files[]': open(r'D:\Users\Desktop\6500X6000.jpg', 'rb')
        }
        res = RequestUtil().send_all_request(method="post", url=url, files=data, headers=header)
        # res = self.sess.request("post", url=url, files=data, headers=header)
        # res = requests.post(url=url, files=data, headers=header)
        # print(res.json())


if __name__ == '__main__':
    testinf = TestInf()
    testinf.test_get_login()
    testinf.test_get_token()
    testinf.test_open_file()
    # TestInf2.test_open_file()
