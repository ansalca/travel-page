from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']     # POST['name of input field in credentials.html']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
    return render(request,'credential.html')
#
# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
#
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('login')
#         else:
#             messages.error(request, 'Error in form data')
#     else:
#         form = UserCreationForm()
#     return render(request, 'credential.html', {'form': form})
