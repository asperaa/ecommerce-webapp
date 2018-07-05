from django.db import models
import os
import random

from django.db.models import Q
from django.db.models.signals import pre_save
from ecommerce.utils import unique_slug_generator
from django.urls import reverse

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.pathname(filepath)
    name, ext = os.path.splitext(base_name)

    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 1223444)
    name, ext = get_filename_ext(filename)

    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)

    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(tag__title__icontains=query))

        return self.filter(lookups).distinct()


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
         return self.get_queryset().filter()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()

        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=39.99)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)