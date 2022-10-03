from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.views import generic, View


#
class Register(generic.CreateView):
    form_class = AddNewStudent
    template_name = 'Students/for_base/add_student.html'
    success_url = '/student/regist-student/'


class Login(LoginView):
    form_class = Login_s
    template_name = 'Students/for_base/login.html'
    success_url = '/student/regist-student/'

    def get_success_url(self):
        return reverse_lazy('register')


def logout_system(request):
    logout(request)
    return redirect('login')


class Main(View):
    def get(self, request):
        model = InfoStudent.objects.all()
        paginator = Paginator(model, 3)
        page_number = request.GET.get('page')
        page_ogj = paginator.get_page(page_number)
        return render(request, "Students/for_base/main_site.html", {'model': page_ogj, 'page_ogj': page_ogj})
#
# class RegisterS(View) :
#
#     def get(self, request):
#         form = AddNewStudent()
#         return render(request, "Students/for_base/add_student.html", {'form': form, 'data': 'привет'})
#
#     def post(self, request):
#         form = AddNewStudent(request.POST, request.FILES)
#
#         if form.is_valid():
#             print('yes')
#             print(form.cleaned_data)
#             form.save()
#         print('no')
#         print(form.cleaned_data)
#         error = [equals for _, one in form.errors.items() for equals in one]
#         print(form.errors.items())
#         form = AddNewStudent()
#         return render(request, "Students/for_base/add_student.html", {'form': form, 'data': 'привет',
#                                                                       'error': error})

# def form_valid(self, form):
#     form = form.save()
#     return redirect('home')

# class RegisterS(View):
#     def get(self, request):
#         return render(request, 'Students/for_base/add_student.html', {})
