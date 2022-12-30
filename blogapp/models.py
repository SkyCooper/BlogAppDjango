from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name
  class Meta:
    ordering = ("-name",)
    verbose_name = "Kategori"
  
class Post(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  content = models.TextField(max_length=50, blank=True)
  status = models.BooleanField(default=False)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title
  
  class Meta:
    # ordering = ("id",)
    verbose_name = "Gönderi"
