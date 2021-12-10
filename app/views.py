from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction

from datetime import datetime
from django.utils import timezone

from app.models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


#log in view
def signin(request):
    if request.method == "POST":
        this_username = request.POST['username']
        this_password = request.POST['password']
        user = authenticate(username=this_username, password=this_password)
        login(request, user)
    return redirect('app:index')


#signout view
def signout(request):
    logout(request)
    return redirect('app:index')


#signup view
def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            try:
                with transaction.atomic():
                    user_obj = myCustomUser.objects.create(
                        username = request.POST['username'],
                        email = request.POST['email'],
                        password = make_password(request.POST['password'], salt=None, hasher='default'),
                        userType = request.POST['userType'],
                    )
                    user_obj.save()
                    return redirect('app:index')
            except IntegrityError:
                print("Error")
    return render(request, 'signup.html')


#approve user view
def approve(request, user_id):
    if request.user.is_superuser or (request.user.isVarified and request.user.userType == 'Admin'):
        user = myCustomUser.objects.get(id=user_id)
        user.isVarified = True
        user.save()
    return redirect('app:index')

#refuse user view
def refuse(request, user_id):
    if request.user.is_superuser or (request.user.isVarified and request.user.userType == 'Admin'):
        user = myCustomUser.objects.get(id=user_id)
        user.isVarified = False
        user.save()
    return redirect('app:index')


#all student list view
def students(request):
    students = myCustomUser.objects.filter(userType='Student')
    return render(request, 'students.html', {'students': students})

#all teacher and admin list view
def teachers(request):
    teachers = myCustomUser.objects.filter(userType='Teacher')
    admins = myCustomUser.objects.filter(userType='Admin')
    return render(request, 'teachers.html', {'teachers': teachers, 'admins' : admins})


#all Blogs view
def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

#blog view
def blogDetails(request, blog_id):
    blogs = Blog.objects.get(id=blog_id)
    return render(request, 'blogDetails.html', {'blogs': blogs})

#add blog
def addBlog(request):
    if request.method == "POST" and (request.user.isVarified or request.user.is_superuser):
        blog = Blog.objects.create(
            title = request.POST['title'],
            body = request.POST['body'],
            author = request.user,
            created_at = timezone.now(),
            picture = request.FILES['picture'],
        )
        blog.save()
        return redirect('app:blogs')
    return render(request, 'addBlog.html')