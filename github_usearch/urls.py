from django.conf.urls import url, include

from .api import GithubUserSearchView
from .views import UserListView, UserDetailView, ReportView


github_api_urls = [
    url('^users/', GithubUserSearchView.as_view(), name="github-user-list")
]

urlpatterns = [
    url(r'^github/', include( github_api_urls )),
    url(r'admin_panel/reports/$', ReportView.as_view()),
    url(r'admin_panel/users/$', UserListView.as_view(), name="admin-user-list"),
    url(r'admin_panel/users/(?P<username>.*)$', UserDetailView.as_view(), name="admin-user-detail"),
    url(r'admin_panel/$', UserListView.as_view())
]
