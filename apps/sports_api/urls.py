from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^baseball$', views.baseball, name="baseball"),
    url(r'^basketball$', views.basketball, name="basketball"),
    url(r'^soccer$', views.soccer, name="soccer"),
    url(r'^alllive$', views.alllive, name="alllive"),
]