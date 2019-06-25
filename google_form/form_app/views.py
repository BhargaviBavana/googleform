from django.shortcuts import render
from django.views import View
from django.shortcuts import render,redirect

from form_app.forms import *
from form_app.models import *

# Create your views here.

class GoogleForm(View):
    def get(self,request,*args,**kwargs):
        google_form=Gform()
        return render(
            request,
            template_name="googleform.html",
            context={'google_form':google_form}
        )
    def post(self,request,*args,**kwargs):
        google_form = Gform(request.POST)
        if google_form.is_valid():
            details = Details(**google_form.cleaned_data)
            details.save()
        else:
            return redirect('google_form')
        return render(
            request,
            template_name="response.html",
            context={}
        )
