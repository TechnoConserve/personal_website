from django_registration.views import RegistrationView
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images.views.serve import ServeView
from wagtail import urls as wagtail_urls

from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin

from landing.views import landing
from civ.views import civ_webhook
from custom_user.forms import CustomUserForm
import custom_user.views as account_views

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('django-admin/', admin.site.urls),
    path('accounts/edit/',
         account_views.edit_profile,
         name='edit_profile',
         ),
    path('accounts/register/',
         RegistrationView.as_view(
             form_class=CustomUserForm
         ),
         name='registration_register',
         ),
    path('accounts/', include('django_registration.backends.activation.urls')),

    path('blog/', include('blog.urls')),

    path("webhooks/civ/bakrui9vwrtuv2dax4a354yit/", civ_webhook),

    # User stats
    path('~<username>/', account_views.user_profile, name='user_profile'),

    re_path(r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(), name='wagtailimages_serve'),

    # Landing page to choose blog or photography
    path('', landing, name='landing'),
    path('', include('django.contrib.auth.urls')),
    path('', include(wagtail_urls)),
]

if settings.DEBUG:
    import os.path
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
