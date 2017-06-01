# -*- coding=utf-8 -*-
'''
Created on 2017.5.30

@author: ch1st
'''
import requests
import sys
import time
from time import sleep 

class WebScanner(object):  
    def __init__(self):
        print(
    '''
\ \      / /__| |__/ ___|  ___ __ _ _ __  _ __   ___ _ __ 
 \ \ /\ / / _ \ '_ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  \ V  V /  __/ |_) |__) | (_| (_| | | | | | | |  __/ |   
   \_/\_/ \___|_.__/____/ \___\__,_|_| |_|_| |_|\___|_|   --ch1st 2017.5.30
    '''
    )
        print("=======The Head method is used=======") 
        if self.checkUrl()==False:
                print("URL?")
                sys.exit()
    def checkUrl(self):#判断用户是否输入了URL参数
        if len(sys.argv[1])>0:
            url=sys.argv[1]
            return url
        else:
            print("URL error")
            return False
    def HeadWay(self,url,dir): #主程序开始运行
        try:
            dir=open(dir,'r',encoding='gb18030')
            for line in dir.readlines():
                newline=line.strip()
                path=url+newline
                header={
                    'Accept': '*/*',
                    'Referer': sys.argv[1],
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
                    'Cache-Control': 'no-cache',
                }
                conn=requests.head("http://"+path,headers=header,allow_redirects=False)
                if conn.status_code != 404 :#单纯的黑名单./
                    print("%s%s%s%s"%(url,newline,":",conn.status_code))
        except:
            print("The program is occurred exited!")
    def UserChoose(self,Choose):#用户选择的字典判断
        try:
            if Choose == '1':        
                dir = 'dir_1.txt'
                return dir
            elif Choose == '2':
                dir = 'dir_2.txt'
                return dir
            elif Choose == '3':
                dir='dir_3.txt'
                return dir
            elif Choose == '4':
                 sys.exit()
        except Exception as e:
            print(e)
    def run(self):
        try:
            while True:
                if sys.version_info[0]>=3:  #判断python版本是否为3.其实2也能运行
                    print(
                    '''
    Please enter thr Dir.txt you want to scan:
    1.usual text
    2.dir2 text
    3.dir3.text
    4.exit
                    '''
                    )
                    Choose=input()
                    self.HeadWay(self.checkUrl(),self.UserChoose(Choose))
                else:
                    print("The program required Python Version 3.0 or more than 3.0")
                    sys.exit()
        except Exception as e:
            print(e)
            

if __name__=="__main__":
    run=WebScanner()
    run.run()












