from django.urls import path

from .views import CreateStoreView, ListCreateCategoryView


urlpatterns = [
    path('create-store/', CreateStoreView.as_view(), name='create-store'),
    path('categories/', ListCreateCategoryView.as_view(), name='categories'),
]
