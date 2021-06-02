from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView, CreateView
from .forms import SignupForm, LoginForm, UserUpdateForm, MemoryCreateForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .models import User, Memory
from django.urls import reverse_lazy


#ページのpkとログインされたpkが一致しないと403エラーが発生する。
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class Top(ListView):
    template_name = 'top.html'
    model = Memory

    def get_queryset(self):
        object_list = Memory.objects.select_related().order_by('id')[:5]
        return object_list



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

class MemoryCreate(CreateView):
    template_name = 'memories/create.html'
    form_class = MemoryCreateForm
    success_url = reverse_lazy('top')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MemoryDetail(DetailView):
    template_name = 'memories/detail.html'
    model = Memory
