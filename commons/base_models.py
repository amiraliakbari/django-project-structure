# -*- coding: utf-8 -*-
import uuid
from django.db import models


class Node(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)

    def get_depth(self):
        depth = 0
        p = self
        while p and p.parent:
            p = p.parent
            depth += 1
        return depth

    class Meta:
        abstract = True


class Named(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Slugged(models.Model):
    slug = models.CharField(max_length=32, db_index=True, blank=True)

    def save(self, *args, **kwrags):
        if self.pk is None:
            self.slug = unicode(uuid.uuid4()).replace('-', '')
        super(Slugged, self).save(*args, **kwrags)

    class Meta:
        abstract = True


class Ordered(models.Model):
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True
