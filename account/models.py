from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password =None,):
        if not email:
            return ValueError("Users must have an email address")
        if not username:
            return ValueError("Users must have an username")

        user = self.model(
                email = self.normalize_email(email),
                username = username,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
                email = self.normalize_email(email),
                username = username,
                password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username= models.CharField(max_length=30, unique=True)
    fullname= models.CharField(max_length=60, blank=False )
    phone_number= models.IntegerField(blank=False, default=True)
    address = models.CharField(max_length=60, blank=False)
    date_joined= models.DateTimeField(verbose_name='date joined', auto_now_add= True)
    last_login= models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)


    USERNAME_FIELD = 'email' #use this to login
    REQUIRED_FIELDS = ['username',] #must have during sign up

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete = models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to = "profile/", default = 'dog.jpg')

    def __str__(self):
        return self.user.username
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)