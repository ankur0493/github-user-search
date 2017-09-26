from __future__ import unicode_literals

import dateutil.parser
from decimal import Decimal

from django.db import models

from rest_framework import serializers, fields

from .models import GithubUserData
from .constants import GITHUB_USER_LIST_ATTRIBUTE_MAP


class GitHubUserSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        d = {}
        for k in data:
            if k in GITHUB_USER_LIST_ATTRIBUTE_MAP:
                key = GITHUB_USER_LIST_ATTRIBUTE_MAP[k]
            else:
                key = k
            if key in self.fields:
                field = self.Meta.model._meta.get_field(key)
                if isinstance(field, models.DateTimeField):
                    d[key] = dateutil.parser.parse(data[k])
                else:
                    d[key] = data[k]
        for field_name in self.fields:
            if field_name not in d or not d[field_name]:
                field = self.Meta.model._meta.get_field(field_name)
                default = field.default
                if isinstance(field, (models.AutoField, models.DateTimeField)):
                    pass
                elif default != models.fields.NOT_PROVIDED:
                    d[field_name] = default
                elif isinstance(field, (models.CharField, models.TextField)):
                    d[field_name] = ''
                elif isinstance(field, models.DecimalField):
                    d[field_name] = Decimal(0)
                else:
                    d[field_name] = None
        return d

    class Meta:
        model = GithubUserData
        fields = '__all__'
