from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#@login_required
class HomePageView(LoginRequiredMixin,TemplateView):
    permission_clases=[IsAuthenticated]
    def get(self,request):
        try:
            return render(request,"index.html",{'titulo':'Bienvenida'})
        except (Exception) as error:
            return HttpResponse(error)