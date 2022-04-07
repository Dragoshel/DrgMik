from django import forms
from django.forms.widgets import NumberInput

from .widgets import DrgMikTextArea, DrgMikTextInput


class ArticleCreateForm(forms.Form):
    title = forms.CharField(
        label="Your title here",
        widget=DrgMikTextInput(attrs={"placeholder": "Enter a title here..."}))
    abstract = forms.CharField(
        label="Your abstract here",
        widget=DrgMikTextInput(attrs={"placeholder": "Enter an abstract here.."}))
    cover_img = forms.ImageField(label="Your cover image here")


class ParagraphCreateForm(forms.Form):
    text = forms.CharField(
        label="Your paragraph here",
        widget=DrgMikTextArea(attrs={"placeholder": "Enter a paragraph here..."}))
    index = forms.IntegerField(max_value=100, widget=NumberInput(attrs={"type": "hidden"}))


class ImageCreateForm(forms.Form):
    img = forms.ImageField(label="Your image here")
    index = forms.IntegerField(max_value=100, widget=NumberInput(attrs={"type": "hidden"}))
