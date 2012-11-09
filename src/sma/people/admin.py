# -*- coding: utf-8 -*-
from django.contrib import admin
from sma.people.models import Entry, Member, Domain

admin.site.register(Domain)
admin.site.register(Entry)
admin.site.register(Member)
