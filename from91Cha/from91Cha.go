package from91Cha

import (
	"encoding/json"
	"fmt"
	"github.com/bitly/go-simplejson"
	"io/ioutil"
	"net/http"
	"strings"
)

var (
	keywordRankKey       = "408a2f2774f54c7a86bdf84719440fde"
	keywordBaiduIndexKey = "2de7cd043a6d46ba910aa611c23fcd94"
)

func GetKeyWordRanks(hostUrl, keyword string) {
	var keywordRankInfo KeywordRank
	requestUrl := "http://api.91cha.com/bdsort?key=" + keywordRankKey +
		"&host=" + hostUrl + "&wd=" + keyword
	resp, err := http.Get(requestUrl)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	js, err := simplejson.NewJson([]byte(body))
	if err != nil {
		panic(err)
	}
	state, err := js.Get("state").Int()
	if err != nil {
		panic(err)
	}
	if state != 1 {
		fmt.Println("查询失败")
	} else {
		err = json.Unmarshal(body, &keywordRankInfo)
		if err != nil {
			panic(err)
		}
	}
	fmt.Println(keywordRankInfo)
}

func GetKeywordBaiduIndex(keywords []string) {
	var keywordBaiduIndex KeywordBaiduIndex
	requestUrl := "http://api.91cha.com/index?key=" + keywordBaiduIndexKey +
		"&kws=" + strings.Join(keywords, ",")
	resp, err := http.Get(requestUrl)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	js, err := simplejson.NewJson([]byte(body))
	if err != nil {
		panic(err)
	}
	state, err := js.Get("state").Int()
	if err != nil {
		panic(err)
	}
	if state != 1 {
		fmt.Println("查询失败")
	} else {
		err = json.Unmarshal(body, &keywordBaiduIndex)
		if err != nil {
			panic(err)
		}
	}
	fmt.Println(keywordBaiduIndex)
}
