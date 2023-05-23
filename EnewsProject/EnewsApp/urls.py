from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about.html', views.about, name='about'),
    path('contactus.html', views.contactus, name='contactus'),
    path('bours.html', views.bours, name='bours'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]
