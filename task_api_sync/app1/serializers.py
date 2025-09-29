from rest_framework import serializers
from .models import AccUsers
from .models import Misel
from .models import AccLedgers,AccMaster,AccUsers,AccInvmast,CashAndBankAccMaster,AccTtServicemaster

# AccUsersSerializer
class AccUsersSerializer(serializers.ModelSerializer):
    pass_field = serializers.CharField(source='pass_field', max_length=100)

    class Meta:
        model = AccUsers
        fields = ['id', 'pass_field', 'role', 'accountcode', 'client_id']  # added client_id

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['pass'] = data.pop('pass_field')
        return data

    def to_internal_value(self, data):
        if 'pass' in data:
            data['pass_field'] = data.pop('pass')
        return super().to_internal_value(data)

# MiselSerializer
class MiselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misel
        fields = ['firm_name', 'address', 'phones', 'mobile',
                  'address1', 'address2', 'address3', 'pagers',
                  'tinno', 'client_id']  # added client_id
        





# AccMasterSerializer
class AccMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccMaster
        fields = ['code', 'name', 'opening_balance', 'debit', 'credit',
                  'place', 'phone2', 'openingdepartment', 'area', 'client_id']



# AccLedgersSerializer
class AccLedgersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccLedgers
        fields = ['code', 'particulars', 'debit', 'credit', 'entry_mode',
                  'entry_date', 'voucher_no', 'narration', 'client_id']


# AccInvmastSerializer
class AccInvmastSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccInvmast
        fields = ['modeofpayment', 'customerid', 'invdate', 'nettotal',
                  'paid', 'bill_ref', 'client_id']
        



class CashAndBankAccMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashAndBankAccMaster
        fields = ['code', 'name', 'super_code', 'opening_balance', 'opening_date', 'debit', 'credit', 'client_id']



class AccTtServicemasterSerializer(serializers.ModelSerializer):
    class Meta:
        model  = AccTtServicemaster
        fields = ['slno', 'type', 'code', 'name', 'client_id']