from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from .models import Details


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

def studentdetails_view(request):
    return render(request, 'studentclick.html')

def student_signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, password,)

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('studentsignup')

        if len(username) > 14:
            messages.error(request, "Username must be under 20 characters!!")
            return redirect('studentsignup')

        myuser = User.objects.create_user(username=username, email=email, password=password)
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
            return redirect('studentdetails')
        else:
            messages.error(request, "Please enter valid credentials.")
            return redirect('studentlogin')
    return render(request, 'studentlogin.html')

def teacher_signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, password,)

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('teachersignup')

        if len(username) > 14:
            messages.error(request, "Username must be under 20 characters!!")
            return redirect('teachersignup')

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()
        return redirect('teacherlogin')
    return render(request, 'teachersignup.html')

def teacher_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(username=username, password=password)
        print("User is {}",user)
        if user is not None:
            login(request, user)
            # messages.success(request, ("Teacher Login Successful!"))
            return redirect('teacherfetch')
        else:
            messages.error(request, "Please enter valid credentials.")
            return redirect('teacherlogin')
    return render(request, 'teacherlogin.html')

def studentdetails_view(request):
    # Getting data from the HTML and accepting
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        useremail = request.POST['useremail']
        graduation = request.POST['graduation']
        phone = request.POST['phone']
        activityname = request.POST['activityname']
        activityassigned = request.POST['activityassigned']
        print(firstname, lastname, useremail, graduation, phone, activityname, activityassigned)

        obj = Details()
        obj.firstname = firstname
        obj.lastname = lastname
        obj.useremail = useremail
        obj.graduation = graduation
        obj.phone = phone
        obj.activityname = activityname
        obj.activityassigned = activityassigned
        obj.save()
        return render(request, "studentdetailssuccess.html")
    return render(request, 'studentdetailsform.html')

def teacher_fetch_student_details(request):
    # return render(request, 'studentdetailsfetch.html')
	studentfetch = Details.objects.all()
	return render(request, 'studentdetailsfetch.html',
		{'studentfetch': studentfetch})

