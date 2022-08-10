from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#
# class RegisterS(generic.CreateView):
#     model = pass
