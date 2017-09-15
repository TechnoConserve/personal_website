from django.template import Library

register = Library()


@register.inclusion_tag('blog/tags/archive_list.html', takes_context=True)
def archives_list(context):
    index_page = context['index_page']
    context['archives'] = index_page.get_posts().datetimes('date', 'day', order='DESC')
    return context
