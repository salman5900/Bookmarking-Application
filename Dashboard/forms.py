from django import forms 
from . import models

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = models.Bookmark
        fields = ['title', 'url', 'description', 'folder']

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

        self.fields['folder'].widget.attrs.update({
            'class': 'folder-select',
            'style': '''
                border: 2px solid #4a90e2;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 16px;
                background-color: #f9f9f9;
                color: #333;
                box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
                transition: border-color 0.3s ease;
            '''
        })


class FileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = ['name']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter file name',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'
        })
