# leetcodeblog

LeetcodeBlog is for my UCSC Python class' final project, and also a personal blog.

## Getting Strarted

### Prerequisites

pip requirement list:

```shell
Django==1.8.5
Markdown==2.6.2
MySQL-python==1.2.5
bootstrap-admin==0.3.6
django-ckeditor==5.0.2
django-summernote==0.6.16
django-wysiwyg==0.7.1
python-memcached==1.57
six==1.10.0
uWSGI==2.0.11.2
wsgiref==0.1.2
```

## deploy on CentOS7
## Install MariaDB / MySQLdb and Memcached
MariaDB is shipped in the CentOS repo as of CentOS 7 instead of mysql.
if you still want to install mysql you need to add mysql rpm dependency into your yum repo.

```shell
sudo yum install python-devel
sudo yum install mysql-devel
sudo yum install gcc
sudo yum -y install memcached
systemctl restart memcached
systemctl start memcached
```
Be sure that Memcached starts at boot:
```shell
systemctl enable memcached
```

To check the status of Memcached:
```shell
systemctl status memcached
```

To stop memcached
```shell
systemctl stop memcached
```

## After everything is done
```shell
python manage.py syncdb --noinput
python manage.py migrate
python manage.py createsuperuser
```

## Follow Me
You can find me on [Twitter](https://twitter.com/mactanxin).

## License
LeetCodeblog is released under the [MIT license](https://github.com/mactanxin/leetcodeblog/blob/master/license.md).

