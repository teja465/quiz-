from django.forms import ModelForm
from .models import questions

class questionForm(ModelForm):
    class Meta:
        model=questions
        fields='__all__'

