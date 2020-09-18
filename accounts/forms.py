from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm


class EmployeeFrom(SignupForm):
    picture = forms.FileField()
    phone = forms.CharField(max_length=50)

    def save(self, request):
        user = super(EmployeeFrom, self).save(request)
        # Create an instance of your model with the extra fields
        # then save it.
        # (N.B: the are already cleaned, but if you want to do some
        # extra cleaning just override the clean method as usual)
        profile_user = EmployeeFrom(
            profile_user=user,
            picture=self.cleaned_data.get('picture'),
            phone=self.cleaned_data.get('phone'),
            )
        profile_user.save()

        # Remember to return the User instance (not your custom user,
        # the Django one), otherwise you will get an error when the
        # complete_signup method will try to look at it.
        return profile_user