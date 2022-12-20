from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now


UserModel = get_user_model()

class CreationBaseModel(models.Model):
    created_at = models.DateTimeField(default=now, null=True, blank=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True
