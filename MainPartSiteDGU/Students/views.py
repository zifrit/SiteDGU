from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
from django.views import generic, View

#
class RegisterS(generic.CreateView):
    form_class = AddNewStudent
    template_name = 'Students/for_base/add_student.html'
    context_object_name = 'aas'

# class RegisterS(View):
#     def get(self, request):
#         return render(request, 'Students/for_base/add_student.html', {})