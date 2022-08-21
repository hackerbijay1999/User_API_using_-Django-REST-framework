from django.db import models

# Create your models here.

class Department(models.Model):
    dept_id = models.BigAutoField(primary_key=True)
    dept_name = models.CharField(max_length=50, blank=True, null=True)
    org_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'
  
class Organisation(models.Model):
    org_id = models.BigAutoField(primary_key=True)
    org_name = models.CharField(max_length=50, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organisation'   

class Modules(models.Model):
    mod_id = models.BigAutoField(primary_key=True)
    mod_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modules'

class User(models.Model):
    user_id = models.BigAutoField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50, blank=True, null=True)
    org_name = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50)
    modules = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    phone = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user'

