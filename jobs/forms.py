from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    summary = forms.CharField(error_messages={'required': 'This field is required! Please fill Job summary field.'})
    description = forms.Textarea()
    language = forms.CharField()
    company = forms.CharField()
    status = forms.CharField()
    urgency = forms.CharField()

    class Meta:
        model = Job
        fields = (
            'summary',
            'description',
            'language',
            'company',
            'status',
            'urgency',
        )
