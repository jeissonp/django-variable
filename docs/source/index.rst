.. _installation:

Installation
============

Requirements
------------

* Python 2.7, 3.4, 3.5, 3.6 or 3.7
* Django >= 5

Pip
---

::

    pip install django-variable

Configuration
-------------

::

    # settings.py

    INSTALLED_APPS = [
        # ...

        'django_variable',
    ]
Django >= 5

Afterwards, run::

    python manage.py migrate


Administration
--------------

Go to admin/django_variable/configuration


Usage
=====

Import function get_config
------------------------
::

    from django_variable.utils import get_config

    get_config('NAME_VARIABLE', 'DEFAULT_VALUE')

All done.