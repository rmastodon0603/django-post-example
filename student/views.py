from django.shortcuts import render


# Create your views here.
from student.models import Student


def index(request):
    context = {
        'students': Student.objects.all()
    }

    if request.method == "POST":
        print(request.POST.get('first_name', 'default'))
        Student.objects.create(first_name=request.POST.get('first_name', 'default'),
                               last_name=request.POST.get('last_name', 'default'),
                               phone=request.POST.get('phone', 'default'),
                               date_of_birth=request.POST.get('date_of_birth', 'default'))

    return render(request, 'form-student.html', context=context)
