from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
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

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    redirect('post_detail_view', pk=pk)


################################################
################ Comments Views ################
################################################

@login_required
def add_comments_to_post(request, pk):
    """ In this function we are posting a comment on the published POST """
    post = get_object_or_404(Post, pk=pk) # Fetching 'POST' Class

    if request.method == 'POST':
        # Fetching 'Comments' Class if user has submitted a comment
        form = CommentsFormClass(request.POST)
        # Validating if comment passes all requirements.
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            # Redirecting to the POST on which was commented.
            return redirect('post_detail_view', pk=post.pk)

    else:
        form = CommentsFormClass()

    return render(request, 'Dumper/comment_form.html', {'form':form})

@login_required
def comment_approve(request, pk):
    """  """
    comment = get_object_or_404(Comments, pk=pk)
    comment.approve()
    return redirect('post_detail_view', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    redirect('post_detail_view', pk=post_pk)