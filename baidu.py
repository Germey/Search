from urllib.parse import urlencode

import math
from pyquery import PyQuery as pq
import requests

from proxy import get_proxy

keyword = 'nba'

headers = {
    'Host': 'www.baidu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def get_result(keyword, page):
    data = {
        'wd': keyword,
        'rn': 50,
        'pn': (page - 1) * 50
    }
    proxy = get_proxy()
    proxies = {
        'https': 'https://' + proxy,
        'http': 'http://' + proxy
    }
    url = 'https://www.baidu.com/s?' + urlencode(data)
    print(url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.status_code == 200:
        html = response.text
        doc = pq(html)
        results = doc('.result.c-container').items()
        for result in results:
            title = result.find('h3.t').text()
            href = result.find('h3.t a').attr('href')
            abstract = result.find('.c-abstract').text()
            url = result.find('.c-showurl').text().replace(' ', '')
            snapshot = result.find('.m').attr('href')
            yield dict({
                'title': title,
                'href': href,
                'abstract': abstract,
                'url': url,
                'snapshot': snapshot
            })


def get_request(keyword, total):
    total_page = math.ceil(total / 50)
    total_result = []
    for i in range(1, total_page + 1):
        results = get_result(keyword, i)
        for result in results:
            total_result.append(result)

    if (len(total_result) > total):
        return (total_result[0: total])
    else:
        return total_result


if __name__ == '__main__':
    print(get_request('nba', 120))