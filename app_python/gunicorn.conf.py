'''Gunicorn configuration file'''

import multiprocessing

# pylint: disable=invalid-name
wsgi_app = 'main:app'
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
