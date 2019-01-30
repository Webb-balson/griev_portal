from django.shortcuts import render, get_object_or_404
from .models import Student
from .student import StudentForm
from django.shortcuts import redirect


# Create your views here.
def home(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'portal/home.html', {'home':home})

def student(request):
    form = StudentForm()
    return render(request, 'portal/student.html', {'form':form})

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

def complain_list(request, pk):
    student = get_object_or_404(Student)
    return render(request, 'portal/complain_list.html', {'student':student})

def complain_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'portal/complain_detail.html', {'student':student})
