PythonGithub
=====================
PythonGithub is a library(wrapper) for the Github API V3. 

.. image:: https://api.travis-ci.org/nicchub/PythonGithub.png?branch=master
   :target: https://travis-ci.org/nicchub/PythonGithub

.. image:: https://badge.fury.io/py/PythonGithubAPI.png
   :target: http://badge.fury.io/py/PythonGithubAPI

.. image:: https://pypip.in/d/PythonGithubAPI/badge.png
   :target: https://pypip.in/d/PythonGithubAPI/badge.png

Requirements
=====================
Python: 2.6, 2.7 o 3.2

Quickstart
=====================
from github import api

user = api.users.get(username='nicchub')
user.objects.username
