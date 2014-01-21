django-cms-boilerplate
======================

Simplified Django-cms installation

I wanted to create a default django project for use with django-cms.  The django-cms tutorial tells you how to do this, but I wanted to have a framework readily available.  It currently uses Django-cms 2.4.3 and Python 2.7.x.  I plan to support Django-cms 3.0 and Python 3.x in the future and it will probably be in a separate repo under a different name.

Usage:

Just install with "python setup.py install".  Then use "cms-admin.py startproject [YOUR PROJECT NAME]" anywhere in the filesystem to create a default django cms project template.  Comes with HTML and CSS Templates based on Bootstrap to get you started quickly.  There's a few bugs with cms-admin.py if you don't include "startproject".  Not a big deal, just a misleading error message to an end-user.  Once I fix that, my plan is to upload a beta release to PyPI so you can just use pip.
