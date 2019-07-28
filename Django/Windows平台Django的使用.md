# Windows平台Django的使用



## 先在桌面创建一个文件夹，名字是 *django_demo*

* 在命令行中输入 <code>cd C:\Users\uers\Desktop\django_demo</code>切到django_demo目录下

## 安装virtualenv

命令行输入<code>pip install --user virtualenv</code>安装virtualenv包   

安装成功显示

![5XKHBl.png](https://s1.ax2x.com/2018/10/29/5XKHBl.png)  

###    	安装成功之后，创建虚拟环境



输入命令<code>virtualenv netpage</code>创建虚拟环境，在该目录下创建了一个netpage的文件夹

![5XKXAB.png](https://s1.ax2x.com/2018/10/29/5XKXAB.png)

django_demo目录下新添加的文件夹



![5XKVjp.png](https://s1.ax2x.com/2018/10/29/5XKVjp.png)



### pip的安装

稍后更新

---------

## 激活虚拟环境

键入命令<code>cd netpage/Scripts</code>跳转到该目录下   

再键入<code>activate</code>  激活虚拟环境     

激活之后注意文件夹*netpage* 有一对括号，表示激活成功  

![5XKWVG.png](https://s1.ax2x.com/2018/10/29/5XKWVG.png)

当需要关闭虚拟环境时，键入<code>deactivate</code>      

[![5XKdvn.png](https://s1.ax2x.com/2018/10/29/5XKdvn.png)](https://imgse.com/i/5XKdvn)

括号包起来的netpage消失，代表关闭成功  

-----

## 安装Django  

输入<code>pip install Django</code>即自动安装

![5XKMFQ.png](https://s1.ax2x.com/2018/10/29/5XKMFQ.png)    



正在下载...   

[![5XKbAa.png](https://s1.ax2x.com/2018/10/29/5XKbAa.png)](https://imgse.com/i/5XKbAa)

安装成功...   

Django仅在虚拟环境处于活动状态才可用     

---

## 在Django中创建项目

键入<code>cd ..</code>

返回django_demo的第一层子目录中   

键入<code>django-admin.py startproject learning_log</code>  

创建一个learning_log的项目  



![5XKpwz.png](https://s1.ax2x.com/2018/10/29/5XKpwz.png)

此时django_demo目录下包含两个子文件夹，其中一个为learning_log的项目  

---

## 创建数据库

输入<code>cd learning_log</code>

跳转到该目录下  

输入<code>python manage.py migrate</code>之后    

![5XKujS.png](https://s1.ax2x.com/2018/10/29/5XKujS.png)  



---

## 查看项目

来何时Django是否正确地创建了项目  

键入<code>python manage.py runserver</code>    

![5XK4Eh.png](https://s1.ax2x.com/2018/10/29/5XK4Eh.png)        

  

可以在浏览器中输入<code>localhost:8000</code>  

![5XKJ7H.png](https://s1.ax2x.com/2018/10/29/5XKJ7H.png)  



初步配置成功  















