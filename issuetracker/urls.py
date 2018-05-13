from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^issue/$', views.IssueList.as_view() , name='issue_list'),
	url(r'^issue/(?P<pk>[0-9]+)/$', views.IssueDetail.as_view(), name='issue_detail'),
]
