from django.apps import AppConfig
from django.conf import settings

from elasticsearch_dsl.connections import connections
from elasticsearch.exceptions import NotFoundError

from .search import Question, Answer

class QAConfig(AppConfig):
    name = 'qa'
    verbose_name = "Q & A"

    def ready(self):
        connections.configure(**settings.ES_CONNECTIONS)
