from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['image_url','breadcrumb','url']
        labels = {
            'image_url_first': 'Image URL'  
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        names = [(category.id, category.name) for category in categories]

        self.fields['category'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
