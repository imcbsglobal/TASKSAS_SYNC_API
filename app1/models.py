from django.db import models

class AccUsers(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pass_field = models.CharField(max_length=100, db_column='pass')
    role = models.CharField(max_length=30, blank=True, null=True)
    accountcode = models.CharField(max_length=30, blank=True, null=True)
    client_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'acc_users'
        managed = True
        unique_together = ('id', 'client_id')


class AccMaster(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=200, blank=True, null=True)
    super_code = models.CharField(max_length=5, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    debit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    credit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=60, blank=True, null=True)
    openingdepartment = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)
    client_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'acc_master'
        managed = True
        unique_together = ('code', 'client_id')
