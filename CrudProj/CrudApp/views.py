from django.shortcuts import render, redirect
from .form import StudentForm
from django.views import View
from .models import StudentModel

class Home(View):
    def get(self, request):
        student_data = StudentModel.objects.all()
        return render(request, 'base/home.html', {'student_data': student_data})

class Add_Student_Data(View):
    def get(self, request):
        form = StudentForm()
        return render(request, "base/add_student.html", {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'base/add_student.html', {'form': form})

class Delete(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studentdata = StudentModel.objects.get(id=id)
        studentdata.delete()
        return redirect('home')

class EditStudent(View):
    def get(self, request, id):
        studentdata = StudentModel.objects.get(id=id)
        form = StudentForm(instance=studentdata)
        return render(request, 'base/edit-student.html', {'form': form})

    def post(self, request, id):
        studentdata = StudentModel.objects.get(id=id)
        form = StudentForm(request.POST, instance=studentdata)
        if form.is_valid():
            form.save()
            return redirect('home')
