from django.shortcuts import render, get_object_or_404
from .models import Student
from .student import StudentForm
from .models import Parent
from .parent import ParentForm
from .models import Staff
from .staff import StaffForm
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def home(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'portal/home.html', {'home':home})


def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('complain_detail',pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'portal/student.html', {'form': form})

def parent(request):
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            parent = form.save(commit=False)
            parent.save()
            return redirect('complain_detail',pk=parent.pk)
    else:
        form = ParentForm()
    return render(request, 'portal/parent.html', {'form': form})

def staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.save()
            return redirect('complain_detail',pk=staff.pk)
    else:
        form = StaffForm()
    return render(request, 'portal/staff.html', {'form': form})

def complain_list(request):
    students = Student.objects.all()
    return render(request, 'portal/complain_list.html', {'students':students})

def complain_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'portal/complain_detail.html', {'student':student})
