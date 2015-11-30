# -*- coding: utf-8 -*-
#Copyright (C) 2010, 2011 Seán Hayes
#
#Licensed under a BSD 3-Clause License. See LICENSE file.

import os
import shutil
import tempfile

from django.conf import settings
from django.core.management import call_command
from django.test import override_settings, TestCase

from django_config_gen.management import patch_settings


try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


config_dir = os.path.join(tempfile.gettempdir(), 'config')


@override_settings(
    CONFIG_GEN_TEMPLATES_DIR=os.path.join(config_dir, 'templates'),
    CONFIG_GEN_GENERATED_DIR=os.path.join(config_dir, 'generated')
)
class CallCommandTestCase(TestCase):
    def setUp(self):
        self.tmp_files = []

    def tearDown(self):
        for tmp_file in self.tmp_files:
            try:
                os.remove(tmp_file)
            except FileNotFoundError:
                pass

        shutil.rmtree(config_dir)

    def test_handles_unicode_in_file_contents(self):
        "Make sure unicode is supported in file contents."

        test_file_name = 'test_file'
        test_file_template_path = os.path.join(settings.CONFIG_GEN_TEMPLATES_DIR, test_file_name)
        test_file_generated_path = os.path.join(settings.CONFIG_GEN_GENERATED_DIR, test_file_name)
        self.tmp_files.append(test_file_template_path)
        self.tmp_files.append(test_file_generated_path)

        if not os.path.exists(settings.CONFIG_GEN_TEMPLATES_DIR):
            os.makedirs(settings.CONFIG_GEN_TEMPLATES_DIR)

        config_template = u"""
This is some text with unicode!
-Seán Hayes
""".encode('utf-8')

        fo = open(test_file_template_path, 'wb')
        fo.write(config_template)
        fo.close()

        self.assertTrue(os.path.exists(test_file_template_path))
        self.assertFalse(os.path.exists(test_file_generated_path))

        call_command('config_gen')

        fi = open(test_file_generated_path, 'rb')
        generated_text = fi.read()
        fi.close()

        self.assertTrue(os.path.exists(test_file_generated_path))
        #make sure the unicode didn't get silently mangled
        self.assertEqual(config_template, generated_text)


    def test_copies_sub_folder_contents(self):
        "Make sure unicode is supported in file contents."
        os.makedirs(os.path.join(settings.CONFIG_GEN_TEMPLATES_DIR, 'foo', 'bar'))

        test_file_name = 'test_file'
        test_file_template_path = os.path.join(settings.CONFIG_GEN_TEMPLATES_DIR, 'foo', 'bar', test_file_name)
        test_file_generated_path = os.path.join(settings.CONFIG_GEN_GENERATED_DIR, 'foo', 'bar', test_file_name)
        self.tmp_files.append(test_file_template_path)
        self.tmp_files.append(test_file_generated_path)

        if not os.path.exists(settings.CONFIG_GEN_TEMPLATES_DIR):
            os.makedirs(settings.CONFIG_GEN_TEMPLATES_DIR)

        config_template = u"""
This is some text with unicode!
-Seán Hayes
""".encode('utf-8')

        fo = open(test_file_template_path, 'wb')
        fo.write(config_template)
        fo.close()

        self.assertTrue(os.path.exists(test_file_template_path))
        self.assertFalse(os.path.exists(test_file_generated_path))

        call_command('config_gen')

        fi = open(test_file_generated_path, 'rb')
        generated_text = fi.read()
        fi.close()

        self.assertTrue(os.path.exists(test_file_generated_path))
        #make sure the unicode didn't get silently mangled
        self.assertEqual(config_template, generated_text)
