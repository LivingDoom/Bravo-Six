from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('faq', views.faq, name='faq'),
    path('welfare', views.welfare, name='welfare'),
    path('application', views.application, name='application'),
    path('unemploymentConfirmation', views.unemploymentConfirmation, name='unemploymentConfirmation'),
    path('gettingStarted', views.gettingStarted, name='gettingStarted'),
    path('login', views.login, name='login'),
    path('createAccount', views.createAccount, name='createAccount'),
]
