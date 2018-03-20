# coding:utf-8
"""
    @author:    sunyuhao
    @date:      2018.03.20
    @desc:      fetch keyword info from aizhan
"""

from pyquery import PyQuery as pq

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
    pc_heat = doc('tbody').find('td.center').eq(0).find('span.blue').text().split('/')[0].strip()
    mobile_heat = doc('tbody').find('td.center').eq(0).find('span.blue').text().split('/')[1].strip()
    long_tail_keyword_num = doc('tbody').find('td.center').eq(1).find('a.gray').text()
    include_num = doc('tbody').find('td.level').eq(0).text()
    keyword_info_aizhan['pc_heat'] = pc_heat
    keyword_info_aizhan['mobile_heat'] = mobile_heat
    keyword_info_aizhan['long_tail_keywords_num'] = long_tail_keyword_num
    keyword_info_aizhan['include_num'] = include_num
    return keyword_info_aizhan

def run_main():
    keyword = 'arduino'
    keyword_info_aizhan = get_keyword_info_from_aizhan(keyword)

if __name__ == "__main__":
    run_main()
