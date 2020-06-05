from django.db import models
from django.contrib.postgres.fields import JSONField


class POI(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=800)
    precision = models.IntegerField(default=10)

    poi = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    space = models.CharField(max_length=200, default="")
    did = models.CharField(max_length=200, default="")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "precision": self.precision,
            "poi": self.poi,
            "space": self.space,
            "did": self.did
        }


class Availability(models.Model):
    STATUS = (
        ('active', 'active'),
        ('challenged', 'challenged'),
    )
    poi = models.ForeigKey(POI)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    space = models.CharField(max_length=200, default="")
    did = models.CharField(max_length=200, default="")
    status = models.CharField(max_length=200, choices=STATUS, default='active')
    schedule = JSONField(default=dict())
    challenge = models.ForeigKey('availability.Availability', null=True, blank=True)

    @property
    def status(self):
        return 'open'

    def to_dict(self):
        return {
            "id": self.id,
            "poi": self.poi.to_dict(),
            "space": self.space,
            "did": self.did,
            "info": self.info,
            "schedule": self.status,
            "challenge": self.challenge.id
        }


class Features(models.Model):
    STATUS = (
        ('active', 'active'),
        ('challenged', 'challenged'),
    )

    poi = models.ForeigKey(POI)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    space = models.CharField(max_length=200, default="")
    did = models.CharField(max_length=200, default="")
    info = JSONField(default=dict())
    status = models.CharField(max_length=200, choices=STATUS, default='active')
    challenge = models.ForeigKey('availability.Features', null=True, blank=True)

    def to_dict(self):
        return {
            "id": self.id,
            "poi": self.poi.to_dict(),
            "space": self.space,
            "did": self.did,
            "info": self.info,
            "status": self.status,
            "challenge": self.challenge.id
        }