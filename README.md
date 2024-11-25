---
title: My-Rime-Config
---

<div align="center">

# My-Rime-Config

![GitHub repo size](https://img.shields.io/github/repo-size/daomingze/My-Rime-Config)

我的 RIME 输入法配置，皮肤、词典、输入方案、配置

[CN](README.md) | ~~[EN](README_en.md)~~

**输入法**|排版

</div>

## 当前状态

1. 英文说明尚未更新（the README_en.md is outdated.）
2. 目前**完全**使用[雾凇拼音](https://github.com/iDvel/rime-ice)，部分配置参考[someok/rime-ice-custom](https://github.com/someok/rime-ice-custom)
3. 通过子模块引入[融合拼音](https://github.com/tumuyan/rime-melt)、[雾凇拼音](https://github.com/iDvel/rime-ice)、[白霜词库](https://github.com/gaboolic/rime-frost)
4. 参考 [rimerc](https://github.com/Bambooin/rimerc) 设置 release。
5. 考虑使用脚本优化[同文（Trime）输入法](https://github.com/osfans/trime/releases)的主题。

## 简介

文字输入需求：汉语（现代汉语和古代汉语）、英文（常用词汇）、特殊符号。

输入方案和词典来源：

```bash
mkdir raw
cd raw
git submodule add --depth=1 https://github.com/tumuyan/rime-melt raw/rime-melt
git submodule add --depth=1 https://github.com/iDvel/rime-ice raw/rime-ice
git submodule add --depth=1 https://github.com/gaboolic/rime-frost raw/rime-frost
```

部分配置参考 [rime-ice-custom](https://github.com/someok/rime-ice-custom)

目前尝试支持：

|OS|软件|版本|
|---|---|:---:|
|Windows 11|[小狼毫 weasel](https://github.com/rime/weasel/releases)|![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/rime/weasel?include_prereleases)|
|Linux（Debian stable）|[fcitx5-rime](https://github.com/fcitx/fcitx5-rime)|![Debian package](https://img.shields.io/debian/v/fcitx5-rime)|
|Android 13|[同文（Trime）输入法](https://github.com/osfans/trime/releases)|![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/osfans/trime?include_prereleases)|

[^1]: 国务院关于公布《通用规范汉字表》的通知：国发〔2013〕23 号

[TOC]

## 需求

### 输入的上限：辞典（dictionaries）

字符、t 编码、t 频率（非负整数）

#### 字典

##### 字形

简体字或言规范字，以 [《通用规范汉字表》](http://www.gov.cn/zhengce/content/2013-08/19/content_1289.htm)8105 字 [^1] 为标准。在此之上则有《GB 18030-2022 信息技术 中文编码字符集》的字样，约 8 万 7 千字。

广义上的汉字，或者 [Unihan](http://www.unicode.org/reports/tr38/)（Unicode 中的 CJK Unified Ideographs 子集）包括传承字（正）、异体字（包含但不限于俗体）、简化规范字（简化及类推简化的一个子集）、海外汉字（以日本和制汉字为典型）等来源。当前的 Unicode 15 中 CJK Unified（20992 字）、CJK Ext-A（6592 字）、CJK Ext-B（42720 字）、CJK Ext-C（4154 字）、CJK Ext-D（222 字）、CJK Ext-E（5762 字）、CJK Ext-F（7473 字）、CJK Ext-G（4939 字）、CJK Ext-H（4192 字），合计 97046 字。此外还有兼容区（472 字）和兼容补充区（542 字），共计 98060 字。而以目前笔者所知最大的汉字字库“全宋体”来看，广义汉字约有 18 万余。

因此有，全宋体（18 万）>Unihan（9 万 7 千）>GB18030（8 万 7 千）。

##### 字音

但是，正如汉语存在方言上的有音无字一样，Unicode 也存在为数不少的有字无音。[ZengYL](https://www.zengyulin.cn) 提供了一个 [将 Unicode 可读性标注转换为词库的方法](https://github.com/iDvel/rime-ice/issues/116)，[iDvel](https://github.com/iDvel) 处理后得到了 41448 字的普通话标注。

多音字定音，对于字典而言，有其音就尽量有其字，而无须在意该字义的词频。

##### 字义

而字典可释义大概在 10 万字左右，其中有大量的异体、同形、避讳缺笔等字形。据 WFG 先生统计，[台湾“教育部”异体字字典](https://dict.variants.moe.edu.tw/) 合并同形字后实际收字 96800 字，略少于《汉字海》。

在字形语义转字符问题（如输入“四个又”，输出“叕”；`other.dict.yaml`、`emoji.txt`）上，雾凇拼音做了很多有价值的工作。但考虑到基本字典部分是语法严格的，因此字形语义转字符单列。

##### 字频

在现代汉语领域，常用的是 8105 字，但缺乏相关语料字频统计。而以 [邢红兵等在 2019 年公开的 25 亿字语料汉字字频表](https://faculty.blcu.edu.cn/xinghb/zh_CN/article/167473/content/1437.htm) 来看，14975 字覆盖了约 19 亿字的现代汉语字频。因此基本字频可以根据 14975 字确定。[雾凇拼音](https://github.com/iDvel/rime-ice) 的`8105.dict.yaml`即是采用了 UTF-8、拼音、邢红兵等汉字字频的通用规范汉字表。

- [国家语委现代汉语平衡语料库](http://corpus.zhonghuayuwen.org/) 字符 19455328 个（含汉字、字母、数字、标点等），

古代汉语方面，有书同文公司的古籍汉字字频统计，另有诸多自行统计。

- [古典中文語料庫](https://github.com/rime-aca/corpus)

##### 字典处理小结

1. 以`Unihan code`为字符字形基础，以`Unihan Readings`为字符读音基础，以邢红兵等 25 亿语料字频表和古籍汉字字频统计为字频基础。
2. 考虑到使用情景，以现代汉语：古代汉语=7:3 的比例关系重构字频。
3. 对于有字无音的字形，根据字义和其他参考进行赋音或编码。
4. 对于多音字，重复列出。

因此，字典有

1. unihan_a：有字频且有字音的 14975 字
2. unihan_b：有字频无字音，但可以通过其他方式标注的（其他方言或语言、字形语义、寓意）
3. unihan_c：Unihan 中无字频，但有本方案主要标注方式的（音码如拼音、形码如字海两分等）
4. unihan_d：无字频，通过其他方式标注的。

#### 词语

- 常用词双音节词：
- 成语：搜狗细胞词库
- 俗语
- 其他多音节词
  - 流行
  - 百科词头：wiki、moe

雾凇拼音的词库倾向语用，融合拼音的词库倾向语义。就更新和实用而言，具有专业词库要求的最好选用融合拼音词库方式，通过不同类型的“挂载”实现词库需求；而日常输入方面，雾凇拼音不断调整的词库词频为便捷、省心的输入提供了方便（8105+base）。

#### 语句

- 古诗词
- 文章语句

## 设计

### 输入方案

为了方便拉取合并更新，自定义事项使用`patch`。

功能上，微机（PC）以`微软拼音`为参考，移动终端以`Gboard`（谷歌 Gboard 输入法）为参考，结合 Rime 的各种方案组合如下

- 状态栏功能
  - [x] 中英、中英标点、全半角切换，Rime 自带
  - [x] 简繁转换，opencc 实现
  - [x] 表情及符号面板，仅 Trime（同文风主题、流体键盘）
- 输入方案相关
  - [x] 模糊拼音，袖珍简化字拼音实现
  - [ ] 双拼，理想中的简易双拼是注音输入
- 输入操作
  - [ ] 候选字翻页，融合拼音由于使用了`-`，因此不支持-/=翻页。
  - [x] 以词定字，左右方括号，雾凇拼音实现。
  - [x] u 模式，部件拼字。以字海两分输入方案为反查（融合拼音实现），反查起首从、`改为`u`（雾凇拼音实现）。
  - [x] uu 模式，专门字符。以`symbol.yaml`为基础，将默认的`/`改为`uu`（雾凇拼音实现以 v 开头）。
  - [ ] v 模式，输入内容格式转换。计划通过 lua 脚本实现（脚本有现成的）
    - 数字
    - 日期
    - 时间
    - 公式
  - [ ] v[uc|gb] 模式，字符集编码输入。Unicode 输入有现成方案，但不知能否增加反查。
  - [ ] ; 模式，人名候选，提高姓氏、常见名字组合权重。考虑和分词等有关，或者设计一个过滤器。
- 词库
  - [x] 自定义短语，Rime 自带。
  - [x] 内置文本替换，融合拼音实现_oo 输入替换。
  - [x] emoji 语义输入，雾凇拼音通过 opencc 实现
  - [x] 专业/扩展词典，Rime 自带。

1. [融合拼音](https://github.com/tumuyan/rime-melt)：以 [袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)、[【Rime 简体中文用户定制文件】](https://github.com/huaxianyan/Rime) 为基础，[字海两分](http://cheonhyeong.com/Simplified/download.html) 为反查，配合修改版 [Easy English](https://github.com/BlindingDark/rime-easy-en) 实现了简体中文和常用英语的混合输入。
2. [雾凇拼音](https://github.com/iDvel/rime-ice)，一个长期维护的简体词库，包含全拼和常用的自然码双拼、小鹤双拼、微软双拼
3. Unicode 输入：基于 lua 脚本的 Unicode 输入方案，解决部分未支持的字符输入问题，建议配合 [babelpad](https://www.babelstone.co.uk/Software/BabelPad.html)（Windows OS）、unicodepad（Android OS）、[unicode 字符百科](https://unicode-table.com/)（web）等工具、或 [unicode 标准文件](https://home.unicode.org/)。

### 皮肤/键盘

## 说明

由于融合拼音是 Apache-2.0 协议，而雾凇拼音是 GPL-3.0 协议，据 [《开源许可证兼容性指南》](https://gitee.com/trustworthy-open-source-community/License-Compatibility/tree/master)，将变更许可证为 GPL-3.0 协议。同时，尽量描述对于原项目的修改部分。

文件结构树

```cmd
├─basic
│  ├─[fonts]
│  ├─lua
│  └─opencc
├─custom
├─ex_dict
├─others
│   └─old
├─schema
└─theme
    └─trime
```

组件更新检查

|仓库|最近提交|许可证|
|---|---|---|
|[rime-prelude](https://github.com/rime/rime-prelude)|![GitHub last commit](https://img.shields.io/github/last-commit/rime/rime-prelude)|![GitHub license](https://img.shields.io/github/license/rime/rime-prelude)|
|[rime-essay](https://github.com/rime/rime-essay)|![GitHub last commit](https://img.shields.io/github/last-commit/rime/rime-essay)|![GitHub license](https://img.shields.io/github/license/rime/rime-essay)|
|[OpenCC](https://github.com/BYVoid/OpenCC)|![GitHub last commit](https://img.shields.io/github/last-commit/BYVoid/OpenCC)|![GitHub license](https://img.shields.io/github/license/BYVoid/OpenCC)|
|[袖珍簡化字拼音](https://github.com/rime/rime-pinyin-simp)|![GitHub last commit](https://img.shields.io/github/last-commit/rime/rime-pinyin-simp)|![GitHub license](https://img.shields.io/github/license/rime/rime-pinyin-simp)|
|[Rime 简体中文用户定制文件](https://github.com/huaxianyan/Rime)|![GitHub last commit](https://img.shields.io/github/last-commit/huaxianyan/Rime)|![GitHub license](https://img.shields.io/github/license/huaxianyan/Rime)|
|[字海两分](http://cheonhyeong.com/Simplified/download.html)|5.0|[叶典网](http://yedict.com/)独有|
|[Easy English](https://github.com/BlindingDark/rime-easy-en)|![GitHub last commit](https://img.shields.io/github/last-commit/BlindingDark/rime-easy-en)|![GitHub license](https://img.shields.io/github/license/BlindingDark/rime-easy-en)|
|[融合拼音](https://github.com/tumuyan/rime-melt)|![GitHub last commit](https://img.shields.io/github/last-commit/tumuyan/rime-melt)|![GitHub license](https://img.shields.io/github/license/tumuyan/rime-melt)|
|[雾凇拼音](https://github.com/iDvel/rime-ice)|![GitHub last commit](https://img.shields.io/github/last-commit/iDvel/rime-ice)|![GitHub license](https://img.shields.io/github/license/iDvel/rime-ice)|
|[雾凇拼音自定义配置](https://github.com/someok/rime-ice-custom)|![GitHub last commit](https://img.shields.io/github/last-commit/someok/rime-ice-custom)|![GitHub license](https://img.shields.io/github/license/someok/rime-ice-custom)|
|[白霜词库](https://github.com/gaboolic/rime-frost)|![GitHub last commit](https://img.shields.io/github/last-commit/gaboolic/rime-frost)|![GitHub license](https://img.shields.io/github/license/gaboolic/rime-frost)|

工具

```cmd
#Windows
winget install GNU.Wget2 --source winget
#Linux Debian
apt install wget
```

### 分类说明

```bash
curl -OL https://github.com/rime/rime-prelude/raw/master/symbols.yaml
curl -OL https://github.com/rime/rime-essay/raw/master/essay.txt
# curl -OL https://ci.appveyor.com/api/projects/Carbo/opencc/artifacts/OpenCC.zip?branch=master&job=Environment:%20nodejs_version=none;%20Platform:%20x64 | 7z e .\OpenCC.zip "-oopencc" "-ir!build\share\opencc\*"
# osfans/trime develop:app/src/main/assets/shared/opencc

```

#### Basic：基础与支持文件

主要来自 [rime-prelude](https://github.com/rime/rime-prelude) 和 [雾凇拼音](https://github.com/iDvel/rime-ice)

- `default.yaml`，缺省配置文件，【有修改】根据雾凇拼音增加相关项注释
- `key_bindings.yaml`，键位绑定配置
- `punctuation.yaml`，全半角转换符号配置
- `symbols.yaml`，符号配置
- `essay.txt`，八股文，预设词汇表和语言模型。来自 [rime-easay](https://github.com/rime/rime-essay)，更新方式：拉取（git pull）
- `zh-hans-t-essay-bgc.gram`和`zh-hans-t-essay-bgw.gram`都是根据 [八股文（語法）](https://github.com/lotem/rime-octagram-data) 生成的语法配置文件
- `default.custom.yaml`，启用方案记录，**空文件**
- 符号修改，在 `symbols.yaml`全角 → 多个相似符号中，插入部分常用半角符号（圆括号、方括号）

##### 文件夹

- `fonts/`，**空文件夹**，用来存放字库文件，详见 [字体](#字体)一节
- `lua/`，详见 [lua 脚本](#lua-脚本)一节
- `opencc/`，由 [OpenCC](https://github.com/BYVoid/OpenCC) 提供简繁转换，[融合拼音](https://github.com/tumuyan/rime-melt) 提供拼音滤镜，[雾凇拼音](https://github.com/iDvel/rime-ice) 提供`Emoji`滤镜。

###### opencc 更新词典文件

进入 [OpenCC/data](https://github.com/BYVoid/OpenCC/tree/master/data) 使用`OpenCC/data/config/*.json`和`OpenCC/data/dictionary/*.txt`替换本文件夹中的相关文件

`OpenCC/data/config/*.json`文件默认匹配的是。ocd2 文件（"type": "ocd2", "file": "TSPhrases.ocd2"）

1. 替换为 txt
2. 下载 [opencc 预编译包](https://ci.appveyor.com/api/projects/Carbo/opencc/artifacts/OpenCC.zip?branch=master&job=Environment:%20nodejs_version=none;%20Platform:%20x64)

以下文件由部分词典文件进一步操作产生，需要手动处理或使用 OpenCC 脚本处理

- HKVariantsRev.txt 由 HKVariants.txt 反转列产生
- JPVariantsRev.txt 由 JPVariants.txt 反转列产生
- TWPhrases.txt 由 TWPhrasesIT.txt TWPhrasesName.txt TWPhrasesOther.txt 合并产生
- TWPhrasesRev.txt 由 TWPhrases.txt 反转列产生
- TWVariantsRev.txt 由 TWVariants.txt 反转列产生

##### 字体

多平面字体

- 非商用：中华书局宋体、[天珩全字库 4.0](http://cheonhyeong.com/Simplified/download.html)、[全宋体](https://fgwang.blogspot.com/)
- 开源：花园明朝体

特定书体

- 旧字形宋体：[一点明体 8.0，2022-09-06](https://github.com/ichitenfont/I.Ming)
- 楷体：[霞鹜文楷](https://github.com/lxgw/LxgwWenKai)

更多开源字体可见 [猫啃网](https://www.maoken.com/) 的收集整理

###### lua 脚本

- `rime.lua`，综合配置
- `lua/lua_unicode_translator.lua`，Unicode 转字符脚本，来自 [Trime 同文输入法 QQ 群](458845988)@[Shitlime](1753102572)
- `lua/melt.lua`，来自 [融合拼音](https://github.com/tumuyan/rime-melt)

#### Schema：输入方案文件

输入方案和基本词典同目录

##### 字海两分 5.0 输入方案

来自 [天珩的小站-下载页](http://cheonhyeong.com/Simplified/download.html)，`ZHLF_rime_5.0.7z`

- `liangfen.dict.yaml`
- `liangfen.schema.yaml`

充当拆分组字功能的基础

##### 融合拼音

来自 [融合拼音](https://github.com/tumuyan/rime-melt)

- `melt_eng.schema.yaml`，
- `melt_pinyin.schema.yaml`
- `melt_pinyin.custom.yaml`，在融合拼音中增加半全角切换。

详见 [融合拼音](README_origin.md)[文件组成及授权](README_origin.md#文件组成及授权）一节。`other`文件夹中存放部分拟作词典的中间产物（即未完成)。

1. 作为主词库的 `melt_pinyin.dict.yaml`，同时也是词库加载文件
   1. `pinyin_simp.main.dict.yaml`，袖珍简化字拼音主词库
   2. `pinyin_simp_base.dict.yaml`，基础词库，现代汉语常用词表
   3. `pinyin_simp_wiki.dict.yaml`，维基百科词库，选用的是去除中文后的精简版，@tumuyan 抓取
   4. `pinyin_simp_moe.dict.yaml`，萌娘百科词库，@tumuyan 抓取
2. 作为反查词库的 `liangfeng.dict.yaml`
3. 作为扩展的转换词库（深蓝转换工具）
   1. `pinyin_simp_chengyu.dict.yaml`，搜狗细胞词库-成语
   2. `pinyin_simp_gushi.dict.yaml`，搜狗细胞词库-古诗

melt_eng 方案（即 Easy Englishi Nano）要求：

1. 作为主词库的 `melt_eng.dict.yaml`，同时也是词库加载文件
   1. `melt_mult_language.dict.yaml`，多语言字符拉丁化输入

##### 雾凇拼音

来自 [雾凇拼音](https://github.com/iDvel/rime-ice)

##### 其他

- `unicode.schema.yaml`，来自 [Trime 同文输入法 QQ 群](458845988)@[Shitlime](1753102572)
- `uncode.dict.yaml`，无内容

#### Ex_dict：方案词库文件

#### Custom：自定义部分

- `pinyin_simp_custom.dict.yaml`，袖珍简化字拼音自定义词语词库
- `melt_eng_custom.dict.yaml`，自定义英文词库
- `pinyin_simp_pin.txt`，固顶

#### Theme：主题文件

- `wendao.trime.yaml`，自定义。用于 Trime。
- `trime.yaml`，缺省主题，提取自 [Trime](https://github.com/osfans/trime)的[app/src/main/assets/shared](https://github.com/osfans/trime/tree/develop/app/src/main/assets/shared)路径。用于 Trime。
- `weasel.custom.yaml`，用于小狼毫。可参考[owlzou的小狼毫主题编辑器](https://owlzou.github.io/weasel-theme-editor/)。

主题/皮肤/键盘

```yaml
# 信息区
config_version: 
name: 
author: 
description: 
# 常量区
# 风格区
style:
# 回滚配色
fallback_colors:
  __include: trime:/fallback_colors
# 预设配色方案
preset_color_schemes:
# Android键值
android_keys:
  __include: trime:/android_keys
#预设键值

#流体键盘
#预设键盘
```

#### Other

- essay_script
- repo
  - OpenCC

## 运行环境与处理

### fcitx配置

- fcitx5-rime，`defualt.custom.yaml`在`/home/{user}/.local/share/fcitx5/rime/`

```cmd
rime_frontend=fcitx5-rime bash rime-install iDvel/rime-ice:others/recipes/full
```

### 拉取词库

使用子模块方法

```bash
#更新子模块
git submodule update --remote
#手动调整
```

### 下载

推荐使用 [补丁](https://github.com/rime/home/wiki/Configuration#補靪)的方式启用。

① 生成更新包。生成思路参考 [rimerc](https://github.com/Bambooin/rimerc)，提供 bat 文件。

1. 输入目标 fcitx、fcitx5、ibus、squirrel、trime or weasel，目前只支持 trime or weasel
2. 根据输入，复制 theme 文件到 releases 文件夹中的 rime 文件夹
3. 自动复制 basic、schema、ex_dict、custom 中的所有文件到 releases 文件夹中的 rime 文件夹
4. 调用 7-zip，将 releases 文件夹压缩

② 使用提供的发行包

③ 使用东风破（plum）

```cmd
rime_frontend=fcitx5-rime bash rime-install iDvel/rime-ice:others/recipes/full
```

### 设置

1. 在“方案”启用方案
2. 【Trime】在“键盘外观”启用 `wendao`
3. Trime 初次部署时间较长，需耐心等待

### 错误检查与修复

1、在【融合拼音】方案下无法混输英文

验证部署，查看 `rime/build/`文件夹，是否存在 `melt_eng.table.bin`。此步意在确定 `melt_eng`词库部署是否出错，若缺失词库文件，则不会生成 `melt_eng.table.bin`。
