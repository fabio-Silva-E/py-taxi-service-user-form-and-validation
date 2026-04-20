from django import forms
from .models import Driver, Car
import re


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if not re.fullmatch(r"[A-Z]{3}\d{5}", license_number):
            raise forms.ValidationError(
                "License must be 3 uppercase letters followed"
                " by 5 digits (e.g. ABC12345)"
            )

        return license_number


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "drivers": forms.CheckboxSelectMultiple(),
        }
