from rest_framework import serializers
from .models import AccUsers, AccMaster

class AccUsersSerializer(serializers.ModelSerializer):
    pass_field = serializers.CharField(source='pass_field', max_length=100)

    class Meta:
        model = AccUsers
        fields = ['id', 'pass_field', 'role', 'accountcode', 'client_id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['pass'] = data.pop('pass_field')
        return data

    def to_internal_value(self, data):
        if 'pass' in data:
            data['pass_field'] = data.pop('pass')
        return super().to_internal_value(data)


class AccMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccMaster
        fields = ['code', 'name', 'super_code', 'opening_balance', 'debit', 'credit',
                  'place', 'phone2', 'openingdepartment', 'area', 'client_id']
