from django.shortcuts import render, redirect
from .controller import ViewController
from .forms import ImportExelForm
import time

# Create your views here.
def main(request):
    return render(request, 'graduate_report/main.html')

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