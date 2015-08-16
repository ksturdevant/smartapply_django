from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Application
from django.shortcuts import get_object_or_404, render

# 
def index(request):
    application_list = Application.objects.order_by('-created_date')[:5]
    context = {'application_list': application_list}
    return render(request, 'applications/index.html', context)

#not working
def detail(request, application_id):
#	application = get_object_or_404(Application, pk=application_id)
#	return render(request, 'applications/detail.html', {'application': application})
	try:
		application = Application.objects.get(pk=application_id)
	except Application.DoesNotExist:
		raise Http404("Application does not exist")
	return render(request, 'applications/detail.html', {'application': application})
