import os

bind = ["127.0.0.1:8000", "unix:/tmp/gunicorn.sock"]
chdir = "server"
workers = os.cpu_count() or 1
worker_class = "utils.workers.BeakleWorker"

wsgi_app = "main:app"