#define URL route for index() view
from django.urls import path, include
from . import views

#import router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', include(router.urls)),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]