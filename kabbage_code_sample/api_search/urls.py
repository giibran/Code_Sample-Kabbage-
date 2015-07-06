from django.conf.urls import patterns, url
from api_search import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^api/search/$', views.SearchView.as_view(), name='search'),
)
