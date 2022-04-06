from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .form import NameForm


def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            send_mail(
                form.data['name'] + ' | ' + form.data['subject'],
                form.data['message'],
                form.data['email'],
                ['thibault.montel@gmail.com.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'contact/contact.html', {'form': form})

