from django.urls import re_path

from .views import BlogPageServe

urlpatterns = [
    re_path(
        r'^(?P<blog_path>[-\w\/]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        view=BlogPageServe.as_view(),
        name='blog_page_serve_slug'
    ),
    re_path(
        r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        view=BlogPageServe.as_view(),
        name='blog_page_serve'
    ),
]
