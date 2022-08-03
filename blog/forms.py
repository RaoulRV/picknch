from django import forms
from .models import Post


class CreationForm(forms.ModelForm):
    
    class Meta:

        model = Post
        fields = (
            'item',
            'phone_number',
            'author',
            'address',
            'description',
            'featured_image',
        )


    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)