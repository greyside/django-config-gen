=================
django-config-gen
=================

**Maintenance/updates now handled by brillgen/django-config-gen:** https://github.com/brillgen/django-config-gen

.. image:: https://travis-ci.org/greyside/django-config-gen.svg
    :target: https://travis-ci.org/greyside/django-config-gen
    :alt: CI

.. image:: https://coveralls.io/repos/greyside/django-config-gen/badge.svg?service=github
    :target: https://coveralls.io/github/greyside/django-config-gen
    :alt: Code Coverage

.. image:: https://img.shields.io/pypi/v/django-config-gen.svg
    :target: https://pypi.python.org/pypi/django-config-gen
    :alt: Version

.. image:: https://img.shields.io/pypi/dm/django-config-gen.svg
    :target: https://pypi.python.org/pypi/django-config-gen
    :alt: Downloads

Generates configuration files for Apache, Nginx, etc. using values in
settings.py and the Django template system. You can write your own templates
for whatever text based config file you need.

Install
=======

Requires:
---------

* Python 2.7+ or Python 3.4+
* Django 1.7 through Django 1.9

1. `pip install django-config-gen`

2. Add 'django_config_gen' to your `INSTALLED_APPS`.

Usage
=====

Run './manage.py config_gen' on the command line in your project directory.

Templates for your config files go in:
<project_path>/config/templates/

All text files in that directory are loaded with the Django template system
using values from settings.py as Context. The output of each file is saved with
the same filename but in the following directory:
<project_path>/config/generated/

These output directories can be customized using CONFIG_GEN_TEMPLATES_DIR and CONFIG_GEN_GENERATED_DIR in settings.py.

Example templates are provided in 'django-config-gen/django_config_gen/management/commands/example_templates'. If the folder specified by CONFIG_GEN_TEMPLATES_DIR is empty then these will be copied there and used for generating templates.

Default Variables
=================

Some default variables are used in the Context used to render the config files,
and they can be manually overridden in settings.py.

PROJECT_ROOT
The absolute path to the directory your manage.py is in.

LOG_DIR
A directory called 'logs/' within your PROJECT_ROOT.

CONFIG_GEN_TEMPLATES_DIR
A directory called 'config/templates/' in your PROJECT_ROOT.

CONFIG_GEN_GENERATED_DIR
A directory called 'config/generated/' in your PROJECT_ROOT.

CONFIG_GEN_CONTEXT_PROCESSORS
A list of custom context processors that are to be used when rendering config
files. Example:

settings.py:

.. code:: python

    CONFIG_GEN_CONTEXT_PROCESSORS = ['myapp.config_context_processors.foo']

myapp/config_context_processors.py:

.. code:: python

    def foo(*args, **kwargs):
        return {'foo': 'bar'}

Nothing is currently passed in to the context processors but that may change in
the future, so using *args and **kwargs in the method signature will help
ensure forward compatibility.

HOST
The hostname specified in your database for the current Site. If
`./manage.py syncdb` hasn't been run yet, the value 'localhost' is used.

Contributing
============

You can fork this project on GitHub: http://github.com/greyside/django-config-gen.

License
=======

This project is licensed under the BSD License.
http://www.opensource.org/licenses/bsd-license.php

Links
=====

https://github.com/greyside/django-config-gen
http://pypi.python.org/pypi/django-config-gen
http://djangopackages.com/packages/p/django-config-gen/
