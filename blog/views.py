from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })
