django-cms-boilerplate
======================

Simplified Django-cms installation

I wanted to create a default django project for use with django-cms.  The django-cms tutorial tells you how to do this, but I wanted to have a framework readily available.  It currently uses Django-cms 2.4.3 and Python 2.7.x.  I plan to support Django-cms 3.0 and Python 3.x in the future and it will probably be in a separate repo under a different name.

Usage:

Using a virtualenv is recommended.

pip install virtualenv

virtualenv cms-env

source cms-env/bin/activate

Then to install within the virtualenv (this project currently only has a beta release, USE WITH CAUTION, however, testing is appreciated):

pip install django-cms-boilerplate==1.0beta2

Then use

cms-admin.py startproject [YOUR PROJECT NAME]

anywhere in the filesystem to create a default django cms project template.  Comes with HTML and CSS Templates based on Bootstrap to get you started quickly.
