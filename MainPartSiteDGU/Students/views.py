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

menu = [{'student': [{'title': "Главная", 'url_name': 'list_events'},
                     {'title': "Добавить Мероприятие", 'url_name': 'create_events'}],
         'teacher': [{'title': "Главная", 'url_name': 'list_events'},
                     {'title': "Добавить Мероприятие", 'url_name': 'create_events'},
                     {'title': "Список студентов ", 'url_name': 'list_students'},
                     {'title': "Добавить студента", 'url_name': 'type_reg_student'}],
         'birds': [{'title': "Главная", 'url_name': 'list_events'},
                   {'title': "Добавить Мероприятие", 'url_name': 'create_events'},
                   {'title': "Список студентов ", 'url_name': 'list_students'}],
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

    def form_valid(self, form):
        form.instance.full_name = f'{form.cleaned_data["surname"]} {form.cleaned_data["name"]} ' \
                                  f'{form.cleaned_data["middle_name"]}'
        return super().form_valid(form)


class AdvancedRegisterStudent(BaseRegister):
    form_class = FormAdvancedRegisterStudent


class FullRegisterStudent(BaseRegister):
    form_class = FormFullRegisterStudent


class Login(LoginView):
    form_class = FormLogin_s
    template_name = 'Students/for_base/login.html'

    def get_success_url(self):
        return reverse_lazy('list_students')


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'Students/for_base/login.html'

    def get_success_url(self):
        return reverse_lazy('list_students')


def logout_system(request):
    logout(request)
    return redirect('login')


class ListStudent(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        model = InfoStudent.objects.all().select_related('direction')
        paginator = Paginator(model, 5)
        page_number = request.GET.get('page')
        page_ogj = paginator.get_page(page_number)
        return render(request, "Students/for_base/main_site.html", {'model': page_ogj, 'menu': menu})

    def post(self, request):
        search = request.POST['FIO']
        model = InfoStudent.objects.filter(full_name__contains=search).select_related('direction')
        paginator = Paginator(model, 5)
        page_number = request.GET.get('page')
        page_ogj = paginator.get_page(page_number)
        return render(request, "Students/for_base/main_site.html", {'model': page_ogj, 'menu': menu})


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


class TypeRegisterStudent(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        but = [('Базовая', 'base_register'), ('Расширенная', 'advanced_register'), ('Полная', 'full_register')]
        return render(request, 'Students/for_base/add_student.html', {'but': but, 'reg': True, 'menu': menu})


class CreateEvents(LoginRequiredMixin, generic.CreateView):
    login_url = 'login'
    form_class = FormCreateEvents
    template_name = 'Students/for_base/create_events.html'
    success_url = '/create_events/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['list'] = False
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListEvents(LoginRequiredMixin, View):
    def get(self, request):
        model = Events.objects.all()
        paginator = Paginator(model, 5)
        page_number = request.GET.get('page')
        page_ogj = paginator.get_page(page_number)

        return render(request, "Students/for_base/create_events.html", {'models': page_ogj, 'menu': menu, 'list': True})

    def post(self, request):
        search = request.POST['events']
        model = Events.objects.filter(name__contains=search)
        paginator = Paginator(model, 5)
        page_number = request.GET.get('page')
        page_ogj = paginator.get_page(page_number)

        return render(request, "Students/for_base/create_events.html", {'models': page_ogj, 'menu': menu, 'list': True})


class DetailEvent(LoginRequiredMixin, View):

    def get(self, request, pk):
        model = Events.objects.get(id=pk)
        form = FormCreateEvents(instance=model)
        return render(request, 'Students/for_base/detail_events.html',
                      {'form': form, 'events': model, 'menu': menu, 'pk': pk})

    def post(self, request, pk):
        model = Events.objects.get(id=pk)
        form = FormCreateEvents(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
        return render(request, 'Students/for_base/detail_events.html',
                      {'form': form, 'events': model, 'menu': menu, 'pk': pk})
