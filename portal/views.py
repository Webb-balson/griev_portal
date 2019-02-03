from django.shortcuts import render, get_object_or_404
from .models import Student
from .student import StudentForm
from .models import Parent
from .parent import ParentForm
from .models import Staff
from .staff import StaffForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.
def home(request):
    #post = get_object_or_404(Post, pk=pk)
    if request.user.is_superuser:
        return redirect("complain_list" , "student")
    else:
        return render(request, 'portal/home.html', {'home':home})


def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'portal/student.html', {'form': form})

def parent(request):
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            parent = form.save(commit=False)
            parent.save()
            return redirect('home')
    else:
        form = ParentForm()
    return render(request, 'portal/parent.html', {'form': form})

def staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.save()
            return redirect('home')
    else:
        form = StaffForm()
    return render(request, 'portal/staff.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def complain_list(request , complainer):
    if complainer=="student":
        students = Student.objects.all()
        return render(request, 'portal/complain_list.html', {'students':students , "counts": len(students)})
    elif complainer == "parent":
        parents = Parent.objects.all()
        return render(request, 'portal/complain_list.html', {'parents':parents , "counts": len(parents)})
    elif complainer == "staff":
        staffs = Staff.objects.all()
        return render(request, 'portal/complain_list.html', {'staffs':staffs , "counts": len(staffs)})

# @login_required
# @user_passes_test(lambda u: u.is_superuser)
# def complain_detail(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     return render(request, 'portal/complain_detail.html', {'student':student})
