from django.db import models
from django.contrib.auth.models import User,AbstractUser
from PIL import Image

# Create your models here.

class User(AbstractUser):
	is_parent=models.BooleanField(default=False)
	is_staff=models.BooleanField(default=False)

class Parent(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	fullnames=models.CharField(max_length=100)
	telephone=models.IntegerField(null=True,blank=True)
	country=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	address=models.CharField(max_length=100)

class Staff(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	fullnames=models.CharField(max_length=100)
	telephone=models.CharField(max_length=200)
	city=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	nationid=models.IntegerField(null=True,blank=True)
	

# class Profile(models.Model):
# 	user=models.OneToOneField(User,on_delete=models.CASCADE)
# 	image=models.ImageField(default='default.jpg',upload_to='profile_pics')

# 	def __str__(self):
# 		return f'{self.user.username} Profile'

# 	def save(self, *args, **kwargs):
# 		super(Profile, self).save(*args, **kwargs)

# 		img=Image.open(self.image.path)

# 		if img.height>300 or img.width>300:
# 			output_size=(300,300)
# 			img.thumbnail(output_size)
# 			img.save(self.image.path)
