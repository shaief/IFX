"""ifx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
# from django.conf.urls import url, include
# from django.contrib import admin


# urlpatterns = [
#    url(r'', include("movies.urls")),
#    url(r'^admin/', admin.site.urls),
#    url(r'^i18n/', include('django.conf.urls.i18n'))
# ]


from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

urlpatterns = i18n_patterns(
    url(r'', include("movies.urls")),
    url(r'^people/', include("people.urls")),
    url(r'^search/', include("search.urls")),
    url(r'^collections/', include("curation.urls")),
    url(r'^links/', include("links.urls")),

    url(r'^enrich/', include("enrich.urls")),

    url(r'^logs/', include("editing_logs.urls")),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
)
