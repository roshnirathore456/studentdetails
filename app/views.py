from django.shortcuts import render, redirect

from .models import Details, StudentSignup, TeacherSignUp, StudentLogin, TeacherLogin

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

def teacher_signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(username, password, password2)
        # Creating the Object of record every time user clicks on 'Add Data'
        teacherSignup = TeacherSignUp()
        teacherSignup.username = username
        teacherSignup.password = password
        teacherSignup.password2 = password2
        teacherSignup.save()

    # Fetching the details and saving in an dictionary
    from django.core import serializers
    teacherSignupData = serializers.serialize("python", TeacherSignUp.objects.all())

    # Dictionary to store the data and send it back to HTML format
    context = {
        'data': teacherSignupData,
    }
    return render(request, 'teachersignup.html', context)

def teacher_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        # Creating the Object of record every time user clicks on 'Add Data'
        teacherLogin = TeacherLogin()
        teacherLogin.username = username
        teacherLogin.password = password
        teacherLogin.save()

    # Fetching the details and saving in an dictionary
    from django.core import serializers
    teacherLoginData = serializers.serialize("python", TeacherLogin.objects.all())

    # Dictionary to store the data and send it back to HTML format
    context = {
        'data': teacherLoginData,
    }
    return render(request, 'teacherlogin.html', context)

def student_signup_view(request):
    # Getting data from the HTML and accepting
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(username, password, password2)
        # Creating the Object of record every time user clicks on 'Add Data'
        studentSignUp = StudentSignup()
        studentSignUp.username = username
        studentSignUp.password = password
        studentSignUp.password2 = password2
        studentSignUp.save()

    # Fetching the details and saving in an dictionary
    from django.core import serializers
    studentSignUpData = serializers.serialize("python", StudentSignup.objects.all())

    # Dictionary to store the data and send it back to HTML format
    context = {
        'data': studentSignUpData,
    }
    return render(request, 'studentsignup.html', context)

def student_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        studentLogin = StudentLogin()
        studentLogin.username = username
        studentLogin.password = password
        studentLogin.save()

    # Fetching the details and saving in an dictionary
    from django.core import serializers
    studentLoginData = serializers.serialize("python", StudentLogin.objects.all())

    # Dictionary to store the data and send it back to HTML format
    context = {
        'data': studentLoginData,
    }
    return render(request, 'studentlogin.html', context)
