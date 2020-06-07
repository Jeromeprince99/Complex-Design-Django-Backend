from django.conf.urls import url, include
from rest_framework import  routers
from complex_design_backend_rest_api.viewsets import PostViewSet

router = routers.DefaultRouter()
router.register('post',PostViewSet ,'post')

urlpatterns = [
    url('',include(router.urls) )
]
