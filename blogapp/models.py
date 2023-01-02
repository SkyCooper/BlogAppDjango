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
  PRIORITY = (
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low')
  )
  
  priority = models.SmallIntegerField(choices=PRIORITY, default=3)
  
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

class Author(models.Model):
  name = models.CharField(max_length=50)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name  
  
