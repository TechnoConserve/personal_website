import datetime

from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from .routes import BlogRoutes

LANGUAGES = (
    # Each code block is tagged with the language used so highlight.js marks the code up correctly
    ('python', 'Python'),
    ('django', 'Django'),
    ('css', 'CSS'),
    ('http', 'HTTP'),
    ('javascript', 'JavaScript'),
    ('bash', 'Bash'),
    ('ini', 'Ini'),
    ('sql', 'SQL'),
    ('json', 'JSON'),
    ('markdown', 'Markdown'),
    ('html', 'HTML'),
    ('xml', 'XML'),
    ('java', 'Java'),
    ('nginx', 'Nginx'),
)


class CodeBlock(blocks.StructBlock):
    code = blocks.TextBlock(max_length=8000)
    language = blocks.ChoiceBlock(choices=LANGUAGES, required=False, default='python')

    class Meta:
        template = 'blocks/code.html'
        icon = 'spinner'
        label = 'Code chunk'


class Heading(blocks.CharBlock):
    class Meta:
        template = 'blocks/heading.html'
        icon = 'grip'
        label = 'Heading'


class BlogIndexPage(BlogRoutes, Page):
    intro = RichTextField(blank=True)
    about = RichTextField(blank=True, help_text='What is the blog about?')

    filtered_posts = None

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('about', classname="full"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro', 'about'),
    ]

    subpage_types = [
        'blog.BlogPage',
    ]

    def get_posts(self):
        return BlogPage.objects.descendant_of(self).live().order_by('-date')

    def get_context(self, request, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        context['index_page'] = self
        return context


class BlogTagIndexPage(Page):
    def get_context(self, request):
        #Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter().filter(tags__name=tag)

        # Update template context
        context = super(BlogTagIndexPage, self).get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


BLOCK_TYPES = [
    ('heading', Heading(classname='full title')),
    ('paragraph', blocks.RichTextBlock(requeried=True, classname='paragraph')),
    ('code_chunk', CodeBlock()),
]


class BlogPage(Page):
    date = models.DateTimeField(
        'Post date', default=datetime.datetime.today,
        help_text=("This date is displayed on the blog post. It is not used "
                   "to schedule posts to go live at a later date.")
    )
    intro = models.CharField(max_length=250)
    body = StreamField(block_types=BLOCK_TYPES, verbose_name='body')
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading='Blog information'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label='Gallery images'),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
