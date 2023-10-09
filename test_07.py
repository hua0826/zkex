import pytest
import requests


def test_get_kline():
#     kline_url = "https://aws-test-1.zkex.com/api-v1/api/products/wETH-USD/candles?granularity=60"
#     kline = requests.get(kline_url, verify=False).json()
#     return kline

    session = requests.Session()
    session.trust_env = False
    resp = session.get(url="https://aws-test-1.zkex.com/api-v1/api/products/wETH-USD/candles?granularity=60")
    print(resp.status_code)
    # print(resp.json())

    # assert resp.status_code == 200

if __name__ == '__main__':
    pytest.main(["-s","test_07.py"])