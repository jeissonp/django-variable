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
Django >= 1.10

Afterwards, run::

    python manage.py migrate


Administration
--------------

Go to admin/django_variable/configuration


All done.