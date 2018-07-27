# Django利用celery实现任务进度条

[![Python3](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-2.07-brightgreen.svg?style=plastic)](https://www.djangoproject.com/)
[![Celery](https://img.shields.io/badge/celery-3.1.26.post2-brightgreen.svg?style=plastic)](http://docs.celeryproject.org/en/latest/)


在网上找了很久都没有找到celery的django版任务进度条，搜索出来的都是flask去实现的。然后根据flask实现的移植到python上。

[flask-celery](http://www.pythondoc.com/flask-celery/first.html#id6)


## 运行demo

```
pip install -r requirements.txt
python manage.py runserver
# 启动一个工作进程用来处理异步任务
python manage.py celery worker
```

打开浏览器访问:[http://127.0.0.1:8000/](http://127.0.0.1:8000/)



## 代码


