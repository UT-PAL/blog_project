from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from login_app.forms import SignUpForm, UserProfileChange
from login_app.models import Follow,User_profile
from django.contrib.auth.models import User
from login_app.forms import EditInfo

from blog_app.models import Blog
# Create your views here.


def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form, 'registered':registered}
    return render(request, 'login_app/signup.html', context=dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'login_app/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    return render(request, 'login_app/profile.html', context={})

def show_followers(request):
    follower_list = Follow.objects.filter(following=request.user)
    return render(request, 'login_app/profile.html', context={'list': follower_list})

def show_following(request):
    following_list = Follow.objects.filter(follower=request.user)
    return render(request, 'login_app/profile.html', context={'list1':following_list})


@login_required
def user_change(request):
    current_user = User.objects.get(username=request.user)
    form = UserProfileChange(instance=current_user)

    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)

        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)

            return HttpResponseRedirect(reverse('login_app:profile'))

    return render(request, 'login_app/change_profile.html', context={'form':form})


@login_required
def edit_othersInfo(request):
    current_user = User.objects.get(username=request.user)
    form1= EditInfo(instance=current_user)
    if request.method == 'POST':
        form1= EditInfo(request.POST,request.FILES,instance=current_user)
        if form1.is_valid():
            form1.save(commit=True)
            form1 = EditInfo(instance=current_user)

            return HttpResponseRedirect(reverse('login_app:profile'))
    return render(request, 'login_app/edit_othersInfo.html', context={'form1':form1})



@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'login_app/pass_change.html', context={'form':form, 'changed':changed})


def user(request,username):
    other_user = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user,following=other_user)
    blogs = Blog.objects.filter(author=other_user)
    dict={'other_user':other_user,'already_followed':already_followed,'blogs':blogs}
    if other_user == request.user:
        return HttpResponseRedirect(reverse('login_app:profile'))
    return render(request,'login_app/other_user.html',context=dict)

def follow (request,username):
    following_user = User.objects.get(username=username)
    follower_user = User.objects.get(username=request.user)
    already_followed = Follow.objects.filter(follower=follower_user,following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user,following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('login_app:other_user',kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = User.objects.get(username=request.user)
    already_followed = Follow.objects.filter(follower=follower_user,following=following_user)
    already_followed.delete()
    return  HttpResponseRedirect(reverse('login_app:other_user',kwargs={'username':username }))



