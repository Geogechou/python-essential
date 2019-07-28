from __future__ import print_function
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
import ctypes, sys
import os
import win32api
import clipboard
from os.path import expanduser
import _thread

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
home = expanduser("~")  
top=Tk()    
label = tkinter.Label(top, text="NetWork status unknow",
                bg="black", fg="green",
                font=("黑体", 15),
                width=40,
                height=3,
                #wraplength=100,
                justify="right",
                anchor="ne")
label.grid(row=3,columnspan=4)      
submitBtn=tkinter.Button(top,text="Submit",command=lambda:poweroff(-10000),width=10,height=2,bg="red")
def openChrome():
    chromePath=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    win32api.ShellExecute(0, 'open', chromePath, '','',0) 
def openXxNet():
    xxPath=home+r"\OneDrive\集装箱\翻墙用\XX-Net-3.13.1\start.vbs"
    win32api.ShellExecute(0, 'open', xxPath, '','',0)
def openRuijie():
    rjPath=r"C:\Program Files\Ruijie Networks\Ruijie Supplicant\RuijieSupplicant.exe"
    win32api.ShellExecute(0, 'open', rjPath, '','',0)
def openSSR():
    ssrPath=home+r'\OneDrive\集装箱\翻墙用\shadowsocks连接服务器网络\win\SSR4.0.exe'
    win32api.ShellExecute(0, 'open', ssrPath, '','',0)    
def openterminal():
    terminalPath=r"C:\Users\geoge\OneDrive\t.lnk"
    win32api.ShellExecute(0, 'open', terminalPath, '','',0)  
def shutdownProcess(exeName):
    os.system("taskkill /F /IM "+exeName)    
def ping(name,label):
    hostname = "ipv6.test-ipv6.com"
    response = os.system ("ping -6 " +hostname)
    if response ==0:
        label["text"]="IPV6 is available"
    else:
        label["text"]="IPV6 doesn't work"
def poweroff(top):
    if top == -10000:
        os.system("shutdown -s -t 10")  
    else:              
        submitBtn.grid(row=2,column=3)     
        label["text"]="click Submit button to assume"     
def checkNet(label):
    _thread.start_new_thread(ping,("network",label))  

def my_script():
 
    top.geometry("500x500+100+50")
    top.title("Tools(Admin)")
    B1=tkinter.Button(top,text="启动chrome",command=openChrome,width=10,height=2)
    b1=tkinter.Button(top,text="关闭chrome",command=lambda:shutdownProcess("chrome.exe"),width=10,height=2)
    B2=tkinter.Button(top,text="启动xxNet",command=openXxNet,width=10,height=2)
    b2=tkinter.Button(top,text="关闭xxNet",command=lambda:shutdownProcess("pythonw.exe"),width=10,height=2)
    B3=tkinter.Button(top,text="启动锐捷",command=openRuijie,width=10,height=2)
    b3=tkinter.Button(top,text="关闭锐捷",command=lambda:shutdownProcess("8021x.exe"),width=10,height=2)
    B4=tkinter.Button(top,text="启动SSR",command=openSSR,width=10,height=2)
    b4=tkinter.Button(top,text="关闭SSR",command=lambda:shutdownProcess("SSR4.0.exe"),width=10,height=2)
    B6=tkinter.Button(top,text="检测网络",command=lambda:checkNet(label),width=10,height=2)
    B7=tkinter.Button(top,text="启动terminal",command=openterminal,width=10,height=2)
    B8=tkinter.Button(top,text="关机",command=lambda:poweroff(top),width=10,height=2)
    B1.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    B2.grid(row=0,column=2)
    b2.grid(row=0,column=3)
    B3.grid(row=1,column=0)
    b3.grid(row=1,column=1)
    B4.grid(row=1,column=2)
    b4.grid(row=1,column=3)
    B6.grid(row=2,column=0)
    B7.grid(row=2,column=1)
    B8.grid(row=2,column=2)
 
    mainloop()    
if is_admin():
    try:
        my_script()
    except Exception as e:
        print(e)
else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
