from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(verbose_name='enter your description')

    def __str__(self):
        return self.first_name

    class Meta():

        verbose_name_plural = 'Contact'


class Category(models.Model):
    cat_name = models.CharField(max_length=30, verbose_name='Category Name')
    cat_desc = models.TextField(blank=True, null=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural = 'Category'


class Post(models.Model):
    pst_title = models.CharField(max_length=150, verbose_name='name of product')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='created by', null=True, blank=True)
    images = models.FileField(upload_to='uploads/', verbose_name='upload a photo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural = 'Post'
    
    

class Comment(models.Model):
    name = models.CharField(max_length=150)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.pst_title

    class Meta():
        verbose_name_plural = 'Comment'

class Advertisement(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    image = models.FileField(verbose_name='image or video', upload_to='media')
    description = models.TextField(verbose_name='enter your description')

    def __str__(self):
        return self.email

    class Meta():
        verbose_name_plural = 'Advertisement'

class Password(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta():
        verbose_name_plural = 'Password'



class Video(models.Model):
    pst_title = models.CharField(max_length=150, verbose_name='name of product')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='created by', null=True, blank=True)
    video = models.FileField(upload_to='videos/', verbose_name='upload a video')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural = 'Video'


class Hello(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Hello'
