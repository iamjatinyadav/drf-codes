from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Student

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"



class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(style={'input_type': 'password'},write_only=True, required=True )
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "password field didn't match"})
        return attrs

    def create(self, vaildate_data):
        user = User.objects.create_user(vaildate_data['username'], vaildate_data['email'], vaildate_data['password'])
        
        return user

        

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

