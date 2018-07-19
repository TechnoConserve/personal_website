from django.contrib.auth import get_user_model

from wagtail.wagtailcore.models import Page
from wagtail.tests.utils import WagtailPageTests

from .models import BlogIndexPage, BlogPage


class TestBlogPage(WagtailPageTests):
    def setUp(self):
        home = Page.objects.get(slug='home')
        self.user = get_user_model().objects.create_user(username='test', first_name='Test', last_name='User',
                                                         email='test@test.test', password='pass')
        self.xml_path = "example_export.xml"
        self.blog_index = home.add_child(instance=BlogIndexPage(
            title='Blog Index', slug='blog', search_description='search description',
            owner=self.user))

    def test_index(self):
        url = self.blog_index.url
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

        blog_page = self.blog_index.add_child(instance=BlogPage(
            title='Blog Page', slug='blog_page1', search_description='search description', intro='Intro',
            owner=self.user))
        url = blog_page.url
        res = self.client.get(url)
        self.assertContains(res, "Blog Page")
