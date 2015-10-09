from django.shortcuts import get_object_or_404, render
from django.views import generic

# Create your views here.

from .models import Institution

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
    template_name = 'programs/detail.html'

class EditView(generic.DetailView):
    model = Institution
    template_name = 'programs/edit.html'

def update(request, institution_id):
    print("update called")
