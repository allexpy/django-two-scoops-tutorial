"""application URL Configuration

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
import debug_toolbar

from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('two_scoops.urls')),
    path('extra/', include('extra.urls', namespace='extra')),
    path('tastings/', include('tastings.urls', namespace='tastings')),
    path('sprinkles/', include('sprinkles.urls')),
    path('flavors/', include('flavors.urls', namespace='flavors')),
    path('store/', include('stores.urls', namespace='store')),
    path('vouchers/', include('vouchers.urls', namespace='vouchers')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('__debug__/', include(debug_toolbar.urls)),
]
