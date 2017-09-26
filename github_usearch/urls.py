from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .api import GithubUserSearchView, GithubUserDetailView
from .views import UserListView, UserDetailView, ReportView


github_api_urls = [
    url('^users/$', GithubUserSearchView.as_view(), name="github-user-list"),
    url('^users/(?P<username>.*)', GithubUserDetailView.as_view(), name="github-user-detail")
]

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name="login" ),
    url(r'^github/', include( github_api_urls )),
    url(r'^admin_panel/reports/$', ReportView.as_view()),
    url(r'^admin_panel/users/$', UserListView.as_view(), name="admin-user-list"),
    url(r'^admin_panel/users/(?P<username>.*)$', UserDetailView.as_view(), name="admin-user-detail"),
    url(r'^admin_panel/$', UserListView.as_view()),
    url(r'^$', UserListView.as_view())
]
