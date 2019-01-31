from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$',views.youtube_fetch,name='youtube_fetch'),
    url('^$',views.index,name='index')
]
