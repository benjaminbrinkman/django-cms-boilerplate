django-cms-boilerplate
======================

Simplified Django-cms installation

I wanted to create a default django project for use with django-cms.  The django-cms tutorial tells you how to do this, but I wanted to have a framework readily available.  It currently uses Django-cms 2.4.3 and Python 2.7.x.  I plan to support Django-cms 3.0 and Python 3.x in the future and it will probably be in a separate repo under a different name.

Usage:

Using a virtualenv is recommended.

pip install virtualenv

virtualenv cms-env

source cms-env/bin/activate

Then to install within the virtualenv:

pip install django-cms-boilerplate

Then use

cms-admin.py startproject [YOUR PROJECT NAME]

anywhere in the filesystem to create a default django cms project template.  Comes with HTML and CSS Templates based on Bootstrap to get you started quickly.  Please note, there is a known issue of an incompatibility between Bootstrap and the inline editing feature in Django-cms, which affects the default theme.  It prevents use of the cms_toolbar in the default theme.  I will be working on submitting a patch to upstream that resolves this.
