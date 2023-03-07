from django.urls import path
from home import views


urlpatterns = [
    path('', views.analyze, name='analyze'),
    path('analyze/', views.output, name='output'),
]
