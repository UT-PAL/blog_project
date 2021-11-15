from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author',null=True)
    blog_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="What is on your mind?")
    blog_reference = models.URLField(max_length=200,null=True)
    blog_image = models.ImageField(upload_to='blog_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-publish_date', ]

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment',null=True)
    comment = models.TextField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return self.comment


class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="liked_blog",null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker_user",null=True)

    def __str__(self):
        return self.user,"likes",self.blog

class Dislikes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="disliked_blog", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="disliker_user", null=True)

    def __str__(self):
        return self.user , "dislikes" ,self.blog

class shared_post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='shared_blog',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_sharer",null=True)
    shared_date = models.DateTimeField(auto_now_add=True)
    whats_on_mind = models.TextField(verbose_name="Write something about the blog ")
    class Meta:
        ordering = ('-shared_date',)

    def __str__(self):
        return self.whats_on_mind
