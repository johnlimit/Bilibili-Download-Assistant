# Download Assistant：B站音视频下载助理

作者：南京邮电大学 林宏扬

## 一、简介

​	Download Assistant是一款基于Python及ffmpeg构成的、可以实现B站音频、视频下载的一个工具。本工具使用前需要安装Python 3.10（Windows 7用户请安装Python 3.8），建议保持联网状态（需要在线下载工具所需库）。

​	本工具基于本人的BILIBILI_SCRAPER工具改写而成，简化了其他功能，为用户提供一个精炼简洁的B站音视频下载工具，避免了配置其他不相关软件的麻烦。

​	**本工具遵守GPL 3.0协议。**本工具以非盈利目的分享给任何人进行使用、借鉴、指正，亦可进行转载，但转载需注明出处和作者。

## 二、功能

​	本工具可用于下载B站指定视频（亦支持仅下载音频）。

## 三、依赖库

​	**请注意**：此处列举的依赖库并不是要求您自己去安装，而是列举出来本工具所使用的所有库，以供学习网络爬虫的人士进行参考。

​	1.系统标准库（包括os库、time库、platform库、json库、re库、subprocess库）

​	2.requests库（用于抓取音视频内容）

​	3.colorama库（用于彩色字体）

​	4.tqdm库（用于展示下载进度条）

## 四、使用前准备

​	为使用本工具，您需要进行如下准备：

### 1.安装Python

​	本工具基于Python 3.10构建，**因此为达到最好的效果，建议您安装Python 3.10（即目前的最新版本）。安装方式可以参考如下文章：

​	[(9条消息) 真小白入门：python的安装（一）_大橘子呀的博客-CSDN博客_python](https://blog.csdn.net/nmjuzi/article/details/79075736)		

​	请注意：

​		（1）Windows 7系统由于系统版本过旧，最高仅支持Python 3.8版本。本GitHub项目附有Python 3.8的安装包，**请Windows 7用户下载并安装3.8版本的Python**。经作者测试，**Windows 7 + Python 3.8可以正常使用本软件。**

​		（2）若您电脑已经安装Python，建议您查询当前安装版本是否在3.8及以上。查询方法为：打开命令提示符/终端，输入以下命令并回车：

```shell
python --version
```

​		（3）Linux用户默认自带Python。建议您也通过第二条注意来查询系统自带Python版本。若版本较低，建议您通过终端更新Python（注意在Linux中应写作python3）：

```shell
sudo apt-get install python3
```

### 2.下载本仓库文件

​	本仓库内置download.py（程序主体）、LICENSE（GPL 3.0协议说明）、ffmpeg.exe（音视频转换工具）、README.md（说明文档）及python-3.8.13-amd64.exe（适用于Windows 7 64位的Python 3.8安装包）。您可直接点击此网页的绿色“code”按钮，再选择“Download ZIP”将整个仓库文件均下载下来。

​	下载完成后，对下载的ZIP文件进行解压，即可得到本工具的所有文件。

​	**请注意：必须保证download.py和ffmpeg.exe同时存在，否则本工具无法顺利实现音视频下载。**

## 五、使用指南

​	下面我们详细展示本工具的使用方法。

​	1.将download.py和ffmpeg.exe放置在同一目录后，双击download.py运行。初次运行时，工具会自动下载补全所需的库。

![](https://github.com/johnlimit/Bilibili-Download-Assistant/blob/main/pic/pic1.PNG?raw=true)

​	2.进入欢迎界面，此时您不需要任何操作，3秒后自动跳转。

![](https://github.com/johnlimit/Bilibili-Download-Assistant/blob/main/pic/pic2.PNG?raw=true)

​	3.工具提示您输入需要下载的音视频的BV号。您可以选择手动输入，也可以在网页上找到BV号并复制粘贴。

​		（请注意：对于Linux、Win7、Win8、Win8.1系统，粘贴的方式是右键->粘贴；对于Win10及Win11系统，粘贴的方式是直接右键。）

![](https://github.com/johnlimit/Bilibili-Download-Assistant/blob/main/pic/pic3.png?raw=true)

​	4.随后您可选择下载音频还是下载视频，输入1和2之后回车即可进入下一步。

![](https://github.com/johnlimit/Bilibili-Download-Assistant/blob/main/pic/pic4.PNG?raw=true)

​	5.工具开始自动下载、合并。您可以查看当前下载速度及进度。

![](https://github.com/johnlimit/Bilibili-Download-Assistant/blob/main/pic/pic5.PNG?raw=true)

​	6.工具下载、合并完成后，会告知您成功/失败。若成功，则下载完成的音视频文件就放置在download.py所属的文件夹里。若失败，请检查ffmpeg.exe是否与download.py放置在同一目录中。

![](https://github.com/johnlimit/Bilibili-Download-Assistant/blob/main/pic/pic6.PNG?raw=true)
