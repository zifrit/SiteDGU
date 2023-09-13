from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
import logging
from .forms import *
from ExecutableCode.new_password import new_password
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

log = logging.getLogger('my_log')

menu = [{'student': [{'title': "Главная", 'url_name': 'list_events'},
                     {'title': "Добавить Мероприятие", 'url_name': 'create_events'},
                     {'title': "Личный кабинет", 'url_name': 'account'}],
         'teacher': [{'title': "Главная", 'url_name': 'list_events'},
                     {'title': "Добавить Мероприятие", 'url_name': 'create_events'},
                     {'title': "Список студентов ", 'url_name': 'list_students'},
                     {'title': "Добавить студента", 'url_name': 'type_reg_student'}],
         'birds': [{'title': "Главная", 'url_name': 'list_events'},
                   {'title': "Добавить Мероприятие", 'url_name': 'create_events'},
                   {'title': "Список студентов ", 'url_name': 'list_students'},
                   {'title': "Личный кабинет", 'url_name': 'account'}],
         }]


class BaseRegister(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = ['Students.add_customuser', 'Students.change_customuser', 'Students.view_customuser', ]
    form_class = FormBaseRegisterStudent
    template_name = 'Students/templates/add_student.html'

    def get_success_url(self):
        return reverse(
            'type_reg_student',
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg'] = False
        context['menu'] = menu
        return context

    def form_valid(self, form):
        group = Group.objects.get(name='Студент')
        new_user = CustomUser.objects.create_user(username=form.cleaned_data['last_name'], password=new_password(16),
                                                  first_name=form.cleaned_data['first_name'],
                                                  last_name=form.cleaned_data['last_name'],
                                                  middle_name=form.cleaned_data['middle_name'],
                                                  )
        new_user.groups.add(group)
        new_user.save()
        form.instance.student = new_user
        return super().form_valid(form)


class AdvancedRegisterStudent(BaseRegister):
    form_class = FormAdvancedRegisterStudent


class FullRegisterStudent(BaseRegister):
    form_class = FormFullRegisterStudent


class Login(LoginView):
    form_class = FormLogin_s
    template_name = 'Students/templates/login.html'

    def get_success_url(self):
        return reverse_lazy('list_events')


class Register(UserPassesTestMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'Students/templates/login.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('list_students')


def logout_system(request):
    logout(request)
    return redirect('login')


class ListStudent(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = ['Students.view_customuser']
    template_name = 'Students/templates/list_student.html'
    paginate_by = 5
    model = ProfileStudent
    context_object_name = 'model'

    def get_context_data(self, *, object_list=None, **kwargs):
        log.info('test')
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['pagination'] = True
        return context

    def get_queryset(self):
        return ProfileStudent.objects.select_related('student', 'student_status', 'organization_sector',
                                                     'direction')


class DetailStudent(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    permission_required = ['Students.view_customuser']
    model = ProfileStudent
    template_name = 'Students/templates/detail_student.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['edit'] = False
        return context


class EditStudent(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = ['Students.add_customuser', 'Students.change_customuser', ]
    model = ProfileStudent
    template_name = 'Students/templates/detail_student.html'
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
        first_name = self.request.POST['first_name']
        last_name = self.request.POST['last_name']
        middle_name = self.request.POST['middle_name']
        user = self.object.student
        user.first_name = first_name
        user.last_name = last_name
        user.middle_name = middle_name
        user.save()
        return super().form_valid(form)


class TypeRegisterStudent(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ['Students.add_customuser', ]

    def get(self, request):
        button = [('Базовая', 'base_register'), ('Расширенная', 'advanced_register'), ('Полная', 'full_register')]
        return render(request, 'Students/templates/add_student.html', {'but': button, 'reg': True, 'menu': menu})


class Account(LoginRequiredMixin, generic.TemplateView):
    template_name = 'Students/templates/student_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # model = ProfileStudent.objects.select_related('student', 'student_status',
        #                                               'organization_sector',
        #                                               'direction').get(student=self.request.user)
        model = self.request.user.profilestudent
        context['menu'] = menu
        context['account'] = model
        context['form'] = FormFullRegisterStudent(instance=model)
        return context


class Test(generic.TemplateView):
    template_name = 'Students/templates/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'ghbdtn'
        return context
