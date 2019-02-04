from django.shortcuts import render, redirect
from django.db.models import Q
from .controller import ViewController
from .forms import ImportExelForm, SearchForm
from .models import Student, VernLib
import time
import re
from .wordendslib import WORD_ENDS


# Create your views here.
def main(request, preview=None):
    if request.method == 'POST':
        queries = []
        if 'search' in request.POST:
            search = True
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            data = search_form.cleaned_data

            students = Student.objects.filter(deleted=0).filter(~Q(theme=''))
            vern_lib = VernLib.objects.filter(~Q(theme=''))

            if data['start']:
                students = students.filter(protection_date__gte=data['start'])

            if data['end']:
                students = students.filter(protection_date__lte=data['end'])

            if data['phrases'] != '':
                phrases = re.split(r'\s', data['phrases'])
                keys = []

                for phrase in phrases:
                    for word in WORD_ENDS:
                        if len(phrase) - len(word) > 2:
                            result = re.sub(r'{}'.format(word), '', phrase)
                            if len(result) < len(phrase):
                                keys.append(result)
                                break

                for key in keys:
                    students = students.filter(theme__icontains=key)
                    vern_lib = vern_lib.filter(theme_icontains=key)

        students = students.order_by('protection_date', 'theme')
        vern_lib = vern_lib.order_by('theme')
    else:
        search_form = SearchForm()

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