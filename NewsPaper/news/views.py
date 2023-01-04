from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    # название модели
    model = Post
    # поле для сортировки - по дате создания ( '-' - от конца)
    ordering = '-dateCreation'

    template_name = 'news.html'

    context_object_name = 'news'



class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'