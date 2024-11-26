from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

class SmartLiteLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class SmartLiteLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirige al login tras hacer logout

class SmartLiteLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, "Has iniciado sesión exitosamente.")
        return super().form_valid(form)

class SmartLiteLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Has cerrado sesión.")
        return super().dispatch(request, *args, **kwargs)