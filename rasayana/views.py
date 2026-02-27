from django.shortcuts import render, redirect
from .models import ContactMessage
from .models import Appointment

def home(request):
    return render(request, 'rasayana/home.html')

def about(request):
    return render(request, 'rasayana/about.html')

def contact(request):
    return render(request, 'rasayana/contact.html')

def gallery(request):
    return render(request, 'rasayana/gallery.html')

def team(request):
    return render(request, 'rasayana/our_team.html')

def book_consultation(request):
    return render(request, 'rasayana/bookconsultation.html')

def message_submit(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message'),
        )
        return render(request, 'rasayana/message_submit.html')

    return redirect('contact')

def confirmation(request):
    if request.method == "POST":
        Appointment.objects.create(
            patient_name=request.POST.get('patient_name'),
            age=request.POST.get('age'),
            specialist=request.POST.get('specialist'),
            preferred_date=request.POST.get('preferred_date'),
            phone=request.POST.get('phone'),
            concerns=request.POST.get('concerns'),
        )
        return redirect('confirmation')

    return render(request, 'rasayana/confirmation.html')
