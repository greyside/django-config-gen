from django.core.management.base import NoArgsCommand, CommandError
from django.conf import settings
from django.template.loader import render_to_string
from django.template import Template, Context
import os
import logging

CONFIG_DIR = settings.CONFIG_GEN_CONFIG_DIR if hasattr(settings, 'CONFIG_GEN_CONFIG_DIR') else 'config/'
TEMPLATES_DIR = settings.CONFIG_GEN_TEMPLATES_DIR if hasattr(settings, 'CONFIG_GEN_TEMPLATES_DIR') else '%stemplates/' % CONFIG_DIR
GENERATED_DIR = settings.CONFIG_GEN_GENERATED_DIR if hasattr(settings, 'CONFIG_GEN_GENERATED_DIR') else '%sgenerated/' % CONFIG_DIR

class Command(NoArgsCommand):
	help = 'Generates configuration files for Apache, Nginx, etc. using values in settings.py and the Django template system.'
	
	def handle_noargs(self, **options):
		#get all templates in TEMPLATES_DIR, parse them, and output files in GENERATED_DIR
		#logging.debug(settings)
		ctx = Context(dict(settings._wrapped))
		
		if not os.path.exists(CONFIG_DIR):
			os.makedirs(CONFIG_DIR)
		
		if not os.path.exists(TEMPLATES_DIR):
			os.makedirs(TEMPLATES_DIR)
		
		if not os.path.exists(GENERATED_DIR):
			os.makedirs(GENERATED_DIR)
		
		dir_list=os.listdir(TEMPLATES_DIR)
		for filename in dir_list:
			fi = open('%s%s' % (TEMPLATES_DIR, filename), 'r')
			t = Template(fi.read())
			fi.close()
			
			fo = open('%s%s' % (GENERATED_DIR, filename), 'w')
			fo.write(t.render(ctx))
			fo.close()
