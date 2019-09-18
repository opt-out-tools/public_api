"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import opt_out.public_api.api.views as api
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^submit_urls", api.submit),
    url(r"^submit_further_details", api.submit_further_details),
    url(r"^predict", api.predict),
    url(r"", api.home),
]
