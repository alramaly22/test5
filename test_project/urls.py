from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('calc/', views.calc, name='calc'),
    path('calc2/', views.calc2, name='calc2'),
    path('card/', views.card, name='card'),
    path('wheel/', views.wheel, name='wheel'),
    path('book/', views.book, name='book'),
    path('webhook/paid/', views.paid_webhook, name='paid_webhook'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
