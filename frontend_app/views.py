from django.shortcuts import render, redirect

from django.http import HttpResponse

from.models import *

from.forms import *

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def home(request):

    home = Post.objects.all()

    return render(request, 'frontend/home.html', {'home':home})


def get_one(request, pst_id):
    if not request.user.is_authenticated:
        return redirect('frontend:log_in')


    home = Post.objects.get(id=pst_id)
    get_comment = Comment.objects.filter(post__id=pst_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        Comment.objects.create(name=name, comment=comment, post=home)
        messages.success(request, 'comment created')

    return render(request, 'frontend/get-one.html', {'home':home, 'comment':get_comment})


def register(request):
    if request.method == 'POST':
        form = Register(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('frontend:log_in')
            messages.success(request, 'user has been register')
    else:
        form = Register()

    return render(request, 'frontend/register.html', {'form':form})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('frontend:add_post')
        else:
            messages.error(request, 'username and password does not match')

    return render(request, 'frontend/login.html')


def view_user(request):
    user = User.objects.all().order_by('first_name')
    return render(request, 'frontend/view-user.html', {'user':user})


def view(request, get_id):
    get_user = User.objects.get(id=get_id)
    return render(request, 'frontend/view.html', {'get':get_user})

    
def add_post(request):
    if not request.user.is_authenticated:
        return redirect('frontend:log_in')

    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, 'product added successfully ')
    
    else:
        form = AddPost()

    return render(request, 'frontend/addpost.html', {'form':form})

def view_post(request):
    if not request.user.is_authenticated:
        return redirect('frontend:log_in')


    get_post = Post.objects.filter(created_by=request.user)

    return render(request, 'frontend/view-post.html', {'get':get_post})
@login_required(login_url='/talknet/')
def delete_post(request, pst_id):
    single_post = Post.objects.get(id=pst_id)
    single_post.delete()

    return redirect('frontend:view_post')


def edit_post(request, pst_id):
    edited = Post.objects.get(id=pst_id)
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES, instance=edited)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, 'product edited successfully')
    
    else:
        form = AddPost(instance=edited)

    return render(request, 'frontend/edit-post.html', {'form':form})

def video(request):
    if not request.user.is_authenticated:
        return redirect('frontend:log_in')

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, 'video added successfully ')
    
    else:
        form = VideoForm()

    return render(request, 'frontend/video.html', {'form':form})

def view_video(request):

    home = Video.objects.all()

    return render(request, 'frontend/view-video.html', {'home':home})

def get_video(request, pst_id):
    if not request.user.is_authenticated:
        return redirect('frontend:log_in')


    home = Video.objects.get(pk=pst_id)
    get_comment = Hello.objects.filter(post__pk=pst_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        Hello.objects.create(name=name, comment=comment, post=home)
        messages.success(request, 'comment created')

    return render(request, 'frontend/get-video.html', {'home':home, 'comment':get_comment})

def user_video(request):
    if not request.user.is_authenticated:
        return redirect('frontend:log_in')


    get_post = Video.objects.filter(created_by=request.user)

    return render(request, 'frontend/user-video.html', {'get':get_post})

def delete_video(request, pst_id):
    single_video = Video.objects.get(pk=pst_id)
    single_video.delete()

    return redirect('frontend:user_video')

def edit_video(request, pst_id):
    if not request.user.is_authenticated:
        return redirect('frontend:log_in')
    edit = Video.objects.get(pk=pst_id)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, 'video edited successfully ')
    
    else:
        form = VideoForm(instance=edit)

    return render(request, 'frontend/edit-video.html', {'form':form})


def confirm_logout(request):

    return render(request, 'frontend/confirm-logout.html')

def logout_view(request):

    logout(request)

    return redirect('frontend:log_in')

def contact_us(request):
    if not request.user.is_authenticated:
        return redirect('frontend:log_in')

    if request.method == 'POST':
        form = AddContact(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'data sent successfully')
        
        
    
    else:
        form = AddContact()

    return render(request, 'frontend/contact-us.html', {'form':form})

def advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'data sent successfully')
        
    
    else:
        form = AdvertisementForm()

    return render(request, 'frontend/advertisement.html', {'form':form})


def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('frontend:log_in')

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile edited successfully')
        else:
            messages.error(request, 'user not edited')
    else:
        form = Register(instance=request.user)


    return render(request, 'frontend/edit-profile.html', {'form':form})

def view_profile(request):

    return render(request, 'frontend/view-profile.html')

def about(request):

    return render(request, 'frontend/about.html')

def privacy(request):

    return render(request, 'frontend/privacy.html')

def advert(request):
    ading = Advertisement.objects.all()

    return render(request, 'frontend/advert.html', {'ading':ading})
def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        query_filter = Post.objects.all().filter(pst_title=search)
    else:
        messages.error(request, 'no result found')

    return render(request, 'frontend/search-result.html', {'query':query_filter})

def get_search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        query_filter = Video.objects.all().filter(pst_title=search)
    return render(request, 'frontend/get-search.html', {'query':query_filter})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
        update_session_auth_hash(request, form.user)
        messages.success(request, 'password change successfully')
    
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'frontend/change-password.html', {'form':form})

def application(request):

    return render(request, 'frontend/application.html')

def web_services(request):

    return render(request, 'frontend/web-services.html')

def forget_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'data sent successfully')
        
        
    
    else:
        form = PasswordForm()

    return render(request, 'frontend/forget-password.html', {'form':form})


def term_condition(request):

    return render(request, 'frontend/term-condition.html')

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    