from django.db import models

class AccUsers(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pass_field = models.CharField(max_length=100, db_column='pass')
    role = models.CharField(max_length=30, blank=True, null=True)
    accountcode = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'acc_users'
        managed = True  # ✅ Let Django create this table via migration





from django.db import models

class Misel(models.Model):
    firm_name = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    phones = models.CharField(max_length=60, blank=True, null=True)
    mobile = models.CharField(max_length=60, blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    address3 = models.CharField(max_length=50, blank=True, null=True)
    pagers = models.CharField(max_length=60, blank=True, null=True)
    tinno = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'misel'
        managed = True  # ✅ Let Django create this table via migration