from django.views.generic import TemplateView
from .forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


class Top(TemplateView):
    template_name = 'top.html'

class Signup(TemplateView):
    def get(self, request):
        initial_dict = {'username': None}
        return render(request, 'users/signup.html', {'form': SignupForm(initial=initial_dict)})

    def post(self, request, *args, **kwargs):
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('top')
        return render(request, 'users/signup.html', {'form': form,})
