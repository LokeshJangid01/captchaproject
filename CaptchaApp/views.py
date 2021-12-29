from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .form import CaptchaForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
            messages.success(request,"Captcha varified successfully")
        else:
            messages.error(request,"Wrong Captcha")  

    form = CaptchaForm()
    return render(request,"index.html",{"form":form})

