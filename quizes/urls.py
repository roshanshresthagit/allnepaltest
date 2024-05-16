from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('Course/<int:category_id>/subjects/', display_subjects, name='display_subjects'),
    path('subjects/<int:subject_id>/', quiz_view, name='quiz_view'),
    path('quiz_results/', quiz_results, name='quiz_results'),

]
