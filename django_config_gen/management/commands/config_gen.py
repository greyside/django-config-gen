from django.core.management.base import NoArgsCommand, CommandError
from django.conf import settings
from django.template.loader import render_to_string
from django.template import Template, Context
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
from .. import patch_settings
import os
import shutil
import logging

logger = logging.getLogger(__name__)

patch_settings()

TEMPLATES_DIR = settings.CONFIG_GEN_TEMPLATES_DIR
#logger.debug(TEMPLATES_DIR)
GENERATED_DIR = settings.CONFIG_GEN_GENERATED_DIR
#logger.debug(GENERATED_DIR)
CONTEXT_PROCESSORS = settings.CONFIG_GEN_CONTEXT_PROCESSORS

class Command(NoArgsCommand):
	help = 'Generates configuration files for Apache, Nginx, etc. using values in settings.py and the Django template system.'
	ctx = None
	
	def handle_noargs(self, **options):
		#get all templates in TEMPLATES_DIR, parse them, and output files in GENERATED_DIR
		#logging.debug(settings)
		self.ctx = Context(settings._wrapped.__dict__)
		
		#run context processors
		for path in CONTEXT_PROCESSORS:
			logger.debug('Processing Context Processor: %s' % path)
			#these next 10 lines were taken from Django (file: django/template/context.py), which is under a BSD license
			i = path.rfind('.')
			module, attr = path[:i], path[i+1:]
			try:
				mod = import_module(module)
			except ImportError, e:
				raise ImproperlyConfigured('Error importing config processor module %s: "%s"' % (module, e))
			try:
				func = getattr(mod, attr)
			except AttributeError:
				raise ImproperlyConfigured('Module "%s" does not define a "%s" callable request processor' % (module, attr))
			
			d = func()
			logger.debug(d)
			self.ctx.update(d)
		
		if not os.path.exists(TEMPLATES_DIR):
			os.makedirs(TEMPLATES_DIR)
		
		if not os.path.exists(GENERATED_DIR):
			os.makedirs(GENERATED_DIR)
		
		dir_list=os.listdir(TEMPLATES_DIR)
		#if no templates are present, populate template directory with the examples
		if len(dir_list) is 0:
			logger.debug('%s was empty' % TEMPLATES_DIR)
			example_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'example_templates')
			for filename in os.listdir(example_dir):
				shutil.copy2(os.path.join(example_dir, filename), TEMPLATES_DIR)
			dir_list=os.listdir(TEMPLATES_DIR)
		
		logger.debug(self.ctx)
		self.create_nodes('', dir_list)
	
	def create_nodes(self, rel_path, dir_list):
		for filename in dir_list:
			logger.debug('Filename: %s' % filename)
			t_filename = os.path.join(TEMPLATES_DIR, rel_path, filename)
			g_filename = os.path.join(GENERATED_DIR, rel_path, filename)
			if os.path.isfile(t_filename):
				fi = open(t_filename, 'r')
				t = Template(fi.read())
				fi.close()
			
				fo = open(g_filename, 'w')
				fo.write(t.render(self.ctx))
				fo.close()
			elif os.path.isdir(t_filename):
				if not os.path.exists(g_filename):
					logger.debug('Creating directory')
					os.mkdir(g_filename)
				self.create_nodes(filename, os.listdir(t_filename))
