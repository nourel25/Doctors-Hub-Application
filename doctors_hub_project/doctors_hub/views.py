from django.shortcuts import render, redirect
from .models import Specialization, Area, Doctor
from django.views.generic import DetailView, ListView
# Create your views here.

def home(request):
    context = {
        'specializations': Specialization.objects.all(),
        'areas': Area.objects.all(),
        'doctors': Doctor.objects.all()
    }
    
    return render(request, 'doctors_hub/home.html', context)

def doctor_search(request):

    if request.method == 'GET':
        specialization_id = request.GET.get('specialization')
        area_id = request.GET.get('area')

        doctors = Doctor.objects.all()
        if specialization_id:
            doctors = doctors.filter(specialization__id=specialization_id)
        if area_id:
            doctors = doctors.filter(area__id=area_id)

        print(specialization_id)
        print(area_id)

    context = {'doctors': doctors }
    
    return render(request, 'doctors_hub/doctors_search_results.html', context)
