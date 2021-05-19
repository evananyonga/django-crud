from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, edit
from django.urls import reverse_lazy
from .models import Post, User
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class UpdatePost(edit.UpdateView):
    model = Post
    template_name = 'post_detail.html'
    fields = ['content']
    success_url = reverse_lazy('post_detail.html')


class DeletePost(edit.DeleteView):
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('post_detail.html')


class CreatePost(edit.CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = [
        'post',
        'user'
    ]
    success_url = reverse_lazy('post_detail.html')


class CreateUser(edit.CreateView):
#     def register_request(request):
#         if request.method == "POST":
#             form = User(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 login(request, user)
#                 messages.success(request, 'Registration successful')
#                 return redirect("home")
#             messages.error(request, "Unsuccessful Registration, Invalid information")
#         form = User
#         return render(request=request, template_name="register.html", context={"register_form":form})
#
#
# def get_query_set(self):
#     return User.objects.order_by['-date_added']

    model = User
    fields = [
        'username',
        'email',
        'password'
    ]
    template_name = 'register.html'
