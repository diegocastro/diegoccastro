from django.utils import timezone
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    context_object_name = 'post_list'
    template_name = "website/post/list.html"

    def get_queryset(self):
        return Post.objects\
            .filter(published_date__lte=timezone.now())\
            .filter(language__exact=self.request.LANGUAGE_CODE)\
            .order_by('-published_date')
