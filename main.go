package main

import (
	"keywords_heats/from91Cha"
)

func main() {
	kw := "arduino"
	host := "www.amazon.de"
	kws := []string{"arduino"}
	from91Cha.GetKeyWordRanks(host, kw)
	from91Cha.GetKeywordBaiduIndex(kws)
}
