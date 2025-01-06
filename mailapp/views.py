from django.shortcuts import render, redirect
from .forms import FutureMailForm
# Create your views here.


def index(request):
    return render(request, 'mailapp/index.html')


def mailform(request):
    if request.method == "POST":
        form = FutureMailForm(request.POST)
        if form.is_valid():
            # print(form)
            form.save()
            return redirect('mailapp-index')  # Redirect after saving
    else:
        form = FutureMailForm()
    return render(request, 'mailapp/mailform.html', {'form': form})
