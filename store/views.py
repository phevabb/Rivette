from django.shortcuts import render, redirect
from .forms import GeneralInfoForm
from .models import GeneralInfo
import uuid

# Create your views here.
def index(request):

    form = GeneralInfoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        info=form.save(commit=False)
        info.token_number = str(uuid.uuid4())
        info.save()

        return redirect('store:payment', token_number=info.token_number)  # Redirect or render a success page

    return render(request, 'index.html', {'form': form})


def payment(request, token_number):
    obj = GeneralInfo.objects.get(token_number=token_number)
    return render(request, 'payments.html', context={'obj': obj})