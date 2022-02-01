from django import template
from django.conf import settings
from django.utils.html import format_html, mark_safe

register = template.Library()


@register.simple_tag()
def fontawesome_css():
    css_file = "wagtailiconify_fontawesome.min.css"
    href = f"{settings.STATIC_URL}wagtailiconify/css/{css_file}"

    return format_html(mark_safe(f'<link rel="stylesheet" href="{href}">'))
