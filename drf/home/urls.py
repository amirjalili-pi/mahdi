from django.urls import path
from .views import *
app_name = 'home'

urlpatterns = [
    path('one/', test),
    # path('persons/', show_persons),
    # path('person/<int:id>/', show_person),
    # path('create/', create_person),
]