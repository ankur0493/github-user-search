from django.conf.urls import url, include

from .views import GithubUserSearchView

github_api_urls = [
    url('^users/', GithubUserSearchView.as_view(), name="github-user-list")
]

urlpatterns = [
    url(r'^github/', include( github_api_urls )),
]
