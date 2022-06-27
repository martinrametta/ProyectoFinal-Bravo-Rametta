from django.shortcuts import render, redirect
from .models import *


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from BlogApp.forms import *


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Users.models import Avatar




def home(request):
    #aca se busca si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''
    
    posts = Post.objects.all().order_by('-date') [0:3]
    return render (request, 'BlogApp/home.html', {'avatar':avatar, 'posts': posts})

#Creacion de CRUD

class PostList(ListView):
    model = Post
    template_name = 'BlogApp/posts.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'BlogApp/post_detail.html'

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'


# Creamos el  viewpost
def posts(request):
    
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    posts = Post.objects.all().order_by('-date')
    return render(request, "BlogApp/posts.html", {"posts":posts, "avatar":avatar})

#agregar post

@login_required
def postForm(request):
    #buscamos si el usuario tiene avatar:
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method == 'POST':
        myForm = PostForm(request.POST, request.FILES)
        print(myForm)

        if myForm.is_valid():
            info = myForm.cleaned_data
            post = Post(title=info['title'], subtitle=info['subtitle'], author=info['author'],image=info['image'], content=info['content'])
            post.save()
            return redirect('blogapp:Posts')
    else:
        myForm = PostForm()
    return render(request, 'BlogApp/post_form.html', {"myForm":myForm, "avatar":avatar})

#editar post

@login_required
def editPost(request, post_id):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogapp:Posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'BlogApp/posteo_editar.html',{'form':form, 'avatar':avatar, 'title':post.title})


#buscar post
def searchPost(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    return render(request, 'BlogApp/searchPost.html', {"avatar":avatar})

def searchResult(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.GET["title"]:
        title = request.GET["title"]
        post = Post.objects.filter(title__icontains=title).order_by("-date")
        return render(request, 'BlogApp/searchPost.html', {"post":post, "avatar":avatar})
    else:
        response="You haven't entered any data."
    return render(request, 'BlogApp/posts.html', {"response":response, "avatar":avatar})


#Acerca de nosotros

def about(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    return render(request, "BlogApp/acerca.html", {'avatar':avatar})
