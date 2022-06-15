from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('category', views.CategoryView, basename='category')

urlpatterns = [] + router.urls
