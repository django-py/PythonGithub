.. image::
    https://raw.githubusercontent.com/nicchub/PythonGithub/master/images/PythonGithub.png

PythonGithub is a Library for communicating with the `GitHub API <https://developer.github.com/v3/>`_. The goal of the library is to support 100% of the GitHub v3 API.

.. image:: https://api.travis-ci.org/nicchub/PythonGithub.png?branch=master
   :target: https://travis-ci.org/nicchub/PythonGithub

.. image:: https://badge.fury.io/py/PythonGithubAPI.png
   :target: http://badge.fury.io/py/PythonGithubAPI

.. image:: https://pypip.in/d/PythonGithubAPI/badge.png
   :target: https://pypip.in/d/PythonGithubAPI/badge.png

Requirements
=====================
Tested with: Python 2.6, Python 2.7 and Python 3.2.

Installation:
=====================
::
    
    pip install -U PythonGithub

Quickstart
=====================
PythonGithub is easy, the most simple method is `zen() <https://api.github.com/zen>`_ that don't required authentication.

api.zen()
**********************
Returns a ramdon selection of the github design philosophy.
::

    from github import api
    
    api.zen()
    > u'Mind your words, they are important.'


api.users.get()
**********************
Get all information about a specific github username.  
::

    from github import api
    
    user = api.users.get('nicchub')
    
    user.name
    > u'Nicco'
    user.login
    > u'nicchub'

    
Documentation
====================

Examples
====================

Contribute guide
===================

Testing
===================
