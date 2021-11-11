from django.shortcuts import render, redirect
from .models import Thread
from .forms import ThreadForm, PostForm

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