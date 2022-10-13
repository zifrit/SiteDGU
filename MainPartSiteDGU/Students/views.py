from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView

from .models import *
from .forms import *
from django.views import generic, View

# permission
from django.contrib.auth.mixins import LoginRequiredMixin

menu = [{'student': [{'title': "Главная", 'url_name': 'main'}],
         'teacher': [{'title': "Главная", 'url_name': 'main'},
                     {'title': "Список студентов ", 'url_name': 'main'},
                     {'title': "Добавить студента", 'url_name': 'type_reg_student'}],
         'birds': [{'title': "Главная", 'url_name': 'main'},
                   {'title': "Список студентов ", 'url_name': 'main'}],
         }]


#
class BaseRegister(LoginRequiredMixin, generic.CreateView):
    login_url = 'login'
    form_class = FormBaseRegisterStudent
    template_name = 'Students/for_base/add_student.html'
    success_url = '/type_reg_student/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg'] = False
        context['menu'] = menu
        return context


class AdvancedRegisterStudent(BaseRegister):
    form_class = FormAdvancedRegisterStudent


class FullRegisterStudent(BaseRegister):
    form_class = FormFullRegisterStudent


class Login(LoginView):
    form_class = FormLogin_s
    template_name = 'Students/for_base/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'Students/for_base/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def logout_system(request):
    logout(request)
    return redirect('login')


class Main(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        model = InfoStudent.objects.all()
        paginator = Paginator(model, 5)
        page_number = request.GET.get('page')
        page_ogj = paginator.get_page(page_number)
        return render(request, "Students/for_base/main_site.html", {'model': page_ogj, 'menu': menu})


# class DetailStudent(LoginRequiredMixin, DetailView):
#     login_url = 'login'
#     model = InfoStudent
#     template_name = 'Students/for_base/detail_student.html'
#     context_object_name = 'student'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         return context


class DetailStudent(LoginRequiredMixin, View):

    def get(self, request, pk):
        model = InfoStudent.objects.get(id=pk)
        form = FormFullRegisterStudent(instance=model)
        return render(request, 'Students/for_base/detail_student.html',
                      {'form': form, 'student': model, 'menu': menu, 'pk': pk})

    def post(self, request, pk):
        model = InfoStudent.objects.get(id=pk)
        form = FormFullRegisterStudent(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
        return render(request, 'Students/for_base/detail_student.html',
                      {'form': form, 'student': model, 'menu': menu, 'pk': pk})


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

class TypeRegisterStudent(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        but = [('Базовая', 'base_register'), ('Расширенная', 'advanced_register'), ('Полная', 'full_register')]
        return render(request, 'Students/for_base/add_student.html', {'but': but, 'reg': True, 'menu': menu})
