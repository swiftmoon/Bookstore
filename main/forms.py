import layout as layout
import picture as picture
from django import forms
from .models import Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Field, Layout


class BookCreateForm(forms.ModelForm):
    name = forms.CharField(label='Ism', widget=forms.TextInput(attrs={'placeholder': 'Kitob nomi'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = Book
        fields = ['name', 'picture', 'author', 'email', 'describe', 'price']
        labels = {
            'picture': "Rasm",
            'author': "Muallif",
            'email': "Email",
            'describe': "Tavsif",
            'price': "Narx",

        }

    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout = Layout(
            HTML('')
        )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row'),
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn btn-primary'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-2'
        return helper
