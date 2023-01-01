import pytest
from commom.requests_util import RequestUtil
from commom.yaml_util import write_yaml, read_yaml, read_yaml_testcase


class TestTwater:
    @pytest.mark.parametrize("caseinfo", read_yaml_testcase("data/test_get_token.yaml"))
    def test_get_token(self,caseinfo,base_url):
        print(caseinfo["featrue"])
        print(caseinfo["title"])
        url = base_url + caseinfo["request"]["url"]
        data = caseinfo["request"]["data"]
        res = RequestUtil().send_all_request(method=caseinfo["request"]["method"], url=url, data=data)
        write_yaml({"access_token": res.json()['data']['authorization']})

    @pytest.mark.parametrize("caseinfo", read_yaml_testcase("data/test_get_ttwater.yaml"))
    def test_get_ttwater(self, caseinfo,my_fixture):
        print(caseinfo["featrue"])
        print(caseinfo["title"])
        urls = caseinfo["request"]["url"]
        data = caseinfo["request"]["data"]
        header = {
            'Authorization': read_yaml("access_token")
        }
        res = RequestUtil().send_all_request(method=caseinfo["request"]["method"], url=urls, data=data, headers=header)

#
# if __name__ == '__main__':
#     testinf = TestTwater()
#     testinf.test_get_token()
#     testinf.test_get_ttwater()
