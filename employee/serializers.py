from rest_framework import serializers, status
from .models import Employee
# from django.contrib.auth import get_user_model
# User = get_user_model()
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class EmployeeSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Employee
        fields = ('user', 'subject',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        Employee, created = Employee.objects.update_or_create(user=user,
                            subject=validated_data.pop('subject'))
        return student



# Change Password

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)