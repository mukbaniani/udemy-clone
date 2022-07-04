from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('category', views.CategoryView, basename='category')
router.register('course', views.CourseAddView, basename='course')
router.register('rates', views.CreateRateView, basename='rates')
router.register('section', views.AddSection, basename='courses')
router.register('language', views.AddLanguage, basename='language')

urlpatterns = [] + router.urls
