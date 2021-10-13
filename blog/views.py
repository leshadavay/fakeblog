from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView 
from .models import Post

#function based view 
def home(request):
 
  return render(request,'blog/home.html',{
    'posts': Post.objects.all()
  })

#class based view
class PostListView(ListView):
  model = Post
  
  #overwrite template (escape from convention)
  template_name  = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']

#class based view
class PostDetailView(DetailView):
  model = Post


 
class PostCreateView(CreateView):
  model = Post
  
 

def about(request):
  return render(request,'blog/default.html',{'title':'About'})