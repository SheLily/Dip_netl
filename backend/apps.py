from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'backend'

    def ready(self):
        """
        импортируем сигналы
        """

        from backend import signals
