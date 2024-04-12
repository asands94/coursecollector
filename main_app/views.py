from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Course, Category, Profile, User, Note
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm, NoteForm
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'home.html', {'courses':courses})

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
    paginate_by = 5
    model = Course
    template_name = 'course/course_list.html'

    def get_queryset(self):
        category_filtered_queryset = self.category_query(self.request)
        return category_filtered_queryset.filter(user=self.request.user)
    
     # pass in categories to template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(user=self.request.user)
        context['categories'] = categories
        return context
    
    def category_query(self, request):
        q = request.GET.get('q')
        if q:
            # find the category by name
            category_obj = get_object_or_404(Category, name=q)
            return Course.objects.filter(category=category_obj.pk)
        else:
            return Course.objects.all()

class CourseDetail(LoginRequiredMixin,DetailView):
    model = Course
    template_name = 'course/course_detail.html'
    
    # redirect user to course index if trying to view a course they didn't make
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user != self.request.user:
            return redirect('course_index')
        
        return super().dispatch(request, *args, **kwargs)

    # make sure NoteForm is passed to the view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note_form'] = NoteForm()
        return context

    def post(self, request, *args, **kwargs):
        course = self.get_object()  
        form = NoteForm(request.POST) 

        if form.is_valid():
            note_text = form.cleaned_data['content']
            date_text = form.cleaned_data['date']
            Note.objects.create(courses=course, content=note_text, date=date_text)
        return redirect('course_detail', pk=course.pk)

class CourseCreate(LoginRequiredMixin,CreateView):
    model = Course
    template_name = 'course/course_form.html'
    fields = ['image', 'name', 'url', 'description', 'price', 'recurring_fee', 'rating', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CourseUpdate(LoginRequiredMixin,UpdateView):
    model = Course
    template_name = 'course/course_form.html'
    fields = ['image', 'name', 'url', 'description', 'price', 'recurring_fee', 'rating', 'category']

class CourseDelete(LoginRequiredMixin,DeleteView):
    model = Course
    template_name = 'course/course_confirm_delete.html'
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse-lazy
    success_url = reverse_lazy('course_index')

class CategoryList(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'category/category_list.html'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

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

class NoteUpdate(LoginRequiredMixin,UpdateView):
    model = Note
    template_name = 'note/note_form.html'
    fields = ['content', 'date']

class NoteDelete(LoginRequiredMixin,DeleteView):
    model = Note
    template_name = 'note/note_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.courses.pk})

class ProfileDetail(LoginRequiredMixin,ListView):
    model = User
    template_name = 'profile/profile.html'

class ProfileCreate(LoginRequiredMixin,CreateView):
    model = Profile
    template_name = 'profile/profile_form.html'
    # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/
    form_class = ProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile')

class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = 'profile/profile_form.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('profile')

class UsernameUpdate(LoginRequiredMixin,UpdateView):
    model = User
    template_name='profile/change_username.html'
    fields = ['username']

    def get_success_url(self):
        return reverse_lazy('profile')
    
class ProfileDelete(LoginRequiredMixin,DeleteView):
    model = User
    template_name = 'profile/profile_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('home')