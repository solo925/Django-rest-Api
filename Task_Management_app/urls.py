from django.urls import path,include
from rest_framework.routers import DynamicRoute,DefaultRouter
from .views import TaskViewSet
from .views import task_list, task_list_db


router = DefaultRouter()
router.register(r'task',TaskViewSet,basename='/')
# route2.register()


urlpatterns = [
    path('',include(router.urls)),
        path('tasks/', task_list, name='task_list'),  # Using the API endpoint
    path('tasks-db/', task_list_db, name='task_list_db'),  # Using the database

]
