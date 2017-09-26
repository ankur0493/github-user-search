from __future__ import unicode_literals

import datetime

from django.views import generic
from django.shortcuts import get_object_or_404

from .models import GithubUserData

class UserListView(generic.list.ListView):

    model = GithubUserData
    template_name = "user_list.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        #context['users'] = GithubUserData.objects.all().order_by('-created')[:10]
        return context


class UserDetailView(generic.detail.DetailView):

    model = GithubUserData
    template_name = "user_detail.html"

    def get_object(self, **kwargs):
        return get_object_or_404(self.model, username=self.kwargs.get("username", ""))

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        return context


class ReportView(generic.base.TemplateView):

    template_name = "admin_panel_reports.html"

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        today = datetime.datetime.today()
        context['users_today'] = GithubUserData.objects.filter(
            created__day=today.day, created__month=today.month, created__year=today.year).count()
        context['users_week'] = GithubUserData.objects.filter(
            created__range=((today - datetime.timedelta(days=7)), today)).count()
        context['users_month'] = GithubUserData.objects.filter(
            created__month=today.month).count()
        return context
