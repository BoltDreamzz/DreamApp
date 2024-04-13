from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='cat_images', blank=True, null=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    sizes = models.ManyToManyField(Size, blank=True)
    available_colors = models.ManyToManyField(Color, blank=True)
    image = models.ImageField(upload_to='product_images')
    date_posted = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(default=0, max_digits=10, decimal_places=1, blank=True)
    is_sold = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.name



