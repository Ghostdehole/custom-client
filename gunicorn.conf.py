import os

bind = "0.0.0.0:9000"
workers = 4
timeout = 120
max_requests = 1000
max_requests_jitter = 100
wsgi_app = "gdpro.wsgi.application"
