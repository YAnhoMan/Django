from django.conf.urls import url

from . import views

urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    url(r'^index/$', views.index, name='index'),
    url(r'say/', views.say, name='say')
]