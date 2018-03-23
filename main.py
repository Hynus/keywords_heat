# coding:utf-8

import fetch_from_91cha
import fetch_from_5118
import fetch_keyword_info_aizhan
import fetch_keyword_stat_keywordspy
import fetch_merchant_words
import fetch_sogou_index
import from_amz
import utils

def get_final_heat(keyword, country):
    if country == 'uk':
        my_host = 'www.amazon.' + 'co.uk'
    elif country == 'us':
        my_host = 'www.amazon.' + 'com'
    else:
        my_host = 'www.amazon.' + country
    amz_info = {}
    search_index_dict = {}
    other_heat_info = {}
    pdt_num_amz = {}
    search_total_index = 0
    search_mobile_index = 0
    pdt_num_amz = from_amz.get_pdt_nums_in_amz(keyword, country)
    from_91cha_rank_dict = fetch_from_91cha.get_keyword_rank_dict(my_host, keyword)
    from_91cha_baidu_index_dict = fetch_from_91cha.get_keyword_baidu_index(keyword)
    from_5118_keyword_info_dict = fetch_from_5118.get_keyword_info_from5118(keyword)
    from_aizhan_keyword_info_dict = fetch_keyword_info_aizhan.get_keyword_info_from_aizhan(keyword)
    from_keywordspy_keyword_stat_dict = fetch_keyword_stat_keywordspy.get_keyword_statistics_keywordspy_dict(keyword)
    from_merchantwords_keyword_info_dict = fetch_merchant_words.get_countries_keyword_search_volumn(keyword)
    from_sogou_keyword_index_dict = fetch_sogou_index.get_sogou_index_dict(keyword)
    country_search = from_merchantwords_keyword_info_dict[country.upper()]
    if len(country_search) == 0:
        country_search = 'NaN'
    amz_info['search_vol'] = country_search
    amz_info['pdt_nums'] = 'about ' + str(pdt_num_amz[country])
    if from_91cha_baidu_index_dict != None and from_5118_keyword_info_dict != None:
        search_total_index = (utils.comma_str_to_int(from_sogou_keyword_index_dict['total_search_index']) +
                              utils.comma_str_to_int(from_91cha_baidu_index_dict['allindex']) +
                              utils.comma_str_to_int(from_5118_keyword_info_dict['baidu_index']) +
                              utils.comma_str_to_int(from_aizhan_keyword_info_dict['pc_heat']) +
                              utils.comma_str_to_int(from_aizhan_keyword_info_dict['mobile_heat'])) / 4
        search_mobile_index = (utils.comma_str_to_int(from_sogou_keyword_index_dict['mobile_search_index']) +
                               utils.comma_str_to_int(from_91cha_baidu_index_dict['mobileindex']) +
                               utils.comma_str_to_int(from_5118_keyword_info_dict['baidu_mobile_index']) +
                               utils.comma_str_to_int(from_aizhan_keyword_info_dict['mobile_heat'])) / 4
    elif from_91cha_baidu_index_dict == None:
        search_total_index = (utils.comma_str_to_int(from_sogou_keyword_index_dict['total_search_index']) +
                              utils.comma_str_to_int(from_5118_keyword_info_dict['baidu_index']) +
                              utils.comma_str_to_int(from_aizhan_keyword_info_dict['pc_heat']) +
                              utils.comma_str_to_int(from_aizhan_keyword_info_dict['mobile_heat'])) / 3
        search_mobile_index = (utils.comma_str_to_int(from_sogou_keyword_index_dict['mobile_search_index']) +
                               utils.comma_str_to_int(from_5118_keyword_info_dict['baidu_mobile_index']) +
                               utils.comma_str_to_int(from_aizhan_keyword_info_dict['mobile_heat'])) / 3
    elif from_5118_keyword_info_dict == None:
        search_total_index = (utils.comma_str_to_int(from_sogou_keyword_index_dict['total_search_index']) +
                              utils.comma_str_to_int(from_91cha_baidu_index_dict['allindex']) +
                              utils.comma_str_to_int(from_aizhan_keyword_info_dict['pc_heat']) +
                              utils.comma_str_to_int(from_aizhan_keyword_info_dict['mobile_heat'])) / 3
        search_mobile_index = (utils.comma_str_to_int(from_sogou_keyword_index_dict['mobile_search_index']) +
                               utils.comma_str_to_int(from_91cha_baidu_index_dict['mobileindex']) +
                               utils.comma_str_to_int(from_aizhan_keyword_info_dict['mobile_heat'])) / 3
    search_index_dict['total_index'] = utils.group(search_total_index)
    search_index_dict['mobile_index'] = utils.group(search_mobile_index)
    search_index_dict['total_yoy'] = from_sogou_keyword_index_dict['total_yoy']
    search_index_dict['total_mom'] = from_sogou_keyword_index_dict['total_mom']
    search_index_dict['mobile_yoy'] = from_sogou_keyword_index_dict['mobile_yoy']
    search_index_dict['mobile_mom'] = from_sogou_keyword_index_dict['mobile_mom']
    if from_5118_keyword_info_dict != None :
        other_heat_info['bid_company_num'] = from_5118_keyword_info_dict['bidding_company_num']
        other_heat_info['long_tail_num'] = from_5118_keyword_info_dict['long_tail_keywords_num']
        other_heat_info['est_comp'] = from_5118_keyword_info_dict['competitiveness']
    other_heat_info['PPC_advers'] = from_keywordspy_keyword_stat_dict['PPC Advertisers']
    other_heat_info['CPC'] = from_keywordspy_keyword_stat_dict['CPC']
    return amz_info, search_index_dict, other_heat_info



def run_main():
    keyword = 'arduino'
    country = 'de'
    aa, bb, cc = get_final_heat(keyword, country)
    print aa
    print ""
    print bb
    print ""
    print cc
    print ""


if __name__ == "__main__":
    run_main()