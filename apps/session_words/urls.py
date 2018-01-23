from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'session_words/$', views.index, name='index'),
    url(r'session_words/process/$', views.process, name='process'),
    url(r'session_words/clear/$', views.clear, name='clear')
]