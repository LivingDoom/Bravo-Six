from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('faq', views.faq, name='faq'),
    path('welfare', views.welfare, name='welfare'),
    path('apply', views.apply, name='apply'),
    path('unemploymentConfirmation', views.unemploymentConfirmation, name='unemploymentConfirmation'),
]
