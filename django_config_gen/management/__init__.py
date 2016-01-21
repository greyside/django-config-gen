# -*- coding: utf-8 -*-
#Copyright (C) 2010, 2011 Seán Hayes
#
#Licensed under a BSD 3-Clause License. See LICENSE file.

from django.conf import settings
import os
from . import defaults


_names = {
    'PROJECT_ROOT': 'PROJECT_ROOT',
    'PROJECT_PARENT_DIR': 'PROJECT_ROOT',
    'LOG_DIR': 'LOG_DIR',
    'CONFIG_GEN_TEMPLATES_DIR': 'TEMPLATES_DIR',
    'CONFIG_GEN_GENERATED_DIR': 'GENERATED_DIR',
    'CONFIG_GEN_CONTEXT_PROCESSORS': 'CONTEXT_PROCESSORS',
    'HOST': 'HOST',
}


def patch_settings():
    for setting, default in _names.items():
        if not hasattr(settings, setting):
            setattr(settings, setting, getattr(defaults, default))
