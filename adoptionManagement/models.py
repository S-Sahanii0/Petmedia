from django.db import models
from account.models import Account

# Create your models here.
class Dog(models.Model):
    # STATUS = (
    #     ('Available', 'Available'),
    #     ('Booked', 'Booked'),
    # )
    breed_name = models.CharField(max_length=60, blank=False)
    dog_age = models.CharField(max_length= 60, blank=False)
    description = models.CharField(max_length=150)
    gender = models.CharField(max_length=60, null=True, blank=False)
    dog_image = models.ImageField(upload_to="uploads/", null=True, blank = False)
    

    def __str__(self):
        return self.breed_name

class Requests(models.Model):
    # STATUS = (
    #     ('Pending', 'Pending'),
    #     ('Accepted', 'Accepted'),
    # )
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)  
    dog = models.OneToOneField(Dog, on_delete= models.CASCADE)
    is_requested = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

class AdoptionQueue(models.Model):
    # STATUS = (
    #     ('Pending', 'Pending'),
    #     ('Accepted', 'Accepted'),
    # )
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    dog_name = models.CharField(max_length=60, blank=False, null=True, verbose_name='Breed')
    age = models.CharField(max_length=25, blank=False, null=True)
    gender = models.CharField(max_length=60, null=True, blank=False)
    reason = models.CharField(verbose_name='Reason for registering', max_length=150, blank=False, null=True)
    image =  models.ImageField(upload_to="uploads/", null=True, verbose_name='Picture of the dog')
    further_info = models.CharField(verbose_name='Further information (optional)',max_length=150, blank=True, null=True)

    def __str__(self):
       return self.dog_name



