import requests
import json
import sys

def acfun_login():
    url = 'https://id.app.acfun.cn/rest/web/login/signin'

    headers = {
        'Cookie': '_did=web_',
        'Content-Length': '63',
        'Sec-Ch-Ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Origin': 'https://www.acfun.cn',
        'Referer': 'https://www.acfun.cn/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }

    data = {
        'username': username,
        'password': password,
        'key': '',
        'captacha': '',
    }

    request = requests.post(url=url, headers=headers, data=data)
    cookies = requests.utils.dict_from_cookiejar(request.cookies)
    return cookies


def acfun_signin(cookies):
    cookies = json.dumps(cookies)
    cookies = cookies.replace("{", "").replace("}", "").replace("\"", "").replace(":", "=").replace(",", "; ")

    url_signin = 'https://www.acfun.cn/rest/pc-direct/user/signIn'
    headers_signin = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'cookie': cookies
    }

    request_signin = requests.get(url=url_signin, headers=headers_signin)
    return request_signin


def sendMessage(String):
    url = sys.argv[3]
    headers = {
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    }
    data = {
        'msgtype': 'text',
        'text': {'content': sys.argv[4]+'string'},
    }
    data = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=data)
    content = response.text
    print(content)


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    cookies = acfun_login()
    response_signin = acfun_signin(cookies)
    sendMessage(response_signin.text)
