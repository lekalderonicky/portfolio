from django.shortcuts import render, get_object_or_404
from .models import Project


def index(request):
	projects = Project.objects.order_by('-created_at')[:10]
	# fallback to static list if no DB entries
	if not projects:
		projects = [
			{'title': 'Project One', 'description': 'A short description of project one.'},
			{'title': 'Project Two', 'description': 'A short description of project two.'},
			{'title': 'Project Three', 'description': 'A short description of project three.'},
		]
	return render(request, 'portfolio/index.html', {'projects': projects})


def project_list(request):
	projects = Project.objects.order_by('-created_at')
	return render(request, 'portfolio/project_list.html', {'projects': projects})


def project_detail(request, pk):
	project = get_object_or_404(Project, pk=pk)
	return render(request, 'portfolio/project_detail.html', {'project': project})


def about(request):
	return render(request, 'portfolio/about.html')


def contact(request):
	return render(request, 'portfolio/contact.html')
