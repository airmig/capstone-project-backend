from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('restaurant',index, name='home'),
    path('api/menu/', MenuItemsView.as_view(), name='menu'),
    path('api/menu/<int:pk>', SingleMenuItemView.as_view(), name='menu'),
    path('api-token-auth/', obtain_auth_token)
]