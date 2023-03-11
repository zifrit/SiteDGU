from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

import logging
from .forms import *
from django.views import generic, View

# permission
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

log = logging.getLogger('my_log')

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


class BaseRegister(LoginRequiredMixin, generic.CreateView):
    form_class = FormBaseRegisterStudent
    template_name = 'Students/for_base/add_student.html'
    success_url = '/type_reg_student/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg'] = False
        context['menu'] = menu
        return context

    def form_valid(self, form):
        new_user = CustomUser.objects.create_user(username=form.cleaned_data['last_name'], password='Saider569')
        form.instance.student = new_user
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


# class ListStudent(LoginRequiredMixin, View):
#
#     # log.info('saaas')
#
#     def get(self, request):
#         log_message = {
#             'message': 'dssd',
#             'who': self.request.user
#         }
#         log.info(log_message)
#         model = ProfileStudent.objects.all().select_related('direction')
#         paginator = Paginator(model, 5)
#         page_number = request.GET.get('page')
#         page_ogj = paginator.get_page(page_number)
#         return render(request, "Students/for_base/list_student.html", {'model': page_ogj, 'menu': menu})
#
#     def post(self, request):
#         search = request.POST['FIO']
#         model = ProfileStudent.objects.filter(full_name__contains=search).select_related('direction')
#         paginator = Paginator(model, 5)
#         page_number = request.GET.get('page')
#         page_ogj = paginator.get_page(page_number)
#         return render(request, "Students/for_base/list_student.html", {'model': page_ogj, 'menu': menu})


class ListStudent(LoginRequiredMixin, generic.ListView):
    template_name = 'Students/for_base/list_student.html'
    paginate_by = 5
    model = ProfileStudent
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


# class DetailStudent(LoginRequiredMixin, View):
#
#     def get(self, request, pk):
#         model = ProfileStudent.objects.get(id=pk)
#         form = FormFullRegisterStudent(instance=model)
#         return render(request, 'Students/for_base/detail_student.html',
#                       {'form': form, 'student': model, 'menu': menu, 'pk': pk})


#
#     def post(self, request, pk):
#         model = ProfileStudent.objects.get(id=pk)
#         form = FormFullRegisterStudent(request.POST, request.FILES, instance=model)
#         if form.is_valid():
#             form.save()
#         return render(request, 'Students/for_base/detail_student.html',
#                       {'form': form, 'student': model, 'menu': menu, 'pk': pk})

class DetailStudent(LoginRequiredMixin, generic.DetailView):
    model = ProfileStudent
    template_name = 'Students/for_base/detail_student.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['edit'] = False
        return context


class EditStudent(LoginRequiredMixin, generic.UpdateView):
    model = ProfileStudent
    template_name = 'Students/for_base/detail_student.html'
    context_object_name = 'student'
    form_class = FormFullRegisterStudent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['edit'] = True
        return context

    def get_success_url(self):
        return reverse(
            'detail_student',
            kwargs={'pk': self.object.pk}
        )

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_form_class(self):
    #     # a = FormFullRegisterStudent(self.request, instance=self.object)
    #     # form = a.save(commit=False)
    #     # form.first_name = 'asdasd'
    #     # form.save()
    #     return FormFullRegisterStudent(instance=ProfileStudent.objects.first())


class TypeRegisterStudent(LoginRequiredMixin, View):

    def get(self, request):
        button = [('Базовая', 'base_register'), ('Расширенная', 'advanced_register'), ('Полная', 'full_register')]
        return render(request, 'Students/for_base/add_student.html', {'but': button, 'reg': True, 'menu': menu})


class CreateEvents(LoginRequiredMixin, generic.CreateView):
    form_class = FormCreateEvents
    template_name = 'Students/for_base/create_events.html'
    success_url = '/create_events/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# class ListEvents(LoginRequiredMixin, View):
#     login_url = 'login'
#
#     def get(self, request):
#         model = Events.objects.all()
#         paginator = Paginator(model, 3)
#         page_number = request.GET.get('page')
#         page_ogj = paginator.get_page(page_number)
#
#         return render(request, "Students/for_base/list_events.html", {'models': page_ogj, 'menu': menu, 'list': True})
#
#     def post(self, request):
#         search = request.POST['search_events']
#         model = Events.objects.filter(name__contains=search)
#         paginator = Paginator(model, 3)
#         page_number = request.GET.get('page')
#         page_ogj = paginator.get_page(page_number)
#
#         return render(request, "Students/for_base/list_events.html", {'models': page_ogj, 'menu': menu, 'list': True})


class ListEvents(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = ['Students.view_events']
    paginate_by = 5
    model = Events
    template_name = 'Students/for_base/list_events.html'
    context_object_name = 'models'

    def get_queryset(self):
        return Events.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


# class DetailEvent(LoginRequiredMixin, View):
#     login_url = 'login'
#
#     def get(self, request, pk):
#         model = Events.objects.get(id=pk)
#         form = FormCreateEvents(instance=model)
#         return render(request, 'Students/for_base/detail_events.html',
#                       {'form': form, 'events': model, 'menu': menu})
#
#     def post(self, request, pk):
#         model = Events.objects.get(id=pk)
#         form = FormCreateEvents(request.POST, request.FILES, instance=model)
#         if form.is_valid():
#             form.save()
#         return render(request, 'Students/for_base/detail_events.html',
#                       {'form': form, 'events': model, 'menu': menu})


class DetailEvent(LoginRequiredMixin, generic.DetailView):
    model = Events
    template_name = 'Students/for_base/detail_events.html'
    context_object_name = 'ditail_event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['edit'] = False
        return context


class EditEvent(LoginRequiredMixin, generic.UpdateView):
    model = Events
    form_class = FormCreateEvents
    template_name = 'Students/for_base/detail_events.html'
    context_object_name = 'ditail_event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse(
            'detail_events',
            kwargs={'pk': self.object.pk}
        )
