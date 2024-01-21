from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.http import JsonResponse

# Create your views here.
def home(request):
    form = StudentForm()
    stud = Student.objects.all()
    return render(request, 'home.html', {'form':form, 'stud':stud})

def save_data(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            sem = request.POST['sem']
            branch = request.POST['branch']

            usr = Student(name=name, sem=sem, branch= branch)
            usr.save()
            stud_data = Student.objects.values()
            stud_data = list(stud_data)
            return JsonResponse({'status': 'Save', 'stud_data':stud_data})
        else:
            return JsonResponse({'status': 0})
        
def delete_data(request):
    if request.method == 'POST':
        id = request.POST['sid']
        pi = Student.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
        
def edit_data(request):
    if request.method == 'POST':
        id = request.POST['sid']
        usr = Student.objects.get(pk=id)
        usr_data = {'id': usr.id, 'name': usr.name, 'sem': usr.sem, 'branch': usr.branch}

        return JsonResponse(usr_data)





        
