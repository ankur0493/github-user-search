from __future__ import unicode_literals

import datetime

from django.views.generic.base import TemplateView

from .models import GithubUserData

class AdminPanelHomeView(TemplateView):

    template_name = "admin_panel.html"

    def get_context_data(self, **kwargs):
        context = super(AdminPanelHomeView, self).get_context_data(**kwargs)
        context['users'] = GithubUserData.objects.all().order_by('-created')[:10]
        return context

class AdminPanelReportView(TemplateView):

    template_name = "admin_panel_reports.html"

    def get_context_data(self, **kwargs):
        context = super(AdminPanelReportView, self).get_context_data(**kwargs)
        today = datetime.datetime.today()
        context['users_today'] = GithubUserData.objects.filter(
            created__day=today.day, created__month=today.month, created__year=today.year).count()
        context['users_week'] = GithubUserData.objects.filter(
            created__range=((today - datetime.timedelta(days=7)), today)).count()
        context['users_month'] = GithubUserData.objects.filter(
            created__month=today.month).count()
        return context
