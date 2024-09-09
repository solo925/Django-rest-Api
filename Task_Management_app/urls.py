from django.urls import path,include
from rest_framework.routers import DynamicRoute,DefaultRouter
from .views import TaskViewSet,ContentGet


router = DefaultRouter()
router2 = DynamicRoute('tas',"tasiki","details here",initkwargs="tas")
router.register(r'task',TaskViewSet,basename='/')
# route2.register()


urlpatterns = [
    path('',include(router.urls))

]
