from django.shortcuts import render
from Dumper.models import Post, Comments
from Dumper.forms import PostFormClass,CommentsFormClass
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)


# Create your views here.

class AboutView(TemplateView):
    """ This view just mentions the purpose of the website """
    template_name = 'about.html'

class PostListView(ListView):
    """ We will be listing out all the User Posts in the homepage """
    model = Post # connecting to Post model

    def get_queryset(self):
        """ fetching lte --> 'less than equal' data """
        return Post.objects.filter(publisded_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    """ If not signed In, user will be redirected to login """
    login_url = '/login/'
    required_field_name = 'Dumper/post_detail.html'

    form_class = PostFormClass
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    """ If not signed In, user will be redirected to login """
    login_url = '/login/'
    required_field_name = 'Dumper/post_detail.html'

    form_class = PostFormClass
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list_view')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'Dumper/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')