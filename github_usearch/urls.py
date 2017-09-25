from django.conf.urls import url, include

from .api import GithubUserSearchView
from .views import AdminPanelHomeView, AdminPanelReportView


github_api_urls = [
    url('^users/', GithubUserSearchView.as_view(), name="github-user-list")
]

urlpatterns = [
    url(r'^github/', include( github_api_urls )),
    url(r'admin_panel/reports/$', AdminPanelReportView.as_view()),
    url(r'admin_panel/$', AdminPanelHomeView.as_view())
]
