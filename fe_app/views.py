from django.shortcuts import render, redirect
from .models import Thread, Post, Comment
from .forms import ThreadForm, PostForm, CommentForm

def index(request):
    """Home page of forumerrorly."""
    return render(request, 'fe_app/index.html')

def threads(request):
    """Shows all threads/threads."""
    threads = Thread.objects.order_by('date_added')   # sort threads by date
    context = {'threads': threads}   
    return render(request, 'fe_app/threads.html', context)

def thread(request, thread_id):
    """A single thread and all related posts."""
    thread = Thread.objects.get(id=thread_id)
    posts = thread.post_set.order_by('-date_added')  # get all posts under thread
    context = {'thread': thread, 'posts': posts}
    return render(request, 'fe_app/thread.html', context)

def new_thread(request):
    """Add a new thread."""
    if request.method != 'POST':
        form = ThreadForm()   # create a blank form
    else:
        form = ThreadForm(data=request.POST)     # process the data inputted into form
        if form.is_valid():
            form.save()
            return redirect('fe_app:threads')
    
    # show an empty form if invalid input
    context = {'form': form}
    return render(request, 'fe_app/new_thread.html', context)

def new_post(request, thread_id):
    """Add a new post to a thread."""
    thread = Thread.objects.get(id=thread_id)
    # comments = thread.comment_set.order_by('-date_added')  # get all comments under thread

    if request.method != 'POST':
        form = PostForm()   # no data input, so make blank post
    else:
        form = PostForm(data=request.POST)  # process inputted data

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.thread = thread
            new_post.save()
            return redirect('fe_app:thread', thread_id=thread_id)
    
    context = {'thread': thread, 'form': form}
    return render(request, 'fe_app/new_post.html', context)

def new_comment(request, post_id,thread_id):
    """Add a new comment to a thread."""
    # thread = Thread.objects.get(id=thread_id)
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        form = CommentForm()   # no data input, so make blank comment
    else:
        form = CommentForm(data=request.POST)  # process inputted data

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.thread = thread
            new_comment.post = post
            new_comment.save()
            return redirect('fe_app:thread', thread_id=thread_id)   # redirects to thread of post where comment was added
    
    context = {'thread': thread, 'post': post, 'form': form}
    return render(request, 'fe_app/new_comment.html', context)

def edit_post(request, post_id):
    """Edit an existing post."""
    post = Post.objects.get(id=post_id)
    thread = post.thread

    if request.method != 'POST':
        form = PostForm(instance=post)  # auto fill with current entry
    else:
        form = PostForm(instance=post, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('fe_app:thread', thread_id=thread.id)
    
    context = {'post': post, 'thread': thread, 'form': form}
    return render(request, 'fe_app/edit_post.html', context)