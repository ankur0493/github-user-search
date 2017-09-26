A Simple GitHub User Search Application
=======================================

This is a very simple application that exposes an API to search Github users, as well as get public details for those users. It also maintains a local copy of all the users searched for and provides a clean admin interface to view and search local users. In addition, reports are also available for the number of local users created as well as the number of times Github API was hit.

Installation
============

- Preferred way is to install it inside a virtualenvironment
- Make sure you have Python 2.7 installed on your machine
- Install pip and virtualenvironment if not already installed
  ```
  sudo apt-get update
  sudo apt-get install python-pip
  sudo pip install virtualenv
  ```
- Create a directory to store your virtual enironments (if does not already exist):
  ```
  mkdir ~/env/
  ```
- Create a virtualenv for the project:

  ```
  virtualenv --python=/usr/bin/python2.7 ~/env/github-usearch
  ```
- Activate the virtual environment:

  ```
  source ~/env/github-usearch/bin/activate
  ```
- Further Steps:
  ```
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py loaddata github_usearch/fixtures/*
  python manage.py runserver
  ```

API Endpoints
=============

- Github Search API: `/github/users`
- Github User Detail API: `/github/users/:username`

Search Parameters
=================

Search is available in the Github User Search API as well as in the admin panel. Both Searches follow the syntax as specified in `https://help.github.com/articles/searching-users/`
