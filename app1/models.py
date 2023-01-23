from datetime import datetime
from django.db import models

# Create your models here.
from unicodedata import name

# Create your models here.
class Que(models.Model):
    firstName=models.CharField(max_length=100, blank=True)
    lastName=models.CharField(max_length=100, blank=True)
    emailId=models.CharField(max_length=254, blank=True)
    password=models.CharField(max_length=50, blank=True)
    confirmPassword=models.CharField(max_length=50, blank=True)
   
    def __str__(self):
        return self.firstName

# class Products(models.Model):
#     name = models.CharField(max_length=60)
#     price= models.IntegerField(default=0)
#     category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
#     description= models.CharField(max_length=250, default='', blank=True, null= True)
#     image= models.ImageField(upload_to='uploads/products/')

#     @staticmethod
#     def get_products_by_id(ids):
#         return Products.objects.filter (id__in=ids)
#     @staticmethod
#     def get_all_products():
#         return Products.objects.all()

#     @staticmethod
#     def get_all_products_by_categoryid(category_id):
#         if category_id:
#             return Products.objects.filter (category=category_id)
#         else:
#             return Products.get_all_products();


# class Category(models.Model):
#     name= models.CharField(max_length=50)

#     @staticmethod
#     def get_all_categories():
#         return Category.objects.all()

#     def __str__(self):
#         return self.name


class Courses(models.Model):
    Course_name = models.CharField(max_length=100, blank=False)
    Start_date = models.DateField()
    End_date = models.DateField()
    Course_status = models.BooleanField(default=False)
    Course_createdAt= models.DateField(default=datetime.now())
    # course_image = models.ImageField()

    def __str__(self):
        return self.Course_name
