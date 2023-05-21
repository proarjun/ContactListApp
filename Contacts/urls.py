from django.urls import path
from .views import ContactList, DetailViewList

urlpatterns = [
    path('', ContactList.as_view(), name='Contact List'),
    path('<int:id>', DetailViewList.as_view(), name='DetailView List'),
]