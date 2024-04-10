from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Course, Category, Goal, User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GoalForm

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
      return redirect('course_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class CourseList(LoginRequiredMixin,ListView):
    model = Course
    template_name = 'course/course_list.html'

class CourseDetail(LoginRequiredMixin,DetailView):
    model = Course
    template_name = 'course/course_detail.html'

class CourseCreate(LoginRequiredMixin,CreateView):
    model = Course
    template_name = 'course/course_form.html'
    fields = ['image', 'name', 'url', 'description', 'price', 'recurring_fee', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CourseUpdate(LoginRequiredMixin,UpdateView):
    model = Course
    template_name = 'course/course_form.html'
    fields = ['image', 'name', 'url', 'description', 'price', 'recurring_fee', 'rating']

class CourseDelete(LoginRequiredMixin,DeleteView):
    model = Course
    template_name = 'course/course_confirm_delete.html'
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse-lazy
    success_url = reverse_lazy('course_index')

class CategoryList(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'category/category_list.html'

class CategoryCreate(LoginRequiredMixin,CreateView):
    model = Category
    template_name = 'category/category_form.html'
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryUpdate(LoginRequiredMixin,UpdateView):
    model = Category
    template_name = 'category/category_form.html'
    fields = ['name']

class CategoryDelete(LoginRequiredMixin,DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse-lazy
    success_url = reverse_lazy('category_index')

class GoalDetail(LoginRequiredMixin,DetailView):
    model = Goal
    template_name = 'goal/goal.html'

class GoalCreate(LoginRequiredMixin,CreateView):
    model = Goal
    template_name = 'goal/goal_form.html'
    # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/
    form_class = GoalForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('goal', kwargs={'pk': self.request.user.pk})

class GoalUpdate(LoginRequiredMixin,UpdateView):
    model = Goal
    template_name = 'goal/goal_form.html'
    form_class = GoalForm

    def get_success_url(self):
        return reverse_lazy('goal', kwargs={'pk': self.request.user.pk})


            