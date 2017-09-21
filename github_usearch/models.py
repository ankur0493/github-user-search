# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

class GithubUserData(models.Model):
    user_types = (
        ("User", "User"),
        ("Organization", "Organization"),
    )
    username = models.CharField( _("Github username"), max_length=39,
                                 unique=True )
    user_profile_name = models.CharField( _("Name of the user"), max_length=255, blank=True )
    github_id = models.IntegerField( _("Github ID for the user"), unique=True )
    company = models.CharField( _("Github Username for user's organization"),
                                max_length=39, blank=True, )
    # We currently just store the URL of the user's avatar, but  may we
    # eventually start downloading the gravatar itself and store it in our
    # local storage
    avatar_url = models.URLField( _("URL of the user's avatar"), blank=True, )
    user_type = models.CharField( _("Type of the user (User/Organization)"),
                                  max_length=12, choices=user_types,
                                  default=user_types[0][0] )
    is_site_admin = models.BooleanField( _("Is the  user a site admin?"),
                                         default=False )
    score = models.DecimalField( _("Github score for the user"), max_digits=9,
                                 decimal_places=6, blank=True )
    blog = models.URLField( _("Link to user's blog"), blank=True )
    location = models.CharField( _("User's Location"), max_length=255 )
    email = models.EmailField( _("User's public email"), blank=True )
    available_for_hire = models.BooleanField( _("Is the user available for hire?"),
                                              default=False )
    bio = models.TextField( _("Users Github Bio") )
    github_user_created = models.DateTimeField( _("User created datetime for Github") )
    github_user_updated = models.DateTimeField( _("User updated datetime for Github") )
    created = models.DateTimeField( _("User created timestamp"), auto_now_add=True )
    updated= models.DateTimeField( _("User updated timestamp"), auto_now=True )

    class Meta:
        verbose_name = _("GithubUserData")
        verbose_name_plural = _("GithubUsersData")


class ApiRequestsLog(models.Model):
    queryparams = models.TextField( _("Query Params in the API request") )
    request_time = models.DateTimeField( _("Datetime when request was made"), auto_now_add=True )

    class Meta:
        verbose_name = _("ApiRequestLog")
        verbose_name = _("ApiRequestLogs")
