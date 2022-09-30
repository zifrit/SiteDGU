from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
from django.views import generic, View


#
# class RegisterS(generic.CreateView):
#     form_class = TestForm
#     template_name = 'Students/for_base/add_student.html'
#     success_url = '/'
class RegisterS(View):

    def get(self, request):
        form = AddNewStudent()
        return render(request, "Students/for_base/add_student.html", {'form': form, 'data': 'привет'})

    def post(self, request):
        form = AddNewStudent(request.POST, request.FILES)

        if form.is_valid():
            print('yes')
            print(form.cleaned_data)
            form.save()
        print('no')
        print(form.cleaned_data)
        error = [equals for _, one in form.errors.items() for equals in one]
        print(form.errors.items())
        form = AddNewStudent()
        return render(request, "Students/for_base/add_student.html", {'form': form, 'data': 'привет',
                                                                      'error': error})

    # def form_valid(self, form):
    #     form = form.save()
    #     return redirect('home')

# class RegisterS(View):
#     def get(self, request):
#         return render(request, 'Students/for_base/add_student.html', {})
