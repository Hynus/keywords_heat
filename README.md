# 相关py文件输入输出说明
***
### fetch\_from\_91cha.py
<b> get\_keyword\_rank\_dict </b>--用来查询关键词在对应网站的搜索排名
<br>输入：host,&nbsp;keyword&nbsp;(其中host为要查询的网站)
<br>输出：dict,&nbsp;key值为：状态(成功与否)，排名(50名以内名次，或50名以外)，关键词，host
<br><b> get\_keyword\_baidu\_index </b>--用来查询关键词的百度指数
<br>输入：关键词列表（默认还是单个关键词）
<br>输出：dict,&nbsp;key值为：状态，指数信息（一个dict的列表）
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
列表中的dict的key为：移动端日均值，整体日均值，360指数，关键词
——————————————————————————————————————<br>
### fetch\_keyword\_info\_aizhan.py
<b>get\_keyword\_info\_from\_aizhan</b>--用来查询爱站给出的关键词热度结果
<br>输入：keyword
<br>输出：dict，key值为：PC端日热度，移动端日热度，长尾关键词数量，收录数
——————————————————————————————————————<br>
### fetch\_keyword\_stat\_keywordspy.py
<b>get\_keyword\_statistics\_keywordspy\_dict</b>--用来查询keywordspy给出的关键词统计结果
<br>输入：keyword
<br>输出：dict，key值为：PPC广告提供商数量，CPC价值，月均搜索量
——————————————————————————————————————<br>
### fetch\_merchant\_words.py
<b>get\_countries\_keyword\_search\_volumn</b>--用来查询关键词在各个国家（9国）亚马逊站点中的日均搜索量
<br>输入：keyword
<br>输出：dict，key值为：US，UK，CA，DE，FR，ES，IT，AU，JP的日均搜索量
——————————————————————————————————————<br>
### fetch\_sogou\_index.py
<b>get\_sogou\_index\_dict</b>--用来查询关键词的搜狗指数
<br>输入：keyword
<br>输出：dict，key值为：关键词，整体搜索指数，整体同比，整体环比，整体上升（下降），移动搜索指数，移动同比，移动环比，移动上升（下降）【此搜索指数为从一个月前到今天的搜索量的加权平均值】
