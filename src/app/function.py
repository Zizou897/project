from app.models import *


# Pour la page d'accueil (home) ------------------------------------------------

def get_banners(data=dict()):
    return Banner.objects.filter(**data).first()


def get_texts(data=dict()):
    return Text.objects.filter(**data).first()


def get_qualities(data=dict()):
    return Quality.objects.filter(**data)


def get_abouts(data=dict()):
    return About.objects.filter(**data).first()


def get_something_services(data=dict()):
    return Service.objects.filter(**data).order_by('order')[:9]

def get_ask_service(data=dict()):
    return AskService.objects.filter(**data).order_by('order')

#------------------------------------------------------------------------------------


# Pour la page des services (service) ------------------------------------------------

def get_services(data=dict()):
    return Service.objects.filter(**data).order_by('order')

#------------------------------------------------------------------------------------


# Pour la page des sous-services (service) ------------------------------------------------

def get_under_service(data=dict()):
    return SousService.objects.filter(**data).order_by('order')
