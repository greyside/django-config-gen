#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

version = '1.0.0'

setup(name='django-config-gen',
	version=version,
	description="Generates configuration files for Apache, Nginx, etc. using values in settings.py and the Django template system. You can write your own templates for whatever text based config file you need.",
	author='Seán Hayes',
	author_email='sean@seanhayes.name',
	keywords='django configuration generator',
	url='https://github.com/SeanHayes/django-config-gen',
	license='BSD',
	packages=['django_config_gen'],
	install_requires=['django',],
)

