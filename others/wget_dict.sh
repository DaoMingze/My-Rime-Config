#!/bin/bash
echo "请输入下载源代码，默认为github 1为github 2为ghproxy"
read num1
if [{$num1} == 1];then
	#github
	wget https://raw.githubusercontent.com/tumuyan/rime-melt/master/pinyin_simp_moe.dict.yaml
	wget https://raw.githubusercontent.com/tumuyan/rime-melt/master/pinyin_simp_wiki.dict.yaml
elif [{$num1} == 2];then
	# ghproxy
	wget https://ghproxy.com/https://raw.githubusercontent.com/tumuyan/rime-melt/master/pinyin_simp_moe.dict.yaml
	wget https://ghproxy.com/https://raw.githubusercontent.com/tumuyan/rime-melt/master/pinyin_simp_wiki.dict.yaml
else 
	echo "error"
fi
#mv -u pinyin_simp_moe.dict.yaml ./dict/pinyin_simp_moe.dict.yaml
#mv -u pinyin_simp_wiki.dict.yaml ./dict/pinyin_simp_wiki.dict.yaml