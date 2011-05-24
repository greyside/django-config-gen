# -*- coding: utf-8 -*-
#Copyright (C) 2010, 2011 Seán Hayes
#
#Licensed under a BSD 3-Clause License. See LICENSE file.

from django.core.management.base import NoArgsCommand, CommandError
from django.conf import settings
from .. import patch_settings
import json
import copy
import logging

logger = logging.getLogger(__name__)

class NullHandler(logging.Handler):
	def emit(self, record):
		pass

patch_settings()

class Command(NoArgsCommand):
	help = 'Prints out settings serialized as JSON.'
	
	def handle_noargs(self, **options):
		#remove logging statements from output
		l = logging.getLogger('')
		for h in l.handlers:
			l.removeHandler(h)
		l.addHandler(NullHandler())
		
		d = {}
		s_d = settings._wrapped.__dict__
		for key in settings._wrapped.__dict__:
			val = s_d[key]
			logger.debug('%s: %s' % (key, val))
			try:
				#if settings has something like "import django.conf.global_settings as DEFAULT_SETTINGS"
				#in it, then json encoding will throw and error. Copying makes
				#sure modules don't get included.
				d[key] = copy.copy(val)
			except Exception as e:
				logger.error(e)
		print json.dumps(d, indent=4, sort_keys=True)
