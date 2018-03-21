# coding:utf-8

import fetch_from_91cha
import fetch_from_5118
import fetch_keyword_info_aizhan
import fetch_keyword_stat_keywordspy
import fetch_merchant_words
import fetch_sogou_index

def run_main():
    keyword = 'arduino'
    host_url = 'www.amazon.de'
    from_91cha_baidu_index_dict = fetch_from_91cha.get_keyword_baidu_index(keyword)
    from_91cha_keyword_rank_dict = fetch_from_91cha.get_keyword_rank_dict(host_url, keyword)
    from_5118_keyword_info_dict = fetch_from_5118.get_keyword_info_from5118(keyword)
    from_aizhan_keyword_info_dict = fetch_keyword_info_aizhan.get_keyword_info_from_aizhan(keyword)
    from_keywordspy_keyword_stat_dict = fetch_keyword_stat_keywordspy.get_keyword_statistics_keywordspy_dict(keyword)
    from_merchantwords_keyword_info_dict = fetch_merchant_words.get_countries_keyword_search_volumn(keyword)
    from_sogou_keyword_index_dict = fetch_sogou_index.get_sogou_index_dict(keyword)
    print '91cha_baidu_index=', from_91cha_baidu_index_dict
    print ""
    print '91cha_keyword_rank=', from_91cha_keyword_rank_dict
    print ""
    print '5118_keyword_info=', from_5118_keyword_info_dict
    print ""
    print "aizhan_keyword_info=", from_aizhan_keyword_info_dict
    print ""
    print 'keywordspy_info=', from_keywordspy_keyword_stat_dict
    print ""
    print 'merchantword_info=', from_merchantwords_keyword_info_dict
    print ""
    print 'sogou_index=', from_sogou_keyword_index_dict

if __name__ == "__main__":
    run_main()