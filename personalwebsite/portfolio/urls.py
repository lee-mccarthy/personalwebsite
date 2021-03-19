from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contact/', views.ContactMe.as_view(), name='contact'),
    path('thankyou/', views.ThankYou.as_view(), name='thankyou'),
    path('projects/<pk>/', views.ProjectDetail.as_view(), name='project_detail'),
]
