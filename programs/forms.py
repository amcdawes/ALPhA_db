from django.forms import ModelForm
from .models import Instructor

class AddInstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['name','email']
