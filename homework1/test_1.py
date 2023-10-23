import pytest
import requests
import yaml

S = requests.Session()

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_create_post(login):
    url=data['address_post']
    headers={'X-Auth-Token': login}
    d={'title': data['title'], 
       'description': data['description'], 
       'content': data['content']
       }
   
    res = S.post(url, headers=headers, data=d)
    assert str(res) == '<Response [200]>', "Новый пост не создан"


def test_check_description(login, get_description):
    url = data['url_post']
    headers={'X-Auth-Token': login}
    res = S.get(url=url, headers=headers).json()['data']
    print(res)
    lst = [x['description'] for x in res]
    assert get_description in lst, "Новый пост не найден"        

if __name__ == "__main__":
    pytest.main(["-vv"])