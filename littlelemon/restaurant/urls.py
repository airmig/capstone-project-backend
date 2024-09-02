from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',index, name='home'),
    path('api/menu-items/', MenuItemsView.as_view(), name='menu'),
    path('api/menu-items/<int:pk>', SingleMenuItemView.as_view(), name='menu'),
    path('api-token-auth/', obtain_auth_token)
]