import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-cms-boilerplate",
    install_requires = [
        "django-mptt==0.5.2",
        "django-cms==2.4.3",
        "django-reversion==1.7",
    ],
    version = "0.1",
    author = "Benjamin Brinkman",
    author_email = "ben@benjaminbrinkman.com",
    description = ("Django-cms initial project template"),
    license = "MIT",
    keywords = "cms boilerplate django web",
    url = "http://packages.python.org/cms-boilerplate",
    packages=['cms-boilerplate'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
