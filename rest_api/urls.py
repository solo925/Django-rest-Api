from django.urls import path,include
from . import views
from . views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',ArticlesViewset,basename="article")

# Create your views here.
urlpatterns=[
   path('viewset/',include(router.urls)),
   path('viewset/<int:pk>/',include(router.urls)),
   # path('article/',article_list),
   path('article/',ArticleAPIView.as_view()),
   # path('detail/<int:pk>/',article_details),
   path('detail/<int:id>/',ArticleDetails.as_view()),
   path('genericarticle/<int:id>/',GenericApIViews.as_view()),
]
