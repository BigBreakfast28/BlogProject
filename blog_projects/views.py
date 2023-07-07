from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost, Description
from .forms import BlogPostForm, DescriptionForm

# Create your views here.

def index(request):
    return render(request, 'blog_projects/index.html')

@login_required
def blogs(request):
    blogs = BlogPost.objects.order_by('date_added')
    blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs':blogs}
    return render(request, 'blog_projects/blogs.html', context)


@login_required
def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    if blog.owner != request.user:
        raise Http404
    
    descriptions = blog.description_set.order_by('-date_added')
    context = {'blog':blog, 'descriptions':descriptions}
    return render(request, 'blog_projects/blog.html', context) 

@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blog_projects:new_blog')
        
    context= {'form':form}
    return render(request, 'blog_projects/new_blog.html', context)

#Check to make sure BlogPost is the proper class I should be importing information from. 
@login_required
def new_description(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    
    if request.method != 'POST':
        form = DescriptionForm()
    else:
        form = DescriptionForm(data=request.POST)
        if form.is_valid():
            new_description = form.save(commit=False)
            new_description.blog = blog
            new_description.save()
            return redirect('blog_projects:new_description', blog_id=blog_id)
    
    context = {'blog': blog, 'form':form}
    return render(request, 'blog_projects/new_description.html', context)
    
@login_required
def edit_description(request, description_id):
    description = Description.objects.get(id=description_id)
    blog = description.blog
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = DescriptionForm(instance=description)
    else:
        form = DescriptionForm(instance=description, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_projects:blog', blog_id=blog.id)
        
    context = {'description':description, 'blog':blog, 'form':form}
    return render(request, 'blog_projects/edit_description.html', context)        
    
        