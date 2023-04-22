from django.contrib.auth import get_user_model
from django import template

from django.utils.html import escape
from django.utils.safestring import mark_safe

from django.utils.html import format_html

register = template.Library()


user_model = get_user_model()

# Register the filter function into the Library with its filter function.
@register.filter
def author_details(author, current_user=None):
  if not isinstance(author, user_model):
    # return empty string as safe default
    return ""

  if author == current_user:
    return format_html('<strong>me</strong>')

  if author.first_name and author.last_name:
    # name = escape(f"{author.first_name} {author.last_name}")
    name = f"{author.first_name} {author.last_name}"
  else:
    # name = escape(f"{author.username}")
    name = f"{author.username}"

  if author.email:
    # email = escape(author.email)
    # email = author.email
    # prefix = f'<a href="mailto:{email}">'
    prefix = format_html('<a href="mailto:{}">', author.email)
    # suffix = "</a>"
    suffix = format_html('</a>')
  else:
    prefix = ""
    suffix = ""

  # return mark_safe(f'{prefix}{name}{suffix}')
  # return f'{prefix}{name}{suffix}'
  return format_html('{}{}{}', prefix, name, suffix)