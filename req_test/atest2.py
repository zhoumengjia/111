from req_test.atest_1 import TestInf
from commom.requests_util import RequestUtil


class TestInf2:
    def test_open_file(self):
        url = "https://hitpaw-test-api.afirstsoft.cn/app/uploadImage"
        header = {
            # 'Content-Type': 'application/json',
            'authorization': TestInf().token
        }
        data = {
            'files[]': open(r'D:\Users\Desktop\6500X6000.jpg', 'rb')
        }
        res = RequestUtil().send_all_request(method="post", url=url, files=data, headers=header)
        # res = self.sess.request("post", url=url, files=data, headers=header)
        # res = requests.post(url=url, files=data, headers=header)
        # print(res.json())


if __name__ == '__main__':
    testinf = TestInf2()
    testinf.test_open_file()