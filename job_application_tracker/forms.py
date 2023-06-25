from django import forms
from .models import JobApplication

class JopApplicationForm (forms.ModelForm):
    class Meta:
        model = JobApplication 
        exclude = ["created_at",]
