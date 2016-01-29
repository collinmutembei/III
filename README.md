[![Build Status](https://travis-ci.org/andela-cmutembei/III.svg)](https://travis-ci.org/andela-cmutembei/III)
[![Coverage Status](https://coveralls.io/repos/andela-cmutembei/III/badge.svg?branch=develop&service=github)](https://coveralls.io/github/andela-cmutembei/III?branch=develop)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/f3b027bfc00949219f46c6aa0cf5da3a/snapshot/origin:develop:HEAD/badge.svg)](https://www.quantifiedcode.com/app/project/f3b027bfc00949219f46c6aa0cf5da3a)

## [BLST](http://blst-api.herokuapp.com/)
BLST is a RESTful API service for managing bucket lists and their constituent items. It is built using [Django](https://www.djangoproject.com/) and [Django Rest Framework](http://www.django-rest-framework.org/) and uses JSON objects for information interchange.

#### Project requirements
- [Python](https://www.python.org/downloads/)
- [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html)
- [Postgresql](http://www.postgresql.org/download/)

#### Documentation
The API documentation can be found [here](https://blst-api.herokuapp.com/docs)
#### Installation
To run blst locally configure [environment variables](https://github.com/andela-cmutembei/III/wiki) and do the following:
```shell
$ git clone https://github.com/andela-cmutembei/III.git && cd $_

$ workon III-env

(III-env)$ pip install -r requirements.txt

(III-env)$ python manage.py migrate

(III-env)$ python manage.py runserver
```

#### Running tests
To run unit tests for blst
```shell
(III-env)$ python manage.py test
```
#### License

This project is licensed under the terms of the [MIT license.](https://github.com/andela-cmutembei/III/blob/develop/LICENSE)

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://blst-api.herokuapp.com/)
[![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](http://blst-api.herokuapp.com/)
