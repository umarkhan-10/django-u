from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    # Car home
    path('car_home', views.car_home, name='car_home'),
    #Contact apps url
    path('contact/', include('contact.urls')),
    path('games/', include('games.urls')),
    path('laptop/', include('laptop.urls')),
    path('car/', include('car.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)