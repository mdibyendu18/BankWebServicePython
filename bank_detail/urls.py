from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bank_detail import views

urlpatterns = [
    url(r'^branch/(?P<ifsc>.+)/$', views.BranchView.as_view(), name='branch-detail'),
    url(r'^bank/(?P<bank_name>.+)/city/(?P<city>.+)$', views.BankBranchView.as_view(), name='bank-branch-detail'),
    #url(r'^city/(?P<city>.+)$', views.BankBranchView.as_view(), name='bank-branch-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)