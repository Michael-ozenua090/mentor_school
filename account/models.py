from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from requests import request
# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE = ((1, "Lecturer"), (2, "Student"),)
    GENDER = [("M", "Male"), ("F", "Female"), ("OTHERS", "Others")]
    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True)
    last_name = models.CharField(null=False, max_length=80)
    first_name = models.CharField(null=False, max_length=80)
    gender = models.CharField(max_length=7, choices=GENDER)
    user_type = models.PositiveSmallIntegerField(default=2, choices=USER_TYPE,)
    number = models.CharField(max_length=11)
    image = models.ImageField(upload_to='images/account')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.last_name + " " + self.first_name

    class Meta:
        ordering = ['-id']


class Score(models.Model):

    courses = (('CSE 219', 'CSE 219'), ('GNS 219', 'GNS 219'), ('CSE 223', 'CSE 223'), ('CSE 203', 'CSE 203'))
    courses_offered = models.CharField(choices=courses, max_length=7)
    ca = models.IntegerField()
    test = models.IntegerField()
    exam = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.courses_offered

    class Meta:
        ordering = ['-id']

