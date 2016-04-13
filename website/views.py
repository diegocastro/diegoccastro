from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    context_object_name = 'post_list'
    template_name = "website/post/list.html"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects\
            .filter(published_date__lte=timezone.now())\
            .filter(language__exact=self.request.LANGUAGE_CODE)\
            .order_by('-published_date')


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "website/post/detail.html"
