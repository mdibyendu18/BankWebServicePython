from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bankapi import views

urlpatterns = [
    url(r'^branch/(?P<ifsc>.+)/$', views.BranchView.as_view(), name='branch-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)