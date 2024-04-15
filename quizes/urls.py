from django.urls import path
from .views import home, display_subjects

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/subjects/', display_subjects, name='display_subjects'),
]
