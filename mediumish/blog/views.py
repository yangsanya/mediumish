from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['related'] = Post.objects.filter(tags__in=self.object.tags.all()).distinct()[:3]

        return context
