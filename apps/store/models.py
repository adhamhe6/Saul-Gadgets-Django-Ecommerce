from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    ordering = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)