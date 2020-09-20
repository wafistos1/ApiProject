from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm


class EmployeeFrom(SignupForm):
    picture = forms.FileField()
    phone = forms.CharField(max_length=50)

    def save(self, request):
        user = super(EmployeeFrom, self).save(request)
        profile_user = EmployeeFrom(
            profile_user=user,
            picture=self.cleaned_data.get('picture'),
            phone=self.cleaned_data.get('phone'),
            )
        profile_user.save()

    
class DeleveryFrom(SignupForm):
    picture = forms.FileField()
    phone = forms.CharField(max_length=50)

    def save(self, request):
        user = super(DeleveryFrom, self).save(request)
        profile_user = DeleveryFrom(
            profile_user=user,
            picture=self.cleaned_data.get('picture'),
            phone=self.cleaned_data.get('phone'),
            )
        profile_user.save()