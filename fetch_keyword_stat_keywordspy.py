# coding: utf-8
"""
    @author:    sunyuhao
    @date:      2018.03.20
    @desc:      fetch keyword basic stat info from keywordspy.com
"""

from pyquery import PyQuery as pq
import utils

def get_keyword_statistics_keywordspy_dict(keyword):
    req_url = 'http://www.keywordspy.com/research/search.aspx?q=' + keyword + '&tab=keyword-overview'
    keyword_statistics_keywordspy_dict = {}
    doc = pq(req_url)
    base_table_td = doc('div.panel').eq(0).find('table.data').find('tr').find('td')
    ppc_adver = base_table_td.eq(0).text().encode('unicode-escape').decode('string_escape').split(':')[0]
    ppc_adver_num = base_table_td.eq(1).text().encode('unicode-escape').decode('string_escape')
    cpc = base_table_td.eq(3).text().encode('unicode-escape').decode('string_escape').split(':')[0]
    cpc_num = base_table_td.eq(4).text().encode('unicode-escape').decode('string_escape')
    search_volum = base_table_td.eq(6).text().encode('unicode-escape').decode('string_escape').split(':')[0] + '(month_avg)'
    search_volum_num = base_table_td.eq(7).text().encode('unicode-escape').decode('string_escape').split('/')[0].replace(',', '')
    keyword_statistics_keywordspy_dict[ppc_adver] = utils.group(ppc_adver_num)
    keyword_statistics_keywordspy_dict[cpc] = cpc_num
    keyword_statistics_keywordspy_dict[search_volum] = utils.group(search_volum_num)
    return keyword_statistics_keywordspy_dict
