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


def postview(request):
    return render(request, 'blog/post.html')


class GetPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
