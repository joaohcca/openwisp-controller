from django.conf.urls import include, url
from .views import portal,vagalume_status,vagalume_discovery,vagalume_inventary
urlpatterns = [
    url(r'^vagalumen/', vagalume_status),
    url(r'^discovery/', vagalume_discovery),
    url(r'^inventory/', vagalume_inventary),
    url(r'^$', portal),
]
