from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    code = forms.CharField(max_length=200, widget=forms.TextInput({ "placeholder": "B001"}))
    class Meta:
        model = Book
        exclude = ['id','slug','published', 'create', 'updated']
        #   widgets = {
        #     'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
        #     'password' : forms.PasswordInput(attrs = {'placeholder': 'Password'}),
        # }
        

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['code'].error_messages = {
            'required':'Please enter book code',
            
        }
        self.fields['name'].error_messages = {
            'required':'Please enter book name',
        }
        self.fields['price'].error_messages = {
            'required':'Please enter book price',
            'invalid':'Please enter a valid book price',
        }
    
    def clean(self):
        cleaned_data = super(BookForm, self).clean()
        if not cleaned_data.get('category'):
            self.add_error('category', 'Please select category name')
        
        if not cleaned_data.get('author'):
            self.add_error('author', 'Please select author name')
        
        if not cleaned_data.get('level'):
            self.add_error('level', 'Please select level')