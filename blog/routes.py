from datetime import date

from django.utils.dateformat import DateFormat
from django.utils.formats import date_format

from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.models import Page


class BlogRoutes(RoutablePageMixin):

    @route(r'^(\d{4})/$')
    @route(r'^(\d{4})/(\d{2})/$')
    @route(r'^(\d{4})/(\d{2})/(\d{2})/$')
    def entries_by_date(self, request, year, month=None, day=None, *args, **kwargs):
        self.filtered_posts = self.get_posts().filter(date__year=year)
        if month:
            self.filtered_posts = self.filtered_posts.filter(date__month=month)
            df = DateFormat(date(int(year), int(month), 1))
            self.search_term = df.format('F Y')
        if day:
            self.filtered_posts = self.filtered_posts.filter(date__day=day)
            self.search_term = date_format(date(int(year), int(month), int(day)))
        return Page.serve(self, request, *args, **kwargs)
