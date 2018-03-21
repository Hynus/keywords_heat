# coding: utf-8
"""
    @author:    sunyuhao
    @date:      2018.03.21
    @desc:      fetch the keyword info from 5118.com(login requested, so I used cookie with the cookie)
"""

from pyquery import PyQuery as pq
import requests
import utils

def get_keyword_info_from5118(keyword):
    keyword_info5118_dict = {}
    req_url = 'http://www.5118.com/seo/words/' + keyword.lower()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'ASP.NET_SessionId=ysepsthbcg4tnf53dcehyauz; __cfduid=d535b8eeea1bda41b00e9052c24c5a7321521607634; Hm_lvt_f3b3086e3d9a7a0a65c711de523251a6=1521607421,1521609495,1521609888,1521609942; uid=Mp3cF7xfqXQk1so8LfMn4bEX%2fJGufjO%2bbOTMceGfoiE%3d; Hm_lpvt_f3b3086e3d9a7a0a65c711de523251a6=1521610136',
        'Host': 'www.5118.com',
        'Referer': 'http://www.5118.com/seo/words/' + keyword,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    resp = requests.get(url=req_url, headers=headers)
    doc = pq(resp.content)
    for i in xrange(5):
        keyword_tuni = doc('dd.col3-8.word.select').find('span.hoverToHide')
        if keyword_tuni.eq(i).text().encode('unicode-escape').decode('string_escape').upper() == keyword.upper():
            tmp_record = doc('div.Fn-ui-list.dig-list').find('dl').eq(i+1).text().encode('unicode-escape').decode('string_escape').split('\n')
            keyword_info5118_dict['keyword'] = keyword
            keyword_info5118_dict['search_result_num'] = utils.group(tmp_record[6])
            keyword_info5118_dict['bidding_company_num'] = utils.group(tmp_record[7])
            keyword_info5118_dict['long_tail_keywords_num'] = utils.group(tmp_record[8])
            keyword_info5118_dict['baidu_index'] = utils.group(tmp_record[9])
            keyword_info5118_dict['baidu_mobile_index'] = utils.group(tmp_record[10])
            keyword_info5118_dict['360index'] = utils.group(tmp_record[11])
            keyword_info5118_dict['baidu_pc_search_vol'] = utils.group(tmp_record[12])
            keyword_info5118_dict['baidu_mobile_search_vol'] = utils.group(tmp_record[13])
            keyword_info5118_dict['competitiveness'] = tmp_record[14]
    return keyword_info5118_dict

