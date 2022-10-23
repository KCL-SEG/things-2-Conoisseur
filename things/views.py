from django.shortcuts import render
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data.get("submit_button")
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
