from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

from .models import Institution, Instructor
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


class DetailView(generic.DetailView):
    model = Institution
    template_name = 'programs/institution_detail.html'

class InstructorView(generic.DetailView):
    model = Instructor
    template_name = 'programs/instructor.html'

class EditView(generic.DetailView):
    model = Institution
    template_name = 'programs/edit.html'

class InstructorCreate(CreateView):
    model = Instructor
    fields = ['name','email','institution']

class InstructorUpdate(UpdateView):
    model = Instructor
    fields = ['name','email','institution']

class InstructorDelete(DeleteView):
    model = Instructor
    #success_url = reverse_lazy('detail')
    def get_success_url(self, **kwargs):
        return reverse_lazy('institution_detail', kwargs={'pk': self.get_object().institution.pk})
