from random import randint
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from account.models import User
from .forms import PostCreationForm


class Home(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'post'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.all()
        context['featured'] = reversed(Post.objects.all()[:4])

        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context['related'] = Post.objects.filter(tags__in=self.object.tags.all()).distinct()[:3]

        return context


class GetAuthorInfo(DetailView):
    model = User
    template_name = 'blog/author.html'
    context_object_name = 'author'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context['author_posts'] = Post.objects.filter(author=self.get_object())

        return context


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = PostCreationForm
    template_name = 'blog/create_post.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title) + '_' + form.instance.author.username + str(randint(0, 99999))

        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'tags', 'time_to_read', 'text', 'image']
    template_name = 'blog/update_post.html'
    login_url = 'login'


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = 'login'
    template_name = 'blog/confirm_to_delete.html'
    success_url = reverse_lazy('home')


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = f"s={self.request.GET.get('search')}&"
        return context
