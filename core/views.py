from django.shortcuts import render, HttpResponse

# Create your views here.

from .tasks import wait


def wait_view(request):
    wait.delay()
    return HttpResponse('')
