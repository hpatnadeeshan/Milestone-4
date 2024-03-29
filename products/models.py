from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    name_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    url = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=255)
    sku = models.IntegerField()
    gtin12 = models.BigIntegerField(null=True, blank=True)
    breadcrumb = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    availability = models.CharField(max_length=50)
    image_url = models.TextField(null=True, blank=True)
    image_url_first = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    reviews_count = models.IntegerField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    calory_content = models.CharField(max_length=100, null=True, blank=True)
    nutrition_analysis = models.TextField(null=True, blank=True)
    feeding_instructions = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    readonly_fields = ('image_url',)

    def save(self, *args, **kwargs):

        if not self.image_url_first and self.image_url:
            image_urls = (
                self.image_url.strip("[]").replace("'", "").split(", ")
            )
            if image_urls:
                self.image_url_first = image_urls[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
