# -*- coding: utf-8 -*-
#Copyright (C) 2010, 2011 Seán Hayes
#
#Licensed under a BSD 3-Clause License. See LICENSE file.

from django.conf import settings
import os
import defaults

def patch_settings():
	if not hasattr(settings, 'PROJECT_ROOT'):
		settings.PROJECT_ROOT = defaults.PROJECT_ROOT
	
	if not hasattr(settings, 'PROJECT_PARENT_DIR'):
		settings.PROJECT_PARENT_DIR = os.path.dirname(settings.PROJECT_ROOT)
	
	if not hasattr(settings, 'LOG_DIR'):
		settings.LOG_DIR = defaults.LOG_DIR
	
	if not hasattr(settings, 'CONFIG_GEN_TEMPLATES_DIR'):
		settings.CONFIG_GEN_TEMPLATES_DIR = defaults.TEMPLATES_DIR
	
	if not hasattr(settings, 'CONFIG_GEN_GENERATED_DIR'):
		settings.CONFIG_GEN_GENERATED_DIR = defaults.GENERATED_DIR
	
	if not hasattr(settings, 'CONFIG_GEN_CONTEXT_PROCESSORS'):
		settings.CONFIG_GEN_CONTEXT_PROCESSORS = defaults.CONTEXT_PROCESSORS
	
	if not hasattr(settings, 'HOST'):
		settings.HOST = defaults.HOST
