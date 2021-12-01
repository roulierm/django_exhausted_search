from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank = True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null= True)

    def __str__(self):
        return self.name

class Userpost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Year = models.CharField(max_length = 4)
    Mileage = models.CharField(max_length = 8)
    Make = models.CharField(max_length = 50)
    Model = models.CharField(max_length = 50)
    Price = models.DecimalField(max_digits=15, decimal_places=2)
    email = models.EmailField()
    date_published = models.DateField(default = timezone.now)
    image = models.ImageField(null = True, blank = True, upload_to = r"C:\Users\gabri\Desktop\test\ecommerce\static\images")
    zipCode = models.CharField(max_length=5)
    

    def __str__(self):
        return self.Year + " " + self.Make + " " + self.Model
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Dealer(models.Model):
    dealersName = models.TextField(('DealersName'))
    zipcode = models.CharField(("zipcodex"), max_length = 15)
    zipcode_2 = models.CharField(("zipCode"), max_length = 15)	
    state = models.CharField(("state"), max_length=5)
    address = models.TextField(("Address"))
    ids = models.BigIntegerField(("ids"), primary_key=True)
    

    def __str__(self):
        return self.dealersName