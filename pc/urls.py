from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'pc.views.index', name='index'),
]