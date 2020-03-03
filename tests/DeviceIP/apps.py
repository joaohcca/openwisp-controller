from django.apps import AppConfig

class BaseConfig(AppConfig):
    name = 'DeviceIP'
    label = 'DeviceIP.app'

    def ready(self):
        import DeviceIP.signals
