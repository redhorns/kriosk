from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.conf import settings
from django.utils import timezone


from panel.models import Service, Portfolio
from blog.models import Blog




# static sitemap
class StaticSitemap(Sitemap) :
    protocol = 'http' if settings.DEBUG else 'https'

    def items(self) :
        return ['home', 'about', 'service_list', 'portfolio_list', 'blog', 'contact', 'career']

    def location(self, item) :
        return reverse(item)

    def lastmod(self, item) :
        return timezone.now()

    def priority(self, item):
        return {'home': 1.00, 'about': 1.00, 'service_list': 1.00, 'portfolio_list': 1.00, 'blog': 1.00, 'contact': 1.00, 'career': 1.00,}[item]


# model sitemap : Services
class ServiceSitemap(Sitemap) :
    priority = 0.9
    protocol = 'http' if settings.DEBUG else 'https'

    def items(self) :
        return Service.objects.all()

    def lastmod(self, item) :
        return timezone.now()


# model sitemap : Blog
class BlogSitemap(Sitemap) :
    priority = 0.9
    protocol = 'http' if settings.DEBUG else 'https'

    def items(self) :
        return Blog.objects.all()

    def lastmod(self, item) :
        return timezone.now()


# model sitemap : Portfolio
class PortfolioSitemap(Sitemap) :
    priority = 0.8
    protocol = 'http' if settings.DEBUG else 'https'

    def items(self) :
        return Portfolio.objects.all()

    def lastmod(self, item) :
        return timezone.now()