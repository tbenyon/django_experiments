from django.core.mail import send_mail
from django.conf import settings
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

        send_mail('Contact-us request from ' + formData.get('name', 'ANON'),
            formData.get('comments','No comment?!'),
            formData.get('email'),
            [settings.EMAIL_HOST_USER],
            fail_silently=False)

        for key, value in formData.items():
            print (key + ": " + str(value))

    return render(request, "home.html", context)