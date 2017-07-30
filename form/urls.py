from django.conf.urls import url
from views import CreateClient


urlpatterns = [
    url(r'^$', CreateClient.as_view())
]
