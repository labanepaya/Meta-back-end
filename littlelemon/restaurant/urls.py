#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import UserViewSet

'''urlpatterns = [
    path('', views.index, name='index')
]'''

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]