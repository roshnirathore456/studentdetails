from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def home(request):
    return render(request, "authentication/index.html")

def home_view(request):
    return render(request, 'index.html')

def adminclick_view(request):
    return render(request, 'adminclick.html')

def teacherclick_view(request):
    return render(request, 'teacherclick.html')

def studentclick_view(request):
    return render(request, 'studentclick.html')

def student_signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(username, password, password2)

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if len(username) > 14:
            messages.error(request, "Username must be under 20 characters!!")
            return redirect('home')

        if password != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        myuser = User.objects.create_user(username, password, password2)
        myuser.username = username
        myuser.password = password
        myuser.password2 = password2
        myuser.save()
        return redirect('studentlogin')
    return render(request, 'studentsignup.html')

def student_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(username=username, password=password)
        print("User is {}",user)
        if user is not None:
            login(request, user)
            uname = user.username
            return render(request, "authentication/index.html", {"uname": uname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    return render(request, 'studentlogin.html')
