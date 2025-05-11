from django import forms 
from . import models

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = models.Bookmark
        fields = ['title', 'url', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter title',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })
        
        self.fields['url'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter the URL',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })
        
        self.fields['description'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter the Content',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })

