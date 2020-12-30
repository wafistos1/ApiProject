
from rest_framework import serializers
from rest_framework import exceptions
from django.forms.fields import RegexField
from django.core.validators import RegexValidator
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from .models import DeliveryMan, ClientUser, Address, SalaryCustomUser, EmployeeUser
from django.conf import settings
from django.contrib.auth import authenticate
from rest_auth.registration.serializers import RegisterSerializer
from django.utils.translation import gettext_lazy as _
from accounts.models import Region, City
import re




expression = r"^09([ .-]?[0-9]{2}){4}$"
expression2 = r"^09([ .-]?[0-9]{2}){2}([ .-]?[0-9]{3})$"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields ='__all__'  
        

class CustomRegisterSerializer(RegisterSerializer):
    # phone = RegexField(expression, max_length=None, min_length=None, allow_blank=False)
    phone = serializers.CharField(required=False,max_length=200,)
    facebook_name = serializers.CharField(required=False,max_length=200,)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    facebook_id = serializers.IntegerField(required=False)
    
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['phone'] = self.validated_data.get('phone', '')
        data_dict['facebook_name'] = self.validated_data.get('facebook_name', '')
        data_dict['facebook_id'] = self.validated_data.get('facebook_id', '')
        data_dict['first_name'] =  self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        return data_dict
    
    def validate_phone(self, phone):
        phone = get_adapter().clean_email(phone)
        if re.search(expression, phone) is None:
                raise serializers.ValidationError(
                    _("The phone number is not valid."))
        return phone
    
    def custom_signup(self, request, user):
        # connect the data with the user
        region = Region.objects.filter(id=self.validated_data['region']).first()
        location = self.validated_data['location']
        address = Address(
        #    city=self.validated_data['city'],
           region=region,
           location=location,
           )
        address.save() 
        profile = ClientUser(
            user=user,
            phone=self.validated_data['phone'],
            facebook_name=self.validated_data['facebook_name'],
            facebook_id=self.validated_data['facebook_id'],
            address=address,
        )
        profile.save()
        return profile


    
    
class EmplyeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields ='__all__'  

      
class DeliveryManSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields ='__all__'  
  
      
class SalaryCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryCustomUser
        fields ='__all__'  

   


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True, allow_blank=False)
#     password = serializers.CharField(style={'input_type': 'password'})

#     def authenticate(self, **kwargs):
#         return authenticate(self.context['request'], **kwargs)

#     def _validate_email(self, email, password):
#         user = None
#         if email and password:
#             user = self.authenticate(email=email, password=password)
#         else:
#             msg = _('Must include "email" and "password".')
#             raise exceptions.ValidationError(msg)

#         return user

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         user = None
#         if 'allauth' in settings.INSTALLED_APPS:
#             from allauth.account import app_settings
#             # Authentication through email
#             if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:
#                 user = self._validate_email(email, password)

#         # Did we get back an inactive user?
#         if user:
#             if not user.is_active:
#                 msg = _('User account is disabled.')
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg = ('Unable to log in with provided credentials.')
#             raise exceptions.ValidationError(msg)

#         # If required, is the email verified?
#         if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
#             from allauth.account import app_settings
#             if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
#                 try:
#                     email_address = user.emailaddress_set.get(email=user.email)
#                 except:
#                     raise serializers.ValidationError(_('E-mail is not registered.'))
#                 else:
#                     if not email_address.verified:
#                         raise serializers.ValidationError(_('E-mail is not verified.'))


#         attrs['user'] = user
#         return attrs