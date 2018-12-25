from django.shortcuts import render
from .models import Category, News
from .services import populate_data

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