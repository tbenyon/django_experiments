from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def home(request):
    user = str(request.user)
    if user == "AnonymousUser":
        userStatus = "No user logged in."
    else:
        userStatus = "User logged in as " + user + '.'

    form = SignUpForm(request.POST or None) #If there's post data send it through this form, if not don't do validation


    context = {
            'title': "Benyon's Django App!",
            'userStatus': userStatus,
            'form': form
            }

    if form.is_valid():
        instance = form.save(commit = False)
        if not instance.full_name:
            instance.full_name = "Barry"
        instance.save()
        print(instance)
        print(instance.email)
        print(instance.timestamp)
        context['title'] = "Thank you!!!"
        context['form'] = ""


    return render(request, "home.html", context)