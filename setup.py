#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import django_config_gen

package_name = 'django_config_gen'
test_package_name = '%s_test_project' % package_name

setup(name='django-config-gen',
	version=django_config_gen.__version__,
	description="Generates configuration files for Apache, Nginx, etc. using values in settings.py and the Django template system. You can write your own templates for whatever text based config file you need.",
	author='Seán Hayes',
	author_email='sean@seanhayes.name',
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Framework :: Django",
		"Intended Audience :: Developers",
		"Intended Audience :: System Administrators",
		"License :: OSI Approved :: BSD License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.6",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
		"Topic :: Internet :: WWW/HTTP :: Site Management",
		"Topic :: Software Development :: Build Tools",
		"Topic :: Software Development :: Code Generators",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules"
	],
	keywords='django configuration generator',
	url='http://seanhayes.name/',
	download_url='https://github.com/SeanHayes/django-config-gen',
	license='BSD',
	packages=[
		'django_config_gen',
		'django_config_gen_test_project',
	],
	package_data={'django_config_gen': ['management/commands/example_templates/*']},
	include_package_data=True,
	install_requires=['Django>=1.2',],
	test_suite = '%s.runtests.runtests' % test_package_name,
)

