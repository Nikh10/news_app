from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, News
from .services import populate_data

@login_required(login_url='/login')
def home_view(request):
	queryset = News.objects.all()
	context = {
		'newss': queryset
	}
	return render(request, 'nknews_app/home.html', context)

def details_view(request, id):
    query = News.objects.get(pk=id)
    context = {
        'newss': query
    }

    return render(request, 'nknews_app/details.html', context)
    
# @login_required(login_url='/login')
def index_view(request):
    result = populate_data()
    listvar = []
    data = result['articles']
    for i in range(20):
        listvar.append(data[i])

    context = {
        'listvar':listvar,
        }
    return render(request,'nknews_app/index.html',context)


###########################
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

def login_view(request):    
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/nknews_app')
        else:
            context = {'error': 'Invalid username/password'}
            return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login')  


def register_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    elif  request.method == 'POST':
        first_name = request.POST.get("first name")
        last_name = request.POST.get("last name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user = authenticate(first_name=first_name, last_name=last_name,email=email,password1=password1,password2=password2)
        print(user)
        if user is not None:
            user.save()
            return redirect('/nknews_app')
        else:
            context = {'error': 'Invalid Account '}
 
    return render(request, 'accounts/register.html',context)

    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # user.save()