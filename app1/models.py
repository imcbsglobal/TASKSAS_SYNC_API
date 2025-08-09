from django.db import models

class AccUsers(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pass_field = models.CharField(max_length=100, db_column='pass')
    role = models.CharField(max_length=30, blank=True, null=True)
    accountcode = models.CharField(max_length=30, blank=True, null=True)
    client_id = models.CharField(max_length=100)  # <-- ADD THIS

    class Meta:
        db_table = 'acc_users'
        managed = True
        unique_together = ('id', 'client_id')


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
    client_id = models.CharField(max_length=100)  # <-- ADD THIS

    class Meta:
        db_table = 'misel'
        managed = True



class AccMaster(models.Model):
    id = models.AutoField(primary_key=True)  # Add auto-incrementing primary key
    code = models.CharField(max_length=30)   # Remove primary_key=True from code
    name = models.CharField(max_length=200, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    debit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    credit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=60, blank=True, null=True)
    openingdepartment = models.CharField(max_length=100, blank=True, null=True)
    client_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'acc_master'
        managed = True
        unique_together = ('code', 'client_id')  # This ensures code is unique per client


class AccLedgers(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    particulars = models.CharField(max_length=500, blank=True, null=True)
    debit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    credit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    entry_mode = models.CharField(max_length=20, blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    voucher_no = models.IntegerField(blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    client_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'acc_ledgers'
        managed = True


class AccInvmast(models.Model):
    id = models.AutoField(primary_key=True)
    modeofpayment = models.CharField(max_length=10, blank=True, null=True)
    customerid = models.CharField(max_length=30, blank=True, null=True)
    invdate = models.DateField(blank=True, null=True)
    nettotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    paid = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bill_ref = models.CharField(max_length=100, blank=True, null=True)
    client_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'acc_invmast'
        managed = True




class CashAndBankAccMaster(models.Model):
    id = models.AutoField(primary_key=True)  # Add explicit primary key
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=250)
    super_code = models.CharField(max_length=5, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    opening_date = models.DateField(blank=True, null=True)
    debit = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    client_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'cashandbankaccmaster'
        managed = True
        unique_together = ('code', 'client_id')  # Keep unique constraint on business logic
