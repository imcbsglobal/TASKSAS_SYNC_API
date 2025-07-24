from rest_framework import serializers
from .models import AccUsers

class AccUsersSerializer(serializers.ModelSerializer):
    # Map the 'pass' field to 'pass_field' in the model
    pass_field = serializers.CharField(source='pass_field', max_length=100)
    
    class Meta:
        model = AccUsers
        fields = ['id', 'pass_field', 'role', 'accountcode']
        
    def to_representation(self, instance):
        # Convert 'pass_field' back to 'pass' in API response
        data = super().to_representation(instance)
        data['pass'] = data.pop('pass_field')
        return data
        
    def to_internal_value(self, data):
        # Convert 'pass' to 'pass_field' for internal use
        if 'pass' in data:
            data['pass_field'] = data.pop('pass')
        return super().to_internal_value(data)
    





from rest_framework import serializers
from .models import Misel

class MiselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misel
        fields = ['firm_name', 'address', 'phones', 'mobile', 'address1', 'address2', 'address3', 'pagers', 'tinno']