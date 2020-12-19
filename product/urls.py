from django.urls   import path
from product.views import PostView, GetView

urlpatterns = [
        path('/post', PostView.as_view()),
        path('/get', GetView.as_view()),
]

