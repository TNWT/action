from django.db import models

import uuid

from account.models import User

class Items(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fleet = models.CharField(max_length=255)
    tail = models.CharField(max_length=255)
    remark = models.TextField(blank=True, null=True)
    required_action = models.TextField(blank=True, null=True)
    owner = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    logged = models.CharField(max_length=255)
    duedate = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    level1 = models.CharField(max_length=255)
    level2 = models.CharField(max_length=255)
    level3 = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    requestedby = models.CharField(max_length=255)
    

    def __str__(self):
        self.name