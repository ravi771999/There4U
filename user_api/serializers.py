from datetime import datetime

from rest_framework import fields, serializers, viewsets

from user_api import models as user_models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=user_models.User
        fields=['id','email','name','city','state','zipcode','balance','phone']
    
    def create(self,validate_data):
        return user_models.User.objects.create(**validate_data)

    def validate_zipcode(self,value):
        """
            we are validating zip code by first checking if it has 6 digit or not.
            then i am first converting it in string, then checking if all characters of zip code string
            is digit or not.
        """
        if len(str(value)) != 6:
            return serializers.ValidationError("Invalid ZipCode")
        
        valid_digits=[str(z) for z in range(0,10)]
        for d in str(value):
            if d not in valid_digits:
                return serializers.ValidationError("Invalid Phone Number")

        return value

    def validate_phone(self,value):
        """
            we are validating phone number by first checking if it has 10 digit or not.
            then i am first converting it in string, then checking if all characters of phone number string
            is digit or not.
        """
        if(len(str(value)) != 10):
            return serializers.ValidationError("Invalid Phone Number")
        
        valid_digits=[str(z) for z in range(0,10)]
        for d in str(value):
            if d not in valid_digits:
                return serializers.ValidationError("Invalid Phone Number")

        return value

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