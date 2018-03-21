# coding: utf-8
"""
    @author:    sunyuhao
    @date:      2018.03.20
    @desc:      fetch the keyword search volumn from merchantwords.com
"""

from pyquery import PyQuery as pq
import utils

def get_countries_keyword_search_volumn(keyword):
    req_url = 'https://www.merchantwords.com/search/us/' + keyword + '/sort-highest'
    search_volumns = []
    search_volumn_dict = {}
    doc = pq(req_url)
    countries = doc('ul.nav.nav-stats').find('span').find('strong').text().encode('unicode-escape').decode('string_escape').split(' ')
    search_volumns_ori = doc('ul.nav.nav-stats').find('small').text().encode('unicode-escape').decode('string_escape').split(' ')
    for num in search_volumns_ori:
        remove_comma = num.replace(',', '')
        search_volumns.append(remove_comma)
    for i in xrange(len(countries)):
        search_volumn_dict[countries[i]] = utils.group(search_volumns[i])
    return search_volumn_dict

