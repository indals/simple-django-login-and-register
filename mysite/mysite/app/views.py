# from django.http import request
# from django.shortcuts import render, HttpResponse
# from datetime import datetime
# from django.contrib import messages

# from datetime import datetime
# from django.contrib import messages
# # Create your views here.

# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import login
# from django.contrib.auth.models import User
# from django.shortcuts import render, HttpResponse

# def index(request):
#     return render(request, 'index.html')

# def signup(request):
#     # if request.method == "POST":
#         # username = request.POST('username')
#         # fname = request.POST('fname')
#         # lname = request.POST('lname')
#         # email = request.POST('email')
#         # phone = request.POST('phone')
#         # password1 = request.POST('password1')
#         # password2 = request.POST('password2')
#         # myuser = User.objects.create_user(username, email, password1)
#         # myuser.firstname = fname
#         # myuser.lastname = lname
#         # myuser.save()
#         messages.success(request, "Your accout has been succefully created!!") 
#         return render(request, 'signup.html')

# def signin(request):
#     return render(request, 'signin.html')

# def signout(request):
#     pass



from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

def index(request):
    if request.user.is_anonymous:
        print(request.user)
        return render (request, 'signup.html')
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        print(request.user)
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        # print(user.objects.filter(username=username))

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            # messages.success('<p class="success_login">You were successfully login</p>')
            # messages.success(request, 'Profile details updated.')
            return render(request, 'login.html')

        # if user.objects.filter(username=username) is None:
        if not User.objects.filter(username = username).exists():
            messages.warning(request,'User is not registered please do registration first!!')
            return render(request, 'index.html')
        else:
            # No backend authenticated the credentials
            print("ERROR")
            messages.warning(request,'Username/Password is not correct!!')
            return render(request, 'index.html')
            # return HttpResponse("Username/Password is not correct!!")


    return render(request, 'index.html')

def logoutUser(request):
    logout(request)


def logoutUser(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if User.objects.filter(username=uname).count()>0:
            messages.warning(request,'user is already exist!')
            return redirect('signup')
        else:
            user = User(username=uname, password=pwd)
            user.phone=request.POST.get('phone')
            user.email=request.POST.get('email')
            user.password=request.POST.get('pwd')
            user.set_password(pwd)
            user.save()
            messages.warning(request,'You have signed up successfully!!')
            return redirect('login')
    else:
        return render(request, 'signup.html')