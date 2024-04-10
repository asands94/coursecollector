from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Course, Category
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('courses_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class CourseList(LoginRequiredMixin,ListView):
    model = Course

class CourseDetail(LoginRequiredMixin,DetailView):
    model = Course

class CourseCreate(LoginRequiredMixin,CreateView):
    model = Course
    fields = ['image', 'name', 'description', 'price', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CourseUpdate(LoginRequiredMixin,UpdateView):
    model = Course
    fields = ['image', 'name', 'description', 'price']

class CourseDelete(LoginRequiredMixin,DeleteView):
    model = Course
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse-lazy
    success_url = reverse_lazy('course_index')

class CategoryList(LoginRequiredMixin,ListView):
    model = Category

class CategoryCreate(LoginRequiredMixin,CreateView):
    model = Category
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryUpdate(LoginRequiredMixin,UpdateView):
    model = Category
    fields = ['name']

class CategoryDelete(LoginRequiredMixin,DeleteView):
    model = Category
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse-lazy
    success_url = reverse_lazy('category_index')

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

            