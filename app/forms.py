from django import forms

from app.models import Plan_info


class Plan_infoForm(forms.ModelForm):
    class Meta:
        model = Plan_info
        fields = '__all__'