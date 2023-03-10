from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete, PostUpdate, CategoryListView, subscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', cache_page(60*5) (PostDetail.as_view())),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('', PostList.as_view(), name='post_list'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]