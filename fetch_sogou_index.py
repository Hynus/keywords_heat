# coding:utf-8
"""
    @author: sunyuhao
    @date:   2018.03.19
    @desc:   use selenium + PhantomJS to fetch keyword index in sogou
"""

from selenium import webdriver
from pyquery import PyQuery as pq
import json
import utils

phantomjs_path = '/Users/sunyh/Downloads/phantomjs/bin/phantomjs'
sogou_index_base_url = 'http://zhishu.sogou.com/index/searchHeat?'

def get_source_data(keyword):
    req_url = sogou_index_base_url + 'kwdNamesStr=' + keyword + '&timePeriodType=MONTH&dataType=SEARCH_ALL&queryType=INPUT'
    driver = webdriver.PhantomJS(phantomjs_path)
    driver.get(req_url)
    ori_source = pq(driver.page_source).html()
    data_needed_unicode = ori_source.split("\"infoList\":[")[1].split("],\"topPvDataList\"")[0]
    data_needed_str = data_needed_unicode.encode('unicode-escape').decode('string_escape')
    driver.quit()
    return json.loads(data_needed_str)

def judge_up_or_down(compare_str):
    if float(compare_str.split('%')[0]) > 0.0:
        return "up"
    elif float(compare_str.split('%')[0]) < 0.0:
        return "down"
    else:
        return "flat"


def get_sogou_index_dict(keyword):
    sogou_index_dict = {}
    source_dict = get_source_data(keyword)
    sogou_index_dict["keyword"] = keyword
    sogou_index_dict["total_search_index"] = utils.group(source_dict["avgPv"])
    sogou_index_dict["total_yoy"] = source_dict["ratioMonth"]
    sogou_index_dict["total_yoy_flag"] = judge_up_or_down(source_dict["ratioMonth"])
    sogou_index_dict["total_mom"] = source_dict["ratioChain"]
    sogou_index_dict["total_mom_flag"] = judge_up_or_down(source_dict["ratioChain"])
    sogou_index_dict["mobile_search_index"] = utils.group(source_dict["avgWapPv"])
    sogou_index_dict["mobile_yoy"] = source_dict["ratioWapMonth"]
    sogou_index_dict["mobile_yoy_flag"] = judge_up_or_down(source_dict["ratioWapMonth"])
    sogou_index_dict["mobile_mom"] = source_dict["ratioWapChain"]
    sogou_index_dict["mobile_mom_flag"] = judge_up_or_down(source_dict["ratioWapChain"])
    return sogou_index_dict

