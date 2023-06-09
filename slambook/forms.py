from django import forms
from slambook.models import Person

class PersonForm(forms.ModelForm):
  class Meta:
    model = Person
    fields = "__all__"