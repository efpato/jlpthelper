JLPTHelper
==========

Web service for JLPT preparing.  

# Requirements

- Python3.4
- pip
- virtualenv

# Developer environment

```bash
$ virtualenv -p /usr/local/bin/python3.4 jlpthelper_env
$ cd jlpthelper_env
$ source bin/activate
$ git clone git@github.com:OdinO4ka/jlpthelper.git
$ cd jlpthelper
$ git checkout develop
$ pip install -r requirements/development
$ export JLPT_DEV=1
$ ./manage.py syncdb
$ ./manage.py runserver
```
