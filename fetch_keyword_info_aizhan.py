# coding:utf-8
"""
    @author:    sunyuhao
    @date:      2018.03.20
    @desc:      fetch keyword info from aizhan
"""

from pyquery import PyQuery as pq
import utils

def keyword2aizhai_urlstr(keyword):
    url_str = ''
    for i in xrange(len(keyword)):
        tmp = str(hex(ord(keyword[i]))).split('0x')[1]
        if len(tmp) == 2:
            url_str += 'n' + tmp
        else:
            url_str += tmp
    return url_str

def get_keyword_info_from_aizhan(keyword):
    keyword_info_aizhan = {}
    keyword_encoded = keyword2aizhai_urlstr(keyword)
    req_url = 'https://ci.aizhan.com/' + keyword_encoded + '/'
    doc = pq(req_url)
    pc_heat = doc('tbody').find('td.center').eq(0).find('span.blue').text().encode('unicode-escape').decode('string_escape').split('/')[0].strip()
    mobile_heat = doc('tbody').find('td.center').eq(0).find('span.blue').text().encode('unicode-escape').decode('string_escape').split('/')[1].strip()
    long_tail_keyword_num = doc('tbody').find('td.center').eq(1).find('a.gray').text().encode('unicode-escape').decode('string_escape')
    include_num = doc('tbody').find('td.level').eq(0).text()
    include_num = include_num.replace(u'万',u'0000').encode('unicode-escape').decode('string_escape')
    keyword_info_aizhan['pc_heat'] = utils.group(pc_heat)
    keyword_info_aizhan['mobile_heat'] = utils.group(mobile_heat)
    keyword_info_aizhan['long_tail_keywords_num'] = utils.group(long_tail_keyword_num)
    keyword_info_aizhan['include_num'] = utils.group(include_num)
    return keyword_info_aizhan

