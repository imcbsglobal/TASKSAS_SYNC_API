from rest_framework import serializers
from .models import AccUsers
from .models import Misel

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