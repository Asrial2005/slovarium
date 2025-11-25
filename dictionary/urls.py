from django.urls import path
from . import views

urlpatterns = [
    path('', views.term_list, name='term_list'),  # Главная страница (поиск)
    path('all-terms/', views.all_terms, name='all_terms'),  # ← Новый маршрут
    path('<int:pk>/', views.term_detail, name='term_detail'),
    path('search/', views.search_terms, name='search_terms'),
    path('autocomplete/', views.autocomplete_terms, name='autocomplete_terms'),
]