from django.shortcuts import render

from app.function import *
# Create your views here.


def home(request):
    get_banner = get_banners({'status':True})
    get_text = get_texts({'status':True})
    get_quality = get_qualities({'status':True})
    get_about = get_abouts({'status':True})
    get_something_service = get_something_services({'status':True})
    get_ask_services = get_ask_service({'status':True})
    context = {
        'get_banner': get_banner,
        'get_text': get_text,
        'get_quality': get_quality,
        'get_about': get_about,
        'get_something_service': get_something_service,
        'get_ask_services': get_ask_services,
    }
    return render(request, 'app/index.html', context)


def service(request):
    get_something_service = get_services({'status':True})

    context = {
        'get_something_service': get_something_service,
        'is_active': True,
    }
    return render(request, 'app/service.html', context)


def under_service(request):
    get_under_services = get_under_service({'status':True})
    context = {
        'get_under_services': get_under_services,
        'is_active': True,
    }
    return render(request, 'app/under-service.html', context)
