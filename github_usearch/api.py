from __future__ import unicode_literals

import json

from rest_framework import views, response

from .constants import GITHUB_USER_SEARCH_URL
from .interface import invoke_github_api
from .models import GithubUserData, ApiRequestsLog
from .serializers import GitHubUserSearchSerializer

class GithubUserSearchView(views.APIView):

    def get_search_term(self, request):
        query_params = request.query_params
        q = query_params.get("q", "")
        for param in query_params:
            if param != "q":
                q += "+" if q else ""
                q += param + ":" + query_params[param]
        return "?q=" + q

    def _create(self, data):
        bulk_create_objs = []
        for obj_data in data:
            try:
                obj = GithubUserData.objects.get(github_id=obj_data['github_id'])
                for (key, value) in obj_data.items():
                    setattr(obj, key, value)
                obj.save()
            except GithubUserData.DoesNotExist:
                bulk_create_objs.append(GithubUserData(**obj_data))
        if bulk_create_objs:
            GithubUserData.objects.bulk_create(bulk_create_objs)

    def get(self, request):
        search_params = self.get_search_term(request)
        url = GITHUB_USER_SEARCH_URL + search_params
        r = invoke_github_api(url, "GET")
        ApiRequestsLog.objects.create(queryparams=search_params[3:])
        serializer = GitHubUserSearchSerializer(data=json.loads(r.content)["items"], many=True)
        serializer.is_valid(raise_exception=True)
        self._create(serializer.data)
        return response.Response(data=serializer.data)
