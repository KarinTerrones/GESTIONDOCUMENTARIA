from .models import settings
from .models import *
from django.contrib.auth.models import Group
from django.db.models.signals import post_save


def Account_Create(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='en_espera')
        instance.groups.add(group)
post_save.connect(Account_Create,sender=settings.AUTH_USER_MODEL)
    