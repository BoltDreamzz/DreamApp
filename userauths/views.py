
from django.contrib.auth import logout as v_logout

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignupForm, LoginForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, '{user}'")
            return redirect("shop:index")

    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "userauths/login.html", context)


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Welcome!")
#                 # Redirect to a success page
#                 return redirect('shop:index')
#             else:
#                 # Return an 'invalid login' error message.
#                 return render(request, 'userauths/login.html', {'form': form, 'error': 'Invalid username or password'})
#     else:
#         form = LoginForm()
#     return render(request, 'userauths/login.html', {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Registered as '{username}'. Now log in.")
            return redirect("userauths:login")
    else:
        form = SignupForm()
    return render(request, "userauths/signup.html", {
        "form": form,
    })


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, f"Welcome {username}")
#             # Redirect to a success page
#             return redirect('shop:index')
#     else:
#         form = SignupForm()
#     return render(request, 'userauths/signup.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Welcome!")
#             # Redirect to a success page
#             return redirect('shop:index')
#         else:
#             # Return an 'invalid login' error message.
#             return render(request, 'userauths/login.html', {'error': 'Invalid username or password'})
#     return render(request, 'userauths/login.html')
#
#
# # You can similarly implement a signup view
#
#
# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         # Create the user
#         user = User.objects.create_user(username=username, email=email, password=password)
#         if user is not None:
#             # Login the user after signup
#             login(request, user)
#             messages.success(request, f"Welcome {username}")
#             # Redirect to a success page
#             return redirect('shop:index')
#         else:
#             messages.debug(request, "An error occurred, retry")
#             # Return an error message if signup fails
#             return render(request, 'userauths/signup.html', {'error': 'Signup failed. Please try again.'})
#     return render(request, 'userauths/signup.html')
#

def logout(request):
    v_logout(request)
    messages.warning(request, "Logged out.")
    return redirect("shop:index")
