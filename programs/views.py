from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

from .models import Institution, Instructor, Course
# from .forms import AddInstructorForm

# def index(request):
#     institution_list = Institution.objects.order_by('name')
#     context = {'institution_list': institution_list}
#     return render(request, 'programs/index.html', context)
#
# def detail(request, institution_id):
#     institution = get_object_or_404(Institution, pk=institution_id)
#     context = {'institution': institution}
#     return render(request, 'programs/detail.html', context)

class IndexView(generic.ListView):
    template_name = 'programs/index.html'
    context_object_name = 'institution_list'

    def get_queryset(self):
        """Return the institutions."""
        return Institution.objects.all()


class InstitutionView(generic.DetailView):
    model = Institution
    template_name = 'programs/institution_detail.html'

class InstitutionUpdate(UpdateView):
    model = Institution
    fields = ['name','state','zipcode','USNewsRank']



class CourseView(generic.DetailView):
    model = Course
    template_name = 'programs/course.html'

class CourseCreate(CreateView):
    model = Course
    fields = ['name','level']
    def my_institution(self, **kwargs):
        return Institution.objects.get(pk=self.kwargs['instid'])

    def get_context_data(self, **kwargs):
        context = super(CourseCreate, self).get_context_data(**kwargs)
        context['institution'] = self.my_institution()
        return context

    def form_valid(self, form):
        form.instance.institution = self.my_institution()
        return super(CourseCreate, self).form_valid(form)

class CourseUpdate(UpdateView):
    model = Course
    fields = ['name','level','institution']

class CourseDelete(DeleteView):
    model = Course
    def get_success_url(self, **kwargs):
        return reverse_lazy('institution_detail', kwargs={'pk': self.get_object().institution.pk})



class InstructorView(generic.DetailView):
    model = Instructor
    template_name = 'programs/instructor.html'

class InstructorCreate(CreateView):
    model = Instructor
    fields = ['name','email','courses']
    # fields['courses'].queryset = Course.objects.filter(institution__id=kwargs['instid'])
    def get_form(self, form_class):
        form = super(InstructorCreate,self).get_form(form_class)
        form.fields['courses'].queryset = Course.objects.filter(institution__id=self.kwargs['instid'])
        return form

    def my_institution(self, **kwargs):
        return Institution.objects.get(pk=self.kwargs['instid'])

    def get_context_data(self, **kwargs):
        context = super(InstructorCreate, self).get_context_data(**kwargs)
        context['institution'] = self.my_institution()
        return context

    def form_valid(self, form):
        form.instance.institution = self.my_institution()
        return super(InstructorCreate, self).form_valid(form)

class InstructorUpdate(UpdateView):
    model = Instructor
    fields = ['name','email','courses','institution']
    def get_form(self, form_class):
        form = super(InstructorUpdate,self).get_form(form_class)
        form.fields['courses'].queryset = Course.objects.filter(institution = self.get_object().institution)
        return form
    template_name_suffix = "_update_form"

class InstructorDelete(DeleteView):
    model = Instructor
    #success_url = reverse_lazy('detail')
    def get_success_url(self, **kwargs):
        return reverse_lazy('institution_detail', kwargs={'pk': self.get_object().institution.pk})
