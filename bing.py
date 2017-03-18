from urllib.parse import urlencode

import math
from pyquery import PyQuery as pq
import requests

from proxy import get_proxy

headers = {
    'Host': 'cn.bing.com',
    'Referer': 'http://cn.bing.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie': 'SRCHHPGUSR=CW=1231&CH=397&DPR=2&UTC=480&NEWWND=1&NRSLT=50&SRCHLANG=&AS=1&NNT=1&HIS=1&HAP=0'
}


def get_result(keyword, page):
    data = {
        'q': keyword,
        'first': (page - 1) * 50,
    }
    proxy = get_proxy()
    proxies = {
        'https': 'https://' + proxy,
        'http': 'http://' + proxy
    }
    url = 'http://cn.bing.com/search?' + urlencode(data)
    print(url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.status_code == 200:
        html = response.text
        doc = pq(html)
        results = doc('li.b_algo').items()
        for result in results:
            title = result.find('h2').text()
            href = result.find('h2 a').attr('href')
            abstract = result.find('.b_caption').text()
            url = result.find('cite').text().replace(' ', '')
            yield dict({
                'title': title,
                'href': href,
                'abstract': abstract,
                'url': url,
            })


def get_request(keyword, total):
    total_page = math.ceil(total / 50)
    total_result = []
    for i in range(1, total_page + 2):
        results = get_result(keyword, i)
        for result in results:
            total_result.append(result)

    if (len(total_result) > total):
        return {
            'length': total,
            'content': total_result[0: total]
        }
    else:
        return {
            'length': len(total_result),
            'content': total_result
        }


if __name__ == '__main__':
    print(get_request('nba', 120))
