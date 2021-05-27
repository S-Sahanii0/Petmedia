from django.forms import ModelForm
from .models import Dog, AdoptionQueue, Requests

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'

class RegForm(ModelForm):
    class Meta:
        model = AdoptionQueue
        fields = ('dog_name', 'age', 'reason', 'gender', 'further_info', 'image')

class RequestForm(ModelForm):
    class Meta:
        model = Requests
        fields  = '__all__'