from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

# sitemap
from django.contrib.sitemaps.views import sitemap
from kriosk_main.sitemaps import StaticSitemap, ServiceSitemap, PortfolioSitemap, BlogSitemap


sitemaps = {
    'static': StaticSitemap,
    'service': ServiceSitemap,
    'blog': BlogSitemap,
    'portfolio': PortfolioSitemap,
}

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'', include('kriosk_main.urls')),
    url(r'', include('blog.urls')),
    url(r'', include('authentication.urls')),
    url(r'', include('panel.urls')),
    url(r'', include('inquiry.urls')),
    url(r'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]


urlpatterns += static (
    settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static (
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

