# coding: utf-8
from pyquery import PyQuery as pq
import requests


def handle_total_result_str(country, desc):
    str_list = desc.split(' ')
    if country == 'fr':
        if str_list[3].split(u'\xa0')[0].isdigit() and str_list[3].split(u'\xa0')[1].isdigit():
            return str_list[3].split(u'\xa0')[0] + ',' + str_list[3].split(u'\xa0')[1]
        elif str_list[0].split(u'\xa0')[0].isdigit():
            return str_list[0].split(u'\xa0')[0]
    if str_list[4].replace('.', '').isdigit():
        return str_list[4].replace('.', ',')
    elif str_list[3].replace(',','').isdigit():
        return str_list[3]
    elif str_list[2].isdigit():
        return str_list[2]
    elif str_list[0].isdigit():
        return str_list[0]

def get_total_result_count(keyword, country):
    if country == 'us':
        country = 'com'
    elif country == 'uk':
        country = 'co.uk'
    req_url = 'https://www.amazon.' + country + '/s/ref=sr_pg_1?url=search-alias%3Daps&field-keywords=' + keyword.replace(' ', '+') + '&rh=i%3Aaps%2Ck%3A' + keyword.replace(' ', '+')
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.amazon.' + country,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    resp = requests.get(url=req_url, headers=headers)
    doc = pq(resp.content)
    total_desc_str = doc('span#s-result-count').text()
    return handle_total_result_str(country, total_desc_str)

def get_pdt_nums_in_amz(keyword, country):
    pdt_num_dict = {}
    pdt_num_dict[country] = get_total_result_count(keyword, country)
    return pdt_num_dict