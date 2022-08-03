from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib import messages
from .forms import CreationForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "liked": liked
            },
        )

class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def create_posts(request):
    if request.method == 'POST':
        postitem_form = CreationForm(request.POST, request.FILES)
        if postitem_form.is_valid():
            postitem_form.save()
            messages.success(
                request, 'You have successfully posted an item!'
                )
            return redirect(reverse('home'))
    else:
        postitem_form = CreationForm()

    context = {
        'postitem_form': postitem_form
    }

    return render(request, "create_posts.html", context)

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def about(request):
    return render(request, "about.html")