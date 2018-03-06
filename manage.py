#!/usr/bin/env python

import os
import sys
from dotenv import load_dotenv


if __name__ == "__main__":
    project_folder = os.path.expanduser('~/PycharmProjects/otus_dz7_site_otus/')
    load_dotenv(os.path.join(project_folder, '.env'))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_site_otus.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
