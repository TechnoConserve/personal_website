from django.conf.urls import url
from django.urls import reverse

from .utils import strip_prefix_and_ending_slash
from .views import BlogPageServe

urlpatterns = [
    url(
        regex=r'^(?P<blog_path>[-\w\/]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        view=BlogPageServe.as_view(),
        name='entry_page_serve_slug'
    ),
    url(
        regex=r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        view=BlogPageServe.as_view(),
        name='entry_page_serve'
    ),
]


def get_entry_url(entry, blog_page, root_page):
    """
    Get the entry url given and entry page a blog page instances.
    It will use an url or another depending if blog_page is the root page.
    """
    if root_page == blog_page:
        return reverse('entry_page_serve', kwargs={
            'year': entry.date.strftime('%Y'),
            'month': entry.date.strftime('%m'),
            'day': entry.date.strftime('%d'),
            'slug': entry.slug
        })
    else:
        # The method get_url_parts provides a tuple with a custom URL routing
        # scheme. In the last position it finds the subdomain of the blog, which
        # it is used to construct the entry url.
        # Using the stripped subdomain it allows Puput to generate the urls for
        # every sitemap level
        blog_path = strip_prefix_and_ending_slash(blog_page.specific.last_url_part)
        return reverse('entry_page_serve_slug', kwargs={
            'blog_path': blog_path,
            'year': entry.date.strftime('%Y'),
            'month': entry.date.strftime('%m'),
            'day': entry.date.strftime('%d'),
            'slug': entry.slug
        })
