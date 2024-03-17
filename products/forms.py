from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["image_url", "breadcrumb", "url"]
        labels = {"image_url_first": "Image URL"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        names = [(category.id, category.name) for category in categories]

        self.fields["category"].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"

    def clean(self):
        cleaned_data = super().clean()
        image_url_first = cleaned_data.get("image_url_first")
        image = self.cleaned_data.get("image")

        if not image_url_first and not image:
            raise forms.ValidationError(
                "You must provide either an image link or upload an image."
            )

        return cleaned_data
