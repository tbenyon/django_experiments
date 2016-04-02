from django.shortcuts import render
from .forms import contact_form

# Create your views here.


def contact_us(request):

    form = contact_form(request.POST or None)

    context = {
        'title': "Contact-us Form",
        'form': form
    }


    if form.is_valid():
        formData = form.cleaned_data
        for key, value in formData.items():
            print (key + ": " + str(value))

    return render(request, "home.html", context)