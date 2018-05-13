# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class IssuetrackerConfig(AppConfig):
    name = 'issuetracker'

    def ready(self):
        import issuetracker.signals 
