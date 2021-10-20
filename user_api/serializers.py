from datetime import datetime

from rest_framework import fields, serializers, viewsets

from user_api.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        exclude=['password','active','staff','admin','last_login']
    
    def create(self,validate_data):
        return User.objects.create(**validate_data)

    def validate_zipcode(self,value):
        if len(str(value)) == 6:
            return value
        return serializers.ValidationError("Invalid ZipCode")

    def validate_phone(self,value):
        if(len(str(value))==10):
            return value
        return serializers.ValidationError("Invalid Phone Number")

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.updated_at=datetime.now()
        instance.save()
        return instance


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)