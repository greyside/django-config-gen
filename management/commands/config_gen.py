from django.core.management.base import NoArgsCommand, CommandError
from django.conf import settings
from django.template.loader import render_to_string
from django.template import Template, Context
import defaults
import os
import shutil
import logging

logger = logging.getLogger(__name__)

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

if not hasattr(settings, 'HOST'):
	settings.HOST = defaults.HOST

TEMPLATES_DIR = settings.CONFIG_GEN_TEMPLATES_DIR
logger.debug(TEMPLATES_DIR)
GENERATED_DIR = settings.CONFIG_GEN_GENERATED_DIR
logger.debug(GENERATED_DIR)

class Command(NoArgsCommand):
	help = 'Generates configuration files for Apache, Nginx, etc. using values in settings.py and the Django template system.'
	
	def handle_noargs(self, **options):
		#get all templates in TEMPLATES_DIR, parse them, and output files in GENERATED_DIR
		#logging.debug(settings)
		ctx = Context(settings._wrapped.__dict__)
		
		if not os.path.exists(TEMPLATES_DIR):
			os.makedirs(TEMPLATES_DIR)
		
		if not os.path.exists(GENERATED_DIR):
			os.makedirs(GENERATED_DIR)
		
		dir_list=os.listdir(TEMPLATES_DIR)
		#if no templates are present, populate template directory with the examples
		if len(dir_list) is 0:
			logger.debug('dir_list was empty')
			example_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'example_templates')
			for filename in os.listdir(example_dir):
				shutil.copy2(os.path.join(example_dir, filename), TEMPLATES_DIR)
			dir_list=os.listdir(TEMPLATES_DIR)
		
		for filename in dir_list:
			fi = open(os.path.join(TEMPLATES_DIR, filename), 'r')
			t = Template(fi.read())
			fi.close()
			
			fo = open(os.path.join(GENERATED_DIR, filename), 'w')
			fo.write(t.render(ctx))
			fo.close()
