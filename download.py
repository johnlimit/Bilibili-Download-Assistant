import time                      #用于延时
import os                        #用于暂停
import platform                  #用于判断操作系统类型
try:
    import requests                  #用于抓取
except:
    print('检测到缺少requests库，正在安装中...')
    time.sleep(1)
    os.system('pip3 install requests')
    import requests
import re                        #用于正则匹配
import json                      #用于处理抓取的JSON数据
import subprocess                #用于启动外部程序(ffmpeg)
try:
    from colorama import Fore,Style  #用于彩色字体
except:
    print('检测到缺少colorama库，正在安装中...')
    time.sleep(1)
    os.system('pip3 install colorama')
    from colorama import Fore,Style
try:
    from tqdm import tqdm
except:
    print('检测到缺少tqdm库，正在安装中...')
    time.sleep(1)
    os.system('pip3 install tqdm')
    from tqdm import tqdm

class BilibiliDownloader:
    def __init__(self,bv_number):
        self.bv_number = bv_number
        self.audio_url = ''
        self.video_url = ''

    
    def get_html(self,url,is_stream=False):
        headers = {
            'referer':'https://www.bilibili.com', #要有防盗链，否则就是403 Forbidden
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
        if is_stream == True:
            html = requests.get(url,headers=headers,stream=True)
        else:
            html = requests.get(url,headers=headers)
        return html

    def parser(self,html):
        json_data = re.findall('<script>window\.__playinfo__=(.*?)</script>', str(html))[0]
        json_data = json.loads(json_data)

        #提取音频和视频的URL地址
        #优先提取backupUrl。
        #有时提取不到，那就提取base_url。
        try:
            self.audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
            self.video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
        except Exception as e:
            print(Fore.RED + '无法抓取BackupURL，错误类型为',end='')
            print(type(e),end='')
            print(Style.RESET_ALL)
            print(Fore.YELLOW + '转为抓取base_url.' + Style.RESET_ALL)
            try:
                self.audio_url = json_data['data']['dash']['audio'][0]['base_url']
                self.video_url = json_data['data']['dash']['video'][0]['base_url']
            except Exception as eg:
                print(Fore.RED + '无法抓取base_url，错误类型为',end='')
                print(type(eg),end='')
                exit()


    def download_data(self,audio_only=False):
        print('准备下载音频数据...')
        resp = self.get_html(self.audio_url,is_stream=True)
        total = int(resp.headers.get('content-length',0))
        print(str(total))
        print('正在下载并保存为音频文件...' )
        if audio_only == True:
            with open(self.bv_number + '.mp3',mode='wb') as f,tqdm(
                desc=self.bv_number+'.mp3',
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024
            )as bar:
                for data in resp.iter_content(chunk_size=1024):
                    size = f.write(data)
                    bar.update(size)
        else:
            with open(self.bv_number + '_audio.mp3',mode='wb') as f,tqdm(
                desc=self.bv_number+'_audio.mp3',
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024
            )as bar:
                for data in resp.iter_content(chunk_size=1024):
                    size = f.write(data)
                    bar.update(size)
        print(Fore.GREEN + f'音频文件保存成功!' + Style.RESET_ALL)
        if audio_only == False:
            resp = self.get_html(self.video_url,is_stream=True)
            total = int(resp.headers.get('content-length',0))
            print('正在下载并保存为视频文件...' )
            with open(self.bv_number + '_video.mp4',mode='wb') as f,tqdm(
                desc=self.bv_number+'_video.mp4',
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024
            )as bar:
                for data in resp.iter_content(chunk_size=1024):
                    size = f.write(data)
                    bar.update(size)
            print(Fore.GREEN + '保存视频文件成功。' + Style.RESET_ALL)

    def merge(self):
        print('正在合并生成最终视频...')
        time.sleep(1)
        COMMAND = f'ffmpeg -i {self.bv_number}_video.mp4 -i {self.bv_number}_audio.mp3 -c:v copy -c:a aac -strict experimental {self.bv_number}.mp4'
        subprocess.run(COMMAND,shell=True)
        if os.path.exists(self.bv_number + '.mp4'):
            print(Fore.GREEN + f'视频合成成功！文件名为{self.bv_number}.mp4。' + Style.RESET_ALL)
            os.remove(bvid + '_audio.mp3')
            os.remove(bvid + '_video.mp4')
        else:
            #没有最终合成的文件，说明ffmpeg没有正确安装
            print(Fore.RED + '视频合成失败！请检查ffmpeg软件是否正确安装！\n提示:现在已经得到了纯音频文件和纯视频文件，若不安装ffmpeg软件，则可以用其他软件手动合成。' + Style.RESET_ALL)

def welcome_page():
    clear_screen()
    print()
    print('------------------------------------------------------')
    print()
    print(Fore.GREEN + 'BILIBILI_DOWNLOAD_ASSISTANT:B站音视频下载助理' + Style.RESET_ALL)
    print('作者：南京邮电大学 林宏扬')
    print('初稿：2022年8月26日')
    print('当前版本：2022年8月27日版')
    print('这是一个轻量级的B站音视频下载工具。')
    print(Fore.YELLOW + '操作系统类型:'+ platform.system() +Style.RESET_ALL)
    print()
    print('------------------------------------------------------')
    print()
    print('此为欢迎页，3秒后进入主页面...')
    time.sleep(3)

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')

def pause():
    if platform.system() == 'Windows':
        os.system('pause')
    else:
        #很遗憾,linux里面并没有pause函数。
        input('按回车键继续...')

if __name__ == '__main__':
    welcome_page()
    clear_screen()
    print()
    print(Fore.YELLOW + '    ┌------------注意------------┐')
    print('    | 本工具需要依赖ffmpeg软件。 |')
    print('    | 请确认是否正确安装、配置。 |')
    print('    └----------------------------┘' + Style.RESET_ALL)
    print()
    while True:
        bvid = input('请输入要下载视频/音频的BV号(以BV开头):')
        if bvid.upper().find('BV') == -1:
            print(Fore.RED + '输入错误。请注意：要输入以BV开头的BV号！' + Style.RESET_ALL)
            continue
        choice2 = input('请问需要下载视频还是音频?\n1:下载视频\n2:下载音频\n请输入:')
        if choice2 == '1':
            audio_only = False
        elif choice2 == '2':
            audio_only = True
        else:
            print(Fore.RED + '输入错误，请重试。' + Style.RESET_ALL)
            continue
        if os.path.exists(bvid + '.mp3') and audio_only == True:
            print('您现在正在获取音频文件' + bvid +'.mp3，但是' + Fore.RED +'此文件已存在!' + Style.RESET_ALL + '\n如果想保留原有文件，建议您移动原有文件，否则将会覆盖原文件!')
            choice3 = input('请选择: (1:继续 0:取消操作)')
            if choice3 != '1':
                continue
            else:
                os.remove(bvid + '.mp3')
        if os.path.exists(bvid + '.mp4') and audio_only == False:
            print('您现在正在获取视频文件' + bvid +'.mp4，但是' + Fore.RED +'此文件已存在!' + Style.RESET_ALL + '\n如果想保留原有文件，建议您移动原有文件，否则将会覆盖原文件!')
            choice3 = input('请选择: (1:继续 0:取消操作)')
            if choice3 != '1':
                continue
            else:
                os.remove(bvid + '.mp4')
        downloader = BilibiliDownloader(bvid)
        data = downloader.get_html('https://www.bilibili.com/video/' + str(bvid)).text
        downloader.parser(data)
        downloader.download_data(audio_only)
        if audio_only == False:
            downloader.merge()
            
        pause()
        clear_screen()
