from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Django Admin
    path('admin/', admin.site.urls),
    # Main page 
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    #Games home
    path('home', views.home, name='home'),
    # Laptop home
    path('about', views.about, name='about'),
    # Book home
    path('books/', views.books_view, name="books" ),
    # Author home
    path('author', views.authors_view, name='author'),
    # Car home
    path('car_home', views.car_home, name='car_home'),
    #Contact apps url
    path('contact/', include('contact.urls')),
    path('games/', include('games.urls')),
    path('laptop/', include('laptop.urls')),
    path('car/', include('car.urls')),
    path('book/', include('book.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)