import requests

# 公共方法
class RequestUtil:
    def __init__(self):
        self.token = ''
        self.sess = requests.session()

    # 统一请求封装
    def send_all_request(self, **kwargs):
        res = self.sess.request(**kwargs)
        print(res.json())
        return res