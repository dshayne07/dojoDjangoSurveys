from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'survey_app/$', views.index, name='index'),
    url(r'survey_app/process/$', views.process, name='process'),
    url(r'survey_app/result/$', views.result, name='result')
]