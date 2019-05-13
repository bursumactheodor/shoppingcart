
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm


def index(request):
    if request.method == 'POST':
        loc=request.POST['localitate']
        obiecte = Student.objects.all().filter(localitate=loc).order_by('id')
        return render(request, "student/index.html", {'lst': obiecte})
    else:
        obiecte = Student.objects.all().order_by('id')
        return render(request, "student/index.html", {'lst': obiecte})



def adauga1(request):
     #obiecte = Student.objects.all()
     #return render(request, "student/adauga1.html")
     return render(request, "student/index.html", {'nume1':request.POST['nume'],'telefon1':request.POST['telefon'],'bursa1':request.POST['bursa'],'localitate1':request.POST['localitate'],'adauga1':request.POST['adauga']})



def adauga(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            stud = Student()
            #xxxx = request.POST['nume']

            stud.nume = cd['nume']
            stud.telefon = cd['telefon']
            stud.bursa = cd['bursa']
            stud.localitate = cd['localitate']
            stud.save()
            #form = StudentForm()
            return redirect("/student")
        else:
            print("Form is not valid")
    else:
        form = StudentForm()

    return render(request, 'student/adauga.html', {'form': form})



def sterge(request,ids):
    Student.objects.all().filter(id=ids).delete()
    return redirect("/student")



def modifica(request,ids):
    #stud=Student.objects.all().filter(id=ids)
    stud = Student.objects.get(id=ids)

    #stud = Student(id=10,nume="doru",telefon='0726 70 95 76',bursa=1000,localitate="Bucuresti")

    if request.method == 'POST':
        stud = Student()
        stud.id=int(ids)
        stud.nume = request.POST['nume']
        stud.telefon = request.POST['telefon']
        stud.bursa = request.POST['bursa']
        stud.localitate = request.POST['localitate']
        stud.save()
        return redirect("/student")
    else:
        return render(request, 'student/modifica1.html', {'ms': "test", 'stud': stud})