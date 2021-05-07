from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from account.models import Account

# Create your models here.
class Vendor(models.Model):
    fullname           = models.CharField(max_length=100, null=True)
    phone              =  models.CharField(max_length=100, null=True)
    email              = models.EmailField(verbose_name='email', max_length=50, null=True)

    def __str__(self):
        return self.fullname

class CouponCode(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=20)
    valid = models.BooleanField()
    active = models.BooleanField()

    def __str__(self):
        return self.code

class Post(models.Model):
    title = models.CharField(max_length=200, blank=True,null=True)
    content = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    sharer = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,blank=True)
    shared = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postDetail', kwargs={'slug': self.slug})

