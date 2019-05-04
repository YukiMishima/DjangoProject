from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.http import HttpResponse


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_edit(request, post_id=None):
    # return HttpResponse('日記の編集')
    if post_id:
        # return HttpResponse('日記を編集します')
        post = get_object_or_404(Post, pk=post_id)
    else:
        # return HttpResponse('日記を追加します')
        post = Post()

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', dict(form=form, post_id=post_id))


def post_del(request, post_id):
    # return HttpResponse('日記の削除')
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('blog:post_list')