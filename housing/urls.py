from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ContactUs,
    Home,
    HousingStats,
    HousingAI,
    Technology
)
from . import views

urlpatterns = [
    path('', Home, name='housing-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='housing-about'),
    path('contact/', ContactUs, name='contact-page'),
    path('sales/', PostListView.as_view(), name='hot-sales'),
    path('housing_stats/', HousingStats, name='housing-stats'),
    path('housing_ai/', HousingAI, name='housing-ai'),
    path('technology/', Technology, name='tech-page')
]