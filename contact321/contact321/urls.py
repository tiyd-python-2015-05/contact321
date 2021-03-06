"""contact321 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from contacts import views
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet, base_name="contact")

urlpatterns = [
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^contacts/(?P<contact_pk>\d+)/phones/$',
        views.PhoneListCreateView.as_view(), name="phone-list"),
    url(r'^phones/(?P<pk>\d+)/$', views.PhoneDetailView.as_view(),
        name="phone-detail"),
    url(r'^contacts/(?P<contact_pk>\d+)/emails/$',
        views.EmailListCreateView.as_view(), name="email-list"),
    url(r'^emails/(?P<pk>\d+)/$', views.EmailDetailView.as_view(),
        name="email-detail"),
]
