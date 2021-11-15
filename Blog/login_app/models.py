from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#built-in user model
class User_profile(models.Model):
    user=models.OneToOneField(User,primary_key=True, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics')
    dob = models.DateField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)

class Follow (models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Follower')
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Following')
    following_date= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.follower , 'Follows ', self.following
