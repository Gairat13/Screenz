from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.base import View

from video.models import Movie
from .forms import RegistrationForm

User = get_user_model()


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('successful-registration')


class SuccessfulRegistrationView(View):
    def get(self, request):
        return render(request, 'account/successful_registration.html')


class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html')


class SigninView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')


class DetailUserView(DetailView):
    model = User
    template_name = 'video/includes/base.html'
    context_object_name = 'user'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = kwargs.get('pk', None)
        # self.user2 = request.user
        if user != request.user.pk:
            raise Http404
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['favorites'] = self.request.user.movies.all()
        print(self.request.user)
        return context





