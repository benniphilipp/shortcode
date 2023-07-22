from django.forms import ModelForm, forms
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Hidden, Div

from django.forms import ModelForm, Textarea, CharField, HiddenInput, Select




from .models import ShortcodeClass

class ShortcodeClassForm(forms.ModelForm):
    
    url_destination = forms.CharField(label="Ziel Url", widget=forms.TextInput(attrs={'placeholder': 'Ziel Url'}))
    url_titel = forms.CharField(label="Titel", widget=forms.TextInput(attrs={'placeholder': 'Titel'}))
    url_source = forms.CharField(label="Source", required=False, widget=forms.TextInput(attrs={'placeholder': 'z.B Google, Newsletter'}))
    url_medium = forms.CharField(label="Medium", required=False, widget=forms.TextInput(attrs={'placeholder': 'z.B. CPC, Banner, E-Mail'}))
    url_campaign = forms.CharField(label="Campaign", required=False, widget=forms.TextInput(attrs={'placeholder': 'z.B spring_sale'}))
    url_term = forms.CharField(label="Term", required=False, widget=forms.TextInput(attrs={'placeholder': 'z.B etwas'}))
    url_content = forms.CharField(label="Content", required=False, widget=forms.TextInput(attrs={'placeholder': 'z.B etwas'}))
    url_tags = forms.CharField(label="Tags", required=False, widget=forms.TextInput(attrs={'placeholder': 'z.B etwas anderes'}))

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('url_destination', css_class='form-group col-12 my-2'),
                css_class='row'
            ),
            Row(
                Column('url_titel', css_class='form-group col-12 my-2'),
                css_class='row'
            ),
            Row(
                Column('url_source', css_class='form-group col-md-6 my-2'),
                Column('url_medium', css_class='form-group col-md-6 my-2'),
                css_class='row'
            ),
            Row(
                Column('url_campaign', css_class='form-group col-md-6 my-2'),
                Column('url_term', css_class='form-group col-md-6 my-2'),
                css_class='row'
            ),
            Row(
                Column('url_content', css_class='form-group col-md-6 my-2'),
                Column('url_tags', css_class='form-group col-md-6 my-2'),
                css_class='row'
            ),
            Hidden('url_creator', '{{ admin }}'),
            HTML('<input id="crate-form-shortcode" class="btn btn-primary mt-3" type="submit" value="Neuen Link Kreieren">')
        )
    
    class Meta:
        model = ShortcodeClass
        fields = ['url_tags', 'url_destination' , 'url_titel', 'url_source', 'url_medium', 'url_campaign', 'url_term', 'url_content', 'url_tags', 'url_creator']
        
        widgets = {
            'url_creator': HiddenInput(),
        }

            