from django.urls import path
from .views import test, show_persons, show_person, create_person
app_name = 'home'

urlpatterns = [
    path('one/', test),
    path('persons/', show_persons),
    path('person/<int:id>/', show_person),
    path('create/', create_person),
]