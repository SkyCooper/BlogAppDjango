from django.db import models

# Create your models here.

class Category(models.Model):
  # id = yazmaya gerek yok, django zaten default id üretiyor.
  name = models.CharField(max_length=50, unique=True) 
  #? her kategoriden sadece 1 tane create edilsin diye unique=True verildi.
  
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
  
  STATUS = (
    ('p', 'Published'),
    ('d', 'Draft')
  )
  
  priority = models.SmallIntegerField(choices=PRIORITY, default=3)
  
  title = models.CharField(max_length=100)
  content = models.TextField(blank=True) # max_length vermeye gerek yok, istediği kadar yazsın, veya boş geçebilsin
  category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
  #? PROTECT , yani bu Category içinde Post varsa onu koru, silinmesine izin verme
  # status = models.CharField(max_length=100, choices=STATUS, default='d')
  is_published = models.BooleanField(default=False)
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
  
