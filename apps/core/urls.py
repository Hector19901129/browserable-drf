from core.views import IconViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, path


initialize = IconViewSet.as_view({
    'get': 'initialize',
})

router = DefaultRouter()
# initialize = FolderViewSet.as_view({'get': 'index'})
# resource = FolderViewSet.as_view({'get': 'resource'})

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('initialize/', initialize, name='snippet-list'),
#     path('initialize1/', initialize1, name='snippet-list'),
# ])
router.register(r'initialize', initialize, base_name="Icon")
urlpatterns = router.urls
