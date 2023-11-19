
from django.urls import path
from .views import HomePageView
from . import views

app_name = 'companies'

urlpatterns = [
  path('',HomePageView.as_view(),name='home'),
  path('import/',views.import_excel, name='import_excel'),
    
]