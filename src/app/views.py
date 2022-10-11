
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
import json

from jamoh import settings
from app.models import *
from app.function import *
# Create your views here.

def verify_email(email):
    try:
        validate_email(email)
        return False
    except ValidationError:
        return True

def home(request):
  get_banner = get_banners({'status':True})
  get_text = get_texts({'status':True})
  get_quality = get_qualities({'status':True})
  get_about = get_abouts({'status':True})
  get_something_service = get_something_services({'status':True})
  get_ask_services = get_ask_service({'status':True})
  get_under_services = get_under_service({'status':True})
  context = {
      'page':{
        'title': 'De-missa | Bienvenue',
        'text_title': 'De quel service avez-vous besoins ?',
        'text_description': 'Pour chaque situation, trouvez le prestataire dont les compétences répondent à vos attentes et à votre niveau d’exigence.',
        
      },
      'get_banner': get_banner,
      'get_text': get_text,
      'get_quality': get_quality,
      'get_about': get_about,
      'get_something_service': get_something_service,
      'get_ask_services': get_ask_services,
      'get_under_services': get_under_services,
  }
  return render(request, 'app/index.html', context)


def service(request):
  get_something_service = get_services({'status':True})

  context = {
      'page':{
        'title': 'De-missa | Service',
        'text_title': ' Tous nos services ?',
        'text_description': '',
      },
      'get_something_service': get_something_service,
      'is_true': True,
  }

  return render(request, 'app/service.html', context)


def under_service(request, id):
  get_related_services =  get_related_service(id)
  cartogory = SousService.service
  #get_all_related_services = get_all_related_service({'service':cartogory})
  get_under_services = get_under_service({'status':True})
  get_about = get_abouts({'status':True})
  context = {
      'page':{
        'title': 'De-missa | Service',
        
      },
      'get_about': get_about,
      'get_under_services': get_under_services,
      'get_related_services' : get_related_services,
      #'get_all_related_services': get_all_related_services,
      'is_active': True,
  }
 
  return render(request, 'app/under-service.html', context)


def payment(request):
  get_banner = get_banners({'status':True})
  is_active_pay = True
  return render(request, 'app/payment.html', locals())


@csrf_exempt
def postData(request):


  all_is_true = False
  msg = ''
  
  name = request.POST.get('name')
  email = request.POST.get('email')
  address = request.POST.get('address')
  phone = request.POST.get('phone')

          
  if not name or name.isspace():
    msg = 'Veuillez entrer un nom valide'
  elif not email or email.isspace():
    msg = 'Veuillez entrer un email'
  elif not phone or phone.isspace():
    msg = 'Veuillez entrer un phone valide'
  else:
    all_is_true, msg = True, 'Enregistrement effectué'
  
  subject = "Bienvenue chez DE-MISSA"
  message = f"Bienvenue M. {name}  \nMerci de contacter DE-MISSA\n\n\npour tous vos services a domicile"
  from_email = settings.EMAIL_HOST_USER
  print("###############  1  #####################")
  to_list = [email]
  print("###############  2  #####################")         
  send_mail(subject, message, from_email, to_list, fail_silently=False)
  print("###############  3  #####################")
          
   
  
  data = {
    'success': all_is_true,
    'msg': msg
  }
  return JsonResponse(data,safe=False)