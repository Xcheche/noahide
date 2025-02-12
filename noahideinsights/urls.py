"""nicksblog URL Configuration

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
import posts.views
import sitepages.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', posts.views.home, name="home"),
    re_path(r'^posts/(?P<post_id>[0-9]+)/$', posts.views.post_details, name="post_detail"),
    re_path(r'^about/', sitepages.views.about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
