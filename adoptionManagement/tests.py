from django.test import TestCase
from adoptionManagement.views import *
from adoptionManagement.models import *
from django.contrib.auth.models import User
from django.urls import reverse
from account.models import Account


class DisplayDogTest(TestCase):
    
    def setUp(self):
        Dog.objects.create(breed_name = 'test', dog_age = '1 month', description = 'test', gender ='test', dog_image= 'test\test', status = True)
        

    def test_display(self):
        dog = Dog.objects.get(breed_name = 'test')
        self.assertEqual(dog.breed_name, 'test')

   