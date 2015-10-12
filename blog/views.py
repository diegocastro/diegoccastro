from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .models import Post
from .forms import ContactForm


class PostList(ListView):
    queryset = Post.objects.filter(published_date__lte=timezone.now).order_by('-published_date')
    context_object_name = 'post_list'
    template_name = "blog/post/list.html"


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "blog/post/detail.html"


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = "blog/contact/index.html"
    success_url = reverse_lazy('blog:contact_view')
    success_message = 'Contato enviado com sucesso'

    def form_invalid(self, form):
        response = super(SuccessMessageMixin, self).form_invalid(form)
        messages.error(self.request, 'Por favor corrija os erros abaixo')

        return response

    def form_valid(self, form):
        form.send_email()

        return super(ContactView, self).form_valid(form)
