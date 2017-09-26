from __future__ import unicode_literals

import datetime

from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import GithubUserData, ApiRequestsLog

class UserListView(LoginRequiredMixin, generic.list.ListView):

    model = GithubUserData
    template_name = "user_list.html"
    paginate_by = 15
    ordering = 'created'

    def _get_user_type(self, raw_type):
        type_user = ("user", "usr")
        type_org = ("org", "organization", "organisation")
        if raw_type.lower() in type_user:
            return "User"
        elif raw_type.lower() in type_org:
            return "Organization"
        return ""

    def get_queryset(self, **kwargs):
        queryset = super(UserListView, self).get_queryset(**kwargs)

        query = self.request.GET.get("q")
        if query:
            query_params = query.split()
            search_terms = []
            search_restriction = ("username", "email")
            for q in query_params:
                if len(q.split(":", 1)) == 2:
                    filter_field, filter_text = q.split(":", 1)
                else:
                    search_terms.append(q)
                    continue
                if filter_field == "type":
                    queryset = queryset.filter(Q(user_type=self._get_user_type(filter_text)))
                elif filter_field == "location":
                    queryset = queryset.filter(Q(location__icontains=filter_text))
                elif filter_field == "created":
                    if filter_text.startswith("<"):
                        date = dateutil.parser.parse("filter_text[1:]")
                        queryset = queryset.filter(Q(github_created__lt=date))
                    elif filter_text.startswith("<="):
                        date = dateutil.parser.parse("filter_text[2:]")
                        queryset = queryset.filter(Q(github_created__lte=date))
                    elif filter_text.startswith(">"):
                        date = dateutil.parser.parse("filter_text[1:]")
                        queryset = queryset.filter(Q(github_created__gt=date))
                    elif filter_text.startswith(">="):
                        date = dateutil.parser.parse("filter_text[2:]")
                        queryset = queryset.filter(Q(github_created__gte=date))
                    elif len(filter_text.split("..")) == 2:
                        range_l, range_r = filter_text.split("..")
                        queryset = queryset.filter(Q(github_created__range=(
                                       dateutil.parser.parse(range_l),
                                       dateutil.parser.parse(range_r))))
                elif filter_field == "in":
                    search_restriction = filter_text.split(",")
            q_query = None
            for search_term in search_terms:
                for search_field in search_restriction:
                    if q_query:
                        q_query = q_query | Q(**{search_field + "__icontains": search_term})
                    else:
                        q_query = Q(**{search_field + "__icontains": search_term})
            queryset = queryset.filter(q_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return context


class UserDetailView(generic.detail.DetailView, LoginRequiredMixin):

    model = GithubUserData
    template_name = "user_detail.html"

    def get_object(self, **kwargs):
        return get_object_or_404(self.model, username=self.kwargs.get("username", ""))

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        return context


class ReportView(generic.base.TemplateView, LoginRequiredMixin):

    template_name = "admin_panel_reports.html"

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        today = datetime.datetime.today()
        week_range = ((today - datetime.timedelta(days=7)), today)
        context['users_today'] = GithubUserData.objects.filter(
            created__day=today.day, created__month=today.month, created__year=today.year).count()
        context['users_week'] = GithubUserData.objects.filter(
            created__range=week_range).count()
        context['users_month'] = GithubUserData.objects.filter(
            created__month=today.month).count()
        context['api_calls_today'] = ApiRequestsLog.objects.filter(
            request_time__day=today.day, request_time__month=today.month, request_time__year=today.year).count()
        context['api_calls_week'] = ApiRequestsLog.objects.filter(
            request_time__range=week_range).count()
        context['api_calls_month'] = ApiRequestsLog.objects.filter(
            request_time__month=today.month).count()

        return context
