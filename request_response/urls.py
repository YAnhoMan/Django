from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^weather/(?P<area>\w+)/(?P<year>\d{4})/$', views.weather),
    url(r'get/', views.query),
    url(r'get_body/', views.get_body),
    url(r'post_json/', views.post_json),
    url(r'register/', views.Register.as_view(), name='register')
]