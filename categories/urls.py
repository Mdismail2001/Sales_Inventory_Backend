from django.urls import path
from .views import(
    CategoryListView
)

urlpatterns = [
    path('/list-category',CategoryListView.as_view(), name='list-category'),
    # path('<int:pk>', views.CategoryDetail.as_view()),
]