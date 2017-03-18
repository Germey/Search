import requests

def get_proxy():
    url = 'http://proxy.cuiqingcai.com'
    proxy = requests.get(url, auth=('admin', '123456')).text
    return proxy