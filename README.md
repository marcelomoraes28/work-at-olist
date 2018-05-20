# Work at Olist

[Olist](https://olist.com/) is a company that offers an integration platform
for sellers and marketplaces allowing them to sell their products across
multiple channels.

The Olist development team consists of developers who loves what they do. Our
agile development processes and our search for the best development practices
provide a great environment for professionals who like to create quality
software in good company.

We are always looking for good programmers who love to improve their work. We
give preference to small teams with qualified professionals over large teams
with average professionals.

This repository contains a problem used to evaluate the candidate skills.
It's important to notice that satisfactorily solving the problem is just a
part of what will be evaluated. We also consider other programming disciplines
like documentation, testing, commit timeline, design and coding best
practices.

Hints:

* Carefully read the specification to understand all the problem and
  artifact requirements before start.
* Check the recommendations and reference material at the end of this
  specification.


## Description

This project aims to start and end phone calls and then calculate the bill for each call


## Install
* Requirements
  * Docker (https://www.docker.com/)
  * Github account (http://github.com/)

* Start application
  * After configure github account, run: git clone https://github.com/marcelomoraes28/work-at-olist.git
  * Access the root project folder: cd work-at-olist
  * Run command: docker-compose up
  * Create a superuser for djangoadmin:
    * Access django container: docker exec -it django bash
    * Running command: python3 manage.py createsuperuser

* Running test:
  * After starting the project, run command to access django container: docker exec -it django bash
  * Running command: python3 manage.py test

* Observation:
  * By default the system initializes with data 99988526423 (source) and 9993468278 (destination)
    * call_id: 70, started at 2016-02-29T12:00:00Z and ended at 2016-02-29T14:00:00Z.
    * call_id: 71, started at 2017-12-12T15:07:13Z and ended at 2017-12-12T15:14:56Z.
    * call_id: 72, started at 2017-12-12T22:47:56Z and ended at 2017-12-12T22:50:56Z.
    * call_id: 73, started at 2017-12-12T21:57:13Z and ended at 2017-12-12T22:10:56Z.
    * call_id: 74, started at 2017-12-12T04:57:13Z and ended at 2017-12-12T06:10:56Z.
    * call_id: 75, started at 2017-12-12T21:57:13Z and ended at 2017-12-13T22:10:56Z.
    * call_id: 76, started at 2017-12-12T15:07:58Z and ended at 2017-12-12T15:12:56Z.
    * call_id: 77, started at 2018-02-28T21:57:13Z and ended at 2018-03-01T22:10:56Z.


* Architecture description:
  * Containers
    * Nginx
    * Redis (Used as broken)
    * PostgresDB
    * Celery (Used as working. Default 4 workers)
    * Django
  * Used for development
    * OS System: Ubuntu 16.04 LTS
    * IDE : PyCharm Community 2016.3
  * Python libraries
    * django v2.0.4
    * djangorestframework v3.8.2
    * markdown v2.6.11
    * django-filter v1.1.0
    * psycopg2 v2.7.4
    * psycopg2-binary v2.7.4
    * celery v4.1.0
    * redis v2.10.6
    * django-rest-swagger v2.2.0
    * gunicorn v19.8.1

* Endpoints:
    * /docs
      * API documentation
    * /calls/
      * Start or finish a call
    * /bill/
      * Get call bills