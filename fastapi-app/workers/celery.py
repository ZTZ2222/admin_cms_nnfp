from celery import Celery

from core.config import settings


def configure_celery() -> Celery:
    celery_app = Celery("worker", include=["tasks.celery"])
    celery_app.conf.enable_utc = True
    celery_app.conf.timezone = settings.celery.timezone
    celery_app.conf.broker_url = settings.celery.broker_url
    celery_app.conf.result_backend = settings.celery.result_backend
    return celery_app


celery_app = configure_celery()
