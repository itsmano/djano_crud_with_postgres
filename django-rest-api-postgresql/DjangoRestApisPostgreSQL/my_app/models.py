from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)

    class Meta:
        db_table = "tutorial"


class User(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=200, blank=False, default='')
    active = models.BooleanField(default=False)

    class Meta:
        db_table = "user"


class Group(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=200, blank=False, default='')
    active = models.BooleanField(default=False)

    class Meta:
        db_table = "group"


class Role(models.Model):
    rolename = models.CharField(max_length=70, blank=False, default='')
    active = models.BooleanField(default=False)

    class Meta:
        db_table = "role"
