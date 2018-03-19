from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('material/', views.MaterialListView.as_view(), name='material'),
    path('material/<int:pk>', views.MaterialDetailView.as_view(),
         name='material-detail'),
    path('mill/', views.MillListView.as_view(), name='mill'),
    path('mill/<int:pk>', views.MillDetailView.as_view(), name='mill-detail'),
    path('vendor/', views.VendorListView.as_view(), name='vendor'),
    path('vendor/<int:pk>', views.VendorDetailView.as_view(),
         name='vendor-detail'),
]
