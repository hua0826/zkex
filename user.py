import pytest
import requests


def test_user():
    headers = {
        "Access-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZGRyZXNzIjoiMHg3NzdhOWY5YzExZGRlNjE0ZDM2M2YyNmZkODhjMWVmZTQyYjg0MTEzIiwiZXhwaXJlZEF0IjoiMTY5NzI2MzU1NiIsImlkIjoxMjF9.iKVv2l_gfcfs-VmC-vLWhCY8eS4ibBT6pJJmumhzqXM"
    }

    session = requests.Session()
    session.trust_env = False
    resp = session.get(url="https://aws-test-1.zkex.com/api-v1/api/users/self", headers=headers)
    print(resp.status_code)
    # print(resp.json())

    assert resp.status_code == 200


if __name__ == '__main__':
    pytest.main(["-s", "user.py"])
