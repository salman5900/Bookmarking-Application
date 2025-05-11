from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add custom widget classes for styling
        self.fields['username'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter username',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })
        
        self.fields['password1'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter password',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })
        
        self.fields['password2'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Confirm password',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })


class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add custom widget classes for styling
        self.fields['username'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter username',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Enter password',
            'style': 'border-radius: 5px; padding: 10px; font-size: 16px;'  # Custom styling
        })
