from re import template
from django.forms.widgets import TextInput, Textarea


class DrgMikTextInput(TextInput):
	template_name = "builder/text_input.html"

class DrgMikTextArea(Textarea):
	template_name = "builder/textarea_input.html"