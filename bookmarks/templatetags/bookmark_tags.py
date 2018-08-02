from django import template
from django.db import models
from django.urls import reverse
from django.utils.html import format_html_join

from bookmarks.models import Tag

register = template.Library()


@register.simple_tag(takes_context=True)
def tag_cloud(context, owner=None):
    url = reverse('bookmark_list_view')
    filters = {'bookmark__is_public': True}

    if owner is not None:
        url = reverse('user_bookmark_view', kwargs={'username': owner.username})
        filters['bookmark__owner'] = owner
    if context['user'] == owner:
        del filters['bookmark__is_public']

    tags = Tag.objects.filter(**filters)
    tags = tags.annotate(count=models.Count('bookmark'))
    tags = tags.order_by('name').values_list('name', 'count')
    fmt = '<a href="%s?tag={0}">{0} ({1})</a>' % url
    return format_html_join(', ', fmt, tags)
