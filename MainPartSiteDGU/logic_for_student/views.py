from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
import logging
from .forms import *
# permission
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

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


class CreateEvents(LoginRequiredMixin, generic.CreateView):
    form_class = FormCreateEvents
    template_name = 'logic_for_student/templates/create_events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_events')


class ListEvents(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = ['Students.view_events']
    paginate_by = 5
    model = Events
    template_name = 'logic_for_student/templates/list_events.html'
    context_object_name = 'models'

    def get_queryset(self):
        return Events.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class DetailEvent(LoginRequiredMixin, generic.DetailView):
    model = Events
    template_name = 'logic_for_student/templates/detail_events.html'
    context_object_name = 'ditail_event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['edit'] = False
        return context


class EditEvent(LoginRequiredMixin, generic.UpdateView):
    model = Events
    form_class = FormCreateEvents
    template_name = 'logic_for_student/templates/detail_events.html'
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
