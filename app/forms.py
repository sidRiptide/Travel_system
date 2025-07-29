from django.forms import forms

from app.models import Plan_info


class Plan_infoForm(forms.Form):
    class Meta:
        model = Plan_info
        fields = '__all__'