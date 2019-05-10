from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })
