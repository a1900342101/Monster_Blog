# Monster_Blog
一个基于django的小博客

效果:http://www.0hao0hao.com


背景:
以前使用过别人写的一个基于flask的好像叫"Mini_Blog",
用了两周,问题有点多,自己慢慢解决.
从中得到了启发,不如自己写一个小博客吧,这样就知道如何快速解决出现的问题,同时也是锻炼一下自己.
因此决定用django自己来开发


About me:
本人菜的抠脚,学校没有这些课程,这些知识全靠Internet及万千网友!
在大一开始接触python,到了现在大二才开始写一点小项目来锻炼自己
希望有大佬能带带小学弟,万分感谢


Thanks:
DanceSmile-杨青,CSND社区... ...

# 在服务器部署Monster_blog
1.pip install uwsgi
(centos7 报错没有Python.h的话，先执行yum install python-devel)

2.编辑uwsgi配置文件mysite.ini

	[uwsgi]
	project = Monster_blog
	base =/data/Monster_blog ;这个目录要看自己服务器的具体情况
	chdir = %(base)
	module = %(project).wsgi:application
	http = 0.0.0.0:80
	master = true
	processes = 3
	vacuum = true
	daemonize = %(base)/Monster_blog/uwsgi8001.log
	wsgi-file=%(base)/Monster_blog/wsgi.py
	static-map=/static=%(base)/blog/static
                                                  
3.django初始化数据库
	
	3.1)create database MonsterBlog;(这步要到mysql数据库操作，sqlite3的数据库忽略这步)
	3.2)python manage.py makemigrations
	3.3)python manage.py migrate
	3.4)python manage.py createsuperuser(这步创建的管理员用户用于博客后台登录)

4.部署静态文件:
	
	python manage.py collectstatic

5.uwsgi --ini /data/mysite.ini
	运行成功，结束:killall -s 9 uwsgi

6.配置nginx/apache2(可忽略)
	方法多样，自行研究
	结束nginx:nginx -s stop

