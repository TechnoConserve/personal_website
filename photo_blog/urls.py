"""photo_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os.path

from registration.backends.hmac.views import RegistrationView
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from custom_user.forms import CustomUserForm
import custom_user.views as account_views

urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/uwsgi/', include('django_uwsgi.urls')),
    url(r'^accounts/edit/$',
        account_views.edit_profile,
        name='edit_profile',
        ),
    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=CustomUserForm
        ),
        name='registration_register',
        ),
    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'^blog/', include('blog.urls')),

    # User stats
    url(r'^~(?P<username>[\w.@+-]+)/$', account_views.user_profile, name='user_profile'),

    url(r'', include('django.contrib.auth.urls')),
    url(r'', include(wagtail_urls)),    # At the end so as not to override others
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
