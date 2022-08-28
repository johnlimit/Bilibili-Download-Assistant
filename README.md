# BILIBILI_SCRAPER：B站数据爬取工具

作者：南京邮电大学 林宏扬

## 一、简介

​	BILIBILI_SCRAPER是一款基于Python的可以实现B站视频、音频、评论、动态的抓取工具。本工具基于Python的基本库、pymongo库及MongoDB数据库、ffmpeg音频处理软件实现，使用时需要安装对应的库及程序。

​	本工具为非盈利目的，代码开源，任何人均可以对本工具进行使用、学习、借鉴、指正，亦可进行转载，但转载需注明出处和作者。

## 二、功能

​	1.可抓取您给定的B站视频下面的评论区的信息。具体包括以下内容：

​		（1）评论的信息，包括文字、点赞数、发表日期；

​		（2）评论者的个人信息，包括用户名、性别、大会员类型、装扮名称、装扮编号、等级。

​	2.可抓取您给定的B站用户的个人动态信息。具体包括以下内容：

​		（1）动态类型（文字/图文/视频/转发）；

​		（2）动态文字；

​		（3）点赞数、评论数、转发数；

​		（4）所带话题；

​		（5）若为转发他人动态，则还有原动态的类型、原动态的文字、原动态的BV号、时长和简介（转发视频时适用）

​	3.可下载您给定的B站视频或音频。**下载后的文件自动保存在本工具所处的目录中。**

​	4.可通过本地设置文件随心调整抓取设置。

## 三、结构

​	本工具包括以下文件：

​		1.main.py（主界面）：用于启动本工具的程序。请从main.py文件开始执行！

​		2.scrape.py（抓取工具）：用于实现网络爬取的功能，将网上的内容爬取下来。

​		3.convert.py（转换工具）：用于将BV号转换成AV号。

​		4.settings.py（设置工具）：用于处理程序设置。

​		5.save_data.py（保存工具）：将爬取的数据保存到数据库中。

​		6.download.py（下载工具）：用于下载视频和音频。

​		7.settings.json（设置文件）：用于保存程序的设置情况。

​	请注意，**如果只需要视频/音频下载功能，请从download.py运行；否则，请从main.py中运行**。

## 四、安装清单

​	在使用本工具之前，请一定要安装好以下内容：

​		（1）Python 3.10 及以上版本（用于爬取评论、动态，以及下载视频、音频）；

​		（2）pymongo库（用于爬取评论、动态）；

​		（3）MongoDB数据库（用于爬取评论、动态）；

​		（4）ffmpeg音频软件（用于下载视频、音频）；

​		（5）BeautifulSoup库（用于爬取评论、动态）；

​		（6）Stdio 3T数据可视化管理软件（用于爬取评论、动态）。

​	具体安装方式见下一节。

## 五、使用前准备

### 1.安装Python 3.10

​	请注意，若电脑原来已经安装Python软件，请**注意确认您所安装的Python版本是否为3.6版以上**（此为**最低限度要求**，否则部分代码会报错）。建议使用Python 3.10，从而得到最佳性能效果。

​	若想查询电脑所安装的Python版本，请打开命令提示符并输入：<u>（没装过的就不用查版本了）</u>

```shell
python --version
```

​	安装Python 3.10的方法比较简单，按照这个网址来操作就好了：

[(1条消息) 真小白入门：python的安装（一）_大橘子呀的博客-CSDN博客_python](https://blog.csdn.net/nmjuzi/article/details/79075736)

### 2.安装pymongo库

​	**[注意]请先安装Python 3.10，再来安装pymongo库。**

​	安装的方式比较简单，打开命令提示符（cmd），输入：

```shell
pip3 install pymongo
```

### 3.安装MongoDB数据库

​	可以参考这篇文章：[MongoDB 的安装 | 静觅 (cuiqingcai.com)](https://cuiqingcai.com/31070.html)

### 4.安装ffmpeg音频软件

​	这个视频每一步都讲得很详细（这是个合集，**看第一个视频就好了**）：

[【FFmpeg 分P教学】转码、压制、录屏、裁切、合并、提取 … 统统不是问题。_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Ft411s7Xa?spm_id_from=333.337.search-card.all.click&vd_source=40c74775a6bbe5ee7026636cb04e2b9f)

### 5.安装BeautifulSoup库

​	**[注意]请先安装Python 3.10，再来安装BeautifulSoup库。**

​	安装的方式与安装pymongo库类似。打开命令提示符（cmd），输入：

```shell
pip3 install bs4
```

​	需要注意的是，由于BeautifulSoup隶属于bs4库里面，所以上述命令会安装bs4库，此时BeautifulSoup也被自动安装在电脑中。

### 6.安装Studio 3T可视化管理软件

​	点击以下连接，选择里面大大的“Download"按钮即可下载：

[Download Studio 3T for MongoDB | Windows, macOS & Linux](https://studio3t.com/download/)

​	需要注意的是，这个软件有30天的试用期。**如有可能请支持正版**。若想**以学习目的暂时屏蔽**试用期限制，可以参考以下连接：

[(1条消息) Studio 3T 试用期破解（含破解补丁） - 解决办法_草巾冒小子的博客-CSDN博客_studio3t过期了怎么办](https://blog.csdn.net/qq_35393869/article/details/85245785?ops_request_misc=&request_id=&biz_id=102&utm_term=studio 3t&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-4-85245785.142^v42^control,185^v2^control&spm=1018.2226.3001.4187)

## 六、使用方法

​	1.做好上一节的准备后，可以将本工具的所有文件放置在同一目录中，然后双击“main.py”运行。之后按照程序的提示进行抓取、下载即可。

​	2.用户选择下载视频/音频时，视频/音频文件会自动保存在本工具所在目录中。

​	3.评论/动态抓取完毕后，若想查看/分析数据，请打开studio 3T软件，连接本地数据库，选择想查看的数据库和想查看的集合即可进行数据查看和数据分析。具体数据查看和分析方法见下一节。

## 七、Studio 3T软件的简单使用

​	本工具将爬取到的评论和动态均存储到MongoDB数据库中。之所以存到数据库中，是因为数据库方便管理、分析数据。下面我们简单介绍一下Studio 3T软件。

​	1.打开Studio 3T后，首先选择工具栏的“Connect”。

![pic1](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic1.PNG)

​	2.在弹出来的对话框中，选择右上角的“New Connection”。

![pic2](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic2.PNG)

​	3.随后弹出来一个对话框，我们不管它，直接按“Next”。

![pic3](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic3.PNG)

​	4.又弹出来一个对话框，我们还是不管它，直接按“Save”。**此时系统默认连接本地数据库。**

![pic4](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic4.PNG)

​	5.原本弹出的“Connection Manager”列表中会多出一个名为“localhost:27017"的连接，我们单击这个连接，点击”Connect“即可连接。

![pic5](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic5.PNG)

​	6.此时左侧的列表就会出现本地数据库中的数据库名字。双击一个数据库，就会列出该数据库里面的集合。

![pic6](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic6.PNG)

​	7.点击一个集合，主界面就会显示该集合中所有的字段和内容。

![pic7](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic7.PNG)

​	8.若想对一个集合内的数据进行分析，选择工具栏的”Schema”按钮即可。此处需要自行选择样本容量（可选随机、部分或者全部）。分析完成后，程序将会生成一系列分析结果。

![pic8](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic8.PNG)

![pic9](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic9.PNG)

## 八、使用示例：爬取并分析B站视频评论

​	我们以[【自制】如何制作一个赛博朋克风格的 百大UP奖杯 【软核】_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1VA411p7MD?spm_id_from=333.999.0.0&vd_source=40c74775a6bbe5ee7026636cb04e2b9f)为例，该视频共有2000+条评论（该数据包含楼中楼），爬取量适中。

​	下面为大家展示如何使用本工具爬取并分析B站视频评论。

​	1.运行main.py，进入主界面，选择“1”进行评论爬取。

![](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic10.PNG)

​	2.输入要爬取视频所对应的BV号（本例中应输入BV1VA411p7MD）

![pic11](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic11.PNG)

​	3.随后程序将自动进行爬取。**当程序提示绿色字体的“爬取结束”时，整个爬取过程结束。**

![pic12](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic12.PNG)

​	4.打开Studio 3T，找到BilibiliComments -> Collections ->对应日期和BV号的集合（本例中为2022-08-26 21:18:45  -  BV1VA411p7MD）。需要注意的是，如果运行程序之前已经打开了Studio 3T，则需在左侧栏中右键选择“Refresh All”来刷新。

![pic13](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic13.PNG)

​	5.随后我们可以选择工具栏的“Schema”进行数据分析。由于数据量不大，故我们可以直接选择“All”对全部样本进行分析。随后点击“Run analysis”进行分析。最后我们可以得到数据分析的结果，点进每个字段可以得到系统对该字段的分析内容。如在评论中提及次数最多的词汇是“太强了” 、性别未保密的用户中男性评论者较多等。![pic14](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic14.PNG)

![pic15](C:\Users\lenovo\Desktop\Bilibili_Scraper\帮助文档\pic15.PNG)