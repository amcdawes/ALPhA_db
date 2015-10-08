from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Institution

def index(request):
    institution_list = Institution.objects.order_by('name')
    context = {'institution_list': institution_list}
    return render(request, 'programs/index.html', context)

def detail(request, institution_id):
    institution = get_object_or_404(Institution, pk=institution_id)
    context = {'institution': institution}
    return render(request, 'programs/detail.html', context)
