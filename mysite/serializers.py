from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        user_info = dict()
        # user_id is already in token['user_id']
        user_info['username'] = user.get_username()
        user_info['email'] = user.email
        user_info['full_name'] = user.get_full_name()
        user_info['is_staff'] = user.is_staff
        token['user_info'] = user_info
        return token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'full_name', 'is_staff')
