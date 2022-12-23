from django.urls import path

from .views import CreateStoreView, ListCreateCategoryView, ProductCreateView


urlpatterns = [
    path('create-store/', CreateStoreView.as_view(), name='create-store'),
    path('categories/', ListCreateCategoryView.as_view(), name='categories'),
    path('create-product/', ProductCreateView.as_view(), name='create-product'),
    # path('create-store-hyperlink/', CreateStoreHyperLinkedView.as_view()),
    
]
