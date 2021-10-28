"""Illabunda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    # Keep the most generic at the bottom so that it does not override others
    path('', include(wagtail_urls)),
]

# wagtailadmin_urls provide the admin interface for wagtail, which is different to the admin interface for django
# wagtaildocs_urls provide location from which documents would be served. you don't need this if not using document features
# wagtail_urls is the base location from which wagtail site will be served.


# Add media handling
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
