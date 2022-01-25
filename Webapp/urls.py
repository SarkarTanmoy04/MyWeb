from django.urls import path
from Webapp import views

urlpatterns = [
    path('', views.index,name='Index'),
    path('about',views.about,name='About'),
    path('contact_us',views.contact_us,name='Contact'),
    path('testing',views.testingvar,name='Testingvar'),
    path('profile',views.Profile,name='Profile'),
]