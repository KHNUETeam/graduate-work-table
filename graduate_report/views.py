from django.shortcuts import render, redirect
from .controller import ViewController
from .forms import ImportExelForm, SearchForm
from .models import Student
import time
import re

# Create your views here.
def main(request):
    students = Student.objects.filter(theme__icontains="структур")

    if request.method == 'POST':
        if 'search' in request.POST:
            search = True
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            data = search_form.cleaned_data
            print(data)

            students = Student.objects.filter(deleted=0)

            if data['start']:
                students = students.filter(protection_date=data['start'])

            if data['end']:
                students = students.filter(protection_date=data['end'])

            if data['phrases'] != '':
                phrases = re.split(r'\s*,\s*', data['phrases'])
                for phrase in phrases:
                    students = students.filter(theme__icontains=phrase)
    else:
        search_form = SearchForm()
        students = Student.objects.filter(deleted=0)

    return render(request, 'graduate_report/main.html', locals())

def load(request):
    view_controller = ViewController()

    if request.method == 'POST':
        send_form = ImportExelForm(request.POST, request.FILES)
        if send_form.is_valid():
            status = view_controller.handle_file(request.FILES['file'])
            if status:
                view_controller.get()
            time.sleep(3)
            return redirect('/')
    else:
        send_form = ImportExelForm()

    return render(request, 'graduate_report/load.html', locals())