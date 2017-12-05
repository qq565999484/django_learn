from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.urls import reverse



def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
  
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.save()
           return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'post_edit.html',{'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        print(form)
    return render(request, 'post_edit.html', {'form': form})
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request,'post_draft_list.html',{'posts':posts})

def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
