from os import getenv

if getenv('JLPT_ENV') == 'development':
    from .development import *
else:
    from .production import *
