from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('restaurant',index, name='home'),
    path('api/menu/', MenuItemsView.as_view(), name='menu'),
    path('api/menu/<int:pk>', SingleMenuItemView.as_view(), name='menu')
]