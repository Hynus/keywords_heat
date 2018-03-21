#coding:utf-8
"""
    @author:   sunyuhao
    @date:     2018.03.19
    @desc:     get keyword rank and keywords baidu index from API in 91cha
"""
import requests
import utils
keyword_rank_key = '408a2f2774f54c7a86bdf84719440fde'
keyword_baidu_index_key = '2de7cd043a6d46ba910aa611c23fcd94'

def get_keyword_rank_dict(host_url, keyword):
    keyword_rank_dict = {}
    req_url = 'http://api.91cha.com/bdsort?key=' + keyword_rank_key + '&host=' + host_url + '&wd=' + keyword
    resp = requests.get(req_url)
    if resp.json().get('state') != 1:
        keyword_rank_dict["state"] = 'failure'
        return keyword_rank_dict
    ret_host = resp.json().get('data').get('host')
    ret_keyword = resp.json().get('data').get('keyword')
    ret_rank = resp.json().get('data').get('sort')
    if ret_rank == u'50名以外':
        ret_rank = 'not in top 50'
    keyword_rank_dict['state'] = 'success'
    keyword_rank_dict['host'] = ret_host.encode('unicode-escape').decode('string_escape')
    keyword_rank_dict['keyword'] = ret_keyword.encode('unicode-escape').decode('string_escape')
    keyword_rank_dict['rank'] = ret_rank.encode('unicode-escape').decode('string_escape')
    return keyword_rank_dict

def get_keyword_baidu_index(keyword):
    keyword_baidu_index_dict = {}
    keywords = [keyword]
    req_url = 'http://api.91cha.com/index?key=' + keyword_baidu_index_key + '&kws=' + ','.join(keywords)
    resp = requests.get(req_url)
    if resp.json().get('state') != 1:
        keyword_baidu_index_dict['state'] = 'failure'
        return keyword_baidu_index_dict
    for item in resp.json().get('data'):
        keyword_baidu_index_dict['keyword'] = item.get('keyword').encode('unicode-escape').decode('string_escape')
        keyword_baidu_index_dict['allindex'] = utils.group(item.get('allindex'))
        keyword_baidu_index_dict['mobileindex'] = utils.group(item.get('mobileindex'))
        keyword_baidu_index_dict['so360index'] = utils.group(item.get('so360index'))
    keyword_baidu_index_dict['state'] = 'success'
    return keyword_baidu_index_dict

def run_main():
    keyword = 'arduino'
    keywords = ['arduino', 'arduinoUNO']
    search_host = 'www.amazon.de'
    keyword_rank_dict = get_keyword_rank_dict(search_host, keyword)
    keyword_baidu_index_dict = get_keyword_baidu_index(keywords)

if __name__ == "__main__":
    run_main()
