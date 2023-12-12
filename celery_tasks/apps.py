from django.apps import AppConfig


class CeleryTasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'celery_tasks'

    def ready(self):
        from celery_tasks.signals import init_signals
        init_signals()
        return super(CeleryTasksConfig, self).ready()