from django.db import models
from django.contrib.auth.models import User
from django.db.models import BigAutoField,AutoField
from django.core.validators import MaxValueValidator,MinValueValidator

STATE_CHOICES=[
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Chattisgarh','Chattisgarh'),
    ('Chandigarh','Chandigarh'),
    ('Bihar','Bihar'),
    ('Daman and Diu','Daman and Diu'),
]

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=200)

    def __str__(self):
        return str(self.name)

CATEGORY_CHOICES = [
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
    ('G', 'Grocery'),
    ('B', 'Beauty product'),
    ('E', 'Electronics'),
    ('H', 'Home_decorate'),
    ('D', 'Offer'),
    ('F', 'Furniture'),
    ('A', 'Applinces'),
]

class Product(models.Model):
    title= models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    discription= models.TextField()
    brand = models.CharField(max_length=100)
    category= models.CharField( choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='productimg')
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
STATUS_CHOICES=[
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
]
    
class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    ordered_data=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.id)
    
#------------------------------------------------------------------
class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.product)