from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Course

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class CourseList(ListView):
    model = Course

class CourseDetail(DetailView):
    model = Course

class CourseCreate(CreateView):
    model = Course
    fields = ['image', 'name', 'description', 'price']

class CourseUpdate(UpdateView):
    model = Course
    fields = ['image', 'name', 'description', 'price']

class CourseDelete(DeleteView):
    model = Course
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse-lazy
    success_url = reverse_lazy('course_index')

# class CourseCreate(CreateView):
#     def add_image(request):
#         us=Course.objects.get(roll_no=user)
#         if request.method == 'POST' and request.FILES['myfile'];
#             myfile = request.FILES['myfile']
#             fs = FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             uploaded_file_url = fs.url(filename)
#             us.img_link=uploaded_file_url
#             us.save()
#             print(uploaded_file_url)

            