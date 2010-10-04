from django.core.management.base import NoArgsCommand, CommandError
from django.conf import settings
from django.template.loader import render_to_string
from django.template import Template, Context
import os
import logging

class Command(NoArgsCommand):
	help = 'Generates configuration files for Apache, Nginx, etc. using values in settings.py and the Django template system.'
	
	def handle_noargs(self, **options):
		#get all templates in config/templates/, parse them, and output files in config/
		#logging.debug(settings)
		ctx = Context(settings._wrapped.__dict__)
		config_dir = 'config/'
		templates_dir = '%stemplates/' % config_dir
		output_dir = '%sgenerated/' % config_dir
		
		if not os.path.exists(templates_dir):
			os.makedirs(templates_dir)
		
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		
		dir_list=os.listdir(templates_dir)
		for filename in dir_list:
			fi = open('%s%s' % (templates_dir, filename), 'r')
			t = Template(fi.read())
			fi.close()
			
			fo = open('%s%s' % (output_dir, filename), 'w')
			fo.write(t.render(ctx))
			fo.close()
