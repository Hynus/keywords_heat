package from91Cha

type KeywordRankData struct {
	Host    string `json:"host"`
	Keyword string `json:"keyword"`
	Sort    string `json:"sort"`
}

type KeywordRank struct {
	State int64           `json:"state"`
	Msg   string          `json:"msg"`
	Data  KeywordRankData `json:"data"`
}

type KeywordBaiduIndexData struct {
	Keyword     string `json:"keyword"`
	AllIndex    int64  `json:"allindex"`
	MobileIndex int64  `json:"mobileindex"`
	So360Indx   int64  `json:"so360indx"`
}

type KeywordBaiduIndex struct {
	State int64                   `json:"state"`
	Msg   string                  `json:"msg"`
	Data  []KeywordBaiduIndexData `json:"data"`
}
