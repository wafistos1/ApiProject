
from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from .models import CustomUser

from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField(
        required=False,
        max_length=200,
    )
    picture = serializers.ImageField(
            required=False,
        )
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['phone'] = self.validated_data.get('phone', '')
        data_dict['picture'] = self.validated_data.get('picture', '')
        return data_dict
    
    def custom_signup(self, request, user):
        # connect the data with the user
        profile = CustomUser(
            user=user,
            phone=self.validated_data['phone'],
            picture=self.validated_data['picture'],
        )
        profile.save()
        return profile