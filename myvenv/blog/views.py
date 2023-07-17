from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import TaskForm
from django.utils import timezone
# Create your views here.

def home(request):
    data=Post.objects.all()
    context={"data": data}
    return render(request,template_name="blog/home.html",context=context)

def detail(request,id):
    data=Post.objects.get(id=id)
    context={"data": data}
    return render(request,template_name="blog/detail.html",context=context)

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'blog/create_task.html', {'form': form})

def delete_task(request,pk):
    task=get_object_or_404(Post,pk=pk)
    task.delete()
    return redirect('home')
    
def mark_completed(request, todo_id):
    todo = Post.objects.get(id=todo_id)
    todo.mark_completed()
    return redirect('home')

def update_task(request,id):
    task=get_object_or_404(Post,id=id)
    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'blog/update_task.html', {'form': form})
    


