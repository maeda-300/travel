from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView
from .forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

#ページのpkとログインされたpkが一致しないと403エラーが発生する。
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

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

class Login(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm

class Logout(LogoutView):
    pass

class Mypage(DetailView):
    template_name = 'users/mypage.html'
    model = User

class UserUpdate(UpdateView):
    template_name = 'users/update.html'
    form_class = UserUpdateForm
    model = User
    success_url = reverse_lazy('top')

class UserDelete(DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('top')
