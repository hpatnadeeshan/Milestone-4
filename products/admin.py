from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = (
        "image_url",)
    list_display = (
        "name",
        "url",
        "sku",
        "gtin12",
        "price",
        "availability",
        "average_rating",
        "display_image_urls",
    )

    ordering = ("sku",)

    def display_image_urls(self, obj):
        if obj.image_url:
            image_urls = (
                obj.image_url.strip("[]").replace("'", "").split(", ")
            )
            return mark_safe(
                "<br>".join(
                    [
                        '<a href="{0}">{0}</a>'.format(url)
                        for url in image_urls
                    ]
                )
            )
        else:
            return "No Image Available"

    display_image_urls.short_description = "Image URLs"


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
