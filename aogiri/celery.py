import os

import celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aogiri.settings")

app = celery.Celery("aogiri")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
    
