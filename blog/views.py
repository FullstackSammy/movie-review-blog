from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your comment was succesfully posted!',
            )
            return HttpResponseRedirect(request.path_info)
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm(),
            }
        )

    def delete_own_comment(request, id=None):
        comment = get_object_or_404(Comment, id=id)
        if (
            comment.name ==
            request.user.username
            and request.user.is_authenticated
        ):
            comment.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your comment has been deleted.'
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.add_message(
                request, messages.ERROR, 'An error has occured')

    def edit_own_comment(request, id=None):
        comment = get_object_or_404(Comment, id=id)
        if request.method == 'POST':
            if (
                comment.name ==
                request.user.username
                and request.user.is_authenticated
            ):
                form = CommentForm(data=request.POST)
                if form.is_valid():
                    comment.body = form.cleaned_data['body']
                    comment.save()
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        'Your comment has been edited.'
                    )
                    return HttpResponseRedirect(
                        request.META.get('HTTP_REFERER'))
                else:
                    messages.add_message(
                        request, messages.ERROR, 'An error has occured')

        return render(
            request,
            "edit_comment.html",
            {
                'comment': comment,
                'comment_form': CommentForm(instance=comment)
            }
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class Suggestions(TemplateView):

    template_name = "movie_suggestions.html"
