from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from profiles.models import Profile
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'account/login.html', {"error": '아이디 또는 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('index')
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            profile = Profile.objects.create(user=request.user, phonenumber=request.POST['phonenumber'])
            return redirect('index')
        else:
            return render(request, 'account/signup.html',{"pwerror":'패스워드가 일치하지 않습니다.'})
    return render(request, 'account/signup.html')


