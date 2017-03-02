"""tutorial URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

# from .swagger import SwaggerSchemaView

swagger_view = get_swagger_view(title=settings.API_NAME)
# custom swagger_view
# swagger_view = SwaggerSchemaView.as_view()

schema_view = get_schema_view(title=settings.API_NAME)

# Routers provide an easy way of automatically determining the URL conf
# router = routers.DefaultRouter()

urlpatterns = [
    #
    # url(r'^', include(router.urls)),

    # admin views
    url(r'^admin/', admin.site.urls),

    # http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    # https://django-rest-swagger.readthedocs.io/en/latest/
    url(r'^swagger/$', swagger_view, name='swagger-root'),

    # http://drfdocs.com/
    url(r'^docs/', include('rest_framework_docs.urls')),

    # API schemas
    # http://www.django-rest-framework.org/tutorial/7-schemas-and-client-libraries/
    url(r'^schema/$', schema_view),

    # App 'snippets'
    url(r'^', include('snippets.urls')),

    # App 'experiments'
    url(r'^', include('experiments.urls')),

    # App 'apiAdmin'
    url(r'^', include('apiAdmin.urls')),
]
