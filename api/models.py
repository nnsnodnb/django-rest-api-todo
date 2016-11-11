# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ApiTask(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100)  # Field name made lowercase.
    schedule_date = models.CharField(db_column='SCHEDULE_DATE', max_length=10)  # Field name made lowercase.
    finish_date = models.CharField(db_column='FINISH_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rank = models.CharField(db_column='RANK', max_length=1)  # Field name made lowercase.
    finish_check = models.IntegerField(db_column='FINISH_CHECK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'api_task'


class Task(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100)  # Field name made lowercase.
    schedule_date = models.CharField(db_column='SCHEDULE_DATE', max_length=10)  # Field name made lowercase.
    finish_date = models.CharField(db_column='FINISH_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rank = models.CharField(db_column='RANK', max_length=1)  # Field name made lowercase.
    finish_check = models.IntegerField(db_column='FINISH_CHECK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task'
