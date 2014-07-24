# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.db import models

#class Coop(models.Model):
#    reporting_country = models.CharField(max_length=3)
#    consulting_country = models.CharField(max_length=3)
#    class Meta:
#        managed = False
#        db_table = 'COOP'

class Passport(models.Model):
    id_passport = models.CharField(primary_key=True, unique=True, max_length=8)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=45, blank=True)
    nationality = models.CharField(max_length=3)
    sex = models.CharField(max_length=1)
    issue_date = models.DateField()
    issue_place = models.CharField(max_length=45)
    personal_document = models.CharField(max_length=45, blank=True)
    expiry_date = models.DateField()
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.nationality + '<' + self.id_passport
    class Meta:
        db_table = 'PASSPORT'

class Report(models.Model):
    id_report = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=1)
    last_place_seen = models.CharField(max_length=45)
    crime_description = models.CharField(max_length=45)
    crime_date = models.DateField()
    reporting_date = models.DateField()
    reporting_country = models.CharField(max_length=3, blank=True)
    reincidence = models.ForeignKey('self', db_column='reincidence', blank=True, null=True)
    id_passport = models.ForeignKey(Passport, db_column='id_passport')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.id_report
    class Meta:
        db_table = 'REPORT'

class Coop(models.Model):
    id_agreement = models.AutoField(primary_key=True)
    country_a = models.CharField(max_length=3)
    country_b = models.CharField(max_length=3)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.country_a + '&' + self.country_b
    class Meta:
        db_table = 'COOP'


