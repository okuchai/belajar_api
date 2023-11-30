from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    alamat = models.TextField()
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True) 


#  install django
# 1. Buat folder di c 
# 2. arahkan folder visual studiocode ke folder yg sudah dibuat
# 3. buka terminal -> install django : pip install django   
#    buat project : django-admin startproject myblog
# 4. buat application : python manage.py startapp myapp
# 5. coba jalankan server : python manage.py runserver