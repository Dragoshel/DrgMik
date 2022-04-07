from django import template
from django.template.loader import get_template

from drgmik.models import Image, Paragraph

register = template.Library()

prg_template = get_template("blog/paragraph.html")
img_template = get_template("blog/image.html")


@register.simple_tag
def render_line(line):
    if isinstance(line, Paragraph):
        return prg_template.render({"line": line})
    elif isinstance(line, Image):
        return img_template.render({"line": line})
