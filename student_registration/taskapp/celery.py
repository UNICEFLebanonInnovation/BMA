
from __future__ import absolute_import
import os
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # pragma: no cover


app = Celery('student_registration')


class CeleryConfig(AppConfig):
    name = 'student_registration.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.
        app.config_from_object('django.conf:settings', namespace='CELERY')
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)

        # if hasattr(settings, 'RAVEN_CONFIG'):
            # Celery signal registration
# Since raven is required in production only,
            # imports might (most surely will) be wiped out
            # during PyCharm code clean up started
            # in other environments.
            # @formatter:off
            # from raven import Client as RavenClient
            # from raven.contrib.celery import register_signal as raven_register_signal
            # from raven.contrib.celery import register_logger_signal as raven_register_logger_signal
# @formatter:on

            # raven_client = RavenClient(dsn=settings.RAVEN_CONFIG['DSN'])
            # raven_register_logger_signal(raven_client)
            # raven_register_signal(raven_client)

        if hasattr(settings, 'OPBEAT'):
# Since opbeat is required in production only,
            # imports might (most surely will) be wiped out
            # during PyCharm code clean up started
            # in other environments.
            # @formatter:off
            from opbeat.contrib.django.models import client as opbeat_client
            from opbeat.contrib.django.models import logger as opbeat_logger
            from opbeat.contrib.django.models import register_handlers as opbeat_register_handlers
            from opbeat.contrib.celery import register_signal as opbeat_register_signal
# @formatter:on

            try:
                opbeat_register_signal(opbeat_client)
            except Exception as e:
                opbeat_logger.exception('Failed installing celery hook: %s' % e)

            if 'opbeat.contrib.django' in settings.INSTALLED_APPS:
                opbeat_register_handlers()


@app.task(bind=True)
def debug_task(self):
    logger.info('Request: {0!r}'.format(self.request))  # pragma: no cover
