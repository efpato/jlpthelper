#!/usr/bin/env python
import os
import django
import sys
from home import models
from kanji_analyzer import models

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jlpthelper.settings")
    django.setup()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
