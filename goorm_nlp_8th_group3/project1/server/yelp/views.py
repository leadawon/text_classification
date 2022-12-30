from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        
    }
    return render(request, 'yelp/index.html', context)


def about(request):
    return render(request, 'yelp/about.html')


def contact(request):
    return render(request, 'yelp/contact.html')


def method(request):
    return render(request, 'yelp/method.html')


def method_details(request):
    return render(request, 'yelp/method-details.html')


def resume(request):
    return render(request, 'yelp/resume.html')


def services(request):
    return render(request, 'yelp/services.html')